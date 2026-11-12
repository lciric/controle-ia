# Vérification courte — socle de preuves de l'entretien, v4 — v1

- **Rôle** : vérificateur court neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni le socle (v1 à v4), ni ses journaux, ni la contre-lecture de la v3, ni aucune pièce citée.
- **Modèle** : Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur de la v4 (Claude Opus 5.5).
- **Heures** (`date -u`, 10 novembre 2026) : consigne vérifiée et lue à 12:46:57 ; rejeu des annexes à 12:47:16 ; registre relu à 12:49:23 ; rapport écrit à 12:51:06.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-verification-courte-socle-v4-v1.md` (`65538d08eb369d1ffea3a2c89a6805c951a2681f77740638829409b662c2781a`, égale à son compagnon), interdits communs v2 et interdits propres lus en entier.
- **Pièces vérifiées, empreintes recalculées et égales aux compagnons** : socle v4 (`b1c76e273f4b939b0b7fb80c00975d6efeb30e24748b239233fc0a823d3bcb30`) ; son journal (`bd39da504f627e7e7822e6b4c5444075b7a71b8decb0a7366fa8c9b9b98b5f0d`), lu en entier ; socle v3 (`b9377f1dfc72082a1c95224b7a3746cce5b575ec1a2e6dae882394c6b3f36265`) ; contre-lecture de la v3 (`3a1df7959475b440e61193500d44f58b72dd433e928dbba338452875cb45079b`).
- **Registre des décisions** : `registres/decisions.md` = `8fd7620f49f7193d6d191648b8e63aff821703ef185d10f72d6d063d6dc53685` à 12:51:06, 2 180 lignes, dernière ligne R-2223.

## Verdict

**Utilisable pour l'entretien après corrections** : **un couple exigé** (VS-C1, sur le couple C24 : condition de configuration de GO-2026-11-10-10, R-2220) ; trois couples facultatifs (VS-C2 à VS-C4).

Le rejeu est exact à l'octet, les douze textes modifiés sont fidèles à leurs sources, les ajouts AJ07 à AJ13 tiennent, aucun taux de calibration ne figure, et l'état du bras est dit « non vérifiable par la mère ». **Aucune phrase de la v4 n'est fausse** au registre lu jusqu'à R-2223 ; une est incomplète depuis R-2220 (VS-03).

## Constats

**VS-01 — rejeu de l'annexe A : conforme.** Programme extrait du journal par motif (bloc `~~~python`), empreinte `83c7045f…` égale à celle que le journal déclare ; lancé par `.venv/bin/python -I` sur la v3 et la contre-lecture, heure de fin `12:39:46` : code 0, 719 → 740 lignes, 38 couples tels quels, 12 modifiés, 13 ajouts, sortie `b1c76e27…`, **égale à l'octet** à la v4 scellée (`cmp`). Avec `12:00:00`, la sortie ne diffère que par la ligne 6.

**VS-02 — rejeu de l'annexe B : conforme.** Programme extrait de même (`3dae137a…`, égal au journal) : **neuf essais sur neuf conformes**, code 0 (garde : refus sur la v3 et sur la contre-lecture, saine sur l'essai et sur la v4 ; reproduction égale ; empreinte altérée, ancien en double, ancien absent : arrêt, code 2 ; faux dépôt identique : aucun arrêt).

**VS-03 — R-2220 (2) contre C24 : aucune phrase fausse, une phrase incomplète (couple exigé VS-C1).** `registres/go.md` l. 300 (`2c396b01…`, inchangé) : GO-2026-11-10-10 exige, pour l'organisme, « conditions de GO-2026-11-08-02 inchangées et toutes exigées : code v65 contre-lu, machine `bwrap` validée […], préenregistrement de la course scellé, configuration v5 (`995eb918…`) ». La v4 (l. 206) écrit « organisme 45, sous les conditions de GO-2026-11-08-02 — son code v65, contre-lu « utilisable pour la course après corrections », est repris en v66, en cours, R-2215 — » : exact (R-2206, R-2215). Mais R-2220 constate que le code v65 porte une configuration v5 d'une autre empreinte, qu'aucune pièce de `main` n'explique `995eb918…`, et que la v66 changera la configuration : la condition de la ligne est « à faire préciser par Lazar ». Un juré qui lit la ligne d'autorisation verrait une course autorisée sous une condition que le code en cours ne remplit pas à la lettre : à dire. Je n'ai pas recalculé l'empreinte de la configuration du code v65 (fichier absent de `main`) : elle est citée d'après R-2220. Recherche dans la v4 des autres passages que R-2220 pourrait toucher (v65, v66, configuration, GO-2026-11-10-10, GO-2026-11-08-02, GO-2026-11-02-23, GO-2026-11-02-25, audit de calibration des juges, boucle réelle) : **aucun autre**.

**VS-04 — R-2220 (1) : aucune phrase fausse.** « ligne `CODE-T07` non inscrite » (§ 6 point 5, l. 691) reste vrai : `registres/scellements-v1.md` (`0651adca…`, trois lignes) n'a aucune ligne `CODE-T07` ; un commit est seulement proposé. « attend aussi […] le module de T0.7 » (l. 362) reste vrai. La colonne « en cours » de la rangée du 10 (l. 539 : « ligne `CODE-T07` après sa réponse ») est périmée, ce que le § 7 point 9 déclare. Couple facultatif VS-C4.

**VS-05 — lignes postérieures à R-2221 : une seule, R-2222** (rendu du socle v4 et lancement de cette vérification) : elle ne touche aucune phrase de la v4. R-2221 (inventaire des idées) : aucun passage du socle n'en parle.

**VS-06 — les douze couples modifiés contre leurs sources : conformes.** Écarts au texte de la contre-lecture relevés par programme (comparaison mot à mot), puis relus contre les sources :
- **C14** : rapport du lot 7-B (`bf9b6af8…`, égal à son compagnon, branche `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`), l. 1-34 lues : § 0.1 point 1 (2611.02153, score de paire sur les représentations internes d'instances d'un même modèle ; 2611.10620, balayage sur les scores de sondes par agent), point 2, § 0.2 (« Déclencheur de bascule à examiner par Lazar », « Aucun des deux articles ne vient de ces équipes, et aucun ne publie un test séquentiel toujours valide sur sondes ») : fidèle. **Nuance non portée** : le même § 0.2 ajoute que la version 2 de NARCBench nomme la détection séquentielle comme prochaine étape, que 2611.10620 en réalise une forme faible, et que la veille « devient urgente » ; le socle dit « à réexaminer par Lazar », sans cette précision. Non faux ; à dire si un juré interroge le déclencheur.
- **C15** : R-2190 nomme bien H8, H6 (2605.26047) et la prédiction 1 de HC1 contredite (2606.05384) : fidèle.
- **C17** : rapport du lot 7-A (`8a6dd0e0…`, égal à son compagnon, même branche), l. 1-22 lues : « En tête », point 1 (« Aucun des trois articles n'occupe H1 ni H2 ») et point 4 (classifieur de texte entraîné contre sonde) : fidèle. « égale la sonde » résume un écart minime imprimé par les auteurs ; R-2188 dit « ≈ ». Acceptable.
- **C22** : R-2210 (`defd8ef0…`) et R-2212 (`0d51099e…`), empreintes recalculées sur `main` : fidèles. Mineur : ces deux lignes disent les brouillons « scellés » (empreinte compagnon) ; « rendus, non scellés » s'entend ici « non scellés comme textes définitifs » (couple facultatif VS-C3).
- **C24** : R-2206, R-2207, R-2175, R-2182, R-2215 ; `registres/go.md` l. 297-300 relues : fidèle ; incomplet depuis R-2220 (VS-03).
- **C25 à C29** : R-2216 et `registres/scellements-v1.md` (ligne `SCELLEMENT-T08-BASE-A`, `2026-11-10T12:21:55Z`, `72b067d5…`, empreinte du texte recalculée) ; R-2175 (D-2 (a)) ; R-2211 (douze traits) ; chaîne « contre-lecture, vérification courte » (R-2216) : fidèles.
- **C32** : R-2218 point (1), mot pour mot quant au fond (aucune pièce unique ; plupart des séries ; seul registre pour le rejeu R1-R2 et la relance v4 ; non établi pour trois textes d'analyse et les deux premières courses d'A1-v3) ; pièce `9639b715…` hachée, égale à l'empreinte citée, non lue (le socle le dit) ; R-2195 : « lecture à confirmer par Lazar » : fidèle.
- **C42** : R-2207 (lecture large), R-2210 (« contre-lecture différentielle […] sur T0.7 scellé ») : fidèle.

**VS-07 — ajouts AJ07 à AJ13 : conformes.** AJ07 : R-2160, chemin et `5f2167d7…` recalculés ; aucun brouillon 5 dans `docs/procedures/` ; aucune ligne de scellement de l'ordre. AJ08 : formule de la consigne, mot pour mot (VS-09). AJ09 : R-2162 (publication), R-2177 (nouveau « go publication » requis). AJ10 : `5268f0f0…` et `2c396b01…` égales aux registres à 12:51:06. AJ11, AJ12 : R-2216 ; plus aucune phrase de la v4 ne dit la règle « mots et coût » en attente (onze mentions relues) ; reste, l. 532, la cible « visés scellés le 12 au soir » de R-2177, exacte comme cible, dépassée pour la règle (couple facultatif VS-C2). AJ13 : R-2165 à R-2167 sont bien les rendus de T0.8 brouillon 1, T0.7 brouillon 21 et P3-bis brouillon 11 ; le point 9 couvre toute la colonne « en cours » du 10, où la page publique, l'ordre de 7b « brouillon 4 (R-2143) » et les concepts sont aussi périmés (déclaré en bloc, non énuméré).

**VS-08 — aucun taux de calibration : conforme.** Garde par empreintes : saine sur la v4 (annexe B). À l'œil : § 1.3 (l. 191-193) et § 6 point 15 (l. 711) ne portent que les nombres bruts 33, 7, 6 ; les mentions de « calibration » et de « taux » ailleurs concernent des seuils de moniteurs et des pièces de littérature. « 31 prédictions sur 31 » (simulation) et « 8 prédictions tenues sur 11 » (A1-v4) sont des décomptes propres à une épreuve, déjà admis par la contre-lecture de la v3 : à la mère de dire s'ils restent.

**VS-09 — état du bras : conforme.** § 2.5, première puce (l. 497) : « état du bras non vérifiable par la mère (cloison) ; ce qui a tourné ou non, et la phrase à dire au jury, reviennent à Lazar » ; § 7 point 9 (l. 738) de même ; la phrase ancienne est absente (garde). Le reste du § 2.5 et la l. 539 ne portent que des décisions inscrites ; le § 7 point 8 (l. 731) dit que les états du bras « sont ceux de la v2 », borné à la v3 par le point 9.

**VS-10 — en-tête.** « registre des décisions lu jusqu'à sa dernière ligne, R-2219 » : exact à 12:39:46, dépassé depuis (R-2220 à R-2222) ; le journal (§ 2 bis) le déclare. À relever dans la version suivante.

## Couples exacts (texte ancien trouvé une fois et une seule dans la v4, blancs normalisés ; contrôle par programme)

**VS-C1** (exigé) — § 1.4, « chiffres exacts », l. 206

~~~text
ANCIEN : est repris en v66, en cours, R-2215 —, témoin de Bailey 75
~~~

~~~text
NOUVEAU : est repris en v66, en cours, R-2215 ; la ligne exige aussi la « configuration v5 (`995eb918…`) », que le code v65 ne porte pas (sa configuration v5 a une autre empreinte, et la v66 la changera) : condition à faire préciser par Lazar avant toute course de l'organisme, R-2220 —, témoin de Bailey 75
~~~

**VS-C2** (facultatif) — § 4, chapeau, l. 532

~~~text
ANCIEN : T0.7, la règle « mots et coût », P3-bis et la consigne d'audit visés scellés le 12 au soir ;
~~~

~~~text
NOUVEAU : T0.7, la règle « mots et coût » (scellée dès le 10, R-2216), P3-bis et la consigne d'audit visés scellés le 12 au soir ;
~~~

**VS-C3** (facultatif) — § 6, point 5, l. 690

~~~text
ANCIEN : (brouillon 3, `defd8ef0…`, R-2210) rendus, non scellés ;
~~~

~~~text
NOUVEAU : (brouillon 3, `defd8ef0…`, R-2210) rendus en brouillons à empreinte, non scellés comme textes définitifs ;
~~~

**VS-C4** (facultatif) — § 6, point 5, l. 691

~~~text
ANCIEN : dernier non exécutable en l'état, R-2153) ; ligne `CODE-T07` non inscrite.
~~~

~~~text
NOUVEAU : dernier non exécutable en l'état, R-2153) ; ligne `CODE-T07` non inscrite (module rendu, commit seulement proposé, contre-lecture courte en cours, R-2220).
~~~

## Ce que je n'ai pas fait, et gestes à déclarer

- **Vérification courte** : la v4 n'a pas été relue en entier ; lus en entier son en-tête, le § 0, le § 1.3, le § 2.5, et chaque passage d'un couple modifié, d'un ajout ou d'un motif cherché. Les 38 couples tels quels n'ont pas été recontrôlés contre leurs sources (mandat de la contre-lecture de la v3). Aucun PDF ouvert.
- **Registre des décisions** : lu en entier de R-2206 à R-2222, plus R-2160, R-2162, R-2165 à R-2167 (débuts), R-2175, R-2177, R-2188, R-2190, R-2195, R-2204 ; non relu avant. R-2204 et la contre-lecture de la v3 portent des taux : vus parce que la consigne les donne à lire, repris nulle part.
- **Contre-lecture de la v3** : plan, en-tête, verdict et « Ce que j'ai vérifié » lus ; les 50 couples lus par le programme de l'annexe A, non un à un à l'œil.
- **Geste à déclarer** : `ls brouillons/entretien-taif-v3/` a affiché les noms du dossier, dont un nom contenant « pince-bras-attaque » : nom vu, fichier ni ouvert ni haché. L'addendum du bras B (audit de fuite, non le bras d'attaque) a été haché, non lu.
- Autres commits lus par `git show <commit>:<chemin>` seulement, sur la seule branche `prep/etat-de-l-art-niveau3-pieces-v1` (référence résolue par `git rev-parse --verify`) ; aucune écriture git, aucun appel de modèle ni d'interface externe, aucune dépense, aucune recherche récursive, `verifier-arbre` non lancé, suite d'essais non lancée ; aucun refus de contrôle de permissions ni de classifieur.
- Seul chemin écrit au dépôt : ce rapport et son compagnon `.sha256`. Bac à sable vidé à la fin.
