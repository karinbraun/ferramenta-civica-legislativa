"""Gera a tabela de incidência tema x programa (Polo 2) a partir dos arquivos de codificação.

Uso: python3 -I etapa2/scripts/incidencia_polo2.py etapa2/codificacao/programas
Lê só os arquivos .md de codificação; não acessa a rede.
"""
import re, sys, json, pathlib
from collections import OrderedDict

base = pathlib.Path(sys.argv[1])
ORDEM = ["rui-costa-pimenta", "clariana-barao", "edmilson-costa", "pablo-marcal", "hertz-dias",
         "wilson-grassi", "renan-santos", "zema", "samara", "leonardo-avalanche",
         "flavio-bolsonaro", "lula", "augusto-cury", "ronaldo-caiado"]
SIGLA = {"rui-costa-pimenta": "PCO", "clariana-barao": "DC", "edmilson-costa": "PCB", "pablo-marcal": "Marçal",
         "hertz-dias": "PSTU", "wilson-grassi": "DEM", "renan-santos": "MISSÃO", "zema": "NOVO", "samara": "UP",
         "leonardo-avalanche": "Avalanche", "flavio-bolsonaro": "PL", "lula": "PT", "augusto-cury": "AVANTE",
         "ronaldo-caiado": "PSD"}
res = OrderedDict()
for chave in ORDEM:
    f = next(base.glob(f"*{chave}*.md"))
    txt = f.read_text(encoding="utf-8")
    pres = {}
    for m in re.finditer(r"^\| ((?:SEG|IMP|SAU|T\d+[-A-Z]*|E-[A-Z]+)) \| (\*\*)?(Sim|Não)(?: \([^)]*\))?(\*\*)? \|", txt, re.M):
        pres[m[1]] = m[3] == "Sim"
    uni = {"SEG": [0, 0, 0], "IMP": [0, 0, 0], "SAU": [0, 0, 0]}  # proposta, diagnóstico, balanço
    for m in re.finditer(r"^\| [A-Z]{2,3}-[SIH]\d+ \|.*\| ([^|]+) \|$", txt, re.M):
        cod = m[1].strip()
        t = re.match(r"(SEG|IMP|SAU)\.", cod)
        if not t:
            continue
        i = 2 if "[balanço]" in cod else (1 if ".DIAG" in cod else 0)
        uni[t[1]][i] += 1
    res[SIGLA[chave]] = {"presenca": pres, "unidades": uni}
json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
