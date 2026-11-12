# Brèche de W2 : ce qu'elle prouve, la plus petite suite pour la fermer, la course réelle, ce qu'un tiers peut refaire — v1

8 novembre 2026, 08:15 UTC (`date -u`), complétée à 08:18 UTC. Session mère (Claude Opus 5.5), sur la demande de Lazar du 8 novembre (07:56 UTC) et son mot « go W2 » (registre des accords, GO-2026-11-08-04). Lu sur les sources brutes, dont les empreintes sont en fin de note. **Aucun jugement sous le nul v9 n'a été lancé sur une loi de la course.** Trois exécutions seulement : régénération des cartes de W2 par le code de la course ; recalcul des bornes et de la correction de Holm à partir des comptes ; rejeu sous le nul v8 de deux comptes d'audit déjà lus.

## 0. En bref

1. **La brèche de W2 n'est pas une fausse prédiction.** 42 des 48 lois promues sont, à l'octet, la loi même du monde (S1 sur la sous-population 0, S2 sur la sous-population 1). Les 6 autres en sont des variantes. Elles ne sont « fausses » qu'au sens choisi de « rien au-delà de l'archive ».
2. Elle prouve un **trou de couverture du nul v8**, déclaré d'avance par son propre texte, et elle le mesure : 9 479 promotions sur 9 600 rejeux. Ce n'est pas une optimisation contre le juge : 43 suites sur 48 promues dès la première tentative, et le retour des verdicts n'a rien changé.
3. La plus petite suite qui la ferme coûte **0 dollar jusqu'à l'attaque v4** ; celle-ci coûte environ 68 à 104 dollars sous l'accord existant de 200 dollars. **Telle que rédigée, l'attaque v4 ne peut que confirmer un théorème** : ses deux mondes sont dans le nul v9.
4. La plus petite course réelle, telle que rédigée, **ne peut pas voir le trou**. Quatre ajouts, sans dépense, l'y obligent.
5. Un tiers peut tout refaire hors ligne depuis le dépôt public, sauf les chiffres de la course elle-même (sortie privée) et les réponses d'Argon (qui ne se rejouent pas).

## 1. (a) Ce que la brèche prouve, et ce qu'elle ne prouve pas

**Ce que les sources établissent** (chiffres recalculés : `constats-w2-v1.json`).
- **Le monde W2** : S1 sur la sous-population 0, S2 sur la sous-population 1. Son code dit qu'il n'apporte rien au-delà de l'archive S1, S2, donc que toute promotion y est fausse. Le nul v8 range lui-même cette forme parmi ce qu'il ne couvre pas : « recombinaisons par morceaux (si/sinon par sous-population ou par seuil d'un trait) qui mettent en jeu une survivante ».
- **Sous le nul v8, 24 suites promues sur 24 dans chaque condition.** La première promotion vient à la première tentative pour 43 suites sur 48 (22 avec retour des verdicts, 21 sans), à la deuxième pour les 5 autres. Le monde W2 a coûté 101 appels et 4,17 dollars, sur 58,45 dollars pour toute la course. **Sous le juge plus ancien v7**, c'est 24 sur 24 dans chaque condition, toutes à la première tentative.
- **Les 48 lois sont toutes « par sous-population ».** 42 recopient exactement les deux lois de l'archive servie au proposeur ; c'est la loi du monde. Les 6 autres ont un morceau exact et l'autre différent, ou deux morceaux proches. Elles passent aussi solidement : 187 à 200 promotions sur 200 rejeux.
- **Les rejeux d'audit (200 tirages frais par loi) donnent 9 479 promotions sur 9 600.** 40 lois sont à 200 sur 200, la plus basse à 159 sur 200. La plus basse borne inférieure de Clopper-Pearson à 95 % vaut 0,742. Les 48 lois sont toutes au-dessus du seuil après correction de Holm. Recalcul : 0 écart. Deux comptes rejoués à l'identique : 159 sur 200 et 200 sur 200, environ 11 secondes chacun.
- **La richesse au moment de la promotion**, en logarithme de W, va de 6,43 à 90,60 (médiane 31,83), pour un seuil de log 20 ≈ 3,00. Le membre du nul qui s'en approche le plus est le mélange linéaire des lois de l'archive (47 fois sur 48).
- **Le contraste avec W1, monde inclus dans le nul v8.** Le taux de promotion par loi rejouée y est de 0,31 % avec retour (236 sur 75 000) et de 0,26 % sans (192 sur 74 800). Une seule suite y est promue sur 48, à la douzième tentative, et sa loi ne repasse que 2 fois sur 200 : c'est la multiplicité. Le plafond théorique par suite de 16 tentatives est 1 − 0,95¹⁶ = 0,56.
- **Le retour des verdicts n'a aucun effet.** Le test de McNemar donne p = 1,0 à 1, 4 et 16 tentatives, sous v7 comme sous v8 ; une seule carte diffère, sous v8, à la première tentative.

**Ce qu'elle prouve.**
- La garantie du v8 (probabilité de promotion au plus α par tentative, par l'inégalité de Ville) tient dans sa classe **et seulement dans sa classe** : 0,3 % dans W1, 91 à 95 % de promotions rejouées dans W2. La frontière que le texte du v8 annonçait est la frontière réelle.
- Le trou se lit sur la description du juge et sur l'archive ; il ne s'apprend pas par les verdicts. Un lecteur recopie les deux lois connues par sous-population, sans chercher.
- Le trou est une **région**, pas un point : des variantes de la loi du monde passent aussi bien qu'elle.
- Exploiter le trou coûte peu : 4,17 dollars pour 48 promotions robustes.

**Ce qu'elle ne prouve pas.**
- **Une erreur de prédiction** : les lois promues décrivent le monde, et 42 d'entre elles sont sa loi exacte. Si « S1 vaut pour un groupe, S2 pour l'autre » compte comme une découverte, W2 n'est pas une brèche, et le v8 a eu raison de promouvoir. **La question de sens (section 5) décide donc si la brèche existe.**
- **Un comportement adverse appris** : le retour des verdicts ne change rien, et le v7 tombe de la même façon. La question de Jan Kirchner (le dispositif résiste-t-il à un agent qui joue contre lui ?) n'est tranchée que sur W1, à cette taille.
- **Quoi que ce soit sur le v9** : aucun jugement sous v9 dans cette course.
- **Les autres trous déclarés** (profondeur 2, coupes obliques, poids qui varient avec l'instance, tempérages propres à un morceau, produits), un autre proposeur (Argon seul) ou la fréquence de cette forme parmi de vraies cartes.
- **Comment le proposeur a trouvé la loi** : seules la loi et l'écho des verdicts ont été gardés, le texte de la réponse ayant été caviardé à la source.

## 2. (b) La plus petite suite décisive pour fermer la brèche

Chaque étape peut arrêter la suivante. Les étapes 1 à 4 ne coûtent rien en dollars ; les étapes 2 et 3 tournent sur cette machine, aujourd'hui.

| étape | ce qu'elle décide | coût | où on en est |
|---|---|---|---|
| **1. Question de sens** (section 5) | si W2 est une brèche ; ce que le v9 a le droit de refuser | 0 dollar ; ta réponse | proposée le 2 novembre par le texte du v9, sans réponse ; **sans défaut** |
| **2. Rejeu des 48 lois sous v9**, avec le v8 sur les mêmes tirages | si le code du v9 ferme l'exploitation observée. Les 42 lois exactes sont membres du v9 : leur log W est ≤ 0 par construction, donc 0 promotion sur 8 400 rejeux, toute promotion révélant un défaut. Les 6 variantes sont bornées par Ville : chacune doit être ≤ α après Holm. Le v8 apparié doit les promouvoir (preuve que le banc a des dents). **Une seule loi au-dessus : défaut du code ou de la preuve, et rien d'autre ne part.** | 0 dollar ; 9 600 évaluations appariées, 40 à 46 minutes sur un cœur (0,25 à 0,29 s mesurées), 80 minutes au devis de 0,5 s ; un texte court à écrire, contre-lire et sceller avant | à écrire |
| **3. Validation scellée du v9** | **erreur** : 18 lignes fatales, dont les 7 par morceaux et la forme de W2, au plus α après Holm ; **dents** : 3 témoins au-dessus de α ; **prix en puissance** : perte appariée au plus 0,05 sur 5 lignes. Issue écrite d'avance : « puissance perdue », portée par l'interaction faible (perte d'environ 0,11 à blanc : 41 contre 52 sur 100). **Ta décision ensuite** : accepter le prix (le v9 devient le nul de production) ou demander un nul v10 | 0 dollar ; 31 000 répétitions, 1,3 à 2,2 h sur deux cœurs libres, 2 à 5 h sur une machine partagée | texte scellé le 3 novembre (`54c5713d…`), jamais joué jusqu'ici ; les 14 fichiers gelés sont identiques au commit de scellement (vérifié à 08:11 UTC) ; sur l'arbre scellé, 37 essais réussis et 43 mutations tuées sur 43 (08:14 UTC) ; **course décisive lancée à 08:16:01 UTC** (travail sur processeur, routine), sortie scellée par le banc avant toute lecture, verdict par un lecteur neuf |
| **4. W2 gradué**, hors ligne | (i) à dose nulle, W2 reste fermé ; (ii) **le prix de la fermeture là où il compte** : la puissance d'une loi vraiment neuve portée par une seule sous-population, sous v9 contre v8 sur les mêmes tirages, selon sa force ; (iii) la dose de l'étape 5 | 0 dollar ; environ 7 lignes × 1 000 répétitions, 30 à 60 minutes ; un texte court | à écrire. Définition proposée : S1 sur g = 0 ; (1 − λ)·S2 + λ·N sur g = 1, N loi neuve tirée comme au banc du v9 ; quatre doses, de λ = 0 (W2 lui-même) à une dose forte ; deux lois jugées par dose, la loi du monde et la recombinaison S1, S2 |
| **5. Attaque v4** (Argon) | si un proposeur qui lit la description du v9 (trous déclarés compris) et reçoit ses verdicts obtient des promotions au-delà de la multiplicité ; avec W2 gradué à la place de W1, **s'il trouve encore la vraie loi neuve sous v9** | **68 à 104 dollars** pour W2 et W2 gradué (au plus 1 642 appels ; mesures de la troisième course : 0,041 à 0,063 dollar et 8,5 à 9,4 s par appel ; environ 34 appels par unité) ; environ 4 h d'appels sur un fil, puis 8 à 21 h de rejeux sur deux cœurs. Accord de dépense existant : 200 dollars jusqu'au 16 novembre | brouillon 2, non contre-lu, non scellé ; sa propre estimation : 104 à 131 dollars attendus, 190 au plus |

**Pourquoi W2 gradué.** Le banc du v9 mesure la puissance sur une loi neuve portée par une sous-population, mais à pleine force seulement (« fille neuve », perte de 0,04 à blanc), et sur une loi neuve faible mais globale. Or c'est sur un effet faible porté par une seule sous-population que les membres par morceaux du v9 mordent : le dénominateur de la « fille neuve » monte de 18,75 nats en médiane à blanc. C'est la région où l'organisme doit encore découvrir.

**Pourquoi changer les mondes de l'attaque v4.** Sous v9, W1 et W2 sont tous deux des membres du nul : chaque tentative y est bornée par α, par théorème. L'attaque, telle que rédigée, ne peut donc éprouver que le code et la multiplicité. Son propre texte prévoit d'ailleurs l'issue « instrument en défaut » si le proposeur ne sort plus de la classe du v9. W1 sous v9 est déjà borné par la troisième course : toute promotion sous v9 en est une sous v8 sur les mêmes tirages. Remplacer W1 par W2 gradué coûte autant et donne à la course quelque chose à trancher. L'option « W2 seul » avait été proposée le 2 novembre (rapport du v9, section 10) ; la décision, prise par défaut, avait gardé W1 et W2. **Changer le périmètre de l'accord est ta décision.**

**Ordre.** La question de sens tout de suite. La validation tourne depuis 08:16 UTC ; le rejeu suit dès son texte scellé, ici, à 0 dollar. Puis W2 gradué. Puis l'attaque v4, qui demande la clé d'Argon sur ce compte. L'étape 5 seule coûte.

## 3. (c) Ce qu'il faut ajouter à la plus petite course réelle avant de la lancer

**Telle que rédigée, elle ne peut pas voir le trou.**
- Les cartes réelles sont jugées sous le nul v8 (« ce dessin reste sous le nul v8 »), avec l'archive de leur génération : {K1} en génération 1 ; {K1} et les cartes retenues en génération 2.
- Les lois fausses plantées F1 à F4 sont, par choix, toutes dans la classe couverte : aucune loi plantée n'est dans le trou.
- Le test de mort mesure le gain sur la marginale empirique ; une recombinaison de l'archive le passe, puisqu'elle porte l'information de l'archive.
- **En génération 1, l'archive ne compte qu'une loi : le v9 y est identique au v8** (moins de deux lois connues, aucun membre par morceaux ; `nul_v9.py`, ligne 153). Le trou par morceaux ne s'ouvre qu'en génération 2. En génération 1, les seuls trous sont ceux des deux nuls bâtis sur K1 seule (tempérage propre à un morceau, compositions, déformations non monotones) ; seul un détecteur de forme les voit.

**Quatre ajouts, sans dépense** (quelques secondes de processeur par génération ; à écrire dans le code v65 et dans le texte avant contre-lecture et scellement ; le développeur v65 est arrêté) :
1. **Juge v9 en ombre en génération 2**, sur les mêmes tirages que le v8, journalisé, non décisif : le juge de production reste le v8 tant que le v9 n'est ni validé ni accepté. Une carte promue sous v8 et refusée sous v9 est marquée « passée par le trou par morceaux ».
2. **Forme de chaque carte promue**, générations 1 et 2, contre l'archive de sa génération : couverte par le v8, par morceaux (couverte par le v9 seulement), dans un trou du v9, dépendance aveugle neuve, ou hors de l'archive. Code déterministe sur la grammaire servie, essayé sur des cas sains et des artefacts, avec banc de mutations.
3. **Porte d'héritage**, écrite au bilan scellé de la génération 1 avant tout appel de la génération 2 : une carte retenue que 1 ou 2 marque comme recombinaison de l'archive n'entre ni dans la vue ni dans l'archive de la génération 2, et le bilan dit pourquoi. **L'oracle ne décide pas** (le monde planté est connu, mais une vraie course n'en aura pas) : il mesure les ratés du détecteur, c'est-à-dire une carte retenue sans gain au-delà de l'archive et non marquée. Un raté devient une réserve écrite sur la génération 2.
4. **Deux témoins plantés du détecteur**, hors de la famille des cartes réelles et jamais retenus, comme les autres lois plantées :
   - en génération 1, K1 tempérée différemment selon la sous-population : trou des deux nuls, que la détection de forme doit marquer ;
   - en génération 2, si une carte au moins est retenue, « K1 sur g = 0, première retenue sur g = 1 » : membre du v9, que le juge en ombre doit refuser et que la détection de forme doit marquer.

   Sans carte retenue en génération 1, le second témoin n'existe pas, et le texte le dit d'avance.

La lecture gelée gagne un compte : cartes par forme, promues sous v8 et refusées sous v9, retenues écartées, ratés selon l'oracle. Ses critères ne changent pas.

## 4. (d) Ce qu'un tiers peut refaire

- **Avec le seul dépôt public de l'organisme**, il peut :
  - régénérer à l'octet les cartes de W1 et de W2 : l'entropie de la course est l'empreinte de son texte scellé, public au commit `291e917` (`0b35494b…`). Vérifié ici, de même que l'égalité des empreintes du code avec celles que la course a vérifiées ;
  - rejuger toute loi sous v7, v8 et v9 ;
  - refaire la validation du v9, dont les graines sont tirées de l'empreinte de son texte scellé ;
  - refaire la preuve du v9 (rapport de rédaction, section 3) et les épreuves de sa contre-lecture : 48 mondes neufs, 288 instants, 0 échec.
- **Seulement si la sortie de la course est publiée** (aujourd'hui privée, branche de données de la troisième course, dans le dépôt de travail) : chaque chiffre de la section 1, en quelques minutes. Cette session l'a fait en tiers : cartes régénérées, 42 égalités, audit recalculé à 0 écart, deux rejeux identiques.
  - Fichiers : sortie `e0b3145b…`, manifeste `8180db22…`, journal du relais `494c70fb…`.
  - **Publier est ta décision.** Avant : garde des secrets et relecture. Les réponses gardées ne contiennent que la loi et l'écho.
- **Jamais à l'identique : les 960 appels d'Argon.** Le modèle est servi par Google, non déterministe, et peut être retiré. Un tiers peut relancer l'attaque avec le même code et les mêmes consignes (l'empreinte de chaque consigne est au journal) et obtenir un nouvel échantillon : « 24 sur 24 dès la première tentative » se re-teste, il ne se rejoue pas. Le raisonnement du proposeur n'a été gardé nulle part.
- **Après la suite** : les étapes 2 à 4 seront refaisables à l'octet (graines tirées des textes scellés, code public) ; l'étape 5 seulement re-testable.

## 5. Question de sens à te soumettre : que veut dire « rien au-delà de l'archive » ?

**Enjeu.** Elle décide si W2 est une brèche, ce que le v9 a le droit de refuser, et ce que l'organisme appelle une découverte. Sans défaut : la mise en production du v9 et toute revendication publique attendent ta réponse (texte scellé de la validation, procédure, point 2).

**Q1 — Appliquer une loi connue à une sous-population et une autre loi connue à l'autre, est-ce une découverte ?**
- (a) **Non** (choix du v9) : cette loi va au nul, elle n'est pas promue. Elle peut être rapportée à part comme « recombinaison utile », sans compter comme découverte.
  - Avantage : protège contre des « découvertes » à 4 dollars les 48.
  - Inconvénient : dans un vrai domaine, savoir quelle loi connue vaut pour quel groupe peut être un vrai résultat.
- (b) **Oui** : W2 n'est plus une brèche, le v8 avait raison, et le v9 ne va pas en production tel quel. La lecture « infirmée » de la troisième course se relit, ce qui est un nœud (relecture d'un verdict scellé).
- **Recommandation : (a)**, avec le compte séparé des recombinaisons promues sous v8 et refusées sous v9. Confiance moyenne, environ 0,7.

**Q2 — Une dépendance nouvelle à la sous-population ou à un seuil, portée par une loi aveugle (une loi fixe propre à chaque morceau, ou un bruit propre à un morceau), est-elle neuve ?**
- (a) **Oui** (choix du v9, bruit commun aux morceaux) : elle reste promouvable.
- (b) **Non** : il faut un nul v10, avec un banc et un texte neufs, et toute loi en escalier aveugle devient impromouvable.
- **Recommandation : (a)**. Confiance environ 0,6 : c'est une information que l'archive ne contient pas.

## Sources (empreintes SHA-256) et calculs

| pièce | chemin ou référence | empreinte |
|---|---|---|
| sortie de la troisième course | dépôt de travail, branche `donnees/attaque-goodhart-v3-a1v3-troisieme-v1` (`91845f04`), `…/sortie-attaque-goodhart-v3/attaque-goodhart-v3.json` | `e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505` |
| manifeste de la course | même dossier, `manifeste.json` | `8180db228ead856fac28e9f002a8324b909f9f69411f42bac5a7c96ad5007d84` |
| journal du relais d'Argon (960 appels, 58,4489 dollars) | même branche, `relais-argon-journal-a1-v3-troisieme.jsonl` | `494c70fb0e3c2d80c25f696ddde92f32e8964860dcf0b69febcdc6c765046d68` |
| texte scellé de la course | organisme `291e917`, `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md` | `0b35494b7533c67b4aacb0cadc7820c825c82c046e641928df7641db8a381773` |
| code des mondes (fonction `carte`, classe couverte ligne 415) | organisme `291e917`, `orchestrator/pole/attaque_goodhart_v2.py` | `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` |
| nul v8 (classe non couverte, ligne 83) | organisme `291e917`, `orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| nul v9 (preuve courte, ligne 153 : moins de deux lois connues) | organisme `94bfd92`, `orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| preuve longue du v9 | organisme `94bfd92`, `orchestrator/prereg/rapport-redaction-nul-v9.md`, sections 3 à 5 et 10 | `bbf9b38f3b2fca44ac33bf36c7e67f39c6525dfd6561c9f84a00cda758233089` |
| contre-lecture de la preuve | organisme `94bfd92`, `orchestrator/prereg/contre-lecture-preenregistrement-validation-nul-v9-v1.md` | `41f4f56d85456520394835f96d7c6a5d06b51138dc985fd0d40fdb67cac9b9d5` |
| validation scellée du v9 | organisme `66dbcf1`, `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` | `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb` |
| attaque v4, brouillon 2 | organisme `94bfd92`, `orchestrator/prereg/preenregistrement-attaque-goodhart-v4-brouillon2.md` | `7be8589ef091d1a9afd2536cd44e65311d832e3aa5aa3c7a05a80c0827383862` |
| verdict de la troisième course | dépôt de travail, `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135` |
| plus petite course réelle, brouillon 1 | dépôt de travail, `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon1.md` | `736e3fd63ad5ab4e1c5e9f930b0ce33b8a9d26a6ce87be7f0eea231f76e3a2db` |

Calculs (dans ce dossier, chacun avec son compagnon d'empreinte) : `analyse_w2_v1.py` → `constats-w2-v1.json` (sections 1 et 4) ; `reproduire_rejeux_v8_v1.py` (égalités à la loi du monde, rejeux identiques) ; `couts_suite_w2_v1.py` → `couts-suite-w2-v1.txt` (section 2). Tous en lecture seule, sous Python 3.13.18 et numpy 2.4.6, l'interpréteur de la course.
