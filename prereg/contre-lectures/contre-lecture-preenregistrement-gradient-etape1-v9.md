# Contre-lecture n° 9 — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes), v9 « économe »

## Identité

Relecteur **neuf (R2)**. Je n'ai écrit ni ce préenregistrement (v1 à v9), ni le code du noyau, ni les lanceurs et leurs
essais, ni les scripts de scellement, ni aucune contre-lecture ou revérification précédente.

Périmètre : **revérification limitée**. Elle porte sur deux choses :
- le traitement des douze remarques de la contre-lecture n° 8 (CL8-01 à CL8-12) ;
- les deux changements nouveaux du code (`5d1d4fd` → `4de6544`) et du lanceur (v5 → v6) : clé OpenAlex (R-415) et
  clé Semantic Scholar (R-417).

J'y ajoute la règle R1 sur le diff du texte, la cohérence des renvois, un scellement à blanc et les défauts que la v9
introduit. Je ne refais pas la contre-lecture n° 8.

J'ai lu seulement les pièces du dossier, avec ma copie temporaire. Je n'ai fait aucun accès réseau ni appel payant. Je
n'ai lu ni affiché aucune clé réelle ni variable de clé : tous les essais ont tourné sous
`env -u OPENALEX_API_KEY -u SEMANTIC_SCHOLAR_API_KEY` ou `env -i`, avec des valeurs factices. Je n'ai lancé aucun
sous-agent, n'ai rien écrit dans git et n'ai modifié aucune pièce.

## Heures (UTC)

- Début : 2026-10-25 11:27:48 (`date -u`).
- Fin des vérifications : 2026-10-25 11:46:53 (`date -u`). Le rapport a été rédigé juste après.

## Texte relu et empreinte

- `pieces/gradient-etape1-sondes-v9.md`. Les marqueurs `<<…>>` ne sont pas remplis, ce qui est attendu. Il en reste cinq,
  chacun une fois.
  - sha256 = `7f012573e6f45bb18c7ec30680bc365a7f3c30d21edb3eed38ab98ec800d6fd2`.
  - Le compagnon `.sha256` concorde, et R-414 cite la même empreinte.
- `EMPREINTES-pieces.txt` : 243 sur 243 OK.
- La v8 de référence a l'empreinte `4c98ed51…`, celle que cite la v9. Le rapport n° 8 a l'empreinte `64e4fe74…`, citée
  elle aussi.

## VERDICT : **« scellable »**

Compte par gravité : **0 bloquante, 0 majeure, 3 mineures, 3 de forme** (CL9-01 à CL9-06).

Les douze remarques de la n° 8 sont traitées. Huit le sont en entier ; quatre ont un reste de forme hors du texte
(lanceur, registre), repris en CL9-06. La seule majeure de la n° 8, CL8-01, est fermée : la question « structure »
n'atteint aucune course décisive, ni par le texte, ni par le lanceur, ni par les essais, ni par une voie de côté.

La v9 ne change aucune hypothèse testée, prédiction, métrique principale, seuil ni table de lecture (R1).

Le code de R-415 et R-417 fait ce que dit le texte : la clé ne va qu'au noyau, l'échec est masqué avant la troncature, et
la présence est appariée par le noyau et par le lanceur. Mes rejeux le confirment.

Trois mineures restent, et aucune ne touche la symétrie des bras ni la lecture de H-G1 :
- des voies par où une clé peut sortir sans passer par le masquage : redirections, réponses brutes, copie poussée
  (CL9-01) ;
- deux propriétés revendiquées qu'aucun artefact ne prouve (CL9-02) ;
- une présence de clé qui peut changer entre A_r et B_r après un redémarrage de la session (CL9-03).

Ces trois mineures peuvent être acceptées comme réserves dans le champ « traitement » de l'entrée 9. Le script les y
insère sans toucher au reste, et elles sont scellées avec le texte : je l'ai vérifié à blanc. Corriger le corps du texte,
par exemple pour la règle de CL9-03, donnerait un brouillon nouveau à faire relire, puisque le script ne scelle que
`7f012573…`.

## Suivi des remarques CL8-01 à CL8-12

| remarque | état | preuve rejouée |
|---|---|---|
| CL8-01 (majeure) question de `c001` au seul bras qui a le service | **fermée** : faite, juste, complète | **Texte** : H-C (« Aucune question ouverte n'est posée dans les courses décisives »), Métrique (6), Plan, points 2, 3 (A_r « sans question, R-410 ») et 14 (« Aucune course décisive ne la reçoit », raison dite), Liste d'arrêt ; diff des sections recalculé. **Lanceur v6** : `--question-ouverte` ne figure que dans les arguments de `repetition` (l. 273) ; A_r (l. 280-283) et B_r (l. 287-288) n'en ont pas. **Essais** : constat nouveau « A1 sans question (R-410) » (absence de `--question-ouverte` dans la ligne de A1) et « bras B sans question ni vivier », tous deux OK dans la sortie 79/79. **Analyseur d'options** : `question à c001 dans la ligne` vaut 1 pour la répétition, 0 pour la répétition B, A2 et B1. **Aucune voie de côté** : le noyau ne pose la question que sur `--question-ouverte` (défaut `None`, `cli.py` l. 412) ; le contrat § 7 décrit le mécanisme sans le contenu ; les entrées sont en 0700 à root ; la vue de la répétition est fermée aux utilisateurs des autres courses (CE3-06) ; le second pilote est fini avant A_r. Reste sans effet : le lanceur exige encore l'empreinte et la pièce de la question pour toute course, pour l'extraction seulement. **Observation** : la répétition est la seule à recevoir la question, elle n'est donc plus en ce point la répétition de A_r. Ce que la répétition B dit de « répond sans le service » porte sur des organismes qui ont reçu la question : au pire, c'est plus pessimiste que B_r, sans effet sur H-G1. |
| CL8-02 coupures par la réflexion, surtout sur B ; seuil 50 % ; Argon | faite | Métrique (7) nomme le mécanisme. Plan, point 6 : statuts et appels qui ont réfléchi, par paire et par bras, sans seuil, tirés de l'extrait mécanique. L'extrait est bien scellé par l'outil lui-même (`extrait_mecanique.py` l. 12 et 270), et les champs `appels`, `par_espece`, `reflexion_par_statut` existent (essai `test_r402_…` rejoué). Point 8 : taux soumis à Lazar quels qu'ils soient, Argon compris, et limite d'Argon dite ; Liste d'arrêt mise à jour. La limite d'Argon est **confirmée par la pièce source** : 11 857 jetons de sortie, `types_blocs` = `['text']` seul. Information : la même pièce montre 16 812 jetons de sortie pour Fable et 26 930 pour Opus, réflexion comprise, sur des questions de conception. La part coupée à 4 096 pourra donc être forte sur les appels longs ; c'est ce que la vérification humaine de la répétition tranche. |
| CL8-03 garde du test de dépense sans essai | limite dite ; un accessoire non traité | La Liste d'arrêt dit la limite, avec le résultat du rejeu n° 8, exact. Le § 11 du lanceur est **inchangé** du v5 au v6 (diff recalculé, identique au patch fourni) : le rejeu n° 8 vaut donc encore. `noyau_env` ne gagne que deux exports. L'accessoire « pièce de question en lien symbolique » n'est ni éprouvé ni dit (CL9-06 d). |
| CL8-04 hôte : cohabitation, mandataire, perte du disque | faite | (a) Plan, point 3, « Cohabitation » : second pilote fini avant A_1 et A_2, constat consigné, décalages 700 et 800, aucune autre course pendant A_r et B_r. C'est une vérification humaine ; les décalages du second pilote ne sont pas vérifiables ici. (b) Limite des HTTP 405 et 407 dite (Métrique (4)) ; la règle des pannes est inchangée (`analyse_gradient.py` `4b54d380…`). (c) Copie scellée poussée après chaque course, et perte entre A_r et B_r dite. La copie ouvre une voie nouvelle pour les clés : voir CL9-01 (b). |
| CL8-05 clés nommées par une ligne de GO | faite | La ligne d'extension de GO-2026-10-24-04 du 25 octobre (`go-extrait.md`, R-411) nomme les clés n° 3, LUC et Gemini n° 2, sur le compte du programme. Le texte la cite au Plan, points 3 et 12. Les clés de moisson ne sont nommées par aucune ligne : CL9-05. |
| CL8-06 borne par exécution ; plafond de recharge | faite | Plan, point 3 et Annexe : « 1 150 USD par exécution », règle « aucune relance » et engagement ; « aucune console ne plafonne la recharge » (R-412). L'engagement à usage unique, proposé « au mieux », n'est pas fait. |
| CL8-07 chiffres du § 3 du contrat sans source | faite | Plan, point 2 : le pilote est cité (R-391, R-400), et le tour « structure » par `journal.jsonl` `43b54f06…`. Empreinte recalculée sur la pièce : égale. Contenu : Fable et Opus à `max_tokens` 64 000, `OK`, blocs `thinking` et `text`. Le plafond de 1 200 jetons non cité et Gemini non couvert sont dits comme limites. Le contrat est inchangé (`06333cb3…` recalculé). |
| CL8-08 lecture de H-G1 annoncée changeante | faite | Plan, point 6 : « La lecture de H-G1 ne changera pas », un éventuel ajout descriptif passera par un addendum scellé et contre-lu avant toute lecture (R-413). La table est identique octet pour octet. |
| CL8-09 en-tête et banc | faite ; un reste au registre | Le paragraphe de la v8 est corrigé dans l'en-tête : « `5d1d4fd` », « quatre changements du noyau (trois corrections et le contrat) », « hypothèse testée ». La docstring de `muter_v8_v1.py` est juste (« quatre changements … étendu de trois à quatre mutants »), et R-414 (a) consigne l'extension. Reste : la sortie du banc v8 a été régénérée sous le même nom, sans que ce soit consigné (CL9-06 e). |
| CL8-10 empreintes des pièces ; script de scellement | faite | J'ai recalculé : pytest de `4de6544` `eb2fcfe8…`, mutations v8 `e06d662c…` et banc `24bcf2df…`, mutations v9 `9a753f02…` et banc `d7baee98…`, script v9 `6def483c…`. Toutes égales aux valeurs citées. La suite de `5d1d4fd` (`cd623558…`) est égale à celle de la table de la n° 8. |
| CL8-11 noms et précisions | faite dans le texte ; restes dans le lanceur | (a) Dans le texte, « appel de contrôle » ne reste que dans trois rangées de tables historiques (CE3-13, CE4-09, CL5-08), ce qui est acceptable. Le lanceur le garde (CL9-06 a). (b) Plafonds rattachés aux 27 appels coupés. (c) Motifs précisés en Métrique (4). (d) « plafonds `max_tokens` servis — après le rabattement à 4 096 » au point 8 ; le lanceur, l. 14, dit encore « demandés ». (e) Contrat § 7 : limite dite au point 14. (f) R-414 (b). |
| CL8-12 « 3 × 3 × 5 » | faite | Plan, point 4 : « 3 × 1 × 5 » ; 6,6 + 12 + 15 = 33,6 ≤ 40. |

## R1, section par section

Le diff recalculé (`diff -u` v8 → v9) est identique au patch fourni, à l'en-tête près. J'ai découpé les sections par
leurs titres et comparé leurs mots.

| section | état | ce qui change |
|---|---|---|
| Prédiction chiffrée et signe attendu | **identique** octet pour octet | — |
| Seuil | **identique** | — |
| Critères de lecture gelés | **identique** | — |
| Hypothèse | H-C seule, qui est descriptive | La question ne figure plus aux courses décisives. H-G1, H-G0, H-G2 et H-G3 sont inchangées. |
| Métrique | « ce qui reste différent » seul | (4) présence des clés OpenAlex et Semantic Scholar au manifeste et parité, motifs précisés, limite des 405 et 407 ; (6) question retirée ; (7) mécanisme nommé. Score, unité, statistique et intervalle sont inchangés. |
| Plan d'analyse | points 2, 3, 4, 6, 8, 12 et 14 ; point 5 : « entrée 9 » | L'appel gelé `lire_h_g1` est inchangé. Ce qu'ajoute le point 6 est descriptif et sans seuil. `analyse_gradient.py` et `analyse.py` gardent les empreintes citées (recalculées). |
| Liste d'arrêt | de 43 à 44 lignes | Une ligne nouvelle (R-415, R-417). Trois lignes sont réécrites, et aucune n'est retirée sans remplaçant. |

## Vérifications de R-415 et R-417

1. **La clé n'atteint jamais l'organisme.**
   - Les environnements de l'organisme, de la métrique et de l'entraîneur sont construits à partir de rien
     (`bac_a_sable.py` l. 354 et 480, `entrainement.py` l. 355). Aucune copie de `os.environ` n'existe dans le code
     (recherche faite).
   - L'organisme tourne dans un autre espace de processus, sous un autre utilisateur.
   - La clé n'est ni dans le contexte ni dans la vue : le dossier `noyau` est exclu de la vue (`archive.py` l. 146 et
     204).
   - L'`echec` rendu à l'organisme est masqué.
2. **Elle n'atteint aucun journal.**
   - `journal-recherches.jsonl` reçoit le même `echec` masqué.
   - Le manifeste ne porte que des booléens. Rejeu : la valeur factice n'est pas dans le manifeste, et le fichier existe
     bien dès la construction, si bien que l'assertion conditionnelle de `test_r415` n'est pas vide.
   - L'extrait mécanique ne lit du journal des recherches que le statut et la source (`extrait_mecanique.py`
     l. 177-192).
   - Le lanceur n'écrit que `oui|non` (`cles.txt`, notes).
3. **Masquage avant toute troncature.** `masquer_cles(f"{type(e).__name__}: {e}")[:200]`. Rejeu avec un message de
   180 caractères, puis la clé, puis 50 caractères : aucun préfixe de la clé dans l'échec rendu ni au journal. La
   propriété est juste, mais non prouvée par l'essai (CL9-02).
4. **Le lanceur ne passe la clé qu'au noyau.** J'ai extrait `noyau_env` (l. 298-312) tel quel et je l'ai rejoué sous
   `env -i`, avec des valeurs factices :
   - les trois clés de moisson sont exportées si elles ne sont pas vides, absentes sinon, et absentes aussi si elles sont
     définies vides ;
   - les variables étrangères (`AUTRE_SECRET`, `RR_ANTHROPIC_API_KEY_LUC`) sont retirées ;
   - la présence vue par le lanceur (`[ -n … ]`) égale donc celle que vit le noyau (`bool(os.environ.get(…))`) ;
   - aucune valeur ne passe par une ligne de commande.
   Aucun essai de la suite n'exerce `noyau_env`. Un défaut d'export ferait refuser B_r, sans créer d'asymétrie.
5. **La présence est au manifeste et appariée.**
   - Noyau : `boucle.py` l. 285-286 ; `cli.conditions_moisson_differentes` l. 230-235.
   - Lanceur : l. 211-213 (`cles.txt`) et l. 258-261 (manifeste de A).
   - Rejeu direct dans le sens que les essais du noyau n'éprouvent pas (origine sans clé, B avec) : refus avec le bon
     motif, pour les deux clés.
6. **Essais et banc rejoués.** Copie de l'arbre, `/opt/essaim-m3-venv-v1/bin/python -B`, `ESSAIM_M3_COLLISIONNEUR` vers
   le collisionneur des pièces, espace des organismes dans un dossier dédié sous `/var/lib/`.
   - 17 essais passés : `test_r415_…`, `test_r417_…`, `test_ce305_sources_moisson_au_manifeste_et_bras_apparie`,
     `test_ce305_credit_epuise_arrete_la_course`, `test_rv07_…`, `test_rv12_…`,
     `test_recherche_refuse_une_requete_qui_copie_une_tache_de_test`, `test_moisson_de_bout_en_bout_en_simulation`,
     deux essais du téléchargeur, `test_garde_fuite_empreintes_et_recoupement`, trois essais du mode réel, trois essais
     du bras apparié.
   - 10 essais liés de plus, passés : R-395, R-396, R-398, R-402, extrait mécanique, `rv04`, `cl5_01`, `cl5_02`.
   - Banc `muter_v9_v1.py` rejoué : témoin vert, cinq mutants rouges, comme la sortie fournie.
   - Six mutants supplémentaires, que le banc n'essaie pas :
     - détectés : nom Semantic Scholar retiré de la liste des noms masqués ; nom OpenAlex retiré ; présence au manifeste
       forcée à faux ;
     - **survivent** : troncature avant le masquage ; parité à un seul sens, pour OpenAlex comme pour Semantic Scholar
       (CL9-02).
   - Essais du lanceur : les quatre artefacts nouveaux (`openalex-differente-fichier`, `openalex-differente-manifeste`,
     `semanticscholar-differente-fichier`, `semanticscholar-differente-manifeste`) sont dans la sortie 79/79, avec le bon
     motif. Je ne les ai pas rejoués : ils exigent le vrai dépôt.
7. **Voies de fuite cherchées.**

| voie | résultat |
|---|---|
| message d'exception | couverte (masquage) ; la forme encodée n'est pas masquée (CL9-02) |
| adresse finale d'une redirection et en-têtes suivis | **non couverte** (CL9-01 a) |
| réponse brute gardée (`recherches/<id>.brut`) | hors de la vue ; non masquée ; part dans la copie poussée (CL9-01 b) |
| journal du noyau, sortie d'erreurs | couverte (l'exception est rattrapée dans `rechercher`) |
| extrait mécanique | couverte |
| manifeste, `cles.txt`, notes du lanceur | booléens seulement |
| ligne de commande | aucune valeur |
| environnement de l'organisme ou de l'entraîneur | construit à partir de rien |
| mandataire de sortie de la session | voit l'adresse avec `api_key` (hors de l'organisme ; non vérifiable ici) |

## Cohérence

- **Empreintes.**
  - Les 17 empreintes de fichiers du bloc du commit, recalculées, sont égales. L'arbre du noyau, recalculé par
    l'algorithme de `boucle.empreinte_arbre`, vaut `3b90daa0…`, la valeur citée.
  - Diff du code : les blobs git d'après sont les fichiers des pièces (5 sur 5). Le diff inversé redonne les empreintes
    citées par la v8 pour `boucle.py`, `cli.py`, `moisson.py` et `recherche.py`. Le diff est donc complet, et les
    fichiers dits « inchangé » le sont.
  - Recalculées et égales aux valeurs citées : lanceur v6 `96c92eeb…`, essais `bd1f5aba…`, sortie des essais
    `8797b98b…`, analyseur `2e074ec7…`, environnement `f308af5c…`, question `a54da93e…` (pièce v6), collisionneur
    `213b52ef…`, mission `bd2c6a15…`, note `6b415104…`, v5 du lanceur `e0c9f8ce…`.
  - Les diffs v5 → v6 du lanceur et des essais, recalculés, sont identiques aux patches fournis.
- **Comptes.**
  - 139 + 3 = 142 définitions d'essais (125 + 17).
  - 26 mutations = 12 + 4 + 1 + 4 + 5.
  - 79 = 75 + 4 artefacts nouveaux. Le constat « question à c001 pour A1 » est remplacé par « A1 sans question ».
  - 47 noms d'essais du lanceur cités par la Liste d'arrêt, tous dans la sortie. Tous les essais pytest cités sont
    définis.
- **Chemins.** Le lanceur lit `PREREG=prereg/gradient-etape1-sondes-v9.md` et la question sous
  `docs/procedures/gradient-etape1-v6/`. Les essais écrivent le préenregistrement factice sous le nom v9.
- **Décisions et GO.** R-410 à R-417 concordent avec le texte. Lignes de GO : extension de GO-04 (R-411), extension de
  GO-05 (R-403), GO-2026-10-25-01 et son extension à 120 USD (R-409).
- **Heures.**
  - Contre-lecture n° 8, de 09:28 à 10:08 UTC : concorde avec son rapport.
  - R-410 à R-413 « vers 11:00 », R-415 et R-416 « vers 11:05 » ; essais du lanceur de 11:22:02 à 11:22:35.
  - L'« État au scellement » est daté « vers 11:10 » : CL9-04.

## Script de scellement v9 (à blanc)

J'ai monté un faux dépôt dans mon dossier temporaire : `prereg.py` des pièces, doublures minimales de `gardes.py` et de
`scellement.py` (absents des pièces), copie du lanceur v6 sous `docs/procedures/gradient-etape1-v6/`. La configuration
est factice, mais elle porte le vrai `texte_relu_sha256` et les vraies valeurs du vivier (n° 35).

- **Cas sain**, code 0 :
  - les cinq marqueurs sont remplis, chacun une fois, et aucun marqueur ne reste ;
  - l'entrée « Contre-lecture 9 » est trouvée et remplacée, avec le texte relu et le rapport ;
  - les sept valeurs littérales sont chacune en une seule occurrence ;
  - E est entier et inférieur à 2^128 ; les graines valent `SeedSequence(E).spawn(3)` et `generate_state(1, uint64)[0]` ;
  - le compagnon est conforme et le validateur ne relève rien ;
  - le motif et l'extraction du lanceur, rejoués en bash, relisent les graines, `vivier_commit` et `question_c001_sha256` ;
  - le texte scellé ne diffère du brouillon que par les marqueurs et l'entrée 9.
- **Refus pour la bonne raison**, rien d'écrit dans chaque cas :
  - lanceur qui lit `…-v8.md` ;
  - lanceur au bon `PREREG=` mais dont l'empreinte n'est pas citée ;
  - deux lignes `PREREG=` ;
  - sortie sous un autre nom ;
  - sortie hors du dépôt ;
  - brouillon différent du texte relu ;
  - marqueur en double ;
  - marqueur inconnu restant ;
  - entrée 9 altérée ;
  - `graine_1 = 7` glissé dans un champ libre ;
  - `question_c001_sha256` en double ;
  - sortie existante (R12) ;
  - rapport de même empreinte que le texte (validateur, sortie supprimée, code 3).
- Aucune graine n'a été affichée ni gardée : la vérification n'a imprimé que des booléens, et la sortie scellée et son
  compagnon ont été détruits aussitôt. Une recherche finale dans mon dossier ne trouve aucune graine.

## Remarques nouvelles

### CL9-01 — mineure — des voies par où une clé de moisson peut sortir sans passer par le masquage

**Emplacement.**
- `moisson._lire_https` (l. 56-72) ; `semanticscholar_rechercher`, `openalex_rechercher`, `brave_rechercher`.
- `recherche.Rechercheur.rechercher` (l. 213, `recherches/<id>.brut`).
- Plan, point 3, « Copie » ; Plan, point 9 (« l'adresse finale d'une redirection est suivie en https ») ; docstring de
  `moisson.py` (« aucune redirection hors https »).
- Liste d'arrêt, dernière ligne.

**Constat.**

(a) **Redirections.** `_lire_https` laisse `urllib` suivre toute la chaîne de redirections, puis vérifie le schéma et
l'hôte final. Le gestionnaire de redirection de Python 3.13.17 recopie tous les en-têtes vers la cible, `x-api-key`
compris, même vers un autre hôte et même en http. Une redirection de `api.semanticscholar.org` enverrait donc la clé à un
tiers, en clair si la cible est en http, et le refus ne viendrait qu'après. Il en va de même pour la clé Brave
(`X-Subscription-Token`), depuis avant la v9. Pour OpenAlex, la clé est dans l'adresse : elle ne suit une redirection que
si le serveur la recopie dans `Location`. La probabilité est faible (il faut qu'une interface officielle redirige), et
l'organisme n'y a aucune prise. Mais le refus « hors https » et le refus de l'hôte ont lieu après l'envoi.

(b) **Réponses brutes et copie.** Le masquage ne couvre que les messages d'échec. La réponse brute est gardée sans
masquage dans `travail/noyau/recherches/<id>.brut`. Elle est hors de la vue de l'organisme, mais elle part dans la copie
scellée que la v9 fait pousser après chaque course « sans être ouverte ». Si une réponse recopiait la requête (je n'ai
pas pu le vérifier), la clé partirait sur la branche distante. La ligne « clé … dans une sortie versée » prévoit une
vérification humaine « par les formes de clés », mais elle ne dit ni qu'elle s'applique à cette copie, ni comment la
faire sans ouvrir la sortie.

**Preuve.**
- Rejeu sans réseau de `HTTPRedirectHandler().redirect_request` : la requête nouvelle porte
  `{'User-agent': …, 'X-api-key': 'FACTICE'}`, vers `https://autre-hote…` comme vers `http://autre-hote…`.
- Lecture de `_lire_https` : le contrôle a lieu après `urlopen`.
- `archive.py` l. 146 : la vue est copiée sans `noyau`.

**Correction proposée.**
1. Pour les trois sources à clé, refuser toute redirection, ou retirer en-tête et paramètre au changement d'hôte ou de
   schéma. Ajouter un essai sain et un artefact, faisables sans réseau par `redirect_request`. À défaut, dire la limite
   au point 9, ou en réserve dans le champ « traitement » de l'entrée 9.
2. Au point « Copie » : avant de pousser, chercher mécaniquement dans la copie les **valeurs** des clés de la course
   (Anthropic, Gemini, Brave, OpenAlex, Semantic Scholar), en ne rendant qu'un compte et sans ouvrir le contenu. Le
   versement est refusé si le compte n'est pas nul.

### CL9-02 — mineure (R5) — deux propriétés revendiquées par la Liste d'arrêt ne sont prouvées par aucun artefact

**Emplacement.** Liste d'arrêt, ligne « clé OpenAlex ou Semantic Scholar… » (« masquée avant toute troncature », « bras
B refusé ») ; `test_r415_…`, `test_r417_…` ; banc `muter_v9_v1.py`.

**Constat.**
- (a) Les messages d'artefact font moins de 200 caractères. Un code qui tronquerait avant de masquer passerait donc les
  essais, et c'est ce cas qui laisserait un préfixe de la clé en clair.
- (b) Côté noyau, la parité n'est éprouvée que dans un sens : origine avec clé, bras B sans clé. Le sens contraire est le
  plus probable dans cette session (CL9-03) ; seul le lanceur l'éprouve, par le fichier `cles.txt`.

Le code actuel est juste dans les deux cas. Accessoires :
- le lanceur n'a pas de cas sain « clé présente dans A et dans B » ;
- la forme encodée d'une clé dans une adresse (`%2B`, `%2F`, `%3D`) n'est pas masquée. C'est sans effet si la clé
  n'a que des lettres et des chiffres, ce qui n'est pas vérifiable ici.

**Preuve.**
- Mutants supplémentaires : « tronquer puis masquer » **survit** (2 passés). « Parité à un sens » survit pour OpenAlex et
  pour Semantic Scholar.
- Rejeu direct : un message long ne laisse aucun préfixe ; une origine sans clé et un B avec clé sont refusés ;
  `masquer_cles("…api_key=ab%2Bcd%2Fef%3Dgh")` rend le texte inchangé.

**Correction proposée.**
- Dans une version suivante du noyau : un artefact long (clé à cheval sur la position 200), l'artefact de parité
  inverse, et au besoin le masquage de `quote_plus(valeur)`.
- D'ici là, écrire dans la ligne que ces deux propriétés sont vérifiées par lecture et par ce rejeu, comme la v9 l'a
  fait pour CL8-03, ou le porter en réserve dans le champ « traitement ».

### CL9-03 — mineure — la présence des clés OpenAlex et Semantic Scholar peut changer entre deux courses ; le texte la tient pour acquise

**Emplacement.** Plan, point 3, « État au scellement » (« absentes au lancement, les sources `openalex` et
`semanticscholar` sont servies sans clé, dans les deux bras ») ; R-415, R-416, R-417.

**Constat.**
- Les deux clés sont versées aux réglages. Elles deviennent visibles après un redémarrage du processus de la session :
  R-416 le constate pour les clés n° 3 et LUC.
- Les courses partent de cette session et s'étalent sur un à deux jours (A_r jusqu'à 10,5 h, voire 15,75 h).
- **Redémarrage entre A_r et B_r** : B_r voit « oui » et il est refusé par le lanceur et par le noyau. La garde est juste
  et ne crée pas d'asymétrie, mais le texte ne dit pas la conduite à tenir. Lancer B_r en retirant ces variables de
  l'environnement tient la parité et la condition écrite, mais ce n'est pas prévu.
- **Redémarrage entre la répétition et A_r** : A_r et B_r courraient avec les clés, sur un chemin que la répétition n'a
  pas exercé. Une clé invalide, par exemple, ferait échouer OpenAlex dans les deux bras.
- La décision « maintenant » de Lazar (R-415) restera sans effet sur les courses si les clés restent absentes. C'est
  écrit, mais pas présenté comme un choix.

**Correction proposée.**
- Écrire, au corps du texte ou dans le champ « traitement » de l'entrée 9 (qui est scellé), que la présence des clés de
  moisson est celle de la répétition pour toute l'étape : chaque course part avec cette présence, au besoin en retirant
  les variables de l'environnement du lanceur, et une course dont la présence diffère ne part pas.
- Soumettre à Lazar une ligne : (a) étape sans ces clés ; (b) redémarrer la session avant la répétition, pour que la
  répétition et les quatre courses les aient.

### CL9-04 — de forme — heure de l'« État au scellement »

**Emplacement.** Plan, point 3 : « au 25 octobre vers 11:10 UTC … `OPENALEX_API_KEY` et `SEMANTIC_SCHOLAR_API_KEY`,
versées par Lazar après 11:01 UTC, ne le sont pas encore ».

**Constat.** D'après R-417, la clé Semantic Scholar a été versée vers 11:15 UTC. R-415 et R-417 constatent l'absence des
deux clés à 11:20 UTC. À 11:10, la clé Semantic Scholar n'était donc pas encore versée.

**Correction proposée.** Écrire « vers 11:20 UTC », comme les registres.

### CL9-05 — de forme — clés de moisson hors de toute ligne de GO valide après le 26 octobre

**Emplacement.** Plan, point 3, « Clés » ; `go-extrait.md`.

**Constat.**
- GO-05 renvoie à GO-04 pour Anthropic et nomme `GEMINI_API_KEY`. L'extension de GO-04 (R-411) nomme les clés n° 3,
  LUC et Gemini n° 2.
- `BRAVE_API_KEY` n'est nommée que par GO-07, qui échoit le 26 octobre.
- `OPENALEX_API_KEY` et `SEMANTIC_SCHOLAR_API_KEY` ne sont nommées par aucune ligne de GO : R-415 et R-417 sont des
  décisions.

La logique de CL8-05 vaut si l'une de ces clés débite un compte, par exemple Brave au-delà de son quota.

**Correction proposée.** Une ligne d'extension. Ou une ligne de registre qui dit que ces clés ne débitent rien, et sous
quelle décision elles sont employées (R-363, R-415, R-417).

### CL9-06 — de forme — restes du suivi de CL8-03, CL8-09 et CL8-11, hors du texte

**Constat.**
- (a) CL8-11 (a) annonce « test de dépense » partout. Or le lanceur v6 garde « appel de contrôle » dans ses notes de
  journal, l. 329-330 (« appel de contrôle en échec », « appel de contrôle : … »), et dans ses commentaires, l. 37, 44-46,
  53 et 186. Le journal `lancements.txt` portera donc un autre nom que le texte. De plus, l. 44 dit « statut OK exigé »
  sans les jetons de sortie.
- (b) CL8-11 (d) : le lanceur, l. 14, dit encore « plafonds demandés ».
- (c) L'en-tête du lanceur, l. 39-41, décrit la parité « Anthropic, Gemini et Brave », sans OpenAlex ni Semantic Scholar.
- (d) CL8-03, accessoire : l'artefact « pièce de question en lien symbolique » n'est ni ajouté ni dit.
- (e) CL8-09 : `sortie-mutations-v8-v1.txt` a été régénérée sous le même nom après la contre-lecture n° 8. La n° 8 a
  relu `5198e834…`, la v9 cite `e06d662c…`. Le banc a changé de même, de `c43dc574…` à `24bcf2df…`. R-414 consigne la
  docstring, pas la nouvelle exécution du banc.

**Correction proposée.**
- Unifier les noms au prochain lanceur ; ce sont des commentaires et des notes, sans effet sur les gardes.
- Une ligne de registre pour (e).
- (d) : le dire dans la ligne de la Liste d'arrêt, ou l'accepter.

## Ce que je n'ai pas pu vérifier

- **Essais du lanceur v6.** Ils exigent le vrai dépôt. Je m'appuie sur la sortie 79/79, sur la lecture, et sur mes
  rejeux de `noyau_env` et du motif littéral.
- **Suite complète.** Les fichiers JSON de la banque sont retirés des pièces. J'ai rejoué 27 essais ; les 139 passés
  reposent sur la sortie fournie (`eb2fcfe8…`).
- **Préenregistrement du second pilote** : décalages 700 et 800, fin avant A_r.
- **Comportement réel des interfaces** : redirections, écho éventuel de la requête dans les réponses, format des clés
  OpenAlex et Semantic Scholar, et journalisation des adresses par le mandataire de la session.
- **Présence réelle des clés** dans la session : aucune variable n'a été lue. Garde de calcul et vrai registre des GO
  non rejoués.
- **Pièces du dépôt citées par chemin** sous `prereg/pieces-gradient-etape1-v9/`, la banque `f1387a20…` et le vrai
  fichier du vivier.

## Hygiène

- Toutes les copies (arbre, diff inversé, faux dépôt, copies des mutants) ont été faites dans
  `/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/cl9-travail/`, puis
  supprimées. Il n'y reste que mes scripts, les diffs recalculés et les sorties des rejeux de mutation, sans clé ni graine.
- L'espace des organismes a été redirigé (`ESSAIM_M3_ESPACE`) vers un dossier dédié, `/var/lib/essaim-m3-cl9-9bEerF`
  (0711). Il a été retiré à la fin par son chemin exact, et rien n'a été écrit dans `/var/lib/essaim-m3`.
- Scellement à blanc : sortie et compagnon détruits ; aucune graine affichée ni gardée.

## Empreintes

- Texte relu `gradient-etape1-sondes-v9.md` : `7f012573e6f45bb18c7ec30680bc365a7f3c30d21edb3eed38ab98ec800d6fd2`.
- Ce rapport : voir son compagnon `contre-lecture-preenregistrement-gradient-etape1-v9.md.sha256`. Un fichier ne peut
  pas contenir sa propre empreinte.
