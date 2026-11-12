# Avis indépendant — règle de repli si la porte G0 n'est pas franchie fin novembre 2026 — v1

Sous-agent Fable neuf, sollicité par Lazar. Début de lecture : 2026-10-29 09:35 UTC. Aucune dépense, aucun réseau.
Pièces lues : `question-repli-g0-v1.md`, `faits-repli-g0-v1.md` ; dans le dépôt, en lecture seule : brief v2 (sections 1,
4, 6, 7 « Porte G0 », 8 « Porte G1 », 13, 15, 17), programme v2 (sections 10, 13, 14), `registres/decisions.md` (N-027,
R-041, R-046, R-052, R-742), `registres/etat.md` (lignes sur G0 et les GO de calcul), entretien v12 (§ 1 bis, § 4, § 8, § 9,
points à trancher 12 et 13), liste de `prereg/` (noms seulement). Rien d'interdit n'a été ouvert.
Ce qui n'est pas dans ces pièces est marqué **SUPPOSÉ**. Cet avis est un matériau ; il ne tranche rien.

## 0. Verdict en trois lignes

La porte G0 doit rester binaire (franchie ou non franchie), prononcée à date fixe par un sous-agent neuf contre une grille de
lecture scellée **avant** la lecture. Le repli recommandé : **phase 1 fermée ; phase 0 prolongée une seule fois, sous
préenregistrement de reprise, avec une seconde et dernière lecture de G0 au plus tard le 31 décembre 2026 ; échec à cette
seconde lecture = arrêt de la phase 0 et rapport, sans nœud après lecture.** Confiance moyenne (≈ 0,6). Ce qui manque
aujourd'hui pour que ce soit applicable n'est pas la règle : c'est la **grille de lecture de G0**, qui n'existe pas
(`prereg/` ne contient aucun préenregistrement de G0 ; constat par la liste des noms, R11 non appliqué au-delà).

## 1. Ce qui déclenche le repli

### Constat de fait
- Le brief (§ 7) exige « tous les critères remplis, preuves scellées à l'appui ». Il n'y a donc pas de porte « aux trois
  quarts ». Le brief prévoyait déjà un nœud si un critère ne tenait pas au 1er novembre ; N-027 a consommé ce nœud en
  reportant la lecture à fin novembre, critères inchangés. La question d'aujourd'hui est : que fait-on si le nœud se représente,
  **sans** le rejouer après lecture.
- Le vocabulaire des verdicts existe déjà, par critère : « non concluant » (R-041), « non prouvé par ce run » (R-046),
  « prouvé » (R-052). Il suffit de le geler.

### Options
- **(1a) Échec = un seul critère non prouvé.** Avantage : fidèle au brief, aucune interprétation. Inconvénient : brutal si un
  critère est à une contre-lecture près. Mais « à une contre-lecture près » est exactement ce qu'un lecteur ne doit pas juger.
- **(1b) Échec seulement si un critère « bloquant » manque ; les autres tolérés.** Avantage : souple. Inconvénient : c'est un
  changement de critère déguisé (un critère toléré n'est plus un critère). **Hors cadre.**
- **(1c) Distinguer, par critère, trois états — prouvé / non prouvé (verdict scellé négatif ou non concluant) / non tenté
  (aucun verdict scellé) — et, à la porte, un seul état : franchie si huit « prouvé », sinon non franchie.** Avantage : la
  porte reste binaire, mais le rapport et une bascule (section 2, (c)) peuvent dépendre de l'état des critères sans qu'un
  lecteur ait rien à décider. Inconvénient : il faut écrire d'avance où est la preuve de chaque critère (section 4).

**Recommandation : (1c)**, confiance élevée (≈ 0,8).

### Détails à geler
- **Quand** : la lecture a lieu à une heure fixe, le **30 novembre 2026 à 23:59 UTC**, ou plus tôt si les huit preuves sont
  scellées (franchissement anticipé permis à tout moment, jamais partiel).
- **Qui** : un sous-agent neuf (R13), qui n'a écrit ni une preuve ni la grille, reçoit la liste explicite des fichiers (R2) ;
  il **compte**, il n'interprète pas. Il rend un tableau à huit lignes, un état par ligne, puis une seule ligne de porte.
- **« En cours » ou « presque fini »** : n'existe pas. Un critère sans verdict scellé à l'heure de lecture est « non tenté ».
  Aucune preuve de « presque fini » n'est recevable, parce que toute preuve de ce genre demanderait un jugement de degré.
- **Échec contre non concluant** : la distinction existe au niveau du critère (elle décide ce qui est publiable, section 2 (c)),
  pas au niveau de la porte. Une porte « non concluante » serait une porte « on verra » : **non scellable**.
- **R4** : si un ou plusieurs critères passent de « non tenté » à « prouvé » dans les sept derniers jours, le verdict le signale
  en réserve et l'audit de symétrie s'applique au même titre qu'à un résultat négatif trop propre. Cela ne change pas l'état.

## 2. Les options de repli

| option | autorise | interdit | coût | risque de dérive | R1 / R4 / R13 / N-027 | ce qu'on dit au financeur |
|---|---|---|---|---|---|---|
| **(a) report unique et borné** de la lecture (par exemple au 31 décembre) | continuer la phase 0 sur les critères manquants | entrer en phase 1 ; toucher un critère | temps ; calcul sur devis | **fort** : N-027 était déjà un report ; un deuxième report décidé *après* lecture est la « porte de sortie déguisée » type ; borné et décidé *avant*, il est acceptable une fois, pas deux | compatible avec R1, R13 si la grille ne bouge pas ; **tension avec N-027** (« au plus tard fin novembre ») si la *lecture* est déplacée ; aucune tension si la lecture a lieu et que seule la *reprise* est bornée | « one bounded extension, written in advance » |
| **(b) porte non franchie, travail continu sur les critères manquants, sans phase 1** | même chose que (a), mais la porte est *prononcée* fin novembre | phase 1 ; franchissement partiel | temps ; calcul sur devis | **moyen** : sans borne, c'est (a) sans le dire ; avec borne, c'est la forme honnête de (a) | compatible avec les quatre : la lecture a lieu à la date de N-027, le verdict est scellé (R13), la reprise est préenregistrée (R1) | « the gate was read and not passed ; we are finishing the missing criteria under a sealed plan » |
| **(c) bascule vers ce qui ne dépend pas des critères manquants** | (c1) un résultat négatif scellé sur un critère 2, 3 ou 4 devient une note publiable (brief § 1 : « un résultat négatif propre est un livrable ») ; (c2) la piste C commence si ses préalables propres sont prouvés | tout ce qui dépend d'un critère manquant ; toute publication sans GO (nœud) | faible pour (c1) ; devis pour (c2) | **moyen** : (c2) repose sur une lecture du brief (§ 9 « Préalable : préenregistrement de HC1 à HC3 scellé (G0) et GO sur le devis ») qui ne dit pas « G0 franchie » comme le § 8 le dit pour la phase 1 ; cette lecture doit être tranchée **maintenant** par Lazar, sinon le lecteur la tranchera | compatible si (c2) est décidé d'avance ; sinon non scellable | « what does not depend on the missing criteria proceeds ; nothing else does » |
| **(d) arrêt et rapport** | rapport de phase 0 scellé ; livrables existants | tout calcul nouveau ; toute phase | nul | **nul** comme dérive, mais fort comme perte : deux critères prouvés et un financement au 1er décembre jetés sur une échéance interne | compatible avec tout | « the gate failed ; here is the report » — vrai, mais à un fonds qui vient de commencer à payer |

Lecture : (b) est (a) prononcé honnêtement ; (d) est la borne de (b) ; (c1) est un sous-produit automatique ; (c2) est une
décision à prendre maintenant. **La règle recommandée est donc (b), bornée par (d), avec (c1) automatique et (c2) tranché
aujourd'hui.**

## 3. La règle recommandée — clause scellable

**Phrase principale.** « Si, à la lecture de G0 du 30 novembre 2026 (23:59 UTC au plus tard), le verdict R13 scellé ne
déclare pas les huit critères « prouvé », la porte G0 est **non franchie** ; la phase 1 ne s'ouvre pas ; la phase 0 se
poursuit **une seule fois**, sur les seuls critères non prouvés, sous un préenregistrement de reprise scellé et contre-lu
au plus tard le 7 décembre 2026, avec une **seconde et dernière lecture** de G0, par un sous-agent neuf, contre la **même
grille**, au plus tard le **31 décembre 2026 à 23:59 UTC** ; si cette seconde lecture ne déclare pas les huit critères
« prouvé », la phase 0 est **close sur échec**, le rapport de phase 0 est scellé, et G0 n'est plus relue sans une version
nouvelle du programme transmise par Lazar. »

**Conditions (toutes bornées, aucune laissée au lecteur).**
1. Aucun critère ne change de texte, de preuve exigée ni de seuil, ni à la première ni à la seconde lecture ; la grille de
   lecture de G0 (section 4, point 1) est scellée avant le 15 novembre 2026 et sert aux deux lectures.
2. Les critères « prouvé » à la première lecture restent prouvés à la seconde, sauf changement de modèle ou de harnais
   (lui-même un nœud à GO ; sans GO, impossible).
3. Le préenregistrement de reprise ne contient que : les critères manquants, les expériences prévues, leur devis, leur liste
   d'arrêt. Il ne peut ni réinterpréter un critère ni en proposer la réécriture. Toute proposition de réécriture est un nœud
   séparé, hors de la reprise, et ne suspend pas la borne du 31 décembre.
4. Calcul de la reprise : sur devis, GO de Lazar ; le devis est joint au verdict du 30 novembre, pas demandé après. Sans
   GO sous sept jours, la reprise se fait sur processeur seulement.
5. Bascule automatique (c1) : tout critère « non prouvé » par un verdict scellé négatif (et non « non tenté ») produit une
   note de résultat négatif, scellée, jointe au rapport ; sa publication reste un nœud.
6. Bascule (c2), seulement si Lazar la tranche maintenant (section 4, point 3) : la piste C peut s'ouvrir sur GO de devis dès
   que les critères 1, 7 et 8 sont « prouvé », indépendamment des critères 2, 3, 4 et 6, pour les seules expériences que le
   préenregistrement du papier C déclare indépendantes des organismes et des sondes (EC.1 au moins ; EC.2 **SUPPOSÉ**
   dépendant des organismes). Sinon, aucune piste ne s'ouvre avant G0.
7. Ordre de préférence si plusieurs critères manquent : il n'y en a pas à la porte (le chemin est le même quel que soit le
   critère manquant). À la reprise, l'ordre de travail est fixé d'avance par la dépendance, pas par la facilité : 2 avant 3
   (pas de sonde au-dessus du plancher sans organisme à dose-réponse), 2 et 3 avant 4 (même jeu d'épisodes), 2 à 4 avant 6
   (le préenregistrement de G1 cite les instruments), 8 et 7 à tout moment sur processeur.
8. Borne : **un seul** report de la reprise, **aucun** report de la seconde lecture ; date butoir 31 décembre 2026 ; après,
   seule une version nouvelle du programme (docs/, empreinte, décision de Lazar) peut rouvrir G0.
9. Clôture sur échec : le rapport de phase 0 contient les huit états, les preuves scellées, les notes négatives, les dépenses,
   et ce que la proposition financée peut tenir sans phase 1 (à écrire d'avance, section 4, point 6). Il est scellé par le
   sous-agent qui a rendu le verdict, pas par l'auteur des expériences.

**Confiance : moyenne, ≈ 0,6.** Ce qui la limite : (i) la date du 31 décembre est un choix, justifié seulement par la
proposition envoyée (GC fin du mois 2, G1 fin du mois 4 : une G0 fin décembre laisse ces jalons atteignables — **SUPPOSÉ**,
proposition non lue) ; (ii) je ne sais pas si le calendrier des six critères ouverts tient en un mois de plus (le § 4 de
l'entretien dit que le critère 2 « n'a pas avancé ») ; (iii) la lecture (c2) du brief est discutable.

Pourquoi pas plus souple : un deuxième report serait le troisième calendrier de G0 en trois mois (1er novembre, fin novembre,
fin décembre) ; au-delà, la porte ne porte plus rien. Pourquoi pas plus dur : fermer le programme le 30 novembre sur une
échéance interne, le jour avant le début d'un financement, serait une décision de gouvernance prise par une date, pas par
un résultat.

## 4. Ce qui doit être décidé maintenant (avant le 30 novembre, sans quoi la règle est non scellable)

1. **La grille de lecture de G0 v1** — n'existe pas. Pour chaque critère : le ou les fichiers scellés qui font preuve
   (chemin, empreinte attendue ou « à sceller »), le verdict R13 déjà rendu s'il existe (critère 1 : `docs/verdicts/
   verdict-T0.4-critere-1-G0-v3.md`, 63444faa… ; critère 5 : T0.3, à pointer), et pour les six autres la nature exacte de la
   preuve : critère 2, un verdict R13 scellé « dose-réponse mesurée » sur (i) et (ii) ; critère 3, un verdict R13 scellé
   « au-dessus du plancher aléatoire apparié » sur (i) et (ii) ; critère 4, un manifeste de run de la base boîte noire sur
   le même jeu d'épisodes, par action et séquentielle ; critères 6 et 7, préenregistrement scellé + contre-lecture scellée ;
   critère 8, le livrable `etat-de-l-art-verifie` et une table « aucun chiffre non vérifié ». Rédigée par une instance, contre-lue
   par une autre (R2), scellée avant le 15 novembre. Sans cette grille, le lecteur du 30 novembre décide ce qu'est une preuve.
2. **Les trois états par critère** (prouvé / non prouvé / non tenté) et « en cours = non tenté » : à consigner comme décision.
3. **La lecture (c2) du préalable de la piste C** : « G0 franchie » ou « critères 1, 7 et 8 prouvés ». Recommandation :
   critères 1, 7 et 8, pour EC.1 seule au départ, confiance ≈ 0,55 ; défaut si Lazar ne tranche pas : **rien ne s'ouvre**
   avant G0 (la forme la plus prudente, et la seule qui ne lise pas le brief).
4. **Les dates** : lecture 30 novembre 23:59 UTC ; reprise scellée au plus tard le 7 décembre ; seconde lecture au plus tard
   le 31 décembre 23:59 UTC. Un seul jeu de dates, consigné dans `registres/etat.md` et `docs/decisions/`.
5. **Le devis de reprise** : préparé avant le 30 novembre pour les critères encore ouverts à ce moment (il peut être
   conditionnel : « si 2 et 3 manquent, X USD ; si seuls 6 et 7 manquent, 0 USD »), joint au verdict. GO-2026-10-24-05 échoit
   le 30 novembre (R-355) : rien ne couvre décembre aujourd'hui.
6. **Le texte du rapport d'échec** : son plan, écrit d'avance (sections fixes : états, preuves, négatifs, dépenses, ce que la
   proposition financée tient sans phase 1). Écrit avant lecture, il ne peut pas être ajusté au résultat.
7. **Le sous-agent de la lecture** : neuf, d'une autre lignée que l'auteur des preuves si possible (N-052 fait déjà ce choix
   pour la boucle extérieure), instruit par la grille seule.
8. **La phrase au financeur**, décidée aujourd'hui, parce que demain elle sera dite.

## 5. Ce qu'on peut dire demain au financeur

Si Lazar adopte la clause aujourd'hui (une ligne de décision suffit, la grille vient après) :

> « If the gate is not passed on 30 November, phase 1 does not open: the criteria stay as written, we get one bounded
> extension with a final reading by the end of December, and a failure then is reported, not reinterpreted. »

Si Lazar ne tranche pas aujourd'hui, la seule phrase vraie reste celle du point 12 de l'entretien :
« no fallback rule is written yet ».

## 6. Réserves

- Je n'ai pas lu la proposition envoyée au fonds ; la compatibilité de la date du 31 décembre avec ses jalons est SUPPOSÉE.
- Je n'ai pas lu l'état réel d'avancement des critères 2, 3, 4 au-delà du § 4 de l'entretien ; si le critère 2 exige des
  organismes qui n'existent pas, un mois peut ne pas suffire ; la règle le prévoit (clôture), elle ne le résout pas.
- La question demandait un « ordre de préférence si plusieurs critères échouent » ; j'ai répondu qu'à la porte il n'y en a
  pas, et que l'ordre vit dans la reprise (dépendances). Si Lazar veut un ordre de bascule par critère, c'est (c2) qu'il faut
  étendre, et chaque extension est une lecture du brief à trancher d'avance.

Fin de rédaction : Thu Oct 29 09:39:32 UTC 2026.
