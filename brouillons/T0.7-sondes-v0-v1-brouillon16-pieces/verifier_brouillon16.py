"""Vérifications mécaniques du brouillon 16 de T0.7 (sondes v0) — v2 (version neuve de `verifier_brouillon15.py`).

Écrit le 2026-11-09 par le rédacteur des brouillons 15 et 16 (Claude Opus 5.5, sous-agent). Bibliothèque standard et
numpy seulement ; n'écrit rien ; n'imprime que des comptes, des booléens, des empreintes et des noms de marqueurs ou de
clés (jamais un poids, un score, une aire ni un champ de `meta` autre que son empreinte `complet` comparée).

Usage : cd /tmp && <python avec numpy> -I -B <chemin absolu de ce script> <racine absolue du dépôt> [partie]
        partie ∈ {couples, brouillon, grille, tout} (défaut : tout). Code 0 si tout passe, 1 sinon.

(1) couples : fichier léger `sondes-figees-legeres.npz` (empreinte exigée `701f73bd…`, égale à son compagnon) : sondes,
    planchers, couples (famille, concept, couche), Mahalanobis ; **croisement avec la liste `resultat.sondes` de
    `sondes-figees.json` (`fb418127…`)**, qui décrit les 430 sondes du fichier complet `91b61c45…` : les 424 noms du léger y
    figurent avec la même empreinte de sonde, les 6 absents sont des sondes de Mahalanobis, les deux principales
    (`resultat.principales`) sont dans le léger ; `meta.complet` du léger égal à `91b61c45…` (M-1).
(2) brouillon : marqueurs du brouillon 16 (motif de `controle_ia.prereg.GABARIT`) égaux à ceux du brouillon 14
    (`MOT_LAZAR_DS2_GARDE` rempli par N-066) ; balises de la garde en vigueur ; ligne DS-2 du brouillon 14 gardée à
    l'identique ; renvois à P3-bis b6 et clés du registre des préalables ; phrases de M-1, m-2 à m-5 ; aucune option 2 ou
    3 entre les balises ; `controle_ia.prereg.problemes` réduit à la ligne des marqueurs.
(3) grille : joue `grille_l_t07_brouillon16.py` (même dossier) et compare sa sortie, ligne à ligne, à la sortie scellée du
    brouillon 14 (`grille-l-t07-brouillon14.txt`, `0cfef5b2…`) : égales hors de la ligne (0 bis), qui est remplacée.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

LEGER = "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz"
SHA_LEGER = "701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60"
LISTE_COMPLET = "diag/20261019-230011-p3-reel/sondes-figees.json"
SHA_LISTE = "fb41812732711c1a2a152fa776c46be5a4c50a72ccdc8fd9b7b7f9edcc37d208"
SHA_COMPLET = "91b61c45cdafd0ab979e261171b9661920715fa42c6cbc9751cd2697bfd3177a"
B14 = "brouillons/T0.7-sondes-v0-v1-brouillon14.md"
SHA_B14 = "fe7b4e6dbc77edecf56bb16baf24e54939e0f845a76927e144a7f0409fd09345"
B15 = "brouillons/T0.7-sondes-v0-v1-brouillon15.md"
SHA_B15 = "7ed234bf5144a08036c6d41d452d89aad79e4cadc96adee24f0caf05fa28c0e2"
B16 = "brouillons/T0.7-sondes-v0-v1-brouillon16.md"
GRILLE14_SORTIE = "brouillons/T0.7-sondes-v0-v1-brouillon14-pieces/grille-l-t07-brouillon14.txt"
SHA_GRILLE14_SORTIE = "0cfef5b28725fc7407f0b941ad1c26da7d4ae5263cda0c126d0e6185417bf68f"
GRILLE16 = "brouillons/T0.7-sondes-v0-v1-brouillon16-pieces/grille_l_t07_brouillon16.py"
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
DEBUT = "[DÉBUT DE LA GARDE ADAPTÉE — EN VIGUEUR PAR N-066, OPTION 1]"
FIN = "[FIN DE LA GARDE ADAPTÉE]"
ANCIENNES_BALISES = ("[DÉBUT DE LA PROPOSITION « GARDE ADAPTÉE » — NON EN VIGUEUR]", "[FIN DE LA PROPOSITION « GARDE ADAPTÉE »]")
CLES_PREALABLES = ("ECRIT-PERIMETRE-JEUX-P3BIS", "ECRIT-LANCEMENT-RELANCE-P3BIS", "ECRIT-ENGAGEMENT-ETAPE-A-P3BIS",
                   "GARDE-ADAPTEE-T07-P3BIS", "RENDEZ-VOUS-P3BIS-n", "registres/prealables-p3bis-v1.md")
ANCIENS_RENVOIS = ("T07_B15_PERIMETRE_JEUX", "T07_B15_LANCEMENT_RELANCE", "T07_B15_ENGAGEMENT_ETAPE_A", "962dda89")
SECTIONS_EN_VIGUEUR = ("Écrits exigés par P3-bis", "Liste d'arrêt", "Reste avant le scellement", "Marqueurs à remplir")


def sha256(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def oui(b: bool) -> str:
    return "oui" if b else "NON"


def partie_couples(racine: Path) -> bool:
    import numpy as np
    sha = sha256(racine / LEGER)
    compagnon = (racine / (LEGER + ".sha256")).read_text(encoding="utf-8").split()[0]
    with np.load(racine / LEGER, allow_pickle=False) as z:
        index = json.loads(bytes(z["index"]).decode("utf-8"))
    sondes = index["sondes"]
    noms_planchers = {n for liste in index["meta"].get("planchers", {}).values() for n in liste}
    couples = [e for e in sondes if e["nom"] not in noms_planchers]
    triplets = {(e["famille"], e["nom"].split("-")[0], int(e["couche"])) for e in couples}
    maha = sum(1 for e in sondes if e["classe"] == "SondeMahalanobis")
    complet_meta = index["meta"].get("complet") == SHA_COMPLET
    liste_ok = sha256(racine / LISTE_COMPLET) == SHA_LISTE
    r = json.loads((racine / LISTE_COMPLET).read_text(encoding="utf-8"))["resultat"]
    liste = {e["nom"]: e for e in r["sondes"]}
    leger = {e["nom"]: e for e in sondes}
    inclus = set(leger) <= set(liste)
    memes_empreintes = inclus and all(liste[n]["empreinte"] == leger[n]["empreinte"] for n in leger)
    absents = [liste[n] for n in set(liste) - set(leger)]
    absents_maha = sum(1 for e in absents if e["classe"] == "SondeMahalanobis")
    principales = list(r["principales"].values())
    principales_ok = all(n in leger and n not in noms_planchers for n in principales)
    complet_cite = r["sondes_figees_sha256"] == SHA_COMPLET and r["sondes_legeres_sha256"] == SHA_LEGER
    print("(1) sondes figées de P3 : fichier léger, croisé avec la liste du complet")
    print(f"    léger : empreinte 701f73bd… et compagnon : {oui(sha == SHA_LEGER and compagnon == SHA_LEGER)} ; sondes "
          f"{len(sondes)} ; planchers {len(noms_planchers & set(leger))} ; couples {len(couples)} ; triplets {len(triplets)} ;"
          f" Mahalanobis {maha} ; meta.complet = 91b61c45… : {oui(complet_meta)}")
    print(f"    liste du complet (sondes-figees.json, fb418127… : {oui(liste_ok)}) : sondes {len(liste)} ; empreintes du "
          f"complet et du léger citées : {oui(complet_cite)}")
    print(f"    noms du léger tous dans la liste : {oui(inclus)} ; mêmes empreintes de sonde : {oui(memes_empreintes)} ; "
          f"absents du léger : {len(absents)}, dont Mahalanobis : {absents_maha}")
    print(f"    principales ({len(principales)}) dans le léger, hors planchers : {oui(principales_ok)}")
    ok = (sha == SHA_LEGER == compagnon and len(sondes) == 424 and len(couples) == 24 and len(triplets) == 24
          and maha == 0 and len(noms_planchers & set(leger)) == 400 and complet_meta and liste_ok and complet_cite
          and len(liste) == 430 and inclus and memes_empreintes and len(absents) == 6 and absents_maha == 6
          and len(principales) == 2 and principales_ok)
    print(f"    conforme : {oui(ok)}")
    return ok


def section(texte: str, titre: str) -> str:
    i = texte.find("\n## " + titre)
    if i < 0:
        return ""
    j = texte.find("\n## ", i + 4)
    return texte[i:j if j >= 0 else len(texte)]


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def partie_brouillon(racine: Path) -> bool:
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # code du dépôt, lu depuis la racine passée en argument
    t14 = (racine / B14).read_text(encoding="utf-8")
    t16 = (racine / B16).read_text(encoding="utf-8")
    n16 = norm(t16)
    ok_amont = sha256(racine / B14) == SHA_B14 and sha256(racine / B15) == SHA_B15
    m14 = sorted(set(GABARIT.findall(t14)))
    m16 = sorted(set(GABARIT.findall(t16)))
    print("(2) brouillon 16")
    print(f"    brouillons 14 (fe7b4e6d…) et 15 (7ed234bf…) intacts : {oui(ok_amont)} ; lignes du brouillon 16 : "
          f"{t16.count(chr(10))}")
    print(f"    marqueurs distincts : brouillon 14 {len(m14)} ; brouillon 16 {len(m16)} ; mêmes : {oui(m14 == m16)} ; "
          f"MOT_LAZAR_DS2_GARDE entre chevrons : {t16.count('<<MOT_LAZAR_DS2_GARDE>>')}")
    i, j = t16.find(DEBUT), t16.find(FIN)
    dedans = t16[i:j] if 0 <= i < j else ""
    balises = t16.count(DEBUT) == 1 and t16.count(FIN) == 1 and 0 <= i < j
    anciennes = sum(t16.count(b) for b in ANCIENNES_BALISES)
    options = sum(dedans.count(o) for o in ("option 2", "option 3", "règle 4 stricte", "« stricte »"))
    print(f"    balises de la garde en vigueur : {oui(balises)} ; balises « non en vigueur » restantes : {anciennes} ; "
          f"options 2 ou 3 entre les balises : {options} ; N-066 entre les balises : {dedans.count('N-066')}")
    ds2 = [l for l in t14.splitlines() if l.startswith("| DS-2 ordre de lecture de T0.7 |")]
    ds2_ok = len(ds2) == 1 and t16.count(ds2[0]) == 1
    print(f"    ligne DS-2 du brouillon 14 présente à l'identique : {oui(ds2_ok)}")
    zone = "".join(section(t16, s) for s in SECTIONS_EN_VIGUEUR)
    vieux = {r: zone.count(r) for r in ANCIENS_RENVOIS}
    cles = {c: section(t16, "Écrits exigés par P3-bis").count(c) for c in CLES_PREALABLES}
    print(f"    sections en vigueur trouvées : {sum(1 for s in SECTIONS_EN_VIGUEUR if section(t16, s))} sur "
          f"{len(SECTIONS_EN_VIGUEUR)} ; anciens renvois à P3-bis b5 restants : {sum(vieux.values())} ; clés du registre "
          f"des préalables citées dans « Écrits » : {sum(1 for v in cles.values() if v)} sur {len(cles)} ; "
          f"P3-bis b6 (aeb1f63a) cité : {t16.count('aeb1f63a')}")
    hors_tables = t16
    for tete in ("## Table « ce qui change du 14 au 15 »", "## Table « ce qui change du 15 au 16 »"):
        a = hors_tables.find(tete)
        b = hors_tables.find("\n## ", a + len(tete)) if a >= 0 else -1
        if 0 <= a < b:
            hors_tables = hors_tables[:a] + hors_tables[b:]
    nh = norm(hors_tables)
    phrases = {
        "M-1 : plus d'entrée « 91b61c45… (R11) »": nh.count("avec l'empreinte `91b61c45…` (R11)") == 0,
        "M-1 : plus d'entrée « sondes-figees.npz, 91b61c45… »": nh.count("(`sondes-figees.npz`, `91b61c45…`, `figees.lire_sondes") == 0,
        "M-1 : lecture par lire_sondes(chemin, \"701f73bd…\")": nh.count('lire_sondes(chemin, "701f73bd…")') >= 2,
        "M-1 : 9 morceaux sur calcul/regeneration-sondes-p3-v1": nh.count("calcul/regeneration-sondes-p3-v1") >= 2,
        "m-2 : plus de « gardée arrêtée jusqu'au verdict »": nh.count("gardée arrêtée jusqu'au verdict") == 0,
        "m-2 : « gardée arrêtée jusqu'à l'étape A »": nh.count("gardée arrêtée jusqu'à l'étape A") >= 1,
        "m-3 : « non un refus »": nh.count("non un refus") >= 2,
        "m-4 : « dans tous les cas où l'étape aboutit »": nh.count("dans tous les cas **où l'étape aboutit**") == 1,
        "m-5 : « avant le candidat de T0.7 »": n16.count("avant le candidat de T0.7") >= 1,
        "30 couples figés hors des tables": nh.count("30 couples figés") + nh.count("30 figées de P3") == 0,
        "M-3 : dernière ligne RENDEZ-VOUS-P3BIS-n": norm(dedans).count("**dernière** ligne `RENDEZ-VOUS-P3BIS-n`") == 1,
        "M-3 : question Q-J": norm(dedans).count("Question Q-J") == 1,
        "N-066 : ligne GARDE-ADAPTEE inscrite au scellement": norm(dedans).count("inscrite par la session mère au scellement") == 1,
        "N-066 : réserve R14 dans la table des critères": t16.count("| R14 | **brouillon 16, N-066**") == 1,
    }
    for k, v in phrases.items():
        print(f"      {k} : {oui(v)}")
    p = problemes(racine / B16)
    seuls = len(p) == 1 and p[0].startswith("marqueurs de gabarit restants")
    print(f"    controle_ia.prereg.problemes : {len(p)} ; seule la ligne des marqueurs : {oui(seuls)}")
    ok = (ok_amont and m14 == m16 and "<<MOT_LAZAR_DS2_GARDE>>" not in t16 and balises and anciennes == 0
          and options == 0 and ds2_ok and sum(vieux.values()) == 0 and all(cles.values()) and all(phrases.values())
          and seuls)
    print(f"    conforme : {oui(ok)}")
    return ok


def partie_grille(racine: Path) -> bool:
    script = racine / GRILLE16
    r = subprocess.run([sys.executable, "-I", "-B", str(script)], cwd="/tmp", capture_output=True, text=True)
    sortie = r.stdout
    ok14 = sha256(racine / GRILLE14_SORTIE) == SHA_GRILLE14_SORTIE
    l14 = (racine / GRILLE14_SORTIE).read_text(encoding="utf-8").splitlines()
    l16 = sortie.splitlines()
    sans = lambda ls: [l for l in ls if not l.startswith("(0 bis)")]
    egales = sans(l14) == sans(l16)
    une_0bis = sum(1 for l in l16 if l.startswith("(0 bis)")) == 1
    print("(3) grille du brouillon 16")
    print(f"    script : {hashlib.sha256(script.read_bytes()).hexdigest()} ; code {r.returncode} ; sortie : "
          f"{hashlib.sha256(sortie.encode('utf-8')).hexdigest()}")
    print(f"    sortie du brouillon 14 intacte (0cfef5b2…) : {oui(ok14)} ; lignes égales hors (0 bis) : {oui(egales)} "
          f"({len(sans(l16))} lignes) ; une ligne (0 bis) : {oui(une_0bis)} ; dernière ligne : {l16[-1] if l16 else ''}")
    ok = r.returncode == 0 and ok14 and egales and une_0bis and l16[-1].startswith("GRILLE COMPLÈTE")
    print(f"    conforme : {oui(ok)}")
    return ok


def main() -> int:
    racine = Path(sys.argv[1]).resolve()
    partie = sys.argv[2] if len(sys.argv) > 2 else "tout"
    res = []
    if partie in ("couples", "tout"):
        res.append(partie_couples(racine))
    if partie in ("brouillon", "tout"):
        res.append(partie_brouillon(racine))
    if partie in ("grille", "tout"):
        res.append(partie_grille(racine))
    print("TOUT PASSE" if res and all(res) else "ÉCHEC")
    return 0 if res and all(res) else 1


if __name__ == "__main__":
    sys.exit(main())
