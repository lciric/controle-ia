#!/usr/bin/env bash
# Épreuve E1 du lanceur de T0.6 v6 (filtre de fiabilité de la création, 0 USD ; l amorce reste la v4, inchangée) : répétition jouet avec le VRAI lanceur v4
# (`controle_ia.t06.lanceur_v4`, modèle par caractères) sous la VRAIE amorce v4, sans réseau : dépôt distant simulé par un
# dépôt git local nu, outil de location absent, aucune minuterie (AMORCE_ESSAI_LOCAL=1), environnement Python existant.
# Relève : lignes PROGRES du journal de l'amorce ; preuve qu'aucun état de sonde, aucune aire, aucune ligne de table ne
# figure dans le journal, run.err, run.json ni les traces poussées ; morceaux du sous-ensemble poussés, chacun sous 90 Mo ;
# commits (données légères, morceaux, traces) ; état du disque de l'instance simulée (fin normale, arrêt demandé).
#   bash scripts/epreuve_e1_t06_v6.sh DOSSIER_DE_TRAVAIL_NEUF
# Variables : VENV (défaut : .venv du dépôt) ; TESTS_ARGS_E1 (essais joués par l'amorce avant le run, défaut : les essais de
# configuration et de session v2, de configuration et de familles v3 et v4, rapides) ; TESTS_ATTENDUS_E1 (nombre attendu, défaut
# 73) ; MAHALANOBIS_CALCUL_E1 (clé `mahalanobis_calcul` de la configuration jouet v5 écrite pour l'épreuve : défaut
# « paquet_gele », ou « produit_matriciel_v2 » pour la mesure de durée de C-V3-4).
set -euo pipefail
W=$(realpath -m "${1:?dossier de travail neuf}")
[ -e "$W" ] && { echo "$W existe déjà (R12)"; exit 2; }
DEPOT=$(cd "$(dirname "$0")/.." && pwd)
VENV="${VENV:-$DEPOT/.venv}"
[ -x "$VENV/bin/python" ] || { echo "environnement $VENV absent"; exit 2; }
command -v vastai >/dev/null 2>&1 && { echo "vastai présent sur le chemin : E1 exige son absence (aucun appel à Vast)"; exit 2; }
mkdir -p "$W"
SRC="$W/source"; mkdir -p "$SRC"
CALCUL_E1="${MAHALANOBIS_CALCUL_E1:-paquet_gele}"
REELS_E1="${JETONS_REELS_E1:-false}"
echo "E1 : $(date -u +%FT%TZ) : dépôt source réduit sous $SRC (code v2 et v3, essais v2 et v3, consignes de P3, configuration jouet v4 (mahalanobis_calcul=$CALCUL_E1), tâches synthétiques)"
for c in src/controle_ia tests/conftest.py tests/test_t06_v2_configuration.py tests/test_t06_v2_session.py tests/test_t06_v2_lanceur_jouet.py \
         tests/test_t06_v3_configuration.py tests/test_t06_v3_familles.py tests/test_t06_v3_lanceur_jouet.py tests/test_t06_v4_configuration.py tests/test_t06_v4_familles.py scripts pyproject.toml \
         prereg/P3-consignes-v1.md prereg/P3-consignes-v1.md.sha256 docs/notes/g0-deux-semaines-v1/config-t06-jouet-v3.json docs/notes/g0-deux-semaines-v1/config-t06-jouet-v4.json docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json \
         docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon2.json docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon3.json docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v1.json docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v1.json \
         docs/sources/invites-2606.08892-v1 .claude/hooks/garde_calcul.py registres/go.md .gitignore; do
    mkdir -p "$SRC/$(dirname "$c")"; cp -r "$DEPOT/$c" "$SRC/$c"
done
find "$SRC" -name __pycache__ -type d -prune -exec rm -rf {} +
mkdir -p "$SRC/runs" "$SRC/diag" "$SRC/donnees/t06-jouet"; : > "$SRC/runs/.gitkeep"; : > "$SRC/diag/.gitkeep"
cd "$SRC"
PYTHONPATH=src MAHALANOBIS_CALCUL_E1="$CALCUL_E1" JETONS_REELS_E1="$REELS_E1" "$VENV/bin/python" - <<'EOF'
import json
import os
from pathlib import Path
from controle_ia.scellement import sceller
ENONCES = ["Which routing rule makes sparse mixtures of experts train stably?", "Does curriculum ordering change sample efficiency of small language models?",
           "Can retrieval reduce hallucination in long-form question answering?", "How does tokenizer vocabulary size affect multilingual transfer?",
           "Do sparse autoencoders recover known features in toy models?", "Is chain-of-thought faithful under distribution shift?"]
def taches(ids):
    return {"taches": [{"identifiant": i, "questions": ENONCES[k % len(ENONCES)] + f" ({i})"} for k, i in enumerate(ids)]}
d = Path("donnees/t06-jouet")
(d / "taches-evaluation.json").write_text(json.dumps(taches(["e1", "e2", "e3", "e4"]), ensure_ascii=False), encoding="utf-8")
(d / "taches-distillation.json").write_text(json.dumps(taches(["d1", "d2"]), ensure_ascii=False), encoding="utf-8")
c = json.loads(Path("docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json").read_text(encoding="utf-8"))
c["taches_evaluation"]["sha256"] = sceller(d / "taches-evaluation.json")
c["taches_distillation"]["sha256"] = sceller(d / "taches-distillation.json")
c["mahalanobis_calcul"] = os.environ["MAHALANOBIS_CALCUL_E1"]
c["egalite_jetons_reels"] = os.environ["JETONS_REELS_E1"] == "true"          # C-V4-2 : vrai seulement sous produit_matriciel_v2
Path("prereg").mkdir(exist_ok=True)
Path("prereg/T0.6-config-jouet-e1.json").write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
sceller(Path("prereg/T0.6-config-jouet-e1.json"))
EOF
git init -q -b main . && git config user.email e1@example.invalid && git config user.name e1 && git add -A && git add -f donnees/t06-jouet && git commit -qm "E1 : dépôt source réduit"
COMMIT=$(git rev-parse HEAD)
DISTANT="$W/distant.git"; git clone -q --bare "$SRC" "$DISTANT"
R="$W/instance"; mkdir -p "$R"
echo "E1 : $(date -u +%FT%TZ) : amorce v4 sur l'instance simulée $R, commit $COMMIT, dépôt distant $DISTANT"
set +e
env -i PATH="$PATH" HOME="$W" LANG="${LANG:-C.UTF-8}" TMPDIR="${TMPDIR:-/tmp}" COMMIT="$COMMIT" MODE=jouet DEPOT_URL="$DISTANT" GH_TOKEN=jeton-factice-e1 \
    RACINE_AMORCE="$R" VENV_EXISTANT="$VENV" PREREG_ABSENT=1 CONFIG=prereg/T0.6-config-jouet-e1.json TESTS_ATTENDUS="${TESTS_ATTENDUS_E1:-73}" \
    TESTS_ARGS="${TESTS_ARGS_E1:-tests/test_t06_v2_configuration.py tests/test_t06_v2_session.py tests/test_t06_v3_configuration.py tests/test_t06_v3_familles.py tests/test_t06_v4_configuration.py tests/test_t06_v4_familles.py}" AMORCE_ESSAI_LOCAL=1 \
    FIN_GO_UTC_S=1794873600 ECHEANCE_UTC_S=1794873600 DEPENSE_EPUISEE_UTC_S=1794873600 POUSSEE_ATTENTE_S=0 \
    timeout -k 10 900 nice -n 10 bash "$DEPOT/scripts/amorce_instance_t06_v4.sh" > "$W/amorce-sortie.txt" 2>&1
CODE=$?
set -e
echo "E1 : $(date -u +%FT%TZ) : amorce terminée, code $CODE"
J="$R/t06/journal.txt"; T="$R/t06"
RES="$W/resultat-e1.txt"
{
    echo "# Résultat de l'épreuve E1 ($(date -u +%FT%TZ)), code de l'amorce $CODE"
    echo "## lignes PROGRES relevées au journal de l'amorce"; grep '^PROGRES ' "$J" || echo "(aucune)"
    echo "## lignes AMORCE (sortie)"; grep '^AMORCE ' "$W/amorce-sortie.txt" || true
    echo "## mots interdits (au-dessus, non interprétable, échec, ligne_A/B/C, table_, aire=, plancher) dans le journal, run.err, run.json, traces poussées"
    for f in "$J" "$T/run.err" "$T/run.json"; do printf '%s : %s occurrence(s)\n' "$f" "$(grep -ciE 'au-dessus|interprétable|échec|ligne_[ABC]|table_[ABC]|aire=|plancher' "$f" || true)"; done
    for f in $(cd "$R/amorce-depot" && git ls-tree -r --name-only HEAD | grep '^traces/'); do printf 'traces : %s : %s occurrence(s)\n' "$f" "$(cd "$R/amorce-depot" && git show "HEAD:$f" | grep -ciE 'au-dessus|interprétable|échec|ligne_[ABC]|table_[ABC]|aire=|plancher' || true)"; done
    echo "## run.json (sortie standard du lanceur, versée aux traces)"; cat "$T/run.json"
    echo "## commits poussés sur le dépôt distant (branche calcul/t06-jouet-v4)"; git -C "$DISTANT" log --format='%h %s' calcul/t06-jouet-v4
    echo "## fichiers poussés sous donnees/ (taille en octets)"; git -C "$DISTANT" ls-tree -r -l calcul/t06-jouet-v4 | grep -E 'donnees/' | awk '{print $4, $5}'
    echo "## plus gros fichier poussé (octets)"; git -C "$DISTANT" ls-tree -r -l calcul/t06-jouet-v4 | awk '$4 != "-" {print $4}' | sort -n | tail -1
    echo "## marqueurs sur le disque de l'instance simulée"; ls "$R" | grep -E '^t06-' || true; cat "$R/t06-arret-demande" 2>/dev/null || true
    echo "## résumé scellé (diag) : clés présentes (les lignes restent dans le résultat scellé, jamais sur run.json)"
    for f in "$R"/amorce-depot/diag/*/resume.json; do "$VENV/bin/python" -c "import json, sys; print(sorted(json.load(open(sys.argv[1]))['resultat'] if 'resultat' in json.load(open(sys.argv[1])) else json.load(open(sys.argv[1]))))" "$f"; done
    echo "## manifeste du sous-ensemble"; cat "$R"/amorce-depot/donnees/*/activations-sous-ensemble-t06-manifeste.json
    echo "## calcul de Mahalanobis et essais d'égalité (résultat scellé des sondes : calcul, nombre d'essais, tous égaux ; aucune aire)"
    for f in "$R"/amorce-depot/diag/*/lecture-sondes-t06.json; do "$VENV/bin/python" -c "import json, sys; r = json.load(open(sys.argv[1]))['resultat']; v = r['verifications_mahalanobis']; print(r['mahalanobis_calcul'], 'jetons_reels', r['egalite_jetons_reels'], len(v), 'essais dont', sum(1 for k in v if k.endswith('/reels')), 'sur jetons réels', all(x['egal'] for x in v.values()), 'écart max', max([x['ecart_relatif_max'] for x in v.values()] or [0.0]))" "$f"; done
    echo "## durées par couple descriptif (s)"; for f in "$R"/amorce-depot/diag/*/lecture-sondes-t06.json; do "$VENV/bin/python" -c "import json, sys; print(json.dumps(json.load(open(sys.argv[1]))['resultat']['durees_s']))" "$f"; done
    echo "## tests joués par l'amorce"; tail -1 "$T/tests.txt"
    echo "## empreintes"; (cd "$W" && sha256sum amorce-sortie.txt instance/t06/journal.txt instance/t06/run.json instance/t06/run.err)
} > "$RES"
echo "E1 : résultat écrit dans $RES"
cat "$RES"
exit "$CODE"
