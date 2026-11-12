#!/usr/bin/env python3
"""Génère les ordres E2 et E3 v3 (R-1660) : ordres v2 + lanceur v6 (`lancer_t06_v6.sh`) + filtres de lecture LUS dans le lanceur
(`controle_ia.t06.session_v5.filtre_recherche` appliqué aux configurations d'épreuve : une seule source, égalité vérifiée ici et par
`tests/test_t06_v6_scripts.py`). Chaque ancien texte doit être présent exactement une fois. Aucun .sha256 (la mère scelle).
    python3 generer_ordres_v3.py RACINE_DU_DEPOT [--ecrire]"""
import hashlib, json, pathlib, re, sys

NOTES = "docs/notes/g0-deux-semaines-v1/"
CFG_E2, CFG_E3 = NOTES + "config-t06-epreuve-e2-v1.json", NOTES + "config-t06-epreuve-e3-v1.json"


def _appliquer(t, ancien, nouveau, nom, journal):
    n = t.count(ancien)
    if n != 1:
        raise SystemExit(f"ERREUR {nom} : ancien présent {n} fois (1 exigé)")
    journal.append(f"ok {nom}")
    return t.replace(ancien, nouveau)


def filtres(racine):
    """Filtres de recherche tels que le lanceur v6 les construirait : E2 course (carte modeste), E3 course (A100), E3 relance (H200)."""
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.t06 import session_v5
    c2 = json.load(open(racine / CFG_E2, encoding="utf-8")); c3 = json.load(open(racine / CFG_E3, encoding="utf-8"))
    return {"modeste": session_v5.filtre_recherche(c2, "course"), "a100": session_v5.filtre_recherche(c3, "course"),
            "h200": session_v5.filtre_recherche(c3, "relance")}


def textes(racine):
    racine = pathlib.Path(racine); v2 = racine / "brouillons/ordres-t06-e2-e3-v2"; j = []
    f = filtres(racine)
    # E2
    t = (v2 / "ordre-fille-6-t06-e2-v2.md").read_text(encoding="utf-8")
    a = t[t.index("`env -i … timeout 300 vastai search offers 'num_gpus=1 gpu_name=RTX_4090"):t.index("Vérifie par un court script Python")]
    n = (f"`env -i … timeout 300 vastai search offers '{f['modeste']}' -o dph_total --storage 150 --raw > \"$W/offres-modeste.json\"` "
         f"(**ce filtre est exactement celui que `creation auto` envoie**, lu dans le lanceur v6 : `python3 -I -B -c \"import sys; sys.path.insert(0,'src'); from controle_ia.t06 import session_v5; "
         f"import json; print(session_v5.filtre_recherche(json.load(open('{CFG_E2}')), 'course'))\"`, à comparer au caractère près),\n"
         f"même commande avec les filtres de l'ordre d'E3, lus de la même façon dans la configuration d'E3 : `'{f['a100']}'` (`offres-a100.json`, carte « course ») et "
         f"`'{f['h200']}'` (`offres-h200.json`, carte « relance »), puis la même recherche modeste **sans** `--storage` (`offres-modeste-sans-storage.json`). ")
    t = _appliquer(t, a, n, "E2 filtres de lecture = filtres du lanceur", j)
    t = _appliquer(t, "fichiers `offres-*.json` de cette étape ne servent qu'au contrôle E2-1 (lectures), pas à la création.",
                   "fichiers `offres-*.json` de cette étape ne servent qu'au contrôle E2-1 (lectures), pas à la création. **Contrôle de la prédiction (R-1660)** : l'offre de rang 1 (la moins chère, prix de la carte + du stockage) de `offres-modeste.json` doit être l'offre que `creation auto` choisira au rang 1, à un changement d'identifiant près (R-578) : relève la machine (`machine_id`) et le prix de rang 1 ici, puis compare-les à `machine=` et `prix_carte=` de `OFFRE CONFORME` (étape 4) ; une différence n'est pas un arrêt si le marché a bougé entre les deux lectures, mais elle s'écrit au compte rendu.", "E2 contrôle de prédiction", j)
    e2 = t
    # E3
    t = (v2 / "ordre-fille-6-t06-e3-v2.md").read_text(encoding="utf-8")
    t = _appliquer(t, "Pas de `vastai search` à la main pour E3.",
                   f"Lecture facultative, sans location (0 USD), pour prévoir l'offre : `env -i … timeout 300 vastai search offers '{f['a100']}' -o dph_total --storage 150 --raw` — **ce filtre est exactement celui de `creation auto`** (lu dans le lanceur v6 ; même lecture que `offres-a100.json` de l'ordre d'E2). Aucune offre ne se choisit à la main : seul `creation auto` choisit.", "E3 lecture facultative = filtre du lanceur", j)
    e3 = t
    out = {}
    for nom, t in (("e2", e2), ("e3", e3)):
        t = t.replace("lancer_t06_v5.sh", "lancer_t06_v6.sh")
        t = t.replace("lanceur v5", "lanceur v6").replace("(lanceur v6, R-1657)", "(lanceur v6, R-1657, R-1660)")
        t = t.replace("du lanceur de T0.6 v5 :", "du lanceur de T0.6 v6 :").replace("(code 5, v5)", "(code 5, v6)").replace("texte de la v5 :", "texte depuis la v5 :")
        t = t.replace("— v2 (brouillon)", "— v3 (brouillon)")
        t = t.replace("Brouillon v2 de la fille 10", "Brouillon v3 de la fille 10")
        t = t.replace("remplace la v1, qui reste archivée", "remplace les v1 et v2, archivées").replace("remplace la v1, archivée", "remplace les v1 et v2, archivées")
        t = t.replace("adopte le lanceur v6, R-1657)", "adopte le lanceur v6, qui filtre aussi la fiabilité comme la lecture, R-1657, R-1660)")
        restes = [l for l in t.splitlines() if "lancer_t06_v4.sh" in l or "lancer_t06_v5.sh" in l or "<OFFRE>" in l]
        if restes:
            raise SystemExit(f"ERREUR {nom} : restes {restes[:2]}")
        out[nom] = t
    # égalité : tout filtre de `search offers '…'` des ordres appartient aux filtres du lanceur
    for nom, t in out.items():
        for m in re.findall(r"'(num_gpus=1[^']*)'", t):
            if m not in f.values():
                raise SystemExit(f"ERREUR {nom} : filtre de lecture hors du lanceur : {m}")
    return out, j


if __name__ == "__main__":
    racine = pathlib.Path(sys.argv[1]); out, j = textes(racine); print("\n".join(j))
    for nom, t in out.items():
        print(nom, hashlib.sha256(t.encode()).hexdigest(), len(t.splitlines()), "lignes")
        if "--ecrire" in sys.argv:
            p = racine / f"brouillons/ordres-t06-e2-e3-v3/ordre-fille-6-t06-{nom}-v3.md"; p.write_text(t, encoding="utf-8")
