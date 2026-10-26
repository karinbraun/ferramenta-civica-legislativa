"""Sondagem da API de Dados Abertos da Câmara dos Deputados (Etapa 1).

Somente leitura. Cada resposta é salva em etapa1/amostras/camara/ junto com
a URL requisitada e a data/hora da requisição, para rastreabilidade.
Ao final, grava etapa1/amostras/camara/_resumo.json com as contagens usadas
no relatório de cobertura.

Uso: python3 etapa1/scripts/sondagem_camara.py
"""

import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://dadosabertos.camara.leg.br/api/v2"
SAIDA = Path(__file__).resolve().parents[1] / "amostras" / "camara"
PAUSA = 0.3  # segundos entre requisições, para não sobrecarregar a API

# Temas do protótipo -> parâmetros de busca na API (hipótese a validar).
# "Impostos e custo de vida" não existe como tema oficial; testamos os temas
# Economia (40) e Finanças Públicas e Orçamento (70) combinados com palavra-chave.
TEMAS_PROTOTIPO = {
    "saude": [{"codTema": 56}],
    "seguranca": [{"codTema": 57}, {"codTema": 43}],
    "impostos": [{"codTema": 40, "keywords": "tributo"}, {"codTema": 70, "keywords": "imposto"}],
}
AMOSTRAS_POR_TEMA = 5
INICIO_LEGISLATURA = "2023-02-01"

# Mês de referência para a amostra de votações do Plenário.
VOTACOES_INICIO, VOTACOES_FIM = "2025-11-01", "2025-11-30"
# Votações antigas usadas para testar se o partido do voto é o da época.
VOTACOES_ANTIGAS = ("2019-07-01", "2019-07-15")


def slug(texto):
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", texto).strip("_")[:150]


def get(caminho, params=None, nome=None):
    url = BASE + caminho
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    momento = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            status, corpo = r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        status, corpo = e.code, None
    time.sleep(PAUSA)
    registro = {"url": url, "requisitado_em_utc": momento, "status_http": status, "resposta": corpo}
    arquivo = SAIDA / f"{slug(nome or caminho + '_' + urllib.parse.urlencode(params or {}))}.json"
    arquivo.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    return corpo["dados"] if corpo else None


def partido_na_data(historico, data_iso):
    """Último partido registrado no histórico até a data informada."""
    anteriores = [h for h in historico if h["dataHora"] and h["dataHora"][:10] <= data_iso[:10]]
    if not anteriores:
        return None
    return max(anteriores, key=lambda h: h["dataHora"])["siglaPartido"]


def amostrar_proposicoes(resumo):
    resumo["proposicoes"] = []
    historicos = {}
    for tema, buscas in TEMAS_PROTOTIPO.items():
        candidatas = []
        for busca in buscas:
            params = {"siglaTipo": "PL", "dataApresentacaoInicio": INICIO_LEGISLATURA,
                      "ordem": "ASC", "ordenarPor": "id", "itens": 100, **busca}
            candidatas += get("/proposicoes", params, f"lista_{tema}_{slug(str(busca))}") or []
        # Escolha determinística e espaçada ao longo da lista.
        passo = max(1, len(candidatas) // AMOSTRAS_POR_TEMA)
        escolhidas = candidatas[::passo][:AMOSTRAS_POR_TEMA]
        for p in escolhidas:
            pid = p["id"]
            det = get(f"/proposicoes/{pid}", nome=f"prop_{pid}_detalhe")
            temas = get(f"/proposicoes/{pid}/temas", nome=f"prop_{pid}_temas") or []
            autores = get(f"/proposicoes/{pid}/autores", nome=f"prop_{pid}_autores") or []
            tram = get(f"/proposicoes/{pid}/tramitacoes", nome=f"prop_{pid}_tramitacoes") or []
            vots = get(f"/proposicoes/{pid}/votacoes", nome=f"prop_{pid}_votacoes") or []
            st = det["statusProposicao"]
            info_autores = []
            for a in autores:
                item = {"nome": a["nome"], "tipo": a["tipo"], "proponente": a["proponente"],
                        "campo_partido_no_endpoint": "siglaPartido" in a}
                if "/deputados/" in a["uri"]:
                    did = a["uri"].rsplit("/", 1)[1]
                    if did not in historicos:
                        historicos[did] = get(f"/deputados/{did}/historico", nome=f"dep_{did}_historico") or []
                    item["partido_na_data_pelo_historico"] = partido_na_data(historicos[did], det["dataApresentacao"])
                info_autores.append(item)
            resumo["proposicoes"].append({
                "tema_prototipo": tema,
                "id": pid,
                "identificacao": f"{det['siglaTipo']} {det['numero']}/{det['ano']}",
                "dataApresentacao": det["dataApresentacao"],
                "ementa": det["ementa"],
                "temas_oficiais": [(t["tema"], t["relevancia"]) for t in temas],
                "situacao": st["descricaoSituacao"],
                "regime": st["regime"],
                "apreciacao": st["apreciacao"],
                "autores": info_autores,
                "n_tramitacoes": len(tram),
                "tramitacoes_com_parecer": sum(1 for t in tram if "parecer" in (t.get("descricaoTramitacao") or "").lower()),
                "n_votacoes": len(vots),
                "url_pagina": f"https://www.camara.leg.br/propostas-legislativas/{pid}",
                "url_inteiro_teor": det["urlInteiroTeor"],
            })


def analisar_votacoes(resumo, inicio, fim, rotulo, comparar_partido=False):
    lista = get("/votacoes", {"idOrgao": 180, "dataInicio": inicio, "dataFim": fim, "itens": 100},
                f"votacoes_plen_{rotulo}") or []
    contagem = {"total": len(lista), "com_votos_individuais": 0, "com_orientacao": 0,
                "sem_votos_e_sem_orientacao": 0, "sem_votos_com_orientacao": 0}
    exemplos, divergencias_partido = [], []
    historicos = {}
    for v in lista:
        vid = v["id"]
        votos = get(f"/votacoes/{vid}/votos", nome=f"vot_{vid}_votos") or []
        ori = get(f"/votacoes/{vid}/orientacoes", nome=f"vot_{vid}_orientacoes") or []
        contagem["com_votos_individuais"] += bool(votos)
        contagem["com_orientacao"] += bool(ori)
        contagem["sem_votos_e_sem_orientacao"] += (not votos and not ori)
        contagem["sem_votos_com_orientacao"] += (not votos and bool(ori))
        if len(exemplos) < 6:
            exemplos.append({"id": vid, "descricao": v["descricao"], "n_votos": len(votos), "n_orientacoes": len(ori),
                             "tipos_lideranca": sorted({o["siglaPartidoBloco"] for o in ori})})
        if comparar_partido and votos and len(historicos) < 60:
            for voto in votos[:30]:
                dep = voto["deputado_"]
                did = str(dep["id"])
                if did not in historicos:
                    historicos[did] = get(f"/deputados/{did}/historico", nome=f"dep_{did}_historico") or []
                na_data = partido_na_data(historicos[did], v["dataHoraRegistro"])
                if na_data and na_data != dep["siglaPartido"]:
                    divergencias_partido.append({"votacao": vid, "deputado": dep["nome"],
                                                 "partido_no_voto": dep["siglaPartido"],
                                                 "partido_na_data_pelo_historico": na_data})
    resumo[f"votacoes_{rotulo}"] = {"periodo": [inicio, fim], "contagem": contagem, "exemplos": exemplos}
    if comparar_partido:
        resumo[f"votacoes_{rotulo}"]["deputados_verificados"] = len(historicos)
        resumo[f"votacoes_{rotulo}"]["divergencias_partido"] = divergencias_partido


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    resumo = {"executado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    resumo["temas_oficiais"] = get("/referencias/proposicoes/codTema", nome="ref_temas")
    resumo["situacoes_oficiais"] = get("/referencias/proposicoes/codSituacao", nome="ref_situacoes")
    resumo["regimes_oficiais"] = get("/referencias/proposicoes/codRegime", nome="ref_regimes")
    amostrar_proposicoes(resumo)
    analisar_votacoes(resumo, VOTACOES_INICIO, VOTACOES_FIM, "recentes")
    analisar_votacoes(resumo, *VOTACOES_ANTIGAS, "2019", comparar_partido=True)
    (SAIDA / "_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Resumo gravado em {SAIDA / '_resumo.json'}")


if __name__ == "__main__":
    main()
