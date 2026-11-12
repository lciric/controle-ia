"""Contre-lecture v13 de la mesure unanime — vérifications mécaniques du texte (R1, R2, R6, R12).

1. `prereg.problemes` sur la v13 (module du dépôt, importé sans modification).
2. Sections v12 → v13 : Hypothèse, Prédiction, Métrique, Seuil, Critères, Liste d'arrêt identiques au bit près ;
   Plan d'analyse identique jusqu'au point « **Commandes** », puis diff mot à mot ; Contre-lecture : ajout en fin seulement.
3. Toutes les empreintes citées (64 hexadécimaux, ou 8 hexadécimaux suivis de « … ») croisées avec le disque.
4. Appariement des `**` ligne par ligne ; marqueurs ⟨…⟩, À REMPLIR, <<…>>.
Usage : PYTHONPATH=…/src python -B verif_cv13_v1.py DOSSIER > sortie.json
Aucun fichier de `donnees/` n'est ouvert ni empreinté.
"""
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, "/home/claude/canal-conv-audit-n04/src")
from controle_ia import prereg  # noqa: E402

D = Path(sys.argv[1])
V12 = D / "preenregistrement-mesure-unanime-v12.md"
V13 = D / "preenregistrement-mesure-unanime-v13.md"
res = {}


def emp(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


t12, t13 = V12.read_text(encoding="utf-8"), V13.read_text(encoding="utf-8")
res["empreintes_textes"] = {"v12": emp(V12), "v13": emp(V13)}

# 1. prereg.problemes
res["prereg_problemes_v13"] = prereg.problemes(V13)
res["prereg_problemes_v12"] = prereg.problemes(V12)

# 2. sections
s12, s13 = prereg.sections(t12), prereg.sections(t13)
res["sections_v13"] = list(s13)
identiques = {}
for nom in ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Critères de lecture gelés", "Liste d'arrêt"):
    identiques[nom] = {"identique_au_bit": s12[nom] == s13[nom], "caracteres": len(s13[nom])}
res["sections_science_identiques"] = identiques
pa12, pa13 = s12["Plan d'analyse"], s13["Plan d'analyse"]
i12, i13 = pa12.index("**Commandes**"), pa13.index("**Commandes**")
res["plan_analyse"] = {
    "avant_Commandes_identique": pa12[:i12] == pa13[:i13],
    "caracteres_avant_Commandes": i13,
    "diff_mots_apres_Commandes": [
        d for d in difflib.ndiff(pa12[i12:].split(), pa13[i13:].split()) if d[:1] in "+-"
    ],
}
cl12, cl13 = s12["Contre-lecture"], s13["Contre-lecture"]
res["contre_lecture"] = {
    "v13_commence_par_v12": cl13.startswith(cl12.rstrip()),
    "ajout_en_fin_lignes": cl13[len(cl12.rstrip()):].strip().count("\n") + 1,
    "ajout_en_fin_debut": cl13[len(cl12.rstrip()):].strip()[:80],
}

# 3. empreintes citées
disque = {}
for p in list(D.glob("*")) + list(D.glob("*/*")) + list(D.glob("*/*/*")):
    if p.is_file() and not p.name.endswith(".sha256"):
        disque[emp(p)] = str(p.relative_to(D))
for extra in ("/home/claude/canal-conv-audit-n04/src/controle_ia/bases/sequentiel.py",
              "/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v3.md"):
    if Path(extra).is_file():
        disque[emp(extra)] = extra
pleines = sorted(set(re.findall(r"\b[0-9a-f]{64}\b", t13)))
courtes = sorted(set(re.findall(r"\b([0-9a-f]{8})…", t13)))
INTERDITES = {"968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf": "données réelles : non vérifiées (R1, interdit de lire donnees/)",
              "bed9107b67c969e0e9a97336000a569faf2c519dd556731ace14f29de404885e": "synthèse « sur main » : absente de ce worktree, non vérifiable ici"}
pl = {}
for h in pleines:
    if h in INTERDITES:
        pl[h] = INTERDITES[h]
    elif h in disque:
        pl[h] = "OK : " + disque[h]
    elif h == emp(V13):
        pl[h] = "ERREUR : le texte cite sa propre empreinte"
    else:
        pl[h] = "INTROUVABLE sur disque"
res["empreintes_pleines_citees"] = pl
co = {}
prefixes_disque = {h[:8]: f for h, f in disque.items()}
for c in courtes:
    if c in prefixes_disque:
        co[c] = "OK : " + prefixes_disque[c]
    elif any(c == k[:8] for k in INTERDITES):
        co[c] = next(v for k, v in INTERDITES.items() if k[:8] == c)
    else:
        co[c] = "INTROUVABLE sur disque"
res["empreintes_courtes_citees"] = co
res["bilan_empreintes"] = {
    "pleines": len(pleines), "pleines_introuvables": [h for h, v in pl.items() if v.startswith("INTROUVABLE") or v.startswith("ERREUR")],
    "courtes": len(courtes), "courtes_introuvables": [c for c, v in co.items() if v.startswith("INTROUVABLE")],
}

# 4. `**` et marqueurs
impairs = []
for n, l in enumerate(t13.splitlines(), 1):
    k = l.count("**")
    if k % 2:
        impairs.append({"ligne": n, "occurrences": k, "extrait": l[:100]})
res["lignes_a_double_etoile_impaire"] = impairs
res["marqueurs"] = {"⟨": t13.count("⟨"), "À REMPLIR": t13.count("À REMPLIR"), "<<…>>": len(re.findall(r"<<[A-Z0-9_]+>>", t13))}
res["lignes_v13"] = len(t13.splitlines())
# cohérences nominales
res["noms_v12_restants_hors_section_contre_lecture_et_en_tete_historique"] = sorted(set(
    m for m in re.findall(r"[\w-]*v12[\w.-]*", t13)
))
res["noms_vNN_dans_plan_analyse_v13"] = sorted(set(re.findall(r"[\w-]*-v1[0-9][\w.-]*|[\w_]*_v[0-9]+\.py", pa13)))
print(json.dumps(res, ensure_ascii=False, indent=1))
