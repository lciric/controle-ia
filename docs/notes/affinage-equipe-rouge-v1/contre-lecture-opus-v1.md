# Contre-lecture de `conception-affinage-equipe-rouge-v1.md` — contre-lecteur Opus — v1

**Relecteur.** Session neuve servie par Opus 5.5, d'une autre lignée que l'auteur (Fable 5.1). 28 octobre 2026.

**Fichiers ouverts, et eux seuls.**
- La consigne.
- Le document relu : empreinte vérifiée `789141dbde8b4ef343e08186ccfd5df8bbb703b8e49ae02b4d17535bfbb19f33`, 1 515 lignes.
- Les six fichiers du lot.

Aucun autre fichier, aucun appel réseau, aucune clé. « l. » renvoie aux lignes du document relu.

## Verdict

**Solide avec réserves** : l'architecture est fidèle au brief et couvre ses sept attaques minimales (langage de loi fermé, juge mécanique à processus de pari, gel par le noyau, mémoire par cases interdites, ombres-miroir, tests sain / artefact / exception), mais trois défauts locaux et bloquants — mémoire consultée au seul gel v0, survie qui ne juge pas l'amplitude déclarée, plan de données des témoins non défini — imposent une version 2 ciblée avant de coder la mémoire, le juge et le planteur de témoins.

**Décompte** : 28 constats (3 bloquants, 16 majeurs, 9 mineurs) et 13 attaques manquantes.

## 1. Lecture par point de la consigne

- **Fidélité à la mission.**
  - Les quatre parties du livrable sont là : la boucle (sections 4 à 6), le catalogue (section 7), une garde par attaque avec cas sain et artefact, et ce qui n'est pas durci (section 10). Le test « exception » de 8.2 est un bon ajout.
  - Les sept attaques minimales du brief sont nommées (l. 744-746).
  - Deux manques : la garde de routage n'a pas d'entrée testée (CL-O-08), et une réduction de périmètre n'est pas déclarée (CL-O-18).
- **Écarts déclarés en section 1.** Les sept sont fondés, avec trois nuances :
  - n° 1 sous-estime le débit du canal (CL-O-21) ;
  - n° 2 est conforme à la passation : −log α borne la sévérité par en dessous, par l'inégalité de Ville ;
  - n° 5 voit juste, mais sa résolution repose encore sur des verdicts du juge (CL-O-10).

  Un écart n'est pas fondé au regard du brief : la poussée (CL-O-19).
- **Codabilité.** Le squelette est codable par un autre. Les trous sont en CL-O-03, 05, 06, 13, 14, 15 et 20, et dans deux termes non définis : le « proposeur attributaire » (CL-O-10) et l'identité d'un proposeur (CL-O-12).
- **Catalogue.** Il est riche. Mais les jumelles, une attaque exigée par le brief, restent ouvertes par trois voies (CL-O-01, CL-O-03, AM-O-02).
- **Gardes.** La plupart séparent bien le cas sain de l'artefact. Exceptions :
  - G-E2, dont le test est contradictoire (CL-O-03) ;
  - G-06, dont le cas sain et l'artefact tournent sur deux mondes différents (CL-O-27) ;
  - G-02, qui ne mesure pas ce que l'agent reconnaît (CL-O-07) ;
  - G-08, dont l'ordre des opérations est impossible (CL-O-13) ;
  - les règles de percée, qui ne sont pas des tests statistiques (CL-O-16) ;
  - la garde de routage, absente (CL-O-08).

  J'ai trouvé un seul repli silencieux (CL-O-25).
- **Invariant.** Cinq chemins le touchent : les quatre de CL-O-10 et AM-O-08.
- **Frontière.** Le document ne descend nulle part sous le niveau méthode :
  - aucune condition concrète ;
  - aucun agent construit ;
  - des simulateurs qui truquent des fiches, pas des comportements (l. 1308-1311, 1446-1447).

  Deux trous de conception pourraient pourtant laisser la boucle libre affiner des caractérisations de contournement (CL-O-08, CL-O-09). Je les signale sans les développer.

## 2. Constats

**CL-O-01 — La mémoire n'est consultée qu'au gel v0 — bloquant.**
- *Endroit* :
  - 4.3 (l. 320-323), 4.4 (l. 366-378), 4.6, 4.7 ;
  - 6.10 (l. 723) ;
  - E-01 à E-03.
- *Défaut* : le mouvement `RESSERRER_ESPACE` réduit l'empreinte. Une fiche neuve au v0 peut donc devenir, en cours d'affinage, incluse dans une survivante ou une confirmée. Elle va alors au juge sans contrôle, et elle survit parce que la loi est déjà établie : c'est une promotion sans découverte (AM-O-01). Deux autres effets :
  - deux proposeurs peuvent converger vers la même fiche gelée dans une même génération ;
  - la portée de « fiche gelée » au contrôle v0 n'est pas écrite. Selon la lecture, on admet des paires miroir dans une même génération, ou l'on crée une course au premier arrivé.
- *Correction* :
  - appeler la mémoire dans `verifier_mouvement` (code `REFUSEE_REDITE_AFFINAGE`) et dans `GELER` ;
  - comparer aussi aux versions finales de la même génération ;
  - fixer une priorité déterministe, par empreinte d'engagement ;
  - écrire la portée du contrôle.
- *Tests* :
  - sain : un resserrement qui reste neuf est appliqué ;
  - artefact : un v0 resserré dans le domaine d'une survivante est refusé ;
  - exception : une mémoire indisponible donne `GARDE_ERREUR(memoire)`.

**CL-O-02 — La redite ignore le statut de la fiche antérieure — majeur.**
- *Endroit* : 6.3, règle 1 (l. 584), qui contredit E-05 (l. 1049-1050) et 4.3.
- *Défaut* : « f n'interdit rien que f' n'interdise déjà » est bien une redite si f' a survécu. Si f' est réfutée, c'est l'inverse :
  - une loi plus faible peut être vraie, car elle évite la région violée ;
  - une loi plus forte est réfutée d'avance.

  La règle bloque donc pour toujours les restrictions légitimes, et elle laisse passer les généralisations d'une loi réfutée. De plus, E-05 crée une exception (« redite d'une éliminée autorisée si plus puissante ») que 6.3 ignore.
- *Correction* : une table de décision par statut de f', écrite en 6.3 seulement (E-05 y renvoie) :
  - f' survivante, confirmée ou en cours : redite si E(f) ⊆ E(f') ;
  - f' réfutée ou infirmée : refus si E(f) ⊇ E(f') (code `REFUTEE_PAR_INCLUSION`), libre sinon ;
  - f' retirée, non testable ou refusée : voir AM-O-03.

**CL-O-03 — Dans l'empreinte, le rôle de δ et la comparabilité des cases sont contradictoires — majeur.**
- *Endroit* : 6.3 (l. 576-581) ; `RESSERRER_AMPLITUDE` ; E-02 (l. 1023-1024) ; 6.6, condition 2.
- *Défaut* :
  - **Sens de δ.** À la lettre, la case « Y_i' − Y_i de signe contraire au-delà de δ » rétrécit quand δ croît : un δ plus grand interdit moins. L'artefact de E-02 suppose cette lecture. Le cas sain de E-02 et le menu (monter δ revient à « resserrer ») supposent l'inverse. Si la case est identifiée au seul couple, δ n'entre même pas dans l'empreinte.
  - **CONTRASTE.** « Par paire d'instances (S1, S2) » est ambigu.
  - **MODULATION.** Ses cases sont des couples de couples, de l'ordre de n⁴ : impossible à énumérer.
  - **Lignées.** Un affinage honnête resserre la fille et peut faire passer son contenu sous celui du parent. La condition 2 de 6.6 casse alors la lignée.
- *Correction* :
  - une convention où un δ plus grand interdit un sur-ensemble, par exemple « Y_i' − Y_i < δ » pour le signe + ; δ pris sur une grille ;
  - des cases de CONTRASTE définies sur les couples (i ∈ S1, i' ∈ S2) ;
  - pour MODULATION, un échantillon de cases tiré par graine ;
  - dire sur quelle version on compare le contenu d'une lignée ;
  - refaire les tests de E-02.

**CL-O-04 — La survie ne juge pas l'amplitude déclarée — bloquant.**
- *Endroit* :
  - 5.2 (l. 468-471, 486-490) et 4.2 ;
  - 6.7, témoins faux « amplitude au-dessus de la vérité » ;
  - G-03 et 8.3.
- *Défaut* : le processus de survie `E_surv` est valide sous « aucun effet ». Sa victoire établit un effet non nul dans le signe déclaré, pas un effet d'au moins δ. Le processus de réfutation `E_ref`, lui, teste « effet ≥ δ ». Si l'effet vrai est entre 0 et δ, les deux peuvent franchir leur seuil, et c'est l'ordre du code (la survie d'abord) qui tranche. Trois conséquences :
  - la partie « chiffrée » d'une loi promue n'est pas certifiée. C'est le résultat flatteur que la passation désigne ;
  - selon le constructeur de processus, non spécifié, une part des témoins faux « amplitude gonflée » survivra par construction. La règle de percée de 8.3 arrêterait alors la première expérience ;
  - gonfler δ facilite le contrôle de puissance de 4.2, donc permet un alpha plus sévère, donc une aptitude plus haute.
- *Correction* : écrire ce que chaque statut certifie, par l'une de deux voies :
  - (a) la survie rejette « effet ≤ κ·δ », avec κ fixé ;
  - (b) une suite de confiance à validité permanente, à trois issues exclusives. SURVIVANTE si la borne basse dépasse κ·δ ; REFUTEE si la borne haute passe sous δ ; `AMPLITUDE_REFUTEE`, avec une aptitude nulle, si les deux arrivent.

  Ajouter un plancher δ_min, pour que la réfutation reste atteignable.
- *Tests* :
  - sain : un effet égal à δ survit ;
  - artefact : un effet égal à δ/4 n'est jamais SURVIVANTE ;
  - exception : une forme sans constructeur de processus n'est pas admise.

**CL-O-05 — La « sévérité attendue recalculée » n'est pas définie — majeur.**
- *Endroit* : 4.2 ; 4.4 (l. 373-376) ; 4.5, étape 4 (l. 394-396) ; C-01.
- *Défaut* : les deux lectures possibles cassent la mécanique.
  - Si σ = −log α, aucun resserrement ne la change : l'étape 4 ne retient jamais rien.
  - Si σ est −log de la probabilité simulée de franchissement sous le nul, réduire l'échantillon la fait monter : l'étape 4 retient les restrictions qui vident l'espace.
- *Correction* : séparer trois grandeurs nommées, puis réécrire 4.4 et 4.5 avec elles :
  - l'aptitude, −log α du dessin gelé ;
  - la faisabilité : puissance à δ au moins égale à π_min, et borne sous le nul ;
  - un critère de resserrement, par exemple la croissance attendue du logarithme du processus par grappe, estimée sur le développement.

**CL-O-06 — « Jugée sur ses seules cases nouvelles » n'a pas de procédure dans le juge — majeur.**
- *Endroit* : 6.3 (l. 595-597), D-02, E-02, E-06, F-03 ; à comparer avec `JUGER`, qui teste l'espace entier.
- *Défaut* : quatre gardes reposent sur un jugement restreint au neuf, ou sur un « nul informé qui incorpore la loi connue ». Le juge n'a aucune telle procédure.
- *Correction* :
  - pour TRANSFERT, juger les grappes de l'espace de la fille hors des espaces des parents ;
  - pour INTERACTION, juger le seul terme de modulation ;
  - pour une loi qui en implique une connue, construire un nul « la loi connue tient, rien d'autre », par forme ; à défaut, refuser la fiche (`NUL_INFORME_INDISPONIBLE`).

**CL-O-07 — Le plan de données des témoins n'est pas défini, et leur indistinguabilité n'est mesurée que sur le contenu des fiches — bloquant avant tout proposeur ou affineur servi par un modèle.** Ce n'est pas bloquant pour la première expérience sur le monde jouet.
- *Endroit* : 6.7, 6.10 (l. 721), G-02 (l. 1152), P-6, 4.5, G-H5.
- *Défaut* :
  - **Données.** Un témoin vrai l'est « par construction du monde planté ». Mais sur quelles données l'affiner et le juger ? Sur la banque réelle, sa vérité n'est plus connue. Sur le monde planté, ses lots ont une autre distribution que ceux des fiches réelles.
  - **Reconnaissance.** Le proposeur-affineur sait qu'il n'a pas émis le témoin. Un agent servi par un modèle peut donc reconnaître les témoins et s'y conduire honnêtement seulement là. La qualité mesurée ne dirait alors rien des fiches réelles. Le classifieur simple de G-02 ne voit pas ce discernement.
  - **Pollution de la production.** En production, les témoins entrent dans le paquet, la mémoire et le recombineur comme des survivantes. Des lois plantées engendrent des filles et bloquent des lois réelles ; les proposeurs apprennent le monde planté.
- *Correction* :
  - des générations d'étalonnage entièrement plantées. Elles seules nourrissent la mesure de qualité, la mesure du besoin et le choix de composition ;
  - en production, aucun témoin dans le paquet, la mémoire ou le recombineur ;
  - un affineur instancié à neuf par fiche ;
  - un test de discernabilité **comportementale**, préenregistré : mouvements, lots, exposition et refus comparés entre témoins et fiches réelles (code `TEMOINS_RECONNUS`) ;
  - un monde planté renouvelé à chaque course.

**CL-O-08 — Le routage des fiches de contournement n'a pas de garde testée, et sa règle est incomplète — majeur (frontière).**
- *Endroit* : 6.9, règle 1 (l. 701-705). Il n'y a aucune entrée en section 7, alors que le cadre d'intégration (réserves, point 4) exige une garde de code avec cas sain et artefact.
- *Défaut* : la règle a cinq failles.
  - Elle lit l'espace, pas les variables de la loi (X, Z, S1, S2).
  - Son moment n'est pas dit. Au seul v0, un resserrement peut faire entrer une fiche dans la classe pendant l'affinage libre.
  - Une fille de parents non gouvernés peut tomber dans la classe.
  - « Issue de détection » est trop étroit : le score et le moment de l'alerte sont aussi des sorties du moniteur (l. 96-97).
  - La complétude de la sous-liste repose sur un humain, sans témoin.
- *Correction* : une garde G-K1, inscrite au catalogue.
  - Elle porte sur tous les traits nommés et sur toutes les sorties de moniteur.
  - Elle est réévaluée à chaque mouvement et sur chaque fille (code `ROUTAGE_GOUVERNE`).
  - Tests : un trait de la sous-liste en X, ou ajouté par resserrement, déclenche un refus bruyant ; une sous-liste illisible arrête la génération.
  - Des témoins de routage sont plantés.

  Je ne nomme aucune entrée de la sous-liste.

**CL-O-09 — Les lots de la voie gouvernée peuvent faire de l'affinage une recherche itérative — majeur (frontière).**
- *Endroit* : 6.9, règles 2 et 3.
- *Défaut* : le document ne dit pas si ces lots sont produits avant l'affinage ou à la demande. Produits à la demande, en réponse au resserrement courant, ils feraient de la boucle épisode par épisode une recherche itérative des conditions où un moniteur échoue. Le cadre exclut cela. La même remarque vaut pour la recombinaison gouvernée.
- *Correction* :
  - des campagnes fermées, sous revue, jamais conditionnées aux mouvements ni aux statuts ;
  - un plafond de campagnes par fiche, décidé à une porte ;
  - une recombinaison gouvernée seulement sous revue.

  Je m'arrête au niveau de la règle.

**CL-O-10 — Quatre chemins de la conception ne tiennent pas l'invariant à la lettre — majeur (invariant).**
- *Endroit* : section 1, n° 5 ; 4.5 (l. 404-407) ; G-H5 ; 6.4 (l. 621) ; 3.4 ; 10.2, n° 9.
- *Défaut* :
  - (a) Choisir la composition « sur témoins », c'est sélectionner un affineur sur des verdicts du juge. Que ce soit acceptable est une lecture de l'invariant, donc une décision du directeur.
  - (b) Si le « proposeur attributaire » des filles est celui des parents, ceux qui survivent reçoivent plus de matière. C'est une sélection douce.
  - (c) Le directeur voit les taux réels de promotion par proposeur.
  - (d) Le duel « en fiches promues par dollar » viole l'invariant tel qu'il est écrit. C'est un nœud de décision, pas une question ouverte.
- *Correction* :
  - (a) noter les affineurs par l'**oracle du monde planté** (« la loi gelée est-elle vraie dans le monde ? »), sans passer par le juge ;
  - (b) attribuer les filles par tourniquet journalisé ;
  - (c) sceller les taux réels par proposeur jusqu'à la fin de la course ;
  - (d) porter le duel au directeur.

**CL-O-11 — La correction d'exposition récompense l'opacité — majeur.**
- *Endroit* : 4.6 (l. 414-417, 425-427) ; C-04.
- *Défaut* : l'affineur mécanique, qui déclare sa famille, paie log(1 + nombre de traits). L'affineur servi par un modèle paie log(1 + k), quoi qu'il ait essayé en silence. La pénalité frappe donc le plus transparent et biaise la mesure du besoin contre la voie bon marché. Or l'épreuve fraîche suffit à la validité.
- *Correction* : soit une même mesure pour les deux, tirée du courtier (lots consommés, grappes vues) ; soit l'exposition sortie de l'aptitude et seulement rapportée.

**CL-O-12 — Pas de budget d'erreur global, pas d'identité de proposeur — majeur.**
- *Endroit* : P-5 (l. 272-274), F-07, E-03, 6.8.
- *Défaut* :
  - Le budget α_P vaut par proposeur et par génération. Les fausses survies croissent donc avec le nombre de proposeurs et de générations, alors que les revendications sont celles du programme.
  - « Proposeur » n'est pas défini : le proposeur maison sert deux modèles, et un système publié peut être instancié plusieurs fois. Multiplier les identités multiplie le budget.
  - « Cent fois plus de sévérité » (l. 274) est faux : la sévérité augmente de log 100.
- *Correction* :
  - un proposeur est une configuration enregistrée, avec son empreinte ;
  - un α global par génération ;
  - pour les revendications, un contrôle en ligne du taux de fausses découvertes fondé sur des e-valeurs (procédure à choisir ; références à vérifier).
- *Test* : artefact, un clone de proposeur laisse le budget global inchangé (code `CLONE_PROPOSEUR`).

**CL-O-13 — L'engagement de graine est impossible dans l'ordre écrit — majeur.**
- *Endroit* : 4.6 (l. 421) ; 5.1 (l. 458-459) ; G-08.
- *Défaut* : `GELER` s'engage sur une graine « tirée APRÈS ce reçu ». Et un engagement pris après avoir vu les fiches n'empêche pas de retirer la graine jusqu'à une épreuve favorable.
- *Correction* : un secret s engagé avant la génération ; graine = H(s ‖ racine des empreintes gelées), calculée après le gel collectif ; s révélé après le jugement.
- *Test* : artefact, une graine non dérivable donne `GRAINE_INVALIDE`.

**CL-O-14 — Le nul d'archive est mal défini et peut rendre le juge circulaire — majeur.**
- *Endroit* : 5.2 (l. 473-474) ; 4.2 (l. 309) ; brûlage fiche par fiche (l. 491), contre 5.5 et 6.10.
- *Défaut* :
  - Si l'appariement « à traits égaux » porte aussi sur X, ce nul reproduit l'effet. Le minimum éteint alors la puissance de toute loi vraie.
  - S'il ne porte que sur des traits de nuisance, il suppose une échangeabilité non écrite.
  - Si l'on brûle fiche par fiche, une fiche peut être jugée contre un nul fait de sa propre épreuve.
- *Correction* :
  - nommer les traits appariés ;
  - procéder par permutation conditionnelle par grappe ;
  - geler ce réservoir au début de la génération ;
  - brûler en bloc à la clôture ;
  - exclure ce nul de l'échelle 1 (AM-O-04).

  **Question posée au contre-lecteur (l. 476-477).** Un minimum de processus, chacun valide sous son propre nul, est valide sous la réunion des nuls. Sous toute loi de l'un des nuls, le minimum est dominé par le processus de ce nul, et l'inégalité de Ville s'applique. Trois conditions :
  - la bibliothèque, nuls secrets compris, est fixée avant toute lecture d'épreuve ;
  - chaque élément est valide pour son propre nul ;
  - on prend le minimum des processus cumulés.

  La continuation de 5.4 est valide, elle aussi. Ces deux points ont été vérifiés par raisonnement ; un statisticien doit relire.

**CL-O-15 — Les listes disjointes contredisent le gabarit COMPOSITION — majeur.**
- *Endroit* : H-2 ; 4.1, étape 2 (l. 294) ; C-06. Contre : 6.4 (l. 611-612, 626) et F-04 (l. 1097).
- *Défaut* : COMPOSITION exige qu'une issue soit un trait, ce qui est impossible si les listes sont disjointes. Le test sain de F-04 n'est donc pas constructible.
- *Correction* : une disjonction par fiche, plus une liste des issues admissibles comme traits ; sinon, retirer COMPOSITION.

**CL-O-16 — Les règles de percée et d'audit ne sont pas des tests statistiques — majeur.**
- *Endroit* : B-04, C-03, C-04, F-07 ; 8.3 ; 6.1 ; G-G1 (iii).
- *Défaut* : « promu au-delà de son alpha → arrêt du noyau », sans test séquentiel ni correction pour une vingtaine de classes. Le noyau s'arrêtera alors au hasard. Autre cas : un proposeur honnête qui ne trouve rien a des ombres-miroir aussi vivantes que ses fiches, et passe pour un devin.
- *Correction* :
  - par classe, un processus de pari sur les promotions, avec un niveau d'alarme réparti et préenregistré ;
  - pour les ombres, deux comparaisons : fiches contre ombres, et ombres contre alpha ;
  - un taux de fausse alarme fixé d'avance.

**CL-O-17 — La boucle elle-même n'est pas gelée — majeur.**
- *Endroit* : section 9 ; 8.3 ; 10.1, n° 8.
- *Défaut* : rien n'interdit de re-régler les paramètres après les résultats réels, ni de rapporter une seule course parmi plusieurs.
- *Correction* :
  - chaque course est préenregistrée et scellée avant la génération 0 ;
  - tout changement ouvre une nouvelle course ;
  - un registre en ajout seul garde toutes les courses, et toutes sont rapportées.

**CL-O-18 — Une réduction de périmètre n'est pas déclarée — majeur (fidélité).**
- *Endroit* : 3.2, où la fiche n'a plus de champ « protocole » ; P-1 ; H-3. Contre : passation 2.1, cadre d'intégration section 4, et J-02 (l. 1261).
- *Défaut* : le langage n'exprime ni les « nouvelles pistes », ni les « expériences », ni les « failles du programme ». J-02 cite même une faille que la grammaire ne peut pas écrire. Le choix se défend, mais il est absent de la section 1.
- *Correction* : le déclarer, et dire où ces sorties vivent. Par exemple : des fiches de protocole compilées dans la bibliothèque du juge après revue, comme pour J-01.

**CL-O-19 — Poussée malgré « tu ne pousses rien » — majeur pour la gouvernance, sans effet sur la substance.**
- *Endroit* : note de tête (l. 17-24) ; 10.3.
- *Défaut* :
  - L'écart est déclaré et réversible, mais il n'est pas fondé au regard du brief, qui prime.
  - « Dépôt de travail » est ambigu. S'il s'agit du dépôt de travail du programme, la session neuve avait un droit d'écriture près du matériel en quarantaine.
  - La note a été corrigée par un modèle que le document ne nomme pas.
- *Correction* :
  - le directeur ratifie la branche ou la fait supprimer ;
  - établir quel dépôt et quels droits la session avait ;
  - nommer le modèle qui a corrigé la note, pour vérifier que l'auteur et le contre-lecteur ne sont jamais le même modèle.

**CL-O-20 — Ordre des opérations — mineur.**
- *Endroit* : 4.4 (l. 333), 4.5, 4.7, 5.4, 6.10, P-5.
- *Défauts et corrections* :
  - la condition `|lots_servis| < B` sort de la boucle dès le B-ième lot : séparer les plafonds ;
  - le compteur `k` compte les refus, mais la version ne suit que les mouvements appliqués : la chaîne a des trous ;
  - l'étape 3 de l'affineur mécanique peut soumettre δ' < δ ;
  - la reprise d'une indécise doit court-circuiter `AFFINER` ;
  - 6.10 oublie le statut VERIFIEE ;
  - « fusionnées en un seul pari » n'a pas de procédure.

**CL-O-21 — Le compteur de bits a un périmètre incohérent et aucune borne — mineur.**
- *Endroit* : l. 65 (« je le borne »), P-4, 3.4, 4.8. Or 6.2 diffuse les statuts de toutes les fiches.
- *Correction* : compter tout ce que le paquet transmet, puis fixer un plafond ou retirer le mot « borne ».

**CL-O-22 — La formule du vivier ne correspond pas à une épreuve partagée — mineur.**
- *Endroit* : J-03.
- *Correction* : exiger que le tirage de la génération couvre chaque espace gelé à N_min grappes, plus la confirmation.

**CL-O-23 — MODULATION : effet signé ou en valeur absolue ? — mineur.**
- *Endroit* : l. 191-192.
- *Défaut* : en valeur absolue, c'est un pari à deux côtés caché.
- *Correction* : un effet signé.

**CL-O-24 — « Lignée » n'est pas définie, et le vérificateur est surdimensionné — mineur.**
- *Endroit* : 4.7 ; H-04 ; cadre d'intégration, qui réserve Fable 5.1 au vérificateur alors qu'il sert aussi le proposeur maison.
- *Défaut* : G-H4 refusera ce montage. Cinq des six contrôles du vérificateur sont mécaniques.
- *Correction* :
  - définir la lignée comme la famille de modèles ;
  - confier les contrôles 1 à 5 au noyau ;
  - garder un modèle pour la seule détection d'injection.

**CL-O-25 — Cas non traités à la confirmation et dans les lignées — mineur.**
- *Endroit* : 5.4, 5.6, 6.6, F-01, F-06.
- *Défauts et corrections* :
  - espace vide sur la famille inédite : prévoir `NON_TESTABLE` ;
  - seconde indécision à la confirmation : aucun statut terminal, la fiche ensemencerait indéfiniment. C'est le seul repli silencieux trouvé. Prévoir `NON_CONFIRMEE` ;
  - filles d'une parente devenue infirmée : écrire leur sort ;
  - reprise d'une indécise par un autre proposeur : l'interdire ;
  - parents déclarés à la main : les vérifier ;
  - domaine dérivé d'un prédicat sans effet : normaliser la fiche d'abord.

**CL-O-26 — La section 9 est incomplète — mineur.**
- *Correction* : y ajouter
  - la fraction de l'affineur mécanique ;
  - la taille du jeu d'étalonnage ;
  - la part des témoins par classe ;
  - κ et δ_min ;
  - l'α global ;
  - les niveaux d'alarme ;
  - le seuil r_max des traits substituts.

**CL-O-27 — Le test de G-06 est confondu — mineur.**
- *Défaut* : le cas sain et l'artefact tournent sur des mondes différents. Et l'écart de Goodhart confond « apprendre le juge » avec « loi locale ».
- *Correction* : un seul monde pour les deux, et un témoin « loi locale vraie » pour calibrer l'écart.

**CL-O-28 — Seuls les effets peuvent être promus — mineur.**
- *Défaut* : aucune invariance bien mesurée ne peut être promue. La sélection pousse donc vers le résultat flatteur.
- *Correction* : une forme INVARIANCE, à décider par le directeur.

## 3. Attaques manquantes

**AM-O-01 — Jumelle tardive par affinage.**
- *Attaque* : un v0 large et neuf, ensuite resserré dans le domaine d'une survivante. Il redit une loi vraie et prend l'aptitude d'une découverte.
- *Garde* : la mémoire consultée à chaque mouvement et au gel (CL-O-01), et à la clôture un contrôle `REDITE_TARDIVE` qui annule l'aptitude.

**AM-O-02 — Jumelles entre formes et par traits substituts.**
- *Attaque* :
  - un CONTRASTE (X coupé à la médiane) après un MONOTONE sur X ;
  - ou un MONOTONE sur un trait X' presque colinéaire à X.

  Les cases diffèrent, donc la distance de Jaccard est proche de 1.
- *Garde* :
  - des cases communes (CL-O-03) et des règles d'implication entre formes ;
  - des classes d'équivalence de traits recalculées sur le développement : au-delà de r_max, une seule variable ;
  - un jeu d'étalonnage rééchantillonné sur les traits réels.
- *Test* : un trait X' = X plus un bruit faible donne `REFUSEE_REDITE`.

**AM-O-03 — Squat de miroir et empoisonnement par réfutation.**
- *Attaque* : le signe faux, avec un δ infime. La fiche ne peut plus être réfutée ; elle finit retirée, et son miroir — le bon signe — reste bloqué pour tous. On obtient le même effet avec une fiche non testable, avec un refus pour changement de signe (C-02), ou avec une loi large réfutée (CL-O-02). C'est une arme contre un concurrent.
- *Garde* :
  - un plancher δ_min ;
  - le miroir ouvert aussi après un retrait ou un refus ;
  - jamais de redite contre une fiche réfutée ;
  - en production, les témoins hors de la mémoire ;
  - un audit des fiches qui finissent retirées.

**AM-O-04 — L'épreuve brûlée fuit vers l'affinage par les contrôles du noyau.**
- *Attaque* : les contrôles de 4.2, rejoués à chaque mouvement, simulent sous le nul d'archive, qui est fait d'épreuve brûlée. Chaque « appliqué / refusé » en dépend.
- *Garde* : à l'échelle 1, n'utiliser que des nuls tirés du développement.
- *Test* : un contrôle qui lit l'archive donne `CANAL_INTERDIT`.

**AM-O-05 — Canal auxiliaire du coût.**
- *Attaque* : le champ `cout_mesure` (l. 172) inclut les unités d'épreuve lues, et 6.2 ne le retire pas du paquet. S'il est mis à jour après le jugement, ce que le document ne dit pas, il révèle la force de la preuve.
- *Garde* :
  - imputer le budget déclaré, pas les unités lues ;
  - aucun champ postérieur au gel dans le paquet ;
  - des budgets de génération fixes.

**AM-O-06 — Les familles scellées s'apprennent par les confirmations d'autrui.**
- *Attaque* : une famille n'est « vue » que par lignée (G-07). Or les étiquettes de confirmation sont diffusées à tous, et un proposeur peut aussi épuiser la banque à coups de confirmations.
- *Garde* :
  - une famille lue est brûlée pour tous ;
  - des étiquettes diffusées en différé ;
  - un quota de confirmations par proposeur ;
  - écrire que cette banque est distincte de toute famille réservée à l'évaluation finale. Le cadre d'intégration (section 8) associe la confirmation à une « famille tenue à l'écart » : si c'est le même objet, la boucle le consomme.

**AM-O-07 — Double chance à la confirmation.**
- *Attaque* : la seconde tentative de 5.6, faite sur une famille nouvelle, donne deux tests pour un seul alpha.
- *Garde* : continuer le même processus, par produit des e-valeurs.
- *Test* : un processus remis à 1 donne `REPRISE_INVALIDE`.

**AM-O-08 — Les mainteneurs règlent le proposeur maison à partir de l'archive : effet de Goodhart par le développeur.**
- *Attaque* : d'après le cadre d'intégration (section 9), la même lignée semble coder la boucle et servir le proposeur maison. Si c'est le cas, elle peut retoucher ses invites à partir de ce qu'elle lit dans l'archive, ce qui revient à sélectionner un agent sur le score du juge. G-H1 ne le voit pas.
- *Garde* :
  - une empreinte de toute la configuration, scellée par course ;
  - tout changement crée un nouveau proposeur ;
  - les mainteneurs sont aveugles aux nombres scellés et aux témoins ;
  - l'invite est construite depuis le seul paquet, avec journal de H(gabarit ‖ paquet) ;
  - la clé du juge reste hors de leur portée.
- *Test* : une invite divergente donne `INVITE_DIVERGENTE`.

**AM-O-09 — Traduction créatrice pour les systèmes publiés.**
- *Attaque* : si un modèle traduit leurs sorties en fiches, il devient un proposeur caché, et la découverte est mal attribuée. Le document ne parle pas de traduction.
- *Garde* :
  - une traduction mécanique si possible ; sinon faite par une lignée distincte, journalisée et vérifiée ;
  - les fiches traduites comptées à part ;
  - la dérive mesurée sur des idées plantées.

**AM-O-10 — Passager clandestin entre proposeurs.**
- *Attaque* : adopter les filles d'autrui, ou reprendre ses indécises, pour être promu sans découverte propre.
- *Garde* :
  - des îles pour toute comparaison ;
  - un crédit partagé ;
  - la reprise d'une indécise réservée à son auteur.

**AM-O-11 — Canal caché et injection entre proposeurs.**
- *Attaque* : la prose des énoncés et les constantes libres passent d'un proposeur aux autres. La garde A-05 ne protège que le juge et le vérificateur.
- *Garde* :
  - un énoncé re-rendu à partir de la loi formelle, par un gabarit neutre ;
  - des constantes quantifiées ;
  - un débit compté.

**AM-O-12 — Sonder la mémoire par des soumissions refusées.**
- *Attaque* : une fiche refusée n'entre pas dans la mémoire et ne compte pas dans F_max (E-05). Le refus devient une requête gratuite.
- *Garde* : toute soumission compte dans Q_max, pour tous les proposeurs.

**AM-O-13 — Coïncidence par a priori partagés.**
- *Attaque* : la séparation d'auteurs empêche de *lire* les gabarits, pas de les *partager*. Un constructeur de monde de la même famille que le proposeur plante ce que ce dernier devine. Et pour un proposeur modèle, « hors gabarit » n'est pas un ensemble fini.
- *Garde* :
  - des lois plantées tirées au hasard sur tout le langage ;
  - la distribution des propositions estimée sur un monde leurre (sur devis) ;
  - des taux rapportés par strate de probabilité a priori ; seule la strate improbable compte.

## 4. Les cinq priorités

1. **Réparer la mémoire** (CL-O-01, 02, 03 ; AM-O-01 à 03) :
   - consultation à chaque mouvement et au gel ;
   - décisions selon le statut ;
   - convention de δ ;
   - cases communes à toutes les formes.
2. **Fixer la sémantique du juge** (CL-O-04, 05, 06, 14 ; AM-O-04) :
   - ce que chaque statut certifie sur δ ;
   - des grandeurs nommées ;
   - une procédure de jugement sur le neuf ;
   - un nul d'archive défini et réservé au juge.
3. **Décider le régime des témoins** (CL-O-07) avant tout modèle :
   - des générations d'étalonnage plantées ;
   - un test de discernabilité comportementale.
4. **Fermer la frontière en code** (CL-O-08, 09) :
   - une garde de routage testée sur toutes les variables ;
   - des données gouvernées par campagnes fermées.
5. **Tenir l'invariant et geler la boucle** (CL-O-10, 12, 17 ; AM-O-08) :
   - noter par l'oracle du monde planté ;
   - un rapport aveuglé ;
   - un budget d'erreur global ;
   - une course préenregistrée et des configurations scellées.

## 5. Proportion et faisabilité

- **Surdimensionné** :
  - le vérificateur servi par un modèle ;
  - le proposeur permuté, qui double les ombres-miroir ;
  - toutes les familles d'artefacts à chaque génération, alors qu'une rotation suffit ;
  - quatorze statuts.
- **À construire d'abord.** L'ordre de 8.4 est bon. J'y mettrais en tête :
  - l'oracle du monde jouet ;
  - la sémantique de δ ;
  - la mémoire corrigée ;
  - le test de percée ;
  - la garde de routage.

  Puis la première expérience (8.3), en mécanique seulement.
- **Peut attendre** : le recombineur modèle, la récompense d'héritage, l'affineur servi par un modèle et les systèmes publiés.
- **À mesurer d'abord** : la perte de puissance (10.1, n° 5). La simulation de 4.2 ignore les nuls secrets et se montre donc optimiste.

## 6. Section 10 de l'auteur

Je suis d'accord avec les onze points :
- le n° 4 tient (CL-O-14) ;
- les n° 7 et 8 se durcissent en partie (AM-O-11, CL-O-10).

Il y manque :
- le régime des témoins ;
- la sémantique de l'amplitude ;
- la mémoire consultée au seul v0 ;
- l'erreur à l'échelle du programme ;
- la confiance dans l'opérateur du noyau et dans les mainteneurs ;
- le gel de la boucle ;
- les a priori partagés ;
- l'apprentissage des familles ;
- la complétude de la sous-liste « conditions adversariales » ;
- une hypothèse, non un fait : des fiches devenues publiques pourraient entrer dans l'entraînement de futurs modèles.

## 7. Ce que je n'ai pas pu vérifier

- La poussée : quel dépôt, quels droits, et quel modèle a corrigé la note de tête.
- Si la chaîne existante a déjà un langage formel, un juge mécanique et une empreinte prédictive (H-3, H-4, H-9).
- La constructibilité de `E_ref` pour chaque forme, et la puissance réelle de l'ensemble.
- Les deux renvois absents du lot.
- Les formats de sortie des systèmes publiés.
- Les références de contrôle en ligne du taux de fausses découvertes.
- Le minimum et la continuation des processus de pari : établis par raisonnement seulement.
