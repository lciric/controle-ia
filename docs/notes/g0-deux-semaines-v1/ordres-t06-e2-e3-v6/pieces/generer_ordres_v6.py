"""Générateur des ordres E3 v6 et E2 v5 (fille 10, R-1696, R-1697 ; R12 : nouveau nom, le générateur v5 reste tel quel).
Départ : les ordres SCELLÉS EN VIGUEUR lus dans `refs/remotes/origin/main` (E3 v5 `db0ad520…`, E2 v4 `4c1113cd…`), jamais un brouillon.
Chaque remplacement doit trouver son texte exactement une fois (sinon arrêt) : aucune modification silencieuse.
    python3 generer_ordres_v6.py RACINE_DU_DEPOT [--ecrire]
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

E3_V5_PREFIXE = "db0ad520"
E2_V4_PREFIXE = "4c1113cd"
COMMIT_V5 = "1921fc3ea3720fb96402c9ffca4fbec861a7eacf"


def _git_show(racine, chemin):
    return subprocess.run(["git", "-C", str(racine), "show", f"refs/remotes/origin/main:{chemin}"], capture_output=True, text=True, check=True).stdout


def _scelle(racine, chemin, prefixe):
    t = _git_show(racine, chemin)
    h = hashlib.sha256(t.encode()).hexdigest()
    if not h.startswith(prefixe):
        raise SystemExit(f"ERREUR : {chemin} a pour empreinte {h[:12]}, attendu {prefixe}")
    return t, h


def _un(t, ancien, nouveau, nom, journal):
    n = t.count(ancien)
    if n != 1:
        raise SystemExit(f"ERREUR remplacement « {nom} » : {n} occurrence(s) au lieu d'une")
    journal.append(f"ok {nom}")
    return t.replace(ancien, nouveau)


def _tous(t, ancien, nouveau, nom, journal, minimum=1):
    n = t.count(ancien)
    if n < minimum:
        raise SystemExit(f"ERREUR remplacement « {nom} » : {n} occurrence(s), au moins {minimum} attendue(s)")
    journal.append(f"ok {nom} ({n})")
    return t.replace(ancien, nouveau)


def filtres(racine):
    sys.path.insert(0, str(pathlib.Path(racine) / "src"))
    from controle_ia.t06 import session_v7 as s7, session_v8 as s8
    n = pathlib.Path(racine) / "docs/notes/g0-deux-semaines-v1"
    e3 = json.loads((n / "config-t06-epreuve-e3-v3.json").read_text(encoding="utf-8"))
    e3v2 = json.loads((n / "config-t06-epreuve-e3-v2.json").read_text(encoding="utf-8"))
    e2 = json.loads((n / "config-t06-epreuve-e2-v2.json").read_text(encoding="utf-8"))
    return {"a100": s8.filtre_recherche(e3, "course"), "a100_ancien": s7.filtre_recherche(e3v2, "course"),
            "modeste": s8.filtre_recherche(e2, "course"), "modeste_ancien": s7.filtre_recherche(e2, "course")}


def e3_v6(racine):
    j = []
    t, h = _scelle(racine, "docs/procedures/ordre-fille-6-t06-e3-v5.md", E3_V5_PREFIXE)
    t = t[:t.index("\n## Scellement (session mère")].rstrip("\n") + "\n"
    f = filtres(racine)
    t = _un(t, "— v5, scellé (R-1693)", "— v6 (brouillon)", "titre", j)
    a = t[t.index("Brouillon v5 de la fille 10"):]
    a = a[:a.index("Français, sans sigle")]
    n = ("Brouillon v6 de la fille 10 (session de développement, Sonnet 5.5 ; issu de l'ordre v5 scellé par la mère (R-1693), dont il reprend le texte ; adopte l'amorce v7 et le lanceur v9 : "
         "correctifs de la contre-lecture Opus de la v8 (R-1693), clause de mémoire de carte (R-1694, R-1695), plafond d'E3 porté à 4,3 USD (R-1696, R-1697)), pour contre-lecture et scellement par la session mère\n"
         "`session_01Qi7Gr6NLmhhAcdmnACBC7G`. **Non scellé.** Ce texte devient un ordre seulement une fois scellé (la mère écrit le `.sha256` et remplit le seul marqueur `<<COMMIT_EPREUVES>>`). ")
    t = _un(t, a, n, "présentation", j)
    t = _tous(t, COMMIT_V5, "<<COMMIT_EPREUVES>>", "commit d'épreuve", j)
    t = _tous(t, "lancer_t06_v8.sh", "lancer_t06_v9.sh", "lanceur (nom)", j)
    t = _tous(t, "lanceur de T0.6 v8", "lanceur de T0.6 v9", "lanceur (titre)", j)
    t = _tous(t, "lanceur v8", "lanceur v9", "lanceur (texte)", j)
    t = _tous(t, "amorce v6", "amorce v7", "amorce", j)
    t = _tous(t, "essai/t06-e3-v3", "essai/t06-e3-v4", "branche (R12)", j)
    t = _tous(t, "config-t06-epreuve-e3-v2.json", "config-t06-epreuve-e3-v3.json", "configuration v3", j)
    # plafond (R-1696, R-1697)
    t = _un(t, "**Plafonds : E3 ≤ 3,5 USD ; E2 ≤ 1,5 USD ; cumul ≤ 5 USD.**", "**Plafonds : E3 ≤ 4,3 USD (R-1696, R-1697) ; E2 a coûté 0,600 USD ; cumul ≤ 4,9 USD (GO de 5 USD, marge de 0,10).**", "plafonds", j)
    t = _un(t, "(`plafond_usd = 3.5`)", "(`plafond_usd = 4.3` ; configuration v3, seule différence avec la v2 : ce plafond)", "plafond de la configuration", j)
    t = _un(t, "`controles-epreuve` (3,5 seulement pour E3)", "`controles-epreuve` (plafond lu dans la configuration, accepté s'il tient dans le reste du GO : plafond + dépense réelle et finale des autres épreuves, donnée par `T06_DEPENSE_EPREUVES_ANTERIEURES_USD`, ≤ 4,9 ; `creation` relit la même borne)", "controles-epreuve", j)
    t = _un(t, "comparée à 3,5 ;", "comparée à 4,3 ;", "creation", j)
    t = _un(t, "(`ARRET depense` à 3,5 USD ;", "(`ARRET depense` à 4,3 USD ;", "surveillance", j)
    t = _un(t, "+ 3,5 ≤ 4,9`, E2", "+ 4,3 ≤ 4,9`, E2", "condition d'E2", j)
    t = _un(t, "si E2 a dépensé plus de 1,4 USD,", "si E2 a dépensé plus de 0,6 USD (4,9 − 4,3),", "seuil d'E2", j)
    t = _un(t, "`go_id = GO-2026-11-06-01`, `plafond_usd = 3.5`,", "`go_id = GO-2026-11-06-01`, `plafond_usd = 4.3`,", "section 3 plafond", j)
    t = _un(t, "carte `A100 SXM4` (80 Go) à 1,30 USD/h au plus,", "carte `A100 SXM4` (80 Go ; clause `gpu_ram>=78` dans la requête, **en Go** : R-1694, R-1695) à 1,30 USD/h au plus, fiabilité ≥ 0,98 (gardée, R-1696),", "carte", j)
    t = _un(t, "dépense d'E3 ≤ 3,5 USD ; cumul avec E2 ≤ 5 USD", "dépense d'E3 ≤ 4,3 USD ; cumul avec E2 ≤ 4,9 USD (GO de 5 USD)", "E3-11", j)
    t = _un(t, "`ARRET depense` (3,5 USD)", "`ARRET depense` (4,3 USD)", "dépassement", j)
    t = _un(t, "stockage < 3,5 USD ;", "stockage < 4,3 USD ;", "estimation", j)
    t = _un(t, "> 3,5 USD (valeurs imprimées par `OFFRE CONFORME`)", "> 4,3 USD (valeurs imprimées par `OFFRE CONFORME` ; depuis la v9 `prix_carte + prix_stockage` = `dph_total`, le stockage n'est plus compté deux fois, R-1692)", "règle des 3 heures", j)
    # étape 1
    t = _un(t, "`env -i … T06_BRANCHE_CODE=prep/t06-lanceur-v2 T06_REGISTRE_GO=\"$REGGO\" T06_BRANCHE=essai/t06-e3-v4 bash scripts/lancer_t06_v9.sh controles-epreuve",
            "`env -i … T06_BRANCHE_CODE=prep/t06-lanceur-v2 T06_REGISTRE_GO=\"$REGGO\" T06_DEPENSE_EPREUVES_ANTERIEURES_USD=<dépense réelle et finale d'E2 en USD, 0.600 si elle est inchangée> T06_BRANCHE=essai/t06-e3-v4 bash scripts/lancer_t06_v9.sh controles-epreuve", "étape 1 commande", j)
    t = _un(t, "`CONTRÔLES D'ÉPREUVE CONFORMES … (plafond de l'épreuve 3.5 USD sur 5) ; mode reel ; …`", "`CONTRÔLES D'ÉPREUVE CONFORMES … (plafond de l'épreuve 4.3 USD sur 5 ; plafond d'épreuve 4.3 + dépense antérieure <A> = <somme> ≤ 4.9) ; mode reel ; …` (une dépense antérieure qui ferait dépasser 4,9, ou absente, donne le code 2 : arrêt)", "étape 1 attendu", j)
    # filtre de lecture = filtre du lanceur v9 (avec gpu_ram en Go)
    t = _un(t, "'" + f["a100_ancien"] + "'", "'" + f["a100"] + "'", "filtre de lecture", j)
    trouves = re.findall(r"'(num_gpus=1[^']*)'", t)
    if trouves != [f["a100"]]:
        raise SystemExit(f"ERREUR filtre de lecture ≠ filtre du lanceur : {trouves} / {f['a100']}")
    t = _un(t, "puis la même recherche **sans** la clause `cuda_max_good>=13.0` (nombre d'offres, minimum) ;",
            "puis la même recherche **sans** la clause `cuda_max_good>=13.0` (nombre d'offres, minimum), et **sans** la clause `gpu_ram>=78` (nombre d'offres, plus petite `gpu_ram` en Mo : la clé brute est en Mo, la clause en Go ; avec la clause, la plus petite attendue est ≥ 79 872 Mo ; les A100 de 40 Go, 40 960 Mo, doivent disparaître) ;", "lecture sans clauses", j)
    t = _un(t, "une erreur de syntaxe, aucune offre, ou une offre sous 13,0 avec la clause → arrêt et message, sans création.",
            "une erreur de syntaxe, aucune offre, une offre sous 13,0 avec la clause cuda, ou une offre de moins de 79 872 Mo de `gpu_ram` avec la clause mémoire → arrêt et message, sans création.", "arrêt de la lecture", j)
    # étape 5 : trois commits
    t = _un(t, "**Ne lis rien d'autre sous `diag/`.**",
            "**Ne lis rien d'autre sous `diag/`.** Commits attendus (`git log --format=%s`, R-1692, essai E2-3) : après le commit de base, **trois** commits — « résultats et données légères », « sous-ensemble d'activations en morceaux », « traces de l'instance (fin) » ; la poussée initiale (avant l'installation) ne crée aucun commit, et tu n'en fabriques aucun. Un commit « journal de l'instance (<motif>) » avec `traces/consignation-…/journal-consignation.txt` n'apparaît que si la minuterie a consigné (échéance, dépense épuisée) : si c'est le cas, relève-le.", "trois commits", j)
    # ARRET mort : conduite sur une réponse sans id
    d = t[t.index("**une réponse JSON sans champ `id`"):]
    d = d[:d.index("message à la mère) ;") + len("message à la mère) ;")]
    nv = ("**depuis la v9 (R-1693), une réponse sans champ `id` (par exemple `{\"success\": false, \"error\": …}`), un texte d'erreur 500 ou un identifiant qui contient « 404 » ne sont plus lus comme « introuvable »** "
          "(`session_v8.instance_seule` : seuls un statut 404 accompagné d'un message exact — « not found », « no such instance », « does not exist » —, un texte de ce sens exact, ou une liste NON vide qui ne contient pas l'identifiant, établissent l'absence ; "
          "le texte réel de Vast pour une instance détruite n'est pas connu : il sera relevé) ; un tel relevé donne une ALERTE et, au troisième de suite, `ARRET inventaire`. Par prudence, si tu en vois une : l'instance est réputée vivante et sans surveillance ; "
          "refais la vérification toutes les 2 minutes, au plus 20 minutes, détruis-la par son identifiant dès qu'elle répond, et **recopie au compte rendu le texte exact** que `show instance` rend pour une instance détruite (sans valeur de clé) (aucune absence établie au bout de 20 minutes : message à la mère) ;")
    t = _un(t, d, nv, "conduite sur réponse sans id", j)
    t = _un(t, "- **Liste d'inventaire vide, illisible ou en échec (R-1683)**", "- **Masquage (R-1693)** : si le masquage des clés échoue, le lanceur imprime « ALERTE masquage en échec … : relevé écarté » et ne laisse ni copie vidée ni fichier brut ; les inventaires de `creation` et `apres-creation` sont masqués avant d'être écrits. Une ALERTE de ce genre trois fois de suite : arrête la surveillance, vérifie à la main, message à la mère.\n- **Échéance avant la fin du run (R-1692)** : la minuterie dépose sur la branche un commit « journal de l'instance (échéance) » (`traces/consignation-…/journal-consignation.txt` : motif, heure, dernière ligne du journal, 400 dernières lignes ; et `t06-minuterie.log` avec la ligne « ÉCHÉANCE … atteinte (C14) ») avant la destruction ; relève-le.\n- **Liste d'inventaire vide, illisible ou en échec (R-1683)**", "masquage et échéance", j)
    marq = sorted(set(re.findall(r"<<[A-Z_]+>>", t)))
    if marq != ["<<COMMIT_EPREUVES>>"]:
        raise SystemExit(f"ERREUR marqueurs {marq}")
    for reste in ("lancer_t06_v8", "essai/t06-e3-v3", "1921fc3e", "Scellement", "plafond_usd = 3.5"):
        if reste in t:
            raise SystemExit(f"ERREUR reste « {reste} »")
    return t, j, h


def e2_v5(racine):
    """Ordre de REJEU d'E2-6 (et relecture du prix d'E2-2), une seule instance D, plafond 0,10 USD (configuration E2 v3), départ : E2 v4 scellé en vigueur."""
    j = []
    v4, h = _scelle(racine, "docs/procedures/ordre-fille-6-t06-e2-v4.md", E2_V4_PREFIXE)
    f = filtres(racine)
    ent = v4[:v4.index("\n## 1. Cadre")]
    ent = _un(ent, "épreuve E2 du lanceur de T0.6 v7 : interface de Vast, trois redémarrages, minuterie, destruction — v4, scellé (R-1683), révision 2 (R-1685)",
              "rejeu d'E2-6 du lanceur de T0.6 v9 (« E2-6 v1 ») : journal de l'instance sur la branche quand l'échéance tombe avant la fin du run, et relecture du prix d'E2-2 — v1 (brouillon)", "titre", j)
    a = ent[ent.index("Brouillon v4 de la fille 10"):]
    a = a[:a.index("Français, sans sigle")]
    ent = _un(ent, a, ("Brouillon v1 de la fille 10 (session de développement, Sonnet 5.5 ; issu de l'ordre E2 v4 scellé par la mère (R-1683, R-1685), dont il reprend le cadre, les interdits et le registre des GO ; "
                       "**ne rejoue que E2-6 (échéance avant la fin du run) et relit le prix d'E2-2**, avec l'amorce v7 et le lanceur v9 (R-1692)), pour contre-lecture et scellement par la session mère\n"
                       "`session_01Qi7Gr6NLmhhAcdmnACBC7G`. **Non scellé.** Ce texte devient un ordre seulement une fois scellé (la mère écrit le `.sha256` et remplit le seul marqueur `<<COMMIT_EPREUVES>>`). "), "présentation", j)
    interdits = v4[v4.index("- **Interdits** : afficher"):v4.index("- **Clés, par leur nom seulement**")]
    cles = v4[v4.index("- **Clés, par leur nom seulement**"):v4.index("\n\n## 2. Ce qu'E2 prouve")]
    cles = _tous(cles, "lancer_t06_v7.sh", "lancer_t06_v9.sh", "lanceur dans les clés", j)
    reg = v4[v4.index("**Registre des GO qui fait foi (R-1626).**"):]
    reg = reg[:reg.index("\n")]
    surv = v4[v4.index("- **R-1677 — clonage lent ou instance silencieuse.**"):v4.index("- **Deux attendus manquants de suite")]
    surv = _un(surv, "(le lanceur v7 lit un inventaire vide comme une absence)", "(depuis la v8, un inventaire vide n'est plus lu comme une absence ; depuis la v9, une réponse d'erreur sans `id` non plus)", "surveillance (inventaire vide)", j)
    corps = f"""
## 1. Cadre

- **Pourquoi ce rejeu.** À E2 (7 novembre, R-1692), l'instance C a atteint son échéance **pendant l'installation** (hôte lent, clonage de 125 s) : aucune consignation n'a été poussée, le journal de Vast a disparu avec l'instance, les lignes « ÉCHÉANCE … (C14) » et « consigné (échéance) » n'ont pas été observées : E2-6 est **non exercé**. L'amorce v7 (R-1692) dépose désormais sur la branche, quand la consignation vient de la minuterie, un commit « journal de l'instance (échéance) » (`traces/consignation-…/journal-consignation.txt` et `t06-minuterie-fin.txt`). Ce rejeu le vérifie sur une machine réelle.
- **GO : `GO-2026-11-06-01`** (5 USD pour E2 et E3 cumulés, échéance 10 novembre 2026). `GO_ID=GO-2026-11-06-01` en tête de toute création (garde de calcul).
- **Plafond du rejeu : 0,10 USD** (configuration `config-t06-epreuve-e2-v3.json`, seule différence avec la v2 : `plafond_usd = 0.1`). **À jouer APRÈS E3**, et seulement si `dépense réelle et finale d'E2 (0,600) + dépense réelle et finale d'E3 + 0,10 ≤ 5` (GO de 5 USD), **au plus tard le 10 novembre 2026** (fin du GO). La borne du lanceur est volontairement un peu plus stricte (`plafond + dépenses des autres épreuves ≤ 4,9`, marge de 0,10 USD) : si elle refuse (code 2) alors que la condition ci-dessus tient, message à la mère, qui tranche. Le rejeu n'est pas lancé si E3 n'est pas terminée.
- **Aucune donnée décisive** : tâches synthétiques, mode jouet, aucun préenregistrement, aucune sonde décisive lue. Branche poussée : `essai/t06-e26-v1` seulement (**jamais `calcul/…`, jamais `main`, jamais `lciric/controle-ia`**).
{interdits}{cles}

## 2. Ce que ce rejeu prouve et l'attendu de chaque contrôle

| n° | contrôle | où se lit | attendu |
|---|---|---|---|
| E2-2 | prix relu avec le stockage de 150 Go (correction R-1692 : le stockage n'est plus compté deux fois) | `lancement.txt` (`prix_carte`, `prix_stockage`) ; `vastai show instance <ID> --raw` après la création | `prix_carte + prix_stockage` = `dph_total` de l'offre (aucun ajout) ; prix horaire réel de l'instance (`dph_total` de `show instance`, ou facture/heures) égal à cette somme à ± 3 % ; relève les trois valeurs |
| E2-6 | échéance avant la fin du run (C14), journal sur la branche | `vastai logs <ID>` ; branche `essai/t06-e26-v1` | à l'échéance, la minuterie journalise « ÉCHÉANCE … atteinte (C14) » puis « consigné (échéance) : code 0 » puis « instance <ID> détruite » ; **la branche porte un commit « T0.6 : journal de l'instance (échéance) »** avec `traces/consignation-…/journal-consignation.txt` (motif « échéance », heure, dernière ligne du journal avant la consignation, 400 dernières lignes) et `t06-minuterie-fin.txt` (ligne « ÉCHÉANCE … atteinte (C14) ») et `empreintes.sha256` ; l'étape atteinte (installation, clonage, tests) se lit dans la dernière ligne ; aucun « ERREUR DE CHAÎNE » ; aucun autre commit fabriqué |
| E2-9 | destruction par l'identifiant | inventaire ; `t06-minuterie-fin.txt` | l'instance disparaît de l'inventaire dans les 10 minutes qui suivent l'échéance ; `DELETE` en HTTP 2xx ; jamais de destruction par motif |
| E2-10 | facture | relevé de facturation Vast | dépense du rejeu ≤ 0,10 USD ; écart avec l'estimation de `surveillance` écrit |

**Échéance (écart écrit)** : la consigne d'une échéance « 4 minutes après DEMARRAGE » ne peut pas s'exprimer à la création (l'échéance est un instant absolu fixé avant le démarrage) et le lanceur refuse une échéance à moins de 600 s : on pose donc maintenant + 600 s, ce qui tombe pendant l'installation ou les essais (la suite complète est jouée exprès).

**Si la machine est rapide** et que la suite d'essais n'est pas coupée à l'échéance (le run se termine avant 600 s) : le rejeu n'a pas exercé E2-6 ; écris-le, détruis l'instance par son identifiant, message à la mère (le rejeu n'est pas recommencé sans son accord). La suite complète est jouée volontairement (`T06_TESTS_ATTENDUS` vide) pour que l'échéance tombe pendant l'installation ou les essais.

## 3. Pièces et préalables (vérifie chacun ; un manquant → arrêt et message)

1. Dépôt : `git clone https://github.com/lciric/controle-ia-travail.git` (privé) ; ne **jamais** pousser vers `lciric/controle-ia`. `COMMIT=<<COMMIT_EPREUVES>>` (commit de la mère qui contient le code du lanceur v9, l'amorce v7 et la configuration `config-t06-epreuve-e2-v3.json` **avec leurs `.sha256`**). `git fetch origin refs/heads/prep/t06-lanceur-v2:refs/remotes/origin/prep/t06-lanceur-v2` (**refspec explicite, jamais un `git fetch` nu**) ; `git checkout -q "$COMMIT"` ; `git merge-base --is-ancestor "$COMMIT" refs/remotes/origin/prep/t06-lanceur-v2` (code 0 exigé).
2. Environnement : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ; `export PYTHONPATH=src`. `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; `python -m controle_ia.scellement verifier-arbre .`.
3. `vastai --version` = `1.8.3` (sinon arrêt). `VAST=$(command -v vastai)` (chemin absolu, noté au compte rendu) ; toute sous-commande `creation`, `apres-creation` et `surveillance` reçoit `VAST="$VAST"` sous `env -i`. Les variables `VAST_API_KEY` et `CONTROLE_IA_GITHUB_TOKEN` existent (test de présence sans affichage). Aucune instance d'étiquette `t06-e2` ni `t06-e3` sur le compte.
4. Dossier de travail neuf (R12) : `W=$(mktemp -d)` ; dossier de contrôles `$W/d`. Configuration : `docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v3.json` et `donnees/t06-epreuve-e2/taches-{{evaluation,distillation}}.json` au commit ; `go_id = GO-2026-11-06-01`, `plafond_usd = 0.1`, `mode = jouet`, étiquette `t06-e2`, disque 150 Go, carte modeste (`RTX 4090`, 20 Go ou plus, clause `gpu_ram>=19` en Go, ≤ 0,60 USD/h), mémoire vive ≥ 32 000 Mo, cœurs effectifs ≥ 8.

## 4. Étapes

{reg}

Variables : `CFG=docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v3.json` ; `T06_BRANCHE_CODE=prep/t06-lanceur-v2` ; `AUTRES` = dépense réelle et finale des autres épreuves du GO en USD (0.600 pour E2 du 7 novembre, plus la dépense réelle et finale d'E3).

**Étape 1 — contrôles.**
`env -i … T06_BRANCHE_CODE=prep/t06-lanceur-v2 T06_REGISTRE_GO="$REGGO" T06_DEPENSE_EPREUVES_ANTERIEURES_USD="$AUTRES" T06_BRANCHE=essai/t06-e26-v1 bash scripts/lancer_t06_v9.sh controles-epreuve "$W/d" "$COMMIT" "$CFG"`
→ attendu : code 0, `CONTRÔLES D'ÉPREUVE CONFORMES … (plafond de l'épreuve 0.1 USD sur 5 ; plafond d'épreuve 0.1 + dépense antérieure <AUTRES> = <somme> ≤ 4.9) ; mode jouet ; …`. Tout autre code → arrêt et message.

**Étape 2 — lecture de contrôle (0 USD).** `env -i … timeout 300 vastai search offers '{f["modeste"]}' -o dph_total --storage 150 --raw` (**ce filtre est exactement celui de `creation auto`**) : relève le nombre d'offres, le prix de rang 1 (`dph_total`, `storage_total_cost`), la plus petite `gpu_ram` en Mo (≥ 19 456 attendue).

**Étape 3 — création de l'instance D.**
`env -i … VAST="$VAST" T06_REGISTRE_GO="$REGGO" T06_BRANCHE=essai/t06-e26-v1 T06_TESTS_ATTENDUS= bash scripts/lancer_t06_v9.sh creation auto course 0 "$W/d" "$(( $(date -u +%s) + 600 ))"` : `T06_TESTS_ATTENDUS` vide (suite complète : le run est long) ; `T06_TESTS_ARGS` **non** défini ; sixième argument = l'échéance, **maintenant + 600 s** (minimum accepté). Attendu : `OFFRE CONFORME : id=… rang=1 machine=… prix_carte=… prix_stockage=… …`, puis la ligne de création `GO_ID=GO-2026-11-06-01 timeout -k 10 300 $VAST create instance <identifiant> … -e ECHEANCE_UTC_S=<échéance> …` sans valeur de clé. Estimation : (prix de la carte + du stockage) × 15 minutes + forfait de téléchargement (1 Go) doit rester **< 0,10 USD** (≈ 0,09 à 0,36 USD/h) ; sinon n'exécute pas la ligne de création. **Exécute-la une fois, telle quelle** (`bash -c '<ligne>'` sous le même `env -i …`). Attendu : `CRÉÉE : instance <ID> …`. Code 5 : relance la même commande (rang suivant, trois rangs au plus) ; « CRÉATION INCERTAINE » (code 4) : aucune seconde création, message.

**Étape 4 — surveillance et lecture de la fin (E2-6, E2-9).**
`env -i … INTERVALLE=60 bash scripts/lancer_t06_v9.sh surveillance <ID> "$W/d"` en tâche de fond. Relève, toutes les 2 minutes, la dernière ligne `AMORCE`/`PROGRES` (étape atteinte à l'échéance). À l'échéance (+ 600 s) : « ÉCHÉANCE … atteinte (C14) », « consigné (échéance) : code 0 », « instance <ID> détruite » (`vastai logs`, `journal-instance.txt`) ; l'instance disparaît ensuite : `surveillance` imprime `ARRET mort` (code 3) — **attendu ici**, vérifie par `show instance <ID> --raw` que la réponse dit « introuvable » (recopie le texte exact) ; si elle répond, détruis par l'identifiant. Si l'instance subsiste 15 minutes après l'échéance : `timeout -k 5 120 vastai destroy instance <ID>` (**par l'identifiant**) et écris-le comme attendu manquant.
Relève aussi le prix réel (E2-2) : `vastai show instance <ID> --raw` pendant la vie de l'instance (`dph_total`).

**Étape 5 — lecture de la branche (E2-6).**
`git clone --branch essai/t06-e26-v1 --single-branch https://github.com/lciric/controle-ia-travail.git "$W/branche-d"` (par le même moyen que le clone du préalable 1) ; `git log --format=%s` ; liste des fichiers de `traces/consignation-*/` ; lis `journal-consignation.txt` et `t06-minuterie-fin.txt` (ils ne portent aucun résultat) : relève le motif, l'heure, la dernière ligne du journal avant la consignation (étape atteinte) et la ligne « ÉCHÉANCE … atteinte (C14) ». **Ne lis rien d'autre sous `diag/` ni `donnees/`.**

**Étape 6 — nettoyage et facture (E2-10).**
`vastai show instances --raw` filtré sur l'étiquette `t06-e2` : aucune instance ; toute instance restante est détruite par son identifiant. Relevé de facturation (même commande qu'à E2) : dépense du rejeu ≤ 0,10 USD.

## 5. Surveillance, cadence et arrêts

- Cadence : lecture de `surveillance.txt` toutes les 2 minutes pendant que l'instance tourne ; aucune instance laissée sans surveillance.
{surv}- **Deux attendus manquants de suite → arrêt sans destruction** et message à la mère (ligne attendue, ligne obtenue, identifiant, heure). Un attendu manquant isolé est écrit au compte rendu.
- **Dépassement** : `ARRET depense` (0,10 USD) : destruction par l'identifiant, puis message. Aucune seconde création après « CRÉATION INCERTAINE » ; aucune création après le 9 novembre (dernier jour de création de la configuration).
- Si `git` refuse une poussée (jeton), ne réessaie pas plus de trois fois ; message à la mère.

## 6. Compte rendu (message à la mère, aussi `$W/compte-rendu-e2-rejeu.md`, sans valeur de clé)

Identifiant, offre, carte et prix relevés (carte, stockage, total, prix réel), heures de création, d'échéance et de destruction, code de sortie de l'amorce, branche `essai/t06-e26-v1` et son dernier commit. Table E2-2, E2-6, E2-9, E2-10 : attendu, obtenu, conforme / non conforme, ligne exacte à l'appui ; **l'étape atteinte à l'échéance** ; le texte exact que `show instance` rend pour une instance détruite. Montant relevé. Attendus manquants et arrêts. Aucune valeur de clé. Ensuite, reste en attente.
"""
    t = ent.rstrip("\n") + "\n" + corps
    t = _tous(t, "lancer_t06_v7.sh", "lancer_t06_v9.sh", "lanceur (nom)", j, 0)
    marq = sorted(set(re.findall(r"<<[A-Z_]+>>", t)))
    if marq != ["<<COMMIT_EPREUVES>>"]:
        raise SystemExit(f"ERREUR marqueurs {marq}")
    for reste in ("lancer_t06_v7", "amorce v5", "Scellement", "quatre commits", "essai/t06-e2-v3"):
        if reste in t:
            raise SystemExit(f"ERREUR reste « {reste} »")
    return t, j, h


def main():
    racine = pathlib.Path(sys.argv[1])
    t, j, h = e3_v6(racine)
    t2, j2, h2 = e2_v5(racine)
    sortie = {"e3": t, "e2": t2}
    print("\n".join(j + j2)); print("ordres scellés E3 v5", h, "E2 v4", h2)
    for nom, texte in sortie.items():
        print(nom, hashlib.sha256(texte.encode()).hexdigest(), len(texte.splitlines()), "lignes")
        if "--ecrire" in sys.argv:
            (racine / f"docs/notes/g0-deux-semaines-v1/ordres-t06-e2-e3-v6/ordre-fille-6-t06-{"e3" if nom == "e3" else "e2-6"}-v{6 if nom == "e3" else 1}.md").write_text(texte, encoding="utf-8")


if __name__ == "__main__":
    main()
