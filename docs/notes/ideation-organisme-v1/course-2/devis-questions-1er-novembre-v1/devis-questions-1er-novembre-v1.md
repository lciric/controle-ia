# Devis d'ensemble — questions du 1er novembre (tour 2 N12-N13 ; convergence v3, sélection génération à génération, bac à sable non circulaire × Argon seul, Kimi seul, collisionneur) — v1

session-depot (instance 3, seconde session), 1er novembre 2026, ≈ 10:55 UTC. Demandes de Lazar rapportées par conv-audit (n° 313 point 4 ;
n° 314 point 1 : règle nouvelle « toute question reformulée va aussi à Kimi seul, en plus d'Argon seul et du collisionneur »). Aucune
dépense avant un mot direct de Lazar dans cette session ; chaque ligne est engageable séparément (« go ligne N »). Chiffrage par la
commande `devis` du collisionneur v7 sur les fichiers réels et par la garde de pire cas du script « espèce seule » (R-959) ; attendu =
0,36 à 0,55 du pire cas (rapports observés sur cinq runs : 0,55, 0,58, 0,20, 0,37, 0,36) ; plafond ≥ 1,5 × attendu (R-924) et ≥ attendu
+ pire cas de la dernière cellule d'Opus (R-923).

| N | Objet | Faits (empreinte, mots) | Pire cas | Attendu | **Plafond** |
|---|---|---|---:|---:|---:|
| 1 | **Tour 2 N12-N13** (collisionneur, quatre espèces) : question `question-n12-n13-tour2-v1.md` (`0115fd8f…`, verdicts sur l'annexe `9dc13ece…`, résolution des neuf divergences, « qui lit ») | synthèse v2 `f0340581…`, 12 163 | 34,91 | 13 à 19 | **30** |
| 2 | **Convergence v3, collisionneur** (question `73900b1e…`) | `580444a6…`, 35 056 (brouillon 4, vérification, code, gel v4, calibrage en extrait ; pilote JSON et PDF de Bailey non servis) | 41,68 | 15 à 23 | **35** |
| 3 | Convergence v3, **Argon seul** (complément à la v2 déjà servie, GO-08) | idem | 2,48 | ≈ 1,9 | 3 (GO-08) |
| 4 | Convergence v3, **Kimi seul** | idem | 0,50 | ≈ 0,4 | 1 |
| 5 | **Sélection génération à génération v1, collisionneur** (question `c8992218…`) | `7c3404f4…`, 17 253 (11 pièces : dossier factuel, conception du pôle, programme v7, trois lectures de lancements, pont fiche → loi, programme § 5, N-013, N-035 ; 5 passages retirés par la règle 2) | 36,35 | 13 à 20 | **30** |
| 6 | Sélection, Argon seul | idem | 2,00 | ≈ 1,5 | 3 (GO-08) |
| 7 | Sélection, Kimi seul | idem | 0,40 | ≈ 0,3 | 1 |
| 8 | **Bac à sable non circulaire v1, collisionneur** (question `26f2db15…`) | `24064c98…`, 16 508 (LISEZMOI v48, devis machine jetable v3, relecture N12-N13, lecture d'Avalon ; synthèse N12-N13 non servie ; aucune technique d'évasion, trois mentions retirées) | 36,18 | 13 à 20 | **30** |
| 9 | Bac à sable, Argon seul | idem | 1,98 | ≈ 1,5 | 3 (GO-08) |
| 10 | Bac à sable, Kimi seul | idem | 0,40 | ≈ 0,3 | 1 |

**Total si tout est engagé** : plafonds 125 USD pour les quatre runs du collisionneur, 9 sur GO-08 (cumul 6,02 / 25 : 3 appels d'Argon
restent largement sous 25), 3 pour Kimi seul ; **attendu ≈ 60 à 85 USD**. Ordre proposé si séquencé : lignes 3, 4, 6, 7, 9, 10 d'abord
(≈ 6 USD, un avis par espèce) puis les collisionneurs ; chaque run suivi de critères de lecture scellés avant ouverture et d'un lecteur
neuf. Les « espèce seule » passent par `donnees/espece-seule-v1/lancer-espece-seule-v1.sh` (`4ba5fa13…`, relais Kimi local sous
`env -i`) ; les collisionneurs par le gabarit éprouvé (scripts neufs par run, clé Anthropic `RR_ANTHROPIC_API_KEY_LUC`).

**Réserves** : la convergence v3 est servie avec 35 000 mots de faits (le calibrage v4 en extrait) : le pire cas est le plus haut des
runs ; les pièces « gel et calibrage » n'étaient pas listées sous « pièces servies » par la v3 mais citées dans son constat, servies par
prudence. Pour la sélection, le programme de conception v7 n'a pas de compagnon `.sha256` sur la branche de conv-audit (signalé).
Option écartée : servir la synthèse N12-N13 au bac à sable (elle vit sous `donnees/` et son erratum n'est pas diffusable).
