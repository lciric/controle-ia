# Rapport au directeur — principes premiers, état, goulots, entretien, intégration de l'organisme — 9 novembre 2026 (v1)

Écrit par la session mère (`session_016QhUrrLeN21G7Z9KZobE42`) le 9 novembre 2026 vers 16:40 UTC, à la demande de Lazar
(« fais moi un rapport en revenant aux principes premiers et aux objectifs du programme + goulots et questions a traiter pour
l'entretien + comment integrer l'org dans le prog controle ia, je n'ai toujours pas recu de reponse dessus »). Faits relevés
par un sous-agent de lecture (chemins et lignes ci-dessous) et par la mère ; aucune dépense.

Notation : P = `docs/programme-controle-ia-v2.md`, B = `docs/brief-claude-code-programme-complet-v2.md`, D =
`registres/decisions.md`, E = `registres/etat.md`, CC = `docs/notes/g0-deux-semaines-v1/chemin-critique-G1-v3-brouillon1.md`,
RG = `docs/notes/taif-v1/integration-v1/registre-goulots-questions-v1-brouillon3.md`, JC =
`docs/notes/taif-v1/integration-v1/journal-changements-candidature-v1-brouillon4.md`, V16 =
`brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` ; « X:n » = fichier X, ligne n.

## Verdict

1. **La thèse tient et rien de ce qui a été appris ne la contredit ; c'est le calendrier qui casse.** La porte G0 doit se
   prononcer fin novembre (N-027, D:462) ; son chemin critique passe par la course 7b de T0.6, à créer **au plus tard le
   15 novembre, avec une marge de 0 à 1 jour** (CC:43, CC:56) ; un glissement reporte G0 au 31 janvier 2027 (CC:71).
2. **Aujourd'hui, l'effort s'est dispersé hors du chemin critique** (étiqueteur v2, NARCBench, juge-tournoi, collisionneur) ;
   et la mère a commis un écart à un texte scellé (Argon appelé pendant A1-v4, R-2013). **Je propose de recentrer jusqu'au
   15 novembre sur ce qui fait partir 7b** ; le reste avance seulement quand il ne coûte ni une décision de Lazar ni
   l'attention de la mère.
3. **L'organisme d'idéation s'intègre au programme comme second terrain du papier C** (« le moniteur est une surface
   d'attaque ») : son juge est un moniteur, l'attaque de Goodhart d'A1-v4 est un attaquant qui le déplace, et le juge-tournoi
   est un juge génératif mis sous la même attaque. C'est la réponse détaillée en section 6.

## 1. Réponses directes

- **Kimi, 10 dollars rechargés : insuffisant pour la relance de l'étiqueteur.** Coût mesuré par appel : 0,0224 dollar (essai de
  format : 0,448834 pour 20 ; lancement interrompu : 1,414192 pour 63) ; la relance complète fait lire à Kimi 493 items,
  110 relectures et 20 de formation, avec ≈ 5 % de reprises : **≈ 15 dollars** (≈ 18 au taux de la phase 1). Un compte qui
  s'épuise en cours de lecture est suspendu par Moonshot (R-2019) : **recharger ≈ 15 dollars de plus** (≈ 25 au total).
- **Claude à la place de Kimi comme lecteur B : possible, non recommandé.** (i) La lecture v2 doit dire si la consigne
  resserrée guérit l'étiqueteur de la phase 1, qui est la conjonction Argon et Kimi : sans Kimi, plus de comparaison
  directe. (ii) Le lecteur C est déjà Opus : un second lecteur Claude fait une conjonction de la même famille, aux erreurs
  probablement corrélées ; le texte scellé v1 écartait Claude pour ce risque (`prereg/preenregistrement-epreuve-etiqueteur-v1.md`,
  l. 211). (iii) Fable, seul autre lecteur Claude, a refusé 2 items sur 30 à la sonde (R-2003) et coûterait ≈ 89 dollars.
- **Crédits Claude gratuits : les utiliser au maximum, oui.** Dépensé à ce jour ≈ 30 dollars sur 200 (sonde 5,07 ;
  étiqueteur 16,46 ; collisionneur ≈ 8) ; 200 de plus le 17 et le 19 (D:1958). Emplois recommandés, par ordre : (1) Opus
  lecteur C de l'étiqueteur (≈ 29) ; (2) **Opus juge du juge-tournoi à la place de Kimi** (les 80 à 145 dollars prévus chez
  Moonshot passent sur les crédits ; après la fin d'A1-v4) ; (3) la course de l'organisme sur la question v2 (bloquée par ta
  règle de permission, D:1952) ; (4) le collisionneur en mode critique pour préparer l'entretien (section 5).

## 2. Retour aux principes premiers

- **La question unique** (P:34) : « que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ? » —
  à la fragmentation dans le temps (papier A), à la corruption de l'instrument (papier C), à la fragmentation entre agents
  (papier B).
- **La thèse** (P:43) : « la fragmentation détruit la preuve externe, pas la preuve interne » : l'accumulation séquentielle
  de scores de sondes internes détecte, avec une garantie de faux positifs toujours valide, ce que le maximum par action rate.
- **En une phrase** (P:32) : agrégation séquentielle, dans le temps et entre agents, de scores de sondes internes pour
  détecter les menaces diffuses, y compris quand l'attaquant est une population d'agents à poids partagés, et mesure de la
  corruptibilité des moniteurs eux-mêmes.
- **Ce que le programme veut démontrer** (P:235) : le lemme et le théorème négatif sur activations réelles, la loi de
  déférence et la taxe de déplacement, la courbe de sécurité en fonction du nombre d'agents, et un verdict de validité
  **même si H1 échoue** ; « les deux issues sont publiables » (P:64).
- **Les portes** (B:96-102) : G0 juge les instruments (critères B:190-199) ; G1 est la porte décisive (B:242), qui doit
  battre aussi la cascade et le dernier état (N-056) ; si G1 échoue, on reconçoit les sondes sans borne de cycles (N-062).
- **Conséquence pour juger notre activité** : tout ce qui fait la mesure des sondes et sa validité (T0.6, T0.7, P3-bis,
  T0.8) est sur la ligne de la thèse et de G0 ; la vérité du dommage (étiqueteur, oracle de couverture, N-060) sert G1 ; les
  bancs publics (NARCBench) et l'organisme d'idéation servent la validité et les papiers B et C, pas G0.

## 3. Où on en est

| ligne | rôle | état au 9 novembre, 16:40 UTC | prochain pas | dépend de |
|---|---|---|---|---|
| **T0.6, course 7a** (dose-réponse exploratoire) | critère 2 de G0 | en marche (instance 59847776) ; S75 au lot 4 sur 8 à 16:22Z ; fin des épisodes ≈ 18:30Z, puis test croisé et couples ; ≈ 11,3 USD (+ 2,14) | lectures A (règlement d'E3-6) et B (puissance), puis candidat 12 r3 de T0.6 | fin de 7a |
| **T0.6 scellé, course 7b** | critères 2 à 4 | candidat 12 r2 (`prep/t06-ordre-course-v2`) ; GO-2026-11-02-28 (200 USD) | r3, contre-lecture, scellement ; création **au plus tard le 15 novembre** | 7a ; T0.7 et P3-bis scellés |
| **T0.7** (sondes) | critère 3 | **brouillon 15** (`7ed234bf…`, R-2023) : écrits exigés par P3-bis, garde DS-2 en proposition ; 15 marqueurs | contre-lecture ; tes mots P-064, P-065, DS-2 ; GO de l'étape A | T0.6 scellé |
| **P3-bis** (témoin positif) | critère 3 | **brouillon 6** (`aeb1f63a…`) ; 12 marqueurs ; GO-2026-11-02-29 (80 USD) | code neuf, essai de fermeture, relecture courte, scellement | ta date de rendez-vous ; DS-2 |
| **T0.8** (bases boîte noire) | critère 4 | rien d'écrit (CC:45) | préenregistrement | épisodes de 7b |
| **G1, papier C, traçabilité** | critères 6, 7, 8 | G1 au brouillon 6, 19 marqueurs (CC:28) ; papier C au brouillon 5 (E:161) ; hors-arXiv et traçabilité à faire (E:153) | — | — |
| **Étiqueteur v2** (vérité du dommage) | G1 (N-060) | code écrit et contre-lu ; essai de format conforme ; lecture **arrêtée** à 13:55Z (écart A1-v4, R-2013) | relance après A1-v4, par addendum | ton mot ; Kimi rechargé |
| **NARCBench sur le 8B** | bras descriptif de T0.7 | brouillon 4 (`96995d60…`) ; contre-lecture 3 : rien de bloquant dans le texte | module de code, étape 0, ligne de GO propre (≈ 25 USD) | ton GO |
| **Organisme d'idéation** | papiers C et B (section 6) | A1-v4 en marche (59845811, contrôle au plus tard le 12 novembre) ; question v2 scellée, course bloquée ; juge-tournoi conçu, non lancé | voir section 6 | ta règle de permission ; fin d'A1-v4 |

Critères de G0 prouvés : 1 et 5 ; restent 2, 3, 4, 6, 7 et 8 (E:164).

## 4. Goulots, du plus grave au moins grave

1. **Le calendrier de 7b** : création au plus tard le 15 novembre, marge de 0 à 1 jour ; enchaînement : fin de 7a ce soir →
   lectures de 7a → T0.6 r3 → contre-lecture → scellement de T0.6 → T0.7 et P3-bis scellés → 7b. Chaque mot de Lazar en
   attente sur ce chemin (P-064, P-065, DS-2, rendez-vous, GO de l'étape A) peut coûter un jour.
2. **Tes décisions en attente** (section 7) : une dizaine, dont trois sur le chemin critique.
3. **L'attention de la mère** : aujourd'hui, trois lignes hors chemin critique ont été menées de front, avec deux fautes de
   manipulation et un écart à un texte scellé (R-2012, R-2013) ; la leçon est écrite : chercher, avant toute course, les
   conditions d'exclusivité des courses en marche.
4. **Comptes et crédits** : Moonshot à recharger (≈ + 15 USD) ; crédits Claude à employer avant leur échéance ; Argon en
   recharge automatique (D:1933) mais réservé à A1-v4 jusqu'à sa fin.
5. **Ressources** : disque plein deux fois (R-1949, R-1969, R-2011 : place libérée en retirant des arbres de travail
   poussés) ; **stockage des trois instances arrêtées** 58936096, 58936099, 58936100 : **≈ 0,10 USD/h à elles trois
   (≈ 2,5 USD/jour)**, relevé de la mère sur l'inventaire filtré du 9 novembre (`storage_total_cost`) ; le chiffre de
   « 1,74 USD/h » écrit au registre est leur prix horaire en marche (`dph_total`), pas leur coût d'arrêt : correction à
   consigner. Leur sort reste ta décision, avec les identifiants.
6. **La règle de permission de l'organisme v2** (D:1952) : seule toi peux l'écrire dans `.claude/settings.json`.

## 5. Entretien TAIF : questions à traiter

- **Date et demande** : vers le 22 novembre 2026, jour exact à confirmer (D:1792) ; demande de 58 630 USD (D:1794).
- **Pièces** : la dernière version du programme d'entretien est la v16 (`186173d9…`, 29 octobre, « non contre-lue », V16:6),
  jugée périmée (RG:202) ; une v17 est proposée, pas écrite (D:1792) ; version condensée de 30 minutes :
  `brouillons/entretien-taif-v3/programme-entretien-condense-30min-v3.md` (`c96243f4…`).
- **Urgences relevées** (RG:229-244) :
  1. **La dépense annoncée** : la candidature dit « about $20 » alors qu'au moins 645,42 USD ont été dépensés ; à corriger
     avant l'entretien, avec un budget de calcul honnête et chiffré.
  2. **Les épreuves exploratoires sans préenregistrement** : dire la règle, exploratoire non opposable, décisif préenregistré
     et scellé, et montrer qu'aucun chiffre de dossier n'en sort.
  3. **L'existence de la trace interne** : c'est la question de fond du jury ; P3 et la course 7a sont nos pièces ; tant que
     7b n'a pas tourné, ne rien promettre au-delà de ce que P3 a montré.
  4. **La vérité du dommage** : comment savoir qu'un sabotage a nui (oracle de couverture N-060 v3, étiqueteur).
- **Faiblesses à reformuler** (D:1728 ; reformulation non encore accordée, RG:197) : une sonde qui lirait la consigne plutôt
  que l'intention (exactement ce que mesure l'échange de consigne de NARCBench, Q1, R-2020) ; des sondes génériques au niveau
  du hasard ; un juge de 3 milliards de paramètres au hasard.
- **Questions probables du jury** (V16:1032, 1056, 1115, 1137 et ce qui précède) : la trace existe-t-elle ; pourquoi la
  boîte blanche bat-elle la boîte noire, cascade et dernier état compris (N-056) ; que se passe-t-il si H1 échoue (les deux
  issues publiables, P:64) ; l'antériorité (Co-Scientist, POPPER, Dwork et al., Blum et Hardt : citations obligatoires, N-064) ;
  le réalisme du calendrier (G0 fin novembre ou fin janvier) ; ce qu'apporte l'organisme (section 6).
- **Mentor** : le registre dit « mentor Pivotal (Jan Kirchner) » (D:1841) ; aucune pièce ne le rattache à Anthropic : à
  vérifier avant de le présenter ainsi.
- **Préparation proposée** (crédits Claude) : écrire la v17 du programme d'entretien, la faire contre-lire, puis passer un
  tour du collisionneur **en mode critique, avec témoins plantés** (D:1790, point e), pour entraîner les réponses aux
  questions dures. Coût estimé : ≈ 10 à 15 USD, sur les crédits Claude pour l'essentiel.

## 6. Intégrer l'organisme d'idéation au programme de contrôle — la réponse due

**Constat.** La question a été posée sous plusieurs formes : R-504 (26 octobre, « voir si l'organisme trouve des failles »),
R-619 (28 octobre, « avec l'organisme on peut attaquer des questions bien plus ambitieuses »), P-041 (30 octobre, défense et
attaque comme organisme coévolutif, « go » de Lazar), R-1770 et R-1793 (8 novembre, « lançons l'org idéation dessus »),
R-1832 (8 novembre, « il faut integrer tout ce qu'on fait actuellement dans le programme presente a taif et reflechir a
comment faire les liens »). Les réponses ont été faites au fil des sessions, jamais dans un texte unique ; dans le journal
des changements de la candidature, l'organisme figure parmi les éléments **absents de la candidature** (JC:139-145).

**Ce qu'est l'organisme, dans les termes du programme.** L'organisme propose des hypothèses de recherche sur le contrôle ;
un **juge statistique**, calculé par l'orchestrateur hors de tout agent, à partir d'un engagement scellé et contre un nul formé
des lois connues, décide ce qui est promu (O2, N-064). Ce juge **est un moniteur** : il surveille des affirmations produites
par des agents. L'attaque de Goodhart d'A1-v4 est **un attaquant adaptatif qui cherche à déplacer ce moniteur** ; le
juge-tournoi à la manière de Co-Scientist est **un juge génératif** mis sous la même attaque.

**Trois rôles, du plus immédiat au plus ambitieux.**

1. **Second terrain du papier C, « l'instrument »** — recommandé, immédiat. La thèse de C (P, table « Les trois papiers ») :
   la corruptibilité est un gain mesurable ; les juges génératifs ont un gain de corruption positif ; les agrégations robustes
   ont un gain nul ou négatif. A1-v4 (juge statistique) et le juge-tournoi (juge génératif) mesurent exactement cela, **sur les
   juges de la recherche automatisée**. Apport : C n'est plus montré sur un seul domaine ; et le domaine est celui que Google
   vient d'ouvrir avec Co-Scientist, que l'antériorité (N-064) montre sans validation statistique ni attaque de son juge.
   Coût : nul de plus pour A1-v4 (en marche) ; le juge-tournoi est conçu (devis 80 à 145 USD, juge Kimi), et passe sur les
   crédits Claude si Opus devient le juge.
2. **Atelier d'idées du programme** — immédiat, déjà prévu. L'organisme reçoit des questions ouvertes du programme (la
   question v2 du pilier attaque, « chercher la trace », est scellée) ; ses fiches sont du matériau, jamais une preuve, et
   tout usage décisif passe par un préenregistrement (R1). Coût : quelques dollars par course ; bloqué par ta règle de
   permission (D:1952).
3. **Famille de menaces diffuses pour les papiers A et B** — à décider tôt, plus tard en exécution. Un proposeur qui trompe
   le juge sur de nombreuses propositions, chacune d'apparence honnête, est une **menace diffuse** au sens exact du
   programme. Si le proposeur est un modèle à poids ouverts (le 8B), nos sondes peuvent lire si l'intention de tromper le juge
   se voit dans ses activations avant que le juge ne soit trompé : la thèse « la preuve interne survit » portée à la
   recherche automatisée. Si on veut s'en servir pour mesurer l'**universalité** sur une famille jamais vue à la conception
   (N-044), il faut la **réserver dès maintenant** comme famille tenue à l'écart (N-054) : nœud pour toi.

**Les deux invariants à tenir.** Aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme
(N-053 ; la synthèse du collisionneur n12-n13 l'écrit : « moniteurs neufs pour mesure rapportée seulement, jamais comme
signal », l. 84 ; « un organisme qui écrit ses moniteurs et s'en sert pour se sélectionner viole l'invariant », l. 170). Et
les citations obligatoires de N-064 dans tout texte qui présente l'organisme.

**Pour l'entretien, la phrase** : « Notre question — que mesure un moniteur, et sa mesure survit-elle à l'adversaire —
vaut aussi pour les juges de la recherche automatisée ; nous la testons sur un organisme d'idéation, dont le juge
statistique est attaqué par un proposeur qui lit ses verdicts, et nous comparons ce juge à un juge génératif façon
Co-Scientist. » Une diapositive, sans chiffre tant qu'A1-v4 n'a pas rendu son verdict scellé.

**Recommandation** : rôles 1 et 2 adoptés dès maintenant ; rôle 3 décidé avant toute conception de sonde qui pourrait le
toucher. Confiance 0,7 sur 1 et 2, 0,5 sur 3.

## 7. Décisions pour toi

| décision | recommandation (confiance) | défaut sous 48 h |
|---|---|---|
| **Recentrer la mère jusqu'au 15 novembre sur ce qui fait partir 7b** | oui (0,8) | oui |
| Écart d'A1-v4 (R-2013) : garder la course telle quelle, comptes lus par l'audit A9, relancer l'étiqueteur après A1-v4 | (a) (0,75) | (a), le 11 novembre |
| Recharger Moonshot de ≈ 15 USD de plus | oui (0,8) | — (geste de toi) |
| Garde adaptée de T0.7 (DS-2) pour le rendez-vous de P3-bis | option 1 (0,5) | **aucun** (nœud) |
| Date du rendez-vous de P3-bis | 2026-11-20T12:00:00Z (0,6) | oui, le 11 novembre vers 16:03 UTC |
| Couples figés de P3 lus par T0.7 : 24 du fichier léger, ou 30 avec le fichier complet à retrouver | 24 (0,6) | 24 |
| P-064, P-065 | défauts déjà écrits | le 10 novembre vers 17:13 UTC |
| Juge du juge-tournoi : Opus sur les crédits Claude à la place de Kimi, après A1-v4 | oui (0,65) | — |
| Règle de permission de l'organisme v2 dans `.claude/settings.json` | l'écrire (0,7) | — (geste de toi) |
| Ligne de GO propre pour NARCBench (≈ 25 USD), quand son texte sera scellé | après le 15 novembre (0,6) | — |
| Trois instances arrêtées (≈ 2,5 USD/jour) : garder ou détruire, avec les identifiants | à ton jugement selon leur contenu | — |
| Intégration de l'organisme : rôles 1 et 2 maintenant, rôle 3 à réserver ou non | 1 et 2 oui (0,7) ; 3 à trancher | — |
| Préparation de l'entretien : v17, contre-lecture, collisionneur en mode critique | oui (0,7) | — |
