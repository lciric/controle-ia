import re
B5=open("brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon5.md",encoding="utf-8").read()
sec=B5[B5.index("### 2.3 "):B5.index("## 3. Qui exécute")]
for nom,p in (("scellé","prereg/T0.7-sondes-v0-v1.md"),("b21","brouillons/T0.7-sondes-v0-v1-brouillon21.md")):
    T=open(p,encoding="utf-8").read(); L=T.split("\n")
    blocs=re.findall(r"\n\n((?:>.*\n)+)",sec)
    tit=re.findall(r"\n\n([^>\n][^\n]*\(l\. [^\n]*:)\n\n>",sec)
    for t,b in zip(tit,blocs):
        txt="\n".join(x[2:] if x.startswith("> ") else x[1:] for x in b.rstrip("\n").split("\n"))
        n=T.count(txt)
        i=T.find(txt); deb=T[:i].count("\n")+1; fin=deb+txt.count("\n")
        entier=(i==0 or T[i-1]=="\n") and T[i+len(txt)]=="\n"
        print(nom,"|",t[:75],"| occurrences",n,"| lignes",deb,"-",fin,"| lignes entières",entier)
    for a,b_ in ((2442,2444),(2574,2576)):
        pass
S=open("prereg/T0.7-sondes-v0-v1.md",encoding="utf-8").read().split("\n"); B=open("brouillons/T0.7-sondes-v0-v1-brouillon21.md",encoding="utf-8").read().split("\n")
print("module l.2442-2444 b21 == l.2574-2576 scellé :",B[2441:2444]==S[2573:2576])
print("\n".join(S[2573:2576]))
