"""Candidat 1 de T0.6 = brouillon 5 + les 7 couples de la contre-lecture neuve du lanceur v2 et du brouillon 5 (fille 9,
lignée Opus 5.5 ; liste nue, numérotés 1 à 7 dans l'ordre), appliqués dans l'ordre, puis les substitutions C01 et suivantes
(`substitutions-candidat1-v1.json`). Chaque « ancien » doit apparaître exactement le nombre de fois attendu (1 par défaut)
au moment de son application ; sinon arrêt, rien d'écrit. Bibliothèque standard seule ; aucun réseau. Journal écrit à côté
(`journal-candidat1-v1.md`) : empreintes des entrées, ligne de chaque application, comptes des clés de citation et des
marqueurs du résultat, empreinte du résultat. Rédacteur neuf, sous-agent de la fille 7 (T1 bis), 5 novembre 2026.

    python3 -I -B appliquer-candidat1-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
BROUILLON5 = "brouillons/T0.6-organismes-v0-v1-brouillon5.md"
SHA_BROUILLON5 = "e95d4d48825bdb427207be87964fa46ad62918ff8b9dac5e0c106aa35f38f817"
# Pièces de la contre-lecture neuve (branche `prep/fille-9-contre-lectures-v1`, commit 15d2ce93, hors de cet arbre) :
# sha256 complets relevés par `sha256sum` le 5 novembre 2026 ; la copie des couples est vérifiée ici à l'octet.
COUPLES = "couples-brouillon5-vers-candidat1-T0.6-v1.json"
SHA_COUPLES = "34b2c64d94b8931084c4ddf6146c9df74a2b12b216158aaa097a0f733aa8e3d1"
SHA_CL = "b49ca28b660e122fcfa5722bde4ae4b0b67914b008bd5290a63b2d2b9b8f1f2e"
SHA_CORR = "9a89626bce12095930e1bd10006213e9f284f0574fda7c71895198381eb2c792"
CANDIDAT1 = "brouillons/T0.6-organismes-v0-v1-candidat1.md"
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")
MARQUEURS_ATTENDUS = 11
# Clés lues mécaniquement par la chaîne : « clé : ` » (clé, espace, deux-points, espace, accent grave), comptées en lignes.
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6",
        "Tests attendus", "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6",
        "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
FORME_AMORCE = "`scripts/amorce_instance_t06_v3.sh` (`"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ligne_de(texte: str, ancien: str) -> int:
    return texte[: texte.index(ancien)].count("\n") + 1


def appliquer(texte: str, ident: str, ancien: str, nouveau: str, attendu: int, journal: list[str]) -> str:
    n = texte.count(ancien)
    if n != attendu:
        raise SystemExit(f"{ident} : « ancien » trouvé {n} fois, {attendu} attendu : arrêt, rien d'écrit")
    ligne = ligne_de(texte, ancien)
    journal.append(f"| {ident} | {ligne} | {attendu} | {len(ancien)} | {len(nouveau)} |")
    return texte.replace(ancien, nouveau)


def main(racine: Path) -> int:
    b5 = racine / BROUILLON5
    if sha(b5) != SHA_BROUILLON5:
        raise SystemExit("brouillon 5 : empreinte non conforme")
    couples_p = ICI / COUPLES
    if sha(couples_p) != SHA_COUPLES:
        raise SystemExit("couples : empreinte non conforme")
    couples = json.loads(couples_p.read_text(encoding="utf-8"))
    if not (isinstance(couples, list) and len(couples) == 7):
        raise SystemExit("couples : liste nue de 7 couples attendue")
    subs_p = ICI / "substitutions-candidat1-v1.json"
    subs = json.loads(subs_p.read_text(encoding="utf-8"))
    sortie = racine / CANDIDAT1
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà : rien d'écrasé (R12)")
    maintenant = datetime.now(timezone.utc)
    heure = maintenant.strftime("%H:%M")
    texte = b5.read_text(encoding="utf-8")
    journal = ["| couple ou substitution | ligne (au moment de l'application) | occurrences | longueur ancien | longueur nouveau |",
               "|---|---|---|---|---|"]
    for i, c in enumerate(couples, 1):
        texte = appliquer(texte, f"couple {i}", c["ancien"], c["nouveau"], 1, journal)
    rempl = {"{HEURE}": heure, "{SHA_CL}": SHA_CL, "{SHA_COUPLES}": SHA_COUPLES, "{SHA_CORR}": SHA_CORR}
    for s in subs["substitutions"]:
        ancien, nouveau = s["ancien"], s["nouveau"]
        for k, v in rempl.items():
            ancien, nouveau = ancien.replace(k, v), nouveau.replace(k, v)
        texte = appliquer(texte, s["id"], ancien, nouveau, int(s.get("occurrences", 1)), journal)
    # Vérifications du résultat (arrêt, rien d'écrit, si l'une échoue).
    marqueurs = sorted(set(MARQUEUR.findall(texte)))
    comptes_m = {m: texte.count(m) for m in marqueurs}
    if len(marqueurs) != MARQUEURS_ATTENDUS:
        raise SystemExit(f"marqueurs : {len(marqueurs)} distincts, {MARQUEURS_ATTENDUS} attendus : {marqueurs}")
    lignes = texte.split("\n")
    comptes_c = {k: sum(1 for l in lignes if f"{k} : `" in l) for k in CLES}
    if comptes_c["Tests attendus"] != 1:
        raise SystemExit(f"« Tests attendus : ` » : {comptes_c['Tests attendus']} ligne(s), 1 attendue")
    for k, n in comptes_c.items():
        if n > 1:
            raise SystemExit(f"« {k} : ` » : {n} lignes, au plus 1")
    n_amorce = texte.count(FORME_AMORCE)
    if n_amorce != 1:
        raise SystemExit(f"forme de citation de l'amorce « {FORME_AMORCE} » : {n_amorce}, 1 attendue")
    sortie.write_text(texte, encoding="utf-8")
    j = [f"# Journal du candidat 1 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- brouillon 5 : `{BROUILLON5}`, `{SHA_BROUILLON5}` (empreinte vérifiée avant tout ; non scellé, pas de compagnon)",
         f"- contre-lecture neuve du lanceur v2 et du brouillon 5 (hors de cet arbre, branche `prep/fille-9-contre-lectures-v1`, commit `15d2ce93`,"
         f" `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v2/contre-lecture-lanceur-T0.6-v2.md`) : `{SHA_CL}` (relevé par `sha256sum`)",
         f"- corrections de code v3 (même dossier, `corrections-code-lanceur-T0.6-v3.md`) : `{SHA_CORR}` (relevé par `sha256sum`)",
         f"- couples : `{COUPLES}` (copie à l'octet dans ce dossier, `cmp` égal), `{SHA_COUPLES}` (vérifié), {len(couples)} couples, liste nue numérotée 1 à 7 dans l'ordre, appliqués dans l'ordre",
         f"- substitutions : `substitutions-candidat1-v1.json`, `{sha(subs_p)}`, {len(subs['substitutions'])} substitutions, appliquées après les couples",
         f"- script : `appliquer-candidat1-v1.py`, `{sha(Path(__file__).resolve())}`", "", *journal, "",
         f"Marqueurs du candidat 1 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "",
         *[f"- `{m}` : {n}" for m, n in comptes_m.items()], "",
         "Clés lues par la chaîne (lignes qui portent « clé : » suivi d'un accent grave ; « Tests attendus » exactement 1, les autres au plus 1) :", "",
         *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "",
         f"- forme de citation de l'amorce « {FORME_AMORCE} » : {n_amorce}", "",
         f"- résultat : `{CANDIDAT1}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat1-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
