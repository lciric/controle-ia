# Revue d'antériorité et brainstorm à protocole fermé sur la question centrale — protocole v1

Écrit par la session 15 le 17 octobre 2026, **avant toute recherche**, à la demande de Lazar (R-203). Il fixe les requêtes, les
sources, les critères, le tri, les trois tours du brainstorm et les livrables. Il sert deux exécutions : la **revue rapide** (avant
l'appel EA Funds du mercredi 21 octobre, 16 h 30 à Paris) et la **revue exhaustive** (après l'appel, sur une session neuve). Tout
écart à ce protocole est écrit, daté et motivé dans le livrable. **Rien ne change dans le programme ni dans la candidature sans la
décision de Lazar** ; aucun contact externe, aucune publication (les messages aux experts sont rédigés, Lazar les envoie).

## 1. Objet

Décider s'il faut **garder, resserrer, déplacer, élargir ou approfondir** la question de recherche centrale du programme : la
porte G1 (papier A : l'accumulation séquentielle de scores de sondes lues sur l'agent détecte-t-elle un sabotage diffus que le
moniteur par action manque ?) et le papier C (corruptibilité des moniteurs : loi de déférence, taxe de déplacement, contre-mesures,
test d'acceptation) ; le papier B (essaim à poids partagés) en second plan.

## 2. Documents primaires (à lire tels quels ; pas de résumé de la session)

`docs/programme-controle-ia-v2.md` ; `docs/brief-claude-code-programme-complet-v2.md` ; décisions
`docs/decisions/decision-N-003-N-004-v1.md`, `decision-N-005-N-006-v1.md`, `decision-N-007-N-008-v1.md`, `decision-N-013-v1.md`,
`decision-P-008-v1.md` ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` (avec `niveau2-v1/` et les rapports de
`docs/sources/lecture-pdf-niveau2/`) ; `docs/notes/note-mathematique-lemme-theoreme-v3.md` ; `docs/notes/resultats-T0.3-v1.md` ;
`docs/verdicts/verdict-T0.5-pilote-v1.md` ; `brouillons/G1-preenregistrement-v1-brouillon3.md` ;
`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon2.md` ; `brouillons/P3-premier-test-i-a-v1-brouillon4.md` ;
`livrables/candidature-ea-funds-v1/proposal-v1.md` (version du dépôt ; la version envoyée au fonds n'est pas dans le dépôt) ;
`README.md`. **Exclus** : tout `brouillons/pain-axis-*` (aucune diffusion sans GO, DI-26).

## 3. Revendications à confronter

La liste fait foi dans `docs/decisions/decision-N-013-v1.md` (revendiqué, cité comme acquis, retiré) et dans la section 5 du
programme v2 (hypothèses H1, H2, L, T, H6, Tr, H8 ; HC1 à HC6 dont HC2b ; H3, H4′, H5, H7), lue avec N-005, N-006, N-007, N-008 et
P-008. Chaque exécution numérote les revendications (R-A1…, R-C1…, R-B1…) à partir de ces textes, avant toute recherche, et
écrit cette liste en tête de son livrable.

## 4. Sources et requêtes écrites d'avance

**Sources** : arXiv (listes et recherche plein texte) ; OpenReview (soumissions à l'ICLR 2027 ; ateliers de NeurIPS 2026) ;
Alignment Forum et LessWrong, **billets et fils de commentaires** ; pages de projets de SPAR, MATS, Apart Research, LASR, ERA,
Pivotal (sessions 2025 et 2026) ; GitHub (dépôts et leurs fichiers de présentation) ; blogs des équipes de sécurité : Anthropic
(Alignment Science), Redwood Research, OpenAI, Google DeepMind, institut britannique de sécurité de l'IA, METR, Apollo Research,
FAR AI ; Google Scholar, Semantic Scholar ou OpenAlex pour les citations (en amont et en aval) des articles de départ.

**Requêtes** (anglais), chacune jouée sur chaque source qui la permet ; toute requête ajoutée en cours de route est marquée
« ajoutée » avec son motif :
- A (temps, boîte blanche) : `sequential test probe scores agent monitoring` ; `anytime-valid e-process monitoring language model
  agent` ; `linear probe deception agent trajectory aggregation` ; `diffuse sabotage AI agents monitoring` ; `research sabotage
  automated AI research monitor` ; `sandbagging detection probes` ; `white-box monitoring AI control probes untrusted model` ;
  `CUSUM activations language model monitoring` ; `low-stakes AI control distributed threats` ; `probe-based monitor control
  evaluation` ; `accumulate evidence across actions monitor agent` ;
- C (moniteurs) : `persuasion LLM judge monitor susceptibility` ; `prompt injection against AI control monitor` ; `jailbreaking
  LLM monitors` ; `advice taking LLM judge advisor preregistered` ; `LLM judge deference to argument gain` ; `probe robustness
  adversarial obfuscated activations` ; `trusted paraphrasing defense monitor` ; `ensemble heterogeneous monitors probes and judges` ;
  `transfer of attacks between monitors` ; `acceptance test for monitors before deployment` ;
- B (essaim) : `shared weights agents collusion detection activations` ; `backdoor fragmented across commits multi-agent` ;
  `population-level monitoring of AI agent copies`.
- Articles de départ pour les citations : arXiv 2606.08892 (Terekhov et al.) ; 2502.03407 ; 2505.23575 ; 2510.09462 ;
  2609.36490 ; 2606.10456 ; 2603.13791 ; 2605.15377 ; Panin, SSRN 7424179 (PDF attendu de Lazar).

**Fenêtre** : revue rapide, du 1er janvier 2025 au jour de la recherche, priorité aux six derniers mois ; revue exhaustive, sans
plancher de date.

## 5. Tri, vérification, tableau

- **Inclusion** : tout travail (article, prépublication, billet, fil de commentaires, page de projet, dépôt) qui touche au moins
  une revendication ; hors sujet sinon.
- **Double tri** : chaque candidat est classé par deux trieurs indépendants, qui ne voient pas le classement de l'autre, pour
  chaque revendication touchée : **occupe** (même revendication, même cadre, résultat publié), **partiel** (une partie, ou un
  cadre voisin), **voisin** (lié, sans recouvrement), **hors sujet**. Désaccord : un troisième tranche. Accord brut rapporté.
- **Preuve** : citation exacte et lieu (page du PDF, section, ou adresse et passage du billet) ; sans citation vérifiée sur la
  source, le classement est « non opposable » (R7). Un chiffre d'un tiers n'entre qu'avec sa page.
- **Recherche affirmative** (R8) : pour chaque revendication sans « occupe » ni « partiel », un agent dédié cherche activement à
  la trouver occupée (requêtes nouvelles, synonymes, auteurs voisins) ; une zone vierge reste une question, jamais un trou acquis ;
  les zones vierges séduisantes sont vérifiées plus durement.
- **Tableau** : revendication × travail, avec classement, preuve, lien, date, et statut de vérification.

## 6. Brainstorm à protocole fermé (contre-ordre de Lazar, R-203)

Aucun dialogue libre entre modèles : ils convergent par politesse. Trois tours, et seulement trois :

1. **Objections à l'aveugle.** Des objecteurs indépendants, chacun avec un seul angle, lisent les documents primaires (section 2)
   et rien d'autre de la session ; aucun ne voit les objections des autres. Angles : responsable d'une équipe de contrôle dans un
   laboratoire (ce qui changerait ses décisions) ; statisticien sceptique (lemme, théorème, nouveauté) ; chercheur en
   interprétabilité (validité des sondes, construit) ; équipe rouge (évasion, attaques adaptatives) ; financeur (impact,
   contrefactuel) ; critique du modèle de menace (le sabotage diffus est-il la bonne menace, l'organisme instruit la bonne
   preuve ?) ; chercheur en organismes modèles. Chaque objection est classée **fatale** (la revendication centrale ou son récit
   d'impact ne tient pas tel qu'énoncé), **sérieuse** (impose de changer le plan, une hypothèse ou une revendication) ou
   **mineure** ; elle porte son argument, sa preuve (fichier et page, ou source externe à vérifier), ce qui la lèverait, et la
   probabilité, selon l'objecteur, qu'elle soit juste. Chaque objecteur donne aussi au plus deux idées audacieuses (question,
   hypothèse ou expérience, avec ce qui la réfuterait) et ses probabilités chiffrées pour : G1 passée telle qu'énoncée ; ĉ égale à
   la cible de l'attaquant pour au moins une famille d'attaque ; un résultat positif de G1 change une décision d'une équipe de
   contrôle ; un résultat négatif en change une.
2. **Réponses.** Un répondant neuf, qui n'a écrit ni le programme ni une objection, répond à chaque objection : concède, réfute
   avec preuve (fichier et page), ou reformule ; il n'ajoute pas d'objection, ne fusionne pas les objections, et ne ramène pas une
   objection fatale à moins sans preuve.
3. **Note de décision.** Un agent neuf lit les objections, les réponses et le tableau de la revue ; il écrit, pour chaque objection,
   son statut (tient, réfutée, en partie) ; un **rapport minoritaire** de toute objection fatale non réfutée ; puis les livrables
   de la section 7. Grille de notation fixée ici, avant lecture : importance pour une décision d'un laboratoire, originalité
   vérifiée, faisabilité en douze mois au budget de la candidature, valeur de l'information (chacune de 1 à 5).

Un objecteur externe d'une autre famille de modèles peut s'ajouter au tour 1 (Lazar lui donne l'invite du tour 1 et les mêmes
documents, puis colle ses objections) ; ses objections entrent au tour 2 comme les autres.

## 7. Livrables

(a) Tableau « issue → décision », acteur par acteur (équipe de contrôle d'un laboratoire, institut de sécurité, financeur, la
communauté de recherche), pour chaque issue des portes G1 et GC et du papier C. (b) Le tableau revendication × travail de la
section 5, avec les requêtes jouées et l'accord du double tri. (c) Objections, réponses et note de décision, avec les
probabilités (médiane et étendue). (d) Trois reformulations candidates de la question centrale (resserrée, déplacée, élargie),
chacune avec ce qui la réfuterait, son coût (temps, calcul, argent), le travail existant le plus proche (tiré du tableau), et une
recommandation avec sa confiance. (e) Trois à cinq experts à consulter, avec la raison de chacun et un message rédigé, que Lazar
envoie lui-même. Tout est versé sous `brouillons/revue-question-centrale-v1/` (revue rapide) ou `…-v2/` (revue exhaustive), avec
une empreinte compagnon par fichier (R6), non opposable tant que les citations ne sont pas vérifiées.
