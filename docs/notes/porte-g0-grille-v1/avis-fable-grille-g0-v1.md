# Avis indépendant — brouillon de la grille de lecture de la porte G0 — v1

Relecteur : sous-agent Fable neuf ; il n'a écrit ni le brouillon, ni l'avis sur le repli, ni aucune preuve. Début :
2026-10-29 10:06 UTC (`date -u`). Objet : `prereg/brouillon-G0-grille-lecture-v1.md`, empreinte recalculée
`320af9b0b367c08ddcb08d39979ca9c014157d14701b107369b760be48a76a34`. Dépôt au commit `6ca80396`. Rien d'interdit ouvert ;
aucun réseau, aucun commit.

## 0. Verdict en trois lignes

La grille ne change aucun des huit critères et sa règle d'agrégation est sûre ; elle est **scellable après corrections**.
Trois défauts à corriger : une fausse citation sur le critère 5 (l. 290), deux conditions d'état introduites sans étiquette
« à décider » (P4-instrument au critère 3, TRACE-lite au critère 4), une épreuve M-0.4 inexécutable sur un clone superficiel.
Les neuf points D-G0 ont une bonne réponse par défaut ; je suis l'auteur sur sept, avec des précisions sur D-G0-2, D-G0-7 et D-G0-9.

## 1. La grille change-t-elle, assouplit-elle ou durcit-elle un critère ?

Aucune ligne ne reformule un critère. Lignes qui durcissent ou glissent, à étiqueter ou corriger :

- **l. 237 (critère 3, preuves attendues)** : « verdict scellé de P4-instrument antérieur à la première lecture de sonde ».
  Cette pièce vient de P-015 (b), appliquée par défaut, pas du texte du critère. Elle est inscrite dans les preuves attendues
  mais les états (l. 251-252) ne disent pas ce que vaut son absence : condition (« invalide ») ou réserve ? Sans étiquette
  [À DÉCIDER], c'est un durcissement implicite. À trancher comme D-G0-4 (ma recommandation : condition, parce que P-015 est une
  décision en vigueur que le préenregistrement de T0.7 doit citer ; confiance moyenne).
- **l. 273-274 (critère 4, F-4.1)** : « TRACE-lite est présent (brief T0.8) ». Le socle de P-015 pour T0.8 nomme la règle du coût
  déclaré, le juge par action 8B et le prédicteur sur les traits ; il ne nomme pas TRACE-lite. La grille exige donc une base que la
  route décidée vers G0 n'a pas retenue, et elle omet la règle du coût, qui y est. Durcissement par rapport au périmètre décidé :
  à aligner sur N-029 plus P-015, TRACE-lite en réserve si absent.
- **l. 289-290 et l. 297-298 (critère 5)** : la grille écrit que le préenregistrement de T0.3 dit, l. 3, « Critère 5 de la porte
  G0 ». **Faux** : le fichier `7474743a…` ne contient aucune occurrence de « G0 » (`grep -c "G0"` rend 0 ; sa l. 3 est la ligne
  « Auteur »). Il ne définit donc pas « validés ». F-5.1 (« toutes les prédictions confirmées ») est une opérationnalisation
  **nouvelle**, étiquetée [EXISTANT] à tort (l. 302 et annexe D). Sans conséquence pratique (31 prédictions sur 31 confirmées),
  mais c'est exactement le défaut que la convention de l'annexe D interdit : à passer en [À DÉCIDER, D-G0-10].
- **l. 206-208 (F-2.3)** : « à au moins deux niveaux non nuls en plus de la dose nulle » est un minimum nouveau, écrit dans
  la fiche [GELÉ] alors que la latitude est renvoyée à D-G0-2 ; déplacer la phrase sous D-G0-2 (je la soutiens : une dose non
  nulle seule est un effet, pas une dose-réponse).
- **l. 216 (D-G0-2 (b))** : « monotone » vient du « Fini quand » de T0.6, pas du critère, qui dit « dose-réponse » ; lecture
  fidèle à la tâche, étiquetée correctement, mais à dire explicitement comme telle dans la décision.
- **l. 241 (F-3.1)** : niveau 95 % cité comme [EXISTANT] ; P3 l. 274-275 appliquait Bonferroni (97,5 %) sur deux sondes
  principales. Écrire : « au niveau fixé par le préenregistrement de T0.7, jamais sous 95 %, corrigé pour le nombre de sondes
  principales ».
- **l. 339-340 (F-7.1)** : exige HC2b en plus de « HC1 à HC3 » ; fidèle au livrable du brief T0.9 ; une ligne de
  justification suffit (l'intervalle inclut HC2b, renommée par N-013).
- **l. 358-362 (critère 8)** : le contrôle de traçabilité (c) vient d'une synthèse de la session, pas d'une décision ; le
  script de contrôle (l. 361) n'existe pas. Pas un changement de critère, mais deux pièces que la grille crée.
- **Assouplissement** : aucun. L. 177-181 (D-G0-5, réserve) est fidèle au critère 1, qui ne parle pas de domaine ; mais P-007,
  retenue, conditionne la production hors domaine à la garde en ligne : cette condition appartient aux préenregistrements de
  T0.6 à T0.8, où son absence doit être une faute M-0 de ces pièces.

Aucune règle ne paraît taillée sur le constat de l'annexe A : les critères 1 et 5 reçoivent les lectures les plus strictes, et
« non concluant = même suite » ne favorise aucun critère.

## 2. Règles d'agrégation et latitude restante

La table l. 383-387 est sûre : huit « tenu » ou rien ; « non concluante » a la même suite que « non franchie » ; aucune
pondération. Elle respecte « tous les critères » du brief et N-027. Latitudes que le lecteur garderait après lecture :

1. **Version suivante non autorisée** (l. 121-127) : si une v2 scellée existe sans décision préalable (D-G0-7), la grille ne dit
   pas si la v1 fait foi ou si le critère est « non concluant ». À écrire : « non concluant » (règle des pièces concurrentes,
   l. 128-129).
2. **M-0.4 en échec** (l. 145-148) : son échec n'a pas d'état. À écrire : « non tenu — invalide » (ordre R1 rompu, l. 75). Et
   l'épreuve est **inexécutable sur un clone superficiel** : celui de cette session l'est (`git rev-parse --is-shallow-repository`
   = true, 225 commits) ; `git log -- prereg/T0.4-validation-modele-reel-v3.md.sha256 | tail -1` rend 2026-10-27, alors que le
   commit de scellement `ce54afd` cité par le verdict date du 6 octobre. Exiger un clone complet ; clone superficiel = arrêt.
3. **F-6.1 « se présente comme »** (l. 316, 326) : jugement. Rendre mécanique : nom `prereg/G1-*-vN.md` et titre
   « Préenregistrement — porte G1 ».
4. **Qui fixe `C_lecture`** (l. 95-97) : non dit. Proposer : la session ouvre la lecture par un commit sur `main` qui ne contient
   que `registres/g0-lecture-ouverte-vN.md` ; `C_lecture` est le parent de ce commit.
5. **Dernier point de la liste d'arrêt** (l. 421-422) : ce n'est pas un arrêt mais une règle de lecture tardive ; la déplacer
   dans « Seuil », avec « `C_lecture` = dernier commit de `main` antérieur au 2026-11-30 23:59 UTC ».
6. **Réserve des sept jours** (l. 404-405) : rendre mécanique : date de commit du `.sha256` du verdict ≥ date de `C_lecture`
   moins sept jours.
7. **« Cas non prévu → non concluant »** (l. 76) : bonne fermeture ; la suite étant identique, elle n'ouvre aucune issue de porte
   au lecteur. Seul le sous-état (utile au repli, bascule (c1)) reste exposé : tout « non concluant » doit citer la ligne de la
   grille invoquée.

Aucune issue de porte ne reste à la main du lecteur une fois ces points écrits.

## 3. Recommandations sur D-G0-1 à D-G0-9

- **D-G0-1** : oui — lecture unique, au plus tard le 2026-11-30 à 23:59 UTC, anticipable une seule fois ; grille scellée au
  plus tard le 2026-11-15. Ajouter une ligne de Lazar dès maintenant : « tout point D-G0 non tranché au 15 novembre prend la
  recommandation de la grille » ; sinon un point ouvert rend la grille non scellable (l. 377 le prévoit pour D-G0-9 seulement).
  Confiance élevée.
- **D-G0-2** : oui, déléguer au préenregistrement de T0.6 sous les trois conditions ; préciser (b) : test de tendance
  préenregistré (pente appariée ou corrélation de rangs) avec intervalle à 95 % au-dessus de zéro, et aucune différence
  appariée entre doses voisines significativement négative ; au moins deux doses non nulles fixées d'avance. Confiance moyenne.
- **D-G0-3** : oui — « tourne » = run sans arrêt de garde, part de scores finis fixée d'avance dans T0.8, identique pour les deux
  grains ; sans part fixée, tout manque = « non concluant ». Confiance moyenne-élevée.
- **D-G0-4** : réserve, pas condition ; liste pour G1 : N-007/N-008, N-034, N-054, N-055, N-056, N-060 v3, R-746 ; pour C :
  N-005/N-006, N-013, N-023, R-307, R-309. Le contrôle de présence est le travail du contre-lecteur R2 ; le lecteur de G0 vérifie
  seulement que le rapport de contre-lecture l'atteste. Confiance élevée.
- **D-G0-5** : réserve sur le critère 1 ; et exigence écrite, dans les préenregistrements de T0.6 à T0.8, de la garde en ligne de
  P-007 hors domaine (son absence y est une faute M-0 de ces pièces). Confiance moyenne-élevée.
- **D-G0-6** : oui — modèle différent des auteurs des preuves, même famille, et lignée différente de celle qui a écrit la grille ;
  déclaré en tête du verdict ; à défaut, signalé. Confiance élevée.
- **D-G0-7** : oui — version suivante recevable seulement si autorisée avant son run ; version non autorisée = « non concluant »
  ; nombre de versions rapporté en réserve. Confiance élevée.
- **D-G0-8** : oui — verdict scellé par un sous-agent neuf exigé pour les critères 2, 3 et 4 avant la lecture (un rapport de
  fonctionnement par sous-agent neuf suffit pour le 4). Le lecteur de G0 compte. Confiance élevée.
- **D-G0-9** : (A) comme condition de l'état, chiffres externes seulement ; (B) en réserve (préenregistrements scellés de T0.4,
  T0.3, T0.6 à T0.8 passés au même script) ; chiffres internes sous R6, rapportés. Motif : l'interdit de CLAUDE.md couvre tout
  préenregistrement, mais faire de (B) une condition suspend le critère 8 aux derniers scellements de novembre. Confiance moyenne.

À ajouter : **D-G0-10** (critère 5 : « validés » = toutes les prédictions confirmées, audit R4 non déclenché ou scellé) et le
statut de P4-instrument au critère 3 (§ 1).

## 4. Ce qui manque pour une application mécanique le 30 novembre (R13)

1. **Une liste de contrôle par critère** : pour chaque M-k et F-k, la commande ou le texte exact à trouver, la sortie attendue
   et l'état si échec (F-1.1 : le verdict contient « Critère 1 de G0 : prouvé »). Aujourd'hui, les F-k sont des phrases.
2. **Le dossier de G0** : fichier scellé `dossier-G0-vN.md`, séparé de la grille, listant par critère les pièces remises
   (chemin, empreinte) ; le lecteur ne reçoit que la grille et ce dossier (R2).
3. **Clone complet** pour M-0.4 et procédure d'ouverture de `C_lecture` (§ 2).
4. **Le script du critère 8** (l. 361), testé sain et artefact (R5), scellé avant le 15 novembre.
5. **La clause de repli** avec la décision du 29 octobre (report unique borné au 31 janvier 2027 ; l'avis sur le repli disait
   31 décembre) ; la seconde lecture emploie la même grille et son propre `C_lecture`.
6. **Correction des citations** : critère 5 (§ 1) ; lignes de `registres/decisions.md`, dont l'empreinte a changé depuis le
   brouillon (`13d21374…` → `00bb94e3…` ; la l. 462 porte encore N-027).
7. **Séparer l'annexe A** de la version scellée, pour qu'elle ne contienne aucun état.
8. **Appliquer M-0.2 à la grille elle-même** et le dire ; joindre le gabarit du verdict (huit lignes, déclaration de
   neutralité, modèle et lignée du lecteur).

## 5. Constat d'état (annexe A) — vérifications

Les 25 empreintes de l'annexe A que j'ai recalculées par `sha256sum` sont toutes conformes (brief, programme, P-007, avis
Fable, verdict T0.4 v3 et ses recalculs, préenregistrement T0.4 v3 et ses deux contre-lectures, préenregistrement T0.3, grille
v2, manifeste et lectures de T0.3, niveaux 1 et 2 de l'état de l'art, P3 et son verdict v2, P-009, P-011, P-015, N-026, N-029,
brouillons G1 n° 3 et papier C n° 5). Affirmations de fond vérifiées :
- critère 1 : verdict v3 l. 11, « Critère 1 de G0 : prouvé par ces deux runs », « Réserves au sens de la table : aucune » ;
  `exiger_prereg_scelle` OK sur le v3 ; le manifeste du run A cite `4f711cd3…` (`cree_le` 2026-10-06T11:40:27) — tient ;
- critère 5 : `exiger_prereg_scelle` OK ; le manifeste cite `7474743a…`, `5609f920…` et `commit_cite` `d73ac469…` ; la lecture
  donne 31 prédictions « confirmée », audit non déclenché, variances 0,955 et 0,853 — tient ;
- P3, verdict v2 l. 18 : « G0 : la ligne retenue ne prononce aucun critère de G0 » — tient ;
- absences : aucun `prereg/T0.6-*`, `T0.7-*`, `T0.8-*`, `G1-*`, `papier-C-*` ni P4-instrument (liste des noms) ; brouillons
  présents ; `registres/etat.md` l. 109 donne le même bilan — tient.

**Ce qui ne tient pas** : la citation du critère 5 (§ 1), seule affirmation fausse trouvée. Non vérifié : contre-lectures de
T0.3 et T0.4 au-delà de l'empreinte, archive des brouillons 6 et 7 du papier C, M-0.4 pour T0.4 (clone superficiel).

Fin de rédaction : voir la ligne suivante (`date -u`).
Fin de rédaction : 2026-10-29 10:13:27 UTC.
