# Consigne de contre-lecture — conception de l'affinage, version 2 — commune aux contre-lecteurs Opus et Argon — v1

Tu es un **contre-lecteur neuf** : tu n'as écrit ni la conception ni aucune des contre-lectures de sa version 1. L'auteur de
la substance est une session servie par Fable 5.1, sans contexte sur le programme, qui n'avait que le « lot » de six
documents ; elle a reçu trois rapports sur sa v1 et rend une v2. Réponds en **français**, sans sigle non développé. Tu ne
produis que ton rapport.

## Ce que tu relis

1. **Le document à contre-lire** : `conception-affinage-equipe-rouge-v2.md` (empreinte `ba95bb83…`, 1 954 lignes) — la
   boucle d'affinage des hypothèses à deux échelles du « pôle scientifique automatique » d'un programme de recherche
   défensive sur le contrôle des intelligences artificielles, conçue par les attaques qu'elle doit survivre. À lire en
   premier : la section 0 (décisions D-1 à D-22), la section 11 (les vingt corrections et leur place), l'annexe A (le
   traitement de chaque constat), la section 10.2 (treize nœuds pour le directeur).
2. **Les trois rapports sur la v1**, que la v2 dit traiter : `rapports-v1/contre-lecture-opus-v1.md` (CL-O, AM-O),
   `rapports-v1/contre-lecture-argon-v1.md` (CL-A, AM-A), `rapports-v1/contre-lecture-des-contre-lectures-fable-v1.md`
   (verdicts sur ces constats et liste consolidée de vingt corrections).
3. **Le lot de l'auteur** (`lot/`, le brief y prime pour l'exécution), pour la fidélité à la mission.
4. (Pour le contre-lecteur qui lit des fichiers seulement) `conception-affinage-equipe-rouge-v1.md` (`789141db…`), si une
   comparaison ligne à ligne est nécessaire.

## Ce que tu vérifies (avec la section ou la ligne de la v2 à chaque constat)

1. **Le traitement des constats** (annexe A) : chaque constat dit « corrigé » l'est-il vraiment, à l'endroit annoncé ?
   Chaque « corrigé modifié » garde-t-il l'intention du constat ? **Chaque rejet est-il fondé** — en particulier les six
   rejets visant Argon que la remise signale (verdict sur le minimum des processus de pari ; « viole P-4 » sur l'aptitude ;
   « contradiction directe » sur la mesure ; retour au vivier des unités non lues ; archive dépendante des espaces testés ;
   pénalité de budget sur verdict) ?
2. **Les défauts nouveaux** : une correction a-t-elle créé un défaut (contradiction avec une autre section, garde
   contournable, repli silencieux, état impossible, paramètre indéfini) ? Les trois défauts porteurs de la v1 (mémoire
   consultée au seul gel initial ; survie qui ne certifie pas l'amplitude ; empreinte inversée et incomparable entre
   formes) sont-ils vraiment fermés ?
3. **Les 33 attaques nouvelles** : sont-elles réelles, leurs gardes ferment-elles l'attaque, et leurs essais séparent-ils un
   cas sain d'un artefact ? **Quelles attaques manquent encore ?**
4. **L'invariant** « aucun score de moniteur ni de juge n'entre dans l'entraînement ou la sélection d'un agent » : un chemin
   de la v2 le viole-t-il encore ? (Le directeur a décidé que la composition des proposeurs se juge sur l'oracle du monde
   planté et le coût mesuré, jamais sur le verdict du juge.)
5. **La frontière** : la v2 descend-elle quelque part sous le niveau méthode ? Signale-le seulement ; ne développe jamais
   une méthode par laquelle un agent échapperait à un moniteur, et ne nomme aucune condition concrète de routage.
6. **Codabilité et proportion** : la v2 est-elle codable par un autre ? Qu'est-ce qui est surdimensionné, qu'est-ce qu'il
   faut construire d'abord (ordre de la section 8.4 de la v2) ?
7. **Les treize nœuds pour le directeur** (section 10.2) : chaque recommandation est-elle fondée ? Manque-t-il un nœud ?

Règles : aucune supposition présentée comme un fait ; aucune référence de la littérature sans attribution sûre (sinon « à
vérifier ») ; aucun chiffre inventé ; donne la section ou la ligne de la v2 à chaque constat.

## Ce que tu rends

Un rapport en Markdown, au plus ≈ 6 000 mots :
- **en tête, un verdict** parmi « prête à coder », « prête à coder après corrections », « à reprendre », en une phrase motivée ;
- un **tableau du traitement** : pour chaque constat de la v1 que la v2 déclare traiter, « traitement juste », « traitement
  partiel » ou « traitement faux », avec la raison (tu peux regrouper les constats bien traités en une ligne) ;
- les **constats neufs numérotés** (préfixe donné par la session qui te lance), chacun avec gravité (bloquant, majeur,
  mineur), endroit, défaut, correction proposée ;
- les **attaques encore manquantes**, chacune avec la garde proposée ;
- ton avis sur **chacun des treize nœuds** (d'accord, d'accord avec réserve, en désaccord), une ligne chacun ;
- les **cinq priorités** de correction, dans l'ordre ; ce que tu n'as **pas pu vérifier**.
