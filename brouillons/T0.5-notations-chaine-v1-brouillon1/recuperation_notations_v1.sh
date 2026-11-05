#!/usr/bin/env bash
# Contrôles de récupération des notations refaites du pilote de T0.5 (N-021, option (a)), avant toute fusion et avant
# toute proposition de destruction de l'instance ; déclinés de recuperation_pilote_v1.sh selon l'état des lieux de la
# voie « notations seules » (chaine.md, section 4 ; critique adverse, constats 9 et 10). Clone propre du dépôt de travail ;
# rien n'est fusionné ni poussé ici. Aucune valeur de jeton, aucun texte de réponse ni d'ensemble n'est affiché.
# Ce qui est contrôlé : ascendance (S ancêtre), ajouts seulement, sous runs/<R′>/, diag/<R′>/ et traces/t05-*/
# seulement, rien sous les dossiers du pilote noté ; un seul run « …-t05-notations-reel » ; auteurs ; sceaux ; manifeste
# et citations (commit, préenregistrement, configuration, entropie et graines égales à celles du pilote, versions égales
# à celles du pilote, mode, décisif, dépôt propre) ; issue (résumé ou arrêt, un seul) ; pièces rattachées au pilote cité ;
# fichiers de notations exactement ceux des juges « écrit » (cas « un seul fichier » compris : juge échu sans fichier,
# consigné au résumé, constat 9) ; pour chaque fichier : 180 notations, clés et ordre des demandes décisives recalculés
# depuis les épisodes scellés du pilote, alignées par l'empreinte de l'ensemble noté ; aucun vecteur attendu ; journal
# (tests, poussée initiale, carte, lignes de progression conformes au motif fixe) ; carte et mémoire ; pip freeze ; jetons.
# Relance : la branche du premier lancement (…-v1) est lue et citée ; elle ne doit porter aucun fichier de notations.
# Usage : recuperation_notations_v1.sh S DOSSIER_NEUF [relance]
set -uo pipefail
SOI=$(realpath "$0")
S=${1:?commit de scellement}; D=$(realpath -m "${2:?dossier neuf}"); MODE=${3:-premier}
TRAV="$D.travail"                # fichiers de travail dans un dossier neuf, jamais dans le parent partagé
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
PY=$B/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/T0.5-pilote-notations-v1.md
PREMIERE=calcul/t05-notations-reel-v1
case "$MODE" in premier) BRANCHE=$PREMIERE ;; relance) BRANCHE=calcul/t05-notations-reel-v2 ;; *) echo "mode : relance, ou rien"; exit 2 ;; esac
CARTE_EXIGEE=oui                 # A100 SXM4 d'au moins 75 Gio (nvidia-smi.txt des traces) ; la répétition jouet passe « non »
COPIE_EXIGEE=oui                 # ce script égal à sa copie versée à S ; la répétition jouet, qui joue une copie modifiée, passe « non »
MOTIF_RUN='^[0-9]{8}-[0-9]{6}-t05-notations-reel$'
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'
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
    [ "$(git show "$S:docs/procedures/notations-T0.5-v1/recuperation_notations_v1.sh" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$SOI" | cut -d' ' -f1)" ] \
        && ok "0 récupération exécutée = copie versée à S" || ko "0 récupération exécutée ≠ copie versée à S"
fi
PILOTE=$(sed -n "s/.*Run du pilote noté : \`\([0-9]\{8\}-[0-9]\{6\}-[A-Za-z0-9_.-]*\)\`.*/\1/p" "$P" | head -1)
[ -n "$PILOTE" ] || { echo "run du pilote noté non cité par $P"; exit 2; }
# 0. relance : branche du premier lancement lue et citée ; elle ne doit porter aucun fichier de notations (préséance)
if [ "$MODE" = relance ]; then
    if git fetch -q origin "$PREMIERE" 2>/dev/null; then
        V1=$(git rev-parse FETCH_HEAD)
        echo "branche du premier lancement $PREMIERE : tête $V1 ; runs : $(git diff --name-only "$S" "$V1" | grep -E '^diag/' | cut -d/ -f2 | sort -u | tr '\n' ' ')"
        # liste écrite dans un fichier, code de git exigé : jamais de tube vers grep -q sous pipefail
        if git ls-tree -r --name-only "$V1" > "$TRAV/arbre-v1.txt"; then
            if grep -qE '/notations-[^/]+\.json$' "$TRAV/arbre-v1.txt"; then ko "0 $PREMIERE porte un fichier de notations : relancement contraire à la préséance"
            else ok "0 $PREMIERE lue, sans fichier de notations ($(wc -l < "$TRAV/arbre-v1.txt") chemins lus)"; fi
        else ko "0 $PREMIERE : arbre illisible"; fi
    else ko "0 $PREMIERE introuvable : relance sans premier lancement"; fi
fi
# 1. ascendance et contenu
git merge-base --is-ancestor "$S" "$H" && ok "1a S est ancêtre de la branche" || ko "1a S n'est pas ancêtre de la branche"
git diff --name-status "$S" "$H" > "$TRAV/diff-status.txt"
NON_AJOUTS=$(grep -vc '^A' "$TRAV/diff-status.txt" || true)
[ "$NON_AJOUTS" = 0 ] && ok "1b seulement des ajouts ($(wc -l < "$TRAV/diff-status.txt") fichiers)" || ko "1b $NON_AJOUTS changement(s) autre(s) qu'un ajout"
cut -f2 "$TRAV/diff-status.txt" > "$TRAV/chemins.txt"
HORS=$(grep -vE '^(runs/[^/]+/|diag/[^/]+/|traces/t05-[^/]+/)' "$TRAV/chemins.txt" || true)
DANS_PILOTE=$(grep -E "^(runs|diag)/$PILOTE/" "$TRAV/chemins.txt" || true)
[ -z "$HORS" ] && [ -z "$DANS_PILOTE" ] && ok "1c ajouts sous runs/, diag/ et traces/t05-*/ seulement, rien sous les dossiers du pilote noté ($PILOTE)" \
    || ko "1c chemins hors périmètre ou dans le pilote noté : $HORS $DANS_PILOTE"
RUNS=$(grep -E '^(runs|diag)/' "$TRAV/chemins.txt" | grep -vE "^(runs|diag)/$PILOTE/" | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
if [ "$NRUNS" = 1 ] && [[ "$RUN" =~ $MOTIF_RUN ]]; then ok "1d un seul run : $RUN"; else ko "1d runs : $RUNS"; fi
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
# 3. manifeste et citations ; 4. issue, fichiers et comptes
PYTHONPATH=src "$PY" - "$RUN" "$S" "$P" "$PILOTE" <<'EOF' || echecs=$((echecs + 1))
import hashlib, json, re, sys
from pathlib import Path
from controle_ia.manifeste import lire_manifeste, verifier_resultat
from controle_ia.environnements import noter_pilote_a as npa
from controle_ia.environnements.lancer_pilote_a import empreinte_config
from controle_ia.environnements.pilote_a import charger_taches
run, s, p, pilote = sys.argv[1:5]
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
texte = Path(p).read_text(encoding="utf-8")
cite = lambda motif: (re.search(motif, texte) or [None, None])[1]
cfg_c, taches_c, ent_c = cite(r"Configuration des notations \(empreinte canonique\) : `([0-9a-f]{64})`"), \
    cite(r"Tâches du pilote : `([0-9a-f]{64})`"), cite(r"Entropie : `([0-9]+)`")
ep_c = cite(r"Épisodes du pilote noté : `([0-9a-f]{64})`")
chemin_t = cite(r"Chemin des tâches du pilote noté : `([^`]+)`")
m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
mp, sha_mp = lire_manifeste(f"runs/{pilote}/manifeste.json")
(ok if m["commit"] == s else ko)(f"3a commit du manifeste {m['commit'][:12]}… = S")
pr = m.get("preenregistrement") or {}
sha_p = Path(p + ".sha256").read_text().split()[0]
(ok if pr.get("chemin") == p and pr.get("sha256") == sha_p else ko)(f"3b préenregistrement {pr.get('chemin')} {str(pr.get('sha256'))[:12]}…")
(ok if empreinte_config(m["config"]) == cfg_c else ko)(f"3c configuration du manifeste = configuration citée ({str(cfg_c)[:12]}…)")
ents = {g["entropie"] for g in m["graines"].values()}
egales = all(mp["graines"].get(c) == g for c, g in m["graines"].items())
(ok if ents == {ent_c} and egales else ko)(f"3d entropie citée, graines égales à celles du pilote, clé à clé ({len(m['graines'])} graines)")
(ok if m["config"].get("mode") == "reel" and m.get("decisif") is True and m.get("depot_propre") is True else ko)(
    f"3e mode {m['config'].get('mode')}, décisif {m.get('decisif')}, dépôt propre {m.get('depot_propre')}")
v, vp = m.get("versions") or {}, mp.get("versions") or {}
ecarts = [b for b in npa.VERSIONS_EGALES if v.get(b) != vp.get(b)]
(ok if not ecarts and v.get("torch") else ko)(f"3f versions égales à celles du pilote : torch {v.get('torch')}, transformers {v.get('transformers')} ; écarts {ecarts}")
d = Path("diag") / run
r, a = (d / "resume.json").exists(), (d / "arret.json").exists()
(ok if r != a else ko)(f"4a issue : resume.json {r}, arret.json {a}")
corps = json.loads((d / ("resume.json" if r else "arret.json")).read_text())["resultat"]
rattache = corps if r else corps.get("partiel", {})
(ok if rattache.get("run_pilote") == pilote and rattache.get("taches_sha256") == taches_c and rattache.get("episodes_sha256") == ep_c else ko)(
    f"4b run rattaché au pilote cité ({pilote}), tâches et épisodes cités")
juges = rattache.get("juges") or {}
if a:
    print("    arrêt :", json.dumps({x: corps.get(x) for x in ("etape", "motif")}, ensure_ascii=False)[:600])
for nom, j in juges.items():
    print(f"    juge {nom} : statut {j.get('statut')} ; lots faits {j.get('lots_faits')}/{j.get('lots')} ; durée {j.get('duree_s')} s ; "
          f"notations {j.get('notations')} ; complètes {j.get('completes')} ; mémoire {j.get('memoire_pic_gio')} Gio")
ecrits = sorted(n for n, j in juges.items() if j.get("statut") == "écrit")
statuts_permis = {"écrit", "échu"} if r else {"écrit", "échu", "en cours"}
presents = sorted(x.name for x in d.glob("notations-*.json"))
attendus = [f"notations-{n}-decisives.json" for n in sorted(ecrits)]
autres = sorted(x.name for x in d.glob("*.json") if x.name not in presents and x.name not in ("resume.json", "arret.json"))
(ok if presents == attendus and not autres and all(j.get("statut") in statuts_permis for j in juges.values())
     and (not r or sorted(juges) == sorted(j["nom"] for j in m["config"]["juges"])) else ko)(
    f"4c fichiers de notations = juges « écrit » : présents {presents}, attendus {attendus}, autres {autres}")
taches = charger_taches(chemin_t) if chemin_t else []
par_id = {t["identifiant"]: t for t in taches}
pil = {"fiches": verifier_resultat(Path("."), Path(f"diag/{pilote}/episodes.json"))["resultat"]["fiches"]}
ensembles = {f["episode"]: hashlib.sha256(f["bilan"]["ensemble"].encode("utf-8")).hexdigest() for f in pil["fiches"]}
for nom in ecrits:
    f = d / f"notations-{nom}-decisives.json"
    if not f.exists():
        continue
    notes = json.loads(f.read_text())["resultat"]["notations"]
    dem = npa.demandes_decisives(pil, par_id, m["config"], nom)
    cles = [x["cle"] for x in notes]
    alignes = all(n["ensemble_sha256"] == ensembles.get(n["cle"].split("/", 1)[1].rsplit("/", 1)[0]) for n in notes)
    (ok if len(notes) == m["config"]["notations_attendues_par_juge"] == len(dem) and cles == [x["cle"] for x in dem]
         and len(set(cles)) == len(cles) and alignes and juges[nom].get("notations") == len(notes) else ko)(
        f"4d juge {nom} : {len(notes)} notations (attendues {len(dem)}), clés dans l'ordre des demandes, alignées sur les ensembles du pilote : {alignes}")
sys.exit(1 if k else 0)
EOF
echo "--  5 aucun vecteur attendu (notations seules)"
# 6. journal de l'instance versé dans les traces de ce run (dernier dossier nouveau) ; aucun dossier nouveau : KO
[ -n "$NOUVELLES" ] || ko "6 aucune trace versée sur la branche (poussée finale en échec ?) : instance gardée, traces à reprendre"
J=$(printf '%s\n' $NOUVELLES | tail -1)
A=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
for motif in "$A tests attendus" "poussée avant l'installation" "disponible True" "tests : $A passed"; do
    grep -qF "$motif" "$J/journal.txt" 2>/dev/null && ok "6 journal ($J) : « $motif »" || ko "6 journal ($J) : « $motif » absent"
done
grep '^PROGRES ' "$J/journal.txt" > "$TRAV/progres.txt" 2>/dev/null || true
NP=$(grep -c . "$TRAV/progres.txt" || true); NPC=$(grep -cE "$MOTIF_PROGRES" "$TRAV/progres.txt" || true)
[ "$NP" -ge 1 ] && [ "$NP" = "$NPC" ] && ok "6 lignes de progression au journal : $NP, toutes au motif fixe" || ko "6 lignes de progression : $NP, dont $NPC au motif fixe"
# 6b. carte et mémoire (nvidia-smi.txt) ; 6c. pip freeze (descriptif) ; fichiers cherchés dans tous les dossiers nouveaux
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
