"""Contre-lecture v14 : croise chaque empreinte citée par le texte v14 (pleine, 64 hex ; courte, 8 hex suivis de « … »)
avec les empreintes SHA-256 des fichiers sur disque. Ne parcourt JAMAIS donnees/ : l'empreinte des données réelles est
déclarée « non vérifiée à dessein ». Les objets et commits git (40 ou 8 hex) sont listés à part, vérifiés par `git`.
Usage : python verif_empreintes_texte_v14_v1.py RACINE_DEPOT DOSSIER_MESURE TEXTE_V14"""
import sys, re, hashlib, json, os
racine, dossier, texte = sys.argv[1:4]
t = open(texte, encoding="utf-8").read()
disque = {}
def ajoute(p):
    disque.setdefault(hashlib.sha256(open(p, "rb").read()).hexdigest(), []).append(os.path.relpath(p, racine))
for d, _, fs in os.walk(dossier):
    for f in fs:
        ajoute(os.path.join(d, f))
for sous in ("src/controle_ia", "registres/passations", "docs/notes", "brouillons/canal-reprise-releve-v1/envois/mesures-fortes-v1"):
    for d, _, fs in os.walk(os.path.join(racine, sous)):
        for f in fs:
            p = os.path.join(d, f)
            if "/donnees/" in p or not os.path.isfile(p): continue
            ajoute(p)
REELLE = "968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf"
pleines = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", t)))
courtes = sorted(set(re.findall(r"`([0-9a-f]{8})…`", t)))
git40 = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", t)))
git8 = sorted(set(re.findall(r"`([0-9a-f]{8})`", t)))
r = {"pleines": {}, "courtes": {}, "objets_git_40": git40, "commits_8": git8}
for h in pleines:
    r["pleines"][h] = "NON VÉRIFIÉE À DESSEIN (données réelles, R1)" if h == REELLE else (disque.get(h, ["INTROUVABLE"])[0])
for c in courtes:
    m = [v[0] for h, v in disque.items() if h.startswith(c)]
    r["courtes"][c] = "NON VÉRIFIÉE À DESSEIN (données réelles, R1)" if REELLE.startswith(c) else (m[0] if m else "INTROUVABLE")
r["bilan"] = {"pleines": len(pleines), "pleines_introuvables": [h for h, v in r["pleines"].items() if v == "INTROUVABLE"],
              "courtes": len(courtes), "courtes_introuvables": [h for h, v in r["courtes"].items() if v == "INTROUVABLE"]}
print(json.dumps(r, ensure_ascii=False, indent=1))
