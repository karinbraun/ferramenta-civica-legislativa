"""Sondagem das fontes de legislação federal e dos regimentos (Etapa 1).

Somente leitura. Testa:
- LexML (SRU): se aceita acesso automatizado;
- API de legislação do Senado (/legislacao): ementa, classificação temática e
  declarações estruturadas de revogação e alteração ("vides" e "disps");
- Regimentos: o que a API do Senado informa sobre alterações do RISF e do RICD,
  e a edição do PDF do RICD publicado no site da Câmara.

Respostas salvas em etapa1/amostras/legislacao/ com URL e data/hora.
O resumo vai para etapa1/amostras/legislacao/_resumo.json.

Uso: python3 etapa1/scripts/sondagem_legislacao.py
"""

import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SENADO = "https://legis.senado.leg.br/dadosabertos"
LEXML_SRU = "https://www.lexml.gov.br/busca/SRU"
RICD_PDF = "https://www.camara.leg.br/internet/legislacao/regimento_interno/RIpdf/regInterno.pdf"
SAIDA = Path(__file__).resolve().parents[1] / "amostras" / "legislacao"
PAUSA = 0.3

# Leis de teste: uma vigente e alterada, uma revogada no todo, e uma de cada tema do protótipo.
LEIS_TESTE = {
    "lei_8080_1990_saude": "lei/8080/1990",
    "lei_8666_1993_revogada": "lei/8666/1993",
    "lei_13675_2018_seguranca": "lei/13675/2018",
    "lei_12741_2012_impostos": "lei/12741/2012",
}
REGIMENTOS = {"risf": ("rsf/93/1970", ["Art. 332", "Art. 333"]), "ricd": ("rcd/17/1989", ["Art. 105"])}


def slug(texto):
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", texto).strip("_")[:150]


def baixar(url, nome, accept="application/json"):
    req = urllib.request.Request(url, headers={"Accept": accept})
    momento = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            status, tipo, corpo = r.status, r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        status, tipo, corpo = e.code, e.headers.get("Content-Type", ""), e.read()
    except urllib.error.URLError as e:
        status, tipo, corpo = None, "", str(e.reason).encode()
    time.sleep(PAUSA)
    return {"url": url, "requisitado_em_utc": momento, "status_http": status, "content_type": tipo, "corpo": corpo, "nome": nome}


def salvar_json(reg):
    try:
        resposta = json.loads(reg["corpo"].decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        resposta = reg["corpo"][:2000].decode("utf-8", "replace")
    registro = {k: reg[k] for k in ("url", "requisitado_em_utc", "status_http", "content_type")}
    registro["resposta"] = resposta
    (SAIDA / f"{slug(reg['nome'])}.json").write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    return resposta


def como_lista(x):
    if not x or isinstance(x, str):
        return []
    return x if isinstance(x, list) else [x]


def documento(resposta):
    if not isinstance(resposta, dict) or "DetalheDocumento" not in resposta:
        return None
    docs = como_lista(resposta["DetalheDocumento"].get("documentos", {}).get("documento"))
    return docs[0] if docs else None


def testar_lexml(resumo):
    params = {"operation": "searchRetrieve", "version": "1.1", "maximumRecords": 3,
              "query": 'urn="urn:lex:br:federal:lei:1990-09-19;8080"'}
    reg = baixar(LEXML_SRU + "?" + urllib.parse.urlencode(params), "lexml_sru_lei_8080", accept="application/xml")
    texto = reg["corpo"].decode("utf-8", "replace")
    salvar_json(reg)
    resumo["lexml"] = {"url": reg["url"], "status_http": reg["status_http"], "content_type": reg["content_type"],
                       "pagina_de_verificacao": "Verificação de segurança" in texto or "_challenge" in texto,
                       "resposta_sru": "searchRetrieveResponse" in texto}


def testar_leis(resumo):
    resumo["leis"] = {}
    for nome, caminho in LEIS_TESTE.items():
        doc = documento(salvar_json(baixar(f"{SENADO}/legislacao/{caminho}", nome)))
        if not doc:
            resumo["leis"][nome] = {"erro": "sem documento na resposta"}
            continue
        vides = como_lista(doc.get("vides", {}).get("vide") if isinstance(doc.get("vides"), dict) else None)
        revogacoes = [{"norma": v["nomeNormaPosterior"], "declaracao": v["comentario"], "data_assinatura": v["datAssinatura"]}
                      for v in vides if "Revoga" in v["comentario"]]
        resumo["leis"][nome] = {
            "norma": doc["identificacao"]["normaNome"],
            "apelido": doc["identificacao"].get("apelido"),
            "url_documento": doc["identificacao"].get("urlDocumento"),
            "ementa": doc.get("ementa"),
            "classes": doc.get("classes"),
            "observacao": doc.get("observacao"),
            "n_vides": len(vides),
            "tipos_declaracao": Counter(v["comentario"] for v in vides).most_common(),
            "revogacoes_no_todo": revogacoes,
        }
    lista = salvar_json(baixar(f"{SENADO}/legislacao/lista?tipo=LEI&ano=2023", "lista_leis_2023"))
    docs = como_lista(lista.get("ListaDocumento", {}).get("documentos", {}).get("documento")) if isinstance(lista, dict) else []
    resumo["lista_leis_2023"] = {"n": len(docs), "campos": sorted(docs[0].keys()) if docs else []}


def testar_regimentos(resumo):
    resumo["regimentos"] = {}
    for nome, (caminho, artigos) in REGIMENTOS.items():
        doc = documento(salvar_json(baixar(f"{SENADO}/legislacao/{caminho}", f"regimento_{nome}")))
        disps = como_lista(doc.get("disps", {}).get("disp") if doc and isinstance(doc.get("disps"), dict) else None)
        alteracoes = {}
        for art in artigos:
            for d in disps:
                n = d["nomeDispositivo"]
                if n.startswith(art) and (len(n) == len(art) or not n[len(art)].isdigit()):
                    for r in como_lista(d["refs"]["ref"]):
                        alteracoes.setdefault(art, []).append({"dispositivo": n, "norma": r["dispositivo"], "declaracao": r["comentario"]})
        resumo["regimentos"][nome] = {
            "norma": doc["identificacao"]["normaNome"] if doc else None,
            "url_documento": doc["identificacao"].get("urlDocumento") if doc else None,
            "n_dispositivos_com_referencias": len(disps),
            "alteracoes_artigos_alvo": alteracoes,
        }
    reg = baixar(RICD_PDF, "ricd_pdf", accept="application/pdf")
    titulo = re.search(rb"/Title\s*\((.*?)\)", reg["corpo"])
    resumo["ricd_pdf_camara"] = {"url": RICD_PDF, "status_http": reg["status_http"], "content_type": reg["content_type"],
                                 "tamanho_bytes": len(reg["corpo"]),
                                 "titulo_metadado": titulo.group(1).decode("latin-1") if titulo else None}


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    resumo = {"executado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    testar_lexml(resumo)
    testar_leis(resumo)
    testar_regimentos(resumo)
    (SAIDA / "_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in resumo.items() if k != "leis"}, ensure_ascii=False, indent=1)[:4000])
    for nome, info in resumo["leis"].items():
        print(nome, info.get("norma"), info.get("classes"), info.get("tipos_declaracao"), info.get("revogacoes_no_todo"))


if __name__ == "__main__":
    main()
