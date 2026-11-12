"""Compare, section par section, le préenregistrement v11 et le v12 (R1 : la science ne doit pas bouger).
Les sections sont découpées sur les titres de niveau 2 (« ## »). Pour chaque section, on dit si elle est identique au bit
près ; sinon on imprime un diff unifié. Usage : python -I -B sections_v11_v12_v1.py V11.md V12.md"""
import difflib, hashlib, sys

def sections(path):
    txt = open(path, encoding="utf-8").read()
    parts, nom, cur = {}, "EN-TÊTE", []
    ordre = []
    for ligne in txt.splitlines(keepends=True):
        if ligne.startswith("## "):
            parts[nom] = "".join(cur); ordre.append(nom); nom = ligne.strip()[3:]; cur = []
        else:
            cur.append(ligne)
    parts[nom] = "".join(cur); ordre.append(nom)
    return ordre, parts

o11, p11 = sections(sys.argv[1]); o12, p12 = sections(sys.argv[2])
print("sections v11 :", o11); print("sections v12 :", o12)
for s in o12:
    a, b = p11.get(s), p12.get(s)
    if a is None:
        print(f"\n### {s} : ABSENTE de la v11"); continue
    ha, hb = hashlib.sha256(a.encode()).hexdigest()[:16], hashlib.sha256(b.encode()).hexdigest()[:16]
    if a == b:
        print(f"\n### {s} : IDENTIQUE au bit près ({len(b)} caractères, {ha})")
    else:
        print(f"\n### {s} : DIFFÈRE ({len(a)} → {len(b)} caractères, {ha} → {hb})")
        for l in difflib.unified_diff(a.splitlines(), b.splitlines(), "v11", "v12", lineterm="", n=0):
            print("   ", l[:400])
