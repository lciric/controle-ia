# Journal — sections de résultats v4 (programme ; organisme d'idéation)

- Rédacteur : le sous-agent (Claude Opus 5.5) qui a écrit la v3, en continuité (R-2213). Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-sections-resultats-v3-v1.md` (`9db81855aebe778dd73fe225cacf1d18ea9d26e737d93f9d83306c264288b9ff`, égale à son compagnon), mêmes interdits ; message de la session mère du 10 novembre (application de la contre-lecture 1, décisions sur P-02, P-07 et les en-têtes).
- Contre-lecture appliquée : `prereg/contre-lectures/sections-resultats-v3-cl1.md` (`858d92be43a8521cb51c7b934e8a745e9d04555f9e13d2e84739df127470fc75`, égale à son compagnon ; Fable 5.2 ; « transmissible au jury après corrections »).
- Heures (relevées par `date -u`, 10 novembre 2026) : début 12:13:57 UTC ; relevé des statuts retenu à 12:24 UTC ; trois fichiers scellés à 12:24:38 UTC ; journal écrit ensuite.
- Aucun commit, aucune poussée, aucun `fetch`, aucun appel de modèle ni d'interface externe, aucune dépense. Aucun chemin interdit ouvert ; aucune recherche récursive ; `verifier-arbre` et suite d'essais non lancés.

## 1. Sorties (dossier `docs/notes/rapports-directeur/resultats-pour-documents-v4/`)

| fichier | empreinte |
|---|---|
| `section-resultats-programme-v4.html` | `e93b0901113da9400df0c28f551de2a8ee7f0fcb15d569eb65bfabbc3aa6690d` |
| `section-resultats-organisme-v4.html` | `77d0e57a87fedca4e1fdb878034d09d76454b28b8bccb99018b1a0603fb76241` |
| `registre-affirmations-v4.md` | `f7310529020768be44e48ef403037dc19038e9286322275d4a9f02cd287fd38f` |
| `journal-v4.md` | compagnon `.sha256` |

Les v3 sont intactes (vérifiées contre leurs compagnons à la fin).

## 2. Méthode et couples appliqués

Application **par programme** (script Python dans le bac à sable du rédacteur, `faire_v4.py`, `4821922e…` ; couples exportés en `couples-v4.json`, `689aa91a…` ; les deux restent hors du dépôt). Chaque texte ancien est cherché dans le texte courant au moment de son application. Le programme s'arrête s'il le trouve zéro fois ou plus d'une fois, et n'écrit alors rien. Aucun arrêt ne s'est produit. Le programme a tourné trois fois, sur un dossier v4 neuf à chaque fois, parce que les statuts ont bougé pendant le travail (R-2214, puis R-2215 et R-2216). Les fichiers v4 des deux premiers passages n'étaient pas scellés : je les ai retirés avant de rejouer. Seul le troisième passage est scellé.

Le texte neuf est la proposition de la contre-lecture, recopiée à l'identique (« verbatim »), sauf mention contraire. Les couples « E- » sont mes retouches. Chacune est déclarée ici : en-tête, ou statut relevé (CLR-02).

### Section programme

| n° | constat | application |
|---|---|---|
| E-01 | en-tête (CLR-16) | « relevé à 11:45 UTC ; version 3 » → « relevé à 12:24 UTC ; version 4 » |
| P-01 | CLR-16 | **modifié** sur décision de la mère : « contre-lu (cl1 `858d92be…`), corrections appliquées, vérification courte à venir » |
| E-02 | en-tête | « Il remplace la version 2, interrompue et jamais rendue. » → « Il remplace la version 3. » |
| P-02 | CLR-03 | **modifié** sur décision de la mère (« lecture retenue », sans attendre de confirmation) : « selon la lecture retenue de la réponse du directeur du 10 novembre, seuls des nombres bruts sont cités, sans taux [A91] » |
| P-17 | CLR-14 | verbatim |
| P-03 | CLR-11 | verbatim |
| P-04 | CLR-10 | verbatim |
| E-03 | statut | « Le premier brouillon du texte court » → « Le premier brouillon du texte qui préenregistre ces trois pièces » (le texte couvre le texte court, la relecture et le témoin : R-2194) |
| P-05 | CLR-02 | **modifié, statut relevé** : le brouillon 2 est remplacé par le **brouillon 3** (R-2210). Sont chiffrés : la relecture ≈ 2,4 à 4,6 dollars ; l'ensemble ≈ 11 à 17 dollars ; le pire cas ≈ 33 dollars, au-dessus du plafond de 30 dollars, gardé avec un ordre de sacrifice écrit (VA3 l. 222-223, 226 ; N-VA-1 (a)). S'ajoute la lecture large de GO-07 (R-2207). Le chiffre « 2,6 à 3,5 » de la contre-lecture est celui du brouillon 2 : il n'est plus l'état. |
| E-04 | statut | « Rien n'est scellé ni couru : » → « Aucun de ces textes n'est scellé comme préenregistrement, rien n'est couru : » (les brouillons ont un compagnon `.sha256`, aucun n'est un préenregistrement scellé) |
| P-06 | CLR-02 | **modifié, statut relevé** : brouillon 1 contre-lu (R-2200) ; brouillon 2 vérifié, « scellable après corrections », huit couples (R-2214) ; **brouillon 3 scellé le 10 novembre à 12:21 UTC, avant toute création de 7b** (R-2216 ; `registres/scellements-v1.md` l. 5 ; `72b067d5…`). La question de lecture est tranchée par le directeur : douze traits, « ajout permis » (R-2211). La consigne du code de la pièce reste à écrire (R-2216). |
| P-07 | CLR-01 | **modifié** sur décision de la mère : « une autre course » → « le témoin de l'attaque publiée de Bailey », mots de la ligne GO-2026-11-10-10 et rien d'autre. S'ajoutent « chacune sous ses conditions écrites » et « tout dépassement revient au directeur » (`registres/go.md` l. 300). |
| P-08 | CLR-02 | **modifié, statut relevé** : « Texte scellé le 10 novembre ; consigne de son code à écrire [A97] » |
| P-09 | CLR-02 | verbatim (état inchangé de R-2197 et R-2198 à R-2216) |
| P-10 | CLR-02 | **modifié, statut relevé** : « En cours : brouillon 3 rendu, à contre-lire sur ses changements [A97] » (R-2210) |
| P-11 | CLR-02 | **modifié, statut relevé** : brouillon 3 rendu (R-2212) ; restent une contre-lecture courte des écarts (Q16) et CLAF-18, à revérifier sur P3-bis scellé |
| P-12 | CLR-02 | **modifié, statut relevé** : « texte qui préenregistre le contrôle au brouillon 3, rendu, à contre-lire sur ses changements » |
| E-05 | statut | ligne 3 de la liste des changements : « la règle « mots et coût » est scellée à part depuis le 10 novembre, avant toute création de la course de confirmation » (R-2216) |
| P-18 | CLR-08 | **modifié** pour suivre la pièce (N3C l. 10-12) : « sans relecture de ses rapports **ni des PDF** par les auteurs de la synthèse, **qui les contrôleront avant la version finale** [A83] » |
| E-08 | statut | § 8 (i) : « elle sera scellée à part [A58] » → « elle est scellée à part depuis le 10 novembre [A58] [A97] » (R-2216) |
| P-13 | CLR-06 | verbatim |
| P-14 | CLR-13 | verbatim |
| P-15 | CLR-04 | verbatim |
| P-16 | CLR-05 | verbatim |

Note : l'ordre d'application suit l'ordre du fichier, pas l'ordre des numéros.

### Section organisme

| n° | constat | application |
|---|---|---|
| E-06 | en-tête | « relevé à 11:48 UTC ; version 3 » → « relevé à 12:24 UTC ; version 4 » |
| O-01 | CLR-16 | **modifié**, même formule que P-01 |
| E-07 | en-tête | « Il remplace la version 3. » |
| O-02 | CLR-12 | verbatim |
| O-03 | CLR-09 | verbatim |
| E-09 | statut | titre « Code v65 rendu le 10 novembre : non contre-lu. » → « … : contre-lu, à corriger. » (R-2215) |
| O-04 | CLR-02 | **modifié, statut relevé** : la contre-lecture du code v65 est **rendue** (R-2215 ; `contre-lecture-code-v65-v2.md`, `c4ddfc7f…`) : « utilisable pour la course après corrections ». Les essais, le banc et l'essai à blanc sont rejoués à l'identique. Deux bloquants : la lecture gelée peut rendre une issue sans qu'aucune loi fausse plantée ait été jugée (CLV65-01, l. 66), et un arrêt peut masquer une brèche (CLV65-02, l. 83). « Rien de cela ne touche une dépense » (l. 10). La v66 est confiée à un développeur neuf (décision de routine de la mère, R-2215). « Autre lignée » devient « autre modèle que celui du développeur » (R-2197 : Fable, autre modèle que les auteurs). |
| E-10 | statut | « elle attend le code contre-lu, » → « elle attend le code corrigé, » (CLV65 l. 12 : corrections exigées avant le scellement du texte de la course) |
| O-05 | CLR-07 | **modifié** : « sous ces mêmes conditions, la machine devant être validée par un essai à blanc du vrai bac à sable et la configuration de la course étant fixée [B51] ». Raison : GO-2026-11-10-10 (l. 300) exige en plus la validation par `--bac reel` et la configuration v5 ; « ces trois mêmes conditions » aurait omis cette dernière. |

## 3. Retouches du registre (`registre-affirmations-v4.md`)

- En-tête réécrit pour la v4.
- Pièces, par couples (même contrôle « une fois et une seule ») :
  - R-01 à R-03 : DEC, DEC3 et GO3 rehachés au relevé (`registres/decisions.md` `19bb7df8…`, dernière ligne R-2216 ; `registres/go.md` `2c396b01…`, l. 300) ;
  - R-04 : ETA retiré, plus cité.
- Pièces ajoutées après S7D :
  - VA3 (`defd8ef0…`, égal à son compagnon) ;
  - CL1 (`858d92be…`) ;
  - T08A (`prereg/T0.8-base-A-mots-et-cout-v1.md`, `72b067d5…`, égal à son compagnon et à la ligne `SCELLEMENT-T08-BASE-A`) ;
  - CLV65 (`c4ddfc7f…`, égal à son compagnon).
- Rangées demandées par la contre-lecture :
  - A46 (T07B21 l. 877-878, l. 1024) ;
  - A66 ;
  - A91 (R-2195, R-2213) ;
  - A95 (R-2206, R-2213, `registres/go.md` l. 300 ; « non inscrite » retiré) ;
  - A97 (R-2193 à R-2216 selon l'objet ; « contre-lecture du code v65 non relancée » retiré) ;
  - B14 (V9 l. 12-13) ;
  - B49 (R-2215 ; CLV65) ;
  - B51 (`registres/go.md` l. 273, l. 300 ; CLV65 l. 12).
- Numéros de ligne selon CLR-15 :
  - N-064 : B1 et B2 → l. 13 ; B41 → l. 15 ; B45 → l. 13-15 ;
  - N-065 : B4 → l. 15-18 ;
  - A40 → DEC3 R-2186 (l. 2144) au lieu de `registres/etat.md` l. 3 ;
  - B39 → DEC3 R-2162 (l. 2120, « deux décisions ouvertes ») au lieu de `registres/etat.md` l. 414.
- Retouches de ma part, même cause, déclarées :
  - B5 (N064 l. 17 → l. 14) et B42 (N064 l. 16 → l. 13) : même décalage, que la contre-lecture n'a pas listé ;
  - A19 (« quantiles 0,95 du plancher »), A32 (audit structurel), A76 (« méthodes »), A78 (0,072 contre 0,05 ; proposition 2 (a)), A81 (« alerte plus tôt ») et A83 (N3C l. 10-12, 21-29) : ces rangées suivent les couples P-03, P-04, P-13, P-16, P-14 et P-18.

Contrôle par script : tout renvoi `[A…]` ou `[B…]` des deux sections a sa rangée. Les balises HTML sont équilibrées.

## 4. Statuts relevés (12:24 UTC ; `registres/decisions.md` jusqu'à R-2216, `registres/go.md` jusqu'à l. 300, listes de fichiers)

| objet | état écrit | source |
|---|---|---|
| Enveloppe de 120 dollars | inscrite, GO-2026-11-10-10 | R-2206 ; go l. 300 |
| Validité de l'adaptateur | brouillon 3 rendu ; contre-lecture différentielle à faire sur T0.7 scellé ; lecture large de GO-07 | R-2207, R-2210 ; VA3 |
| Base (A) « mots et coût » | **scellée** à 12:21:55 UTC, avant toute création de 7b ; douze traits (CLBA-04 (a)) ; consigne du code à écrire | R-2211, R-2214, R-2216 ; `registres/scellements-v1.md` l. 5 |
| Consigne de l'audit des fuites | brouillon 3 rendu ; Q16 et CLAF-18 restants | R-2212 |
| Témoin positif (P3-bis) | brouillon 11 ; quatrième contre-lecture rendue, un obstacle de procédure levé | R-2197, R-2198 ; aucun brouillon 12 sur disque |
| Code v65 de l'organisme | contre-lu, « utilisable pour la course après corrections », v66 confiée | R-2215 ; CLV65 |
| Texte « accumulation », saboteur à budget | inchangés : aucun rendu inscrit jusqu'à R-2216 ; aucun `brouillons/accumulation-v1/` | `ls` vers 12:17 UTC |
| Verdict de T0.3 | toujours absent de `docs/verdicts/` sur `main` | `ls` vers 12:17 UTC |
| Course 7b | non créée (aucune ligne de création) | registre jusqu'à R-2216 |

Lu et **non repris**, exprès :
- R-2214 (2) porte sur la session du bras d'attaque et sur le devis du témoin de Bailey. Les sections ne disent du bras que ses décisions inscrites ; de Bailey, seulement les mots de la ligne GO-2026-11-10-10.
- R-2215 (2), le pilier « mathématiques nouvelles » de l'organisme, est hors du champ de ces sections.
- R-2195 et R-2199 (même pilier) : pas repris non plus.

## 5. Ce qu'un vérificateur court doit relire

1. **Rejeu des couples** : pour chaque ligne des tables du § 2, le texte neuf figure une fois dans la v4, l'ancien n'y figure plus, et rien d'autre n'a changé hors de ces zones (différence v3 → v4).
2. **Couples modifiés** (P-01, P-02, P-05 à P-08, P-10 à P-12, P-18, O-01, O-04, O-05) et retouches E-01 à E-10 : chaque phrase contre sa source au § 2 et au § 4. En particulier :
   - P-05 contre VA3 l. 222-223, 226 et R-2210 (ordre de sacrifice : « deux doses du témoin, une sonde de la relecture ») ;
   - P-06 contre R-2211, R-2214, R-2216 ;
   - O-04 contre CLV65 l. 10, 14-15, 66, 83 (je rends « prononcer C1 » par « rendre une issue », sans dire quelle issue est C1).
3. **Statuts** : lignes de `registres/decisions.md` après R-2216 et de `registres/go.md` après l. 300, arrivées après mon relevé de 12:24 UTC, qui rendraient une phrase fausse.
4. **Bailey** : la v4 n'en dit que les mots de la ligne GO-2026-11-10-10 (décision de la mère, travail publié) ; rien du devis ni du bras.
5. **Registre** : numéros de ligne de N-064 et N-065 (B1, B2, B4, B5, B41, B42, B45), et rangées A40 et B39 renvoyées à des lignes R-.
6. **« 0,660 »** dans la table du § 5 de la section programme : aire minimale détectable des autres sondes de T0.7 (A67), présente depuis la v3. Ce n'est pas la variante de taux de R-2204.

## 6. Réserves

- **Non vérifié** par un autre lecteur : la v4 attend la vérification courte (R-2213).
- Les statuts sont ceux de 12:24 UTC. Ils ont bougé trois fois pendant ce travail ; ils peuvent bouger encore avant la transmission.
- CLR-17 (« Caught in the Act », point à 9 milliards en figure seulement) n'est pas appliqué : « information, non exigé ».
- Le travail a été réécrit deux fois sur des fichiers v4 non scellés de ce même travail (§ 2). Aucun fichier scellé n'a été réécrit ; les v3 sont intactes.
- Rien n'a été lu des pièces du bras d'attaque, de 7a, de la mesure unanime ni de l'étiqueteur.
