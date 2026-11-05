#!/usr/bin/env bash
# Passages v12 : sorties en cours au bloc-notes, copiées dans le dépôt seulement une fois finies (ligne « code » écrite).
set -u
S=/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/sparks-v12
D=/home/user/controle-ia-travail/docs/notes/weight-space-programming-v1/essais-et-banc-sparks-v12
mkdir -p "$S"
V=/home/user/controle-ia-travail/.venv/bin/python
C=$(git -C /home/claude/wt/sparks-exp7-nul-v12 rev-parse HEAD); K=${C:0:8}
TF="tests/test_sparks_exp7_nul_v1.py tests/test_sparks_exp7_nul_v2.py tests/test_sparks_exp7_nul_v3.py tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v12.py"
verser() { mkdir -p "$D"; cp "$@" "$D/"; }
cd /home/claude/wt/sparks-exp7-nul-v12
if ! grep -q '^code ' $S/essais-tete-$K.txt 2>/dev/null; then
  PYTHONPATH=src timeout 3000 nice -n 10 $V -m pytest -q -p no:cacheprovider $TF -rs > $S/essais-tete-$K.txt 2>&1; echo "code $?" >> $S/essais-tete-$K.txt
fi
verser $S/essais-tete-$K.txt
E=/home/claude/wt/sparks-v12-enfant
if ! ls $S/essais-enfant-*.txt >/dev/null 2>&1 || ! grep -q '^code ' $S/essais-enfant-*.txt; then
  rm -f $S/essais-enfant-*.txt
  git -C /home/user/controle-ia-travail worktree remove --force $E 2>/dev/null; git -C /home/user/controle-ia-travail worktree prune
  timeout 300 git -C /home/user/controle-ia-travail worktree add -q --no-checkout --detach $E $C
  timeout 300 git -C $E sparse-checkout set --no-cone '/*' '!/*/' '/src/' '/tests/' '/scripts/' '/.claude/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md' '/docs/notes/sparks-exp7-nul-v1/'
  timeout 600 git -C $E checkout -q --detach $C
  (cd $E && $V -I -B src/controle_ia/sparks_exp7_nul_v8/addendum_factice.py prereg/SPARKS-EXP7-NUL-addendum-1.md $C > /dev/null)
  git -C $E add -A && git -C $E -c user.name=essai -c user.email=essai@invalid commit -qm "essai : commit enfant (addendum factice)"
  KE=$(git -C $E rev-parse HEAD | cut -c1-8)
  (cd $E && COMMIT_CODE=$C PYTHONPATH=src timeout 3000 nice -n 10 $V -m pytest -q -p no:cacheprovider $TF -rs > $S/essais-enfant-$KE.txt 2>&1; echo "code $?" >> $S/essais-enfant-$KE.txt)
fi
verser $S/essais-enfant-*.txt
if ! grep -q '^code ' $S/banc-$K.txt 2>/dev/null; then
  PYTHONPATH=src timeout 6600 nice -n 10 $V -I -B scripts/banc_mutations_sparks_exp7_nul_v12.py $S/banc-$K.json > $S/banc-$K.txt 2>&1; echo "code $?" >> $S/banc-$K.txt
fi
verser $S/banc-$K.txt $S/banc-$K.json
