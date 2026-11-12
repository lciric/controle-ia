import json, sys, importlib.util, difflib
D, R = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("app", f"{R}/appliquer_couples_brouillon4_v1.py")
app = importlib.util.module_from_spec(spec); spec.loader.exec_module(app)
b3 = open(f"{D}/preenregistrement-epreuve-etiqueteur-v1-brouillon3.md", encoding="utf-8").read()
b4 = open(f"{D}/preenregistrement-epreuve-etiqueteur-v1-brouillon4.md", encoding="utf-8").read()
couples = json.load(open(f"{D}/couples-contre-lecture-epreuve-etiqueteur-brouillon3-v1.json", encoding="utf-8"))
t, _ = app.appliquer_couples(b3, couples)
comps = app.complements("23:12:13", t)
for c in couples:
    if b4.count(c["nouveau"]) == c["n"]:
        continue
    touches = []
    for k in comps:
        a = k["ancien"]
        # recouvrement : ancien du complément contenu dans le nouveau du couple, ou chevauchement partiel
        if a in c["nouveau"] or c["nouveau"] in a:
            touches.append((k["id"], "inclus" if a in c["nouveau"] else "englobe"))
        else:
            # chevauchement partiel dans le texte après couples
            i = t.find(c["nouveau"]); j = t.find(a)
            if i >= 0 and j >= 0 and j < i + len(c["nouveau"]) and i < j + len(a):
                touches.append((k["id"], "chevauche"))
    print("=====", c["id"], touches)
    x = c["nouveau"]
    for k in comps:
        if k["ancien"] in x:
            x = x.replace(k["ancien"], k["nouveau"])
    print("   après compléments, présent dans b4 :", b4.count(x))
    if b4.count(x) == 0 or True:
        for k in comps:
            if (k["id"], "inclus") in touches or (k["id"], "englobe") in touches or (k["id"], "chevauche") in touches:
                print("   ", k["id"], "motif:", k["motif"])
                if k["ancien"] in c["nouveau"]:
                    print("      ancien :", k["ancien"][:300].replace("\n"," / "))
                    print("      nouveau:", k["nouveau"][:600].replace("\n"," / "))
