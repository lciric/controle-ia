#!/usr/bin/env bash
# Contrôles de récupération du pilote de T0.5 (plan de lancement du pilote, étape 7), avant toute fusion et avant toute
# proposition de destruction de l'instance (PL-10, PL-11) ; sur le modèle de recuperation_revalidation_v2.sh, plus la
# branche des vecteurs par action (donnees/t05/<run>, un commit sans parent : empreinte égale à celle d'episodes.json).
# Clone propre du dépôt de travail ; rien n'est fusionné ni poussé ici. Aucune valeur de jeton n'est affichée.
# Relecture R2 (CH-09) : run complet : fichiers de résultats exigés (épisodes, appariement, notations décisives et
# descriptives de chaque juge) et comptes exacts (épisodes = tâches × épisodes par tâche ; notations de chaque juge =
# passes des épisodes à ensemble non vide, recalculées par les fonctions du code cité ; paires de l'appariement) ;
# arrêt : état « partiel » affiché ; versions (manifeste), carte et mémoire (nvidia-smi.txt), pip freeze des traces ;
# relance : la branche du premier lancement (…-v1) est lue et citée. Aucun texte d'épisode n'est affiché.
# Usage : recuperation_pilote_v1.sh S DOSSIER_NEUF [relance]
set -uo pipefail
SOI=$(realpath "$0")
S=${1:?commit de scellement}; D=$(realpath -m "${2:?dossier neuf}"); MODE=${3:-premier}
TRAV="$D.travail"                # fichiers de travail dans un dossier neuf, jamais dans le parent partagé (VH-08)
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
PY=$B/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-pilote-8B-v1.md
PREMIERE=calcul/t05-pilote-reel-v1
case "$MODE" in premier) BRANCHE=$PREMIERE ;; relance) BRANCHE=calcul/t05-pilote-reel-v2 ;; *) echo "mode : relance, ou rien"; exit 2 ;; esac
CARTE_EXIGEE=oui                 # A100 SXM4 d'au moins 75 Gio (nvidia-smi.txt des traces) ; la répétition jouet passe « non »
COPIE_EXIGEE=oui                 # ce script égal à sa copie versée à S (VH-12) ; la répétition jouet, qui joue une copie modifiée, passe « non »
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
# ce script est sa copie versée à S (VH-12)
if [ "$COPIE_EXIGEE" = oui ]; then
    [ "$(git show "$S:docs/procedures/pilote-T0.5-v1/recuperation_pilote_v1.sh" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$SOI" | cut -d' ' -f1)" ] \
        && ok "0 récupération exécutée = copie versée à S" || ko "0 récupération exécutée ≠ copie versée à S"
fi
# 0. relance : branche du premier lancement lue et citée (CH-09) ; elle ne doit porter aucun episodes.json (préséance)
if [ "$MODE" = relance ]; then
    if git fetch -q origin "$PREMIERE" 2>/dev/null; then
        V1=$(git rev-parse FETCH_HEAD)
        echo "branche du premier lancement $PREMIERE : tête $V1 ; runs : $(git diff --name-only "$S" "$V1" | grep -E '^diag/' | cut -d/ -f2 | sort -u | tr '\n' ' ')"
        # liste écrite dans un fichier, code de git exigé : jamais de tube vers grep -q sous pipefail (relecture R2, CH-03)
        if git ls-tree -r --name-only "$V1" > "$TRAV/arbre-v1.txt"; then
            if grep -q '/episodes\.json$' "$TRAV/arbre-v1.txt"; then ko "0 $PREMIERE porte un episodes.json : relancement contraire à la préséance"
            else ok "0 $PREMIERE lue, sans episodes.json ($(wc -l < "$TRAV/arbre-v1.txt") chemins lus)"; fi
        else ko "0 $PREMIERE : arbre illisible"; fi
    else ko "0 $PREMIERE introuvable : relance sans premier lancement"; fi
fi
# 1. ascendance et contenu
git merge-base --is-ancestor "$S" "$H" && ok "1a S est ancêtre de la branche" || ko "1a S n'est pas ancêtre de la branche"
git diff --name-status "$S" "$H" > "$TRAV/diff-status.txt"
NON_AJOUTS=$(grep -vc '^A' "$TRAV/diff-status.txt" || true)
[ "$NON_AJOUTS" = 0 ] && ok "1b seulement des ajouts ($(wc -l < "$TRAV/diff-status.txt") fichiers)" || ko "1b $NON_AJOUTS changement(s) autre(s) qu'un ajout"
HORS=$(cut -f2 "$TRAV/diff-status.txt" | grep -vE '^(runs/[^/]+/|diag/[^/]+/|traces/t05-[^/]+/)' || true)
[ -z "$HORS" ] && ok "1c ajouts sous runs/, diag/ et traces/t05-*/ seulement" || ko "1c chemins hors périmètre : $HORS"
RUNS=$(cut -f2 "$TRAV/diff-status.txt" | grep -E '^(runs|diag)/' | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
if [ "$NRUNS" = 1 ] && [[ "$RUN" =~ ^[0-9]{8}-[0-9]{6}-t05-pilote-reel$ ]]; then ok "1d un seul run : $RUN"; else ko "1d runs : $RUNS"; fi
AUTEURS=$(git log --format='%an' "$S..$H" | sort -u)
[ "$AUTEURS" = "instance de calcul (T0.5)" ] && ok "1e commits de « instance de calcul (T0.5) » ($(git rev-list --count "$S..$H"))" || ko "1e auteurs : $AUTEURS"
# 2. sceaux
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$TRAV/verifier-arbre.txt" 2>&1 && ok "2a verifier-arbre : $(tail -1 "$TRAV/verifier-arbre.txt")" || ko "2a verifier-arbre : $(tail -3 "$TRAV/verifier-arbre.txt")"
for f in diag/"$RUN"/*.json; do
    PYTHONPATH=src "$PY" -c "from controle_ia.manifeste import verifier_resultat; verifier_resultat('.', '$f')" 2>"$TRAV/vr.err" \
        && ok "2b verifier_resultat $f" || ko "2b verifier_resultat $f : $(tail -1 "$TRAV/vr.err")"
done
NOUVELLES=$(for d in traces/t05-*/; do git cat-file -e "$S:${d%/}" 2>/dev/null || echo "${d%/}"; done)
for d in $NOUVELLES; do
    (cd "$d" && sha256sum -c --quiet empreintes.sha256) > "$TRAV/sc.txt" 2>&1 && ok "2c sha256sum -c $d" || ko "2c $d : $(head -2 "$TRAV/sc.txt")"
done
# 3. manifeste et citations ; 4. issue ; vecteurs
PYTHONPATH=src "$PY" - "$RUN" "$S" "$P" "$TRAV" <<'EOF' || echecs=$((echecs + 1))
import json, re, sys
from pathlib import Path
from controle_ia.manifeste import lire_manifeste
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements.lancer_pilote_a import empreinte_config
from controle_ia.environnements.pilote_a import charger_taches
run, s, p, trav = sys.argv[1:5]
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
texte = Path(p).read_text(encoding="utf-8")
cite = lambda motif: (re.search(motif, texte) or [None, None])[1]
cfg_c, taches_c, ent_c = cite(r"Configuration du pilote \(empreinte canonique\) : `([0-9a-f]{64})`"), \
    cite(r"Tâches du pilote : `([0-9a-f]{64})`"), cite(r"Entropie : `([0-9]+)`")
chemin_t = cite(r"Chemin des tâches : `([^`]+)`")
m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
(ok if m["commit"] == s else ko)(f"3a commit du manifeste {m['commit'][:12]}… = S")
pr = m.get("preenregistrement") or {}
sha_p = Path(p + ".sha256").read_text().split()[0]
(ok if pr.get("chemin") == p and pr.get("sha256") == sha_p else ko)(f"3b préenregistrement {pr.get('chemin')} {str(pr.get('sha256'))[:12]}…")
(ok if empreinte_config(m["config"]) == cfg_c else ko)(f"3c configuration du manifeste = configuration citée ({str(cfg_c)[:12]}…)")
ents = {g["entropie"] for g in m["graines"].values()}
(ok if ents == {ent_c} else ko)(f"3d entropie citée ({len(m['graines'])} graines)")
v = m.get("versions") or {}
(ok if v.get("torch") and v.get("transformers") else ko)(f"3f versions : torch {v.get('torch')}, transformers {v.get('transformers')}")
(ok if m["config"].get("mode") == "reel" and m.get("decisif") is True and m.get("depot_propre") is True else ko)(
    f"3e mode {m['config'].get('mode')}, décisif {m.get('decisif')}, dépôt propre {m.get('depot_propre')}")
d = Path("diag") / run
r, a = (d / "resume.json").exists(), (d / "arret.json").exists()
(ok if r != a else ko)(f"4a issue : resume.json {r}, arret.json {a}")
corps = json.loads((d / ("resume.json" if r else "arret.json")).read_text())["resultat"]
t_sha = corps.get("taches_sha256") or corps.get("partiel", {}).get("taches_sha256")
(ok if t_sha == taches_c else ko)(f"4b tâches du run = tâches citées ({str(taches_c)[:12]}…)")
if a:
    print("    arrêt :", json.dumps({x: corps.get(x) for x in ("etape", "motif")}, ensure_ascii=False)[:600])
    print("    partiel :", json.dumps(corps.get("partiel"), ensure_ascii=False)[:900])
    print("    fichiers de résultats écrits :", " ".join(sorted(x.name for x in d.glob("*.json"))))
if r:
    # run complet (CH-09) : fichiers exigés et comptes exacts, recalculés par les fonctions du code cité
    cfg = m["config"]
    juges = [j["nom"] for j in cfg["juges"]]
    app_j = [j["nom"] for j in cfg["juges"] if j["sert_a_l_appariement"]]
    exiges = ["episodes.json", "appariements.json"] + [f"notations-{j}-{e}.json" for j in juges
                                                       for e in ("decisives", "descriptives")]
    manque = [x for x in exiges if not (d / x).is_file()]
    (ok if not manque else ko)(f"4c fichiers d'un run complet ({len(exiges)}) : {'tous présents' if not manque else 'manquent ' + ' '.join(manque)}")
    if not manque and chemin_t:
        taches = charger_taches(chemin_t)
        par_id = {x["identifiant"]: x for x in taches}
        fiches = json.loads((d / "episodes.json").read_text())["resultat"]["fiches"]
        n_ep = len(taches) * cfg["episodes_par_tache"]
        (ok if len(fiches) == n_ep == corps.get("episodes") else ko)(
            f"4d épisodes : {len(fiches)} écrits, {corps.get('episodes')} au résumé, {n_ep} attendus ({len(taches)} tâches)")
        decisifs = {str(x) for x in cfg["episodes_decisifs"]}
        attendu = {"decisives": 0, "descriptives": 0}
        for f in fiches:
            if f["bilan"]["ensemble"].strip():
                cle = "decisives" if f["episode"].rsplit("/e", 1)[1] in decisifs else "descriptives"
                attendu[cle] += lp.passes_de(f["episode"], cfg)
        for j in juges:
            n = {e: len(json.loads((d / f"notations-{j}-{e}.json").read_text())["resultat"]["notations"])
                 for e in ("decisives", "descriptives")}
            n_res = (corps.get("notations") or {}).get(j, {}).get("n")
            (ok if n == attendu and n_res == sum(n.values()) else ko)(
                f"4e notations du juge {j} : {n['decisives']} décisives, {n['descriptives']} descriptives "
                f"(attendues {attendu['decisives']} et {attendu['descriptives']}) ; résumé {n_res}")
        ap = json.loads((d / "appariements.json").read_text())["resultat"]
        n_app = len(lp.paires_d_appariement(fiches, par_id)); n_en = len(lp.paires_enonce_seul(list(par_id.values())))
        (ok if [ap.get("juge")] == app_j and len(ap["appariements"]) == n_app and len(ap["enonce_seul"]) == n_en else ko)(
            f"4f appariement par {ap.get('juge')} : {len(ap['appariements'])} paires (attendues {n_app}), énoncé seul "
            f"{len(ap['enonce_seul'])} (attendues {n_en})")
    elif not chemin_t:
        ko("4d chemin des tâches non cité par le préenregistrement")
ep = d / "episodes.json"
if ep.exists():
    v = json.loads(ep.read_text())["resultat"]
    (Path(trav) / "vecteurs-attendus.txt").write_text(f"{v['vecteurs_sha256']}\n")
    print("    vecteurs attendus :", v["vecteurs_sha256"], v["vecteurs"])
sys.exit(1 if k else 0)
EOF
if [ -f "$TRAV/vecteurs-attendus.txt" ]; then
    VA=$(cat "$TRAV/vecteurs-attendus.txt")
    if git fetch -q origin "donnees/t05/$RUN" 2>/dev/null; then
        VB=$(git rev-parse FETCH_HEAD)
        [ -z "$(git log --format=%P -1 "$VB")" ] && ok "5a branche donnees/t05/$RUN : un commit sans parent" || ko "5a branche des vecteurs : commit avec parent"
        VS=$(git show "$VB:$RUN/vecteurs-par-action.npz" | sha256sum | cut -d' ' -f1)
        [ "$VS" = "$VA" ] && [ "$(git show "$VB:$RUN/vecteurs-par-action.npz.sha256" | cut -d' ' -f1)" = "$VA" ] \
            && ok "5b vecteurs : empreinte égale au sceau et à episodes.json ($VA)" || ko "5b vecteurs : empreinte $VS ≠ $VA"
    else ko "5a branche donnees/t05/$RUN absente : vecteurs restés sur l'instance ? instance gardée (PL-11)"; fi
else echo "--  5 pas d'episodes.json : aucun vecteur attendu"; fi
# 6. journal de l'instance versé dans les traces de ce run (dernier dossier nouveau) ; aucun dossier nouveau : KO (VC-05)
[ -n "$NOUVELLES" ] || ko "6 aucune trace versée sur la branche (poussée finale en échec ?) : instance gardée, traces à reprendre"
J=$(printf '%s\n' $NOUVELLES | tail -1)
A=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
for motif in "$A tests attendus" "poussée avant l'installation" "disponible True" "tests : $A passed"; do
    grep -qF "$motif" "$J/journal.txt" 2>/dev/null && ok "6 journal ($J) : « $motif »" || ko "6 journal ($J) : « $motif » absent"
done
grep -E "vecteurs (absents|trop gros|: empreinte non conforme|: poussée impossible)" "$J/journal.txt" 2>/dev/null | sed 's/^/KO? journal : /' || true
# 6b. carte et mémoire (nvidia-smi.txt) ; 6c. pip freeze (descriptif) ; CH-09
# fichiers cherchés dans tous les dossiers de traces nouveaux, non dans le seul dernier (VC-05)
NS=$(for d in $NOUVELLES; do [ -f "$d/nvidia-smi.txt" ] && echo "$d/nvidia-smi.txt"; done | head -1)
PF=$(for d in $NOUVELLES; do [ -f "$d/pip-freeze.txt" ] && echo "$d/pip-freeze.txt"; done | head -1)
if [ "$CARTE_EXIGEE" = oui ]; then
    CARTE=$(sed -n '2p' "${NS:-/dev/null}" 2>/dev/null)
    MIB=$(printf '%s\n' "$CARTE" | sed -n 's/.*, *\([0-9][0-9]*\) MiB *$/\1/p')
    if [[ "$CARTE" == *A100* && "$CARTE" == *SXM4* ]] && [ -n "$MIB" ] && [ "$MIB" -ge 76800 ]; then ok "6b carte : $CARTE"
    else ko "6b carte ou mémoire inattendue (A100 SXM4, au moins 75 Gio) : « $CARTE »"; fi
else echo "--  6b carte non exigée (répétition sur processeur)"; fi
if [ -n "$PF" ] && grep -q '^torch==' "$PF" && grep -q '^transformers==' "$PF"; then
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
if [ "$echecs" = 0 ]; then echo "RÉCUPÉRATION : TOUS CONFORMES"; else echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"; exit 1; fi
