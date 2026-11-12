# Essai local de l'amorce v6 — journal (0 USD, aucune clé, aucun appel à Vast), 2026-11-07T16:26:33Z

Script : `scripts/essai_amorce_t06_v6.sh`. Commit réel cloné : `20f576dbd8f61aa2ff553095aa01ee4f23a594fb`.

## Mode jouet, dépôt source réduit servi par un miroir nu (poussée initiale comprise)
```
ESSAI : 2026-11-07T16:26:56Z : mode jouet, commit 2c920286d8c32e236be6f8ae1f52448372513ef3, configuration docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v2.json, miroir /tmp/claude-0/essai-jouet-g/distant.git, branche essai/
AMORCE T06 v6 DEMARRAGE 1 : 2026-11-07T16:26:56Z, machine ?, commit 2c920286d8c32e236be6f8ae1f52448372513ef3
AMORCE 2026-11-07T16:27:21Z : CLONAGE mode=jouet secondes=25 octets_git=95507404 octets_arbre=306578562 debit_Mo_s=16.08 motifs=28
2026-11-07T16:27:22Z branche essai/t06-essai-local-v5-jouet-162656 poussée avant l'installation (droit d'écriture éprouvé)
AMORCE 2026-11-07T16:27:21Z : CLONAGE mode=jouet secondes=25 octets_git=95507404 octets_arbre=306578562 debit_Mo_s=16.08 motifs=28
présent  src
présent  tests
présent  scripts
présent  prereg
présent  donnees
présent  docs/notes
présent  registres/go.md
présent  docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v2.json
présent  docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v2.json.sha256
présent  pyproject.toml
présent  requirements-gpu.txt
absent   docs/sources/pdf (exclu)
absent   registres/passations (exclu)
absent   brouillons (exclu)
absent   livrables (exclu)
absent   gemini (exclu)
  essai/t06-essai-local-v5-jouet-162656
```

## Mode reel, dépôt source réduit servi par un miroir nu (poussée initiale comprise)
```
ESSAI : 2026-11-07T16:27:32Z : mode reel, commit de984944ac1ad5018f41a792e523b7e5f8e3bfb9, configuration docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v2.json, miroir /tmp/claude-0/essai-reel-g/distant.git, branche essai/t0
AMORCE T06 v6 DEMARRAGE 1 : 2026-11-07T16:27:32Z, machine ?, commit de984944ac1ad5018f41a792e523b7e5f8e3bfb9
AMORCE 2026-11-07T16:27:58Z : CLONAGE mode=reel secondes=26 octets_git=95528414 octets_arbre=306578562 debit_Mo_s=15.47 motifs=28
2026-11-07T16:27:59Z branche essai/t06-essai-local-v5-reel-162732 poussée avant l'installation (droit d'écriture éprouvé)
AMORCE 2026-11-07T16:27:58Z : CLONAGE mode=reel secondes=26 octets_git=95528414 octets_arbre=306578562 debit_Mo_s=15.47 motifs=28
présent  src
présent  tests
présent  scripts
présent  prereg
présent  donnees
présent  docs/notes
présent  registres/go.md
présent  docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v2.json
présent  docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v2.json.sha256
présent  pyproject.toml
présent  requirements-gpu.txt
absent   docs/sources/pdf (exclu)
absent   registres/passations (exclu)
absent   brouillons (exclu)
absent   livrables (exclu)
absent   gemini (exclu)
  essai/t06-essai-local-v5-reel-162732
```

## Mode reel, dépôt RÉEL (clone du commit poussé, arrêt à la ligne CLONAGE)
```
AMORCE 2026-11-07T16:27:58Z : CLONAGE mode=reel secondes=26 octets_git=95528414 octets_arbre=306578562 debit_Mo_s=15.47 motifs=28
## dossiers de premier niveau extraits (octets)
100156913	./docs
67946427	./diag
66314351	./donnees
61933111	./prereg
2489727	./runs
2212115	./registres
2085630	./tests
2026431	./src
847456	./scripts
558244	./traces
6286	./.claude
788	./requirements-gpu.txt
376	./requirements-cpu.txt
300	./pyproject.toml
237	./requirements-donnees.txt
170	./requirements-pilotage.txt
## chemins exigés présents / exclus absents
```

## Suite complète sur ce clone allégé (trois tranches, 3 005 essais)
```
948 passed in 1810.88s (0:30:10)
1062 passed in 1633.81s (0:27:13)
995 passed in 1154.94s (0:19:14)
```
