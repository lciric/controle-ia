# Journal — « Le programme expliqué depuis zéro » — v2

Rédacteur neuf de la v2 (sous-agent de la session mère, Claude Opus 5.5), qui n'a écrit ni la v1, ni sa contre-lecture, ni sa consigne, ni aucune pièce citée. Début du travail : 2026-11-10 10:15:01 UTC ; journal écrit de 10:47 à 10:52 UTC (heures relevées par `date -u`). La v1 et ses pièces restent intactes (R12).

## Interdits, refus, rôle
- Interdits communs v2 (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiée) tenus en entier, règle 9 comprise : aucun fichier ni aucune branche interdits ouverts ; recherches par `git grep` ou `grep` sur des fichiers nommés, `git ls-files` avec exclusions (`docs/notes/bras-attaque`, `diag`, `runs`, `donnees`) ; aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé. Commandes git en lecture seule seulement : `git log`, `git branch -a | head -40` (noms, rien ouvert), `git merge-base --is-ancestor` sur la branche de la session-dépôt. Le dossier `depuis-zero-comparaison-v1/` et les autres documents « depuis zéro » (nommés en R-2132, R-2138, R-2147) n'ont pas été ouverts. Aucune branche de quarantaine nommée au registre n'a été ouverte ni n'est nommée ici.
- **Aucun refus** d'un contrôle de permissions ni d'un classifieur.
- **Rôle** : j'ai lu `brouillons/T0.7-sondes-v0-v1-brouillon20.md` (l. 836-861) et `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` (l. 1003-1007) : exclu de tout rôle de lecteur de P3-bis.

## Pièces d'entrée vérifiées (toutes conformes)
```
2c639ca3622600ed36427df7c62f07f62be351b4dc69f575499a0b3c9c29b487  programme-depuis-zero-2026-11-10-v1.html
0b4de478057799c2edecddbacbe3d625c24679c688ba631e5d0db4c813035ed6  programme-depuis-zero-2026-11-10-v1-registre-affirmations.md
b69932b164f4f8231a4fb19787519bd842bee763e3c058025b9e92e8ebcb7867  programme-depuis-zero-2026-11-10-v1-journal.md
ee221d75738ae429dd57cc1475ac47a6d36da63f243eac2f9c9801a437e85976  exemple-chiffre-depuis-zero-v1.py
5ef5170775431d6aa32d3f35a353b6f0c089c2d1847dc88722ced0a5eb086131  programme-depuis-zero-2026-11-10-v1-contre-lecture-v1.md
d7a37a10511350f03472858c94a3552db07beb0ada261f9d4acdeb812952877a  consigne-document-de-zero-v1.md
```

## Méthode
1. Les 47 couples de la contre-lecture sont relus **par programme** dans son fichier et recopiés dans `programme-depuis-zero-v2-couples-v1.json` (identifiants `Cnn-k` = constat nn, couple k) ; s'y ajoutent 46 couples du rédacteur (`R01` à `R46`).
2. `programme-depuis-zero-v2-faire-v1.py` contrôle (empreintes ; copie fidèle mot pour mot des 47 couples ; chaque texte actuel exactement une fois dans la v1, puis au moment de son application ; aucun texte actuel subsistant ; chaque nombre décimal des couples « exemple » sorti du script v2, relancé par lui) et écrit la v2. Aucune retouche à la main du HTML.
3. Gardes éprouvées sur un cas sain (sortie écrite, code 0) et sur quatre artefacts (R5), tous refusés :
```
artefact « double » refusé, comme attendu : C01-1 : texte actuel présent 2 fois dans la version 1 (exactement une fois exigé)
artefact « absent » refusé, comme attendu : R01 : texte actuel présent 0 fois au moment de son application
artefact « chiffre » refusé, comme attendu : R07 : le nombre 0,2945 ne sort pas du script de l'exemple chiffré v2
artefact « copie » refusé, comme attendu : C05-1 : différent du couple 5-1 de la contre-lecture
```
4. Sortie du script « faire » (sans les 93 lignes « 4. … appliqué ») :
```
fichier de couples : docs/notes/rapports-directeur/programme-depuis-zero-v2-couples-v1.json sha256 0ce5f3adb0c1581ae80bbc588bfc5ddbc8278b5b0401d4ee1430eebf2c603279
script de l'exemple : docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v2.py sha256 b12b923510bbaff358461d7802f387e226d69dc4817f23204fd6515c874549d0
1. empreintes de la version 1 et de la contre-lecture : conformes
2. copie fidèle des 47 couples de la contre-lecture : conforme
3. chaque texte actuel de la contre-lecture présent exactement une fois dans la version 1 : conforme
5. aucun texte actuel de la contre-lecture ne subsiste dans la sortie : conforme
6. nombres des couples « exemple » : 60 nombres, tous sortis du script v2 : conforme
bilan : 47 couples de la contre-lecture appliqués (41 tels quels, 6 adaptés, 0 non appliqué) ; 46 couples du rédacteur ; sortie sha256 d6d5d448fab06a079f15f9e6b00422d1a5f57b6bd76f78e938e61904b076cdc9
écrit : docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v2.html
```

## Table « constat → traitement »
| constat | gravité | traitement |
|---|---|---|
| 1 | bloquant | couple C01-1 appliqué tel quel |
| 2 | bloquant | C02-1 tel quel |
| 3 | bloquant | C03-1 tel quel (vérifié : T0.3, « Hors de portée », l. 56 ; note v3 § 3) |
| 4 | à corriger | C04-1, C04-2 tels quels |
| 5 | à corriger | C05-1 tel quel |
| 6 | à corriger | C06-1, C06-2 tels quels ; R12 ajoute les valeurs à dix actions |
| 7 | à corriger | C07-1 tel quel ; **C07-2 adapté** : le « ≈ 23 » est un calcul à la main du contre-lecteur, remplacé par la sortie du script v2 (22,8 ; maximum 4,7 ; processus e 6,2), hypothèse « les dix actions sabotées, B = 5 » écrite ; R04 à R12 : horizon de dix actions au § 1 et au § 2.6 (consigne v2, point 2) |
| 8 | à corriger | C08-1 tel quel |
| 9 | à corriger | C09-1 tel quel |
| 10 | à corriger | **C10-1 adapté** : « rendu sur la branche d'une autre session … pas encore fusionné » (R-2126, R-2137, R-2141 ; R-2157 confirme la fusion encore à faire) — consigne v2, point 4 |
| 11 | à corriger | C11-1, C11-2 tels quels (vérifié : verdict P3 v2, différence saboteur moins honnête ; réserve B1 l. 509-512) |
| 12 | à corriger | C12-1 tel quel |
| 13 | à corriger | C13-1 tel quel ; glose validée : N-007 § 1, base (ii) « cascade de portes indépendantes », qui isole « le gain de l'accumulation additive sur la cascade » |
| 14 | à corriger | C14-1 tel quel ; aucune réécriture de D-S10 trouvée dans `docs/decisions/` (la note d'alignement ne porte que sur D-S8) |
| 15 | à corriger | **C15-1, C15-2 adaptés** : « dont le préenregistrement n'existe pas » périmé (premier brouillon de T0.8 lancé, R-2131) ; « prévue » devient « promise », et la possibilité « sans marge » est dite, pour s'accorder à la liste insérée au § 9 (ligne 4) ; R03, R19, R20 : la promesse d'avant l'entretien écrite comme une prévision datée du 10 novembre, source R-2130 (consigne v2, point 5) |
| 16 | à corriger | C16-1, C16-2 tels quels ; R16, R24 : question et réponse de R-2145 verbatim, contenu de R-611 (voir « Choix ») |
| 17 | à corriger | **C17-1 adapté** : le rapprochement est désormais une décision de Lazar (R-2152, 10:30 UTC) ; R35 : développement du code v65 repris (R-2148) |
| 18 | à corriger | C18-1 tel quel |
| 19 | à corriger | C19-1 tel quel |
| 20 | à corriger | C20-1 tel quel |
| 21 | à corriger | C21-1, C21-2 tels quels |
| 22 | à corriger | **C22-1 adapté** : ajout de l'écart omis « I set the questions and take every decision » (candidature l. 256 ; socle § 1.3) ; C22-2 tel quel |
| 23 | à corriger | C23-1 tel quel ; R22 ajoute la voie sans ouverture anticipée (N-066 point 2 ; relevée par la contre-lecture du socle, R-2133) |
| 24 | registre | registre v2 : empreinte de la candidature `b2458c2d209a` (A24, A67, A74, A100) ; empreinte de `registres/decisions.md` à la lecture (A69, A79, A99, A108) ; A74 l. 159 ; A78 (R-2127) et A107 (R-2130) vérifiées ; A73 R-600 ; A58 source T0.7 brouillon 20 |
| 25–30 | mineurs | C25-1, C26-1, C26-2, C27-1, C27-2, C28-1, C29-1, C30-1 tels quels ; R13 ajoute « défini au § 6 » (demandé par le constat 29) |
| 31 | mineur | C31-1 tel quel ; R14 ajoute la famille (iii) au tableau (retirée de la phase 0 : P-002, défaut appliqué le 6 octobre) |
| 32 | mineur | C32-1, C32-2 tels quels ; glose validée : N-056 point 2 (« borne basse du pari apparié (valide à tout nombre de tâches) ») et cœur statistique `pari_apparie.py` (richesse par mises, Ville, borne basse à tout instant) |
| 33–36 | mineurs | C33-1, C34-1, C34-2, C35-1, C36-1 tels quels |
| 37 | mineur | glossaire : R29 à R31 (mode de sabotage, mode tenu à l'écart, dose et dose réalisée, plancher, nœud, oracle, jumeau honnête, pince, pari apparié, ancien et nouveau juge, A1-v3 et A1-v4, ligne du registre, évasion) ; PDF reconstruit sous un nom neuf, non déposé |

**Couples non appliqués : aucun.** 41 appliqués tels quels, 6 adaptés (C07-2, C10-1, C15-1, C15-2, C17-1, C22-1), l'écart écrit dans le fichier de couples.

## Couples du rédacteur
| id | motif |
|---|---|
| R01 | Titre : version 2. |
| R02 | Bandeau : version 2, heure relevée par date -u à la dernière lecture du registre des décisions. |
| R03 | Consigne v2, point 5 : la promesse d'avant l'entretien écrite comme une prévision datée, avec sa source (R-2130). |
| R04 | Consigne v2, point 2 (constat 7) : l'horizon réel de dix actions dit dès le § 1, chiffre tiré du script v2. |
| R05 | Consigne v2, point 2 : chapeau de l'exemple chiffré, script v2 et deux horizons. |
| R06 | Consigne v2, point 2 : tableau (a), en-tête du bloc de 200 actions. |
| R07 | Consigne v2, point 2 : tableau (a), bloc de dix actions, valeurs du script v2 (lignes [A10]). |
| R08 | Consigne v2, point 2 : lecture du tableau (a) à dix actions. |
| R09 | Consigne v2, point 2 : prix de la garantie toujours valide et calendrier à dix actions. |
| R10 | Consigne v2, point 2 : le tableau (b) porte sur 200 actions. |
| R11 | Consigne v2, point 2 : partie (b) à dix actions. |
| R12 | Consigne v2, point 2 : mise en garde de la classe K à dix actions. |
| R13 | Constat 29 : « mode tenu à l'écart » employé avant sa définition (renvoi au § 6, demandé par le constat). |
| R14 | Constat 31 : la famille (iii) du programme (§ 7) manquait au tableau sans être dite écartée (P-002). |
| R15 | Mise à jour (R-2131) : préenregistrement des surveillants de référence en rédaction. |
| R16 | Consigne v2, point 4, et précision de la mère (R-2145) : question et réponse verbatim, avec ce que dit R-611, rien de plus. |
| R17 | Mise à jour (R-2135) : le jeu « coût gonflé » v3 refusé par la règle gelée. |
| R18 | Mise à jour (R-2131) : § 8.1, préenregistrement des bases boîte noire en rédaction. |
| R19 | Consigne v2, point 5 : encadré du § 8 écrit comme une prévision datée, avec sa source. |
| R20 | Consigne v2, point 5 : chemin critique introduit comme une prévision datée. |
| R21 | Mise à jour (R-2131) : scellement visé du préenregistrement des surveillants de référence. |
| R22 | N-066, point 2 : la voie sans ouverture anticipée (relevée par la contre-lecture du socle, R-2133). |
| R23 | Mise en accord avec la liste « ce qui manque » (lignes 3, 4, 8) et R-2131 : ce qui n'est pas promis avant l'entretien. |
| R24 | Précision de la mère (R-2145) : question et réponse verbatim, au point 5 de « ce qui dépend de toi ». |
| R25 | Borne du 31 janvier 2027 : reprise dans la règle de repli approuvée d'un mot direct (R-765 ; contre-lecture du socle, R-2133). |
| R26 | Même point : la borne n'est plus à confirmer ; reste le décalage de l'entretien auprès du fonds. |
| R27 | Mise à jour (R-2131) : brouillon 11 du témoin positif en rédaction. |
| R28 | Mise à jour (R-2131) : brouillon 21 du préenregistrement des sondes en rédaction. |
| R29 | Constat 37 : glossaire, saboteurs publics (iii). |
| R30 | Constat 37 : glossaire, étiquettes A1-v3, A1-v4. |
| R31 | Constat 37 : termes de registre ajoutés au glossaire. |
| R32 | Sources : script de l'exemple v2, contre-lecture de la v1, registre des décisions. |
| R33 | Mise à jour (R-2133) : le socle de preuves v1 a été contre-lu depuis. |
| R34 | Note finale : registre v2, statut de contre-lecture. |
| R35 | Mise à jour (R-2148, R-2152) : développement du code de l'organisme repris. |
| R36 | Mise à jour (R-2162) : la page publique du verdict du juge est publiée, sur le mot de Lazar. |
| R37 | Mise à jour (R-2158 ; registres/depenses.md l. 414) : la dépense d'A1-v4 est inscrite, non rapprochée. |
| R38 | Même mise à jour, tableau des cinq affirmations. |
| R39 | Même mise à jour, « ce qui dépend de toi », point 2. |
| R40 | Mise à jour (R-2158, R-2159) : vérification de l'état de l'art de niveau 3 lancée. |
| R41 | Mise à jour (R-2161) : signalement d'antériorité pour HC2, non vérifié (R7 : sans chiffre). |
| R42 | Demande de Lazar relayée par la mère : liste « ce qui manque » insérée telle quelle au § 9. |
| R43 | Mise en accord du tableau des cinq affirmations avec la liste insérée. |
| R44 | Fait demandé par la mère : témoins de concepts, option (c) (R-2155, R-2158). |
| R46 | Mise en page de la liste insérée (style du tableau). |
| R45 | Fait demandé par la mère : résultat d'A1-v4 publié (R-2162). |

## Choix
1. **Exemple chiffré v2** : horizon de dix actions avec B = 2,5 (même décalage par action et même part sabotée qu'à 200 actions, B = 50), plus la ligne « dix actions sabotées à 0,5 σ » (B = 5) qui donne le chiffre du constat 7. Le bloc de 200 rejoue la v1 à l'identique (mêmes graines, garde interne `V1_ATTENDU` : vrai). Grille de ρ mise à l'échelle √(200/n0) : à n0 = 10, l'optimum (1,01) dépasse la borne de la grille de la v1 ; garde ajoutée si l'optimum tombe au bord. Le tableau (a) est coupé en deux tableaux (en-tête répété) pour qu'aucun bloc ne soit orphelin en bas de page.
2. **Bras d'attaque** : état dicté gardé ; ajoutés tels quels : l'autorisation de dépense sur devis non inscrite (R-2127 ; aucune ligne dans `registres/go.md`), la question de la mère et la réponse « oui » de Lazar (R-2145), le contenu de R-611. **Écart à signaler à la mère** : la précision de la mère (« rien de plus ») précède R-2146 (10:20 UTC), où Lazar **lève la restriction de R-611 pour le bras** ; j'ai ajouté cette décision, sans aucune conclusion sur la date ou la forme du lancement, parce que l'omettre rendait la phrase fausse à la date du document. Elle tient dans deux couples (R16, R24) : à retirer si la mère le décide. Le second arrêt par un classifieur (R-2045) n'est pas ajouté (laissé à la mère par la contre-lecture ; « rien de plus »).
3. **Borne du 31 janvier 2027** : « à confirmer » retiré ; la borne est reprise dans la règle de repli approuvée d'un mot direct (R-765), comme le relèvent la contre-lecture du socle (R-2133) et le socle v2 (R-2156, « N-027 bis non inscrite ») ; le point 7 de « ce qui dépend de toi » ne la redemande plus.
4. **Mises à jour du registre postérieures à la consigne**, intégrées parce qu'elles rendaient une phrase fausse (registre lu jusqu'à R-2163, 10:49 UTC) : préenregistrement de T0.8 en rédaction (R-2131) ; brouillons 11 et 21 (R-2131) ; socle v1 contre-lu (R-2133) ; dépense d'A1-v4 inscrite le 10 novembre (R-2158 ; `registres/depenses.md` l. 414) ; page publique du juge publiée (R-2162) ; vérification de niveau 3 lancée (R-2159) ; signalement d'antériorité non vérifié pour HC2, sans chiffre (R-2161).
5. **Lues, non intégrées** (ne changent aucune phrase ; le document ne promet rien d'autre avant l'entretien) : R-2155 et R-2158 (3) (phrases témoins des concepts de T0.7, option (c)) ; R-2158 (1)-(2) (analyste des prémisses de la trace interne, liste de ce qui manque) ; R-2153 (code de T0.7) ; R-2160 (ordre de 7b, brouillon 4) ; R-2157 (coordination) ; second mot de R-2162 (priorité « sonde au-dessus du hasard », reprise par la liste insérée). Arrivées après la coupure : R-2164 (réseau de la vérification de niveau 3) et R-2165 (premier brouillon du préenregistrement de T0.8 rendu, non contre-lu) ; le document dit « en rédaction », comme la liste insérée (ligne 3) : à mettre à jour dans une version suivante.
6. **Liste « ce qui manque »** (demande de Lazar relayée par la mère, 10:4x UTC ; R-2163) : `docs/notes/rapports-directeur/ce-qui-manque-approche-peut-marcher-v1.md` (`edb0bf03d87dd208b4add5f9630aac19a2f9dc04336215a9c01d4febe0578626`, vérifiée) insérée **telle quelle** au § 9 (couple R42) : texte inchangé, seul le balisage passe de Markdown à HTML (conversion par programme dans l'outil de génération, empreinte contrôlée) ; titre donné par la mère ; une phrase de provenance ajoutée après ses sources. Mise en accord du reste du § 9 sans la réécrire : « Ce qui ne sera pas prêt » devient « Ce qui n'est pas promis avant l'entretien », avec renvois aux lignes 3, 4 et 8 (R23) ; le tableau des cinq affirmations renvoie à la liste (R43) ; C15-1 et C15-2 disent « promise » et « possible, sans marge ». Deux faits demandés : concepts en option (c) au § 8.3 (R44 ; R-2155, R-2158) ; résultat d'A1-v4 publié, au § 6 (R45) et au point 6 de « ce qui dépend de toi » (R36 ; R-2162).
7. PDF d'essai : 20 pages A4 (cible 16 à 20 : à la borne, du fait de la liste insérée), construit dans le dossier temporaire, non déposé.

## Contradictions et manques
1. Contre-lecture, constat 7 : « la même somme … environ 23 fois sur 100 » suppose les dix actions sabotées (B = 5), alors que le § 1 parle de la moitié ; à moitié sabotée (B = 2,5), le script donne 6,2. Les deux sont écrits, chacun avec son hypothèse.
2. R-2156 (socle v2, non contre-lu) signale que le plancher de 645,42 dollars compterait deux fois une ligne de 1,06 : **non vérifié**, chiffre du document inchangé (pièce scellée `total-depenses-v3.md` l. 11) ; à trancher par la mère.
3. N-055 (D-S10) et N-056 (D-S29) sur le mode tenu à l'écart : les deux écrits, la règle se fixe au préenregistrement de G1 (comme le constat 14).
4. La clause N-027 bis de la porte des instruments n'est pas inscrite (R-765 l'annonçait).

## Ce que je n'ai pas vérifié
- Le verdict formel de la simulation (branche d'une autre session, non lue) : seul le registre est repris.
- Les pages des articles cités (R7) ; arXiv 2606.10304 (R-2161) n'est dit que comme signalement non vérifié.
- Les pièces du bras d'attaque (interdites) : la portée des décisions R-611, R-2145, R-2146 n'est écrite que par leurs mots.
- Le doublon de 1,06 (point 2 ci-dessus).

## Registres vivants
`registres/decisions.md` lu jusqu'à R-2163 (l. 2121 ; `7cadb1d486f5f6815d84000c17888ca183518e17f9ed00b1d1bd5941c62f157f` à 10:45:55 UTC, puis `f7d219571825…` à 10:49:58 UTC ; registre en ajout seul, 31 lignes citées recontrôlées à 10:44 UTC) ; `registres/depenses.md` `5268f0f09943ab37d103534206121a30a28b76807b8eae6bac98c3e0d77b02a9` ; `registres/etat.md` `e6d41dbe378aaccc691ebfb443f2562f6cf36fcf092a874680b1f939abe083b4` ; `registres/go.md` `e682abb0db3a0da37c0d764a7c659f638d449df266f6c9580d3ec481c8d44155`.

## Sources lues, empreintes (sha256 complets)
```
2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c  docs/programme-controle-ia-v2.md
9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2  docs/brief-claude-code-programme-complet-v2.md
dfe4fe0fc4d025011bbe0f330fd591b1898dc7e767384e96c946b6388ad81cd0  docs/notes/note-mathematique-lemme-theoreme-v3.md
9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545  docs/notes/resultats-T0.3-v1.md
7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb  prereg/T0.3-simulation-lemme-theoreme-v1.md
ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169  prereg/T0.6-organismes-v0-v1.md
9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9  brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md
9ef671ac08ba79a43fa4fecfb7740bc6b5769587741ae378dc2935a02caf69da  brouillons/T0.7-sondes-v0-v1-brouillon20.md
b8a97629e8376528d3d58fedab5d23da9d132924428dd9509bba3722876fdf2f  brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md
5609fc655b5e48b2326f0511b6ae61eeb15b0eef3d0d2885fde3a977b15bf89c  brouillons/entretien-taif-v3/consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md
b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0  docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt
05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751  docs/verdicts/verdict-P3-premier-test-i-a-v2.md
63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13  docs/verdicts/verdict-T0.4-critere-1-G0-v3.md
b9a072302d6514c0df80c950317012498c7af62b6440e37045a43de46a3faabc  docs/verdicts/verdict-T0.5-pilote-v1.md
1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea  docs/verdicts/verdict-validation-nul-v9-v1.md
7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135  docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md
e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda  docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md
0f1bca5aa900bffed944b9f7c0b2b5f1b2a137b2b3c8337c9b0b28e3d881c0f4  livrables/registres-taif-v4/calibration-v3.md
123be1a7e1c345574d451a0e4ee31f3193f6b7fc1a522f2e293934e03b94ea21  livrables/registres-taif-v4/total-depenses-v3.md
ec6c2cf64d0c9a3bcb3484f2bc58ca986c89e97829bd45fdb96cbc42bf094fef  docs/notes/couche-2-preparation-v1/contre-lecture-garde-delta-v5/outils/copie_pole/pari_apparie.py
ae5f73892026ed83f5d0b08f38efe781d71250cdc1571a745acca0e40a6aafc6  docs/decisions/note-alignement-N-055-D-S8-v1.md
ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232  docs/decisions/decision-N-007-N-008-v1.md
55df073d6918405949f3543308f0de7f90293baeefc5a4525e5f49697b2517e6  docs/decisions/decision-N-035-v1.md
2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf  docs/decisions/decision-N-044-v1.md
c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d  docs/decisions/decision-N-045-v2.md
371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6  docs/decisions/decision-N-055-v1.md
3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d  docs/decisions/decision-N-056-v1.md
387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97  docs/decisions/decision-N-064-v1.md
21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351  docs/decisions/decision-N-066-v1.md
012ddc44baca981620ff2a81211998fd437f6b336436d33406b119227c406628  docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md
0d3ad7545d8ecf46e6012a6925eebddb659085656d26731b5dd7121508d83bb6  docs/notes/rapports-directeur/construire-rapport-pdf-v1.py
1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f  docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md
```
Les autres pièces du registre v2 (lignes « = ») sont celles de la v1, aux empreintes de son journal, rehachées par la contre-lecture ; celles que j'ai recalculées sont égales (registre v2, en-tête).

## Script de l'exemple chiffré v2
Chemin : `docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v2.py`. Commande : `.venv/bin/python -I docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v2.py` (≈ 5,2 s sur processeur ; aussi relancé par le script « faire »). Graines : `SeedSequence(20261110).spawn(24)` ; enfants 0 à 11 pour 200 actions (ceux de la v1), 12 à 23 pour dix actions (indices consignés dans la sortie). Deux exécutions, sorties identiques. Sortie :
```
python 3.13.18 ; numpy 2.4.6 ; scipy 1.17.1 ; entropie 20261110
[graines] SeedSequence(20261110).spawn(24) ; horizon 200 : {'honnete': 0, 'm': (1, 2, 3, 4, 5), 'calendrier': (6, 7), 'b_honnete': 8, 'b_y': 9, 'b_regroupement': 10, 'b_copule': 11} ; horizon 10 : {'honnete': 12, 'm': (13, 14, 15, 16), 'calendrier': (17, 18), 'b_honnete': 19, 'b_y': 20, 'b_regroupement': 21, 'b_copule': 22, 'toutes_sabotees': 23}
[script] sha256 b12b923510bbaff358461d7802f387e226d69dc4817f23204fd6515c874549d0
[A] n0 = 200, B = 50, alpha = 0.01, R = 20000
[A] rho retenu (minimise la frontière à n0) = 0.23 ; frontière terminale S* = 47.424
[A] seuil par action z = 2.3263 ; seuil exact du maximum c = 3.8894
[A] honnête : fausses alertes du processus e (règle de Ville) = 0.0032
[A] m ; delta ; P(une action sabotée > seuil par action) ; maximum de l'épisode ; somme à horizon fixé ; toujours valide (positions au hasard) ; borne terminale
[A]  10 ; 5.00 ; 0.9962 ; 1.0000 ; 0.8867 ; 0.7584 ; 0.5723
[A]  25 ; 2.00 ; 0.3721 ; 0.5302 ; 0.8867 ; 0.7100 ; 0.5723
[A]  50 ; 1.00 ; 0.0924 ; 0.0989 ; 0.8867 ; 0.6876 ; 0.5723
[A] 100 ; 0.50 ; 0.0339 ; 0.0393 ; 0.8867 ; 0.6741 ; 0.5723
[A] 200 ; 0.25 ; 0.0189 ; 0.0270 ; 0.8867 ; 0.6703 ; 0.5723
[A] calendrier, m = 100, delta = 0.50 : toujours valide ; somme à horizon fixé
[A] début ; 0.9712 ; 0.8861
[A] fin ; 0.5910 ; 0.8860
[A] prix de la garantie toujours valide, m = 100, positions au hasard : somme à horizon fixé 0.8867 - toujours valide 0.6741 = 21.3 points
[B] n0 = 200, r = 10, R = 20000, seuils calibrés sur 20000 épisodes honnêtes au quantile 0.99
[B] statistique ; taux d'alerte sans attaque ; taux d'alerte sous regroupement ; égalité trajectoire par trajectoire
[B] somme ; 0.0102 ; 0.0102 ; True
[B] maximum ; 0.0109 ; 0.0109 ; True
[B] somme glissante (w = 10) ; 0.0093 ; 1.0000 ; False
[B] autocorrélation d'ordre 1 ; 0.0082 ; 0.7195 ; False
[B] multi-ensemble préservé : True
[B] classe K (copule AR(1), phi = 0.5, marges N(0,1)) : somme unilatérale 0.0892 ; maximum 0.0093 (alpha = 0.01)
[A10] n0 = 10, B = 2.5, alpha = 0.01, R = 20000
[A10] rho retenu (minimise la frontière à n0) = 1.01 ; frontière terminale S* = 10.604
[A10] seuil par action z = 2.3263 ; seuil exact du maximum c = 3.0889
[A10] honnête : fausses alertes du processus e (règle de Ville) = 0.0013
[A10] m ; delta ; P(une action sabotée > seuil par action) ; maximum de l'épisode ; somme à horizon fixé ; toujours valide (positions au hasard) ; borne terminale
[A10]   1 ; 2.50 ; 0.5689 ; 0.2845 ; 0.0623 ; 0.0272 ; 0.0052
[A10]   2 ; 1.25 ; 0.1409 ; 0.0723 ; 0.0623 ; 0.0175 ; 0.0052
[A10]   5 ; 0.50 ; 0.0339 ; 0.0287 ; 0.0623 ; 0.0134 ; 0.0052
[A10]  10 ; 0.25 ; 0.0189 ; 0.0224 ; 0.0623 ; 0.0104 ; 0.0052
[A10] calendrier, m = 5, delta = 0.50 : toujours valide ; somme à horizon fixé
[A10] début ; 0.0238 ; 0.0602
[A10] fin ; 0.0075 ; 0.0654
[A10] prix de la garantie toujours valide, m = 5, positions au hasard : somme à horizon fixé 0.0623 - toujours valide 0.0134 = 4.9 points
[A10] toutes les 10 actions sabotées, delta = 0.50 (B = 5) : une action 0.0339 ; maximum 0.0471 (simulé 0.0464) ; somme à horizon fixé 0.2281 (simulé 0.2317) ; toujours valide 0.0624 ; borne terminale 0.0382
[B10] n0 = 10, r = 3, R = 20000, seuils calibrés sur 20000 épisodes honnêtes au quantile 0.99
[B10] statistique ; taux d'alerte sans attaque ; taux d'alerte sous regroupement ; égalité trajectoire par trajectoire
[B10] somme ; 0.0095 ; 0.0095 ; True
[B10] maximum ; 0.0087 ; 0.0087 ; True
[B10] somme glissante (w = 3) ; 0.0091 ; 0.0684 ; False
[B10] autocorrélation d'ordre 1 ; 0.0086 ; 0.0800 ; False
[B10] multi-ensemble préservé : True
[B10] classe K (copule AR(1), phi = 0.5, marges N(0,1)) : somme unilatérale 0.0721 ; maximum 0.0103 (alpha = 0.01)
[garde] horizon de 200 identique à la sortie de la v1 : True
```

## Sorties
Document `programme-depuis-zero-2026-11-10-v2.html`, registre `…-v2-registre-affirmations.md` (151 lignes A01 à A151), ce journal, `exemple-chiffre-depuis-zero-v2.py`, `programme-depuis-zero-v2-faire-v1.py`, `programme-depuis-zero-v2-couples-v1.json` ; tous scellés (compagnons `.sha256`). PDF d'essai (20 pages) dans le dossier temporaire du rédacteur, non déposé.
