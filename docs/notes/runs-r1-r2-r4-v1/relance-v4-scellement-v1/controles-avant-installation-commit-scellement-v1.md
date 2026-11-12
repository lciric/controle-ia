# Contrôles d'avant l'installation de R1 v4, rejoués au commit de scellement (copie) — v1

Fait le 2026-11-04T08:21:40Z par conv-audit (fusionnée avec session-depot), sans réseau, sans poussée, sans dépense.

- Copie : arbre détaché de `prep/r1-relance-v4` au commit de scellement `937f13177892933955c9c34839b4b45a4db745df`, `git status --porcelain` vide.
- Bloc rejoué : `scripts/r1_v4_instance_v2.sh`, de `lire_unique() {` à la ligne « addendum lu » (64 lignes, sha256 `1953fb4a33755506a29cffec163e1af176b84f5eaf0cb9282db50c1ac652872b`), variables : `PREREG=prereg/R1-addendum-relance-v4.md`, `PREREG_ABSENT=0`, `TEMOIN_RUN=20261104-000000-essai` (fictif).
- Le clonage, la vérification de branche et la poussée initiale ne sont pas rejoués (réseau) : ils le seront sur l'instance.

## Session 1 (témoin) : code 0 (cas sain)
```
2026-11-04T08:21:29Z addendum lu : 381 tests attendus ; réparation prereg/R1-reparation-v4-config-v2.json ; rejeu prereg/R1-rejeu-config-v6.json ; table v4 à écrire (session 1 : aucune)
OK 0f10881b32fa…  prereg/R1-addendum-relance-v4.md
OK 4d0655d1bac5…  prereg/R1-reparation-v4-config-v2.json
OK a9ebc6b0cd6c…  prereg/R1-rejeu-config-v6.json
OK ead8a66851b2…  prereg/R1-table-tokenisation-v3.json
OK 80c85a0085f4…  prereg/R1-R2-rejeu-p3-v1.md
```

## Session 2 (réparation), sans témoin versé : code 2 (artefact attendu, arrêt avant l'installation)
```
2026-11-04T08:21:29Z résultat du témoin diag/20261104-000000-essai/resolution-graine-lot-v3-temoin.json (ou son sceau, ou son manifeste) absent au commit : arrêt avant l'installation
OK 0f10881b32fa…  prereg/R1-addendum-relance-v4.md
OK 4d0655d1bac5…  prereg/R1-reparation-v4-config-v2.json
OK a9ebc6b0cd6c…  prereg/R1-rejeu-config-v6.json
OK ead8a66851b2…  prereg/R1-table-tokenisation-v3.json
OK 80c85a0085f4…  prereg/R1-R2-rejeu-p3-v1.md
```
