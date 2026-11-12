#!/usr/bin/env bash
# Contrôles de récupération de la revalidation (T0.5), version 2 du préenregistrement (N-018), avant toute fusion
# (plan de lancement v5, étape 7, points 1 à 6). Depuis la v1 de ce script : branche et préenregistrement de la v2.
# Clone propre du dépôt de travail, branche de calcul récupérée ; rien n'est fusionné ni poussé ici.
# Aucune valeur de jeton n'est affichée : seule leur présence est comptée.
# Usage : recuperation_revalidation_v2.sh S DOSSIER_NEUF
set -uo pipefail
S=${1:?commit de scellement}; D=${2:?dossier neuf}
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
PY=$B/scellement-revalidation/venv-gpu-neuf/bin/python
BRANCHE=calcul/t05-revalidation-reel-v2
P=prereg/T0.5-revalidation-equivalence-pilote-v2.md
CANON=50930b3794216c3b857cd906d8b2066eb495534d637041f4d089aa00a9edeefb
ENTROPIE=120571628831802510081029698987406594891
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
echecs=0
ok() { echo "OK  $*"; }
ko() { echo "KO  $*"; echecs=$((echecs + 1)); }
git clone -q https://github.com/lciric/controle-ia-travail.git "$D" || { echo "clonage impossible"; exit 2; }
cd "$D"
git fetch -q origin "$BRANCHE" || { echo "branche $BRANCHE introuvable"; exit 2; }
H=$(git rev-parse FETCH_HEAD); echo "tête de la branche : $H"
git checkout -q --detach "$H"
# 1. ascendance et contenu
git merge-base --is-ancestor "$S" "$H" && ok "1a S est ancêtre de la branche" || ko "1a S n'est pas ancêtre de la branche"
git diff --name-status "$S" "$H" > ../diff-status.txt
NON_AJOUTS=$(grep -vc '^A' ../diff-status.txt || true)
[ "$NON_AJOUTS" = 0 ] && ok "1b seulement des ajouts ($(wc -l < ../diff-status.txt) fichiers)" || ko "1b $NON_AJOUTS changement(s) autre(s) qu'un ajout"
HORS=$(cut -f2 ../diff-status.txt | grep -vE '^(runs/[^/]+/|diag/[^/]+/|traces/t05-[^/]+/)' || true)
[ -z "$HORS" ] && ok "1c ajouts sous runs/, diag/ et traces/t05-*/ seulement" || ko "1c chemins hors périmètre : $HORS"
RUNS=$(cut -f2 ../diff-status.txt | grep -E '^(runs|diag)/' | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
if [ "$NRUNS" = 1 ] && [[ "$RUN" =~ ^[0-9]{8}-[0-9]{6}-t05-revalidation-reel$ ]]; then ok "1d un seul run : $RUN"; else ko "1d runs : $RUNS"; fi
AUTEURS=$(git log --format='%an' "$S..$H" | sort -u)
[ "$AUTEURS" = "instance de calcul (T0.5)" ] && ok "1e commits de « instance de calcul (T0.5) » ($(git rev-list --count "$S..$H"))" || ko "1e auteurs : $AUTEURS"
# 2. sceaux
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > ../verifier-arbre.txt 2>&1 && ok "2a verifier-arbre : $(tail -1 ../verifier-arbre.txt)" || ko "2a verifier-arbre : $(tail -3 ../verifier-arbre.txt)"
for f in diag/"$RUN"/*.json; do
    PYTHONPATH=src "$PY" -c "from controle_ia.manifeste import verifier_resultat; verifier_resultat('.', '$f')" 2>../vr.err \
        && ok "2b verifier_resultat $f" || ko "2b verifier_resultat $f : $(tail -1 ../vr.err)"
done
for d in traces/t05-*/; do
    git cat-file -e "$S:${d%/}" 2>/dev/null && continue        # dossiers de traces déjà présents à S : hors de ce run
    (cd "$d" && sha256sum -c --quiet empreintes.sha256) > ../sc.txt 2>&1 && ok "2c sha256sum -c $d" || ko "2c $d : $(head -2 ../sc.txt)"
done
# 3. manifeste ; 4. issue
PYTHONPATH=src "$PY" - "$RUN" "$S" "$P" "$CANON" "$ENTROPIE" <<'EOF' || echecs=$((echecs + 1))
import json, sys
from pathlib import Path
from controle_ia.manifeste import lire_manifeste, config_canonique
import hashlib
run, s, p, canon, entropie = sys.argv[1:6]
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
m, sha_m = lire_manifeste(f"runs/{run}/manifeste.json")
(ok if m["commit"] == s else ko)(f"3a commit du manifeste {m['commit'][:12]}… = S")
pr = m.get("preenregistrement") or {}
sha_p = Path(p + ".sha256").read_text().split()[0]
(ok if pr.get("chemin") == p and pr.get("sha256") == sha_p else ko)(f"3b préenregistrement {pr.get('chemin')} {str(pr.get('sha256'))[:12]}…")
cles = ("taches_entrainement", "taches_entrainement_sha256", "taches_evaluation", "taches_evaluation_sha256")
c = {x: y for x, y in m["config"].items() if x not in cles}
(ok if all(x in m["config"] for x in cles) else ko)("3c quatre clés des tâches présentes")
(ok if hashlib.sha256(config_canonique(c)).hexdigest() == canon else ko)("3d configuration sans les clés des tâches = 50930b37…")
ents = {g["entropie"] for g in m["graines"].values()}
(ok if ents == {entropie} else ko)(f"3e entropie citée ({len(m['graines'])} graines)")
v = m["versions"]
(ok if "torch" in v and "transformers" in v else ko)(f"3f versions : torch {v.get('torch')}, transformers {v.get('transformers')}")
(ok if m["config"].get("mode") == "reel" and m.get("decisif") is True and m.get("depot_propre") is True else ko)(
    f"3g mode {m['config'].get('mode')}, décisif {m.get('decisif')}, dépôt propre {m.get('depot_propre')}")
d = Path("diag") / run
r, a = (d / "resume.json").exists(), (d / "arret.json").exists()
(ok if r != a else ko)(f"4a issue : resume.json {r}, arret.json {a}")
if r:
    res = json.loads((d / "resume.json").read_text())["resultat"]
    carte = str(res.get("carte"))
    (ok if "A100" in carte.split() or "A100" in carte.replace("-", " ").split() else ko)(f"4b carte : {carte}")
    mem = res.get("memoire_carte_gio")
    (ok if isinstance(mem, (int, float)) and mem >= 75 else ko)(f"4c mémoire de la carte : {mem} Gio")
    print("    noyau retenu :", res.get("noyau_retenu"), "; nœud :", res.get("noeud"), "; réserves :", res.get("reserves"))
if a:
    arr = json.loads((d / "arret.json").read_text())["resultat"]
    print("    arrêt :", json.dumps({x: arr.get(x) for x in ("etape", "motif", "bras_lus", "noyau_retenu_sur_les_bras_lus")}, ensure_ascii=False)[:600])
sys.exit(1 if k else 0)
EOF
# 5. journal de l'instance versé dans les traces de ce run
J=$(for d in traces/t05-*/; do git cat-file -e "$S:${d%/}" 2>/dev/null || echo "$d"; done | tail -1)
for motif in "670 tests attendus" "poussée avant l'installation" "disponible True" "tests : 670 passed"; do
    grep -qF "$motif" "$J/journal.txt" 2>/dev/null && ok "5 journal ($J) : « $motif »" || ko "5 journal ($J) : « $motif » absent"
done
# 6. aucune valeur de jeton dans le différentiel ni dans les fichiers ajoutés (comptée, jamais affichée)
git diff "$S" "$H" > ../diff-complet.txt
python3 - ../diff-complet.txt ../diff-status.txt <<'EOF' || echecs=$((echecs + 1))
import os, sys
from pathlib import Path
diff = Path(sys.argv[1]).read_bytes()
fichiers = [l.split("\t", 1)[1] for l in Path(sys.argv[2]).read_text().splitlines() if "\t" in l]
k = 0
for nom in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(nom)
    if not v or len(v) < 8:
        print(f"--  6 {nom} absent de l'environnement de la session : non recherché"); continue
    b = v.encode()
    n = diff.count(b) + sum(Path(f).read_bytes().count(b) for f in fichiers if Path(f).is_file())
    print(("OK " if n == 0 else "KO ") + f" 6 valeur de {nom} : {n} occurrence(s)")
    k += n > 0
sys.exit(1 if k else 0)
EOF
echo "RUN=$RUN"; echo "TETE=$H"
[ "$echecs" = 0 ] && echo "RÉCUPÉRATION : TOUS CONFORMES" || echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"
