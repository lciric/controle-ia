import json,hashlib,sys,re
D="brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-"
def h(b): return hashlib.sha256(b).hexdigest()
def lire(p): return open(p,"rb").read()
def jouer(src,dst,fc):
    j=json.load(open(fc,encoding="utf-8"))
    a=lire(src); b=lire(dst)
    assert h(a)==j["de"]["sha256"] and h(b)==j["vers"]["sha256"],"empreintes de/vers"
    t=a.decode("utf-8")
    for c in j["couples"]:
        n=t.count(c["ancien"])
        assert n==1,(c["id"],"ancien",n)
        assert c["ancien"]!=c["nouveau"]
        t=t.replace(c["ancien"],c["nouveau"])
    print(fc.split("/")[-1],": aller", "EGAL" if t.encode()==b else "DIFFERENT", h(t.encode()))
    u=b.decode()
    for c in reversed(j["couples"]):
        n=u.count(c["nouveau"])
        assert n==1,(c["id"],"nouveau",n)
        u=u.replace(c["nouveau"],c["ancien"])
    print("  retour", "EGAL" if u.encode()==a else "DIFFERENT", h(u.encode()))
    # unicité statique
    for c in j["couples"]:
        na=a.decode().count(c["ancien"]); nb=b.decode().count(c["nouveau"])
        if na!=1 or nb!=1: print("  note",c["id"],"ancien dans source:",na,"nouveau dans cible:",nb)
    print("  marqueurs cible:",sorted(set(re.findall(r"<<[A-Z0-9_]+>>",b.decode()))),[b.decode().count(m) for m in sorted(set(re.findall(r"<<[A-Z0-9_]+>>",b.decode())))])
    print("  marqueurs source:",{m:a.decode().count(m) for m in sorted(set(re.findall(r"<<[A-Z0-9_]+>>",a.decode())))})
    return j
j4=jouer(D+"brouillon3.md",D+"brouillon4.md",D+"brouillon4-pieces/couples-brouillon3-vers-brouillon4-v1.json")
j5=jouer(D+"brouillon4.md",D+"brouillon5.md",D+"brouillon5-pieces/couples-brouillon4-vers-brouillon5-v1.json")
for j in (j4,j5):
    for c in j["couples"]: print(c["id"],"|",c["motif"][:150],"|",len(c["ancien"]),"->",len(c["nouveau"]))
print("en_attente:",json.dumps(j4["en_attente"],ensure_ascii=False,indent=1))
print("decoupeur:",json.dumps(j5["decoupeur"],ensure_ascii=False,indent=1))
