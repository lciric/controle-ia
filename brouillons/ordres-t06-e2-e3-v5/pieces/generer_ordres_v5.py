#!/usr/bin/env python3
"""Génère le brouillon v5 de l'ordre E3 (R-1683 : lanceur v8, amorce v6) à partir de l'ORDRE SCELLÉ `docs/procedures/ordre-fille-6-t06-e3-v4.md` (révision 2, R-1685) de `main`
(lu dans les objets git de `refs/remotes/origin/main`, empreinte vérifiée) : retrait de la section « Scellement » et des mentions de scellement, commandes
`lancer_t06_v8.sh`, commit d'épreuve en marqueur `<<COMMIT_EPREUVES>>`, branche d'essai neuve `essai/t06-e3-v3`, filtre de lecture LU dans le lanceur
(`controle_ia.t06.session_v7.filtre_recherche`), conduite sur `ARRET mort` et `ARRET inventaire` du lanceur v8. Chaque ancien texte doit être présent
exactement une fois. Aucun .sha256 (la mère scelle) ; seul marqueur : <<COMMIT_EPREUVES>>.
    python3 generer_ordres_v5.py RACINE_DU_DEPOT [--ecrire]"""
import hashlib, json, pathlib, re, subprocess, sys

CFG_E3 = "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v2.json"
SCELLE = ("docs/procedures/ordre-fille-6-t06-e3-v4.md", "1dc7cba6f4c07bf3a9f")          # début de l'empreinte donnée par la mère ; la valeur entière est relue ci-dessous
COMMIT_V4 = "0e52603c2dac3c34988829fba5a8d5b9051ba9ac"          # commit d'épreuve de l'ordre scellé v4 (révision 2, R-1685)


def _appliquer(t, ancien, nouveau, nom, journal):
    n = t.count(ancien)
    if n != 1:
        raise SystemExit(f"ERREUR {nom} : ancien présent {n} fois (1 exigé)")
    journal.append(f"ok {nom}")
    return t.replace(ancien, nouveau)


def filtre_a100(racine):
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.t06 import session_v7
    return session_v7.filtre_recherche(json.load(open(racine / CFG_E3, encoding="utf-8")), "course")


def scelle(racine):
    b = subprocess.run(["git", "-C", str(racine), "show", f"refs/remotes/origin/main:{SCELLE[0]}"], check=True, capture_output=True).stdout
    h = hashlib.sha256(b).hexdigest()
    if not h.startswith(SCELLE[1]):
        raise SystemExit(f"{SCELLE[0]} sur main : empreinte {h} ≠ {SCELLE[1]}…")
    return b.decode("utf-8"), h


def textes(racine):
    racine = pathlib.Path(racine); j = []
    t, h = scelle(racine)
    t = t[:t.index("\n## Scellement (session mère")].rstrip("\n") + "\n"
    t = _appliquer(t, "— v4, scellé (R-1683), révision 2 (R-1685)", "— v5 (brouillon)", "titre", j)
    a = t[t.index("Brouillon v4 de la fille 10"):]
    a = a[:a.index("Français, sans sigle")]
    n = ("Brouillon v5 de la fille 10 (session de développement, Sonnet 5.5 ; issu de l'ordre v4 scellé par la mère (R-1683, révision 2 R-1685), dont il reprend le texte ; "
         "adopte l'amorce v6 et le lanceur v8 après la contre-lecture Opus de la v7), pour contre-lecture (Opus) et scellement par la session mère\n"
         "`session_01Qi7Gr6NLmhhAcdmnACBC7G`. **Non scellé.** Ce texte devient un ordre seulement une fois scellé (la mère écrit le `.sha256` et "
         "remplit le seul marqueur `<<COMMIT_EPREUVES>>`). ")
    t = _appliquer(t, a, n, "présentation", j)
    t = t.replace(COMMIT_V4, "<<COMMIT_EPREUVES>>")
    t = t.replace("lancer_t06_v7.sh", "lancer_t06_v8.sh").replace("lanceur de T0.6 v7", "lanceur de T0.6 v8").replace("lanceur v7", "lanceur v8")
    t = t.replace("amorce v5 <sha256>", "amorce v6 <sha256>").replace("session_v6", "session_v7")
    t = t.replace("essai/t06-e3-v2", "essai/t06-e3-v3")                               # branche neuve (R12)
    t = _appliquer(t, "Les préalables 1 à 4 de l'ordre d'E2 scellé (`docs/procedures/ordre-fille-6-t06-e2-v4.md`, issu du brouillon v4) (clone,",
                   "Les préalables 1 à 4 de l'ordre d'E2 scellé (`docs/procedures/ordre-fille-6-t06-e2-v4.md`) — **avec le commit de cet ordre-ci** (lanceur v8, amorce v6), qui n'est pas celui d'E2 — (clone,", "renvoi à E2", j)
    a = t[t.index("- **`ARRET mort : instance <ID> absente de l'inventaire` (R-1677)**"):]
    a = a[:a.index("\n")]
    n = ("- **`ARRET mort` par absence (R-1677, R-1683)** : le lanceur v8 l'imprime quand une liste d'inventaire NON vide ne contient pas l'instance à deux relevés, ou quand l'instance seule "
         "(`show instance <ID>`) est introuvable à deux relevés : l'instance a disparu (refus de l'amorce après 180 s d'attente annoncée, ou destruction par la minuterie). Vérifie-le toi-même avant de conclure, "
         "par l'instance seule et non par la liste : `timeout -k 5 120 \"$VAST\" show instance <ID> --raw` ; si elle répond (instance trouvée, quel que soit son état), détruis-la par son identifiant "
         "(`timeout -k 5 120 \"$VAST\" destroy instance <ID>`) et écris-le comme attendu manquant grave ; si l'appel échoue sans dire « introuvable », message à la mère avant toute autre création ; relève les dernières "
         "lignes `AMORCE` de `journal-instance.txt` (copie entière à chaque relevé, `logs --tail 20000`, valeurs de clés masquées), puis message.\n"
         "- **Liste d'inventaire vide, illisible ou en échec (R-1683)** : jamais un `ARRET mort`. Le lanceur imprime sur la sortie standard « ALERTE liste d'inventaire non concluante … » (instance seule présente) ou "
         "« ALERTE inventaire (n/3) … » ; **trois relevés de suite sans présence établie : `ARRET inventaire`** (code 3) : vérifie à la main (`vastai show instances`, `show instance <ID>`), message à la mère, ne crée rien.\n"
         "- **Refus de l'amorce (R-1683)** : la ligne « refus : extraction partielle impossible (sparse-checkout …) : <message de git> » cite désormais le message de git ; le délai du `checkout` est de 900 s (pire cas du clonage 1 800 s). **Carte invisible (R-1686)** : en mode réel, `torch.cuda.is_available()` faux donne « refus : carte invisible pour torch … : pilote <version> » (cause consignée sur la branche avant la destruction, après 180 s) : relève la version du pilote, message à la mère, ne crée rien. L'offre doit porter `cuda_max_good` ≥ 13,0 (filtre de création, puis garde locale sur l'offre choisie : la ligne `OFFRE CONFORME` montre `cuda_max_good=…`).")
    t = _appliquer(t, a, n, "ARRET mort et ARRET inventaire", j)
    f = filtre_a100(racine)
    ancien_f = f.replace(" cuda_max_good>=13.0", "")                                  # filtre de l'ordre scellé v3 (lanceur v7) : sans l'exigence de pilote (R-1686)
    t = _appliquer(t, "'" + ancien_f + "'", "'" + f + "'", "filtre de lecture = filtre du lanceur v8 (cuda_max_good>=13.0)", j)
    trouves = re.findall(r"'(num_gpus=1[^']*)'", t)
    if trouves != [f]:
        raise SystemExit(f"ERREUR filtre de lecture ≠ filtre du lanceur : {trouves} / {f}")
    restes = [l for l in t.splitlines() if "lancer_t06_v7.sh" in l or "04d89122" in l or "Scellement" in l or "t06-e3-v2" in l]
    if restes:
        raise SystemExit(f"ERREUR restes : {restes[:2]}")
    marq = sorted(set(re.findall(r"<<[A-Z_]+>>", t)))
    if marq != ["<<COMMIT_EPREUVES>>"]:
        raise SystemExit(f"ERREUR marqueurs {marq}")
    return {"e3": t}, j, h


if __name__ == "__main__":
    racine = pathlib.Path(sys.argv[1]); out, j, h = textes(racine); print("\n".join(j)); print("ordre scellé", h)
    for nom, t in out.items():
        print(nom, hashlib.sha256(t.encode()).hexdigest(), len(t.splitlines()), "lignes")
        if "--ecrire" in sys.argv:
            (racine / f"brouillons/ordres-t06-e2-e3-v5/ordre-fille-6-t06-{nom}-v5.md").write_text(t, encoding="utf-8")
