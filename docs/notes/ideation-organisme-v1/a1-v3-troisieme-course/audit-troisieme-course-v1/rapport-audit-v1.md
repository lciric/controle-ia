# Rapport d'audit — A1-v3, troisième course (texte v4) — v1

Fille 9 (lignée Claude Opus 5.5), lectrice neuve (R13), le 5 novembre 2026 de 20:26 à 20:35 UTC (`date -u`). Verdict : `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md`.

## Démarche, dans l'ordre
1. Consigne vérifiée (`fb6078ff…`, compagnon OK). Texte v4 vérifié à `main` (`0b35494b…`, compagnon OK). Manifeste scellé vérifié (`fb9faf87…`, compagnon OK).
2. Deux branches de données récupérées par refspec explicite (`91845f04…`, `32adbce9…`). `git ls-tree -r --long` reformé en « blob  taille  chemin » est **identique à l'octet** aux deux blocs du manifeste scellé.
3. Arbre de travail à part en lecture seule, réduit par `sparse-checkout` au seul dossier de la course (24 fichiers, 5 Mo : consigne < 2 Go). Les 23 empreintes de la liste de l'hôte et les deux compagnons de la sortie sont égaux.
4. Code gelé : les 73 fichiers du bloc de la section 11 sont extraits des commits `9776ed0` et `291e9178` du dépôt public (`git fetch --filter=blob:none` par refspec explicite) ; les 73 empreintes sont égales, et égales à `manifeste.json` (`reglages.code_sha256`).
5. Lecture : `scripts/relire_lecture_v1.py` appelle `pole.attaque_goodhart_v3.lire` sur les suites, rejeux et audits de la trace, avec le plan et l'entropie du manifeste. Le résultat est **égal** à la lecture écrite par la course (`sorties/lecture-relue-v1.json`, `sorties/lecture-relue-resume-v1.json`). `scripts/tableau_v1.py` en extrait la table (`sorties/tableau-v1.txt`).
6. Audit de symétrie refait à la main, sans `lire_monde` (`scripts/audit_symetrie_v1.py` → `sorties/audit-symetrie-v1.json`) : promotions par case et par n, cohérence de la première promotion, seuil ln(1/α), échos recomptés depuis la réponse caviardée, chaîne du retour, absence de retour au témoin, consignes, invalides et motifs, hors classe, appels (statuts, codes, causes, modèles servis, attentes, coûts), rejeux (A2, A3). Aucun désaccord avec le code.
7. Dépense : `scripts/depense_v1.py` → `sorties/depense-v1.json`. Registre, relais et trace sont appariés appel par appel sur les coûts (multiensembles égaux) ; jetons ; durées.
8. Conformité : journal de l'hôte, amorce, `--verifier-seulement`, garde (continuité des 252 relevés), journal du relais, rapports de la fille 6, ordre v3, registres de `main`.

## Constats hors verdict
- **À corriger** : `registres/depenses.md` doit recevoir la dépense d'Argon (58,44887 USD, GO-2026-11-04-06) et le coût exact de la machine (facture Vast).
- Note : les 25 erreurs `BrokenPipe` du relais correspondent aux 25 relevés de la garde sans compte, pendant qu'un appel occupait le relais monofil ; aucun effet sur les appels.
- Note : les clés et jetons n'ont été ni lus ni cherchés. Le contrôle des secrets de l'hôte n'est pas vérifiable sans eux ; rotation à faire (R-1539, R-1540).

## Empreintes des pièces versées

| fichier | sha256 |
|---|---|
| `scripts/relire_lecture_v1.py` | `d5b8721c58323ebaa5437f0b227768d4f931585820b9d70b6d33c00a05cc903d` |
| `scripts/tableau_v1.py` | `4312802859da8769224946b91fef28d3435943be38648cee4d48101a30e16d40` |
| `scripts/audit_symetrie_v1.py` | `38bd88f3d1a199d23f75de8178e24c2b7325108fece0a01a28b25cdf6b674ccd` |
| `scripts/depense_v1.py` | `7a7d260c66362628da6cce228147247c8e5c0d9ee75a294608a8a8d60d70fa17` |
| `sorties/lecture-relue-v1.json` | `d961896c10ad4c88e65c7ba697a2b2534c616e429a092580533949e231ab1e46` |
| `sorties/lecture-relue-resume-v1.json` | `16c499b59ba2cdb1f90f9249d51662befaaa729da411a22f31962a9665e37775` |
| `sorties/tableau-v1.txt` | `14e125ad46b8204ba30aaefa7fd6f77d47f7de28b920a54619335c785b28889d` |
| `sorties/audit-symetrie-v1.json` | `bca4b5401d32c1028ec1859b4f21e6b5dd1bc66e93ad3dd71955c3c74b174edc` |
| `sorties/depense-v1.json` | `3e3262aa62408cb15285253086c05191207fa55028e0316459c230b4097caad0` |

Reproduire : `python -I scripts/relire_lecture_v1.py <racine orchestrator du commit 291e9178> <attaque-goodhart-v3.json> <manifeste.json> <sortie>`, puis `python -I scripts/tableau_v1.py <sortie>`. Ensuite `python3 -I scripts/audit_symetrie_v1.py <attaque-goodhart-v3.json>` et `python3 -I scripts/depense_v1.py <registre> <journal du relais> <attaque-goodhart-v3.json>`.
