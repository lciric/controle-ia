#!/usr/bin/env bash
# Essai à blanc v66 de bout en bout (fournisseurs simulés, deux générations, exécuteur factice déclaré). Aucun appel, aucun réseau.
# Usage : bash lancer_essai_a_blanc_v66.sh ARBRE_ORGANISME DOSSIER_SORTIES PYTHON [REGISTRE_GO] [DOSSIER_CONFIGURATION_V6]
# REGISTRE_GO (lecture seule) : le vrai registres/go.md du dépôt de travail, lu par le lecteur v66 (étape 13).
# DOSSIER_CONFIGURATION_V6 : le dossier de course (configuration v6, pieces/, commandes-v6/), vérifié par le lanceur (étape 14).
set -u
O="$1/orchestrator"; S="$2"; PY="$3"; REG="${4:-}"; CONF="${5:-}"; mkdir -p "$S"; cd "$O" || exit 9
etape() { local n="$1"; shift; local d=$(date -u +%H:%M:%S); "$@" > "$S/etape-$n.stdout" 2> "$S/etape-$n.stderr"; local c=$?;
          echo "étape $n | $d → $(date -u +%H:%M:%S) | code $c | $*"; }
sha() { sha256sum "$1/boucle-reelle-v66.json" | cut -c1-64; }
etape 1 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course-bac-reel" --a-blanc --graine 20261110 --bac reel --utilisateur-bac 64097
etape 2 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course" --a-blanc --graine 20261110 --bac factice
etape 3 "$PY" -I -B demonstrations/lire_boucle_reelle_v66.py "$S/course" "$S/lecture-course.json" --releve-sha256 "$(sha "$S/course")"
etape 4 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course-arret" --a-blanc --graine 20261110 --bac factice --scenario-proposeur refus:2
etape 5 "$PY" -I -B demonstrations/lire_boucle_reelle_v66.py "$S/course-arret" "$S/lecture-course-arret.json" --releve-sha256 "$(sha "$S/course-arret")"
etape 6 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course-part" --a-blanc --graine 20261110 --bac factice --cout-simule-usd 0.3 --plafond-kimi-usd 0.5 --plafond-argon-usd 7
etape 7 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course-bras" --a-blanc --graine 20261110 --bac factice --bras aleatoire
etape 8 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course-g3" --a-blanc --graine 20261110 --bac factice --generations 3
etape 9 "$PY" -I -B demonstrations/boucle_reelle_v66.py "$S/course-etage" --a-blanc --graine 20261110 --bac factice --scenario-experimentateur fabrique
etape 10 "$PY" -I -B demonstrations/lire_boucle_reelle_v66.py "$S/course-etage" "$S/lecture-course-etage.json" --releve-sha256 "$(sha "$S/course-etage")" --sans-oracle
etape 11 "$PY" -I -B demonstrations/lire_boucle_reelle_v66.py "$S/course" "$S/lecture-sans-empreinte.json"
etape 12 "$PY" -I -B demonstrations/preparer_boucle_reelle_v66.py "$S/blocs"
if [ -n "$REG" ]; then
  etape 13 "$PY" -I -B -c "import sys, datetime, json; sys.path.insert(0, '.'); from pole import registre_go_v66 as R
reg = R.lire_registre_go_v66(sys.argv[1]); print(json.dumps({'identifiants': len(reg), 'lignes_d_extension': sum(len(g['extensions']) for g in reg.values())}))
for gid in ('GO-2026-11-08-02', 'GO-2026-11-10-10'):
    g = R.verifier_go_v66(gid, sys.argv[1], 45, aujourd_hui=datetime.date(2026, 11, 10)); print(gid, g['plafond_lu_usd'], g['forme_du_plafond'], g['echeance'])
    for m in (40, 50):
        try: R.verifier_go_v66(gid, sys.argv[1], m, aujourd_hui=datetime.date(2026, 11, 10)); print('ACCEPTÉ', m)
        except R.GoRefuse as e: print('refus', m)" "$REG"
fi
if [ -n "$CONF" ]; then
  etape 14 "$PY" -I -B -c "import sys, os, importlib.util; sys.path.insert(0, '.')
s = importlib.util.spec_from_file_location('l', 'demonstrations/boucle_reelle_v66.py'); L = importlib.util.module_from_spec(s); s.loader.exec_module(L)
from pole import configuration_v56 as cfg
from pole.outils import sha256_fichier
c = os.path.join(sys.argv[1], 'configuration-boucle-reelle-v6.json'); conf = cfg.lire_configuration_v56(c)
sec, res = L.verifier_configuration_v66(conf, {'plafond_modeles_usd': 40.0, 'plafond_machine_usd': 5.0, 'plafond_kimi_usd': 33.0, 'plafond_argon_usd': 7.0}, sys.argv[1])
print('configuration v6 conforme', sha256_fichier(c)); print(sorted(os.path.relpath(x, sys.argv[1]) for f in ('kimi', 'argon') for x in res['fournisseurs'][f]['commande'] if x.endswith('.py')))" "$CONF"
fi
