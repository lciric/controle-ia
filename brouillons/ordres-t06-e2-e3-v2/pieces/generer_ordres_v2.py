#!/usr/bin/env python3
"""Génère les ordres E2 et E3 v2 : ordres v1 + couples de la contre-lecture du lanceur v4 (E2 1 à 6, E3 1 ; le couple 7 d'E2,
relecture par identifiant, est périmé par le lanceur v5 et remplacé) + substitutions vers le lanceur v5. Chaque ancien texte
doit être présent exactement une fois ; journal sur la sortie standard. Aucun .sha256 (la mère scelle)."""
import hashlib, json, sys, pathlib
R = pathlib.Path(sys.argv[1])            # racine du dépôt
V1 = R / "brouillons/ordres-t06-e2-e3-v1"; V2 = R / "brouillons/ordres-t06-e2-e3-v2"
def sha(b): return hashlib.sha256(b).hexdigest()
def appliquer(t, ancien, nouveau, nom):
    n = t.count(ancien)
    if n != 1: sys.exit(f"ERREUR {nom} : ancien présent {n} fois (1 exigé)")
    print(f"ok {nom}"); return t.replace(ancien, nouveau)
E2P = """**Choix de l'offre — lanceur v5 (R-1657, R-577, R-578).** La relecture d'une offre par son identifiant est abandonnée : elle rend
une liste vide sous vastai 1.8.3 et l'identifiant d'une même offre change d'une recherche à l'autre. Tu ne choisis donc **plus**
l'offre à la main : `creation auto` (étape 4) lance elle-même la recherche filtrée (`--storage 150`) **juste avant** la création,
prend la première offre conforme de la liste triée par prix (rang 1), la crée aussitôt et lit le prix dans cette même liste. Les
fichiers `offres-*.json` de cette étape ne servent qu'au contrôle E2-1 (lectures), pas à la création."""
E2_ETAPE4 = ("`env -i … T06_REGISTRE_GO=\"$REGGO\" T06_BRANCHE=essai/t06-e2-v1-a T06_EPUISEMENT_SIMULE_S=2400 T06_TESTS_ATTENDUS=20 "
 "T06_TESTS_ARGS=tests/test_t06_v4_configuration.py,tests/test_t06_v4_familles.py,tests/test_t06_v4_extraire.py bash scripts/lancer_t06_v4.sh creation <OFFRE> course 0 \"$W/a\"`")
E2_ETAPE4_N = ("`env -i … VAST=\"$VAST\" T06_REGISTRE_GO=\"$REGGO\" T06_BRANCHE=essai/t06-e2-v1-a T06_EPUISEMENT_SIMULE_S=2400 T06_TESTS_ATTENDUS=20 "
 "T06_TESTS_ARGS=tests/test_t06_v4_configuration.py,tests/test_t06_v4_familles.py,tests/test_t06_v4_extraire.py bash scripts/lancer_t06_v5.sh creation auto course 0 \"$W/a\"`")
REPRISE = """
**Offre retirée à la création (code 5, v5).** Si `creation` imprime « OFFRE REFUSÉE À LA CRÉATION (retirée ?) … rang suivant : … »
et rend le code 5, la création a été refusée par Vast (offre déjà louée) **et** l'inventaire ne montre aucune instance du
programme : la machine refusée est inscrite dans `$W/a/lancement.txt` (`machine_refusee`) et exclue. Relance **la même commande**
(mêmes variables `T06_*` et `VAST`, mêmes arguments ; la ligne imprimée ne reprend pas les variables, tu les remets) : elle refait
la recherche filtrée et prend le rang suivant. **Trois rangs au plus** (`essai_creation` dans `lancement.txt`) : au quatrième
appel, code 3 « trois essais de création déjà faits », **aucune création** : arrêt et message à la mère. Une instance du
programme dans l'inventaire, ou un résultat sans `success` clair, donne « CRÉATION INCERTAINE » (code 4) : voir ci-dessous, jamais
de nouvel essai."""
def e2():
    t = (V1 / "ordre-fille-6-t06-e2-v1.md").read_text(encoding="utf-8")
    c = json.load(open(V2 / "couples-ordre-e2-v1.json", encoding="utf-8"))
    for i, k in enumerate(c[:6], 1): t = appliquer(t, k["ancien"], k["nouveau"], f"E2 couple {i} (contre-lecture v4)")
    # couple 7 périmé : paragraphe « Choix de l'offre » remplacé en entier
    a = t[t.index("Choix de l'offre de l'instance A : la moins chère"):]
    a = a[:a.index("\n")]
    t = appliquer(t, a, E2P, "E2 remplacement du couple 7 (périmé par la v5)")
    t = appliquer(t, E2_ETAPE4, E2_ETAPE4_N, "E2 étape 4 commande creation auto")
    t = appliquer(t, "→ attendu : `OFFRE CONFORME : id=<OFFRE> prix_carte=… prix_stockage=… …` puis",
                  "→ attendu : `OFFRE CONFORME : id=<identifiant lu dans la liste> rang=1 machine=<machine> prix_carte=… prix_stockage=… …` puis", "E2 attendu étape 4")
    t = appliquer(t, "`GO_ID=GO-2026-11-06-01 timeout -k 10 300 vastai create instance <OFFRE> …`", "`GO_ID=GO-2026-11-06-01 timeout -k 10 300 $VAST create instance <identifiant> …`", "E2 ligne de création")
    t = appliquer(t, "La ligne appelle elle-même `lancer_t06_v4.sh apres-creation`", "La ligne appelle elle-même `lancer_t06_v5.sh apres-creation`", "E2 apres-creation")
    t = appliquer(t, "« CRÉATION INCERTAINE » (code 4) → **aucune seconde création** ; `vastai show instances` (sans `--raw`) ; message à la mère." + "\n",
                  "« CRÉATION INCERTAINE » (code 4) → **aucune seconde création** ; `vastai show instances` (sans `--raw`) ; message à la mère." + REPRISE + "\n", "E2 reprise code 5")
    t = appliquer(t, "`creation` relit l'offre par `search offers \"id=<OFFRE>\" --storage 150 --raw` ; comparaison avec la lecture sans `--storage`",
                  "`creation auto` lit la liste filtrée `--storage 150` (`$W/a/offres.json`) ; comparaison avec la lecture sans `--storage`", "E2-2 comment")
    t = appliquer(t, "= `dph_total` + `storage_total_cost` de la relecture à ± 5 %", "= `dph_total` + `storage_total_cost` de l'offre choisie (`prix_carte` + `prix_stockage` de `lancement.txt`) à ± 5 %", "E2-2 attendu")
    t = appliquer(t, "`vastai --version` = `1.8.3` (sinon arrêt).",
                  "`vastai --version` = `1.8.3` (sinon arrêt). **Outil de location désigné par son chemin** : `VAST=$(command -v vastai)` (chemin absolu, noté au compte rendu) ; toute sous-commande `creation`, `apres-creation` et `surveillance` reçoit `VAST=\"$VAST\"` sous `env -i`, car `env -i` supprime le chemin habituel.", "E2 VAST")
    t = appliquer(t, "refuse un dossier qui existe).", "refuse un dossier qui existe). Les dossiers ne se partagent pas : le décompte des trois rangs (`essai_creation`) est propre à chaque dossier.", "E2 dossiers")
    t = t.replace("lancer_t06_v4.sh controles-epreuve", "lancer_t06_v5.sh controles-epreuve").replace("lancer_t06_v4.sh surveillance", "lancer_t06_v5.sh surveillance").replace("`scripts/lancer_t06_v4.sh`", "`scripts/lancer_t06_v5.sh`").replace("de `scripts/lancer_t06_v4.sh` ou de `vastai`", "de `scripts/lancer_t06_v5.sh` ou de `vastai`")
    t = t.replace("épreuve E2 du lanceur de T0.6 v4 :", "épreuve E2 du lanceur de T0.6 v5 :").replace("— v1 (brouillon)", "— v2 (brouillon)")
    t = t.replace("bash scripts/lancer_t06_v4.sh creation <OFFRE> course 0", "bash scripts/lancer_t06_v5.sh creation auto course 0")
    t = appliquer(t, "Brouillon de la fille 10 (session de développement, Sonnet 5.5)", "Brouillon v2 de la fille 10 (session de développement, Sonnet 5.5 ; remplace la v1, qui reste archivée ; corrige les sept couples de la contre-lecture du lanceur v4 et adopte le lanceur v5, R-1657)", "E2 présentation")
    return t
E3_STEP2 = ("`env -i … timeout 300 vastai search offers 'num_gpus=1 gpu_name=A100_SXM4 rentable=true reliability>=0.98 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 dph_total<=1.30' -o dph_total --storage 150 --raw > \"$W/offres-a100.json\"` ;")
def e3():
    t = (V1 / "ordre-fille-6-t06-e3-v1.md").read_text(encoding="utf-8")
    c = json.load(open(V2 / "couples-ordre-e3-v1.json", encoding="utf-8"))
    t = appliquer(t, c[0]["ancien"], c[0]["nouveau"], "E3 couple 1 (contre-lecture v4)")
    # étape 2 : l'offre n'est plus choisie à la main
    a = t[t.index("**Étape 2 — offre.**"):t.index("**Étape 3 — création.**")]
    n = ("**Étape 2 — estimation (0 USD).** Plus de choix d'offre à la main (lanceur v5, R-1657) : `creation auto` (étape 3) fait la recherche filtrée "
         "(`A100_SXM4`, `--storage 150`, bornes de la configuration) **juste avant** la création et prend la première offre conforme. Estimation avant de "
         "lancer : durée ≤ 2 h 30 à ≤ 1,3 USD/h + stockage < 3,5 USD ; après `creation`, **si `prix_carte + prix_stockage` × 3 h + forfait de téléchargement > 3,5 USD "
         "(valeurs imprimées par `OFFRE CONFORME`), n'exécute pas la ligne de création** ; relance `creation auto` seulement si la sortie propose un rang suivant "
         "(code 5) ; sinon arrêt et message. Pas de `vastai search` à la main pour E3.\n\n")
    t = t.replace(a, n); print("ok E3 étape 2 réécrite")
    t = appliquer(t, "`env -i … T06_REGISTRE_GO=\"$REGGO\" T06_BRANCHE=essai/t06-e3-v1 T06_TESTS_ATTENDUS= bash scripts/lancer_t06_v4.sh creation <OFFRE> course 0 \"$W/e3\"`",
                  "`env -i … VAST=\"$VAST\" T06_REGISTRE_GO=\"$REGGO\" T06_BRANCHE=essai/t06-e3-v1 T06_TESTS_ATTENDUS= bash scripts/lancer_t06_v5.sh creation auto course 0 \"$W/e3\"`", "E3 étape 3 commande")
    t = appliquer(t, "Attendu : `OFFRE CONFORME …`, puis la ligne de création `GO_ID=GO-2026-11-06-01 timeout -k 10 300 vastai create instance <OFFRE> …",
                  "Attendu : `OFFRE CONFORME : id=… rang=1 machine=… …`, puis la ligne de création `GO_ID=GO-2026-11-06-01 timeout -k 10 300 $VAST create instance <identifiant> …", "E3 attendu étape 3")
    t = appliquer(t, "Attendu : `CRÉÉE : instance <ID> …`. Incertain → aucune seconde création, message.",
                  "Attendu : `CRÉÉE : instance <ID> …`. **Code 5** (« OFFRE REFUSÉE À LA CRÉATION », aucune instance dans l'inventaire) → relance la même commande `creation auto` (mêmes variables, `VAST` compris) : rang suivant, **trois rangs au plus**, puis code 3 : arrêt et message. « CRÉATION INCERTAINE » (code 4) → aucune seconde création, message.", "E3 reprise code 5")
    t = appliquer(t, "Les préalables 1 à 4 de l'ordre d'E2 (", "Les préalables 1 à 4 de l'ordre d'E2 v2 (", "E3 renvoi")
    t = t.replace("lancer_t06_v4.sh controles-epreuve", "lancer_t06_v5.sh controles-epreuve").replace("lancer_t06_v4.sh surveillance", "lancer_t06_v5.sh surveillance")
    t = t.replace("épreuve E3 du lanceur de T0.6 v4 :", "épreuve E3 du lanceur de T0.6 v5 :").replace("— v1 (brouillon)", "— v2 (brouillon)")
    t = appliquer(t, "Brouillon de la fille 10 (session de développement, Sonnet 5.5)", "Brouillon v2 de la fille 10 (session de développement, Sonnet 5.5 ; remplace la v1, archivée ; corrige le couple de la contre-lecture du lanceur v4 et adopte le lanceur v5, R-1657)", "E3 présentation")
    t = appliquer(t, "`surveillance` (`ARRET depense` à 3,5 USD).", "`surveillance` (`ARRET depense` à 3,5 USD ; texte de la v5 : « dépense cumulée ≥ plafond de la configuration »). `VAST=\"$VAST\"` (chemin absolu de `vastai`) sous `env -i` pour `creation`, `apres-creation`, `surveillance`.", "E3 VAST")
    return t
for nom, f in (("e2", e2), ("e3", e3)):
    t = f()
    restes = [l for l in t.splitlines() if "lancer_t06_v4.sh" in l or "<OFFRE>" in l]
    if restes: sys.exit(f"ERREUR {nom} : restes v4/<OFFRE> : {restes[:2]}")
    p = V2 / f"ordre-fille-6-t06-{nom}-v2.md"; p.write_text(t, encoding="utf-8")
    print(nom, p.name, sha(p.read_bytes()), len(t.splitlines()), "lignes")
