#!/usr/bin/env bash
# Contrôles de récupération du premier test boîte blanche sur l'organisme (i-a) (P3, R-192 ; préenregistrement
# prereg/P3-premier-test-i-a-v1.md), avant toute fusion et avant toute proposition de destruction de l'instance ; déclinés
# de la récupération des notations refaites du pilote de T0.5 (docs/procedures/notations-T0.5-v2/recuperation_notations_v1.sh)
# sous un nom nouveau (R12). Clone propre du dépôt de travail ; rien n'est fusionné ni poussé ici. Aucune valeur de jeton,
# aucun texte d'action, de consigne ni de donnée générique n'est affiché.
# Ce qui est contrôlé : ascendance (S ancêtre) ; ajouts seulement, aux seuls chemins permis (manifeste du run ; ses
# résultats : sondes figées, épisodes, résumé ou arrêt ; ses données légères : sondes figées sans les matrices de
# Mahalanobis, scores par action, leurs sceaux et le sceau du fichier complet des sondes, resté sur l'instance ; traces
# p3-*) ; un seul run « …-p3-reel » ; auteurs ; sceaux ; rattachements (résultats au manifeste du run, données légères aux
# empreintes écrites dans les résultats) ; manifeste et citations (commit, préenregistrement, configuration, entropie et
# graines des clés de P3, mode, décisif, dépôt propre, versions égales à celles du pilote) ; issue (résumé ou arrêt, un
# seul), rattachée aux citations ; pièces attendues selon l'issue ; scores (épisodes du plan, actions par condition,
# tableaux sans texte) ; sondes figées relues, empreinte de chaque sonde ; journal (tests, poussée initiale, carte, lignes
# de progression au motif fixe ; empreinte des sondes figées écrite avant le premier épisode ; lots consécutifs ; fin
# seulement avec un résumé) ; carte et mémoire ; pip freeze ; jetons.
# Branche sans run (arrêt avant le run) : contrôles des traces seules, sortie au code 4 (jamais 0). Aucun relancement.
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
CARTE_EXIGEE=oui                 # A100 SXM4 d'au moins 75 Gio (nvidia-smi.txt des traces) ; la répétition jouet passe « non »
VERSIONS_EXIGEES=oui             # versions du run égales à celles du pilote ; la répétition jouet passe « non »
COPIE_EXIGEE=oui                 # ce script égal à sa copie versée à S ; la répétition jouet, qui joue une copie modifiée, passe « non »
MODE_ATTENDU=reel
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
PERMIS='^(runs/[^/]+/manifeste\.json(\.sha256)?|diag/[^/]+/(sondes-figees|episodes-p3|resume|arret)\.json(\.sha256)?|donnees/[^/]+/(sondes-figees-legeres\.npz(\.sha256)?|scores-p3\.npz(\.sha256)?|sondes-figees\.npz\.sha256)|traces/p3-[^/]+/(journal\.txt|tests\.txt|tests\.err|run\.json|run\.err|nvidia-smi\.txt|pip-freeze\.txt|empreintes\.sha256))$'
HORS=$(grep -vE "$PERMIS" "$TRAV/chemins.txt" | tr '\n' ' ' || true)
[ -z "$HORS" ] && ok "1c ajouts aux seuls chemins permis (manifeste, résultats et données légères du run, traces p3-*)" \
    || ko "1c chemins hors périmètre : $HORS"
RUNS=$(grep -E '^(runs|diag|donnees)/' "$TRAV/chemins.txt" | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
# aucun run (arrêt avant le lancement du run : amorce, installation, tests, poussée initiale) : traces seules ; les
# contrôles du run (2b, 3, 4, 5, journal du run) sont sans objet et le script sort avec le code 4, jamais 0
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
# 2b (rattachements), 3 (manifeste et citations), 4 (issue, pièces, scores), 5 (sondes figées) ; sans objet sans run
[ "$SANS_RUN" = oui ] || [ "$SANS_RUN" = illisible ] || PYTHONPATH=src "$PY" - "$RUN" "$S" "$P" "$PILOTE" "$MODE_ATTENDU" "$VERSIONS_EXIGEES" <<'EOF' || echecs=$((echecs + 1))
import hashlib, json, re, sys
from pathlib import Path
import numpy as np
from controle_ia.environnements.noter_pilote_a import VERSIONS_EGALES
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.manifeste import graines, lire_manifeste, verifier_resultat
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.entrainement import FAMILLES_P3
from controle_ia.premier_test_ia.figees import lire_sondes
run, s, p, pilote, mode_attendu, versions_exigees = sys.argv[1:7]
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
texte = Path(p).read_text(encoding="utf-8")
def cite(motif):
    x = re.findall(motif, texte)
    return x[0] if len(x) == 1 else None
cfg_c, taches_c = cite(rp.CONFIG_CITEE.pattern), cite(rp.TACHES_CITEES.pattern)
ent_c, code_c = cite(r"Entropie : `([0-9]+)`"), cite(r"Commit du code d'analyse : `([0-9a-f]{40})`")
chemin_t = cite(r"Chemin des tâches de P3 : `([^`]+)`")
d, dd = Path("diag") / run, Path("donnees") / run
sha = lambda x: hashlib.sha256(x.read_bytes()).hexdigest()
# 2b. chaque résultat : sceau, rattachement au manifeste de CE run ; données légères rattachées aux empreintes écrites
lus = {}
for f in sorted(d.glob("*.json")):
    try:
        corps = verifier_resultat(".", f)
        assert corps.get("run_id") == run, f"run_id {corps.get('run_id')!r} ≠ {run!r}"
        lus[f.name] = corps["resultat"]
        ok(f"2b verifier_resultat {f}, rattaché au run {run}")
    except Exception as e:
        ko(f"2b verifier_resultat {f} : {str(e)[:200]}")
fig, epi = lus.get("sondes-figees.json"), lus.get("episodes-p3.json")
if fig is not None:
    leg, sc = dd / "sondes-figees-legeres.npz", dd / "sondes-figees.npz.sha256"
    if leg.exists():
        (ok if sha(leg) == fig["sondes_legeres_sha256"] else ko)(f"2b sondes figées légères rattachées au résultat ({fig['sondes_legeres_sha256'][:12]}…)")
    if sc.exists():
        (ok if sc.read_text(encoding="utf-8").split() == [fig["sondes_figees_sha256"], "sondes-figees.npz"] else ko)(
            f"2b sceau du fichier complet des sondes = empreinte écrite au résultat ({fig['sondes_figees_sha256'][:12]}…)")
if epi is not None and (dd / "scores-p3.npz").exists():
    (ok if epi["scores"] == str(dd / "scores-p3.npz") and sha(dd / "scores-p3.npz") == epi["scores_sha256"] else ko)(
        f"2b scores rattachés au résultat des épisodes ({str(epi['scores_sha256'])[:12]}…)")
# 3. manifeste et citations
try:
    m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
except Exception as e:
    ko(f"3 manifeste illisible : {str(e)[:200]}")
    sys.exit(1)
(ok if m["commit"] == s else ko)(f"3a commit du manifeste {m['commit'][:12]}… = S")
pr = m.get("preenregistrement") or {}
sha_p = Path(p + ".sha256").read_text(encoding="utf-8").split()[0]
(ok if pr.get("chemin") == p and pr.get("sha256") == sha_p else ko)(f"3b préenregistrement {pr.get('chemin')} {str(pr.get('sha256'))[:12]}…")
(ok if cfg_c and rp.empreinte_config(m["config"]) == cfg_c else ko)(f"3c configuration du manifeste = configuration citée ({str(cfg_c)[:12]}…)")
taches = charger_taches(chemin_t) if chemin_t else []
attendues = graines(rp.cles_des_graines(taches, m["config"]), int(ent_c)) if ent_c and taches else None
(ok if attendues is not None and m["graines"] == attendues else ko)(
    f"3d entropie citée, graines = celles des clés de P3 sous cette entropie ({len(m['graines'])} graines)")
(ok if m["config"].get("mode") == mode_attendu and m.get("decisif") is True and m.get("depot_propre") is True else ko)(
    f"3e mode {m['config'].get('mode')}, décisif {m.get('decisif')}, dépôt propre {m.get('depot_propre')}")
if versions_exigees == "oui":
    mp, _ = lire_manifeste(f"runs/{pilote}/manifeste.json")
    v, vp = m.get("versions") or {}, mp.get("versions") or {}
    ecarts = [b for b in VERSIONS_EGALES if v.get(b) != vp.get(b)]
    (ok if not ecarts and v.get("torch") else ko)(f"3f versions égales à celles du pilote : torch {v.get('torch')}, transformers {v.get('transformers')} ; écarts {ecarts}")
else:
    print("--  3f versions non comparées à celles du pilote (répétition sur processeur)")
# 4. issue, rattachée aux citations ; pièces attendues selon l'issue ; scores
r, a = (d / "resume.json").exists(), (d / "arret.json").exists()
(ok if r != a else ko)(f"4a issue : resume.json {r}, arret.json {a}")
issue = lus.get("resume.json") if r else lus.get("arret.json")
rattache = (issue if r else (issue or {}).get("partiel", {})) or {}
if a and issue:
    print("    arrêt :", json.dumps({x: issue.get(x) for x in ("etape", "motif")}, ensure_ascii=False)[:600])
(ok if rattache.get("commit_cite") == code_c and rattache.get("config_sha256") == cfg_c and rattache.get("taches_sha256") == taches_c
     and rattache.get("consignes_sha256") == m["config"].get("consignes_sha256") else ko)(
    "4b issue rattachée aux citations (code, configuration, tâches, consignes de la configuration)")
presents = sorted(x.name for x in d.glob("*.json"))
permis = {"sondes-figees.json", "episodes-p3.json", "resume.json" if r else "arret.json"}
exiges = []
if (d / "sondes-figees.json").exists():
    exiges += [dd / "sondes-figees-legeres.npz", dd / "sondes-figees-legeres.npz.sha256", dd / "sondes-figees.npz.sha256"]
if (d / "episodes-p3.json").exists():
    exiges += [dd / "scores-p3.npz", dd / "scores-p3.npz.sha256"]
manquants = [str(x) for x in exiges if not x.exists()]
ordre = ((not (d / "episodes-p3.json").exists() or (d / "sondes-figees.json").exists())
         and (not r or {"sondes-figees.json", "episodes-p3.json"} <= set(presents)))
(ok if set(presents) <= permis and not manquants and ordre else ko)(
    f"4c pièces attendues selon l'issue : résultats {presents} ; données manquantes {manquants}")
plan = rp.plan_p3(taches)
ids_plan = [e for e, _, _ in plan]
if epi is not None and fig is not None and (dd / "scores-p3.npz").exists():
    with np.load(dd / "scores-p3.npz", allow_pickle=False) as z:
        cles = set(z.files)
        chaines = ("noms_sondes", "episode", "condition", "tache")
        attendues_cles = {"noms_sondes", "scores", "episode", "condition", "tache", "pas", "jetons", "jetons_notes", "cout",
                          *rp.MESURES_BOOLEENNES}
        noms = [x["nom"] for x in fig["sondes"]]
        n = len(z["episode"]) if "episode" in cles else -1
        courtes = cles == attendues_cles and all(z[c].dtype.kind == "U" and max((len(x) for x in z[c].tolist()), default=0) <= 80
                                                for c in chaines)
        nombres = cles == attendues_cles and all(z[c].dtype.kind in "fiub" for c in cles - set(chaines))
        par_cond = {c: int((z["condition"] == c).sum()) for c in rp.CONDITIONS} if "condition" in cles else {}
        conforme = (courtes and nombres and list(z["noms_sondes"]) == noms and z["scores"].shape == (n, len(noms))
                    and sorted(set(z["episode"].tolist())) == sorted(ids_plan) and n == len(plan) * m["config"]["T"]
                    and [f["episode"] for f in epi["fiches"]] == ids_plan and len(set(par_cond.values())) == 1)
        if r:
            conforme = conforme and issue.get("actions") == n and issue.get("episodes") == len(plan)
        (ok if conforme else ko)(f"4d scores : {n} actions, {len(noms)} sondes, {len(epi['fiches'])} épisodes sur {len(plan)}, "
                                 f"par condition {par_cond}, tableaux sans texte : {courtes and nombres}")
    longues = []
    def parcourir(x):
        if isinstance(x, str):
            longues.append(len(x))
        elif isinstance(x, dict):
            for v in x.values(): parcourir(v)
        elif isinstance(x, list):
            for v in x: parcourir(v)
    parcourir(epi)
    (ok if max(longues, default=0) <= 200 else ko)(f"4d résultat des épisodes sans texte long (chaîne la plus longue : {max(longues, default=0)} caractères)")
elif epi is None:
    print("--  4d aucun résultat d'épisodes (arrêt avant leur fin)")
# 5. sondes figées relues : fichier léger à son empreinte, empreinte de chaque sonde, principales, comptes
if fig is not None and (dd / "sondes-figees-legeres.npz").exists():
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
    print("--  5 aucune sonde figée (arrêt avant leur écriture)")
sys.exit(1 if k else 0)
EOF
# 6. journal de l'instance versé dans les traces de ce run (dernier dossier nouveau) ; aucun dossier nouveau : KO
[ -n "$NOUVELLES" ] || ko "6 aucune trace versée sur la branche (poussée finale en échec ?) : instance gardée, traces à reprendre"
J=$(printf '%s\n' $NOUVELLES | tail -1)
A=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
if [ "$SANS_RUN" = oui ]; then
    [ -s "$J/journal.txt" ] && ok "6 journal versé ($J) : $(grep -c . "$J/journal.txt") lignes ; dernière : $(tail -1 "$J/journal.txt" | cut -c1-160)" \
        || ko "6 journal absent ou vide ($J)"
else for motif in "$A tests attendus" "poussée avant l'installation" "disponible True" "tests : $A passed"; do
    grep -qF "$motif" "$J/journal.txt" 2>/dev/null && ok "6 journal ($J) : « $motif »" || ko "6 journal ($J) : « $motif » absent"
done; fi
grep '^PROGRES ' "$J/journal.txt" > "$TRAV/progres.txt" 2>/dev/null || true
NP=$(grep -c . "$TRAV/progres.txt" || true); NPC=$(grep -cE "$MOTIF_PROGRES" "$TRAV/progres.txt" || true)
[ "$NP" = "$NPC" ] && ok "6 lignes de progression au journal : $NP, toutes au motif fixe" || ko "6 lignes de progression : $NP, dont $NPC au motif fixe"
[ "$SANS_RUN" = oui ] && { [ "$NP" = 0 ] && ok "6 aucune ligne de progression sans run" || ko "6 $NP ligne(s) de progression sans run"; }
# ordre des étapes tiré de l'issue, jamais fixé : sondes figées écrites (une ligne, à l'empreinte du résultat, au nombre
# de sondes) avant la première ligne d'épisodes ; lignes de lot consécutives depuis 1, au total du plan ; ligne de fin
# seulement avec un résumé, aux comptes du résumé
[ "$SANS_RUN" = non ] && PYTHONPATH=src "$PY" - "$RUN" "$TRAV/progres.txt" "$P" <<'EOF' || { [ "$SANS_RUN" = non ] && echecs=$((echecs + 1)); }
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
    return json.loads(f.read_text(encoding="utf-8"))["resultat"] if f.exists() else None
fig, resume = corps("sondes-figees.json"), corps("resume.json")
m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
chemin_t = re.findall(r"Chemin des tâches de P3 : `([^`]+)`", Path(p).read_text(encoding="utf-8"))
n_plan = len(rp.plan_p3(charger_taches(chemin_t[0]))) if len(chemin_t) == 1 else -1
n_lots = -(-n_plan // m["config"]["lot"])
idx = lambda motif: [i for i, l in enumerate(lignes) if re.search(motif, l + " ")]
fig_l, epi_l, fin_l = idx(r" etape=sondes-figees "), idx(r" etape=episodes "), idx(r" etape=fin ")
if fig is not None:
    bonne = (len(fig_l) == 1 and f" empreinte={fig['sondes_figees_sha256']} " in lignes[fig_l[0]] + " "
             and f" sondes={len(fig['sondes'])} " in lignes[fig_l[0]] + " " and (not epi_l or fig_l[0] < epi_l[0]))
    (ok if bonne else ko)(f"6 sondes figées : une ligne à l'empreinte du résultat ({fig['sondes_figees_sha256'][:12]}…), "
                          f"avant la première ligne d'épisodes ({len(fig_l)} ligne(s))")
else:
    (ok if not fig_l and not epi_l else ko)(f"6 sondes figées : aucune ligne de sondes figées ni d'épisodes sans leur résultat ({len(fig_l)}, {len(epi_l)})")
lots = [re.search(r" lot=([0-9]+)/([0-9]+) ", lignes[i] + " ") for i in epi_l]
suite = all(x is not None for x in lots) and [int(x.group(1)) for x in lots] == list(range(1, len(lots) + 1)) \
    and all(int(x.group(2)) == n_lots for x in lots)
if resume is not None:
    suite = suite and len(lots) == n_lots and len(fin_l) == 1 and fin_l[0] > epi_l[-1] \
        and f" episodes={resume['episodes']} actions={resume['actions']} " in lignes[fin_l[0]] + " "
else:
    suite = suite and not fin_l
(ok if suite else ko)(f"6 lots : {len(lots)} ligne(s) consécutive(s) sur {n_lots} ; fin {len(fin_l)} (résumé : {resume is not None})")
sys.exit(1 if k else 0)
EOF
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
python3 - "$TRAV/diff-complet.txt" "$TRAV/diff-status.txt" <<'EOF' || echecs=$((echecs + 1))
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
sys.exit(1 if k else 0)
EOF
echo "RUN=$RUN"; echo "TETE=$H"
if [ "$echecs" != 0 ]; then echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"; exit 1
elif [ "$SANS_RUN" = oui ]; then echo "RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES"; exit 4
else echo "RÉCUPÉRATION : TOUS CONFORMES"; fi
