# Contre-lecture n° 8 — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes), v8 « économe »

## Identité

Relecteur **neuf (R2)**. Je n'ai écrit ni ce préenregistrement (v1 à v8), ni le code du noyau, ni les lanceurs et leurs
essais, ni les scripts de scellement, ni aucune contre-lecture ou revérification précédente.

Périmètre : ce que la v8 change par rapport à la v7, que la contre-lecture n° 7 a jugée « scellable ». Cela couvre le
texte, le diff du code de `bef2c2f` à `5d1d4fd` (R-395, R-396, R-398, R-402), le lanceur v5 et ses essais, le script
de scellement v8, et les risques nouveaux que ces changements apportent. Je ne refais pas les contre-lectures n° 1 à 7.

J'ai lu seulement les pièces du dossier. Je n'ai fait aucun appel payant ni aucun accès réseau. Je n'ai lu ni affiché
aucune clé ni variable de clé, je n'ai lancé aucun sous-agent et je n'ai rien écrit dans git. Je n'ai modifié aucune
pièce : les essais ont tourné dans une copie de l'arbre, placée dans mon dossier temporaire.

## Heures (UTC)

- Début : 2026-10-25 09:28:02 (`date -u`).
- Fin : 2026-10-25 10:08:43 (`date -u`).

## Texte relu et empreinte

- `pieces/gradient-etape1-sondes-v8.md`. Les marqueurs `<<…>>` de scellement ne sont pas remplis, ce qui est attendu.
  - sha256 = `4c98ed5123bbe60d0fabf084340ae705464993027be4535915b27aa7bb2d1995`.
  - Le compagnon `.sha256` concorde.
- `EMPREINTES-pieces.txt` : 237 sur 237 OK. Aucun fichier du dossier n'est hors de cette liste, à part la liste
  elle-même.
- La v7 de référence (`versions-precedentes/gradient-etape1-sondes-v7.md`) a l'empreinte `84708a92…`, celle que cite la v8.

## VERDICT : **« scellable après corrections »**

Compte par gravité : **0 bloquante, 1 majeure, 7 mineures, 4 de forme** (CL8-01 à CL8-12).

Ce qui est vérifié et rejoué :
- La v8 ne change ni la prédiction, ni le seuil, ni la table de lecture : ces sections sont identiques octet pour
  octet. Elle ne change pas non plus la métrique principale (R1, voir le point 3 du tableau).
- Les entrées des deux bras restent identiques sous la question de `c001`, de bout en bout.
- Les quatre changements du noyau (trois corrections et le contrat) sont éprouvés : essais et banc de mutation
  rejoués.
- Le script de scellement v8 fait ce qu'il dit : scellement à blanc, un cas sain et treize artefacts.

Ce qui manque avant le scellement : la v8 ajoute à la conception du bras A une question qui nomme le service
d'entraînement et invite à concevoir les sondes. Cette question interagit avec le traitement, dans le sens prédit, et le
texte ne le dit pas (CL8-01, majeure).

Corrections attendues avant le scellement :
- CL8-01 : une limite à écrire au corps du texte, et un choix de Lazar.
- De préférence aussi CL8-02 (nommer le mécanisme, rapporter les statuts des appels) et CL8-08 (trancher).
- Les autres remarques se corrigent ou s'acceptent comme réserves consignées.

Mécanique du script de scellement : il ne scelle que le texte relu (`4c98ed51…`). Toute correction du corps donne donc
un brouillon nouveau, à faire relire selon votre pratique. Le champ « traitement » de l'entrée 8, que le script insère
sans toucher au reste, peut porter des réserves acceptées. Il ne suffit pas pour CL8-01 : la limite doit se lire là où
H-G1 est définie.

## Points vérifiés et preuve rejouée

| # | point | résultat | preuve rejouée |
|---|---|---|---|
| 1 | Intégrité des pièces | conforme | `sha256sum -c EMPREINTES-pieces.txt` : 237/237. v8 `4c98ed51…`. v7 `84708a92…` (= cité). Rapport n° 7 `624df897…` (= cité). |
| 2 | Diff du texte v7 → v8 | conforme | `diff -u` recalculé = `diff-texte-v7-v8.patch` (identique). |
| 3 | R1, section par section | tenue (nuance CL8-09) | Comparaison automatique des sections. **Identiques** : Prédiction chiffrée, Seuil, Critères de lecture gelés. **Hypothèse** : seule H-C (descriptive) gagne la question de `c001` ; H-G1, H-G0, H-G2, H-G3 inchangées. **Métrique** : (4) décrit enfin la règle de CL5-07 telle que le code l'applique et ajoute R-395 ; (6) ajoute l'héritage de la question ; score, unité, statistique et intervalle inchangés. **Plan** : points 2, 3, 4, 5 (entrée 8), 8, 10, 14 (nouveau). **Liste d'arrêt** : lignes ajoutées ou étendues, aucune retirée sans remplaçant. `analyse_gradient.py` et `analyse.py` ont les mêmes empreintes qu'en v7. |
| 4 | Code au commit cité | conforme | Les 17 empreintes de fichiers citées sont recalculées. Arbre du noyau (algorithme de `boucle.empreinte_arbre`) : `d5d0efcc…` = cité. Les 12 fichiers dits « inchangé » sont absents du diff, et 11 d'entre eux ont les empreintes déjà citées en v7 (`question.py` n'y était pas cité). Les objets git d'après le diff = fichiers des pièces (6/6). |
| 5 | Essais de la v8 et essais liés | 4/4, 20/20 | Copie de l'arbre, `/opt/essaim-m3-venv-v1/bin/python -B`, `ESSAIM_M3_COLLISIONNEUR` vers le collisionneur des pièces. `test_r395…`, `test_r396…`, `test_r398…`, `test_r402…` : 4 passed. Vingt essais liés (import du bras apparié, crédit, plafonds, question ouverte, extrait mécanique, `cl5_03`…) : 20 passed. Suite complète non rejouée (sortie fournie : 137 passés, 3 désélectionnés). |
| 6 | Mutations de la v8 | conforme | `muter_v8_v1.py` rejoué : témoin vert, quatre mutants rouges (= sortie fournie). Comptes : 12 + 4 + 1 + 4 = 21. Définitions d'essais : 123 + 17 = 140 = 137 + 3. |
| 7 | Symétrie de la question, de bout en bout | conforme (entrées) | Simulation sans réseau : A avec `--question-ouverte … --question-ouverte-aux c001`, puis B par `--depuis A --entrainements-max 0`. Résultats : 28 fichiers des vues des rondes identiques en chemins et en contenus. `reponse-question.md` est à `c001/` (racine) et à `c001/travail/` dans les deux vues, absent à `c002`. La question est dans le contexte de `c001` seulement ; `question_ouverte` vaut null à g000 et g001 dans les deux bras. Historique identique. La question est au manifeste de A seulement, que les organismes ne lisent pas. |
| 8 | Lanceur v5 : empreintes et diff | conforme | `e0c9f8ce…` (lanceur) et `9588fd16…` (essais) = cités = compagnons. Diffs v4 → v5 recalculés = patches fournis. Chaque ligne changée correspond à un changement dit. Aucun essai du v4 retiré (`go-refuse-$g` scindé en deux). Le v4 lisait bien `prereg/gradient-etape1-sondes-v5.md` (défaut décrit). |
| 9 | Plan, point 3 et point 8, contre les lignes réelles | conforme | Options communes, A_r, B_r, répétition et répétition B du texte = lignes des essais `sain-A1`, `sain-B1-apres-A1`, `sain-repetition`, `sain-repetition-B` (aux valeurs factices près). Décalages 100 à 600, plafonds 360, 190, 40 et 10, 5 et 3 USD par génération, 12 et 2 USD par ronde. |
| 10 | Essais du lanceur | conforme (sortie) | 75/75 (`7112f7fc…` = cité), cinq en mode réel. Les noms d'essais cités par la Liste d'arrêt sont tous dans la sortie, et les 51 essais pytest cités sont tous définis. Je n'ai pas pu les rejouer : ils exigent le vrai dépôt. |
| 11 | Porte de la répétition, « question à c001 et nulle part ailleurs » | conforme | Code extrait tel quel du lanceur et rejoué sur les extraits factices des essais. Le cas sain est vrai. Les artefacts « aussi à g000 », « non posée » et « posée à c002 » (ajouté par moi) sont faux. Mutant sans la condition : les trois artefacts passent, donc l'essai détecterait le retrait. La structure des extraits factices est celle d'`extrait_mecanique.extraire` (lu). |
| 12 | Test de dépense (statut `OK` et jetons de sortie > 0) | logique juste, **sans essai** (CL8-03) | Code extrait tel quel, exécuté contre une doublure sans réseau du collisionneur : vrai code, appelants remplacés. `OK` donne le code 0. Donnent le code 1 : jetons 0, crédit épuisé sous HTTP 200, `TRONQUE`, `VIDE`, modèle non conforme, une seule espèce en HTTP 402. La clé `sortie` de `usage` est bien celle du collisionneur. |
| 13 | Script de scellement v8 | conforme | Scellement à blanc dans un faux dépôt : `prereg.py` des pièces, doublures minimales de `gardes.py` et `scellement.py`, absents des pièces. **Cas sain** : les cinq marqueurs sont remplis et l'entrée « Contre-lecture 8 » est trouvée et remplacée. E est entier et inférieur à 2^128. Les graines valent `SeedSequence(E).spawn(3)` et `generate_state(1, uint64)[0]`. Les sept valeurs littérales sont en une seule occurrence. Le validateur ne relève rien, le compagnon est conforme, et le code du lanceur relit les sept valeurs. **Refus pour la bonne raison** : lanceur qui lit `…-v7.md` ; lanceur au bon `PREREG=` mais d'empreinte non citée ; deux lignes `PREREG=` ; sortie sous un autre nom ; sortie hors du dépôt ; brouillon différent du texte relu ; marqueur en double ; marqueur inconnu restant ; entrée 8 altérée ; `graine_1 = 7` en double ; `question_c001_sha256` en double ; valeur littérale glissée dans un champ libre ; sortie existante (R12) ; rapport de même empreinte que le texte (validateur : sortie supprimée). Aucune graine affichée ni gardée : sortie détruite. |
| 14 | Chiffres et renvois | conforme (sauf CL8-11, CL8-12) | Vivier, contre le n° 35 § 1 : 786, 755, 20, 7, 4, 249, 194, 0,7968 ; 755 = 786 − 20 − 7 − 4 ; 249/755 fait un tiers. Bornes : 1 150 = 2×360 + 2×190 + 40 + 10. Heures : 03:54–04:06 = rapport n° 7 ; 07:49–07:56 = R-391 ; 08:03 = R-392 ; 09:13 = R-403, R-404 ; 09:58 heure de Paris = 08:58 UTC, avant l'envoi du n° 36 à 09:06 UTC. GO-05 étendu (R-403) ; GO-07 échoit le 26 octobre. Les décisions citées (R-391 à R-405) concordent. |
| 15 | Pièce de la question | conforme | `a54da93e…` = valeur littérale du texte = compagnon. Ni retour chariot ni marque d'ordre d'octets, donc l'empreinte que le noyau calcule sur le texte lu sera la même. 3 488 caractères, sous la limite de 20 000. |
| 16 | Imputation des tests de dépense | conforme | `GO_CONTROLE=GO-2026-10-24-05`. La ligne d'extension de GO-05 est datée du 25 octobre, échéance le 30 novembre. `go_id` est écrit au journal de l'appel. Plafond de l'appelant : 0,50 USD, pire cas d'environ 0,06 USD pour trois appels à 512 jetons. |

## Remarques

### CL8-01 — majeure — la question de `c001` interagit avec le traitement, dans le sens prédit, sans que le texte le dise

**Emplacement.** Métrique : l. 242-243 (« H-G1 mesure donc… »), (6) l. 266-268, (7) et (8) l. 269-277. Plan, point 14
(l. 593-606). H-C (l. 197-199). Pièce `question-apprendre-structure-entrainement-generations-organismes-v2.md`.

**Constat.** La question est posée à `c001`, dans le seul bras où le service d'entraînement est servi. Elle décrit ce
service : « (A) des sondes sur les activations internes … dont tu conçois la perte, l'architecture, la couche lue et
les données (primitives `entrainer` et `predire` de ton contrat) ». Elle annonce aussi un adaptateur (B). Au point 3,
elle demande « comment tu concevrais (A) … ce que chacun t'apporterait et comment tu le mesurerais ».

Le bras B hérite de la trace (contexte, réponse) mais pas du service. La symétrie que revendiquent R-393 et la
Métrique (6) est une symétrie d'**information**, pas une neutralité d'**effet**. Une génération 0 poussée dès `c001`
vers les sondes dépend davantage du service. Sans lui, dans B, elle reçoit `INDISPONIBLE` et perd de la couverture :
- entre 80 et 100 %, les tâches manquées sont des erreurs dans le sens prédit (7) ;
- sous 80 %, les paires sont coupées (8).

L'effet ne peut pousser que vers « confirmé » ou vers « non concluant », jamais vers « réfuté » (R3, R4). Sur le fond,
la question va aussi contre la consigne « ne lui suggère rien » de la conception (24 octobre, 20:42), sauf si la
décision 1 (a) de Lazar l'écarte expressément pour cette question.

**Preuve.**
- La pièce (`a54da93e…`), lignes 10 à 15 et 29 à 30.
- Point 7 du tableau : les entrées sont identiques dans les deux bras. L'asymétrie ne vient donc pas des entrées ; elle
  vient de l'interaction entre la question et la présence du service.

**Correction proposée.**
1. Dire la limite avant la course : au corps du texte, à la suite de « H-G1 mesure donc… », au point 14 et dans H-C.
   Formulation possible : « Depuis la v8, la conception de A s'ouvre sur une question qui nomme les sondes servies et
   demande comment l'organisme les concevrait. Elle peut accroître la dépendance de la génération 0 au service, donc
   Δ dans le sens prédit par la couverture et les demandes `INDISPONIBLE` de B, ou des paires coupées. Le rapport
   descriptif (couverture, `INDISPONIBLE`, Δ sur les tâches répondues par les deux bras) et la répétition B le
   montrent. »
2. Soumettre le choix à Lazar en une ligne :
   - (a) garder la question à `c001` des courses décisives, limite dite. Recommandé si l'objet de la question prime.
   - (b) la poser à la seule répétition, ou dans une course hors de H-G1. Cela retire l'interaction.

### CL8-02 — mineure — les coupures par la réflexion sous 4 096 jetons pèsent sur le chemin de réponse de B, et ne sont ni nommées ni attribuées

**Emplacement.** Métrique (7) (l. 269-273). Plan, point 4 (l. 435-439) et point 8 (l. 492-498). Liste d'arrêt
l. 649. `analyse_gradient.causes_absences`.

**Constat.** La v8 dit que le plafond de 4 096 jetons comprend la réflexion (R-398) et que la part d'appels coupés
n'est pas mesurée (limite dite). Elle ne dit pas que ce risque pèse surtout sur B : B répond à chaque tâche par un
appel, A peut répondre par ses sondes. Un appel coupé (`TRONQUE`) ou vide (`VIDE`) rend un texte vide et reste payé.
Il fait donc une absence de B, comptée comme une erreur entre 80 et 100 % de couverture. Avec quelques dizaines de pour
cent d'appels coupés, c'est un Δ dans le sens prédit du même ordre que l'effet prédit. Trois manques :
- (a) Le rapport descriptif gelé n'attribue pas cette cause. `causes_absences` rend le statut, les refus du noyau,
  `INDISPONIBLE`, le nombre de réponses, les appels et le coût, mais pas les statuts des appels.
- (b) La vérification humaine ne porte que sur les répétitions, que sur les espèces Anthropic, et seulement au-delà de
  50 %. Ce seuil n'est pas justifié : 20 à 50 % d'appels coupés passeraient sans être soumis à Lazar. C'est une
  vérification humaine ; le seuil n'y ajoute rien.
- (c) Argon n'est pas regardé. Gemini compte aussi sa réflexion dans les jetons de sortie (`usage` du collisionneur :
  candidats et pensées). Ses parts « thought » ne sont rendues que sur demande, et l'appelant ne la fait pas
  (`generationConfig` sans configuration de réflexion). Le compte `reflexion_par_espece` d'Argon peut donc rester à 0
  par construction. C'est à vérifier.

**Preuve.**
- `analyse_gradient.py`, l. 301-313.
- Contrat § 3 : texte vide hors `OK`.
- Collisionneur : `appeler_gemini` et `lire_reponse_gemini`.
- Porte du lanceur v5, l. 392-405.

**Correction proposée.**
- Nommer le mécanisme en (7).
- Rapporter, pour chaque course décisive, par paire et par bras, les statuts des appels par espèce et les appels qui
  ont réfléchi. Ils sont déjà dans l'extrait mécanique scellé de chaque course : c'est un simple ajout au rapport, sans
  seuil.
- À la répétition, soumettre à Lazar les taux par espèce quels qu'ils soient, Argon compris, ou justifier le seuil de
  50 %.

### CL8-03 — mineure (R5) — la garde du test de dépense n'a ni cas sain ni artefact dans la suite d'essais

**Emplacement.** Liste d'arrêt l. 660. Lanceur v5, l. 301-317. `essais_lanceur_etape1_v5.sh`.

**Constat.** La v8 change cette garde : elle exige maintenant un statut `OK` **et** des jetons de sortie, y compris
contre un crédit épuisé sous HTTP 200. Pourtant elle n'est éprouvée par aucun essai. Elle ne s'exécute qu'en mode réel,
et les cinq essais réels s'arrêtent avant elle. La ligne de la Liste d'arrêt ne cite aucun essai. Le défaut de chemin
du lanceur v4 montre ce qu'une garde jamais exercée peut cacher.

**Preuve.** Mon rejeu (point 12 du tableau) montre que la logique est juste. Il ne tient pas lieu d'essai dans la
suite du dépôt.

**Correction proposée.**
- Ajouter un cas sain et ces artefacts à une suite d'essais nouvelle (R12), sur le modèle de la porte : code extrait
  tel quel du lanceur, `ESSAIM_M3_COLLISIONNEUR` pointé vers une doublure.
- À défaut, écrire dans la ligne de la Liste d'arrêt que la garde n'est éprouvée que par lecture et par ce rejeu, et
  que son premier cas sain réel sera le test de dépense de la répétition.

Accessoire, de forme : le refus d'une pièce de question qui serait un lien symbolique (lanceur l. 160 et l. 171) n'a
pas d'artefact non plus.

### CL8-04 — mineure — l'hôte « conteneur de la session » (R-405) apporte des risques non dits

**Emplacement.** Plan, point 3, « Hôte » (l. 397-415). Métrique (5). R-405, R-407, GO-2026-10-25-01.

**Constat.** Trois risques.

(a) **Cohabitation.** Le second pilote (GO-2026-10-25-01) tourne dans le même conteneur, « avant les courses
décisives » d'après R-407, qui en donne la raison : la charge du processeur. Ni la v8 ni le lanceur n'exigent :
- qu'il soit fini avant le départ de A_1 et A_2 ;
- que son `--decalage-uid` soit hors de 100 à 600. Le noyau accepte tout multiple de 100 entre 0 et 900, et le lanceur
  v5 ne connaît que ses propres courses.

Un chevauchement ferait peser une charge du processeur sur un seul bras. Un même décalage donnerait aux lignées des deux
expériences les mêmes utilisateurs et les mêmes groupes. Les espaces que le pilote laisse sous la racine des espaces
des organismes deviendraient lisibles par chemin. En pratique, ils restent hors d'atteinte : l'espace en 0711 ne se
liste pas et l'empreinte de la racine ne se devine pas. Mais l'assertion « aucune voie commune … hors des vues » du
point 13 ne serait plus vraie. Les réveils de la session chargent aussi le conteneur.

(b) **Mandataire.** La session sort par un mandataire qui intercepte TLS ; le lanceur garde `HTTPS_PROXY` et les
certificats. Si le mandataire rend lui-même un HTTP 405 ou 407, `echec_exterieur` ne le classe pas comme extérieur :
la liste est 401, 402, 403, 408, 409, 429 et 5xx. L'échec compterait comme une erreur de l'organisme et échapperait à
la règle des pannes. Les refus au niveau de la connexion au mandataire, eux, sont bien extérieurs.

(c) **Perte du disque.** « Le dossier des courses et ses portes n'en sortent pas. » Si le conteneur est perdu, et non
seulement redémarré, l'archive de A_r disparaît : B_r et l'audit deviennent impossibles. Aucune copie scellée hors du
conteneur n'est prévue, alors que le pilote du 25 octobre a poussé ses sorties (R-391).

**Correction proposée.**
- Écrire au point 3 que le second pilote est fini avant le départ de A_1 et A_2, avec un constat consigné, et qu'il
  prend des décalages hors de 100 à 600 (700, 800). Écrire aussi qu'aucune autre course ne tourne pendant A_r et B_r.
- Pour (b) : dire la limite, ou ajouter 405 et 407 aux codes extérieurs avant le scellement. C'est un changement de la
  règle gelée des pannes ; il faut le dire.
- Pour (c) : prévoir une copie scellée des sorties de chaque course hors du conteneur (sans la banque), ou dire la
  limite.

### CL8-05 — mineure — après le 26 octobre, aucune ligne valide du registre des GO ne nomme les clés employées

**Emplacement.** Plan, point 3, « Clés » (l. 361-371). Documents (l. 159-167). `registres-extraits/go-extrait.md`.

**Constat.** La v8 cite « Clés (GO-2026-10-24-04 ; R-394) ». Or :
- GO-04 ne nomme que `RR_ANTHROPIC_API_KEY`, avec `_2` en réserve, et impute la dépense à « l'espace de travail de ces
  clés » ;
- GO-05 renvoie à GO-04 et à `GEMINI_API_KEY` ;
- `GEMINI_API_KEY_2` n'est nommée que par GO-07, qui échoit le 26 octobre. C'est précisément la raison de R-403, mais
  la v8 ne l'a traitée que pour les tests de dépense ;
- `_3` et `_LUC` ne sont nommées que par R-394, qui est une décision, pas une ligne de GO. Le nom « LUC » laisse penser
  à un autre compte ou à un autre espace de travail, que la dépense débiterait sans que le registre des GO le dise.

**Correction proposée.**
- Demander à Lazar une ligne d'extension de GO-04, comme R-403 l'a fait pour GO-05. Elle nommerait
  `RR_ANTHROPIC_API_KEY_3`, `RR_ANTHROPIC_API_KEY_LUC`, `GEMINI_API_KEY_2` et l'espace de travail ou le compte de
  chacune.
- Consigner, par course, dans `registres/depenses.md`, le nom de clé (`<course>.cles.txt`) et l'espace débité.

### CL8-06 — mineure — avec la recharge automatique, la borne de 1 150 USD vaut par course, pas pour l'étape

**Emplacement.** Plan, point 3 (l. 381-389). Liste d'arrêt l. 661. Annexe.

**Constat.** « Au plus 1 150 USD pour l'étape » suppose une seule exécution de chaque course, dans un seul dossier. Les
gardes du lanceur (sortie neuve, verrou, `cles.txt`, ligne d'engagement) sont propres à un dossier. Rien n'empêche une
seconde série dans un autre dossier, par exemple après une perte du conteneur : « aucune relance » est une règle
humaine. GO-05 n'a pas de plafond, et la recharge retire le dernier frein extérieur. Le n° 36 § 4 demandait de
consigner le plafond de recharge mensuel de la console, s'il existe ; la v8 ne le fait pas.

**Correction proposée.**
- Dire que la borne vaut par course et repose sur la règle « aucune relance » et sur l'engagement consigné.
- Consigner le plafond de recharge, ou son absence, sur le mot de Lazar.
- Au mieux, ajouter un engagement à usage unique : une ligne de départ par course dans `registres/depenses.md`, avec le
  chemin du dossier, vérifiée avant l'appel payant.

### CL8-07 — mineure — le § 3 du contrat (R-398) sert aux organismes des chiffres sans source citée

**Emplacement.** Plan, points 2 et 4 (l. 340, l. 435-439). `contrat.py`, § 3 (R-398, R-400).

**Constat.** R-398 consigne un contrat qui parle « comme un fait mécanique et sans valeur conseillée ». Le § 3, servi
aux organismes des deux bras, ajoute pourtant : « à 512 et 640 jetons, la plupart des appels … coupés ou vides ; des
appels à 64 000 jetons ne l'ont pas été ». Trois problèmes :
- (i) « 64 000 » n'a pas de source dans les pièces. R-400 donne 640, 512 et 1 200 pour le pilote ; 1 200 est omis.
- (ii) Sous `--max-tokens-appel 4096`, ce chiffre désigne un plafond que l'organisme ne peut pas obtenir, et il peut
  l'inciter à demander le plus possible.
- (iii) Le paragraphe ne vaut que pour les espèces Anthropic, alors que la réflexion de Gemini compte aussi dans les
  jetons de sortie.

C'est symétrique entre bras, donc sans biais de Δ. Mais c'est un contenu servi aux organismes que le texte ne cite pas
et ne rattache à aucune pièce.

**Correction proposée.**
- Rattacher chaque chiffre à une pièce, ou les retirer, Lazar ayant dit « sans valeur ».
- Citer le paragraphe au point 2 du Plan.
- Vérifier, pour Argon, si la réflexion compte dans `maxOutputTokens`, et le dire au contrat si c'est le cas, sur le
  mot de Lazar.

### CL8-08 — mineure — un changement de la lecture de H-G1 est annoncé pour « après la v8 »

**Emplacement.** Absent du texte. Canal, n° 35 § 3.

**Constat.** « conv-audit » annonce qu'elle proposera « après ta v8, pas avant » d'écrire un plancher de bruit dans la
lecture de H-G1 (σ d'environ 5 à 6 points), et des témoins de sortie. Après le scellement, changer la lecture serait un
écart à un préenregistrement scellé, donc un nœud de décision. Ajouter des témoins descriptifs passerait par un
addendum. La v8 ne dit pas comment ce point sera traité.

**Correction proposée.** Trancher avant le scellement. Soit intégrer ces éléments, soit écrire que la lecture de H-G1
ne changera pas et que ces mesures, si elles viennent, seront descriptives, ajoutées par un addendum scellé et contre-lu
avant toute lecture.

### CL8-09 — de forme — en-tête et banc de mutation

**Emplacement.** En-tête, l. 3-6 ; l. 52 ; docstring de `muter_v8_v1.py` ; R-398.

**Constat.**
- L. 5 dit « sur un code nouveau (`c66f529`) », alors que le commit cité est `5d1d4fd` (l. 52), où se trouve R-402.
- « Trois corrections du noyau » pour quatre changements : R-395, R-396, R-402 et le contrat R-398.
- « Sans changer aucune hypothèse », alors que H-C (descriptive) gagne un objet rapporté. La table des changements le
  dit pourtant : « Hypothèse (H-C) ».
- Le banc `muter_v8_v1.py` se dit « des trois corrections » et en éprouve quatre. R-398 le consigne avec « trois
  mutants rouges » : il a donc été étendu sous le même nom (R12), et la version à trois mutants ne se distingue plus.

**Correction proposée.**
- Écrire « code nouveau (`5d1d4fd`) » et « quatre changements du noyau (trois corrections et le contrat) ».
- Écrire « aucune hypothèse testée n'est changée ; H-C, descriptive, rapporte en plus la question de `c001` ».
- Corriger la docstring du banc, et soit le renommer en v2, soit dire au registre que la v1 a été étendue avant tout
  scellement.

### CL8-10 — de forme (R6) — pièces nouvelles citées sans empreinte ; script de scellement non cité

**Emplacement.** L. 66-72 ; entrée « Contre-lecture 8 » ; Plan, point 5.

**Constat.** `sortie-pytest-5d1d4fd-v1.txt`, `sortie-mutations-v8-v1.txt` et `muter_v8_v1.py` sont cités par chemin,
sans empreinte. Le script de scellement v8, qui tire l'entropie et vérifie le chemin que lit le lanceur, n'est cité
nulle part ; la v7 citait le sien (ligne CL5-12).

**Correction proposée.** Citer chemin et empreinte. Empreintes des pièces que j'ai reçues :

| pièce | sha256 |
|---|---|
| `sortie-pytest-5d1d4fd-v1.txt` | `cd62355894b17f7b94f494971b60d3538b22ce7d54ecbbac0820baf49201398f` |
| `sortie-mutations-v8-v1.txt` | `5198e8342dd28f4e3443dc96e92db1c4b51f80019c2a2404309600215b1a6627` |
| `muter_v8_v1.py` | `c43dc574f9f805619a5e07d320793ae60691a0ebd2cdf3553bb137cd851722d2` |
| `sceller_etape1_v8.py` | `b5f67cb9757c5c987995ca11b5de2e0e23067bbed20c0475c88d071442eeee21` |

### CL8-11 — de forme — noms et précisions

**Emplacement.** L. 379-380, 477, 573 ; l. 437-438 ; l. 250-252 ; l. 494 et l. 649 ; contrat § 7 ; registre R-396.

**Constat.**
- (a) « Appel de contrôle » (l. 379-380, 477, 573) et « test de dépense » désignent le même appel, celui du § 11 du
  lanceur.
- (b) Les l. 437-438 attribuent les plafonds 512, 640 et 1 200 aux 39 appels. R-400 ne les donne que pour les 27
  appels coupés.
- (c) L. 252, « le certificat, reconnus extérieurs sous tout code » : le code ne reconnaît le certificat que sans code
  HTTP, ce qui suffit puisqu'un échec de certificat n'en porte jamais. Le motif « compte » est en outre plus large que
  le texte : il couvre le quota, la facturation, la permission refusée et l'authentification.
- (d) `max_tokens_demandes` compte les plafonds **servis**, après rabattement à 4 096 ; les rabattements ne sont pas
  reportés à l'extrait. Un 4 096 au journal peut donc venir d'une demande plus haute.
- (e) Le contrat, § 7, dit « le recopie dans ta vue (`gNNN/reponse-question.md`) », alors qu'à `c001` c'est
  `c001/reponse-question.md`.
- (f) Le registre R-396 dit que, sans la correction, la réponse n'était pour B « que dans le dossier de travail rendu
  à root ». Elle était déjà dans la vue de B, sous `c001/travail/reponse-question.md` (point 7 du tableau). R-396
  ajoute la copie à la racine de `c001/`, que le contrat annonce : le correctif est juste, sa justification inexacte.

**Correction proposée.**
- Unifier le nom de l'appel.
- Préciser (b), (c) et (d).
- Corriger (e) dans la prochaine version du noyau.
- Pour (f), ajouter une ligne nouvelle au registre, qui ne se réécrit pas.

### CL8-12 — de forme, hors du périmètre de la v8 — un calcul de plafond inexact, présent depuis la v7

**Emplacement.** L. 427.

**Constat.** « Répétition 40 USD (… 3 × 2 rondes × 2, 3 × 3 × 5) » : la répétition n'a qu'une génération
(`--generations 1`), d'où 3 × 1 × 5 = 15 USD. Le pire cas vaut 6,6 + 12 + 15 = 33,6 USD, sous le plafond de 40. Avec
« 3 × 3 × 5 » = 45 USD, le plafond serait dépassé, ce qui contredit « les plafonds ne mordent pas par construction ».
Les contre-lectures n° 5 à 7 ne l'ont pas relevé.

**Correction proposée.** Écrire « 3 × 1 × 5 ».

## Ce que je n'ai pas pu vérifier

- **Essais du lanceur.** Ils exigent le vrai dépôt : `src`, `garde_calcul.py`, registres, objets git. Je m'appuie sur
  la sortie fournie, sur la lecture et sur mes rejeux ciblés (porte, test de dépense).
- **Garde de calcul.** Je n'ai rejoué ni `garde_calcul.py` ni le vrai `registres/go.md`. L'acceptation de la ligne
  d'extension de GO-05 repose sur R-403.
- **Suite complète.** Je n'ai rejoué que 24 essais : les 4 de la v8 et 20 essais liés. Les 137 passés reposent sur la
  sortie fournie.
- **Pièces du dépôt citées par chemin.** `prereg/pieces-gradient-etape1-v8/…`, `-v7/…`, `-v5/…` (dont CL7-01), la
  provenance du vivier `1f283223…`, le script d'extraction `689cf292…` (n° 35 dit qu'il est identique), le message
  n° 33, le vrai fichier du vivier et son commit. Je n'ai vu que les valeurs du n° 35.
- **Environnement.** Noms des clés définis (aucune variable lue), recharge automatique (attestation de Lazar), crédits,
  réglages de la console.
- **Transmission de l'en-tête.** Je n'ai pas pu vérifier que le SDK `anthropic` 2.3.0 transmet
  `ANTHROPIC_CUSTOM_HEADERS` : le collisionneur ne passe aucun en-tête lui-même. C'est antérieur à la v8 et ne concerne
  que la clé n° 1, épuisée.
- **Comportement réel des modèles.** Réflexion adaptative et coupures à 4 096 jetons ; pour Gemini, retour des parts
  « thought » sans demande explicite.
- **Analyseur d'options.** J'ai la sortie, pas le script.

## Hygiène

- **Copie et essais.** J'ai copié l'arbre du code dans mon dossier temporaire. Pour les essais, l'espace des organismes
  a été redirigé (`ESSAIM_M3_ESPACE`) vers un dossier dédié, `/var/lib/essaim-m3-cl8-BL4BzQ` (0711). Il le fallait :
  mon dossier temporaire est en 0700, et les utilisateurs des organismes doivent pouvoir traverser cet espace. Ce
  dossier a été retiré à la fin, par son chemin exact. Rien n'a été écrit dans `/var/lib/essaim-m3`.
- **Balayage du code essayé.** Sous essai, le noyau balaie les systèmes de fichiers pour trouver les dossiers
  inscriptibles par tous (CL5-02). C'est le code essayé qui lit ces métadonnées, pas moi.
- **Scellement à blanc.** La sortie scellée a été détruite. Aucune graine n'a été affichée ni gardée.
- **Fichiers restants.** Dans `/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/cl8-travail/`
  restent seulement mes scripts et des listes, sans graine ni clé.

## Empreintes

- Texte relu `gradient-etape1-sondes-v8.md` : `4c98ed5123bbe60d0fabf084340ae705464993027be4535915b27aa7bb2d1995`.
- Ce rapport : voir son compagnon `contre-lecture-preenregistrement-gradient-etape1-v8.md.sha256`. Un fichier ne peut
  pas contenir sa propre empreinte.
