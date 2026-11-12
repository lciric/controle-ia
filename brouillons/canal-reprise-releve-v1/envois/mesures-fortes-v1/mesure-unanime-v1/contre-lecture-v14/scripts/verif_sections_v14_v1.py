"""Contre-lecture v14 : sections de science de la v14 comparées au bit près à la v13 ; Plan d'analyse comparé après
remplacement inverse des noms de sortie v14 -> v13. Ne lit que les deux textes du préenregistrement.
Usage : python verif_sections_v14_v1.py V13.md V14.md"""
import sys, re, hashlib, json, difflib

def sections(chemin):
    t = open(chemin, encoding="utf-8").read()
    morceaux = re.split(r"(?m)^## ", t)
    d = {"(en-tête)": morceaux[0]}
    for m in morceaux[1:]:
        titre, _, corps = m.partition("\n")
        d[titre.strip()] = corps
    return d

a, b = sections(sys.argv[1]), sections(sys.argv[2])
gelees = ["Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Critères de lecture gelés", "Liste d'arrêt"]
r = {"ordre_v13": list(a), "ordre_v14": list(b), "sections": {}}
for s in gelees:
    r["sections"][s] = {"identique_au_bit": a[s] == b[s], "octets_v13": len(a[s].encode()), "octets_v14": len(b[s].encode()),
                        "sha256_v13": hashlib.sha256(a[s].encode()).hexdigest(), "sha256_v14": hashlib.sha256(b[s].encode()).hexdigest()}
pa13, pa14 = a["Plan d'analyse"], b["Plan d'analyse"]
brut = [l for l in difflib.unified_diff(pa13.splitlines(), pa14.splitlines(), "v13", "v14", lineterm="", n=0)]
# jetons distincts qui diffèrent
jet = lambda t: re.findall(r"[^\s`«»(),;]+", t)
sm = difflib.SequenceMatcher(None, jet(pa13), jet(pa14), autojunk=False)
paires = sorted({(" ".join(jet(pa13)[i1:i2]), " ".join(jet(pa14)[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"})
inverse = pa14
noms = sorted({n for _, n in paires for n in re.findall(r"[A-Za-z0-9_.\-]*v14[A-Za-z0-9_.\-]*", n)})
for n in noms:
    inverse = inverse.replace(n, n.replace("v14", "v13"))
r["plan_analyse"] = {"identique_brut": pa13 == pa14, "lignes_diff_brut": brut, "paires_de_jetons_differents": paires,
                     "noms_v14_remplaces": noms, "nombre_de_noms": len(noms), "identique_apres_remplacement_inverse": inverse == pa13,
                     "occurrences_v14_dans_plan_v14": len(re.findall("v14", pa14)), "occurrences_v13_dans_plan_v13": len(re.findall("v13", pa13)),
                     "occurrences_v13_dans_plan_v14": len(re.findall("v13", pa14))}
print(json.dumps(r, ensure_ascii=False, indent=1))
