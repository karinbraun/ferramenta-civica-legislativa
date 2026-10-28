import re, random, json, sys, pathlib
base = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
excl = ("pco","barao","edmilson")
rows = []
for f in sorted(base.glob("*.md")):
    if any(e in f.name.lower() for e in excl): continue
    for line in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| ([A-Z]{3}-[SIH]\d+) \| ([^|]*) \| ([^|]*) \| (.*) \| ([^|]*) \|$", line)
        if m:
            rows.append(dict(unidade=m[1], pag=m[2].strip(), secao=m[3].strip(), trecho=m[4].strip(), codigo=m[5].strip(), arquivo=f.name))
n = len(rows); k = round(n*0.10)
random.seed(2026)
amostra = random.sample(rows, k)
from collections import Counter
print("universo", n, "amostra", k)
print(Counter(r["unidade"][:3] for r in rows))
(out/"r2_chave.json").write_text(json.dumps([dict(R=f"R{i+1}", **r) for i,r in enumerate(amostra)], ensure_ascii=False, indent=1), encoding="utf-8")
with open(out/"r2_cego.md","w",encoding="utf-8") as fh:
    for i,r in enumerate(amostra):
        fh.write(f"R{i+1}: {r['trecho']}\n\n")
