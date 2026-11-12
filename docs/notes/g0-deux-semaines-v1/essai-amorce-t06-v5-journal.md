# Essai local de l'amorce v5 — journal (0 USD, aucune clé, aucun appel à Vast), 2026-11-07T13:59:20Z

Script : `scripts/essai_amorce_t06_v5.sh`. Commit réel cloné : `c356b836affe4a91f68fcfbaf3a9a0e239eaed2c`.

## Mode jouet, dépôt source réduit servi par un miroir nu (poussée initiale comprise)
```
ESSAI : 2026-11-07T13:59:27Z : mode jouet, commit 2a093ebe171882ee3b21ba9b20f33b9ffa7b8d1b, configuration docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v2.json, miroir /tmp/claude-0/essai-jouet-f/distant.git, branche essai/
AMORCE 2026-11-07T13:59:51Z : CLONAGE mode=jouet secondes=24 octets_git=95431833 octets_arbre=306317232 debit_Mo_s=16.74 motifs=27
2026-11-07T13:59:52Z branche essai/t06-essai-local-v5-jouet-135927 poussée avant l'installation (droit d'écriture éprouvé)
AMORCE 2026-11-07T13:59:51Z : CLONAGE mode=jouet secondes=24 octets_git=95431833 octets_arbre=306317232 debit_Mo_s=16.74 motifs=27
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
  essai/t06-essai-local-v5-jouet-135927
```

## Mode reel, dépôt source réduit servi par un miroir nu (poussée initiale comprise)
```
ESSAI : 2026-11-07T13:59:59Z : mode reel, commit 5865fc4ab463f552df8c00b17157b28238751b47, configuration docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v2.json, miroir /tmp/claude-0/essai-reel-f/distant.git, branche essai/t0
AMORCE 2026-11-07T14:00:24Z : CLONAGE mode=reel secondes=24 octets_git=95236028 octets_arbre=306317232 debit_Mo_s=16.73 motifs=27
2026-11-07T14:00:24Z branche essai/t06-essai-local-v5-reel-135959 poussée avant l'installation (droit d'écriture éprouvé)
AMORCE 2026-11-07T14:00:24Z : CLONAGE mode=reel secondes=24 octets_git=95236028 octets_arbre=306317232 debit_Mo_s=16.73 motifs=27
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
  essai/t06-essai-local-v5-reel-135959
```

## Mode reel, dépôt RÉEL (clone du commit poussé, arrêt à la ligne CLONAGE)
```
AMORCE 2026-11-07T13:28:43Z : CLONAGE mode=reel secondes=10 octets_git=100491991 octets_arbre=306470478 debit_Mo_s=40.70 motifs=27
## dossiers de premier niveau extraits (octets)
100111661	./docs
67946427	./diag
66313991	./donnees
61933111	./prereg
2489727	./runs
2212115	./registres
2016732	./src
1990283	./tests
736784	./scripts
558244	./traces
153246	./brouillons
6286	./.claude
788	./requirements-gpu.txt
376	./requirements-cpu.txt
300	./pyproject.toml
237	./requirements-donnees.txt
170	./requirements-pilotage.txt
## chemins exigés présents / exclus absents
```

## Suite complète sur ce clone allégé (trois tranches, 2 920 essais)
```
953 passed in 1783.38s (0:29:43)
1062 passed in 1606.84s (0:26:46)
905 passed in 943.40s (0:15:43)
```
