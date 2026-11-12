# Total des dépenses de la phase 0 — v3

Somme des dépenses lues dans `registres/depenses.md` par un analyseur strict : une ligne du registre = au plus un montant en USD explicitement relevé. Les estimations (« ≈ », « ≤ », « au plus », « environ », « estimé », fourchettes) sont comptées à part, dans la colonne « estimé », jamais dans le total relevé. Les prix unitaires (par heure, par Go), cumuls, plafonds, devis, crédits, restes, montants d'autres projets ne sont jamais sommés. Une ligne à plusieurs montants (hors un montant unique en gras, convention du registre pour le total de la ligne), un relevé partiel (« premier relevé », « cumulés », « déjà imputé ») ou une fourchette vont au journal `journal-depenses-v3.txt`, jamais devinés ni sommés. Une ligne qui dit remplacer une estimation par un relevé compte une fois (l'estimation antérieure du même GO sort de la colonne « estimé »).

Jour du script (`date -u`) : 2026-11-10. Version : `registres-taif-v3`. Sources de chaque cellule : `sources-v3.json`.

## Global

| total | USD | lignes sommées | lignes non sommées (journal) |
|---|---|---|---|
| **relevé (phase 0)** | **667,36** | 138 | 190 |
| estimé (à part, jamais dans le relevé) | 134,54 | 52 | — |

Le total relevé est la valeur de la clé `total_depenses_phase0` de `sources-v3.json` (marqueur `<<TOTAL_DEPENSES_PHASE0>>` de la page pour le fonds).

## Par GO

| GO | périmètre (registre des GO) | plafond | relevé (USD) | lignes sommées | n° des lignes sommées | estimé (USD, à part) | lignes estimées | n° des lignes estimées | lignes non sommées (journal) | n° des lignes non sommées |
|---|---|---|---|---|---|---|---|---|---|---|
| (GO abrégé, non résolu : GO-04) |  |  | 0,31 | 1 | 301 |  | 0 |  | 0 |  |
| (GO abrégé, non résolu : GO-05) |  |  | 2,21 | 1 | 279 |  | 0 |  | 0 |  |
| (GO abrégé, non résolu : GO-05, GO-06) |  |  |  | 0 |  |  | 0 |  | 1 | 299 |
| (GO abrégé, non résolu : GO-05, GO-06, GO-07) |  |  | 0,00 | 1 | 275 |  | 0 |  | 1 | 273 |
| (GO abrégé, non résolu : GO-06) |  |  |  | 0 |  |  | 0 |  | 1 | 278 |
| (GO abrégé, non résolu : GO-06, GO-08) |  |  |  | 0 |  |  | 0 |  | 1 | 345 |
| (GO abrégé, non résolu : GO-06, GO-09) |  |  |  | 0 |  |  | 0 |  | 1 | 284 |
| (GO abrégé, non résolu : GO-10) |  |  | 0,76 | 2 | 305, 307 |  | 0 |  | 0 |  |
| (GO abrégé, non résolu : GO-17) |  |  | 0,39 | 1 | 265 |  | 0 |  | 0 |  |
| (plusieurs GO cités : GO-2026-10-04-08, GO-2026-10-06-01) |  |  |  | 0 |  |  | 0 |  | 3 | 39, 40, 41 |
| (plusieurs GO cités : GO-2026-10-04-08, GO-2026-10-11-01) |  |  |  | 0 |  |  | 0 |  | 3 | 49, 50, 51 |
| (plusieurs GO cités : GO-2026-10-04-08, GO-2026-10-12-01) |  |  |  | 0 |  |  | 0 |  | 6 | 53, 54, 55, 57, 58, 59 |
| (plusieurs GO cités : GO-2026-10-04-08, GO-2026-10-12-02) |  |  |  | 0 |  | 4,90 | 1 | 67 | 9 | 66, 68, 71, 74, 76, 78, 80, 82, 84 |
| (plusieurs GO cités : GO-2026-10-24-04, GO-2026-10-24-06) |  |  |  | 0 |  |  | 0 |  | 1 | 95 |
| (plusieurs GO cités : GO-2026-10-24-04, GO-2026-10-24-07) |  |  | 0,00 | 1 | 170 |  | 0 |  | 3 | 100, 102, 103 |
| (plusieurs GO cités : GO-2026-10-24-04, GO-2026-10-24-07, GO-2026-10-26-01) |  |  |  | 0 |  |  | 0 |  | 1 | 169 |
| (plusieurs GO cités : GO-2026-10-26-01, GO-2026-10-26-02) |  |  |  | 0 |  |  | 0 |  | 1 | 171 |
| (plusieurs GO cités : GO-2026-10-27-01, GO-2026-10-27-02) |  |  | 0,00 | 2 | 196, 197 |  | 0 |  | 0 |  |
| (plusieurs GO cités : GO-2026-10-29-01, GO-2026-10-29-02) |  |  | 0,00 | 1 | 223 |  | 0 |  | 2 | 224, 225 |
| (plusieurs GO cités : GO-2026-10-29-19, GO-2026-10-29-20) |  |  |  | 0 |  |  | 0 |  | 2 | 247, 248 |
| (plusieurs GO cités : GO-2026-10-30-02, GO-2026-10-30-03) |  |  |  | 0 |  |  | 0 |  | 1 | 249 |
| (plusieurs GO cités : GO-2026-10-30-17, GO-2026-10-31-01) |  |  | 9,19 | 1 | 266 |  | 0 |  | 0 |  |
| (plusieurs GO cités : GO-2026-11-02-02, GO-2026-11-02-14) |  |  |  | 0 |  | 1,79 | 1 | 322 | 1 | 321 |
| (plusieurs GO cités : GO-2026-11-04-06, GO-2026-11-05-03) |  |  | 0,28 | 1 | 375 |  | 0 |  | 1 | 374 |
| (plusieurs GO cités : GO-2026-11-04-06, GO-2026-11-05-03, GO-2026-11-05-06) |  |  |  | 0 |  |  | 0 |  | 1 | 371 |
| (plusieurs GO cités : GO-2026-11-05-02, GO-2026-11-05-05) |  |  | 1,00 | 1 | 377 |  | 0 |  | 1 | 365 |
| (plusieurs GO cités : GO-2026-11-06-01, GO-2026-11-07-08) |  |  | 3,65 | 1 | 390 |  | 0 |  | 0 |  |
| (sans GO cité) |  |  | 54,08 | 12 | 90, 152, 157, 158, 159, 162, 163, 164, 166, 167, 168, 267 | 18,38 | 7 | 34, 42, 48, 52, 65, 86, 88 | 24 | 38, 43, 56, 60, 61, 62, 63, 64, 69, 70, 72, 73, 75, 77, 79, 81, 83, 89, 92, 113, 145, 264, 310, 314 |
| GO-2026-10-04-08 | devis de calcul de la phase 0 (`livrables/premier-rendu-v1/devis-v1.md`, sha256 16d71feb…) : instances de calcul de T0.… | 150 USD (alerte à 120 USD) |  | 0 |  | 2,96 | 6 | 7, 8, 9, 19, 26, 35 | 14 | 20, 21, 22, 27, 28, 29, 31, 33, 36, 37, 45, 46, 47, 87 |
| GO-2026-10-06-02 | N-012, option (a) de `docs/decisions/proposition-N-012-v1.md` (sha256 bbd4ccd6…) : rapatrier dans le dépôt les fichiers… | dans le plafond de GO-2026-10-04-08 (150 USD) |  | 0 |  |  | 0 |  | 1 | 44 |
| GO-2026-10-12-02 | N-021, option (a) de `docs/decisions/proposition-N-021-notations-seules-v1.md` (082e9318…) : notations décisives des ju… | ≈ 10,5 USD (dans GO-2026-10-04-08) |  | 0 |  |  | 0 |  | 1 | 85 |
| GO-2026-10-24-05 | étape 1 du programme « gradient conçu par l'essaim » (sondes ; N-042, R-344) : extraction des traits (activations de Ll… | dans la ligne de R-355 (sans plafond fixé par Lazar) ; moin… |  | 0 |  | 18,59 | 4 | 93, 94, 96, 134 | 2 | 132, 133 |
| GO-2026-10-24-06 | brainstorm du lot 3 « signalement omis » (sabotage diffus d'une délégation ; métriques pour départager des essaims) par… | 25 USD (`--plafond-usd 25`, tenu par le script avant chaque… | 1,01 | 1 | 97 |  | 0 |  | 0 |  |
| GO-2026-10-24-07 | « préparatifs » (décision (a) de Lazar de 22:48, heure de Paris, reçue par « conv-audit », n° 21 ; confirmée par Lazar… | 40 USD imputés à cette ligne | 49,72 | 23 | 101, 104, 105, 106, 108, 109, 111, 114, 115, 117, 119, 120, 122, 127, 128, 146, 151, 160, 174, 177, 178, 183, 184 | 0,10 | 2 | 98, 99 | 21 | 107, 110, 112, 116, 118, 121, 125, 126, 139, 140, 143, 149, 150, 153, 154, 155, 156, 161, 165, 173, 175 |
| GO-2026-10-25-01 | second pilote de l'organisme écrit par Gemini, v5.1 (`outils/gemini-organisme-v5-1`, `7f9cd2e`, arbre `50ffcd7d…`), deu… | 120 USD au plus pour les deux courses | 30,22 | 3 | 124, 129, 131 |  | 0 |  | 2 | 123, 130 |
| GO-2026-10-25-02 | deux courses réelles descriptives de plus, v5.3 puis v6 de Gemini (lignées « assistées »), sous le noyau du pilote (`b1… | 185 USD au plus pour l'ensemble du GO, inchangé (pilote 3 :… | 92,43 | 7 | 136, 138, 180, 181, 182, 186, 187 |  | 0 |  | 4 | 135, 137, 179, 185 |
| GO-2026-10-25-03 | test H-M1 « gabarit contre style » (R-447, R-450) : une instance louée sur Vast.ai (A100 ou H100 80 Go, une carte), mes… | 10 USD au plus (fixé par « session-depot », aucun montant d… |  | 0 |  | 0,23 | 2 | 142, 148 | 2 | 141, 144 |
| GO-2026-10-26-02 | tour du collisionneur v2.6 (`collisionneur_v2.py`, sha256 `0e63febd496368f1…`) sur la question « programme TAIF » de P-… | 10 USD | 4,37 | 1 | 176 |  | 0 |  | 1 | 172 |
| GO-2026-10-26-04 | audit défensif du programme, partie à plusieurs modèles (R-504, R-508, R-509) : (1) tour du collisionneur v2.6 (`0e63fe… | sans plafond (mot de Lazar, R-512) | 9,32 | 3 | 188, 189, 191 |  | 0 |  | 1 | 190 |
| GO-2026-10-26-06 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, ref… | 25 USD | 0,00 | 1 | 192 |  | 0 |  | 0 |  |
| GO-2026-10-26-07 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, ref… | 23 USD | 0,00 | 1 | 193 |  | 0 |  | 0 |  |
| GO-2026-10-27-01 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, ref… | 35 USD | 0,00 | 2 | 194, 195 |  | 0 |  | 0 |  |
| GO-2026-10-27-04 | comparaison d'échelle, `prereg/test-echelle-conscience-eval-v10.md` (`2af6516dce9326d5…`) | 24 USD |  | 0 |  |  | 0 |  | 1 | 198 |
| GO-2026-10-27-05 | premier lancement réel du pôle « scientifique automatique », option (a) : orchestrateur v6 de conv-audit (`canal/conv-a… | 30 USD | 6,24 | 1 | 199 |  | 0 |  | 0 |  |
| GO-2026-10-27-06 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, ref… | 22 USD | 4,05 | 1 | 200 |  | 0 |  | 1 | 205 |
| GO-2026-10-27-07 | « couche 1 bis » : banque T0.5 complète par la chaîne de T0.5 de session-depot — (a) notation par les deux juges des 60… | 25 USD |  | 0 |  | 0,15 | 1 | 203 | 5 | 202, 204, 208, 209, 211 |
| GO-2026-10-27-09 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, ref… | 22 USD | 2,84 | 1 | 201 |  | 0 |  | 0 |  |
| GO-2026-10-27-10 | course de contrôle « (a) bis » du pôle, sous la **délégation GO-2026-10-27-08** : proposée par conv-audit (n° 111, poin… | 15 USD | 5,89 | 1 | 206 |  | 0 |  | 0 |  |
| GO-2026-10-27-11 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, un… | 15 USD |  | 0 |  |  | 0 |  | 1 | 207 |
| GO-2026-10-27-12 | tour du collisionneur v2.6 (`0e63febd…`, étage III standard, trois tours, trois modèles, une tentative par cellule, un… | 30 USD | 5,74 | 1 | 210 |  | 0 |  | 0 |  |
| GO-2026-10-28-03 | collisionneur « évasion et moniteurs » (collisionneur_v2.6, étage III seul ; conception = moniteurs, équipe rouge E3-T2… | 28/22/33 USD par tour (garde 83 USD ; pire cas devis 62,29… | 20,31 | 1 | 230 |  | 0 |  | 0 |  |
| GO-2026-10-28-08 | tour du collisionneur v2.6 (`0e63febd…`, étage III seul : conception, équipe rouge croisée, riposte ; trois modèles Fab… | 30 USD | 3,19 | 2 | 212, 213 |  | 0 |  | 0 |  |
| GO-2026-10-28-09 | **contre-lecture par Gemini Argon** (`gemini-4-argon`, clé `GEMINI_API_KEY_2`, un appel, au plus une relance sur sortie… | 5 USD | 1,29 | 1 | 214 |  | 0 |  | 0 |  |
| GO-2026-10-28-11 | **régénération du fichier complet des sondes figées de P3** (Mahalanobis comprises), devis `docs/notes/regeneration-son… | 6 USD |  | 0 |  | 1,22 | 1 | 221 | 1 | 218 |
| GO-2026-10-28-12 | **contre-lecture par Gemini Argon de la version 2** de la conception de l'affinage (`conception-affinage-equipe-rouge-v… | 5 USD | 1,83 | 1 | 215 |  | 0 |  | 0 |  |
| GO-2026-10-28-14 | **course d'idéation de l'organisme** (orchestrateur du pôle, prise « idéation », version courante de conv-audit au lanc… | 60 USD | 0,00 | 1 | 236 |  | 0 |  | 1 | 238 |
| GO-2026-10-28-15 | tour du collisionneur v2.6 (`0e63febd…`, étage III seul : conception, équipe rouge croisée, riposte ; trois modèles Fab… | 30 USD | 12,59 | 2 | 216, 217 |  | 0 |  | 0 |  |
| GO-2026-10-28-16 | **rejeu du juge sur les 180 textes du pilote de T0.5** (étape (0) du format décision de conv-audit sur la couche 2, `85… | 4 USD |  | 0 |  |  | 0 |  | 2 | 226, 227 |
| GO-2026-10-28-17 | tour du collisionneur v2.6 (`0e63febd…`, étage III seul : conception, équipe rouge croisée, riposte ; trois modèles Fab… | 30 USD | 11,06 | 2 | 219, 220 |  | 0 |  | 0 |  |
| GO-2026-10-29-01 | **tour complémentaire du collisionneur sur le pilote de la couche 2** (v2.6 `0e63febd…`, étage III, trois modèles, une… | 30 USD | 0,00 | 1 | 222 |  | 0 |  | 0 |  |
| GO-2026-10-29-06 | **tour du collisionneur sur la garde appariée δ (P-26)** : question scellée de conv-audit `question-collisionneur-garde… | 25 USD | 14,30 | 1 | 229 |  | 0 |  | 1 | 228 |
| GO-2026-10-29-07 | **tour du collisionneur sur la règle de repli de la porte G0** (si G0 n'est pas franchie fin novembre ; critères inchan… | 15 USD | 3,19 | 1 | 231 |  | 0 |  | 0 |  |
| GO-2026-10-29-10 | **tour neuf du collisionneur sur la règle de repli de G0** après le refus du run v1 (R-748) : question v2 plus techniqu… | 11,8 USD (le total des deux runs reste ≤ 15 USD : 3,19 + 11… | 6,83 | 1 | 235 |  | 0 |  | 1 | 232 |
| GO-2026-10-29-12 | **rejeu des juges v2, plafond relevé de 4 à 5 USD** sous le GO anticipé GO-2026-10-29-11 : lanceur `docs/procedures/rej… | 5 USD |  | 0 |  | 2,79 | 1 | 234 | 1 | 233 |
| GO-2026-10-29-14 | **question « ripostes et classes d'écart » posée à Argon seul** (gemini-4-argon, par le relais Gemini local et la comma… | 6 USD | 0,82 | 1 | 243 |  | 0 |  | 1 | 240 |
| GO-2026-10-29-15 | **tour du collisionneur sur la question-mère v3 de la course 2** (conv-audit n° 201, 205, 206 ; `question-mere-course-i… | 30 USD | 16,28 | 2 | 244, 245 |  | 0 |  | 1 | 241 |
| GO-2026-10-29-16 | **question-mère v3 posée à Argon à part** (gemini-4-argon par le relais Gemini local et la commande v2, consigne seule) | 2 USD | 1,15 | 1 | 242 |  | 0 |  | 1 | 239 |
| GO-2026-10-29-17 | **tour « paramètres de famille de déplacements » posé à Argon seul** (gemini-4-argon, relais Gemini local, commande v2)… | 6 USD | 0,81 | 1 | 246 |  | 0 |  | 0 |  |
| GO-2026-10-30-03 | **course 1, tentative 2, sur l'orchestrateur v50, sans Opus proposeur** (décision de Lazar ≈ 07:20 UTC) : proposeurs Fa… | 52,8 USD |  | 0 |  |  | 0 |  | 1 | 250 |
| GO-2026-10-30-05 | **jugement des 29 fiches validées de la course 1, tentative 2, en mode « juges seulement »** (orchestrateur v52, R-805)… | 20 USD (Claude) + 4 USD (Argon) |  | 0 |  |  | 0 |  | 2 | 251, 252 |
| GO-2026-10-30-06 | **essai Kimi d'un seul appel** (`essai_kimi_v1.sh`, relais Kimi v2) : liste des modèles (`GET /v1/models`, gratuite), p… | 0,5 USD | 0,00 | 1 | 253 |  | 0 |  | 0 |  |
| GO-2026-10-30-09 | **rejugement de la course 1, tentative 2, avec témoins v2 de longueur comparable** (R-820 point 3) : 29 fiches validées… | 11 USD (Opus et Argon 8 ; Kimi 3) | 0,76 | 1 | 255 | 2,03 | 1 | 254 | 0 |  |
| GO-2026-10-30-11 | **brainstorm de la question du texte III de la course 2** (R-824) : un tour d'étage III du collisionneur v3 (Opus 5.5,… | 28 USD | 18,92 | 4 | 256, 257, 258, 259 |  | 0 |  | 0 |  |
| GO-2026-10-30-12 | **tour du collisionneur v6 (quatre espèces) sur le tableau partagé de la course 2** : un tableau complet en lecture et… | 12 USD | 8,01 | 1 | 260 |  | 0 |  | 0 |  |
| GO-2026-10-30-14 | **Argon avec recherche sur le Web** (question fusionnée de conv-audit, n° 259 ; fertilité des croisements, bisociation)… | 3 USD | 0,61 | 1 | 261 |  | 0 |  | 0 |  |
| GO-2026-10-30-15 | **tour du collisionneur v6 (quatre espèces) sur la question « l'idée P-041 est-elle bonne ? »** : le prompt reformulé p… | 12 USD | 8,16 | 1 | 262 |  | 0 |  | 0 |  |
| GO-2026-10-30-16 | **tour du collisionneur v6 (quatre espèces, forme « arbitre ») sur la bisociation** (lot complet de conv-audit, n° 262… | 12 USD | 20,30 | 1 | 263 |  | 0 |  | 0 |  |
| GO-2026-10-31-02 | **tour 1 de l'arène coévolutive (P-041) sur la question v5** (faits 19 à 30 : Bailey et collègues et les occupants ; co… | 25 USD (≈ 12 par tour) | 8,22 | 1 | 268 |  | 0 |  | 1 | 269 |
| GO-2026-10-31-05 | **devis v1 de P-041 et du collisionneur protocelles** (`docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneu… | 210 USD | 18,52 | 1 | 270 |  | 0 |  | 2 | 285, 286 |
| GO-2026-10-31-06 | **collisionneur des nœuds (question v9 de conv-audit : N1, N3 D-j, N4, N5, N6, N9 D-GK-1, N10)**, devis R-900 (`docs/no… | 45 USD | 0,00 | 1 | 282 |  | 0 |  | 1 | 283 |
| GO-2026-10-31-07 | **tour du collisionneur v7 (quatre espèces) sur D-ML-1** (taille du jeu bénin de l'estimation de la malléabilité, `prer… | 12 USD (tour comparable à faits courts : 8,2 à 8,4 USD) |  | 0 |  |  | 0 |  | 1 | 281 |
| GO-2026-10-31-08 | **Argon seul (gemini-4-argon, chaîne relais Gemini v1 → appel-argon-v3 → commande_argon_v2, garde de pire cas avant env… | 25 USD | 4,16 | 4 | 271, 272, 274, 277 |  | 0 |  | 3 | 276, 294, 295 |
| GO-2026-11-01-01 | **collisionneur séparé N12-N13 (couches 3 et 4 de l'organisme ; récompense collective)**, devis v2 (`docs/notes/ideatio… | 30 USD |  | 0 |  |  | 0 |  | 2 | 287, 289 |
| GO-2026-11-01-02 | **avenant à GO-2026-10-31-06 (collisionneur des nœuds) : complément du tour 2**, devis de complément v2 (`docs/notes/id… | 61 USD (GO-06 porté de 45 à 61 ; cumul avant tour 2 : 30,23) | 3,83 | 1 | 290 |  | 0 |  | 2 | 288, 292 |
| GO-2026-11-01-03 | **collisionneur sur la boucle itérative moisson ↔ fiches ↔ bisociateur (question v1 de conv-audit, `72b4f149…`), tour 1… | 30 USD |  | 0 |  |  | 0 |  | 1 | 296 |
| GO-2026-11-01-05 | **collisionneur v8 à cinq espèces (A Fable, B Opus, C Argon, D Kimi, E GPT-6 Astra `gpt-6-astra`, identifiant vérifié s… | 40 USD |  | 0 |  |  | 0 |  | 2 | 317, 319 |
| GO-2026-11-01-09 | **« épreuve fraîche » du pont fiche → loi v1 de conv-audit** (R-1044 de sa branche ; n° 314 point 2 : premier essai sur… | 5 USD |  | 0 |  |  | 0 |  | 2 | 302, 303 |
| GO-2026-11-01-10 | **relecture de la candidature de Lazar au Pivotal Research Fellowship par Argon seul et Kimi seul** (n° 322 de conv-aud… | 5 USD | 0,35 | 1 | 304 |  | 0 |  | 0 |  |
| GO-2026-11-01-11 | **épisodes réels T0.5 « graines neuves » cette nuit** (demande de Lazar relayée par conv-audit, n° 323, point 1 ; devis… | 45 USD |  | 0 |  |  | 0 |  | 3 | 308, 309, 315 |
| GO-2026-11-01-12 | **mini-course d'idéation réelle avec Kimi et Argon seuls** (demande de Lazar relayée par conv-audit, n° 323, point 2 ;… | 10 USD |  | 0 |  | 1,80 | 1 | 312 | 1 | 311 |
| GO-2026-11-01-13 | **runs R1, R2 et R4 proposés par conv-audit (n° 326) pour les mentors du contrôle** : R1 rejeu des 2 400 actions de P3… | 25 USD |  | 0 |  | 3,60 | 1 | 316 | 1 | 313 |
| GO-2026-11-02-07 | **A1 — attaque de Goodhart, deux mondes et grille G1, remplace GO-2026-11-02-03 et GO-2026-11-02-04 (non consommés, auc… | 80 USD | 39,45 | 1 | 320 |  | 0 |  | 1 | 318 |
| GO-2026-11-02-21 | **Attaque de Goodhart contre le juge statistique, reprise propre (« A1-v3 »), plafond relevé** : Argon seul (`gemini-4-… | 400 USD | 4,25 | 1 | 328 |  | 0 |  | 1 | 326 |
| GO-2026-11-02-27 | **Contrôle, relance de R1 sur la table de tokenisation v3** (`ead8a668…`) : addendum v3 scellé chez session-depot, conc… | 60 USD |  | 0 |  | 0,54 | 1 | 327 | 1 | 325 |
| GO-2026-11-02-31 | **Collisionneur, un tour sur le prompt de brainstorm de Lazar** (`brouillons/canal-reprise-releve-v1/envois/conv-audit/… | 40 USD | 23,85 | 3 | 323, 324, 329 |  | 0 |  | 2 | 330, 331 |
| GO-2026-11-03-01 | **Attaque de Goodhart contre le juge statistique, seconde course d'A1-v3** (texte scellé d'A1-v3 `898d5be4…`, section 8… | 400 USD | 48,50 | 1 | 353 |  | 0 |  | 0 |  |
| GO-2026-11-03-02 | **Course d'idéation de l'organisme sur la question 1 du mentor Heimersheim** (pilotage des activations contre la consci… | 244 USD | 10,03 | 1 | 334 |  | 0 |  | 2 | 332, 333 |
| GO-2026-11-03-03 | **R1 rendu lisible (table v4)** : option (a) de conv-audit (n° 404, `4a525a52…`), d'après le rapport `brouillons/preuve… | 60 USD |  | 0 |  | 10,38 | 4 | 355, 356, 357, 360 | 0 |  |
| GO-2026-11-03-04 | **Collisionneur v9, un tour sur la question 2 du mentor Kirchner** (spécification de conv-audit `934f5dcb…`, § 2 ; ques… | 35 USD | 10,35 | 3 | 335, 336, 338 |  | 0 |  | 0 |  |
| GO-2026-11-03-05 | **Course d'idéation de l'organisme sur la question 2 du mentor Kirchner** (spécification de conv-audit `934f5dcb…`, § 2… | 245 USD | 24,07 | 2 | 342, 346 |  | 0 |  | 1 | 343 |
| GO-2026-11-03-06 | **Collisionneur v9, un tour sur la question 1 de la mentore Ibrahim** (conv-audit n° 416 et 417 ; question `5e905798…`… | 35 USD |  | 0 |  | 0,01 | 1 | 339 | 1 | 344 |
| GO-2026-11-03-07 | **Collisionneur v9, un tour sur la question du mentor Scheurer** (conv-audit n° 416 et 417 ; question `edb1d5f1…` ; fai… | 35 USD | 1,00 | 1 | 341 |  | 0 |  | 1 | 349 |
| GO-2026-11-03-08 | **Collisionneur v9, un tour sur la question 2 des mentors Colognese et Ward** (conv-audit n° 416 et 417 ; question `06d… | 35 USD | 2,81 | 1 | 340 |  | 0 |  | 0 |  |
| GO-2026-11-03-09 | **Course d'idéation de l'organisme sur la question 1 de la mentore Ibrahim** (spécification de conv-audit `0874d561…` ;… | 198 USD | 7,98 | 1 | 350 |  | 0 |  | 0 |  |
| GO-2026-11-04-01 | **Appel unique à Astra (`gpt-6-astra`) : intégrer le billet « Sparks of Weight-Space Programming » dans nos deux progra… | 3 USD | 0,26 | 1 | 352 |  | 0 |  | 0 |  |
| GO-2026-11-04-02 | **Collisionneur v9, un tour sur l'intégration du billet « Sparks of Weight-Space Programming » dans nos programmes** :… | 35 USD |  | 0 |  | 8,40 | 1 | 354 | 0 |  |
| GO-2026-11-04-04 | **SPARKS-EXP7-NUL : l'expérience 7 du billet « Sparks » sous paires nulles et aveuglement**, variante carte graphique l… | 40 USD |  | 0 |  | 0,09 | 1 | 373 | 2 | 372, 391 |
| GO-2026-11-04-06 | **Attaque de Goodhart contre le juge statistique, troisième course d'A1-v3, sur hôte durable** (option (a) de R-1463) :… | 400 USD | 0,61 | 1 | 376 |  | 0 |  | 0 |  |
| GO-2026-11-05-01 | **Sonde de l'hôte durable d'A1-v3 sur une machine à une carte bon marché** (constat de R-1510 et de la recherche de 00:… | 1 USD |  | 0 |  | 0,17 | 4 | 358, 359, 361, 362 | 0 |  |
| GO-2026-11-05-02 | **SPARKS-EXP7-NUL tir réel** : une instance Vast à une carte, commit de tir enfant de `prep/sparks-exp7-nul-v9` `4d07d2… | 5 USD |  | 0 |  | 0,01 | 1 | 364 | 1 | 363 |
| GO-2026-11-05-05 | **SPARKS-EXP7-NUL tir réel, codes v10 et suivants** (mêmes conditions que GO-2026-11-05-02 : une instance Vast à une ca… | 5 USD |  | 0 |  | 0,15 | 4 | 366, 368, 370, 378 | 2 | 367, 369 |
| GO-2026-11-06-01 | **T0.6, épreuves à blanc E2 et E3 du lanceur (v4 après la correction C-V4-1)** : E2 sur une machine Vast à une carte mo… | 5 USD (E2 et E3 cumulés) | 2,87 | 6 | 379, 381, 382, 383, 386, 387 |  | 0 |  | 3 | 380, 384, 385 |
| GO-2026-11-07-07 | **Épreuve de l'étiqueteur, phase 1** (appels des lecteurs `gemini-4-argon` et `kimi-k3.1-pro` sur les items plantés), a… | 300 USD |  | 0 |  | 33,56 | 3 | 394, 397, 398 | 4 | 389, 392, 401, 403 |
| GO-2026-11-07-08 | **E3 bis de T0.6** (option (b) de R-1728) : **3 USD de plus sur le GO-2026-11-06-01** (5 → 8 USD pour les épreuves E2,… | 3 USD | 0,16 | 1 | 388 |  | 0 |  | 0 |  |
| GO-2026-11-08-06 | **Collisionneur v2.6, remue-méninges du pilier attaque** sur la question scellée (`29870ac9a8091c165375c51f4b74d6e0f38a… | 25 USD |  | 0 |  |  | 0 |  | 3 | 393, 395, 396 |
| GO-2026-11-08-07 | **Question v2 du pilier attaque (trace interne du sabotage, défense randomisée ou perfectionnée, pince ; scellée `2dbad… | 15 USD |  | 0 |  |  | 0 |  | 2 | 399, 400 |
| GO-2026-11-08-08 | **Organisme d'idéation : course sur la question scellée v1 du pilier attaque** (`29870ac9a8091c165375c51f4b74d6e0f38ae6… | 20 USD | 0,03 | 1 | 402 |  | 0 |  | 2 | 405, 406 |
| GO-2026-11-08-10 | **Collisionneur v9 à cinq espèces (A Fable 5.1, B Opus 5.5, C Argon `gemini-4-argon`, D Kimi `kimi-k3.1-pro`, E Astra `… | 30 USD | 11,05 | 1 | 407 | 0,02 | 1 | 404 | 0 |  |
| GO-2026-11-08-11 | **Course de dose-réponse des organismes (T0.6), MODE EXPLORATOIRE, NON OPPOSABLE** (mots de Lazar : « lance la now » ;… | 100 USD |  | 0 |  | 17,60 | 1 | 413 | 1 | 408 |
| GO-2026-11-09-02 | **Sonde de refus des deux lecteurs candidats Claude de l'étiqueteur v2** (ordre scellé `docs/procedures/ordre-sonde-ref… | 15 USD |  | 0 |  | 5,07 | 1 | 409 | 0 |  |
| GO-2026-11-09-03 | **Étiqueteur du sabotage flou, lecture exploratoire v2, plan complet** (`docs/procedures/ordre-exploratoire-etiqueteur-… | 100 USD hors crédits (+ ≤ 50 sur crédits Claude) |  | 0 |  |  | 0 |  | 1 | 410 |
| GO-2026-11-09-04 | **Dépenses par anticipation pendant l'autonomie de 8 h ouverte le 9 novembre vers 12:57 UTC (fin ≈ 20:57 UTC)**, sur le… | 150 USD (+ 100 sur crédits Claude) | 10,89 | 1 | 412 |  | 0 |  | 0 |  |

## Par tâche de la phase 0 nommée sur la ligne ou dans le périmètre du GO

| tâche(s) nommée(s) | relevé (USD) | lignes sommées | n° des lignes sommées | estimé (USD, à part) | lignes estimées | n° des lignes estimées | lignes non sommées (journal) | n° des lignes non sommées |
|---|---|---|---|---|---|---|---|---|
| (aucune tâche de la phase 0 nommée) | 646,03 | 127 | 97, 101, 104, 105, 106, 108, 109, 111, 114, 115, 117, 119, 120, 122, 124, 127, 128, 129, 131, 136, 138, 146, 151, 152, 157, 158, 159, 160, 162, 163, 164, 166, 167, 168, 170, 174, 176, 177, 178, 180, 181, 182, 183, 184, 186, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 199, 201, 210, 212, 213, 214, 215, 216, 217, 219, 220, 222, 223, 229, 230, 231, 235, 236, 242, 243, 244, 245, 246, 253, 255, 256, 257, 258, 259, 260, 261, 262, 263, 265, 266, 267, 268, 270, 271, 272, 274, 275, 277, 279, 282, 290, 301, 304, 305, 307, 320, 323, 324, 328, 329, 334, 335, 336, 338, 340, 341, 342, 346, 350, 352, 353, 375, 376, 377, 402, 407, 412 | 73,16 | 30 | 48, 52, 93, 94, 96, 98, 99, 134, 142, 148, 234, 254, 327, 339, 354, 358, 359, 361, 362, 364, 366, 368, 370, 373, 378, 394, 397, 398, 404, 409 | 130 | 43, 44, 56, 60, 61, 62, 63, 64, 69, 70, 72, 73, 75, 77, 79, 81, 83, 95, 100, 102, 103, 107, 110, 112, 113, 116, 118, 121, 123, 125, 126, 130, 132, 133, 135, 13… |
| P1 + T0.6 |  | 0 |  |  | 0 |  | 1 | 408 |
| P2 | 4,05 | 1 | 200 | 5,30 | 1 | 86 | 0 |  |
| P2 + T0.4 |  | 0 |  | 0,24 | 1 | 9 | 0 |  |
| P3 | 10,60 | 2 | 90, 206 | 20,95 | 8 | 88, 221, 316, 322, 355, 356, 357, 360 | 6 | 87, 89, 92, 218, 313, 321 |
| T0.4 |  | 0 |  | 3,95 | 5 | 7, 8, 34, 35, 42 | 7 | 27, 31, 33, 36, 38, 39, 40 |
| T0.4 + T0.5 + T0.8 |  | 0 |  | 4,90 | 1 | 67 | 14 | 50, 51, 54, 55, 58, 59, 68, 71, 74, 76, 78, 80, 82, 84 |
| T0.4 + T0.8 |  | 0 |  | 1,60 | 2 | 19, 26 | 9 | 20, 21, 22, 28, 29, 37, 41, 46, 47 |
| T0.5 |  | 0 |  | 6,84 | 3 | 65, 203, 312 | 18 | 45, 49, 53, 57, 66, 85, 202, 204, 208, 209, 211, 226, 227, 308, 309, 310, 314, 315 |
| T0.6 | 6,68 | 8 | 379, 381, 382, 383, 386, 387, 388, 390 | 17,60 | 1 | 413 | 3 | 380, 384, 385 |

Lignes sommées : 138 ; lignes estimées : 52 ; lignes au journal : 190.
