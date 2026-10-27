"""Coleta do corpus da Etapa 2: programas de governo das candidaturas à Presidência (2026).

Fontes (dados abertos do TSE, conjunto "Candidatos - 2026"):
- proposta_governo_2026_BR.zip: programas das candidaturas de âmbito nacional;
- consulta_cand_2026.zip: cadastro de candidaturas (partido, coligação, resultado por turno);
- consulta_cand_complementar_2026.zip: situação do julgamento do registro e substituições.
  No cadastro principal, DS_SITUACAO_CANDIDATURA vem como "#NE" para todas as candidaturas
  à Presidência; por isso a situação do registro é lida do arquivo complementar.

Os zips são tratados como dados não confiáveis: são lidos com zipfile, sem extrair
para caminhos arbitrários e sem executar nada de dentro deles. Para cada arquivo
baixado e cada PDF extraído grava-se o hash SHA-256.

Saídas:
- etapa2/corpus/pdf/        PDFs dos programas (nome = SQ_CANDIDATO ou nome original)
- etapa2/corpus/txt/        texto extraído com pdftotext, com marcador de página
- etapa2/corpus/manifesto.json  URLs, datas, hashes, candidaturas e situação do registro

Uso: python3 etapa2/scripts/coleta_corpus.py
"""

import csv
import hashlib
import io
import json
import re
import subprocess
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

URL_PROPOSTAS = "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_BR.zip"
URL_CANDIDATOS = "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2026.zip"
URL_COMPLEMENTAR = "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand_complementar/consulta_cand_complementar_2026.zip"
CAMPOS_COMPLEMENTAR = ("DS_SITUACAO_JULGAMENTO", "DS_SITUACAO_CANDIDATO_TOT", "ST_SUBSTITUIDO", "SQ_SUBSTITUIDO")
RAIZ = Path(__file__).resolve().parents[1] / "corpus"


def baixar(url):
    momento = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with urllib.request.urlopen(url, timeout=600) as r:
        corpo = r.read()
        modificado = r.headers.get("Last-Modified")
    return {"url": url, "baixado_em_utc": momento, "last_modified": modificado,
            "tamanho_bytes": len(corpo), "sha256": hashlib.sha256(corpo).hexdigest()}, corpo


def ler_csv_br(zip_bytes):
    """Linhas do CSV nacional (sufixo _BR) de um zip do TSE."""
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        nome = next(n for n in z.namelist() if n.upper().endswith("_BR.CSV"))
        return list(csv.DictReader(io.StringIO(z.read(nome).decode("latin-1")), delimiter=";"))


def candidaturas_presidente(zip_cand, zip_comp):
    """Uma entrada por SQ_CANDIDATO com cargo Presidente, com o resultado de cada turno
    (o cadastro traz uma linha por turno) e a situação do registro do arquivo complementar."""
    comp = {}
    for linha in ler_csv_br(zip_comp):
        comp.setdefault(linha["SQ_CANDIDATO"], {k: linha.get(k) for k in CAMPOS_COMPLEMENTAR})
    por_sq = {}
    for linha in ler_csv_br(zip_cand):
        if linha.get("DS_CARGO", "").strip().upper() != "PRESIDENTE":
            continue
        c = por_sq.setdefault(linha["SQ_CANDIDATO"], {k: linha.get(k) for k in (
            "NM_URNA_CANDIDATO", "NM_CANDIDATO", "NR_CANDIDATO", "SG_PARTIDO", "NM_COLIGACAO",
            "DS_COMPOSICAO_COLIGACAO", "SG_FEDERACAO")} | {"resultado_por_turno": {}})
        c["resultado_por_turno"][linha["NR_TURNO"]] = linha.get("DS_SIT_TOT_TURNO")
        c.update(comp.get(linha["SQ_CANDIDATO"], {}))
    return por_sq


def extrair_texto(pdf, txt):
    paginas = int(re.search(r"Pages:\s+(\d+)", subprocess.run(
        ["pdfinfo", str(pdf)], capture_output=True, text=True).stdout or "Pages: 0").group(1))
    partes = []
    for p in range(1, paginas + 1):
        r = subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), str(pdf), "-"],
                           capture_output=True, text=True)
        partes.append(f"\n===== PÁGINA {p} =====\n{r.stdout}")
    txt.write_text("".join(partes), encoding="utf-8")
    return paginas, sum(len(x) for x in partes)


def main():
    (RAIZ / "pdf").mkdir(parents=True, exist_ok=True)
    (RAIZ / "txt").mkdir(parents=True, exist_ok=True)
    meta_prop, zip_prop = baixar(URL_PROPOSTAS)
    meta_cand, zip_cand = baixar(URL_CANDIDATOS)
    meta_comp, zip_comp = baixar(URL_COMPLEMENTAR)
    por_sq = candidaturas_presidente(zip_cand, zip_comp)

    programas = []
    with zipfile.ZipFile(io.BytesIO(zip_prop)) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            nome_original = info.filename
            base = Path(nome_original).name  # descarta qualquer diretório do nome no zip
            corpo = z.read(info)
            sq = re.search(r"(\d{9,})", base)
            sq = sq.group(1) if sq else None
            item = {"arquivo_no_zip": nome_original, "tamanho_bytes": len(corpo),
                    "sha256": hashlib.sha256(corpo).hexdigest(), "sq_candidato": sq}
            if base.lower().endswith(".pdf"):
                destino = RAIZ / "pdf" / base
                destino.write_bytes(corpo)
                paginas, chars = extrair_texto(destino, RAIZ / "txt" / (destino.stem + ".txt"))
                item.update({"pdf": str(destino.relative_to(RAIZ)), "paginas": paginas, "caracteres_texto": chars})
            if sq in por_sq:
                item["candidatura"] = por_sq[sq]
            programas.append(item)

    sq_com_programa = {p["sq_candidato"] for p in programas}
    manifesto = {
        "gerado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fonte_propostas": meta_prop,
        "fonte_cadastro": meta_cand,
        "fonte_complementar": meta_comp,
        "n_arquivos_no_zip_propostas": len(programas),
        "n_candidaturas_presidente_no_cadastro": len(por_sq),
        "programas": programas,
        "candidaturas_sem_programa_no_zip": [
            {"sq_candidato": sq, **c} for sq, c in por_sq.items() if sq not in sq_com_programa],
        "programas_sem_candidatura_presidente": [p["arquivo_no_zip"] for p in programas if "candidatura" not in p],
    }
    (RAIZ / "manifesto.json").write_text(json.dumps(manifesto, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in manifesto.items() if k != "programas"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
