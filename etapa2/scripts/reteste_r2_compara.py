import json, re, sys
from collections import Counter
k = json.load(open(sys.argv[1], encoding="utf-8"))
r = [l.strip() for l in open(sys.argv[2], encoding="utf-8") if l.strip()]
assert len(k)==len(r)
def base(c): return re.match(r"(SEG|IMP|SAU|T\d+[-A-Z]*|E-[A-Z]+)(\.[A-Z]+)?", c).group(0)
ag=0; p1=Counter(); p2=Counter(); dis=[]
for x,y in zip(k,r):
    a=base(x["codigo"]); p1[a]+=1; p2[y]+=1
    if a==y: ag+=1
    else: dis.append((x["R"],x["unidade"],x["codigo"],y,x["pag"],x["secao"]))
n=len(k); po=ag/n
pe=sum(p1[c]*p2[c] for c in set(p1)|set(p2))/n/n
print(f"n={n} acordo={ag} po={po:.3f} pe={pe:.3f} kappa={(po-pe)/(1-pe):.3f}")
for d in dis: print(" | ".join(d))
ag3=sum(1 for x,y in zip(k,r) if base(x["codigo"])[:3]==y[:3]); print("acordo no tema principal", ag3)
for x,y in zip(k,r): print(x["R"], x["unidade"], x["codigo"], "->", y)
