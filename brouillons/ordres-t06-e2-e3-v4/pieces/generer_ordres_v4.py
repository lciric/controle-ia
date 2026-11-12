#!/usr/bin/env python3
"""Génère les brouillons v4 des ordres E2 et E3 (R-1677 : amorce v5, lanceur v7) à partir des ORDRES SCELLÉS de `main` (lus dans les objets git de
`refs/remotes/origin/main`, empreintes vérifiées) : retrait de la section « Scellement » et des mentions de scellement, commandes `lancer_t06_v7.sh`,
filtres de lecture LUS dans le lanceur (`controle_ia.t06.session_v6.filtre_recherche`, `inet_down>=500` compris), attendus nouveaux (ligne CLONAGE,
journal copié, `ARRET mort` par absence de l'inventaire, `refus` qui attend 180 s). Chaque ancien texte doit être présent exactement une fois.
Aucun .sha256 (la mère scelle) ; seul marqueur : <<COMMIT_EPREUVES>>.
    python3 generer_ordres_v4.py RACINE_DU_DEPOT [--ecrire]"""
import hashlib, json, pathlib, re, subprocess, sys

NOTES = "docs/notes/g0-deux-semaines-v1/"
CFG_E2, CFG_E3 = NOTES + "config-t06-epreuve-e2-v2.json", NOTES + "config-t06-epreuve-e3-v2.json"      # R-1670 : bornes de stockage 0,08 USD/h (la mère)
SCELLES = {"e2": ("docs/procedures/ordre-fille-6-t06-e2-v1.md", "8ad0ca95f9820381ffd7bbb3760b0365aac7b93d762c104171864a93ba2c8405"),
           "e3": ("docs/procedures/ordre-fille-6-t06-e3-v1.md", "97a45a31db4f18e38932fa1d41540df12421ecebb460e69ac2b40cd379e54c92")}
COMMIT_V3 = "74f59b28418a4f19dcea5d70b0c5f2c922a301fb"
CLONAGE_E2 = "`AMORCE … : CLONAGE mode=jouet secondes=<s> octets_git=<n> octets_arbre=<n> debit_Mo_s=<x> motifs=27`"
CLONAGE_E3 = "`AMORCE … : CLONAGE mode=reel secondes=<s> octets_git=<n> octets_arbre=<n> debit_Mo_s=<x> motifs=27`"


def _appliquer(t, ancien, nouveau, nom, journal):
    n = t.count(ancien)
    if n != 1:
        raise SystemExit(f"ERREUR {nom} : ancien présent {n} fois (1 exigé)")
    journal.append(f"ok {nom}")
    return t.replace(ancien, nouveau)


def filtres(racine):
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.t06 import session_v6
    c2 = json.load(open(racine / CFG_E2, encoding="utf-8")); c3 = json.load(open(racine / CFG_E3, encoding="utf-8"))
    return {"modeste": session_v6.filtre_recherche(c2, "course"), "a100": session_v6.filtre_recherche(c3, "course"),
            "h200": session_v6.filtre_recherche(c3, "relance")}


def scelle(racine, nom):
    chemin, attendu = SCELLES[nom]
    b = subprocess.run(["git", "-C", str(racine), "show", f"refs/remotes/origin/main:{chemin}"], check=True, capture_output=True).stdout
    if hashlib.sha256(b).hexdigest() != attendu:
        raise SystemExit(f"{chemin} sur main : empreinte ≠ {attendu}")
    return b.decode("utf-8")


def commun(t, nom, f, j):
    t = t[:t.index("\n## Scellement (session mère")].rstrip("\n") + "\n"                       # la section de scellement ne se recopie pas
    t = t.replace("— v3, scellé (R-1666)", "— v4 (brouillon)")
    a = t[t.index("Brouillon v3 de la fille 10"):]
    a = a[:a.index("Français, sans sigle")]
    n = ("Brouillon v4 de la fille 10 (session de développement, Sonnet 5.5 ; issu de l'ordre v3 scellé par la mère, R-1666, dont il reprend le texte ; "
         "adopte l'amorce v5 et le lanceur v7 après le défaut de chaîne d'E2, R-1676 et R-1677), pour contre-lecture (Opus) et scellement par la session mère\n"
         "`session_01Qi7Gr6NLmhhAcdmnACBC7G`. **Non scellé.** Ce texte devient un ordre seulement une fois scellé (la mère écrit le `.sha256` et "
         "remplit le seul marqueur `<<COMMIT_EPREUVES>>`" + ("" if nom == "e2" else ", **le même commit qu'à l'ordre d'E2**") + "). ")
    t = _appliquer(t, a, n, f"{nom} présentation", j)
    t = t.replace(COMMIT_V3, "<<COMMIT_EPREUVES>>")
    t = t.replace("config-t06-epreuve-e2-v1.json", "config-t06-epreuve-e2-v2.json").replace("config-t06-epreuve-e3-v1.json", "config-t06-epreuve-e3-v2.json")      # R-1670
    t = t.replace("essai/t06-e2-v1", "essai/t06-e2-v2").replace("essai/t06-e3-v1", "essai/t06-e3-v2")      # branches neuves : jamais celles d'une tentative antérieure (R12)
    t = t.replace("lancer_t06_v6.sh", "lancer_t06_v7.sh").replace("lanceur de T0.6 v6", "lanceur de T0.6 v7").replace("lanceur v6", "lanceur v7")
    t = t.replace("amorce v4 <sha256>", "amorce v5 <sha256>").replace("session_v5", "session_v6")
    # filtres de lecture = filtres du lanceur v7 (inet_down>=500 compris)
    for ancien_f, cle in (("num_gpus=1 rentable=true gpu_name=RTX_4090 reliability>=0.98 cpu_ram>=32 cpu_cores_effective>=8 disk_space>=150 dph_total<=0.6", "modeste"),
                          ("num_gpus=1 rentable=true gpu_name=A100_SXM4 reliability>=0.98 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=150 dph_total<=1.3", "a100"),
                          ("num_gpus=1 rentable=true gpu_name=H200_NVL reliability>=0.98 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=150 dph_total<=4.7", "h200")):
        k = t.count(ancien_f)
        if k > 1:
            raise SystemExit(f"{nom} : filtre {cle} présent {k} fois")
        if k == 1:
            t = t.replace(ancien_f, f[cle]); j.append(f"ok {nom} filtre {cle} = filtre du lanceur v7")
    return t


def textes(racine):
    racine = pathlib.Path(racine); j = []; f = filtres(racine)
    # ---- E2
    t = commun(scelle(racine, "e2"), "e2", f, j)
    t = _appliquer(t, "ligne `commit <COMMIT>` sans « clonage impossible » ;",
                   f"ligne `commit <COMMIT>` sans « clonage impossible » ; **R-1677 : la ligne {CLONAGE_E2} dans les 20 minutes qui suivent la ligne `commit`** "
                   "(clonage réduit : octets_git + octets_arbre attendus ≈ 400 Mo, au plus 600 Mo ; relève secondes, octets et débit au compte rendu ; un clonage qui dépasse 900 s est un attendu manquant grave) ;", "e2 E2-3 ligne CLONAGE", j)
    t = _appliquer(t, "- **Deux attendus manquants de suite → arrêt sans destruction**",
                   "- **R-1677 — clonage lent ou instance silencieuse.** Si la ligne `CLONAGE` n'est pas dans `progres.txt` 20 minutes après la ligne `commit`, ou si "
                   "`surveillance.txt` ne montre aucune ligne neuve de `AMORCE` depuis 20 minutes alors que l'instance est dans l'inventaire : relis `$W/<dossier>/journal-instance.txt` (copie entière, valeurs de clés masquées, "
                   "recopiée à chaque relevé), puis détruis l'instance par son identifiant (`timeout -k 5 120 vastai destroy instance <ID>`) et écris-le comme attendu manquant grave ; message à la mère avec les dernières lignes `AMORCE`.\n"
                   "- **`refus` de l'amorce (R-1677).** L'amorce annonce la cause (« refus : … rien ne part »), puis **attend 180 s** (ligne « refus annoncé : destruction demandée dans 180 s ») avant de demander la destruction : "
                   "relève la ligne de refus dans `progres.txt` pendant ces 180 s. L'instance disparaît ensuite : `surveillance` imprime alors `ARRET mort : instance <ID> absente de l'inventaire …` (code 3) ; "
                   "il n'y a **rien à détruire ni à arrêter** (ne lance aucune commande d'arrêt) ; la cause se lit dans `journal-instance.txt` et sur la branche si elle a été poussée.\n"
                   "- **Deux attendus manquants de suite → arrêt sans destruction**", "e2 clonage lent et refus", j)
    t = _appliquer(t, "ou `ARRET mort` : **destruction par l'identifiant**",
                   "ou `ARRET mort` (processus mort, instance encore dans l'inventaire) : **destruction par l'identifiant**", "e2 ARRET mort précisé", j)
    e2 = t
    # ---- E3
    t = commun(scelle(racine, "e3"), "e3", f, j)
    t = _appliquer(t, "Les préalables 1 à 4 de l'ordre d'E2 scellé (`docs/procedures/ordre-fille-6-t06-e2-v1.md`)",
                   "Les préalables 1 à 4 de l'ordre d'E2 v4 (`brouillons/ordres-t06-e2-e3-v4/ordre-fille-6-t06-e2-v4.md`, scellé à la place de l'ordre v3 par la mère)", "e3 renvoi à E2", j)
    t = _appliquer(t, "`MATERIEL …` ; « tests : N passed in … » (E3-2)",
                   f"`MATERIEL …` ; **R-1677 : la ligne {CLONAGE_E3} dans les 20 minutes qui suivent la ligne `commit`** (au plus 600 Mo ; au-delà de 20 minutes sans elle : relis `journal-instance.txt`, détruis par l'identifiant, "
                   "attendu manquant grave, message) ; « tests : N passed in … » (E3-2)", "e3 ligne CLONAGE", j)
    t = _appliquer(t, "- **Dépassement** : `ARRET depense` (3,5 USD) ou `ARRET mort` → **destruction par l'identifiant**, message",
                   "- **`ARRET mort : instance <ID> absente de l'inventaire` (R-1677)** : l'instance a disparu (refus de l'amorce après 180 s d'attente annoncée, ou destruction par la minuterie) : rien à arrêter ni à détruire ; relève "
                   "les dernières lignes `AMORCE` de `journal-instance.txt` (copie entière à chaque relevé), puis message.\n"
                   "- **Dépassement** : `ARRET depense` (3,5 USD) ou `ARRET mort` (processus mort, instance encore dans l'inventaire) → **destruction par l'identifiant**, message", "e3 ARRET mort", j)
    e3 = t
    out = {"e2": e2, "e3": e3}
    for nom, t in out.items():
        restes = [l for l in t.splitlines() if "lancer_t06_v6.sh" in l or "lancer_t06_v4.sh" in l or "74f59b28" in l or "Scellement" in l]
        if restes:
            raise SystemExit(f"ERREUR {nom} : restes {restes[:2]}")
        for m in re.findall(r"'(num_gpus=1[^']*)'", t):
            if m not in f.values():
                raise SystemExit(f"ERREUR {nom} : filtre hors lanceur : {m}")
        if not all(v in t for v in f.values() if (nom == "e2" or v == f["a100"])) and nom == "e2":
            raise SystemExit("ERREUR e2 : un filtre de lecture manque")
        marq = sorted(set(re.findall(r"<<[A-Z_]+>>", t)))
        if marq != ["<<COMMIT_EPREUVES>>"]:
            raise SystemExit(f"ERREUR {nom} : marqueurs {marq}")
    return out, j


if __name__ == "__main__":
    racine = pathlib.Path(sys.argv[1]); out, j = textes(racine); print("\n".join(j))
    for nom, t in out.items():
        print(nom, hashlib.sha256(t.encode()).hexdigest(), len(t.splitlines()), "lignes")
        if "--ecrire" in sys.argv:
            (racine / f"brouillons/ordres-t06-e2-e3-v4/ordre-fille-6-t06-{nom}-v4.md").write_text(t, encoding="utf-8")
