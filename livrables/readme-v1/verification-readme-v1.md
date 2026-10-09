# Vérification factuelle du README — v1

Date : 2026-10-07 (UTC). Relecteur neuf : je n'ai écrit ni `README.md` ni les documents du programme.
Objet : `README.md` (sha256 `6f009320…`, identique au contenu du commit `57a416c`, fait pendant ma lecture) et sa table `livrables/readme-v1/tracabilite-readme-v1.md` (`1625732c…`).
Public visé : recruteurs ; équipe de BlueDot Impact (bourse de reconversion vers la sûreté de l'IA).

## Verdict

**Publiable après corrections** (puis remplissage des TO COMPLETE). 0 bloquante, 7 majeures, 14 mineures, 3 suggestions.

Les chiffres sont exacts à leurs sources : 31 sur 31 ; 342 et 544 ; 0,21 à 0,35 ; 98 ; 24 ; 3 497 ; 0 échec ; 147 ; 18 ; 96 = 64 + 32 ; 1 192 ; 644 tests en 917 s ; environ 20 dollars ; 8 pages ; 120 dialogues. La citation de la page 2 est exacte au mot près. Tous les chemins cités existent. Aucun jeton ni aucune clé ne figure dans les fichiers suivis.

Les défauts sont des omissions et des formulations :
- la réserve de la simulation a disparu ;
- l'histoire de la validation du harnais est adoucie ;
- le rôle des agents est incomplet : la rédaction est omise, ainsi que les défauts appliqués sous 48 heures ;
- « independent » désigne des relecteurs qui sont des agents ;
- « the funded plan » laisse croire à un financement acquis ;
- deux questions de diffusion, que seul Lazar peut trancher : une proposition marquée confidentielle pour un autre destinataire, et des PDF et textes de tiers dans le dépôt.

## Remarques

### K-1 — majeure — Simulation : la réserve a disparu (l. 16 et l. 49)
- **Problème.** Le README écrit « 31 of 31 predictions confirmed » sans la réserve que la source met en tête et que la proposition relue a gardée. Un lecteur y lit une confirmation de la théorie. C'est une vérification des instruments. Le README tait aussi un acquis plus parlant : la simulation a réfuté la formulation d'origine du programme.
- **Preuve.**
  - `docs/notes/resultats-T0.3-v1.md` l. 41-46 : « la plupart des prédictions sont des vérifications de l'instrument » ; « Elle ne prouve ni le lemme ni le théorème sur des activations réelles ».
  - Même fichier, l. 115 : « L4 (répartition entre agents au même pas) n'est pas testé ». L. 78 : « le théorème du programme est faux tel qu'écrit ». L. 126 : « réfute les formulations littérales du programme dans les cas annoncés ».
  - `registres/etat.md` l. 14 : « Réserve : … ce n'est pas une preuve sur modèles réels ».
  - `livrables/candidature-ea-funds-v1/proposal-v1.md` l. 26 et l. 69.
- **Correction, l. 16 :** « A pre-registered simulation of the theory: 31 of 31 predictions confirmed. As expected, these check the statistical instruments; they are not yet evidence on real models. »
- **Correction, l. 49 (cellule) :** « Pre-registered. 31 of 31 predictions confirmed (342 statistical and 544 path-level checks, none contrary). As expected, most were checks of the instruments: they validate the statistics, not the claims on real activations, and one part of the lemma (splitting across agents within a step) remains untested. The simulation also refuted the programme's original wording of the lemma and of the theorem in the cases it predicted; the corrected statements are in the mathematical note. It also showed that a textbook threshold fails outside its assumptions: false alarms of 0.21 to 0.35 instead of 0.05 under episode effects. Thresholds are therefore calibrated on whole honest episodes. `docs/notes/resultats-T0.3-v1.md` »

### K-2 — majeure — Harnais : « a partial second one » adoucit un échec, et le critère a changé (l. 50)
- **Problème.**
  - La version 2 n'est pas « partielle » au sens courant. Son verdict est « non prouvé », car la garde de production est contraire (0,52 > 0,1).
  - La version 3 a remplacé cette garde : 99e centile au lieu du maximum, seuil de 0,2 fondé sur le repère de précision. Lazar l'a décidé et la version 3 est préenregistrée.
  - Mais les valeurs de la version 2 étaient connues quand le seuil a été fixé, et la version 2 l'aurait passé.
  - Tout est déclaré dans le préenregistrement v3, et le README invite à lire le verdict qui l'applique. Un lecteur expert qui découvre là ce changement jugera le mot « partial » enjolivé, dans un texte qui met en avant le préenregistrement.
- **Preuve.**
  - `registres/etat.md` l. 15 : « v2 … production au-dessus du seuil sur le maximum, pas de run B : non prouvé ».
  - `registres/decisions.md` l. 275 (N-011) : « P4 contraire (demi-précision : 0,522 > 0,1) … critère 1 de G0 non prouvé » ; « Le seuil de 0,1 sur le maximum ne tient pas en demi-précision (queue longue, jusqu'à 0,79 dans le repère) ».
  - `prereg/T0.4-validation-modele-reel-v3.md` l. 6 et l. 42 ; l. 136 : « la production de la v2 aurait été conforme » ; l. 360 : « Ces valeurs de la production étaient connues quand le seuil de 0,2 a été proposé (N-011) ».
  - `registres/go.md`, GO-2026-10-06-01.
- **Correction (dernière phrase de la cellule) :** « Reached at the third pre-registered version. The first was inconclusive. The second validated the logic but failed its production check: a threshold on the maximum deviation, which half-precision rounding alone exceeds. The third replaced that check with a threshold on the 99th percentile, derived from a measured precision benchmark; the second version's values were known when it was set, and the pre-registration says so. »

### K-3 — mineure — Harnais : domaine de validité, revalidation, « higher-precision reference path » (l. 17 et l. 50)
- **Problème.**
  - (a) Le README a perdu deux mentions que la proposition garde : « within a stated domain », et la revalidation courte avant le pilote. Or le pilote changera de carte et de longueur de contexte. De plus, « contexts up to 1,192 tokens » est le maximum de la production ; le contrôle strict s'arrête à 1 087 jetons.
  - (b) « agreement with a higher-precision reference path » décrit mal ce qui a été vérifié. Les activations capturées pendant la génération sont comparées à une passe avant séparée, dans trois précisions (double, simple, demi). L'écart de la production est ensuite rapporté à un repère qui compare la demi-précision à la double précision. La lecture naturelle de la phrase anglaise, « la production comparée à un calcul de référence plus précis », est fausse.
- **Preuve.**
  - Verdict v3 l. 18 et l. 432 : « sur cette carte, ce pilote, ces bibliothèques et ce noyau. Hors de ce domaine, il faut revalider ».
  - `registres/etat.md` l. 15 (domaine consigné, R-052) et l. 33 (P-007 : revalidation courte avant le pilote).
  - Préenregistrement v3 l. 63-67 : H-logique, H-chemin, H-production comparent la génération à la passe unique ; le repère situe la production.
  - `proposal-v1.md` l. 191.
- **Correction, l. 17 :** « An activation-logging harness, validated on Llama-3.1-8B-Instruct on a rented GPU, within a stated domain. »
- **Correction, l. 50 (début de cellule) :** « Llama-3.1-8B-Instruct on a rented H200 GPU, within a stated domain: this GPU, software stack and attention kernel; contexts up to 1,087 tokens for the strict check, 1,192 in production. Bit-identical replay across processes; activations logged during generation match a separate forward pass within rounding error, in double, single and half precision; an injected defect is detected; guards are tested. A short revalidation on the pilot's domain comes before the pilot. »

### K-4 — majeure — « independent reviewer », « independent readers » : ce sont des agents (l. 23-24, l. 48, l. 60)
- **Problème.**
  - Beaucoup de lecteurs ne liront que « In one minute ». Là, « An independent reviewer counter-reads each pre-registration » se lit comme un relecteur humain.
  - Ce relecteur est un sous-agent neuf, de la même famille de modèles que l'auteur. Le README ne le dit que cinquante lignes plus bas.
  - Même ambiguïté pour « 24 reports by independent readers ».
- **Preuve.** `CLAUDE.md`, R2 et R13 (« sous-agent neuf ») ; synthèse du niveau 2 l. 11 (« 24 rapports de lecteurs neufs ») ; README l. 78 et l. 80.
- **Correction, l. 23 :** « A fresh AI reviewer (a new agent instance that did not write it) reviews each pre-registration. »
- **Correction, l. 24 :** « Another fresh AI reviewer, who wrote neither the plan nor the analysis, applies the frozen criteria; I sign off. »
- **Correction, l. 48 :** « 24 reports by fresh AI reader agents. »
- **Correction, l. 60 :** « **Independent review.** A fresh AI reviewer (an agent instance that did not write the document) reviews it. Gate verdicts are issued by another fresh agent that wrote neither the plan nor the analysis, then submitted to me for sign-off. »

### K-5 — majeure — « Who does what » : la rédaction est omise, « every decision » et le registre sont inexacts (l. 78-80)
- **Problème.**
  1. La liste des tâches des agents omet la rédaction : la note mathématique et ses preuves, les préenregistrements, les analyses, la proposition de projet, et ce README lui-même. Écrit à la première personne, le texte laisse croire que Lazar les a écrits.
  2. « I take every decision » est inexact. Les règles donnent aux agents les décisions de routine (code, bibliothèques, tests, lectures, fichiers). Elles font aussi prendre leur défaut aux propositions restées sans réponse 48 heures. Huit l'ont fait le 6 octobre : moniteur boîte noire, panel de juges, grille du nombre d'agents, familles d'organismes, entre autres.
  3. « My decisions are logged … in `registres/decisions.md` » est inexact. Ce registre consigne surtout les décisions de routine des agents (R-001 à R-102). Les GO de Lazar sont dans `registres/go.md`.
  4. Les 240 commits du dépôt sont signés « Claude » (232) ou par l'instance de calcul (8). Un lecteur qui ouvre l'historique le verra ; mieux vaut le dire.
  5. En contrepartie, le README tait un apport scientifique propre de Lazar, qui compte pour ce public. Sa contre-lecture du verdict sur la loi de déférence a fixé la pièce revendiquée du papier C : la destination libre ĉ.
- **Preuve.**
  - `CLAUDE.md` l. 49-52 (hiérarchie de décision).
  - `registres/decisions.md` l. 3 (« Routine : décidée et consignée ici ») ; l. 245-249 et l. 251-253 : « défaut appliqué le 2026-10-06 08:47 UTC (sans réponse sous 48 heures) » pour P-001, D1, D2, D3 et P-002 à P-005. Voir aussi `registres/etat.md` l. 39.
  - `registres/go.md` l. 3 : « Seul Lazar accorde un GO ».
  - Brief l. 144 (la note mathématique est un livrable de la session) ; note v3 l. 3 (« session 10 ») ; `registres/decisions.md` R-096 et R-097 (candidature et proposition « rédigés par la session ») ; commit `57a416c` (README).
  - `git log --format='%an' | sort | uniq -c`.
  - `registres/decisions.md` l. 27 (R-018) ; `docs/decisions/decision-N-005-N-006-v1.md` l. 20 : « précisée par le point 6 de la contre-lecture de Lazar : … La destination ĉ est donc estimée librement, puis testée ».
- **Correction (remplace l. 78-80 ; garder l. 82) :**
  « I designed the programme: its questions, hypotheses, papers and gates. The work in this repository is done by AI agents (Claude Code) under the written rules above: code, runs, literature checks, the mathematical note and its proofs, pre-registrations, analyses, internal reviews, and the drafting of documents, including this README. Every commit is theirs. One example of my own scientific input: my review of their literature verdict on the deference law set the claimed piece of Paper C, a destination estimated freely rather than imposed (`docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md`, decision N-005).

  The rules split decisions three ways. The agents take routine engineering decisions and log them. Design choices are proposed to me with a recommendation, and take their default if I have not answered within 48 hours; eight did so on 6 October. Gates, compute spending, changes of hypothesis or claim, and any external contact wait for my explicit approval. Decisions are logged with their dates in `registres/decisions.md`, my approvals in `registres/go.md`, and every working session ends with a sealed hand-over note in `registres/passations/`. »
  (Lazar doit confirmer l'exemple de son apport. Ajouter « eight did so on 6 October » à la table de traçabilité, avec la source `registres/decisions.md` l. 245-253.)

### K-6 — majeure — « The funded plan » (l. 80)
- **Problème.** Rien n'est financé. De plus, la validation humaine payée n'existe que dans les scénarios central et ambitieux, pas dans le minimal. Pour un jury de bourse, « funded plan » se lit « plan déjà financé ».
- **Preuve.** `proposal-v1.md` l. 183 (« The mainline and ambitious budgets therefore include… ») et l. 270 (scénario minimal : « — ») ; `registres/etat.md` l. 45 (candidature encore à soumettre par Lazar).
- **Correction :** « The reviewer agents share a model family, so their errors may be correlated. The plan I am seeking funding for therefore budgets paid human expert validation of the ground truth (in its mainline and ambitious versions). »

### K-7 — majeure — Parcours de lecture : une proposition confidentielle, destinée à un autre fonds (l. 87)
- **Problème.**
  - Le PDF porte la mention « Confidential: unpublished research plan, please do not circulate beyond the fund team and its advisors ».
  - Il affiche la demande à EA Funds : 91 740 dollars, dont 60 000 de rémunération du demandeur.
  - Il garde ses champs à compléter : « [SURNAME] », « [position] », « [to confirm] ».
  - Le montrer à des recruteurs contredit sa propre mention.
  - Le montrer à BlueDot révèle une demande concurrente. BlueDot doit sans doute la connaître, mais c'est à Lazar de choisir comment : formulaire ou README.
- **Preuve.** `proposal-v1.md` l. 11, 14, 16 et 265 ; page 1 du PDF (`pdftotext`, empreinte `35226dfd…` conforme) ; `registres/etat.md` l. 45.
- **Correction.** Décision de Lazar. Options :
  - (a) une version de la proposition destinée à ce public (sans la section budget ni la mention de confidentialité, champs remplis), seule citée par le README ;
  - (b) garder ce PDF, en réécrivant la mention ;
  - (c) pour les recruteurs, remplacer l'entrée 2 par : « 2. The project proposal, in English (8 pages): available on request. »
  - Recommandation : (a), confiance moyenne.

### K-8 — majeure — Donner accès au dépôt, c'est partager des textes de tiers (l. 107)
- **Problème.**
  - Le dépôt suit 119 PDF d'arXiv (`docs/sources/pdf/`). Il accueille aussi, par ajout forcé, les sorties de l'extraction, qui portent du texte des papiers.
  - La règle de sélection excluait ces textes du dépôt, pour cause de licences variées. N-014 les y admet « dans le dépôt privé seulement ».
  - Ouvrir le dépôt à des recruteurs ou à BlueDot, c'est redistribuer ces textes.
  - La l. 107 ne parle que des sorties de l'extraction, pas des PDF.
- **Preuve.**
  - `git ls-files docs/sources/pdf | grep -c '\.pdf$'` : 119.
  - `.gitignore` l. 7 (`donnees/`).
  - `registres/decisions.md` l. 278 (N-014 : « que la section 9 de la règle de sélection scellée exclut du dépôt (licences variées) ») et l. 232 (R-095).
  - `registres/etat.md` l. 27.
- **Correction.** Décision de Lazar, proche du nœud « publication ». Options :
  - (a) partager une copie expurgée : branche ou paquet git sans les PDF ni les sorties de l'extraction, en gardant les empreintes et les liens arXiv ;
  - (b) partager tel quel, en connaissance de cause ;
  - (c) ne montrer que le README.
  - Recommandation : (a).
  - Texte de la l. 107 en cas (b) : « This private repository holds copies of third-party arXiv PDFs (`docs/sources/pdf/`) and extraction outputs that contain text derived from those papers (`donnees/`). They are kept for verification only, are not redistributable, and will be removed before any publication. Please do not copy them. »
  - Texte en cas (a) : « This copy omits the third-party PDFs and the outputs derived from them; their SHA-256 hashes remain in `docs/sources/pdf/`. »

### K-9 — mineure — Terekhov et al. (l. 29)
- **Problème.**
  - (a) « The paper that introduced a control setting for this threat » suggère une primauté que le papier ne revendique pas : il cite des travaux antérieurs sur les menaces diffuses (Hebbar 2025 ; Gasteiger et al. 2025).
  - (b) « studies training-based mitigations » : le papier s'y « concentre », mais n'entraîne aucun modèle ; il optimise des invites.
  - (c) La citation retire deux renvois bibliographiques entre crochets, sans le signaler.
- **Preuve.**
  - PDF `docs/sources/pdf/2606.08892v2.pdf` (`aea0f2d1…`, compagnon conforme), page 2 : « We focus on training mitigations, since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. We also sidestep the question of how models generalize from training by focusing on prompt optimization ».
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` l. 110 : « l'entraînement est une hypothèse de modélisation, jamais exécuté ».
- **Correction :** « A recent paper that sets up a control framework for this threat on fuzzy research tasks (Terekhov et al., arXiv 2606.08892) focuses on training-based mitigations, because monitoring and incrimination "seem theoretically and empirically less promising for mitigating diffuse threats" (p. 2, citations omitted). »

### K-10 — mineure — État de l'art : « 147 correction lines », « 0 failures », « Level 2 », « fully occupied » (l. 18, l. 48)
- **Problème.**
  - Sur les 147 lignes, 80 sont corrigées, 11 renvoient à des chiffres introuvables et 56 sont confirmées avec réserve.
  - « 0 échec » vaut au passage final seulement.
  - « Level 2 » est un terme interne.
  - « occupied » est un calque du français.
- **Preuve.** Synthèse du niveau 2 : l. 16 (« 0 échec au passage final ») ; l. 30 ; l. 58 ; l. 76 (« 147 lignes … (80 corrigées, 11 introuvables, 56 confirmées avec réserve) »).
- **Correction, l. 18 :** « A literature check on primary sources: 98 arXiv PDFs, 3,497 quotations checked by script against the page text, 0 failures at the final pass. »
- **Correction, l. 48, statut :** « Second pass done ».
- **Correction, l. 48, cellule :** « 98 arXiv PDFs retrieved and hashed. 24 reports by fresh AI reader agents. 3,497 quotations checked by script against the page text, 0 failures at the final pass. 147 lines of our own documents flagged: 80 corrected, 11 figures not found in the sources, 56 confirmed with a caveat. No claimed contribution was found already published in full; several claims were narrowed. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` »

### K-11 — mineure — Théorie : les classes C et K sont mal séparées (l. 39-40)
- **Problème.**
  - « attacks that preserve the distribution of individual scores » décrit aussi la classe K, qui garde la loi de chaque score. La phrase oppose donc K à K.
  - « does sabotage shift the distribution of probe scores at all? » est trop large : une attaque de classe K change la loi jointe des scores. La question pivot porte sur la loi de chaque score, sa marginale.
- **Preuve.** `proposal-v1.md` l. 65 (« Preserving the multiset (class C) differs from preserving each coordinate's marginal while changing the dependence (class K) ») et l. 71 (« shift the marginal of probe scores (δ > 0) »).
- **Correction, l. 39 (seconde phrase) :** « It also separates attacks that only reorder the scores from attacks that keep each score's distribution but change how the scores depend on one another. »
- **Correction, l. 40 :** « **The pivotal empirical question:** on realistic model organisms, does sabotage shift the distribution of each probe score at all? If it does, sequential accumulation should work. If it does not, the theorem dictates the aggregator, or says when monitoring based on per-score distributions must fail. »

### K-12 — mineure — « a negative theorem … says which aggregation must fail » (l. 31)
- **Problème.** Le théorème couvre les attaques qui gardent la loi de chaque score. Si l'échec vient d'une absence de signal interne, c'est l'analyse de validité de construit qui dit où ne pas se fier aux sondes. La proposition associe les deux.
- **Preuve.** `proposal-v1.md` l. 233 et l. 246.
- **Correction :** « If it does not, the negative theorem and an analysis of what the probes really measure say where probe-based monitoring should not be trusted, and why. That is useful for safety cases either way. »

### K-13 — mineure — Bases et sondes : « lite » et « provisoire » ont disparu (l. 52)
- **Problème.**
  - Le code est TRACE-lite, pas une réimplémentation de TRACE : le contrôleur adaptatif est retiré, et le calendrier d'inspection est fixe, d'au plus 18 appels.
  - Le plancher apparié en covariance suit une recette provisoire.
  - `sondes/` et `bases/` ne sont pas des chemins valides depuis la racine du dépôt.
- **Preuve.** `src/controle_ia/bases/trace_lite.py` l. 1-12 (« le contrôleur B2 est retiré, d'où le « lite » ») ; `registres/etat.md` l. 18 (« recette provisoire, à confronter au code de P3 ») et l. 19 ; `proposal-v1.md` l. 99 ; test de la dose 0 : `tests/test_organismes_lora.py` l. 44.
- **Correction :** « Low-rank adapters with an adjustable dose (tested: dose 0 reproduces the base model bit for bit). Five probe families with a covariance-matched random floor (provisional recipe). TRACE-lite, a simplified reimplementation of the TRACE monitor (arXiv 2606.07054) with a fixed inspection schedule. `src/controle_ia/organismes/`, `src/controle_ia/sondes/`, `src/controle_ia/bases/` »

### K-14 — mineure — L'exemple du pilote (l. 68-74)
- **Problème.**
  - Le préenregistrement du pilote est encore un brouillon (le septième), pas un document scellé.
  - La faille a été trouvée par deux relectures indépendantes : celle du pilote (Y-1) et celle de la revalidation (X-1). Le dire est plus fort.
  - « counter-readings » et « differential re-reads » sont des calques.
- **Preuve.**
  - `registres/etat.md` l. 16 (« Reste avant scellement »).
  - `registres/decisions.md` l. 238 (R-101 : « Majeure commune (X-1, Y-1) »).
  - Rapport `prereg/contre-lectures/T0.5-pilote-rapport-relecture-differentiel-b5-v1.md` (`43f0df46…`), Y-1 : « après la mise en place payée » ; « Le seul relancement permis est donc impossible ».
  - Brouillon 7, section « Contre-lecture », l. 244-251.
  - `tests/test_script_instance_t05.py` l. 22, l. 101-102 et l. 230.
- **Correction :** « **An example of what the review catches.** The draft pre-registration of the environment pilot (not yet sealed) has so far gone through two full reviews, a short verification and two reviews of the later changes. Two of those reviews, of this pilot and of a related revalidation, independently found that the tests of the GPU instance script inherited the instance's environment variables. The only relaunch the procedure allows would then have failed its own test suite, after the paid setup. The fix and a regression test are in `tests/test_script_instance_t05.py`; the reports are in `prereg/contre-lectures/`. »

### K-15 — mineure — Date du démarrage (l. 5)
- **Problème.** La phase 0 court officiellement à partir du 5 octobre, mais le travail du dépôt commence le 4 : brief v2, R-001, run de simulation du 4 à 08:02. Un lecteur des registres verra des dates antérieures au « début ».
- **Preuve.** `CLAUDE.md` (« M0 : 5 octobre → 1er novembre 2026 ») ; `docs/notes/resultats-T0.3-v1.md` l. 3 (« Date : 2026-10-04 ») ; `registres/decisions.md` R-001.
- **Correction :** « **Status, 7 October 2026.** Phase 0 (building and validating the instruments) runs from 5 October to the first decision gate, G0, on 1 November 2026; work in this repository started on 4 October. This repository is private. Its working documents are in French; this README is the English entry point. »

### K-16 — mineure — Chiffres qui bougent : dépenses et tests (l. 20, l. 53, l. 114)
- **Problème.**
  - « About $20 spent so far » vieillit vite. Plus de la moitié est le stockage des six instances arrêtées et gardées : environ 0,30 dollar de l'heure, soit 7,3 dollars par jour, jusqu'au geste de Lazar sur N-012.
  - Le nombre de tests diffère de celui de la proposition jointe (602). Un lecteur des deux documents verra l'écart.
- **Preuve.** `registres/depenses.md` l. 42-44 (« Cumul de la phase 0 ≈ 12,3 USD (marche ≈ 5,1, disques ≈ 7,2) ») ; `registres/etat.md` l. 48 ; message du commit `a0d8777` (« 644 tests réussis (917 s) ») ; `tracabilite-proposal-v1.md` l. 19 (602).
- **Correction, l. 53 :** « About $20 as of 7 October 2026: about $5 of GPU time, the rest storage of stopped instances kept for audit. »
- **Correction, l. 20 :** « 644 automated tests (7 October 2026). »

### K-17 — mineure — Pied de page (l. 148)
- **Problème.** `livrables/readme-v1/` ne contient que `tracabilite-readme-v1.md`, sans compagnon `.sha256`. La copie scellée `README-v1.md`, annoncée à la l. 3 de la table, n'existe pas encore, ni aucun rapport de vérification. La phrase est fausse tant que ce n'est pas fait.
- **Preuve.** `ls livrables/readme-v1/` ; table de traçabilité l. 3 ; message du commit `57a416c` (« La version vérifiée remplacera ce brouillon, avec sa copie scellée »).
- **Correction.** Déposer la copie scellée et ce rapport avant de montrer le README, puis écrire : « *README version 1, 7 October 2026. Every figure is traced to its source in `livrables/readme-v1/` (traceability table, fact-check report and sealed copy, in French).* »

### K-18 — mineure — Anglais : calques et jargon interne (l. 23, 33, 48-49, 51, 59-62, 70-72)
- « counter-reads » et « counter-readings » → « reviews ».
- « differential re-reads » → « reviews of the later changes ».
- « fully occupied » → « already published in full ».
- « 0 contrary » → « none contrary ».
- « pronounced » → « issued ».
- « a signed numeric prediction », qui se lit « signée » → « a numeric prediction with its expected sign ».
- « No run aims at a positive sign » → « No run is designed to produce a positive result ».
- « on a healthy case and on an artefact » → « on a sound case and on a deliberately broken one ».
- « path-level cells » → « path-level checks ».
- « episode effects » → « an effect shared by all steps of an episode ».
- l. 33 : « shows control monitors swayed … or adopting » → « shows control monitors being swayed … and adopting ».
- Orthographe : « optimized » (l. 33) détonne dans un anglais britannique (« programme », « artefact ») → « optimised ».
- **Preuve.** Lecture du texte ; sens des règles : `CLAUDE.md` R1, R3 et R5.

### K-19 — mineure — Ordre des sections et parcours de lecture (l. 76-90, l. 134-144)
- **Problème.**
  - Pour un jury de reconversion et des recruteurs, la personne et le partage du travail viennent trop tard : « About me » est en dernier, « Who does what » vient après les règles.
  - Le parcours « about 15 minutes » est irréaliste : un verdict de 456 lignes en français, de longs registres en français, une proposition de 8 pages.
  - Les puces « How. » de « In one minute » répètent la section « How the work is done ».
- **Preuve.** `wc -l` du verdict : 456 lignes ; README l. 84-90.
- **Correction de l'ordre :** In one minute → Who does what → About me → Why it matters → Progress so far → How the work is done → Theory → Roadmap → Suggested reading path → Repository map → Reproduce.
- **Correction du parcours :** « ## Suggested reading path (about 30 minutes) 1. This README. 2. The project proposal, in English (8 pages) [selon K-7]. 3. A sample of the method, in French: section 1 of the verdict `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` (lines 9–21), the pre-registration it applies, `prereg/T0.4-validation-modele-reel-v3.md`, and its reviews in `prereg/contre-lectures/`. 4. The decision log and my approvals: `registres/decisions.md`, `registres/go.md` [voir K-20]. »

### K-20 — mineure — Les registres cités contiennent plus que le programme (l. 80, l. 90)
- **Problème.**
  - `registres/etat.md` et `registres/depenses.md` mentionnent des instances de calcul hors du programme sur le compte de Lazar, avec leurs étiquettes.
  - `etat.md` mentionne aussi le refus d'un lancement par le classificateur du mode automatique, ainsi que la candidature EA Funds et ses montants.
  - Les registres citent les messages de Lazar mot pour mot.
  - Rien de secret, mais il faut relire ces registres avant d'y envoyer un recruteur.
  - Aucun jeton ni aucune clé dans les fichiers suivis. Recherche par motifs (Hugging Face, GitHub, clés d'API, clés privées), hors `donnees/` et `diag/*t05-extraction*`.
- **Preuve.** `registres/etat.md` l. 3, 16, 44-45 et 51-53 ; `registres/depenses.md` l. 44.
- **Correction.** Décision de Lazar. Au minimum, citer ces registres « on request » dans le parcours de lecture.

### K-21 — mineure — Table de traçabilité (document interne)
- (a) L. 12 : le verdict v3 ne nomme pas Llama-3.1-8B-Instruct (`grep` : aucune occurrence). Sources : préenregistrement v3 l. 27, ou `registres/etat.md` l. 15.
- (b) L. 20 : trois énoncés sur P3 viennent du brief l. 40 et l. 170, pas de la seule l. 150 : « pre-registered », « covariance-matched controls », « construct validity of sycophancy in Llama-3.1-8B-Instruct ».
- (c) L. 3 : la table annonce une copie scellée `README-v1.md`, encore absente.
- (d) Lignes à ajouter si les corrections sont retenues :
  - « eight did so on 6 October » : `registres/decisions.md` l. 245-253 ;
  - « within a stated domain » et la revalidation : `registres/etat.md` l. 15 et l. 33 ;
  - « 1,087 » : verdict v3 l. 18 ;
  - « 80 / 11 / 56 » : synthèse du niveau 2 l. 76 ;
  - « at the final pass » : synthèse du niveau 2 l. 16 ;
  - « TRACE-lite » : `trace_lite.py` l. 1-12 ;
  - « provisional » : `registres/etat.md` l. 18 ;
  - partage des dépenses : `registres/depenses.md` l. 43 ;
  - réfutation de la formulation d'origine : résultats T0.3 l. 126 ;
  - apport de Lazar : `decision-N-005-N-006-v1.md` l. 20.

### K-22 — suggestion — Champs à compléter et « About me » (l. 136-144)
- Les « [TO COMPLETE] » sont bien signalés : l. 136 (deux fois), l. 138 et l. 144. Seul « [SURNAME] » n'a pas le marqueur.
- Uniformiser (« [TO COMPLETE: surname] ») et contrôler avant envoi : `grep -n "TO COMPLETE\|SURNAME" README.md`. Faire le même contrôle sur le PDF de la proposition s'il reste au parcours : « [SURNAME] », « [position] », « [to confirm] ».
- « P3 » n'est pas expliqué. Proposer : « My previous project (P3) studied… ».
- « treat deference, and corruptibility, as a gain rather than a thing » est opaque. Proposer : « measure deference, and corruptibility, as a continuous gain (how far a verdict moves toward the pressure) rather than as a yes-or-no trait ».
- Dire si P3 a aussi été mené avec des agents d'IA, par cohérence avec « Who does what ». La méthode héritée de P3 prévoit déjà une « contre-lecture par une instance qui ne l'a pas écrit » (programme, section 12, l. 229).

### K-23 — suggestion — « Reproduce » et « Roadmap » (l. 116, l. 119, l. 129-130)
- L. 119 parle de gouvernance interne à un lecteur extérieur. Proposer : « GPU runs need `requirements-gpu.txt`. In this repository, a hook (`.claude/hooks/garde_calcul.py`) refuses any paid instance launch that does not cite an approval recorded in `registres/go.md`. »
- L. 116 : `run_factice` écrit un nouveau run ; le dire : « writes a new run into `runs/` and `diag/` ».
- L. 129-130 : ancrer les mois et la condition de financement : « **Months 1–2 (November–December 2026, if funded).** … » ; « **Months 3–7 (January–May 2027).** … ».
- Je n'ai pas exécuté la suite de tests ni le run factice, car tous deux écrivent dans le dépôt.

### K-24 — suggestion — Ce que le README pourrait dire en plus
- Les brouillons de préenregistrement de G1 et du papier C existent : proposition l. 194 ; `brouillons/G1-preenregistrement-v1-brouillon3.md` ; état l. 20 (papier C, brouillon 2). Ajouter une ligne au tableau : « Pre-registrations for gate G1 and Paper C | Drafts, under review ».
- Pour ce public, les deux faits les plus utiles sont :
  - la réfutation, par la simulation, de la formulation d'origine du programme (K-1), qui montre que la méthode mord ;
  - l'apport de Lazar sur la loi de déférence (K-5), qui montre qui pense.
- Ajouter une mention de diffusion, en tête ou en pied : « Shared privately for evaluation; please do not redistribute. »

## Vérifié exact (sans remarque)
- **Simulation.**
  - 31 sur 31 ; 342 et 544 ; 0 contraire : résultats T0.3 l. 29-32.
  - 0,21 à 0,35 au lieu de 0,05 sous effet épisode : l. 97-102.
  - Calibrage sur épisodes honnêtes entiers : l. 107 et l. 127 ; état l. 19.
- **Harnais.**
  - Carte H200 NVL ; 1 192 jetons en production ; rejeu au bit près dans le processus et entre processus (P6, P7) ; défaut D1 vu ; gardes testées : verdict v3 l. 11, 18, 350 et 418.
  - Version 1 non concluante : état l. 15.
- **État de l'art.**
  - 98 PDF ; 24 rapports (4 + 12 + 8) ; 3 497 citations (561 + 1 726 + 1 210) : synthèse l. 7, 11 et 16.
  - Aucun énoncé revendiqué occupé en entier : l. 30.
- **Sources citées.**
  - Citation de Terekhov et al. : mots exacts, page 2 du PDF empreinté.
  - « ni code ni données » : rapport de niveau 1 sur 2606.08892, l. 12 et l. 123.
  - 2505.23575 : rapport lot 2 C1b, point 5. 2510.09462 : rapport lot 2 A4, point 6.
- **Environnement.**
  - 18 invites ; 96 papiers = 64 + 32.
  - Règle scellée (`8f43dcae…`) et tirage par graine : règle, section 6.
  - Procédure d'extraction scellée après trois contre-lectures et une vérification courte : procédure, l. 5-9.
- **Code.**
  - Dose 0 au bit près : `torch.equal` dans `tests/test_organismes_lora.py` l. 44.
  - Cinq familles de sondes : `src/controle_ia/sondes/familles.py`.
- **Dépenses.**
  - Environ 20 dollars : ≈ 17,8 le 7 octobre à 07:40, état l. 48.
  - Chaque location du programme est consignée avec son GO. Plafond de 150 dollars, alerte à 120.
- **Tests et exemple du pilote.**
  - 644 tests réussis en 917 s : commit `a0d8777`.
  - Faille Y-1, correctif et test de non-régression `test_environnement_de_l_instance_sans_effet` ; « after the paid setup » : Y-1.
- **Feuille de route.** Critères restants de G0 : état l. 23. Calendrier et bascule de G1 : proposition, sections 4, 7 et 9 ; programme, section 13.
- **P3.** Brief l. 40, 150 et 170 ; programme l. 84 et l. 200.
- **Proposition.** 8 pages (`pdfinfo`) ; empreinte conforme à la table.
- **Chemins.**
  - Tous les chemins cités existent ; `sondes/` et `bases/` n'existent que sous `src/controle_ia/`.
  - `donnees/` est ignoré par git (`.gitignore` l. 7).
  - Compagnons `.sha256` conformes pour les onze documents scellés relus.

## Limites
- **Non lus**, selon la consigne : `donnees/`, `diag/*-t05-extraction*`.
- **Non exécutés** : la suite de tests, `verifier-arbre` et `run_factice`, qui écrivent dans le dépôt.
- **Aucun appel réseau.**
- **Commit pendant la lecture.** Le README a été commité pendant ma lecture (`57a416c`). Le contenu relu est identique : même empreinte.

## Empreintes sha256 des fichiers relus

```
6f009320329e70342b6ae9fb9df7faad8b060a211abad74a4f483eb9074eda12  README.md
1625732c4a6c0a58ce9fc486bedc757e6f6181a5df260cd9f10c3b3659cc5f8d  livrables/readme-v1/tracabilite-readme-v1.md
9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545  docs/notes/resultats-T0.3-v1.md
63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13  docs/verdicts/verdict-T0.4-critere-1-G0-v3.md
bbe0c1f523ad83e13e5ce96d19c384e8596a96d298431b931f499826c773ceb8  docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md
cbf6bd9ca6b074e70bae957c45d70fa338a578ee6081f958f9277418ec3902d2  registres/etat.md
f5dc9bc2834325bf88e37f94b00463507d9f4765174ed3bce3c020715a3db850  registres/depenses.md
a83bfc0a81a1ed0a6595276d1636b104817deee3e38ab9626f39cbc5f85636eb  registres/decisions.md
1cd03cf1a3eb920204785b02c28d5c18447c3477baa51f07c676fc8c1bcdd7fd  registres/go.md
9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2  docs/brief-claude-code-programme-complet-v2.md
2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c  docs/programme-controle-ia-v2.md
2f1e0864110f5f747347da40c9e9f89174119de5a3a14875b0371ae78c57e2c7  livrables/candidature-ea-funds-v1/proposal-v1.md
35226dfdf7bf1e36931a3b9ca9a056c5b69fce0a5e1b36b127d8eb883efccb36  livrables/candidature-ea-funds-v1/proposal-v1.pdf
3dfe04ec279ff5c4aa08a9f3879d292b9c910f25a59ac6e6e51db069cccea8ed  livrables/candidature-ea-funds-v1/tracabilite-proposal-v1.md
339e579989571bc890d6f64bb908df084e97f146cb67f4c915bc6248b94984c9  CLAUDE.md
07a6d8e5de4b6d87bc4f34d2d244ee8f044951de1d92c57f0d0b1da0a1e37728  brouillons/T0.5-pilote-8B-v1-brouillon7.md
aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a  docs/sources/pdf/2606.08892v2.pdf
4f711cd3a58182856c804e6652ec92c1aaab865fe9b595ea1d6be65757b8ed5f  prereg/T0.4-validation-modele-reel-v3.md
43f0df464806bd23f8f51ffab5d91714b85769b45d241fd11e3be9b5a238440a  prereg/contre-lectures/T0.5-pilote-rapport-relecture-differentiel-b5-v1.md
d23bd62fe1611b8737ccb38a404d96a41746158a7930bef0a065590bd072c26c  docs/procedures/T0.5-extraction-v1.md
8f43dcaeb5fd782c07fe4e0c9d093ed15d6bc09eb183a1fd9a3db589e5cac28b  docs/procedures/T0.5-selection-papiers-v1.md
dfe4fe0fc4d025011bbe0f330fd591b1898dc7e767384e96c946b6388ad81cd0  docs/notes/note-mathematique-lemme-theoreme-v3.md
86b3416297fe7d563702b34432d9aae8be774d3178d6da4230a0495d27e11c2e  tests/test_script_instance_t05.py
4bf4ef35a2c734d19e67f02235c6dc4302ff1b89fd1fccf23b800dae68373ea6  src/controle_ia/bases/trace_lite.py
6ee377ca7f35ec52c4e99f104908b89656d84888057b5509b28ff49fb58baf7c  .gitignore
072b567f35c112276d07dbc1e6d3c890d4b812f02248dbae32cecf4ae5b7a69d  tests/test_organismes_lora.py
6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e  src/controle_ia/sondes/familles.py
cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0  docs/decisions/decision-N-005-N-006-v1.md
9bd27c4d16d35a78411de85b418bdff91917fce289b97a53ea83730d0dc37fb9  docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md
b0b519fe250a839d904e75c66945326d30e47687093852c85eae6355add2cd72  docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md
038d4f87bfa0031349fad9a9df0e7ea5d515d3feba9d35b19c8e405647c0d087  docs/sources/lecture-pdf-niveau1/rapport-2606.08892-v1.md
94f56baf56f80950eeed18b1df3fe98c605c146c9a76f886e01d810282dffd44  docs/sources/lecture-pdf-niveau2/rapport-lot2-C1b-persuasion-v1.md
c19a9a315a60055bee7a9f6a5205134073bb9afc4cffffe8b54c8c5f1e2d5309  docs/sources/lecture-pdf-niveau2/rapport-lot2-A4-protocoles-controle-v1.md
e13da017a844ea09b8c307d7dc977a7ed9fdc7a1a325b24036517c017ce0f04b  requirements-cpu.txt
```
