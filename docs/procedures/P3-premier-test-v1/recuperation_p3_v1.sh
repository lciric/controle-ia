#!/usr/bin/env bash
# Contrôles de récupération du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202 ; préenregistrement
# prereg/P3-premier-test-i-a-v1.md), v1, brouillon 3 (contre-lecture R2 de la chaîne traitée : CH-05, CH-06, CH-07, CH-18 ;
# brouillon 4 du texte : quatre conditions, scores par jeton des sondes principales et textes des actions gardés ;
# relecture courte traitée : textes cherchés aussi dans les chaînes JSON décodées, fenêtres d'un seul caractère répété
# ignorées, RCh-07), avant
# toute fusion et avant toute proposition de destruction de l'instance ; déclinés de la récupération des notations
# refaites du pilote de T0.5 (docs/procedures/notations-T0.5-v2/recuperation_notations_v1.sh) sous un nom nouveau (R12).
# Clone propre du dépôt de travail ; rien n'est fusionné ni poussé ici. Aucune valeur de jeton, aucun texte d'action, de
# consigne ni de donnée générique n'est affiché ; le motif d'un arrêt s'affiche borné à 200 caractères (CH-18).
# Ce qui est contrôlé : ascendance (S ancêtre) ; ajouts seulement, aux seuls chemins permis (manifeste du run ; ses
# résultats : sondes figées, épisodes, résumé ou arrêt ; ses données : sondes figées sans les matrices de Mahalanobis,
# scores par action, scores par jeton des sondes principales, textes des actions, leurs sceaux et le sceau du fichier
# complet des sondes, resté sur l'instance ; traces p3-*) ; un seul run « …-p3-reel » ; auteurs ; sceaux ; résultats
# rattachés au manifeste de CE run ; chaque fichier de données présent vérifié par son sceau compagnon et rattaché à
# l'empreinte écrite dans son résultat et dans le résumé (CH-06 b) ; manifeste et citations (commit, préenregistrement,
# configuration, entropie et graines des clés de P3, mode, décisif, dépôt propre, versions égales à celles du pilote) ;
# issue (résumé ou arrêt, un seul), rattachée aux citations ; pièces attendues selon l'issue, dans les deux sens (toute
# donnée présente a son résultat, CH-06 a) ; scores (chaque action à sa place du plan : épisode, condition, tâche, pas ;
# comptes par condition égaux et de somme n ; tableaux sans texte ; CH-18) ; scores par jeton des sondes principales
# (actions notées, bornes des champs) ; textes des actions (une ligne par action du plan, champs fixes, sans affichage) ;
# aucun texte d'action hors du fichier des textes (chaînes bornées dans les résultats, le manifeste et run.json ;
# recherche des textes des actions dans les autres fichiers ajoutés, hors tableaux npz, et dans les chaînes décodées des
# résultats, du manifeste et de run.json, CH-18, RCh-07) ; sondes figées relues, empreinte de chaque
# sonde ; journal (tests, poussée initiale, carte, lignes de progression au motif fixe ; empreinte des sondes figées
# écrite avant la fin du premier lot ; sondes figées avant le premier épisode, par les durées scellées, CH-05 ; lots
# consécutifs ; fin seulement avec un résumé) ; carte et mémoire ; pip freeze ; jetons.
# Branche sans run (arrêt avant le run) : contrôles des traces seules, sortie au code 4 (jamais 0). Aucun relancement.
# Chaque KO compte un contrôle en échec (le compte final est celui des lignes KO).
# Usage : recuperation_p3_v1.sh S DOSSIER_NEUF
set -uo pipefail
SOI=$(realpath "$0")
[ $# -eq 2 ] || { echo "usage : recuperation_p3_v1.sh S DOSSIER_NEUF (aucun relancement)"; exit 2; }
S=$1; D=$(realpath -m "$2")
TRAV="$D.travail"                # fichiers de travail dans un dossier neuf, jamais dans le parent partagé
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
PY=$B/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/P3-premier-test-i-a-v1.md
BRANCHE=calcul/p3-reel-v1
PILOTE=20261012-105125-t05-pilote-reel   # run du pilote : versions de référence (mêmes dépendances installées)
CARTE_EXIGEE=oui                 # A100 SXM4 d'au moins 75 Gio (nvidia-smi.txt des traces) ; la répétition jouet passe « non », sauf ses cas des gardes réelles
VERSIONS_EXIGEES=oui             # versions du run égales à celles du pilote ; idem
COPIE_EXIGEE=oui                 # ce script égal à sa copie versée à S ; idem
MODE_ATTENDU=reel
LONGUEUR_MAX=200                 # chaîne la plus longue admise hors du fichier des textes (motif d'un arrêt : 1 000)
MOTIF_RUN='^[0-9]{8}-[0-9]{6}-p3-reel$'
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
[ -e "$TRAV" ] && { echo "$TRAV existe déjà (R12)"; exit 2; }
mkdir -p "$TRAV" || exit 2
echecs=0
ok() { echo "OK  $*"; }
ko() { echo "KO  $*"; echecs=$((echecs + 1)); }
git clone -q https://github.com/lciric/controle-ia-travail.git "$D" || { echo "clonage impossible"; exit 2; }
cd "$D"
git fetch -q origin "$BRANCHE" || { echo "branche $BRANCHE introuvable"; exit 2; }
H=$(git rev-parse FETCH_HEAD); echo "tête de la branche : $H"
git checkout -q --detach "$H"
if [ "$COPIE_EXIGEE" = oui ]; then
    [ "$(git show "$S:docs/procedures/P3-premier-test-v1/recuperation_p3_v1.sh" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$SOI" | cut -d' ' -f1)" ] \
        && ok "0 récupération exécutée = copie versée à S" || ko "0 récupération exécutée ≠ copie versée à S"
fi
# 1. ascendance et contenu : ajouts seulement, aux chemins permis
git merge-base --is-ancestor "$S" "$H" && ok "1a S est ancêtre de la branche" || ko "1a S n'est pas ancêtre de la branche"
git diff --name-status --no-renames "$S" "$H" > "$TRAV/diff-status.txt"
NON_AJOUTS=$(grep -vc '^A' "$TRAV/diff-status.txt" || true)
[ "$NON_AJOUTS" = 0 ] && ok "1b seulement des ajouts ($(wc -l < "$TRAV/diff-status.txt") fichiers)" || ko "1b $NON_AJOUTS changement(s) autre(s) qu'un ajout"
cut -f2 "$TRAV/diff-status.txt" > "$TRAV/chemins.txt"
PERMIS='^(runs/[^/]+/manifeste\.json(\.sha256)?|diag/[^/]+/(sondes-figees|episodes-p3|resume|arret)\.json(\.sha256)?|donnees/[^/]+/(sondes-figees-legeres\.npz(\.sha256)?|scores-p3\.npz(\.sha256)?|jetons-principales-p3\.npz(\.sha256)?|textes-actions-p3\.jsonl(\.sha256)?|sondes-figees\.npz\.sha256)|traces/p3-[^/]+/(journal\.txt|tests\.txt|tests\.err|run\.json|run\.err|nvidia-smi\.txt|pip-freeze\.txt|empreintes\.sha256))$'
HORS=$(grep -vE "$PERMIS" "$TRAV/chemins.txt" | tr '\n' ' ' || true)
[ -z "$HORS" ] && ok "1c ajouts aux seuls chemins permis (manifeste, résultats et données du run, traces p3-*)" \
    || ko "1c chemins hors périmètre : $HORS"
RUNS=$(grep -E '^(runs|diag|donnees)/' "$TRAV/chemins.txt" | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
# aucun run (arrêt avant le lancement du run : amorce, installation, tests, poussée initiale) : traces seules ; les
# contrôles du run (2b, 3, 4, 5, 6d à 6f) sont sans objet et le script sort avec le code 4, jamais 0
SANS_RUN=non
if [ "$NRUNS" = 1 ] && [[ "$RUN" =~ $MOTIF_RUN ]] && [ -f "runs/$RUN/manifeste.json" ]; then ok "1d un seul run : $RUN"
elif [ "$NRUNS" = 0 ]; then SANS_RUN=oui; echo "--  1d aucun run sur la branche : récupération des traces seules (arrêt avant le run)"
else ko "1d runs : $(printf '%s ' $RUNS)(un seul, au motif, avec son manifeste, attendu)"; SANS_RUN=illisible; fi
AUTEURS=$(git log --format='%an' "$S..$H" | sort -u)
[ "$AUTEURS" = "instance de calcul (P3)" ] && ok "1e commits de « instance de calcul (P3) » ($(git rev-list --count "$S..$H"))" || ko "1e auteurs : $AUTEURS"
# 2. sceaux
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$TRAV/verifier-arbre.txt" 2>&1 && ok "2a verifier-arbre : $(tail -1 "$TRAV/verifier-arbre.txt")" || ko "2a verifier-arbre : $(tail -3 "$TRAV/verifier-arbre.txt" | tr '\n' ' ')"
NOUVELLES=$(for d in traces/p3-*/; do [ -d "$d" ] || continue; git cat-file -e "$S:${d%/}" 2>/dev/null || echo "${d%/}"; done)
for d in $NOUVELLES; do
    (cd "$d" && sha256sum -c --quiet empreintes.sha256) > "$TRAV/sc.txt" 2>&1 && ok "2c sha256sum -c $d" || ko "2c $d : $(head -2 "$TRAV/sc.txt" | tr '\n' ' ')"
done
# 2b (rattachements, sceaux des données), 3 (manifeste et citations), 4 (issue, pièces, scores, scores par jeton, textes,
# textes hors du fichier des textes), 5 (sondes figées), 6e (durées) ; sans objet sans run. Le programme rend le nombre
# de ses KO (borné à 100), ajouté au compte.
if [ "$SANS_RUN" = non ]; then
PYTHONPATH=src "$PY" - "$RUN" "$S" "$P" "$PILOTE" "$MODE_ATTENDU" "$VERSIONS_EXIGEES" "$LONGUEUR_MAX" "$TRAV/diff-status.txt" "$NOUVELLES" <<'EOF' || echecs=$((echecs + $?))
import hashlib, json, re, sys
from pathlib import Path
import numpy as np
from controle_ia.environnements.noter_pilote_a import VERSIONS_EGALES
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.manifeste import graines, lire_manifeste, verifier_resultat
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.conditions import CHAMPS_BORNES
from controle_ia.premier_test_ia.entrainement import FAMILLES_P3
from controle_ia.premier_test_ia.figees import lire_sondes
from controle_ia.scellement import verifier
run, s, p, pilote, mode_attendu, versions_exigees, longueur_max, diff_status, nouvelles = sys.argv[1:10]
longueur_max = int(longueur_max)
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
def so(m): print("-- ", m)
texte = Path(p).read_text(encoding="utf-8")
def cite(motif):
    x = re.findall(motif, texte)
    return x[0] if len(x) == 1 else None
cfg_c, taches_c = cite(rp.CONFIG_CITEE.pattern), cite(rp.TACHES_CITEES.pattern)
ent_c, code_c = cite(r"Entropie : `([0-9]+)`"), cite(r"Commit du code d'analyse : `([0-9a-f]{40})`")
chemin_t = cite(r"Chemin des tâches de P3 : `([^`]+)`")
d, dd = Path("diag") / run, Path("donnees") / run
DONNEES_EPI = {"scores-p3.npz": ("scores", "scores_sha256"), "jetons-principales-p3.npz": ("jetons_principales", "jetons_principales_sha256"),
               "textes-actions-p3.jsonl": ("textes", "textes_sha256")}
DONNEES_FIG = ("sondes-figees-legeres.npz", "sondes-figees.npz.sha256")
# 2b. chaque résultat : sceau, rattachement au manifeste de CE run
lus = {}
for f in sorted(d.glob("*.json")):
    try:
        corps = verifier_resultat(".", f)
        assert corps.get("run_id") == run, f"run_id {corps.get('run_id')!r} ≠ {run!r}"
        lus[f.name] = corps["resultat"]
        ok(f"2b résultat {f.name} scellé, rattaché au manifeste du run {run}")
    except Exception as e:
        ko(f"2b résultat {f.name} : {str(e)[:200]}")
fig, epi = lus.get("sondes-figees.json"), lus.get("episodes-p3.json")
r_present, a_present = (d / "resume.json").exists(), (d / "arret.json").exists()
issue = lus.get("resume.json") if r_present else lus.get("arret.json")
# 2b. données : chaque fichier présent vérifié par son sceau compagnon (CH-06 b), rattaché à l'empreinte et au chemin
# écrits dans son résultat, et à celle du résumé (ou de l'arrêt) quand il existe ; un rattachement à un résultat absent
# ou non vérifié est sans objet ici (4c et 2b le comptent déjà)
def sceau(f):
    try:
        return verifier(f)
    except Exception as e:
        ko(f"2b {f.name} : sceau compagnon non conforme ({str(e)[:120]})")
        return None
for nom, (cle, cle_sha) in DONNEES_EPI.items():
    f = dd / nom
    if not f.exists():
        continue
    e = sceau(f)
    if e is None:
        continue
    if epi is None:
        so(f"2b {nom} scellé ; rattachement sans objet (résultat des épisodes absent ou non vérifié)")
        continue
    vu = [x for x in (epi.get(cle_sha), (issue or {}).get(cle_sha) if r_present else epi.get(cle_sha)) if x is not None]
    (ok if epi.get(cle) == str(f) and e == epi.get(cle_sha) and all(x == e for x in vu) else ko)(
        f"2b {nom} scellé, rattaché au résultat des épisodes et au résumé ({str(epi.get(cle_sha))[:12]}…)")
leg, sc = dd / "sondes-figees-legeres.npz", dd / "sondes-figees.npz.sha256"
if leg.exists():
    e = sceau(leg)
    if e is not None and fig is None:
        so("2b sondes figées légères scellées ; rattachement sans objet (résultat des sondes figées absent ou non vérifié)")
    elif e is not None:
        (ok if e == fig.get("sondes_legeres_sha256") else ko)(f"2b sondes figées légères scellées et rattachées au résultat ({str(fig.get('sondes_legeres_sha256'))[:12]}…)")
if sc.exists():
    if fig is None:
        so("2b sceau du fichier complet des sondes : rattachement sans objet (résultat des sondes figées absent ou non vérifié)")
    else:
        attendue = fig.get("sondes_figees_sha256")
        autres = [x for x in ((issue or {}).get("sondes_figees_sha256") if r_present else ((issue or {}).get("partiel") or {}).get("sondes_figees_sha256"),) if x is not None]
        (ok if sc.read_text(encoding="utf-8").split() == [attendue, "sondes-figees.npz"] and all(x == attendue for x in autres) else ko)(
            f"2b sceau du fichier complet des sondes = empreinte écrite au résultat et à l'issue ({str(attendue)[:12]}…)")
# 3. manifeste et citations
m = None
try:
    m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
except Exception as e:
    ko(f"3 manifeste illisible : {str(e)[:200]}")
taches = charger_taches(chemin_t) if chemin_t else []
plan = rp.plan_p3(taches)
ids_plan = [e for e, _, _ in plan]
if m is not None:
    (ok if m["commit"] == s else ko)(f"3a commit du manifeste {m['commit'][:12]}… = S")
    pr = m.get("preenregistrement") or {}
    sha_p = Path(p + ".sha256").read_text(encoding="utf-8").split()[0]
    (ok if pr.get("chemin") == p and pr.get("sha256") == sha_p else ko)(f"3b préenregistrement {pr.get('chemin')} {str(pr.get('sha256'))[:12]}…")
    (ok if cfg_c and rp.empreinte_config(m["config"]) == cfg_c else ko)(f"3c configuration du manifeste = configuration citée ({str(cfg_c)[:12]}…)")
    attendues = graines(rp.cles_des_graines(taches, m["config"]), int(ent_c)) if ent_c and taches else None
    (ok if attendues is not None and m["graines"] == attendues else ko)(
        f"3d entropie citée, graines = celles des clés de P3 sous cette entropie ({len(m['graines'])} graines)")
    (ok if m["config"].get("mode") == mode_attendu and m.get("decisif") is True and m.get("depot_propre") is True else ko)(
        f"3e mode {m['config'].get('mode')}, décisif {m.get('decisif')}, dépôt propre {m.get('depot_propre')}")
    if versions_exigees == "oui":
        try:
            mp, _ = lire_manifeste(f"runs/{pilote}/manifeste.json")
            v, vp = m.get("versions") or {}, mp.get("versions") or {}
            ecarts = [b for b in VERSIONS_EGALES if v.get(b) != vp.get(b)]
            (ok if not ecarts and v.get("torch") else ko)(f"3f versions égales à celles du pilote ({pilote}) : torch {v.get('torch')}, transformers {v.get('transformers')} ; écarts {ecarts}")
        except Exception as e:
            ko(f"3f manifeste du pilote illisible : {str(e)[:120]}")
    else:
        so("3f versions non comparées à celles du pilote (répétition sur processeur)")
T = int(m["config"]["T"]) if m is not None else None
# 4. issue, rattachée aux citations ; pièces attendues selon l'issue, dans les deux sens ; scores ; scores par jeton ; textes
(ok if r_present != a_present else ko)(f"4a issue : resume.json {r_present}, arret.json {a_present}")
if issue is None:
    so("4b sans objet : issue absente ou non vérifiée (4a, 2b)")
else:
    rattache = issue if r_present else (issue.get("partiel") or {})
    if a_present:
        print("    arrêt :", json.dumps({x: issue.get(x) for x in ("etape", "motif")}, ensure_ascii=False)[:200])
    (ok if rattache.get("commit_cite") == code_c and rattache.get("config_sha256") == cfg_c and rattache.get("taches_sha256") == taches_c
         and m is not None and rattache.get("consignes_sha256") == m["config"].get("consignes_sha256") else ko)(
        "4b issue rattachée aux citations (code, configuration, tâches, consignes de la configuration)")
presents = sorted(x.name for x in d.glob("*.json"))
permis = {"sondes-figees.json", "episodes-p3.json", "resume.json" if r_present else "arret.json"}
fig_x, epi_x = (d / "sondes-figees.json").exists(), (d / "episodes-p3.json").exists()
exiges = []
if fig_x:
    exiges += [dd / n for n in ("sondes-figees-legeres.npz", "sondes-figees-legeres.npz.sha256", "sondes-figees.npz.sha256")]
if epi_x:
    exiges += [dd / x for n in DONNEES_EPI for x in (n, n + ".sha256")]
manquants = [str(x) for x in exiges if not x.exists()]
orphelins = [n for n in DONNEES_EPI for x in (n, n + ".sha256") if (dd / x).exists() and not epi_x]
orphelins += [x for x in ("sondes-figees-legeres.npz", "sondes-figees-legeres.npz.sha256", "sondes-figees.npz.sha256") if (dd / x).exists() and not fig_x]
orphelins += [n for n in [*DONNEES_EPI, "sondes-figees-legeres.npz"] if (dd / n).exists() != (dd / (n + ".sha256")).exists()]
ordre = (not epi_x or fig_x) and (not r_present or (fig_x and epi_x))
(ok if set(presents) <= permis and not manquants and not orphelins and ordre else ko)(
    f"4c pièces attendues selon l'issue : résultats {presents} ; données manquantes {manquants} ; données sans leur résultat ou sans leur sceau {sorted(set(orphelins))} ; ordre {ordre}")
attendu_lignes = [(e, c, t["identifiant"], q) for e, t, c in plan for q in range(T)] if T else None
notees = None
if epi is None:
    so("4d aucun résultat d'épisodes vérifié (arrêt avant leur fin, ou 2b)")
elif fig is None or m is None or not (dd / "scores-p3.npz").exists():
    so("4d scores : sans objet (fichier des scores, résultat des sondes figées ou manifeste absent ou non vérifié : 4c, 2b, 3)")
else:
    with np.load(dd / "scores-p3.npz", allow_pickle=False) as z:
        cles = set(z.files)
        chaines = ("noms_sondes", "episode", "condition", "tache")
        attendues_cles = {"noms_sondes", "scores", "episode", "condition", "tache", "pas", "jetons", "jetons_notes",
                          *rp.MESURES_REELLES, *rp.MESURES_BOOLEENNES}
        noms = [x["nom"] for x in fig["sondes"]]
        n = len(z["episode"]) if "episode" in cles else -1
        courtes = cles == attendues_cles and all(z[c].dtype.kind == "U" and max((len(x) for x in z[c].tolist()), default=0) <= 80
                                                for c in chaines)
        nombres = cles == attendues_cles and all(z[c].dtype.kind in "fiub" for c in cles - set(chaines))
        par_cond = {c: int((z["condition"] == c).sum()) for c in rp.CONDITIONS} if "condition" in cles else {}
        lignes_z = list(zip(z["episode"].tolist(), z["condition"].tolist(), z["tache"].tolist(), [int(x) for x in z["pas"].tolist()])) \
            if courtes and nombres else None
        conforme = (courtes and nombres and list(z["noms_sondes"]) == noms and z["scores"].shape == (n, len(noms))
                    and n == len(plan) * T and lignes_z == attendu_lignes
                    and [f["episode"] for f in epi["fiches"]] == ids_plan
                    and len(set(par_cond.values())) == 1 and sum(par_cond.values()) == n)
        if nombres and z["scores"].ndim == 2:      # actions notées : lues même si une autre partie de 4d est en échec
            notees = np.flatnonzero(np.all(np.isfinite(z["scores"]), axis=1))
        if r_present and issue is not None:
            conforme = conforme and issue.get("actions") == n and issue.get("episodes") == len(plan) \
                and notees is not None and issue.get("actions_notees") == len(notees) and issue.get("principales") == fig.get("principales")
        (ok if conforme else ko)(f"4d scores : {n} actions, {len(noms)} sondes, {len(epi['fiches'])} épisodes sur {len(plan)}, "
                                 f"chaque action à sa place du plan (épisode, condition, tâche, pas) : {lignes_z == attendu_lignes}, "
                                 f"par condition {par_cond}, tableaux sans texte : {courtes and nombres}")
    if notees is not None and (dd / "jetons-principales-p3.npz").exists():
        with np.load(dd / "jetons-principales-p3.npz", allow_pickle=False) as j:
            cles_j = {"principales", "champs", "rang", "bornes", "bornes_lisibles", "longueur", "debut", "scores_0", "logits_0",
                      "scores_1", "logits_1"}
            princ = [fig["principales"].get(c) for c in ("tromperie", "enjeux")]
            conforme = set(j.files) == cles_j
            if conforme:
                L = int(j["longueur"].sum())
                debut = np.concatenate([[0], np.cumsum(j["longueur"])[:-1]]) if len(j["longueur"]) else np.zeros(0)
                conforme = (j["principales"].tolist() == princ and j["champs"].tolist() == list(CHAMPS_BORNES)
                            and j["rang"].tolist() == notees.tolist() and j["bornes"].shape == (len(notees), len(CHAMPS_BORNES))
                            and len(j["bornes_lisibles"]) == len(notees) and np.array_equal(j["debut"], debut)
                            and all(len(j[x]) == L for x in ("scores_0", "logits_0", "scores_1", "logits_1"))
                            and all(j[x].dtype.kind in "fiub" for x in cles_j - {"principales", "champs"})
                            and all(j[x].dtype.kind == "U" and max((len(v) for v in j[x].tolist()), default=0) <= 80
                                    for x in ("principales", "champs")))
            (ok if conforme else ko)(f"4d scores par jeton des sondes principales : {len(notees)} actions notées, sondes {princ}, bornes des champs")
    elif notees is not None:
        so("4d scores par jeton : fichier absent (4c)")
    else:
        so("4d scores par jeton : sans objet (tableau des scores illisible : 4d)")
textes = None
if epi is not None and (dd / "textes-actions-p3.jsonl").exists() and attendu_lignes is not None:
    fautes, lignes_t, textes = 0, [], []
    for brut in (dd / "textes-actions-p3.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            x = json.loads(brut)
            assert set(x) == {"episode", "condition", "tache", "pas", "texte"} and isinstance(x["texte"], str) \
                and isinstance(x["pas"], int) and not isinstance(x["pas"], bool)
            lignes_t.append((x["episode"], x["condition"], x["tache"], x["pas"]))
            textes.append(x["texte"])
        except Exception:
            fautes += 1
    (ok if not fautes and lignes_t == attendu_lignes else ko)(
        f"4e textes des actions : {len(lignes_t)} lignes sur {len(attendu_lignes)} attendues, chacune à sa place du plan "
        f"({lignes_t == attendu_lignes}), {fautes} ligne(s) mal formée(s) ; aucun texte affiché")
else:
    so("4e textes des actions : sans objet (aucun résultat d'épisodes vérifié, ou fichier absent : 4c)")
# 4f. aucun texte d'action hors du fichier des textes (CH-18, RCh-07) : (a) chaînes bornées dans les résultats, le
# manifeste et run.json des traces ; (b) fenêtres des textes des actions de 64 caractères ou plus (48 caractères de leur
# milieu ; une fenêtre faite d'un seul caractère répété est ignorée : elle retrouverait, par exemple, la barre de
# progression de tests.txt) cherchées dans tous les autres fichiers ajoutés, hors tableaux npz (leurs chaînes : 4d), et
# dans les chaînes décodées des résultats, du manifeste et de run.json (un texte sur plusieurs lignes ou avec des
# guillemets y est échappé, donc invisible aux octets bruts) ; comptes seulement, aucun texte affiché
longues, trouves_json = {}, {}
fenetres = sorted({t[(len(t) - 48) // 2:(len(t) - 48) // 2 + 48] for t in (textes or []) if len(t) >= 64})
ignorees = [x for x in fenetres if len(set(x)) == 1]
fenetres = [x for x in fenetres if len(set(x)) > 1]
def parcourir(x, cle=None, nom=""):
    if isinstance(x, str):
        borne = 1000 if (nom == "arret.json" and cle == "motif") else longueur_max
        if len(x) > borne:
            longues[nom] = max(longues.get(nom, 0), len(x))
        n_x = sum(1 for w in fenetres if w in x)
        if n_x:
            trouves_json[nom] = trouves_json.get(nom, 0) + n_x
    elif isinstance(x, dict):
        for c, v in x.items(): parcourir(v, c, nom)
    elif isinstance(x, list):
        for v in x: parcourir(v, cle, nom)
fichiers_json = [*sorted(d.glob("*.json")), Path(f"runs/{run}/manifeste.json")] + [Path(t) / "run.json" for t in nouvelles.split() if (Path(t) / "run.json").is_file()]
for f in fichiers_json:
    try:
        corps = f.read_text(encoding="utf-8")
        if f.name == "run.json" and not corps.strip():
            continue
        parcourir(json.loads(corps), None, f.name)
    except Exception as e:
        longues[f"{f} (illisible)"] = -1
ajoutes = [l.split("\t", 1)[1] for l in Path(diff_status).read_text(encoding="utf-8").splitlines() if "\t" in l]
autres = [Path(a) for a in ajoutes if Path(a).is_file() and not a.endswith(".npz") and not a.endswith("textes-actions-p3.jsonl")
          and not a.endswith("textes-actions-p3.jsonl.sha256")]
trouves = {}
if textes:
    morceaux = [x.encode("utf-8") for x in fenetres]
    for f in autres:
        b = f.read_bytes()
        n_f = sum(1 for x in morceaux if x in b)
        if n_f:
            trouves[str(f)] = n_f
    (ok if not longues and not trouves and not trouves_json else ko)(
        f"4f aucun texte d'action hors du fichier des textes : chaînes au-delà de la borne {longues} ; "
        f"textes retrouvés (nombre par fichier) {trouves} ; dans les chaînes JSON décodées {trouves_json} ; "
        f"{len(morceaux)} textes cherchés dans {len(autres)} fichiers ({len(ignorees)} fenêtre(s) d'un seul caractère répété ignorée(s))")
else:
    (ok if not longues else ko)(f"4f chaînes des résultats, du manifeste et de run.json dans la borne ({longues}) ; recherche des textes sans objet (aucun fichier des textes vérifié)")
# 5. sondes figées relues : fichier léger à son empreinte, empreinte de chaque sonde, principales, comptes
if fig is not None and (dd / "sondes-figees-legeres.npz").exists() and m is not None:
    try:
        sondes, meta, _ = lire_sondes(dd / "sondes-figees-legeres.npz", fig["sondes_legeres_sha256"])
        liste = [x for x in fig["sondes"] if x["classe"] != "SondeMahalanobis"]
        n_attendu = 2 * len(FAMILLES_P3) * len(m["config"]["couches"]) + 2 * m["config"]["n_plancher"]
        noms = [x["nom"] for x in fig["sondes"]]
        princ = fig["principales"]
        conforme = ([x.nom for x in sondes] == [x["nom"] for x in liste] and [x.empreinte() for x in sondes] == [x["empreinte"] for x in liste]
                    and meta.get("complet") == fig["sondes_figees_sha256"] and meta.get("principales") == princ
                    and len(noms) == n_attendu and set(princ) == {"tromperie", "enjeux"}
                    and all(princ[c] in noms and princ[c].startswith(c + "-") for c in princ))
        (ok if conforme else ko)(f"5 sondes figées relues : {len(sondes)} légères sur {len(noms)} (attendues {n_attendu}), "
                                 f"empreinte de chaque sonde, principales {princ}")
    except Exception as e:
        ko(f"5 sondes figées illisibles : {str(e)[:200]}")
elif fig is None:
    so("5 aucune sonde figée vérifiée (arrêt avant leur écriture, ou 2b)")
# 6e. sondes figées écrites avant le premier épisode, par les durées scellées (CH-05) : même origine (début du run) ;
# durée des sondes figées ≤ durée des épisodes − durée de leur seule boucle (arrondis à 0,1 s : tolérance 0,2 s)
if fig is not None and epi is not None:
    try:
        df, de, dl = float(fig["duree_s"]), float(epi["duree_s"]), float(epi["descriptifs"]["duree_s"])
        (ok if df <= de - dl + 0.2 else ko)(f"6e sondes figées avant le premier épisode (durées scellées) : {df} s ≤ {de} − {dl} s")
    except Exception as e:
        ko(f"6e durées illisibles : {str(e)[:120]}")
else:
    so("6e durées : sans objet (sondes figées ou épisodes absents ou non vérifiés ; l'ordre du journal fait foi, 6d)")
sys.exit(min(k, 100))
EOF
fi
# 6. journal de l'instance versé dans les traces de ce run (dernier dossier nouveau) ; aucun dossier nouveau : KO
[ -n "$NOUVELLES" ] || ko "6a aucune trace versée sur la branche (poussée finale en échec ?) : instance gardée, traces à reprendre"
J=$(printf '%s\n' $NOUVELLES | tail -1)
A=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
if [ "$SANS_RUN" = oui ]; then
    [ -s "$J/journal.txt" ] && ok "6a journal versé ($J) : $(grep -c . "$J/journal.txt") lignes ; dernière : $(tail -1 "$J/journal.txt" | cut -c1-160)" \
        || ko "6a journal absent ou vide ($J)"
else for motif in "$A tests attendus" "poussée avant l'installation" "disponible True" "tests : $A passed"; do
    grep -qF "$motif" "$J/journal.txt" 2>/dev/null && ok "6a journal ($J) : « $motif »" || ko "6a journal ($J) : « $motif » absent"
done; fi
grep '^PROGRES ' "$J/journal.txt" > "$TRAV/progres.txt" 2>/dev/null || true
NP=$(grep -c . "$TRAV/progres.txt" || true); NPC=$(grep -cE "$MOTIF_PROGRES" "$TRAV/progres.txt" || true)
[ "$NP" = "$NPC" ] && ok "6a lignes de progression au journal : $NP, toutes au motif fixe" || ko "6a lignes de progression : $NP, dont $NPC au motif fixe"
[ "$SANS_RUN" = oui ] && { [ "$NP" = 0 ] && ok "6a aucune ligne de progression sans run" || ko "6a $NP ligne(s) de progression sans run"; }
# ordre des étapes tiré de l'issue, jamais fixé : sondes figées écrites (une ligne, à l'empreinte du résultat, au nombre
# de sondes) avant la première ligne d'épisodes, c'est-à-dire avant la fin du premier lot (la ligne d'un lot s'écrit à
# sa fin ; « avant le premier épisode » s'établit par les durées, 6e) ; lignes de lot consécutives depuis 1, au total du
# plan ; ligne de fin seulement avec un résumé, aux comptes du résumé
if [ "$SANS_RUN" = non ]; then
PYTHONPATH=src "$PY" - "$RUN" "$TRAV/progres.txt" "$P" <<'EOF' || echecs=$((echecs + $?))
import json, re, sys
from pathlib import Path
from controle_ia.manifeste import lire_manifeste
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.premier_test_ia import run as rp
run, progres, p = sys.argv[1:4]
d = Path("diag") / run
lignes = Path(progres).read_text(encoding="utf-8").splitlines()
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
def corps(nom):
    f = d / nom
    try:
        return json.loads(f.read_text(encoding="utf-8"))["resultat"] if f.exists() else None
    except Exception:
        return None
fig, resume = corps("sondes-figees.json"), corps("resume.json")
try:
    m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
    lot = m["config"]["lot"]
except Exception:
    lot = None
chemin_t = re.findall(r"Chemin des tâches de P3 : `([^`]+)`", Path(p).read_text(encoding="utf-8"))
n_plan = len(rp.plan_p3(charger_taches(chemin_t[0]))) if len(chemin_t) == 1 else -1
n_lots = -(-n_plan // lot) if lot else -1
idx = lambda motif: [i for i, l in enumerate(lignes) if re.search(motif, l + " ")]
fig_l, epi_l, fin_l = idx(r" etape=sondes-figees "), idx(r" etape=episodes "), idx(r" etape=fin ")
if fig is not None:
    bonne = (len(fig_l) == 1 and f" empreinte={fig['sondes_figees_sha256']} " in lignes[fig_l[0]] + " "
             and f" sondes={len(fig['sondes'])} " in lignes[fig_l[0]] + " " and (not epi_l or fig_l[0] < epi_l[0]))
    (ok if bonne else ko)(f"6d sondes figées : une ligne à l'empreinte du résultat ({fig['sondes_figees_sha256'][:12]}…), "
                          f"avant la première ligne d'épisodes, donc avant la fin du premier lot ({len(fig_l)} ligne(s))")
else:
    (ok if not fig_l and not epi_l else ko)(f"6d sondes figées : aucune ligne de sondes figées ni d'épisodes sans leur résultat ({len(fig_l)}, {len(epi_l)})")
lots = [re.search(r" lot=([0-9]+)/([0-9]+) ", lignes[i] + " ") for i in epi_l]
suite = lot is not None and all(x is not None for x in lots) and [int(x.group(1)) for x in lots] == list(range(1, len(lots) + 1)) \
    and all(int(x.group(2)) == n_lots for x in lots)
if resume is not None:
    suite = suite and len(lots) == n_lots and len(fin_l) == 1 and fin_l[0] > epi_l[-1] \
        and f" episodes={resume['episodes']} actions={resume['actions']} " in lignes[fin_l[0]] + " "
else:
    suite = suite and not fin_l
(ok if suite else ko)(f"6f lots : {len(lots)} ligne(s) consécutive(s) sur {n_lots} ; fin {len(fin_l)} (résumé : {resume is not None})")
sys.exit(min(k, 100))
EOF
fi
# 6b. carte et mémoire (nvidia-smi.txt) ; 6c. pip freeze (descriptif) ; fichiers cherchés dans tous les dossiers nouveaux
NS=$(for d in $NOUVELLES; do [ -f "$d/nvidia-smi.txt" ] && echo "$d/nvidia-smi.txt"; done | head -1)
PF=$(for d in $NOUVELLES; do [ -f "$d/pip-freeze.txt" ] && echo "$d/pip-freeze.txt"; done | head -1)
if [ "$SANS_RUN" = oui ]; then
    echo "--  6b et 6c descriptifs sans run : carte « $(sed -n '2p' "${NS:-/dev/null}" 2>/dev/null) » ; pip freeze ${PF:-absent}"
elif [ "$CARTE_EXIGEE" = oui ]; then
    CARTE=$(sed -n '2p' "${NS:-/dev/null}" 2>/dev/null)
    MIB=$(printf '%s\n' "$CARTE" | sed -n 's/.*, *\([0-9][0-9]*\) MiB *$/\1/p')
    if [[ "$CARTE" == *A100* && "$CARTE" == *SXM4* ]] && [ -n "$MIB" ] && [ "$MIB" -ge 76800 ]; then ok "6b carte : $CARTE"
    else ko "6b carte ou mémoire inattendue (A100 SXM4, au moins 75 Gio) : « $CARTE »"; fi
else echo "--  6b carte non exigée (répétition sur processeur)"; fi
if [ "$SANS_RUN" = oui ]; then :
elif [ -n "$PF" ] && grep -q '^torch==' "$PF" && grep -q '^transformers==' "$PF"; then
    ok "6c pip freeze versé ($PF) : $(grep -c . "$PF") paquets ; $(grep -E '^(torch|transformers)==' "$PF" | tr '\n' ' ')"
elif grep -qF "pip freeze impossible" "$J/journal.txt" 2>/dev/null; then echo "--  6c pip freeze impossible, journalisé (descriptif, sans effet sur le run)"
else ko "6c pip freeze absent des traces, sans échec journalisé"; fi
# 7. aucune valeur de jeton dans le différentiel ni dans les fichiers ajoutés (comptée, jamais affichée)
git diff "$S" "$H" > "$TRAV/diff-complet.txt"
python3 - "$TRAV/diff-complet.txt" "$TRAV/diff-status.txt" <<'EOF' || echecs=$((echecs + $?))
import os, sys
from pathlib import Path
diff = Path(sys.argv[1]).read_bytes()
fichiers = [l.split("\t", 1)[1] for l in Path(sys.argv[2]).read_text().splitlines() if "\t" in l]
k = 0
for nom in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(nom)
    if not v or len(v) < 8:
        print(f"KO  7 {nom} absent de l'environnement de la session : recherche impossible"); k += 1; continue
    b = v.encode()
    n = diff.count(b) + sum(Path(f).read_bytes().count(b) for f in fichiers if Path(f).is_file())
    print(("OK " if n == 0 else "KO ") + f" 7 valeur de {nom} : {n} occurrence(s)")
    k += n > 0
sys.exit(min(k, 100))
EOF
echo "RUN=$RUN"; echo "TETE=$H"
if [ "$echecs" != 0 ]; then echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"; exit 1
elif [ "$SANS_RUN" = oui ]; then echo "RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES"; exit 4
else echo "RÉCUPÉRATION : TOUS CONFORMES"; fi
