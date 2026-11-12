import json,re,sys,difflib,hashlib
from pathlib import Path
B=Path("/home/user/controle-ia-travail/brouillons/accumulation-barreau6-v1")
rd=lambda n:(B/n).read_text(encoding="utf-8")
c2,c3,c4,c5=[rd(f"accumulation-barreau6-v1-candidat{i}.md") for i in (2,3,4,5)]
GEL=("Hypothèse","Prédiction chiffrée et signe attendu","Métrique","Seuil","Plan d'analyse","Critères de lecture gelés","Liste d'arrêt")
T=re.compile(r"^## +(.+?)\s*$",re.M)
def sec(t):
    m=list(T.finditer(t)); out=[("(en-tête)",t[:m[0].start()])]
    for i,x in enumerate(m): out.append((x.group(1).strip(),t[x.start():m[i+1].start() if i+1<len(m) else len(t)]))
    return out
s2,s5=sec(c2),sec(c5)
print("titres égaux:",[n for n,_ in s2]==[n for n,_ in s5]); print([n for n,_ in s5])
k3=json.loads(rd("accumulation-barreau6-v1-candidat3-couples-v1.json"))
k4=json.loads(rd("accumulation-barreau6-v1-candidat4-pieces/accumulation-barreau6-v1-candidat4-couples-v1.json"))
k5=json.loads(rd("accumulation-barreau6-v1-candidat5-pieces/accumulation-barreau6-v1-candidat5-couples-v1.json"))
print("clés k3:",list(k3.keys()),list(k3["couples"][0].keys())); print("clés k5:",list(k5.keys()),list(k5["couples"][0].keys()))
# sections réelles des couples C3
d2=dict(s2)
gel=[]
t=c2
for c in k3["couples"]:
    dans=[n for n,x in sec(t) if c["ancien"] in x]; assert len(dans)==1 and t.count(c["ancien"])==1,(c["id"],dans)
    if dans[0] in GEL: gel.append((c["id"],dans[0],c))
    t=t.replace(c["ancien"],c["nouveau"])
assert t==c3
print("C3 gelés:",[(a,b) for a,b,_ in gel])
for kk,src,dst,key in ((k4,c3,c4,"g4"),(k5,c4,c5,"g5")):
    t=src
    for c in kk["couples"]:
        dans=[n for n,x in sec(t) if c["ancien"] in x]; assert len(dans)==1 and t.count(c["ancien"])==1,(c["id"],dans)
        assert (dans[0] in GEL)==bool(c["gelee"])
        if dans[0] in GEL: gel.append((c.get(key) or c["id"],dans[0],c))
        t=t.replace(c["ancien"],c["nouveau"])
    assert t==dst
print(len(gel),"couples gelés au total")
# appliquer uniquement les gelés à c2 : sections gelées == celles de c5 ?
t=c2
for _,_,c in gel:
    assert t.count(c["ancien"])==1,c["id"]; t=t.replace(c["ancien"],c["nouveau"])
st=dict(sec(t)); d5=dict(s5)
for n in GEL: print(n, "gelée c2+23 couples == c5 :", st[n]==d5[n], "| changée depuis c2 :", d2[n]!=d5[n], len(d2[n]),len(d5[n]))
json.dump([{"g":a,"section":b,"id":c["id"],"ancien":c["ancien"],"nouveau":c["nouveau"],**{k:v for k,v in c.items() if k not in("ancien","nouveau","id")}} for a,b,c in gel],open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
# mots sensibles supprimés/ajoutés, section par section, entre c2 et c5
MOT=re.compile(r"\w+(?:[.,/]\w+)*|[^\w\s]")
sens=lambda m:any(ch.isdigit() for ch in m) or m in {"<",">","≤","≥","=","≠","+","−","%","→","-"} or m.startswith("strict")
for n in GEL:
    a,b=MOT.findall(d2[n]),MOT.findall(d5[n])
    sm=difflib.SequenceMatcher(a=a,b=b,autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op in("replace","delete"):
            print(f"  [{n}] {op}: «{' '.join(a[i1:i2])[:300]}» → «{' '.join(b[j1:j2])[:200]}»")
