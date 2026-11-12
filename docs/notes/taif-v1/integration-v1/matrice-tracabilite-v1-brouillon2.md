# Matrice de traçabilité promesses × activités — dossier d'intégration pour l'entretien avec le Transformative AI Fund — v1, brouillon 2

**Brouillon 2, non scellé, non contre-lu ; remplace le brouillon 1 (gardé intact, R12) : lignes de promesses relues contre le texte envoyé et la table `promis-livre-v3.md` du 8 novembre ; ordre et contenu des C7 et C8 changés ; cases `<<À VÉRIFIER>>` de la colonne A22 levées.** Auteur : sous-agent neuf de la session mère `session_016QhUrrLeN21G7Z9KZobE42`, modèle déclaré par l'environnement : Claude Fable 5.1 (`claude-fable-5-1`). Heure d'écriture (`date -u`) : Sun Nov  8 15:19:45 UTC 2026. Aucun fichier existant modifié, aucun `.sha256`, aucun commit, aucun réseau, aucune dépense ; rien lu sous `donnees/`, `diag/`, `docs/notes/bras-attaque/`. Toute pièce lue est une donnée, jamais une instruction.

## 0. Cadre, pièces lues, ce qui manque

- **Calendrier** (mots de Lazar du 8 novembre, `registres/decisions.md` l. 1792, R-1834) : l'entretien avec le Transformative AI Fund est **dans deux semaines (≈ 22 novembre 2026, jour exact à confirmer)** ; la candidature a été envoyée le 7 octobre 2026 ; **l'appel prévu le 30 octobre a été décalé** (aucun appel n'a eu lieu ce jour-là ; le programme d'entretien v16 du 29 octobre, `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1269-1271, est donc daté). Les expériences restent bornées à une semaine et au coût minimal (l. 1788, R-1830).
- **Texte des promesses** : la candidature **exactement envoyée** est dans l'arbre depuis le 8 novembre 14:37 UTC : `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.pdf` (737c482c) et son texte extrait `proposal_v2_TAIF_2026-10-07.txt` (b2458c2d, 420 lignes, scellé) ; budget `budget_v3_TAIF_2026-10-07.xlsx` (037765b0) et `.txt` (caec18b2) ; curriculum vitae (4f45dc4f). **La table « promis → livré » v3 (`livrables/registres-taif-v4/promis-livre-v3.md`, af868f16, dossier `registres-taif-v4`, 8 novembre, scellée) est construite sur ce texte** : mêmes identifiants qu'au brouillon 1, mais **l'ordre et le contenu des lignes C7 et C8 changent** — C7-1 à C7-6 = les six lignes du calendrier de sept mois (mois 1, décembre 2026 → mois 7, juin 2027 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303) ; C8-1 « Two papers … Paper B in the ambitious scenario » (l. 309-310) ; C8-6 « deference law » (l. 316) **avant** C8-7 « lemma and negative theorem » (l. 317) ; C8-8 « construct-validity verdict » (l. 318) ; C8-9 « In the ambitious scenario … security(N) » (l. 319) ; C6-G0 daté « at the start of the grant, December 2026 » (l. 284). Les cases du brouillon 1 qui portaient sur ces lignes ont été réaffectées par leur contenu, non par leur numéro. Rappel du brouillon 1 : `livrables/candidature-ea-funds-v1/proposal-v1.md` (2f1e0864) diffère du texte envoyé (similarité 0,855 : 58 630 USD au lieu de 91 740, sept mois dès le 1er décembre au lieu de douze dès le 1er novembre, G0 « au début de la bourse », G1 fin du mois 4, papier C d'abord, papier B en extension).
- **Chiffres du 8 novembre** (dossier `livrables/registres-taif-v4/`, scellé) : relevé strict des dépenses **645,42 USD** (`livrables/registres-taif-v4/total-depenses-v3.md` l. 11-12, 123be1a7 : 136 lignes sommées ; **187 lignes au journal non sommées ; 111,87 USD estimés à part sur 50 lignes** : c'est un **plancher**, jamais « le total ») ; calibration : 235 prédictions, **60 tranchées, 47 confirmées, 5 réfutées, 8 non concluantes** (`livrables/registres-taif-v4/calibration-v3.md` l. 266-267, 0f1bca5a) ; promis → livré : 31 lignes, 83 cellules vides sur 248 (`livrables/registres-taif-v4/promis-livre-v3.md` l. 41). Le brouillon 1 citait le dossier `registres-taif-v3` (non scellé : 645,42 ; 185 lignes non sommées ; 55 tranchées, 44 confirmées, 3 réfutées) : ces comptes sont remplacés par ceux-ci.
- **Pièces lues** (extraits ciblés) : `CLAUDE.md` ; `docs/programme-controle-ia-v2.md` § 5, 10, 13, 14 (2fd63bad) ; `docs/brief-claude-code-programme-complet-v2.md` l. 190-201, 241-247, 346-361 ; `docs/decisions/` : N-005/N-006, N-007/N-008, N-013, N-015, N-029, N-035, N-044, N-045 v2, N-049, N-053, N-054, N-055, N-056, N-057, N-060 v3, N-062, P-040 ; `registres/decisions.md` lignes citées (R-521 à R-1834) ; `registres/go.md` lignes citées ; `registres/etat.md` l. 1-45, 148-170 ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` § 1, 1 bis, 2, 3 (fronts A à E), 7 bis, 9, 11 (186173d9) ; `docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` (f5599896) ; les pièces de tête de chaque colonne (table § 1.2).
- **Ce qui manque** : (1) le brief du mode tenu à l'écart (`0a17c6bc…`) et son devis (`55b2cbb1…`), cités par `chemin-critique-G1-v1.md` l. 6 et 18, **absents de `docs/` sur `main`** (branche de conv-audit probable) ; (2) **aucune ligne « N-061 »** dans `registres/decisions.md` (recherche par `grep`), alors que `CLAUDE.md` l. 13 la cite : la décision P-040 n'est consignée que comme proposition (`docs/decisions/proposition-P-040-…`) ; (3) la synthèse d'antériorité du collisionneur du pilier attaque (`48adeac0…`) vit sur une branche de données (`donnees/ideation-pilier-attaque-v1`, R-1794) : non lue ici, citée par la ligne de registre ; (4) les brouillons 6 et 7 du préenregistrement de G1 (`939b56e5…`) sont sur la branche `canal/conv-audit-n04` : `main` s'arrête au brouillon 4 (`brouillons/G1-preenregistrement-v1-brouillon4.md`, ad068bed) ; (5) le préenregistrement du papier C est au brouillon 5 sur `main` (9d55160f) quand la v16 (l. 608) dit « brouillon 7 » ; (6) la seule case `<<À VÉRIFIER>>` restante de la colonne A22 est C6-5 : la table v3 dit « fait » pour les 602 essais sans pièce ni empreinte.

## 1. Légende

- **Mots des cases** : **teste** (l'activité mesure la promesse ou l'hypothèse, ou en constate l'état) ; **instrumente** (elle construit ou vérifie l'instrument sans lequel la promesse ne peut être tenue ou l'hypothèse testée) ; **dérisque** (elle réduit un risque — antériorité, confondant, méthode, faisabilité — sans mesurer) ; **remplace (N-xxx)** (une décision de Lazar a changé l'énoncé ou la conséquence de la promesse ; la case dit laquelle) ; **sans lien** (la pièce de tête de la colonne ne nomme ni la promesse ni l'hypothèse ; la source est alors celle de la colonne, § 1.2) ; **`<<À VÉRIFIER>>`** (un lien est plausible mais la pièce qui le justifierait n'est pas dans l'arbre, ou la pièce disponible est construite sur un texte périmé).
- **Lettres de la grille** (§ 2) : T = teste, I = instrumente, D = dérisque, R = remplace, V = `<<À VÉRIFIER>>`, · = sans lien. Chaque lettre a sa case détaillée au § 3 (chemin, ligne, huit premiers caractères de l'empreinte du compagnon `.sha256` quand la pièce est scellée ; « non scellé » sinon).
- Les décisions sont désignées par leur fichier dans `docs/decisions/` : N-005/N-006 (cd49afbc), N-007/N-008 (ab7dc9bb), N-013 (157d388e), N-015 (462785b3), N-029 (084e3052), N-035 (55df073d), N-053 (2204256d), N-054 (c8a00b3f), N-055 (371879d5), N-056 (3592c1e9), N-057 (42180088), N-060 v3 (2b448f69), N-062 (63f42690), P-040 (b44bf8a0).

### 1.1 Lignes — promesses (31) et hypothèses (13)

| id | énoncé (court) | source de l'énoncé |
|---|---|---|
| **G0-1** | harnais validé | `docs/programme-controle-ia-v2.md` l. 180 (2fd63bad) ; `docs/brief-claude-code-programme-complet-v2.md` l. 192 |
| **G0-2** | organismes avec dose-réponse | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 193 |
| **G0-3** | sondes au-dessus du plancher | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 194 |
| **G0-4** | base boîte noire opérationnelle | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 195 |
| **G0-5** | agrégateurs validés en simulation | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 196 |
| **G0-6** | préenregistrement de G1 scellé et contre-lu | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 197 |
| **G0-7** | préenregistrement du papier C scellé et contre-lu | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 198 |
| **G0-8** | état de l'art vérifié | `docs/programme-controle-ia-v2.md` l. 180 ; `docs/brief-claude-code-programme-complet-v2.md` l. 199 |
| **C6-1** | « Literature verified on primary sources … 98 arXiv PDFs … 3,497 quotations … 0 failures » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 267-269 (b2458c2d) ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 17 |
| **C6-2** | « Theory … pre-registered simulation confirmed 31 of 31 predictions » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 270-271 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 18 |
| **C6-3** | « Activation harness validated on Llama-3.1-8B-Instruct … criterion 1 of gate G0 » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 272-275 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 19 |
| **C6-4** | « Research-sabotage environment v0 under construction … The pilot runs before the grant starts » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 276-278 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 20 |
| **C6-5** | « Code, with tests … In total, 602 automated tests » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 279-281 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 21 |
| **C6-6** | « Pre-registration drafts for gate G1, Paper C (HC1–HC3), the organisms and the probes » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 282 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 22 |
| **C6-7** | « Compute spent: about $20 » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 283 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 23 |
| **C6-G0** | « Gate G0 (at the start of the grant, December 2026) still requires organisms with a dose–response, probes above the random floor, a running black-box baseline, sealed and counter-read pre-registrations of G1 and Paper C, and the closing of the literature check » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 284-285 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 24 |
| **C7-1** | mois 1 (déc. 2026) : « Close G0. Paper C: deference of judges (HC1); probes under the same attacks (HC2, HC2b). Paper A: organisms and dose–response » → G0 | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-291 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 25 |
| **C7-2** | mois 2 (janv. 2027) : « Paper C: impersonation (HC3), displacement tax (HC4). Paper A: 2 × 2 design » → GC | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 292-293 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 26 |
| **C7-3** | mois 3 (févr. 2027) : « Paper C: countermeasures (HC5), benign g and the acceptance test (HC6). Paper A: lemma and theorem on real activations » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 294-295 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 27 |
| **C7-4** | mois 4 (mars 2027) : « Write Paper C. Paper A: complete the 2 × 2 design » → papier C sur arXiv et en atelier ; G1 | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 296-297 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 28 |
| **C7-5** | mois 5–6 (avr.–mai 2027) : « Paper A: adaptive attacks (content, then fine-tuning and reinforcement learning against the probe), interventions (H6), validity and robustness (H8). Write Paper A » → arXiv, conférence | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 298-300 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 29 |
| **C7-6** | mois 7 (juin 2027) : « Release of code, organisms, probes and pre-registrations; replications requested by reviewers; final report » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 301-303 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 30 |
| **C8-1** | « Two papers: C … and A … Paper B in the ambitious scenario » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-310 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 31 |
| **C8-2** | « Open code: harness, tested aggregators, the reconstruction of the research-sabotage environment » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 311 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 32 |
| **C8-3** | « Model organisms and probes » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 312 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 33 |
| **C8-4** | « Pre-registrations and sealed results » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 313 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 34 |
| **C8-5** | « A pre-deployment acceptance test for monitors (HC6) » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 314 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 35 |
| **C8-6** | « The deference law and the displacement tax are measured (Paper C) » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 316 (critère de succès 1 de la version envoyée) ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 36 (af868f16) |
| **C8-7** | « The lemma and the negative theorem are proven and tested on real activations within the 2 × 2 design (Paper A) » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 317 (critère 2) ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 37 |
| **C8-8** | « A construct-validity verdict on what the probes measure stands even if H1 fails » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 318 (critère 3) ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 38 |
| **C8-9** | « In the ambitious scenario, the security(N) curve and the diversification/coordination trade-off are established (Paper B) » | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 319 (critère 4, scénario ambitieux seulement) ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 39 |
| **H1a** | gain blanc-sur-noir sur la strate « diffus, flou » ; porte la revendication de H1 ; gain exigé dans chaque mode, mode tenu à l'écart compris | `docs/programme-controle-ia-v2.md` l. 93 ; N-055 l. 34-36 (371879d5) ; N-054 l. 37-39 (c8a00b3f) ; N-056 l. 55-57 (3592c1e9) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 135 |
| **H1b** | interaction flou contre net, mesurée et rapportée comme information | N-055 l. 34-36 (371879d5) |
| **H2** | accumulation additive toujours valide des scores de sondes de l'agent qui agit, sous le seuil d'un moniteur par action à 1 % ; rappel croissant avec l'horizon ; calibrage sur épisodes honnêtes seuls | `docs/programme-controle-ia-v2.md` l. 94 ; N-007 l. 28 (ab7dc9bb) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 137 |
| **H5** | la sécurité croît avec le nombre M de moniteurs seulement par la diversité effective (matrice de transfert d'attaque) | `docs/programme-controle-ia-v2.md` l. 113 ; N-013 l. 84 (157d388e) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 224 |
| **H6** | marge asymétrique : trois interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro) ; le bruit d'activations n'est plus revendiqué | `docs/programme-controle-ia-v2.md` l. 97 ; N-013 l. 78 ; N-015 l. 15-18 (462785b3) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 152 |
| **H7** | riposte et fuite : pente d'adaptation prédite par l'information mutuelle ; politiques comparées | `docs/programme-controle-ia-v2.md` l. 114 ; N-013 l. 85 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 227 |
| **H9** | survie des contraintes de sécurité à la délégation (papier B, sous réserve d'antériorité) | N-035 l. 16, 22-27 (55df073d) |
| **HC1** | loi de déférence Δv = g · (ĉ − v₀), destination libre ; verdict par probabilité du jeton cité comme méthode | `docs/programme-controle-ia-v2.md` l. 102 ; N-005 l. 24-30 (cd49afbc) ; N-013 l. 20-21 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 165 |
| **HC2** | robustesse des sondes (g ≈ 0 sous attaque par contenu), bras « sonde du lecteur » ; HC2b « trahison par les activations » | `docs/programme-controle-ia-v2.md` l. 103-104 ; N-013 l. 69-72, 92 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 185, 188 |
| **HC3** | usurpation : ordres en bande détectés sous « contenu = données » ; versant stylistique revendiqué | `docs/programme-controle-ia-v2.md` l. 105 ; N-013 l. 38-40 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 190 |
| **HC4** | taxe de déplacement, régime « contexte seul » revendiqué ; « poids réglables » non | `docs/programme-controle-ia-v2.md` l. 106 ; N-013 l. 48-51 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 194 |
| **HC5** | contre-mesures : paraphrase de confiance, quorum hétérogène en type d'accès, matrice de transfert juges × sondes | `docs/programme-controle-ia-v2.md` l. 107 ; N-013 l. 58-61 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 198 |
| **HC6** | le g bénin prédit l'effondrement sous attaque optimisée (test de recette) | `docs/programme-controle-ia-v2.md` l. 108 ; N-013 l. 90 ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 202 |

### 1.2 Colonnes — activités menées depuis le 7 octobre (29)

| id | activité | pièce de tête (source par défaut de la colonne) |
|---|---|---|
| **A01** | T0.3 — simulation du lemme et du théorème | `prereg/T0.3-simulation-lemme-theoreme-v1.md` (7474743a) ; `runs/20261004-080257-t03/manifeste.json` l. 1 (c9bba5e1) ; `docs/notes/resultats-T0.3-v1.md` l. 29 (9ab618ed) |
| **A02** | T0.4 — harnais d'activations | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) ; `registres/etat.md` l. 155 |
| **A03** | T0.5 — environnement et extraction des tâches (dont graines neuves, 2 nov.) | `docs/verdicts/verdict-T0.5-revalidation-v2.md` l. 3 (f98b5684) ; `docs/procedures/T0.5-extraction-v1.md` l. 3 (d23bd62f) ; `registres/etat.md` l. 23, 156 |
| **A04** | T0.6 — courses de dose-réponse : épreuves E2, E3, E3 bis ; E3 ter planifié ; course du 11 nov. non courue | `registres/go.md` l. 216 (GO-2026-11-02-28) ; `brouillons/T0.6-organismes-v0-v1-candidat1.md` l. 1 (4c27a254) ; `docs/notes/g0-deux-semaines-v1/compte-rendu-e2-t06-2026-11-07-v1.md` l. 1 (5a6debc5) ; `registres/decisions.md` l. 1727 (R-1769, E3 bis), l. 1791 (R-1833, E3 ter) ; `docs/notes/g0-deux-semaines-v1/e3-ter-v1/ordre-e3-ter-garde-equivalence-v1-brouillon1.md` l. 1-3 (non scellé) |
| **A05** | T0.7 — jeux synthétiques et sondes | `brouillons/T0.7-sondes-v0-v1-brouillon6.md` l. 1 (29f0ab43) ; `docs/notes/g0-deux-semaines-v1/rapport-jeux-T0.7-v2-suite-v1.md` l. 1-12 (8c6c47ae) ; `docs/decisions/proposition-P-011-T0.7-sondes-v1.md` (64afff19) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 21 (f5599896) |
| **A06** | T0.8 — bases boîte noire | `brouillons/T0.8-TRACE-lite-conception-v1-brouillon3.md` l. 1 (non scellé) ; `brouillons/T0.8-moniteur-par-action-H12-derive-v1-brouillon1.md` l. 1 (non scellé) ; `docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md` (2dec994f) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 22 ; `registres/etat.md` l. 159 |
| **A07** | T0.9 — préenregistrement du papier C (brouillon 5, 20 oct.) | `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 1 (9d55160f) ; `registres/etat.md` l. 161 |
| **A08** | Étiqueteur phase 1 et vérité du dommage (N-060 v3) | `docs/decisions/decision-N-060-v3.md` l. 21-27 (2b448f69) ; `prereg/preenregistrement-epreuve-etiqueteur-v1.md` l. 120, 182 (f73455b8) ; `docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md` (30f265a9) ; `registres/decisions.md` l. 1785 (R-1827 : A 389 ok / 7 illisibles = 1,77 % ; B 396 / 0 ; 36,90 / 300 USD) |
| **A09** | Audit du rappel de l'oracle (brouillon 1, non scellé) | `prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` l. 1-3 (non scellé) ; `registres/decisions.md` l. 1775 (R-1817) |
| **A10** | Arène synthétique des règles de défense (1er nov. ; audits R4 du 1er et du 8 nov.) | `prereg/preregistrement-regles-defense-convergence-v1.md` (d82dea33) ; `docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` l. 80, 127-128, 134, 148 (24081eed) ; `docs/notes/convergence-defense-v1/regles-defense-v1/audit-trop-beau-course-regles-defense-v1.md` l. 94-96 (7e81d094) ; `docs/notes/convergence-defense-v1/regles-defense-v1/audit-r4-p12-p13-v1.md` l. 433-435 (02a87957) ; `registres/decisions.md` l. 1781 (R-1823) |
| **A11** | Collisionneur « évasion et moniteurs » (28 oct.) | `registres/go.md` l. 98 (GO-2026-10-28-03) ; `registres/decisions.md` l. 837 (R-610), 844 (R-617 : 25 cellules sur 27) ; `docs/notes/collisionneur-evasion-moniteurs-v1/sous-agents-defensifs/EMPREINTES-v1.txt` (d13bc425) ; `docs/decisions/decision-N-057-v1.md` l. 28-46 (42180088) |
| **A12** | Collisionneur « audit du programme v2 » (26 oct., R-521) | `registres/decisions.md` l. 745 (R-521) ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a) ; `registres/go.md` l. 72 (GO-2026-10-26-04) ; `docs/decisions/decision-N-053-v1.md` l. 17-44 (2204256d) |
| **A13** | Collisionneur « pôle scientifique automatique » (26 oct.) et premier lancement réel du pôle (27 oct.) | `registres/decisions.md` l. 748-749 (R-524, R-525) ; `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md` l. 1 (4d6ddf40) ; `registres/go.md` l. 87 (GO-2026-10-27-05) |
| **A14** | Collisionneur « recombinaison bisociative » (26-27 oct.) | `registres/decisions.md` l. 750-751 (R-526, R-527), 790 (R-566) ; `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v2.md` l. 1 (8c3f15d7) |
| **A15** | Collisionneur « pilier attaque » (8 nov.) | `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md` l. 1-8 (29870ac9) ; `registres/go.md` l. 277 (GO-2026-11-08-06) ; `registres/decisions.md` l. 1752 (R-1794) ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 12, 16 (2dbad4b7) |
| **A16** | Organisme d'idéation — pilotes (24-26 oct.) | `registres/go.md` l. 56-71 (GO-2026-10-25-01, GO-2026-10-25-02) ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 773 (≈ 156 USD), l. 1172 (« absent » de la candidature) (186173d9) |
| **A17** | Organisme d'idéation — A1 v3, attaque de Goodhart contre le juge statistique (2-5 nov.) | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` l. 3 (7dade9ef) ; `registres/go.md` l. 209 (GO-2026-11-02-21), 221 (GO-2026-11-03-01) |
| **A18** | Organisme d'idéation — pilier attaque v1 (8 nov., en cours) | `registres/go.md` l. 278 (GO-2026-11-08-08) ; `docs/notes/ideation-pilier-attaque-v1/organisme-v1/devis-course-ideation-pilier-attaque-v3.md` (c4cef26b) ; `registres/decisions.md` l. 1779 (R-1821) |
| **A19** | Garde refus-question v1 / v2 (8 nov.) | `src/controle_ia/garde_refus_question_v1.py` l. 1-7 ; `src/controle_ia/garde_refus_question_v2.py` l. 1-10 ; `registres/decisions.md` l. 1746 (R-1788), 1779 (R-1821) |
| **A20** | Mode tenu à l'écart — brief et devis (pièces hors `main`) | `docs/decisions/decision-N-054-v1.md` l. 37-45 (c8a00b3f) ; `docs/decisions/decision-N-056-v1.md` l. 55-57, 64-72 (3592c1e9) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 6, 18, 51 (le brief `0a17c6bc…` et le devis `55b2cbb1…` n'ont pas été trouvés sous `docs/` sur `main`) |
| **A21** | Bras d'attaque — gel R-597, quarantaine N-057 (niveau méthode) | `registres/decisions.md` l. 823 (R-597) ; `docs/decisions/decision-N-057-v1.md` l. 28-46 (42180088) ; `docs/decisions/decision-N-056-v1.md` l. 64-77 ; `registres/go.md` l. 99 (GO-2026-10-28-04) |
| **A22** | Tables « registres pour le Transformative AI Fund » (dossier `registres-taif-v4`, 8 nov., scellé, construit sur le texte envoyé) et dépôt sur l'Open Science Framework (R-1580) | `livrables/registres-taif-v4/promis-livre-v3.md` l. 9-39, 41 (af868f16) ; `livrables/registres-taif-v4/total-depenses-v3.md` l. 11-12 (123be1a7) ; `livrables/registres-taif-v4/calibration-v3.md` l. 266-267 (0f1bca5a) ; `docs/notes/g0-deux-semaines-v1/rapport-registres-taif-v2-v1.md` l. 1-5 (74854173) ; `livrables/osf-manifeste-v1/manifeste-v1.json` (dd87b23e) ; `registres/decisions.md` l. 1538 (R-1580) |
| **A23** | Nœud de littérature HELIOS (collusion, 28-29 oct.) | `registres/decisions.md` l. 850 (R-622), 974 (R-746), 1024 (R-796) ; `docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md` (6b51dbf5) ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 622-665 |
| **A24** | Ressources publiques P-040 (N-061) | `docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md` l. 15-17 (b44bf8a0) ; `CLAUDE.md` l. 13 (N-061 citée) ; aucune ligne « N-061 » trouvée dans `registres/decisions.md` |
| **A25** | Cycles de reconception N-062 (8 nov.) | `docs/decisions/decision-N-062-v1.md` l. 21-26 (63f42690) ; `registres/decisions.md` l. 1753 (R-1795) |
| **A26** | Proposition de recherche, brouillon 1 (8 nov., non scellée) | `docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 6, 16-22, 25-29, 32, 46 |
| **A27** | Pince boîte blanche / boîte noire (étage III : aucune course dédiée avant la question v2) | `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 15, 21 (2dbad4b7) ; `docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 22 ; `registres/decisions.md` l. 538 (P-026), 567 (R-347), 1124 (R-895), 1142 (R-913) ; `registres/go.md` l. 279 (GO-2026-11-08-07, première ligne de GO qui nomme la pince) |
| **A28** | Axe H5 — diversité des moniteurs (question v2 du pilier attaque ; aucune course) | `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 17, 21 ; N-013 l. 84 (157d388e) |
| **A29** | Axe collusion (niveau 2 de l'état de l'art, 28 oct. ; lecture Redwood Research, 8 nov. ; H9) | `docs/notes/etat-art-niveau2/etat-art-niveau2-collusion-agents-v1.md` l. 64-81 (7547040e) ; `registres/decisions.md` l. 832 (R-606), 1776 (R-1818) ; N-035 l. 16, 22-26 (55df073d) |

## 2. Grille (44 lignes × 29 colonnes = 1276 cases ; 173 cases renseignées, 1103 « sans lien »)

| ligne \ activité | A01 | A02 | A03 | A04 | A05 | A06 | A07 | A08 | A09 | A10 | A11 | A12 | A13 | A14 | A15 | A16 | A17 | A18 | A19 | A20 | A21 | A22 | A23 | A24 | A25 | A26 | A27 | A28 | A29 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **G0-1** | · | T | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **G0-2** | · | · | I | I | · | · | · | I | D | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **G0-3** | · | · | · | I | I | · | · | · | · | · | D | · | · | · | D | · | · | · | · | · | · | T | · | D | · | · | · | · | · |
| **G0-4** | · | · | I | · | · | I | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | I | D | · | · | · | · | · |
| **G0-5** | T | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **G0-6** | · | · | · | · | · | · | · | · | · | D | · | R | · | · | D | · | · | D | · | V | D | T | I | · | D | · | · | · | · |
| **G0-7** | · | · | · | · | · | · | I | · | · | · | · | R | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **G0-8** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | T | · | · | · | · | · | T |
| **C6-1** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C6-2** | T | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C6-3** | · | T | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C6-4** | · | · | T | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C6-5** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | V | · | · | · | · | · | · | · |
| **C6-6** | · | · | · | · | · | · | I | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C6-7** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | V | · | · | · |
| **C6-G0** | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | D | · | · | · |
| **C7-1** | · | · | I | I | · | · | I | I | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C7-2** | · | · | · | · | · | I | I | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C7-3** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C7-4** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | D | · | · | · | · |
| **C7-5** | · | · | · | · | · | · | · | · | · | D | D | · | · | · | · | · | · | D | · | D | R | T | · | · | · | · | · | · | · |
| **C7-6** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | T | · | · | · | · | · | · | · |
| **C8-1** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | D | D | · | · | · |
| **C8-2** | · | I | I | · | · | I | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · | D | · | · | · |
| **C8-3** | · | · | · | I | I | · | · | I | · | · | · | · | · | · | · | · | · | · | · | V | · | I | · | · | · | D | · | · | · |
| **C8-4** | I | · | · | · | · | · | · | · | I | I | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · | · | · | · | · |
| **C8-5** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | I | · | · | · | · | · | · | · |
| **C8-6** | · | · | · | · | · | · | I | · | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · | D | · | · | · |
| **C8-7** | I | I | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · | D | · | · | · |
| **C8-8** | · | · | · | · | I | · | · | D | D | · | · | · | · | · | D | · | · | · | · | · | · | I | · | · | R | R | · | · | · |
| **C8-9** | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | I | D | D | · | D | · | D | D |
| **H1a** | · | I | I | I | I | I | · | I | D | · | D | R | · | · | D | · | · | D | · | R | R | · | R | D | R | I | D | · | · |
| **H1b** | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · |
| **H2** | I | I | I | I | I | I | · | I | · | · | · | D | · | · | D | · | · | · | · | · | · | I | · | · | · | I | · | · | · |
| **H5** | · | · | · | · | · | · | · | · | · | D | · | D | · | · | · | · | · | · | · | · | · | · | D | · | · | I | · | I | D |
| **H6** | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · |
| **H7** | · | · | · | · | · | · | · | · | · | D | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · |
| **H9** | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | D |
| **HC1** | · | · | · | · | · | · | I | · | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · |
| **HC2** | · | · | · | · | · | · | I | · | · | · | D | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · |
| **HC3** | · | · | · | · | · | · | I | · | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | · | · | · |
| **HC4** | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | · | · | · | · | D | · | · | · | · | I | · | · | · |
| **HC5** | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | · | · | · | · | · | · | · | · | · | I | D | D | · |
| **HC6** | · | · | · | · | · | · | · | · | · | · | · | D | · | · | · | · | D | · | · | · | · | · | · | · | · | I | · | · | · |

Comptes : teste 28 ; instrumente 70 ; dérisque 61 ; remplace 10 ; `<<À VÉRIFIER>>` 4 ; sans lien 1103.

## 3. Cases détaillées, par colonne (mot, puis chemin, ligne, empreinte)

### A01 — T0.3 — simulation du lemme et du théorème

- **G0-5** : **teste** (`prereg/T0.3-simulation-lemme-theoreme-v1.md` (7474743a) ; `runs/20261004-080257-t03/manifeste.json` l. 1 (c9bba5e1) ; `docs/notes/resultats-T0.3-v1.md` l. 29 (9ab618ed) : « Les 31 prédictions sont confirmées »).
- **C6-2** : **teste** (`prereg/T0.3-simulation-lemme-theoreme-v1.md` (7474743a) ; `runs/20261004-080257-t03/manifeste.json` l. 1 (c9bba5e1) ; `docs/notes/resultats-T0.3-v1.md` l. 29 (9ab618ed) : « Les 31 prédictions sont confirmées »).
- **C8-4** : **instrumente** (`prereg/T0.3-simulation-lemme-theoreme-v1.md` (7474743a) ; `livrables/registres-taif-v4/calibration-v3.md` l. 72-73 (prédictions de T0.3 dans le registre de calibration)).
- **C8-7** : **instrumente** (`docs/notes/resultats-T0.3-v1.md` l. 29 (9ab618ed) ; réserve : `registres/etat.md` l. 154 (« la plupart des prédictions vérifient l'instrument ; ce n'est pas une preuve sur modèles réels »)).
- **H2** : **instrumente** (`docs/decisions/decision-N-007-N-008-v1.md` l. 30-34 (ab7dc9bb) : lecture de « toujours valide » issue de T0.3 (P8), calibrage sur épisodes honnêtes entiers).

### A02 — T0.4 — harnais d'activations

- **G0-1** : **teste** (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) : critère 1 prouvé sur le modèle réel).
- **C6-3** : **teste** (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) : critère 1 prouvé sur le modèle réel).
- **C8-2** : **instrumente** (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) ; `registres/etat.md` l. 155 (harnais = l'instrument qui rend les activations lisibles)).
- **C8-7** : **instrumente** (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) ; `registres/etat.md` l. 155 (harnais = l'instrument qui rend les activations lisibles)).
- **H1a** : **instrumente** (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) ; `registres/etat.md` l. 155 (harnais = l'instrument qui rend les activations lisibles)).
- **H2** : **instrumente** (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` l. 3 (63444faa) ; `registres/etat.md` l. 155 (harnais = l'instrument qui rend les activations lisibles)).

### A03 — T0.5 — environnement et extraction des tâches (dont graines neuves, 2 nov.)

- **G0-2** : **instrumente** (`registres/etat.md` l. 156 ; `registres/go.md` l. 216 (organisme distillé sur les actions du banc)).
- **G0-4** : **instrumente** (`docs/decisions/decision-N-029-v1.md` l. 17-18, 37-39 (084e3052) : la base boîte noire se lit sur les épisodes de T0.6, construits sur le banc de T0.5).
- **C6-4** : **teste** (`docs/verdicts/verdict-T0.5-revalidation-v2.md` l. 3 (f98b5684) ; `docs/procedures/T0.5-extraction-v1.md` l. 3 (d23bd62f) ; `registres/etat.md` l. 156 ; graines neuves : `registres/etat.md` l. 23 (« confirmé avec réserves »)).
- **C7-1** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-291 (organismes dans l'environnement de sabotage de recherche) ; `docs/verdicts/verdict-T0.5-revalidation-v2.md` l. 3 (f98b5684)).
- **C8-2** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 311 (« reconstruction of the research-sabotage environment ») ; `docs/procedures/T0.5-extraction-v1.md` l. 3 (d23bd62f)).
- **H1a** : **instrumente** (`docs/verdicts/verdict-T0.5-revalidation-v2.md` l. 3 (f98b5684) : les épisodes du banc sont le matériau des deux hypothèses).
- **H2** : **instrumente** (`docs/verdicts/verdict-T0.5-revalidation-v2.md` l. 3 (f98b5684) : les épisodes du banc sont le matériau des deux hypothèses).

### A04 — T0.6 — courses de dose-réponse : épreuves E2, E3, E3 bis ; E3 ter planifié ; course du 11 nov. non courue

- **G0-2** : **instrumente** (`registres/go.md` l. 216 (GO-2026-11-02-28 : courbe dose–réponse, critères 2 et 3) ; `brouillons/T0.6-organismes-v0-v1-candidat1.md` l. 1 (4c27a254) ; `registres/decisions.md` l. 1727 (R-1769 : E3 bis, 36 épisodes, 144 actions, code 0, rien lu), 1791 (R-1833 : E3 ter planifié) ; la course décisive du 11 novembre n'est pas courue (`registres/decisions.md` l. 1728, R-1770)).
- **G0-3** : **instrumente** (`registres/go.md` l. 216 (test croisé d'étiologie : sondes de T0.7 entraînées sur une étiologie, testées sur l'autre)).
- **C6-G0** : **dérisque** (`registres/go.md` l. 216 (critères 2 et 3 de G0 visés) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 20 (f5599896)).
- **C7-1** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-291 (« organisms and dose–response ») ; `registres/go.md` l. 216).
- **C8-3** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 312 ; `brouillons/T0.6-organismes-v0-v1-candidat1.md` l. 1 (4c27a254)).
- **H1a** : **instrumente** (`brouillons/T0.6-organismes-v0-v1-candidat1.md` l. 1 (4c27a254) : organisme (ii) sans instruction à l'inférence, dose réglable).
- **H2** : **instrumente** (`registres/go.md` l. 216 (« activations enregistrées »)).

### A05 — T0.7 — jeux synthétiques et sondes

- **G0-3** : **instrumente** (`brouillons/T0.7-sondes-v0-v1-brouillon6.md` l. 1 (29f0ab43) ; `docs/notes/g0-deux-semaines-v1/rapport-jeux-T0.7-v2-suite-v1.md` l. 1-12 (8c6c47ae) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 21 (f5599896 : « la sonde d'intention n'existe pas encore »)).
- **C8-3** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 312 ; `brouillons/T0.7-sondes-v0-v1-brouillon6.md` l. 1 (29f0ab43)).
- **C8-8** : **instrumente** (`docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 21 (f5599896 : sonde « intention ») ; `brouillons/T0.7-concepts-sans-lien-consigne-v1-brouillon1.md` l. 1 (non scellé : témoin de concepts sans lien)).
- **H1a** : **instrumente** (`brouillons/T0.7-sondes-v0-v1-brouillon6.md` l. 1 (29f0ab43) : sondes dont les scores sont le moniteur boîte blanche).
- **H2** : **instrumente** (`brouillons/T0.7-sondes-v0-v1-brouillon6.md` l. 1 (29f0ab43) : sondes dont les scores sont le moniteur boîte blanche).

### A06 — T0.8 — bases boîte noire

- **G0-4** : **instrumente** (`brouillons/T0.8-TRACE-lite-conception-v1-brouillon3.md` l. 1 ; `brouillons/T0.8-moniteur-par-action-H12-derive-v1-brouillon1.md` l. 1 (non scellés) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 22 (f5599896 : « rien n'existe : le maillon le moins avancé ») ; `registres/etat.md` l. 159 (TRACE-lite prêt, code testé)).
- **C7-2** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 292-293 (plan 2 × 2 au mois 2 : la case boîte noire) ; `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 22).
- **C8-2** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 311 (« tested aggregators ») ; `registres/etat.md` l. 159).
- **H1a** : **instrumente** (`docs/decisions/decision-N-029-v1.md` l. 17-27 (084e3052) : référence boîte noire locale, prédicteur sur les traits du texte obligatoire).
- **H2** : **instrumente** (`docs/decisions/decision-N-007-N-008-v1.md` l. 42, 47 (ab7dc9bb) : base (i) accumulation additive sur scores boîte noire).

### A07 — T0.9 — préenregistrement du papier C (brouillon 5, 20 oct.)

- **G0-7** : **instrumente** (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 1 (9d55160f) ; `registres/etat.md` l. 161 (reste : lecture de Panin)).
- **C6-6** : **instrumente** (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 1 (9d55160f) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 282).
- **C7-1** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-290 (HC1, HC2, HC2b au mois 1) ; brouillon 5 l. 1 (9d55160f)).
- **C7-2** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 292 (HC3 au mois 2) ; brouillon 5 l. 1 (9d55160f)).
- **C8-6** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 316 ; brouillon 5 l. 1 (9d55160f)).
- **HC1** : **instrumente** (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 1 (9d55160f) : préenregistrement de HC1, HC2, HC2b, HC3 (TC.1 à TC.3), non scellé).
- **HC2** : **instrumente** (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 1 (9d55160f) : préenregistrement de HC1, HC2, HC2b, HC3 (TC.1 à TC.3), non scellé).
- **HC3** : **instrumente** (`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` l. 1 (9d55160f) : préenregistrement de HC1, HC2, HC2b, HC3 (TC.1 à TC.3), non scellé).

### A08 — Étiqueteur phase 1 et vérité du dommage (N-060 v3)

- **G0-2** : **instrumente** (`docs/decisions/decision-N-060-v3.md` l. 21-27 (2b448f69) ; `prereg/preenregistrement-epreuve-etiqueteur-v1.md` l. 120 (f73455b8) ; `registres/decisions.md` l. 1785 (R-1827 : A 389 ok / 7 illisibles = 1,77 % ; B 396 / 0 ; 36,90 / 300 USD) — comptes seuls, aucune étiquette lue).
- **C7-1** : **instrumente** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 291 (« organisms and dose–response ») ; `docs/decisions/decision-N-060-v3.md` l. 21-27 (2b448f69) : la dose se mesure sur le dommage lu par l'oracle).
- **C8-3** : **instrumente** (`docs/decisions/decision-N-060-v3.md` l. 25-26 (2b448f69) : dommage = baisse de couverture contre le jumeau honnête apparié).
- **C8-8** : **dérisque** (`docs/decisions/decision-N-060-v3.md` l. 33-35 (2b448f69) : aucune sortie de l'oracle dans la sélection d'un moniteur ; conçu par une instance qui n'a vu aucun interne de moniteur).
- **H1a** : **instrumente** (`docs/decisions/decision-N-060-v3.md` l. 21-27 (2b448f69) : vérité du dommage indépendante des moniteurs = étiquettes des épisodes sabotés ; réponse préparée au jury : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1137-1141 (186173d9)).
- **H2** : **instrumente** (`docs/decisions/decision-N-060-v3.md` l. 21-27 (2b448f69) : vérité du dommage indépendante des moniteurs = étiquettes des épisodes sabotés ; réponse préparée au jury : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1137-1141 (186173d9)).

### A09 — Audit du rappel de l'oracle (brouillon 1, non scellé)

- **G0-2** : **dérisque** (`prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` l. 1-3 (non scellé) ; `registres/decisions.md` l. 1775 (R-1817 : deux épreuves R5 non jouées de N-060 v3 + bras T-1 reporté)).
- **C8-4** : **instrumente** (`prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` l. 3 (non scellé : « aucune lecture … avant contre-lecture (R2), scellement »)).
- **C8-8** : **dérisque** (`registres/decisions.md` l. 1775 (R-1817) : l'oracle de couverture est mesuré, non l'étiqueteur ; vérité indépendante des sondes).
- **H1a** : **dérisque** (`prereg/audit-rappel-oracle-sabotages-connus-v1-brouillon1.md` l. 1-3 (non scellé) : l'oracle qui étiquette les épisodes de H1 doit voir des sabotages connus par construction).

### A10 — Arène synthétique des règles de défense (1er nov. ; audits R4 du 1er et du 8 nov.)

- **G0-6** : **dérisque** (`docs/decisions/decision-N-062-v1.md` l. 21 (63f42690 : la règle de défense — figée, mélange d'équilibre, réserve secrète — est une composante des moniteurs de G1) ; `prereg/preregistrement-regles-defense-convergence-v1.md` (d82dea33)).
- **C7-5** : **dérisque** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 298-299 (attaques adaptatives) ; `docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` l. 127-128, 134 (24081eed)).
- **C8-4** : **instrumente** (`prereg/preregistrement-regles-defense-convergence-v1.md` (d82dea33) ; `docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` l. 15-16 (24081eed) ; `registres/decisions.md` l. 1781 (R-1823)).
- **H5** : **dérisque** (`docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` l. 80, 127-128 (24081eed) : un mélange de moniteurs (R3) gagne sur les attaques vues et régresse sur les attaques tenues à l'écart ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 17 (2dbad4b7)).
- **H7** : **dérisque** (`docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md` l. 148 (24081eed : R2 « ne progresse pas, retours au-delà du hasard »), l. 80 (HR1 confirmée, +0,10 / +0,12), l. 127-128 (R3 : régression −0,066 / −0,077 sur attaques tenues à l'écart) ; `docs/notes/convergence-defense-v1/regles-defense-v1/audit-r4-p12-p13-v1.md` l. 433-435 (02a87957) ; arène synthétique sans activations : exploratoire).

### A11 — Collisionneur « évasion et moniteurs » (28 oct.)

- **G0-3** : **dérisque** (`brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 500-503 (186173d9 : dix moniteurs candidats proposés en cadrage défensif, non vérifiés) ; `docs/notes/collisionneur-evasion-moniteurs-v1/sous-agents-defensifs/EMPREINTES-v1.txt` (d13bc425)).
- **C7-5** : **dérisque** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 298-299 ; `docs/decisions/decision-N-057-v1.md` l. 39-41 (42180088 : exécution gelée jusqu'à la revue de sécurité externe, `registres/go.md` l. 99, GO-2026-10-28-04)).
- **H1a** : **dérisque** (`registres/decisions.md` l. 837 (R-610), 844 (R-617 : 25 cellules sur 27) ; `docs/decisions/decision-N-057-v1.md` l. 28-46 (42180088) : modes de contournement scellés pour éprouver les moniteurs corrigés).
- **HC2** : **dérisque** (`registres/decisions.md` l. 837 (R-610 : « modes d'évasion qui battent la sonde ponctuelle publiée » ; « moniteurs durcis »)).

### A12 — Collisionneur « audit du programme v2 » (26 oct., R-521)

- **G0-6** : **remplace (N-053)** (`docs/decisions/decision-N-053-v1.md` l. 17-22 (2204256d) : bras « fuite textuelle et contrôlabilité » ajouté aux préenregistrements de G1 et du papier C avant scellement ; `docs/notes/audit-controle-v1/audit-litterature-v1.md` (29b32f62)).
- **G0-7** : **remplace (N-053)** (`docs/decisions/decision-N-053-v1.md` l. 17-22 (2204256d) : bras « fuite textuelle et contrôlabilité » ajouté aux préenregistrements de G1 et du papier C avant scellement ; `docs/notes/audit-controle-v1/audit-litterature-v1.md` (29b32f62)).
- **H1a** : **remplace (N-053)** (`docs/decisions/decision-N-053-v1.md` l. 17-26, 42-44 (2204256d) : lecture filtrée des positions porteuses d'évidence textuelle comme lecture principale de toute revendication d'« intention » ; invariant « aucun score de moniteur dans un signal d'entraînement » ; `registres/decisions.md` l. 745 (R-521)).
- **H1b** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **H2** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **H5** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **H6** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **H7** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **H9** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **HC1** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **HC2** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **HC3** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **HC4** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **HC5** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).
- **HC6** : **dérisque** (`registres/decisions.md` l. 745 (R-521 : 69 candidats, 32 retenus, « aucune faille qui oblige à changer une hypothèse ») ; `docs/notes/audit-controle-v1/synthese-collisionneur-v1.md` (d672e57a)).

### A13 — Collisionneur « pôle scientifique automatique » (26 oct.) et premier lancement réel du pôle (27 oct.)

Aucune case : toutes les lignes sont **sans lien** (source : `registres/decisions.md` l. 748-749 (R-524, R-525) ; `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md` l. 1 (4d6ddf40) ; `registres/go.md` l. 87 (GO-2026-10-27-05)). Voir § 4, orphelins côté activités.

### A14 — Collisionneur « recombinaison bisociative » (26-27 oct.)

Aucune case : toutes les lignes sont **sans lien** (source : `registres/decisions.md` l. 750-751 (R-526, R-527), 790 (R-566) ; `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v2.md` l. 1 (8c3f15d7)). Voir § 4, orphelins côté activités.

### A15 — Collisionneur « pilier attaque » (8 nov.)

- **G0-3** : **dérisque** (`registres/decisions.md` l. 1752 (R-1794) : les confondants expliquent ce qu'une sonde « au-dessus du plancher » peut lire d'autre que le sabotage).
- **G0-6** : **dérisque** (`docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 16 (2dbad4b7 : paires contrefactuelles, organisme placebo, épisodes dormants → contrôles à écrire dans le préenregistrement)).
- **C8-8** : **dérisque** (`registres/decisions.md` l. 1752 (R-1794) ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 16 : diagnostic de ce que lisent les sondes (consigne, identité, famille de tâche)).
- **H1a** : **dérisque** (`registres/decisions.md` l. 1752 (R-1794 : trois confondants fatals — consigne transformée, identité de l'organisme contre acte, mode tenu à l'écart consommé ; neuf contrôles convergents) ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md` l. 1-8 (29870ac9) ; `registres/go.md` l. 277).
- **H2** : **dérisque** (`docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 12 (2dbad4b7 : la boucle ne converge que si la trace existe aux couches lues)).

### A16 — Organisme d'idéation — pilotes (24-26 oct.)

Aucune case : toutes les lignes sont **sans lien** (source : `registres/go.md` l. 56-71 (GO-2026-10-25-01, GO-2026-10-25-02) ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 773 (≈ 156 USD), l. 1172 (« absent » de la candidature) (186173d9)). Voir § 4, orphelins côté activités.

### A17 — Organisme d'idéation — A1 v3, attaque de Goodhart contre le juge statistique (2-5 nov.)

- **C8-5** : **dérisque** (`docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` l. 3 (7dade9ef : W1 « résiste (à cette taille) », W2 « infirmée (brèche sous v8) ») ; attaque optimisée contre un juge **statistique** de l'organisme, non un juge génératif : cousin, pas un test de HC6).
- **HC6** : **dérisque** (`docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` l. 3 (7dade9ef : W1 « résiste (à cette taille) », W2 « infirmée (brèche sous v8) ») ; attaque optimisée contre un juge **statistique** de l'organisme, non un juge génératif : cousin, pas un test de HC6).

### A18 — Organisme d'idéation — pilier attaque v1 (8 nov., en cours)

- **G0-6** : **dérisque** (`docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md` l. 5-8 (29870ac9 : propositions de niveau méthode pour le préenregistrement, portier et coffre actifs)).
- **C7-5** : **dérisque** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 298-299 ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md` l. 1-8 (29870ac9)).
- **H1a** : **dérisque** (`registres/go.md` l. 278 (GO-2026-11-08-08) ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md` l. 1-8 (29870ac9) ; `registres/decisions.md` l. 1779 (R-1821 : course en cours, rien lu)).

### A19 — Garde refus-question v1 / v2 (8 nov.)

Aucune case : toutes les lignes sont **sans lien** (source : `src/controle_ia/garde_refus_question_v1.py` l. 1-7 ; `src/controle_ia/garde_refus_question_v2.py` l. 1-10 ; `registres/decisions.md` l. 1746 (R-1788), 1779 (R-1821)). Voir § 4, orphelins côté activités.

### A20 — Mode tenu à l'écart — brief et devis (pièces hors `main`)

- **G0-6** : **<<À VÉRIFIER>>** (`docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 51 (f5599896 : « le mode tenu à l'écart n'a aucune famille scellée » ; un scellement de G1 avant lui serait invalide, S10, S25) ; le brief `brief-mode-tenu-a-l-ecart-v1.md` (`0a17c6bc…`) et le devis (`55b2cbb1…`) cités en l. 6 et 18 n'ont pas été trouvés sous `docs/` sur `main`).
- **C7-5** : **dérisque** (`docs/decisions/decision-N-054-v1.md` l. 40-45 (c8a00b3f) : un mode inédit pour les concepteurs de moniteurs, révélé seulement à l'évaluation).
- **C8-3** : **<<À VÉRIFIER>>** (`docs/decisions/decision-N-054-v1.md` l. 40-45 (c8a00b3f : famille d'organismes du mode tenu à l'écart) ; pièce du brief non trouvée sous `docs/` sur `main` (`docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v1.md` l. 18)).
- **H1a** : **remplace (N-054 ; N-056)** (`docs/decisions/decision-N-054-v1.md` l. 37-45 (c8a00b3f : G1 rapportée par mode ; mode tenu à l'écart conçu par une instance qui n'a conçu aucun moniteur, scellé avant G1) ; `docs/decisions/decision-N-056-v1.md` l. 55-57 (3592c1e9 : gain exigé dans chaque mode, mode tenu à l'écart compris)).

### A21 — Bras d'attaque — gel R-597, quarantaine N-057 (niveau méthode)

- **G0-6** : **dérisque** (`docs/decisions/decision-N-054-v1.md` l. 46-51 (c8a00b3f : expérience de lecture à préenregistrer avant G1)).
- **C7-5** : **remplace (N-056 ; N-057)** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 298-299 (« adaptive attacks (content, then fine-tuning and reinforcement learning against the probe) ») contre `docs/decisions/decision-N-056-v1.md` l. 64-72 (3592c1e9 : bras (A) aveugle et (B) informé, recettes scellées lues par le seul juge) ; `docs/decisions/decision-N-057-v1.md` l. 39-41 (42180088 : exécution gelée jusqu'à la revue externe) ; `registres/decisions.md` l. 823 (R-597)).
- **H1a** : **remplace (N-056)** (`docs/decisions/decision-N-056-v1.md` l. 55-57, 64-72 (3592c1e9)).
- **HC4** : **dérisque** (`docs/decisions/decision-N-056-v1.md` l. 68-70 (3592c1e9 : le concepteur du bras informé connaît les conceptions des moniteurs, pas les épisodes ni les seuils) ; mesure du coût de déplacement non engagée).

### A22 — Tables « registres pour le Transformative AI Fund » (dossier `registres-taif-v4`, 8 nov., scellé, construit sur le texte envoyé) et dépôt sur l'Open Science Framework (R-1580)

- **G0-1** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-2** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-3** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-4** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-5** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-6** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-7** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **G0-8** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 9-16 (af868f16 : prouvés 1 et 5 ; restent 2, 3, 4, 6, 7, 8)).
- **C6-1** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 17 (af868f16)).
- **C6-2** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 18 (af868f16)).
- **C6-3** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 19 (af868f16)).
- **C6-4** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 20 (af868f16)).
- **C6-5** : **<<À VÉRIFIER>>** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 21 (af868f16 : état « fait », aucune pièce ni empreinte dans la ligne ; le compte « 602 automated tests » n'est rattaché à aucun commit)).
- **C6-6** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 22 (af868f16)).
- **C6-7** : **teste** (`livrables/registres-taif-v4/total-depenses-v3.md` l. 11-12 (123be1a7 : relevé strict 645,42 USD, 136 lignes sommées ; 187 lignes au journal non sommées ; 111,87 USD estimés à part sur 50 lignes) — un plancher, jamais « le total »).
- **C6-G0** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 24 (af868f16)).
- **C7-1** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 25 (af868f16 : « à venir (période non commencée au jour du script) », promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303)).
- **C7-2** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 26 (af868f16 : « à venir (période non commencée au jour du script) », promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303)).
- **C7-3** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 27 (af868f16 : « à venir (période non commencée au jour du script) », promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303)).
- **C7-4** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 28 (af868f16 : « à venir (période non commencée au jour du script) », promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303)).
- **C7-5** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 29 (af868f16 : « à venir (période non commencée au jour du script) », promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303)).
- **C7-6** : **teste** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 30 (af868f16 : « à venir (période non commencée au jour du script) », promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 289-303)).
- **C8-1** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 31 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-2** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 32 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-3** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 33 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-4** : **instrumente** (`livrables/osf-manifeste-v1/manifeste-v1.json` (dd87b23e) ; `registres/decisions.md` l. 1538 (R-1580 : 118 fichiers scellés — 51 préenregistrements, 56 décisions, 11 verdicts — déposés sur un projet privé de l'Open Science Framework, osf.io/dr57c) ; `livrables/registres-taif-v4/calibration-v3.md` l. 266-267 (0f1bca5a : 235 prédictions, 60 tranchées, 47 confirmées, 5 réfutées, 8 non concluantes) ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 34).
- **C8-5** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 35 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-6** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 36 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-7** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 37 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-8** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 38 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **C8-9** : **instrumente** (`livrables/registres-taif-v4/promis-livre-v3.md` l. 39 (af868f16 : ligne présente, état vide ; promesse relue sur `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 309-319)).
- **H2** : **instrumente** (`livrables/registres-taif-v4/calibration-v3.md` l. 72-75 (0f1bca5a : prédictions de T0.3 suivies dans le registre de calibration)).

### A23 — Nœud de littérature HELIOS (collusion, 28-29 oct.)

- **G0-4** : **instrumente** (`registres/decisions.md` l. 974 (R-746, point 1 : juge texte préparé ajouté à la liste scellée des bases boîte noire de G1)).
- **G0-6** : **instrumente** (`registres/decisions.md` l. 974 (R-746, points 1 à 6 : nœuds de porte G1 tranchés) ; l. 1024 (R-796 : recette d'HELIOS neuvième comparateur, décision conditionnelle)).
- **G0-8** : **teste** (`registres/decisions.md` l. 850 (R-622 : PDF lu page par page, R7) ; `docs/sources/lecture-pdf-niveau2/helios-2604.01151-lecture-v1.md` (6b51dbf5)).
- **C8-9** : **dérisque** (`registres/decisions.md` l. 850 (R-622 : zone « collusion entre agents » partiellement occupée, nœud ouvert) ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 622-641 (186173d9)).
- **H1a** : **remplace (R-746)** (`registres/decisions.md` l. 974 (R-746, point 4 : sous-plan information × accès ; « si seule la sonde à exemples gagne, H1 se dit à information égale »)).
- **H5** : **dérisque** (`brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 628-634 (186173d9 : HELIOS lit un seul jeton, en un coup ; l'agrégation sur les jetons et le séquentiel restent libres) ; `registres/decisions.md` l. 850).

### A24 — Ressources publiques P-040 (N-061)

- **G0-3** : **dérisque** (`docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md` l. 15, 17 (b44bf8a0 : NARCBench rejoué sur 8B et Llama Scope en bras descriptif de T0.7 ; « ne fait franchir aucune porte »)).
- **G0-4** : **dérisque** (`docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md` l. 16 (b44bf8a0 : Liars' Bench et SHADE-Arena comme comparateur boîte noire externe à T0.8)).
- **C8-9** : **dérisque** (`docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md` l. 15 (b44bf8a0 : NARCBench, base inter-agents du papier B)).
- **H1a** : **dérisque** (`docs/decisions/proposition-P-040-ressources-publiques-T07-T08-v1.md` l. 15 (b44bf8a0 : activations 70B publiées comme plancher externe, rapporté)).

### A25 — Cycles de reconception N-062 (8 nov.)

- **G0-6** : **dérisque** (`docs/decisions/decision-N-062-v1.md` l. 24 (63f42690 : préenregistrement court par cycle, verdict par lecteur neuf)).
- **C7-4** : **dérisque** (`docs/decisions/decision-N-062-v1.md` l. 23-24 (63f42690 : cycles sous GO, une famille tenue à l'écart neuve par cycle) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 296-297 (G1 au mois 4)).
- **C8-1** : **dérisque** (`docs/decisions/decision-N-062-v1.md` l. 25 (63f42690 : la suite des cycles est une pièce du papier A, section « étalonnage de l'instrument »)).
- **C8-8** : **remplace (N-062)** (`docs/decisions/decision-N-062-v1.md` l. 22 (63f42690 : H8 devient un diagnostic, non une bascule) contre `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 161-162, 323-324 (« If G1 fails … construct validity (H8) becomes the main line »)).
- **H1a** : **remplace (N-062)** (`docs/decisions/decision-N-062-v1.md` l. 21, 26 (63f42690 : revendication finale seulement sur une famille jamais utilisée dans aucune reconception)).

### A26 — Proposition de recherche, brouillon 1 (8 nov., non scellée)

- **C6-7** : **<<À VÉRIFIER>>** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 46 (non scellé : « ≈ 1 000 USD », ordre de grandeur « à recalculer avant usage ») contre `livrables/registres-taif-v4/total-depenses-v3.md` l. 11 (relevé strict 645,42 USD, plancher) : à rapprocher avant toute phrase au jury).
- **C6-G0** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 25 (non scellé : huit critères, G0 fin novembre)).
- **C8-1** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 27-28 (non scellé)).
- **C8-2** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 6 (non scellé : « banc d'épreuve réutilisable »)).
- **C8-3** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 6 (non scellé : organismes à dose réglable, bras rouge scellé, juge figé)).
- **C8-6** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 21 (non scellé)).
- **C8-7** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 18 (non scellé)).
- **C8-8** : **remplace (N-062)** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 32 (non scellé : « échouée → reconception … H8 devient un diagnostic »)).
- **C8-9** : **dérisque** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 28-29 (non scellé)).
- **H1a** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **H1b** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **H2** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **H5** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **H6** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **H7** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **H9** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **HC1** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **HC2** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **HC3** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **HC4** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **HC5** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).
- **HC6** : **instrumente** (`docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 16-22 (non scellé : énoncés exacts et probabilités du programme, réécrits pour le jury)).

### A27 — Pince boîte blanche / boîte noire (étage III : aucune course dédiée avant la question v2)

- **H1a** : **dérisque** (`docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 15 (2dbad4b7 : « l'étau » — pour tromper la mâchoire externe, l'agent doit dissimuler davantage et cet effort se voit à la mâchoire interne), l. 21 (« l'étau de la pince mesuré » : absent du dépôt) ; `docs/notes/taif-v1/proposition-recherche-programme-v1-brouillon1.md` l. 22 (non scellé : pas encore dans un préenregistrement) ; `registres/go.md` l. 279 (GO-2026-11-08-07, première ligne de GO qui nomme la pince)).
- **HC5** : **dérisque** (`docs/decisions/decision-N-013-v1.md` l. 58-61 (157d388e : quorum hétérogène en type d'accès, juges et sondes) ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 15 (2dbad4b7)).

### A28 — Axe H5 — diversité des moniteurs (question v2 du pilier attaque ; aucune course)

- **C8-9** : **dérisque** (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 224 (H5 au papier B, scénario ambitieux) ; `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 17).
- **H5** : **instrumente** (`docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md` l. 17 (2dbad4b7 : H5 retenue, instrument = matrice de transfert), l. 21 (« matrice de transfert mesurée sur nos sondes et nos organismes : absente du dépôt ») ; `docs/decisions/decision-N-013-v1.md` l. 84 (157d388e)).
- **HC5** : **dérisque** (`docs/decisions/decision-N-013-v1.md` l. 61 (157d388e : la matrice de transfert entre juges et sondes est l'instrument commun à H5 et à HC5)).

### A29 — Axe collusion (niveau 2 de l'état de l'art, 28 oct. ; lecture Redwood Research, 8 nov. ; H9)

- **G0-8** : **teste** (`docs/notes/etat-art-niveau2/etat-art-niveau2-collusion-agents-v1.md` l. 1-8, 64-81 (7547040e) ; `registres/decisions.md` l. 832 (R-606)).
- **C8-9** : **dérisque** (`docs/notes/etat-art-niveau2/etat-art-niveau2-collusion-agents-v1.md` l. 81 (7547040e) ; `registres/decisions.md` l. 1776 (R-1818 : billet de Redwood Research, contre-mesures de niveau protocole, aucun résultat empirique)).
- **H5** : **dérisque** (`registres/decisions.md` l. 1776 (R-1818 : « moniteur d'un autre modèle ou entraîné à part » parmi les contre-mesures listées — diversité des moniteurs)).
- **H9** : **dérisque** (`docs/decisions/decision-N-035-v1.md` l. 16, 22-26 (55df073d : hypothèse ajoutée sous réserve d'antériorité ; aucune recherche affirmative faite)).

## 4. Orphelins

### 4.1 Côté activités — sans lien à aucune promesse ni hypothèse : « à justifier ou à garer » (4)

- **A13** Collisionneur « pôle scientifique automatique » (26 oct.) et premier lancement réel du pôle (27 oct.) — sans lien (`registres/decisions.md` l. 748-749 (R-524, R-525) ; `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md` l. 1 (4d6ddf40) ; `registres/go.md` l. 87 (GO-2026-10-27-05)) : à justifier comme infrastructure ou comme front E « pôle scientifique automatique » (absent de la candidature : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1172), ou à garer jusqu'après l'entretien.
- **A14** Collisionneur « recombinaison bisociative » (26-27 oct.) — sans lien (`registres/decisions.md` l. 750-751 (R-526, R-527), 790 (R-566) ; `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v2.md` l. 1 (8c3f15d7)) : à justifier comme infrastructure ou comme front E « pôle scientifique automatique » (absent de la candidature : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1172), ou à garer jusqu'après l'entretien.
- **A16** Organisme d'idéation — pilotes (24-26 oct.) — sans lien (`registres/go.md` l. 56-71 (GO-2026-10-25-01, GO-2026-10-25-02) ; `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 773 (≈ 156 USD), l. 1172 (« absent » de la candidature) (186173d9)) : à justifier comme infrastructure ou comme front E « pôle scientifique automatique » (absent de la candidature : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1172), ou à garer jusqu'après l'entretien.
- **A19** Garde refus-question v1 / v2 (8 nov.) — sans lien (`src/controle_ia/garde_refus_question_v1.py` l. 1-7 ; `src/controle_ia/garde_refus_question_v2.py` l. 1-10 ; `registres/decisions.md` l. 1746 (R-1788), 1779 (R-1821)) : à justifier comme infrastructure ou comme front E « pôle scientifique automatique » (absent de la candidature : `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` l. 1172), ou à garer jusqu'après l'entretien.

### 4.2 Côté promesses et hypothèses — qu'aucune activité ne sert : « à replanifier ou à renégocier » (1 strictes ; 2 servies seulement par des pièces documentaires)

- **C6-5** (« Code, with tests … In total, 602 automated tests »…) — aucune case hors `<<À VÉRIFIER>>` (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 279-281 ; `livrables/registres-taif-v4/promis-livre-v3.md` l. 21) : à replanifier (période à venir) ou à renégocier.
- **H1b** (interaction flou contre net, mesurée et rapportée comme information…) — servie seulement par l'audit documentaire du 26 octobre (A12) et par la proposition de recherche (A26), aucune mesure ni instrument depuis le 7 octobre (N-055 l. 34-36 (371879d5)) : à replanifier ou à renégocier.
- **H6** (marge asymétrique : trois interventions non spécifiques (paraphrase, ré-échantillonnage, r…) — servie seulement par l'audit documentaire du 26 octobre (A12) et par la proposition de recherche (A26), aucune mesure ni instrument depuis le 7 octobre (`docs/programme-controle-ia-v2.md` l. 97 ; N-013 l. 78 ; N-015 l. 15-18 (462785b3) ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` l. 152) : à replanifier ou à renégocier.

## 5. Comptes rendus au lecteur

- Lignes : 44 (31 promesses, 13 hypothèses) ; colonnes : 29 ; cases : 1276 ; renseignées : 173 ; `<<À VÉRIFIER>>` : 4 ; orphelins côté activités : 4 ; orphelins côté promesses : 1 strictes + 2 documentaires.
- Ce brouillon 2 est une lecture de l'arbre au 8 novembre 2026 (après 15:17 UTC) ; il ne décide rien, ne recommande rien, ne modifie aucun énoncé. Les mots des cases sont des jugements de ce lecteur, à contre-lire (R2) avant usage devant le jury.

Fin d'écriture (`date -u`) : Sun Nov  8 15:19:45 UTC 2026
