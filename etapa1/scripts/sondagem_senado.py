"""Sondagem da API de Dados Abertos do Senado Federal (Etapa 1).

Somente leitura. Usa os endpoints novos (/processo, /votacao), que substituem
os antigos (/materia/...) desativados oficialmente em 01/02/2026, segundo os
metadados de descontinuação da própria API.

Cada resposta é salva em etapa1/amostras/senado/ com a URL e a data/hora da
requisição. O resumo das contagens vai para etapa1/amostras/senado/_resumo.json.

Uso: python3 etapa1/scripts/sondagem_senado.py
"""

import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://legis.senado.leg.br/dadosabertos"
SAIDA = Path(__file__).resolve().parents[1] / "amostras" / "senado"
PAUSA = 0.3

# Temas do protótipo -> códigos de classe do Senado (/processo/classes).
# A classificação por assunto (/processo/assuntos) só cobre processos até 2021;
# o teste com ela fica registrado em ASSUNTOS_TESTE.
TEMAS_PROTOTIPO = {
    "saude": [33808942],                 # Política Social / Saúde
    "seguranca": [33809619, 33805617],   # Ordem Pública / Segurança Pública; Jurídico / Direito Penal e Penitenciário
    "impostos": [33804940],              # Economia e Desenvolvimento / Tributos
}
ASSUNTOS_TESTE = {"saude": 149, "seguranca": 135, "impostos": 117}
AMOSTRAS_POR_TEMA = 5
# A API limita a busca por data a janelas de até 1 ano.
JANELA_APRESENTACAO = ("2025-01-01", "2025-12-31")

# Períodos de votações do Plenário: um recente e um antigo (para testar o partido da época).
PERIODOS_VOTACAO = {"recentes": ("2025-11-01", "2025-11-30"), "2019": ("2019-07-01", "2019-07-31")}

TERMOS_TRAMITACAO = ("parecer", "simbólica", "nominal", "arquiv")


def slug(texto):
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", texto).strip("_")[:150]


def get(caminho, params=None, nome=None):
    url = BASE + caminho
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    momento = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            status, corpo = r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        status, corpo = e.code, None
    time.sleep(PAUSA)
    registro = {"url": url, "requisitado_em_utc": momento, "status_http": status, "resposta": corpo}
    arquivo = SAIDA / f"{slug(nome or caminho + '_' + urllib.parse.urlencode(params or {}))}.json"
    arquivo.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    return corpo


def como_lista(x):
    if x is None:
        return []
    return x if isinstance(x, list) else [x]


def filiacoes(codigo, cache):
    """Lista de (sigla, data_filiacao, data_desfiliacao) de um senador."""
    if codigo not in cache:
        corpo = get(f"/senador/{codigo}/filiacoes.json", nome=f"sen_{codigo}_filiacoes") or {}
        parl = corpo.get("FiliacaoParlamentar", {}).get("Parlamentar", {})
        cache[codigo] = [(f["Partido"]["SiglaPartido"], f.get("DataFiliacao"), f.get("DataDesfiliacao"))
                         for f in como_lista(parl.get("Filiacoes", {}).get("Filiacao"))]
    return cache[codigo]


def partido_na_data(lista, data_iso):
    data = data_iso[:10]
    for sigla, ini, fim in lista:
        if ini and ini <= data and (not fim or data <= fim):
            return sigla
    return None


def amostrar_processos(resumo, cache_fil):
    resumo["processos"] = []
    for tema, classes in TEMAS_PROTOTIPO.items():
        candidatos = []
        for cod in classes:
            params = {"sigla": "PL", "codigoClasse": cod, "dataInicioApresentacao": JANELA_APRESENTACAO[0],
                      "dataFimApresentacao": JANELA_APRESENTACAO[1]}
            candidatos += get("/processo", params, f"lista_{tema}_{cod}") or []
        # Teste da classificação antiga por assunto: anos de apresentação cobertos.
        antigos = get("/processo", {"sigla": "PL", "codAssuntoEspecifico": ASSUNTOS_TESTE[tema]},
                      f"teste_assunto_{tema}") or []
        resumo.setdefault("teste_assuntos", {})[tema] = sorted({x["dataApresentacao"][:4] for x in antigos})
        candidatos.sort(key=lambda p: p["id"])
        passo = max(1, len(candidatos) // AMOSTRAS_POR_TEMA)
        for p in candidatos[::passo][:AMOSTRAS_POR_TEMA]:
            det = get(f"/processo/{p['id']}", nome=f"proc_{p['id']}_detalhe") or {}
            doc = det.get("documento") or {}
            autores = []
            for a in det.get("autoriaIniciativa") or []:
                item = {"autor": a.get("autor"), "tipo": a.get("siglaTipo"),
                        "partido_no_registro": a.get("siglaPartido"), "uf": a.get("siglaUf") or a.get("uf")}
                if a.get("siglaTipo") == "SENADOR" and a.get("codigoParlamentar"):
                    item["partido_pelas_filiacoes"] = partido_na_data(
                        filiacoes(a["codigoParlamentar"], cache_fil), doc.get("dataApresentacao", ""))
                autores.append(item)
            informes = [i for aut in det.get("autuacoes") or [] for i in aut.get("informesLegislativos") or []]
            textos = " ".join((i.get("descricao") or "").lower() for i in informes)
            resumo["processos"].append({
                "tema_prototipo": tema,
                "id": p["id"],
                "identificacao": det.get("identificacao"),
                "dataApresentacao": doc.get("dataApresentacao"),
                "ementa": (det.get("conteudo") or {}).get("ementa"),
                "classificacoes": [c.get("descricaoHierarquia") for c in det.get("classificacoes") or []],
                "situacaoAtual": det.get("situacaoAtual"),
                "tramitando": det.get("tramitando"),
                "casa_iniciadora": det.get("siglaCasaIniciadora"),
                "processo_inicial": det.get("identificacaoProcessoInicial"),
                "autores": autores,
                "n_informes": len(informes),
                "informes_com_termo": {t: textos.count(t) for t in TERMOS_TRAMITACAO},
                "url_documento": doc.get("url"),
                "url_pagina": f"https://www25.senado.leg.br/web/atividade/materias/-/materia/{det.get('codigoMateria')}",
            })


def analisar_votacoes(resumo, rotulo, inicio, fim, cache_fil):
    votacoes = get("/votacao", {"dataInicio": inicio, "dataFim": fim}, f"votacao_{rotulo}") or []
    ori = get(f"/plenario/votacao/orientacaoBancada/{inicio.replace('-', '')}/{fim.replace('-', '')}.json",
              nome=f"orientacao_{rotulo}") or {}
    lista_ori = ori.get("votacoes", [])
    divergencias, verificados = [], 0
    for v in votacoes:
        for voto in v.get("votos", [])[:40]:
            if verificados >= 80:
                break
            atual = partido_na_data(filiacoes(voto["codigoParlamentar"], cache_fil), v["dataSessao"])
            verificados += 1
            if atual and atual != voto["siglaPartidoParlamentar"]:
                divergencias.append({"votacao": v["codigoSessaoVotacao"], "senador": voto["nomeParlamentar"],
                                     "partido_no_voto": voto["siglaPartidoParlamentar"], "partido_pelas_filiacoes": atual})
    resumo[f"votacoes_{rotulo}"] = {
        "periodo": [inicio, fim],
        "n_votacoes_nominais": len(votacoes),
        "secretas": Counter(v.get("votacaoSecreta") for v in votacoes),
        "tipos_voto": Counter(x["siglaVotoParlamentar"] for v in votacoes for x in v.get("votos", [])),
        "n_votacoes_no_endpoint_orientacao": len(lista_ori),
        "n_com_orientacao_preenchida": sum(1 for x in lista_ori if x.get("orientacoesLideranca")),
        "exemplos_orientacao": [x["orientacoesLideranca"][:6] for x in lista_ori if x.get("orientacoesLideranca")][:2],
        "votos_verificados_partido": verificados,
        "divergencias_partido": divergencias,
    }


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    cache_fil = {}
    resumo = {"executado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    resumo["assuntos"] = get("/processo/assuntos", nome="ref_assuntos")
    resumo["tipos_situacao"] = get("/processo/tipos-situacao", nome="ref_tipos_situacao")
    get("/processo/classes", nome="ref_classes")
    amostrar_processos(resumo, cache_fil)
    for rotulo, (ini, fim) in PERIODOS_VOTACAO.items():
        analisar_votacoes(resumo, rotulo, ini, fim, cache_fil)
    (SAIDA / "_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1, default=dict), encoding="utf-8")
    print(f"Resumo gravado em {SAIDA / '_resumo.json'}")


if __name__ == "__main__":
    main()
