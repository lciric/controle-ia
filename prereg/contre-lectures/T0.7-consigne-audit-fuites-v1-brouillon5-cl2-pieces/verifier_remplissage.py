import hashlib,re
def h(s): return hashlib.sha256(s.encode() if isinstance(s,str) else s).hexdigest()
def lignes(p): return open(p,encoding="utf-8").read().split("\n")
SC=lignes("prereg/T0.7-sondes-v0-v1.md"); B21=lignes("brouillons/T0.7-sondes-v0-v1-brouillon21.md"); B22=lignes("brouillons/T0.7-sondes-v0-v1-brouillon22.md")
B5=open("brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon5.md",encoding="utf-8").read()
def cle(L,k):
    r=[(i+1,l) for i,l in enumerate(L) if l.startswith("| `"+k+"` ")]
    assert len(r)==1,(k,len(r)); return r[0]
def cellules(l):
    assert l.startswith("| ") and l.endswith(" |")
    c=re.split(r"(?<!\\) \| ",l[2:-2]); return c
res={}
for nom,L in (("scellé",SC),("b22",B22),("b21",B21)):
    for k in ("AUDIT-FUITES-T07","CONSIGNE-AUDIT-FUITES-T07"):
        n,l=cle(L,k); c=cellules(l); res[(nom,k)]=(n,l,c)
        print(nom,k,"l.",n,"cellules:",len(c),"sha ligne",h(l),"sha c2",h(c[1]))
# comptes sans ancrage
for nom,L in (("scellé",SC),):
    for k in ("AUDIT-FUITES-T07","CONSIGNE-AUDIT-FUITES-T07"):
        print("  occurrences début de ligne '| `%s`'"%k, sum(1 for l in L if l.startswith("| `"+k+"`")))
a=res[("scellé","AUDIT-FUITES-T07")]; b=res[("b22","AUDIT-FUITES-T07")]; o=res[("b21","AUDIT-FUITES-T07")]
print("ligne scellé == b22 :",a[1]==b[1])
print("cellules 1,3,4 scellé == b21 :",a[2][0]==o[2][0],a[2][2]==o[2][2],a[2][3]==o[2][3])
# recopie dans le brouillon 5
print("c2 scellé citée dans b5 ('> '+c2) :",B5.count("> "+a[2][1]+"\n"))
print("c3 — c4 citées :",B5.count("> "+a[2][2]+" — "+a[2][3]+"\n"))
for x in ("381a72d5b52c1534d116c81b71568dd4728d1a4d90a22a25e99109508e30fede","53eca69ef2cd0c777d16f8ad64f380ecaa62381fa21ea05a728ba92c55ce6051"):
    print("empreinte",x[:8],"dans b5 :",B5.count(x), "| égale c2:",x==h(a[2][1]),"| égale ligne:",x==h(a[1]))
c=res[("scellé","CONSIGNE-AUDIT-FUITES-T07")]; c21=res[("b21","CONSIGNE-AUDIT-FUITES-T07")]
print("CONSIGNE ligne scellé == b21 :",c[1]==c21[1],"; c2 citée dans b5 :",B5.count("> "+c[2][1]+"\n"),"; c3—c4 :",B5.count("> "+c[2][2]+" — "+c[2][3]+"\n"),"; sha c2 == 95c8b659… :",h(c[2][1])=="95c8b659c54f218a903e1d0359a5a4a9ca9bd2e81072741803861a4bb4fa1121")
# annexe B = cellule 2 du b21
print("annexe B : c2 b21 citée dans b5 :",B5.count("> "+o[2][1]+"\n"))
# couples du § 2.1
sec=B5[B5.index("### 2.1 "):B5.index("### 2.2 ")]
cp=re.findall(r"Couple (\d) \(.*?\) — ancien :\n\n> (.*?)\n\nnouveau :\n\n> (.*?)\n\n",sec,flags=re.S)
t=o[2][1]
for n,an,no in cp:
    print("couple",n,"ancien présent dans c2 b21 :",t.count(an)); t=t.replace(an,no)
print("couples appliqués à c2 b21 == c2 scellé :",t==a[2][1], len(cp))
