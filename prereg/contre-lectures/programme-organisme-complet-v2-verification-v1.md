# Rapport de vérification — programme complet de l'organisme, v2

## En-tête

- **Rôle** : rédacteur neuf du rapport de vérification. Je n'ai écrit ni le texte vérifié, ni son registre des affirmations, ni l'inventaire qu'il reprend. Je n'ai pas refait la vérification : je consigne les résultats des vérificateurs et des sceptiques, tels qu'ils m'ont été remis.
- **Modèle** : Fable 5.2 (`claude-fable-5-2`).
- **Heure** : 2026-11-10 13:22 UTC (relevée par `date -u`).
- **Texte vérifié** : `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v2.md`, sha256 `dffe0b632bfa24ffa5af3e460110515e05dfc74283d856a15eba01afab168556` (recalculée par moi : conforme).
- **Registre des affirmations** : `docs/notes/rapports-directeur/programme-organisme-complet-v1/registre-affirmations-programme-v2.md`, sha256 `4594a5cd5800ab4559bbb24ebd279ee965283694cabd019b68a297db9d778bef` (recalculée par moi : conforme).
- **Méthode** : le texte est découpé en six tranches (I-a, I-b, I-c, I-d pour la partie I ; II-a, II-b pour la partie II). Un vérificateur par tranche compare chaque affirmation à sa pièce (renvoi [RAn] du registre des affirmations ; clés du § II.1 en partie II). Un sceptique par tranche tente ensuite de réfuter chaque écart signalé, à la source. **Seuls les constats tenus après cette tentative comptent** ; un constat réfuté n'est pas repris. Chaque couple « ancien → nouveau » a été compté présent une seule fois dans le texte par le sceptique.
- **Règles suivies** : fichier des interdits communs v2 lu en entier ; cloison du bras d'attaque (R-2152, R-2170) ; aucune branche autre que la tête de main ; rien sous `donnees/`, `diag/`, `runs/` ; aucune sortie payée et non lue ouverte ; aucun taux de calibration dans ce rapport ; niveau méthode pour toute attaque (R-607) ; aucun appel externe ; aucune écriture git. Seul fichier écrit : ce rapport et son empreinte compagnon.
- **Réserve de rédaction** : je n'ai rouvert aucune pièce citée ; les numéros de lignes, les empreintes abrégées et les citations ci-dessous sont ceux des sceptiques.

## Verdict

**Transmissible après corrections.**

42 constats tenus : 1 bloquant, 17 à corriger, 24 mineurs. Aucun ne renverse une conclusion du programme ; ils portent sur des états périmés (le registre des décisions a avancé jusqu'à R-2226 après la remise du texte), sur quelques formules plus fortes que leurs pièces, et sur des renvois.

Liste exacte des couples à appliquer avant transmission (le bloquant et les 17 « à corriger ») : VP-01 à VP-18, donnés mot pour mot plus bas. Les 24 mineurs (VP-19 à VP-42) sont à appliquer dans la même passe ; ils ne conditionnent pas la transmission.

Trois points à trancher par celui qui corrige, avant d'appliquer :

1. **Identité « à l'octet » de la partie II (ligne 853).** Le sceptique de la tranche II-a a refusé de toucher au texte repris de l'inventaire v7 et a déplacé ses corrections dans le préambule (VP-01). Le sceptique de la tranche II-b a, lui, gardé douze couples qui modifient ce même texte repris (VP-14 à VP-18, VP-37 à VP-42 et la moitié de VP-15). Les deux choix ne sont pas cohérents entre eux. Appliquer les couples de II-b rompt l'identité annoncée à la ligne 853 et au titre de la ligne 862 : il faut alors amender ces deux déclarations et le dire au journal ; sinon, porter ces douze corrections dans le préambule, à la manière de VP-01.
2. **Lignes 181 et 243**, hors des tranches qui l'ont relevé : elles portent le même état « en cours » de la lecture du tour 2 N12-N13 que VP-10 et VP-11 corrigent. Aucun couple ne m'a été remis pour elles : à aligner à la main.
3. **Lignes 428 et 752** portent la même formule sur le bac à sable ; VP-04 et VP-12 les corrigent séparément, dans des termes voisins mais non identiques : à harmoniser si souhaité.

Le registre des affirmations v2 porte lui-même quatre entrées à reprendre (hors du texte) : RA65 et RA89 périmées depuis R-2215, RA110 (« R-964 » au lieu de R-1036), RA127 (« l. 8 » au lieu de l. 7).

## Bilan par tranche

| Tranche | Vérifiées | Conformes | Signalées | Tenues | Réfutées |
|---|---|---|---|---|---|
| I-a (lignes 1 à 264) | 141 | 136 | 5 | 4 | 1 |
| I-b | 214 | 206 | 8 | 8 | 0 |
| I-c | 236 | 227 | 9 | 9 | 0 |
| I-d | 106 | 96 | 10 | 8 | 2 |
| II-a | 272 | 263 | 9 | 1 | 9 |
| II-b | 219 | 208 | 12 | 12 | 0 |
| **Total** | **1 188** | **1 136** | **53** | **42** | **12** |

Lecture de la table :

- Les décomptes sont des pointages à la main des vérificateurs, à quelques unités près.
- Tranche II-a : les neuf écarts signalés sont **exacts sur le fond** (aucun n'a pu être réfuté à la source) ; ce sont leurs neuf couples qui ont été refusés, parce qu'ils modifiaient le texte recopié de l'inventaire. Ils sont fusionnés en un seul constat tenu, VP-01, placé dans le préambule. D'où « 9 signalés, 1 tenu, 9 réfutés » : la somme ne se lit pas comme dans les autres tranches.
- Tranche II-b : 229 éléments (209 entrées, 20 chiffres du décompte), dont 10 non vérifiables retirés ; 12 constats touchent 11 entrées (deux sur BOU-005).
- Répartition des tenus par gravité : bloquant 1 (II-a) ; à corriger 17 (I-a 2, I-b 4, I-c 2, I-d 3, II-b 6) ; mineur 24 (I-a 2, I-b 4, I-c 7, I-d 5, II-b 6).

## Constats tenus

Format : lignes du texte ; renvoi ; source ; problème ; couple ancien → nouveau (mot pour mot).

### Bloquant

#### VP-01 — Statuts de l'inventaire déjà périmés à sa date de lecture, non déclarés (tranche II-a)

- **Lignes** : 858-860 (préambule de la partie II), pour les entrées des lignes 872, 912, 975, 1048, 1059, 1124, 1130, 1152, 1153.
- **Renvoi** : ATQ-016, ATQ-038, ATQ-039, ARC-013, JUG-001, et quatre renvois imprécis.
- **Source** : `registres/decisions.md` (fichier vivant, `cbd3f950…` à la lecture du sceptique, 2 184 lignes) : ligne 1117 (R-888, 31 octobre : « R-611 levée »), 1118 (R-889), 2104 (R-2146), 862 (R-634), 1984 (R-2026), 2171 (R-2213), 2158 (R-2200) ; `docs/decisions/proposition-P-036-couche-2-preparation-v2.md:41-42` (`155f0511…`) ; `registre-affirmations-v3.md:232` (`38c24c92…`) ; `synthese-collisionneur-question-mere-v2-v1.md:70-71, 182` (`25e2d351…`) ; `verdict-officiel-a1-v4-v1.md:36` (`e6e2f170…`).
- **Problème** : cinq entrées donnent pour actuel un état périmé : ATQ-016, ATQ-038 et ATQ-039 citent R-611 comme en vigueur alors qu'elle a été levée le 31 octobre ; ARC-013 et JUG-001 sont dites « proposé non tranché » alors que le directeur a tranché (R-634, R-2026). Ces états étaient déjà périmés dans la plage que l'inventaire dit avoir lue (jusqu'à R-2200 environ) : la mise en garde actuelle du préambule ne les couvre pas, et la partie I ne dit rien de R-611 ni de D1 de P-036. Le texte se contredit en outre (OUT-024, ligne 1403 : « plus tard levée (R-888) »). Les neuf couples d'origine modifiaient le texte déclaré recopié « à l'octet » (ligne 853 ; titre de la ligne 862) ; la correction est donc portée dans le préambule, texte propre de l'auteur.
- **Ancien** :
```
en cas d'écart, la partie I prime pour l'état, l'inventaire pour l'idée.
```
- **Nouveau** :
```
en cas d'écart, la partie I prime pour l'état, l'inventaire pour l'idée ; (3) statuts de l'inventaire déjà périmés à sa date de lecture, laissés tels quels pour garder l'identité à l'octet : ATQ-016, ATQ-038 et ATQ-039 citent R-611 comme en vigueur, alors qu'elle a été levée le 31 octobre (R-888 ; examen final et estimation de la malléabilité dits hors gel par R-889 ; restriction levée pour le bras d'attaque par R-2146 ; OUT-024 le dit) ; ARC-013 : D1 tranchée (b) par le directeur (R-634), chaque lancement restant sous son GO ; JUG-001 : décidé (R-2026), conception v3 et devis à écrire ; (4) renvois imprécis de l'inventaire, laissés tels quels : la copie DEC de 2 171 lignes va jusqu'à R-2213 ; `[Bn]` est à la ligne 187 + n pour B46 à B53 ; ROL-035 se lit QM:70-71, 182 ; la citation d'ATQ-010 omet « sous v9 » (A4V:36).
```

### À corriger

#### VP-02 — Le texte v2 renvoie au registre des affirmations v1 (tranche I-a)

- **Lignes** : 15-17. **Renvoi** : aucun (en-tête, « Sources »).
- **Source** : registre des affirmations v2, l. 3-5 et 196-205 (`4594a5cd…`) ; registre v1 du même dossier (`18e06990…`) ; `registres/decisions.md:2181` (R-2223).
- **Problème** : les renvois RA134 à RA143, appelés dès le verdict (l. 32 et 40), n'existent que dans le registre v2, compagnon déclaré de la v2 ; le registre v1 n'en contient aucun. Un lecteur qui suit le renvoi ne les trouve pas.
- **Ancien** :
```
(`registre-affirmations-programme-v1.md`), qui donne
```
- **Nouveau** :
```
(`registre-affirmations-programme-v2.md`, `4594a5cd…`), qui donne
```

#### VP-03 — « Juge attaqué et réparé » : plus fort que la pièce (tranche I-a)

- **Lignes** : 29-32. **Renvoi** : RA1, RA2, RA3, RA134.
- **Source** : `/home/user/ideation-organism/README.md:9` (`b72c983e…`) ; registre des affirmations v2, l. 64 (RA2).
- **Problème** : la page publique dit que le nul v9 qui ferme la brèche a rendu « power lost » à sa validation décisive, que le v8 reste le nul de production tant que le directeur n'a pas décidé du prix, et que le v9, attaqué à son tour, a sa frontière déclarée « crossed, robust ». Le juge de production n'est donc pas réparé ; la fin de la même phrase du texte (v8 en production, v9 candidat) contredit « réparé ».
- **Ancien** :
```
dont le juge a été attaqué et réparé
```
- **Nouveau** :
```
dont le juge a été attaqué, la réparation (nul v9) restant candidate et non en production
```

#### VP-04 — « Le vrai bac n'a jamais tourné » : plus fort que les pièces (tranche I-b)

- **Lignes** : 428-429. **Renvoi** : RA19, RA65.
- **Source** : `/home/user/ideation-organism/orchestrator/pole/tests_de_mort_v2.py:4, 977, 1277-1278` (`363a3725…`) ; `tests_de_mort_v3.py:9-11` (`ea05eb55…`) ; `orchestrator/essais/test_v51_bac_reel.py` ; `essais/test_v52b_borne_memoire.py` ; `README.md:69, 118, 132` (`b72c983e…`).
- **Problème** : les gardes du bac ont été éprouvées sous un vrai `bwrap` 0.9.0 aux v51 (CL15) et v52b (CL16). La page publique dit seulement que l'étage des tests de mort et la boucle n'ont jamais tourné en réel, et que le vrai bac n'a pas tourné « avec cet étage ».
- **Ancien** :
```
**le vrai bac n'a jamais tourné**
```
- **Nouveau** :
```
**l'étage des tests de mort et la boucle n'ont jamais tourné en réel** ; seules les gardes du bac ont été éprouvées sous un vrai `bwrap` 0.9.0, aux v51 et v52b (contre-lectures CL15 et CL16)
```

#### VP-05 — « Six brouillons, chacun contre-lu » (tranche I-b)

- **Lignes** : 441. **Renvoi** : RA85.
- **Source** : `/home/user/ideation-organism/orchestrator/prereg/` (contre-lectures v1, v2, v3, courtes v5 et v6 ; brouillons 1 à 6) ; commits `7e357d1`, `82ad7a8`, `8261c30`, `171b856`, `d54b85c` à la tête `6510199`.
- **Problème** : six brouillons, mais cinq contre-lectures dans l'arbre public (brouillons 1, 2, 3, 5 et 6) ; le brouillon 4 n'a pas de contre-lecture propre. Les deux dernières disent « scellable après couples » et le commit `d54b85c` « Nothing sealed » : l'arbre public ne contient aucun préenregistrement scellé du tour fermé. « Non scellé » est borné à l'arbre public, seul vérifié.
- **Ancien** :
```
préenregistrement en six brouillons, chacun contre-lu
```
- **Nouveau** :
```
préenregistrement en six brouillons, aucun scellé dans l'arbre public ; cinq contre-lectures (brouillons 1, 2, 3, 5 et 6 ; aucune propre au brouillon 4), la dernière « scellable après couples »
```

#### VP-06 — Les six témoins du pont ne sont plus « à écrire » (tranche I-b)

- **Lignes** : 409-410. **Renvoi** : RA50.
- **Source** : `/home/user/ideation-organism/pont-fiche-loi-v1/LISEZMOI-pont-v1.md:41` (`7b1c131d…`) ; `registres/decisions.md:1215` (R-986) ; `registres/go.md:183` (GO-2026-11-01-09) ; `registres/depenses.md:302-303`.
- **Problème** : périmé. L'épreuve fraîche du 1er novembre au soir a servi les six témoins (L1 : 6 justes sur 6), ce que le même paragraphe du texte rapporte quatre lignes plus haut (l. 403-404).
- **Ancien** :
```
six témoins du pont par un metteur en forme tiers,
```
- **Nouveau** :
```
(les six témoins du pont, « à écrire » selon le LISEZMOI, ont depuis servi à l'épreuve fraîche : L1, 6 justes sur 6),
```

#### VP-07 — « D-P2 à D-P5 attendent aussi » (tranche I-b)

- **Lignes** : 408. **Renvoi** : RA81.
- **Source** : `LISEZMOI-pont-v1.md:34-35, 42` (`7b1c131d…`) ; `registres/go.md:183` ; `registres/decisions.md:1215, 1217, 1219` (R-986, R-988, R-990) ; `registres/etat.md:198`.
- **Problème** : périmé pour D-P5 (nœud « premier essai, devis et GO » : ce premier essai a reçu son GO et a couru), sans source pour D-P2 à D-P4 (aucune ligne des registres ne les nomme ; seul D-P1 y figure). Le lien entre D-P5 et GO-2026-11-01-09 est une lecture : la ligne de GO ne nomme pas D-P5 ; le remplacement est adouci en conséquence.
- **Ancien** :
```
D-P2 à D-P5 attendent aussi
```
- **Nouveau** :
```
le premier essai que visait D-P5 (devis et GO) a reçu GO-2026-11-01-09 et a couru ; D-P2 à D-P4, « défaut sous 48 heures » selon le LISEZMOI du pont, n'ont aucune ligne au registre
```

#### VP-08 — « Deux mondes jouets » pour la lecture du v9 (tranche I-c)

- **Lignes** : 507-509. **Renvoi** : RA100.
- **Source** : `docs/notes/rapports-directeur/resultats-pour-documents-v3/section-resultats-organisme-v3.html:64` (`d6d702f5…`, [B27]) ; `/home/user/ideation-organism/resultats/attaque-goodhart-v2/README.md:11, 17` (`c549a31b…`).
- **Problème** : plus fort que la source. Les deux pièces précisent que la phrase gelée a été écrite pour deux mondes dans le nul v9 et que, dans cette course, W2 seul y est ; sur W2 gradué, une promotion sous v9 n'est pas fausse par construction. Le texte garde « deux mondes » sans cette réserve.
- **Ancien** :
```
sur deux mondes jouets, un fournisseur, une forme d'optimisation
```
- **Nouveau** :
```
sur un monde jouet dans le nul v9 (W2 ; le texte gelé dit « deux mondes jouets au nul v9 », mais dans cette course W2 seul l'est), un fournisseur, une forme d'optimisation
```

#### VP-09 — La table des GO ouverts du § 8.3 se lit comme complète (tranche I-c)

- **Lignes** : 621-634. **Renvoi** : RA120.
- **Source** : `registres/go.md` (`2c396b01…`), l. 199, 200, 207, 222, 224-238, 277-279, 281.
- **Problème** : d'autres lignes de type « calcul » qui touchent l'organisme sont encore dans leur échéance au 10 novembre, sans révocation au registre. Le § 8.2 se dit « non exhaustive », le § 8.3 non. Le remplacement d'origine citait une plage qui incluait GO-2026-11-03-03 (hors organisme) ; le sceptique l'a corrigé.
- **Ancien** :
```
### 8.3 Lignes de GO de l'organisme encore ouvertes
```
- **Nouveau** :
```
### 8.3 Lignes de GO de l'organisme encore ouvertes (principales ; liste non exhaustive : restent aussi dans leur échéance au registre des GO les lignes d'A1-bis GO-2026-11-02-11 et -12, du tour fermé à 15 USD GO-2026-11-02-19, des courses et collisionneurs sur les questions des mentors GO-2026-11-03-02 et -04 à -18, et du pilier attaque GO-2026-11-08-06, -07, -08 et -10)
```

#### VP-10 — Couche 4 : pas (a) fait, pas (b) lancé (tranche I-d)

- **Lignes** : 727. **Renvoi** : RA22, RA5, RA28, RA134 (table du § 9).
- **Source** : `registres/decisions.md:2184` (R-2226, 13:00 UTC ; registre `cbd3f950…`, 2 184 lignes) ; synthèse `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md`, sha256 `6ef6bc2e1cbea69b0b47f20508fa09391e7c2271785287c470dc632de5a2b1ce` (empreinte recalculée par le sceptique, contenu non ouvert).
- **Problème** : état périmé par une ligne du registre postérieure au texte (rendu à 12:49 UTC, R-2223). Le même état « en cours » figure aux lignes 181 et 243, sans couple remis (voir le verdict, point 2).
- **Ancien** :
```
(a) lecture du tour 2 N12-N13 en cours, (b) devis de l'essai Lean, (c) note du pilier « génération »
```
- **Nouveau** :
```
(a) lecture du tour 2 N12-N13 faite (synthèse scellée `6ef6bc2e…`, R-2226), (b) devis de l'essai Lean en écriture (rédacteur neuf lancé, R-2226), (c) note du pilier « génération »
```

#### VP-11 — Annexe A : le tour 2 N12-N13 n'est plus « non lu » (tranche I-d)

- **Lignes** : 779. **Renvoi** : RA123, RA28, RA134.
- **Source** : `registres/decisions.md:2184` (R-2226) et `:2173` (R-2215) ; `registres/depenses.md:319`.
- **Problème** : état périmé : depuis R-2226, cette sortie est lue et sa synthèse scellée. Montant, GO, branche et commit conformes au registre des dépenses.
- **Ancien** :
```
| lecture en cours : critères scellés (`6bdbfe47…`), lecteur neuf lancé (R-2215) | [RA123, RA28, RA134] |
```
- **Nouveau** :
```
| **lue le 10 novembre** : synthèse scellée par un lecteur neuf (`6ef6bc2e…`, R-2226), sous les critères scellés `6bdbfe47…` (R-2215) | [RA123, RA28, RA134] |
```

#### VP-12 — Bac à sable `bwrap` « jamais joué en vrai » : formule sans borne (tranche I-d)

- **Lignes** : 752. **Renvoi** : RA19, RA65 (table du § 9).
- **Source** : `registres/decisions.md:1024` (R-796) et `:1025` (R-797) ; `/home/user/ideation-organism/README.md:118, 132` ; `docs/notes/organisme-boucle-reelle-v1/code-v65/contre-lecture-code-v65-v2.md:60, 125, 166-172`.
- **Problème** : le registre rapporte un `bwrap` vérifié fonctionnel et trois contre-lectures de l'orchestrateur faites sous un vrai `bwrap`. Ce qui est établi, c'est qu'aucune course réelle ne l'a employé. Même formule à la ligne 428 (VP-04).
- **Ancien** :
```
| bac à sable `bwrap` | codé ; jamais joué en vrai |
```
- **Nouveau** :
```
| bac à sable `bwrap` | codé ; contre-lectures CL13 à CL15 de l'orchestrateur faites sous un vrai `bwrap` (R-797) ; jamais joué dans une course réelle, essais du vrai bac déclarés non joués pour la v65 |
```

#### VP-13 — BOU-005 : dépense et contre-lecture de la première course réelle (tranche II-b)

- **Lignes** : 1189. **Renvoi** : BOU-005.
- **Source** : `registres/decisions.md:2173` (R-2215) et `:2164` (R-2206) ; `registres/go.md:299` (GO-2026-11-10-09) et `:300` (GO-2026-11-10-10) (`2c396b01…`).
- **Problème** : « interrompue par la fin du quota » est périmé (contre-lecture rendue, R-2215). Pour la dépense, le texte n'est pas faux mais il manque la ligne propre : 45 USD sous GO-2026-11-10-10, échéance 30 novembre, conditions de GO-2026-11-08-02. Les deux enveloppes sont gardées.
- **Ancien** :
```
dépense sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre ; contre-lecture du code lancée puis interrompue par la fin du quota
```
- **Nouveau** :
```
dépense de 45 USD au plus (GO-2026-11-08-02, repris par GO-2026-11-10-10, R-2206, jusqu'au 30 novembre), inscrite sur devis dans l'enveloppe de calcul accordée jusqu'au 27 novembre (GO-2026-11-10-09) ; contre-lecture du code rendue le 10 novembre (R-2215 : utilisable après corrections, v66 lancée)
```

#### VP-14 — BOU-003 : code v65 « non contre-lu » (tranche II-b)

- **Lignes** : 1187. **Renvoi** : BOU-003.
- **Source** : `registres/decisions.md:2173` (R-2215, 10 novembre 12:20 UTC).
- **Problème** : périmé ; la ligne contredit aussi la partie I du même texte (l. 327 et 757 : « contre-lu »).
- **Ancien** :
```
codé (branche prep/organisme-v65-v1, tête 3daf08e24) ; non contre-lu
```
- **Nouveau** :
```
codé (branche prep/organisme-v65-v1, tête 3daf08e24) ; contre-lu le 10 novembre (R-2215 : « utilisable pour la course après corrections », bloquants CLV65-01 et CLV65-02) ; v66 lancée sous noms neufs
```

#### VP-15 — MAT-002 : pilier « mathématiques nouvelles », pas (a) (tranche II-b)

- **Lignes** : 1324. **Renvoi** : MAT-002.
- **Source** : `registres/decisions.md:2184` (R-2226, dernière ligne du registre).
- **Problème** : périmé. Le pas (a) est fait (synthèse du tour 2 scellée, `6ef6bc2e…`) ; le pas (b) est lancé.
- **Ancien** :
```
décidé (R-2199) ; (a) lancé le 10 novembre
```
- **Nouveau** :
```
décidé (R-2199) ; (a) fait le 10 novembre (R-2226 : synthèse du tour 2 N12-N13 scellée) ; (b) lancé (dessin et devis en rédaction, aucune dépense avant GO)
```

#### VP-16 — OUT-006 : écart d'A1-v4 déjà tranché (tranche II-b)

- **Lignes** : 1385. **Renvoi** : OUT-006.
- **Source** : `registres/decisions.md:2001` (R-2043, 9 novembre 21:03 UTC).
- **Problème** : périmé. Lazar a tranché l'option (a) le 9 novembre. L'entrée OUT-030 du même inventaire (l. 1409) le dit : les deux lignes se contredisent.
- **Ancien** :
```
proposé, défaut (a) le 11 novembre ; leçon écrite
```
- **Nouveau** :
```
tranché par Lazar le 9 novembre : option (a) (R-2043, voir OUT-030) ; leçon écrite
```

#### VP-17 — OUT-007 : collisionneur en mode critique, décidé (tranche II-b)

- **Lignes** : 1386. **Renvoi** : OUT-007.
- **Source** : `registres/decisions.md:1984` (R-2026, 9 novembre 17:17 UTC) ; `registres/go.md:290` (GO-2026-11-09-05).
- **Problème** : périmé. Lazar a dit « go » ; le GO est inscrit. Aucune ligne ne consigne le tour en mode critique comme couru.
- **Ancien** :
```
confiance 0,7 | proposé non tranché | RPG:42, 120-122, 188
```
- **Nouveau** :
```
confiance 0,7 | décidé (« go » de Lazar le 9 novembre, R-2026 ; GO-2026-11-09-05) ; aucun tour en mode critique consigné comme couru au registre | RPG:42, 120-122, 188
```

#### VP-18 — OUT-049 : « la relecture reste » contraire à la pièce citée (tranche II-b)

- **Lignes** : 1428. **Renvoi** : OUT-049.
- **Source** : `registres/decisions.md:770` (R-546) et `:776` (R-552). PCO:14-15 est sur une autre branche, non ouverte.
- **Problème** : si « relecture » désigne la contre-lecture du texte, c'est contraire à R-546, qui lève R1 « et la contre-lecture du texte (R2) qui s'y attache » ; R-552 le redit. La seule relecture que R-552 dit maintenue est celle de la lecture mécanique (R13).
- **Ancien** :
```
(27 octobre, R-546) ; la relecture reste.
```
- **Nouveau** :
```
(27 octobre, R-546) ; la contre-lecture du texte (R2) qui s'y attache est levée aussi (lecture de conv-audit consignée en R-546, redite en R-552) ; les autres règles restent (lecture dans les deux sens, gardes, empreintes, rien d'écrasé, aucun run visant un signe).
```

### Mineurs

#### VP-19 — Mots de Lazar : segment qui n'est pas de lui (tranche I-a)

- **Lignes** : 93-95. **Renvoi** : RA12.
- **Source** : `docs/decisions/decision-N-044-v1.md:8-9, 22-23` (`2b70bdac…`).
- **Problème** : dans N-044, le segment sur l'universalité est entre crochets à l'intérieur de la citation : c'est la proposition à laquelle Lazar répond. La note dit aussi que ces mots sont rapportés par relais (R-331).
- **Ancien** :
```
(25 octobre, 00:05) l'universalité
```
- **Nouveau** :
```
(25 octobre, 00:05 ; mots rapportés par relais, le premier segment étant la proposition à laquelle il répond, entre crochets dans N-044) l'universalité
```

#### VP-20 — Renvoi RA32 erroné pour la fermeture de la couche 4 (tranche I-a)

- **Lignes** : 231-232. **Renvoi** : RA32.
- **Source** : registre des affirmations v2, l. 94 (RA32) et l. 67 (RA5) ; `registres/decisions.md:1188` (R-959, points (1) et (5)).
- **Problème** : RA32 porte sur la durée des tests de mort, sans rapport ; le fait est entièrement couvert par RA5.
- **Ancien** :
```
[RA5, RA32]
```
- **Nouveau** :
```
[RA5]
```

#### VP-21 — « Scripté 5/35 » : lequel des deux bras scriptés (tranche I-b)

- **Lignes** : 275. **Renvoi** : RA37.
- **Source** : `docs/notes/ideation-organisme-v1/orchestrateur-v52b/LISEZMOI-orchestrateur-pole-v7-v7.md:15, 20-22` (`4bc261a0…`).
- **Problème** : chiffres conformes, mais la démonstration a quatre bras, dont deux scriptés.
- **Ancien** :
```
scripté 5/35
```
- **Nouveau** :
```
scripté avec exploration 5/35 (scripté aveugle 2/35)
```

#### VP-22 — Il n'existe pas de `budget_v55.py` (tranche I-b)

- **Lignes** : 300. **Renvoi** : RA54.
- **Source** : `/home/user/ideation-organism/orchestrator/pole/` (tête `6510199`) ; registre des affirmations v2, l. 116.
- **Ancien** :
```
`budget_v53.py` à `_v56.py`
```
- **Nouveau** :
```
`budget_v53.py`, `_v54.py`, `_v56.py`
```

#### VP-23 — `lecteur_tables` n'est pas le nom du rôle (tranche I-b)

- **Lignes** : 280. **Renvoi** : RA42.
- **Source** : `/home/user/ideation-organism/orchestrator/pole/juges_idees_v2.py:1375-1384` (`57e4474a…`).
- **Problème** : c'est un juge scripté du contrôle de diagnosticité, de rôle « temoin ».
- **Ancien** :
```
**juges d'idée v2** (`lecteur_tables`)
```
- **Nouveau** :
```
**juges d'idée v2** (`lecteur_tables` y est le juge scripté témoin du contrôle de diagnosticité)
```

#### VP-24 — Plages de versions du cœur et de la lecture gelée (tranche I-b)

- **Lignes** : 326. **Renvoi** : RA64.
- **Source** : `orchestrator/pole/` : `tour_ferme_v61.py` à `_v64.py`, `lecture_tour_ferme_v60.py` à `_v63.py`, `adaptateur_commande_v64.py`. La ligne 289 du texte donne les bonnes plages.
- **Ancien** :
```
cœur et lecture gelée (v61-v63), adaptateur de commande (v64)
```
- **Nouveau** :
```
lecture gelée (v60-v63), cœur (v61-v64), adaptateur de commande (v64)
```

#### VP-25 — Classes non couvertes par le v9 : liste périmée (tranche I-c)

- **Lignes** : 501. **Renvoi** : RA101.
- **Source** : `/home/user/ideation-organism/orchestrator/pole/nul_v9.py:118-129` (tête `6510199`) ; message du commit `5e352ec`.
- **Problème** : la liste recopie un message de commit. Dans le code publié, le bruit propre à un morceau est classé « hors du nul par choix » et non comme trou ; deux classes manquent.
- **Ancien** :
```
profondeur 2, marches douces, produits, bruit propre à un morceau, morceaux tempérés, compositions
```
- **Nouveau** :
```
profondeur 2 et seuils sur une combinaison de traits, marches douces, produits et déformations non monotones, morceaux tempérés, compositions (`NON_COUVERT_V9` au commit `6510199` ; le bruit aveugle propre à un morceau y est classé « hors du nul par choix », promouvable, et non comme trou)
```

#### VP-26 — Dernière mention de « N13 » avant R-2199 (tranche I-c)

- **Lignes** : 542. **Renvoi** : RA110.
- **Source** : `registres/decisions.md:1264` (R-1036, 2 novembre).
- **Problème** : faux à la lettre ; le fond tient (aucune trace d'exécution de l'audit de calibration des juges). Le registre des affirmations (RA110) porte la même erreur.
- **Ancien** :
```
dernière mention R-964 avant R-2199
```
- **Nouveau** :
```
dernière mention R-1036 avant R-2199, qui ne porte que l'état d'une course du collisionneur N12-N13
```

#### VP-27 — Calendrier : le code v63 est du 2 novembre (tranche I-c)

- **Lignes** : 588. **Renvoi** : RA64.
- **Source** : `/home/user/ideation-organism`, `git log` : `af92034`, `a12713a` (2 novembre) ; `registres/go.md:211`.
- **Ancien** :
```
tour fermé v60 à v62 ;
```
- **Nouveau** :
```
tour fermé v60 à v63 ;
```

#### VP-28 — Calendrier : seule la v64 est du 3 novembre (tranche I-c)

- **Lignes** : 589. **Renvoi** : RA64.
- **Source** : `git log` : `63ed933` (v64, 3 novembre) ; `af92034` (v63, 2 novembre).
- **Ancien** :
```
| 3 novembre | v63, v64 ;
```
- **Nouveau** :
```
| 3 novembre | v64 ;
```

#### VP-29 — Renvoi de ligne à la page publique (tranche I-c)

- **Lignes** : 565-566. **Renvoi** : RA127.
- **Source** : `/home/user/ideation-organism/README.md:7` (`b72c983e…`).
- **Problème** : les citations sont à la ligne 7 ; la ligne 8 est vide. Le registre des affirmations (RA127) porte la même erreur.
- **Ancien** :
```
l. 8) ; la recommandation d'y ajouter Qu, Chen et Wang
```
- **Nouveau** :
```
l. 7) ; la recommandation d'y ajouter Qu, Chen et Wang
```

#### VP-30 — Table R-2201 à R-2221 : trois lignes manquent, R-2208 mal classée (tranche I-c)

- **Lignes** : 678-684. **Renvoi** : RA142.
- **Source** : `registres/decisions.md:2161-2163` (R-2203, R-2204, R-2205) et `:2166` (R-2208).
- **Problème** : R-2203 à R-2205 manquent (toutes hors organisme). R-2208 touche l'organisme : son point (2) décide l'orchestration de vérification de ce programme.
- **Ancien** :
```
| R-2207, R-2208, R-2209, R-2210, R-2211, R-2212, R-2214, R-2218 | validité de l'adaptateur, base (A) de T0.8, audit des fuites de T0.7, orchestrations ciblées, registre des prédictions | non |
```
- **Nouveau** :
```
| R-2203, R-2204, R-2205, R-2207, R-2208, R-2209, R-2210, R-2211, R-2212, R-2214, R-2218 | audit des fuites de T0.7, chiffre corrigé, validité de l'adaptateur, base (A) de T0.8, orchestrations ciblées, registre des prédictions | non, sauf R-2208 (2) : orchestration de vérification de ce programme |
```

#### VP-31 — Invariant de N-053 : exception omise (tranche I-c)

- **Lignes** : 538. **Renvoi** : RA108.
- **Source** : `docs/decisions/decision-N-053-v1.md:42-43` (`2204256d…`).
- **Problème** : la décision écrit « hors bras d'attaque déclaré ».
- **Ancien** :
```
de l'agent », valable aussi pour la piste
```
- **Nouveau** :
```
de l'agent, hors bras d'attaque déclaré », valable aussi pour la piste
```

#### VP-32 — Collisionneur v9 : lieu de la sortie incomplet (tranche I-d)

- **Lignes** : 783. **Renvoi** : RA124 (annexe A).
- **Source** : `registres/decisions.md:1330` (R-1102), `:1338` (R-1110), `:1340` (R-1112) ; `registres/depenses.md:324, 329-331` ; `sorties-non-lues-v2.md` § 1. Aucune branche de données ouverte.
- **Problème** : la dépense citée comprend la suite, mais le lieu donné ne porte que la première partie.
- **Ancien** :
```
| branche `donnees/collisionneur-v9-brainstorm-v1`, commit `ac25c055`, liste `08aebf56…` |
```
- **Nouveau** :
```
| branche `donnees/collisionneur-v9-brainstorm-v1`, commit `ac25c055`, liste `08aebf56…` (13 cellules sur 15) ; suite sur `donnees/collisionneur-v9-brainstorm-v1-suite`, commit `42aa6b1b…` (R-1110) |
```

#### VP-33 à VP-36 — Table du § 9 : « non codé » sans le renvoi RA14 (tranche I-d)

- **Source commune** : registre des affirmations v2, l. 76 (RA14), 167 (RA105), 168 (RA106) ; `docs/decisions/decision-N-045-v2.md:101` ; `docs/decisions/decision-N-049-v1.md:46` ; recherche rejouée à la tête `6510199` du dépôt public, chemins cloisonnés exclus.
- **Problème commun** : RA105 et RA106 portent la décision ; « non codé » repose sur la recherche de RA14, non citée, alors que la rangée voisine « questions ouvertes » cite bien [RA12, RA14].

**VP-33** (ligne 704) — ancien :
```
| composition apprise (modèle par rôle) | décidé ; non codé | [RA105] |
```
nouveau :
```
| composition apprise (modèle par rôle) | décidé ; non codé | [RA105, RA14] |
```

**VP-34** (ligne 705) — ancien :
```
| coût dans le signal, score net | décidé ; non codé | [RA105] |
```
nouveau :
```
| coût dans le signal, score net | décidé ; non codé | [RA105, RA14] |
```

**VP-35** (ligne 708) — ancien :
```
| héritage récompensé sur K ≥ 3 générations | décidé ; non codé | [RA105] |
```
nouveau :
```
| héritage récompensé sur K ≥ 3 générations | décidé ; non codé | [RA105, RA14] |
```

**VP-36** (ligne 711) — ancien :
```
| tâches fraîches : part `test` tirée par génération | décidé ; non codé dans l'orchestrateur | [RA106] |
```
nouveau :
```
| tâches fraîches : part `test` tirée par génération | décidé ; non codé dans l'orchestrateur | [RA106, RA14] |
```

#### VP-37 — BOU-005 : « aucune course réelle autorisée » (tranche II-b)

- **Lignes** : 1189. **Renvoi** : BOU-005.
- **Source** : `registres/go.md:273` (GO-2026-11-08-02) et `:300` (GO-2026-11-10-10) ; `registres/decisions.md:2153` (R-2195), `:2164` (R-2206).
- **Problème** : formule trompeuse : un GO de calcul existe depuis le 8 novembre ; ce qui manque, ce sont ses conditions. La partie I dit « GO ouverts » (l. 757).
- **Ancien** :
```
prévu ; aucune course réelle autorisée au 10 novembre
```
- **Nouveau** :
```
prévu ; GO accordé sous conditions (GO-2026-11-08-02, repris par GO-2026-11-10-10) ; conditions non remplies et aucune course réelle lancée au 10 novembre
```

#### VP-38 — BOU-026 : conditions de la course réelle (tranche II-b)

- **Lignes** : 1210. **Renvoi** : BOU-026.
- **Source** : `registres/decisions.md:2173` (R-2215), `:2153` (R-2195), `:2164` (R-2206) ; `registres/go.md:273, 300`.
- **Problème** : périmé et incomplet : la v65 est contre-lue, la v66 en développement ; la machine à bac à sable, condition du GO, n'est pas citée.
- **Ancien** :
```
course réelle attend v65 contre-lu et préenregistrement (GO-2026-11-08-02, 45 USD)
```
- **Nouveau** :
```
course réelle attend le code corrigé (v65 contre-lue le 10 novembre, R-2215 ; v66 en cours), la machine à bac à sable et le préenregistrement scellé (GO-2026-11-08-02, repris par GO-2026-11-10-10, 45 USD)
```

#### VP-39 — MAT-005 : devis de l'essai Lean (tranche II-b)

- **Lignes** : 1327. **Renvoi** : MAT-005.
- **Source** : `registres/decisions.md:2184` (R-2226).
- **Ancien** :
```
devis prévu (R-2199 (b))
```
- **Nouveau** :
```
dessin et devis en rédaction (R-2199 (b), lancé en R-2226)
```

#### VP-40 — MAT-008 : pilier « génération » dit « en conception » (tranche II-b)

- **Lignes** : 1330. **Renvoi** : MAT-008.
- **Source** : `registres/decisions.md:2157` (R-2199) et `:2184` (R-2226) ; `registres/passations/2026-11-10-1159.md:78`.
- **Problème** : plus fort que la pièce : R-2199 place la note de conception après (a) et (b) ; aucune ligne ne consigne son début.
- **Ancien** :
```
pilier « génération » en conception (R-2199 (c))
```
- **Nouveau** :
```
note de conception du pilier « génération » prévue après (a) et (b) (R-2199 (c)) ; aucun début consigné au registre (R-2226)
```

#### VP-41 — OUT-008 : renvoi de ligne décalé (tranche II-b)

- **Lignes** : 1387. **Renvoi** : OUT-008.
- **Source** : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md:4, 6` (`e6e2f170…`) ; `registres/decisions.md:2069` (R-2111).
- **Problème** : le lecteur neuf est nommé à la ligne 6, pas à la ligne 4. Le fond est conforme.
- **Ancien** :
```
DEC R-2111 ; A4V:4
```
- **Nouveau** :
```
DEC R-2111 ; A4V:6
```

#### VP-42 — UNI-010 : texte de référence de la garde de disjonction (tranche II-b)

- **Lignes** : 1268. **Renvoi** : UNI-010.
- **Source** : `registres/decisions.md:600` (R-378) et `:621` (R-399).
- **Problème** : R-378 écrit « d'un texte de la banque » pour l'exclusion ; pour un texte de test, la règle nommée est autre (l'item est servi et compté).
- **Ancien** :
```
d'un texte de test est écarté
```
- **Nouveau** :
```
d'un texte de la banque est écarté
```

## Affirmations non vérifiables

Les vérificateurs n'ont pas pu établir ce qui suit, sous les règles de la consigne. Rien ici n'est un constat : ce sont des limites de la vérification.

### Cause commune : pièces hors de la tête de main, ou sous la cloison

- **Pièces sur d'autres branches, non ouvertes, empreintes non recalculées** : PCO1, PCO6, PCO7 (branche `origin/canal/conv-audit-n04` ; PCO7 porte en plus des sections du bras), V65R (branche `origin/prep/organisme-v65-v1`), SDN (branche `origin/claude/upbeat-cray-dmauvv`, note `ddb77ed6…`), C4R (branche `prep/etat-de-l-art-niveau3-v1`), C7R, N3S.
- **Pièce COF** (chemin contenant « coffre ») : non ouverte et non hachée.
- **Fichiers du dépôt public sous la cloison** (`bras_attaque_v54.py`, `reserve_tenue_a_l_ecart_v60.py` et `_v61.py`, `coffre_v53.py`, `coffre_v55.py`) : vus par leur nom seul, ou pas du tout ; les recherches d'absence dans `orchestrator/pole` (RA14) valent à la réserve de ces fichiers.

### Partie I

- **Tranche I-a** (environ 38 affirmations sur environ 179) : l. 118 (« voie hybride ancrée sur notre noyau » le 26 octobre, « versions 0 à 65 ») ; § 2.1 (contenu exact des numérotations (i) et (ii), lignes citées, « repris en v6 et v7 ») ; § 2.2 (coûts estimés, dimensionnements, lecture du 27 octobre, portes de sortie citées de chaque couche, « go » du 27 octobre pour la couche 4) ; l. 183-191 ; § 2.4 (définition de la réécriture) ; § 2.5 (définition, « Go » du 27 octobre, voie (b)) ; § 2.6 (liste et acceptation des neuf voies le 28 octobre). La contradiction des numérotations elle-même est corroborée sur main (R-2221 ; inventaire v7 l. 144).
- Empreinte `bff138d8…` de la configuration v5 et chemin du fichier : vérifiés seulement par le relais R-2220 (préfixe).
- R-597 (suspension du bras) : contenu non ouvert, seule la date relevée ; R-2045 et R-2047 non ouverts.
- Affirmations d'absence (l. 105, 191) : non contredites, mais le registre n'a pas été relu en entier pour les établir.
- L. 123-124 (continuité du code entre le noyau de l'étape 1 et l'orchestrateur du pôle) : le texte dit lui-même ne pas l'avoir vérifiée.
- L. 4 : l'identifiant de la session mère du texte est conforme à la ligne GO-2026-11-10-10 ; le fichier des interdits communs v2 en nomme une autre (écrite le 9 novembre) : reprise entre deux sessions mères, non tranché.
- **Tranche I-b** : l. 317 (« vivier de 60 », « graine du noyau secrète », « répétition générale », « prêt pour (a) ») ; l. 359-362 (« nul fixe », contraste calculé après le gel, héritage entre parties disjointes) ; l. 460-466 (« gardes de dépense avant chaque appel », seul point sans recoupement) ; l. 480-481 (empreinte longue et note de la session-dépôt, par relais seulement) ; l. 446 (réutilisation du cœur v64, déduite) ; l. 277 (M4 non calculée : état au 1er novembre, non revérifié depuis) ; l. 280 (« brouillon 4 privé », sur R-1469 seul) ; l. 282 et 387-388 (déclarées non vérifiées par le texte lui-même).
- Geste déclaré par le vérificateur de I-b : une recherche dans `registres/decisions.md` a affiché le début de la ligne R-2147, qui relate un message de la session du bras d'attaque (en-tête seulement). Rien n'en est repris ; aucun document du bras n'a été ouvert.
- **Tranche I-c** : ligne du 27 octobre du calendrier, « voie hybride » au 26 octobre, « neuf voies » au 28 octobre, moitié « programme de conception v1 » de la contradiction des numérotations ; empreinte complète de la configuration v5 (§ 8.4, point 10) ; contenu de la note SDN ; pièces « citées par » RES3 (verdicts A1-v3 et A1-v4, lecture de dose) non relues à la source ; absences (« sans source contraire », « aucune trace ») vérifiées seulement dans les registres ; « juge-tournoi : non codé » (l. 553), sans source citée ; factures réelles des fournisseurs (le registre des dépenses dit lui-même A1-v4 « non rapproché d'une facture »).
- **Tranche I-d** : l. 722 (le mot « franchie » pour la couche 0) ; l. 730 (neuf voies « décidé ») ; l. 745 (règle e-BH « défaut décidé » : employée par le code, décision non relue) ; l. 771 (existence des fichiers v60 et v61 de la réserve) ; l. 803 (absence du verdict d'A1 `795e5e99…` sur main : recherche non aboutie dans le délai) ; l. 794-795 (note SDN, par relais ; absence de `995eb918` hors des registres non rejouée sur tout main).

### Partie II

- **Tranche II-a** — entrées à source seulement PCO : ARC-044, ARC-046, ROL-040, JUG-051, et la part PCO de ARC-045, ROL-039, ATQ-065. À source seulement C4R : ARC-042, ROL-032, ROL-033, JUG-045 à JUG-048, ATQ-063. À source C7R ou N3S (concordantes avec des relais sur main, pas avec la pièce primaire) : JUG-010, JUG-012, JUG-013, JUG-014, ATQ-015 ; JUG-009 compté vérifié sur ces seuls relais.
- Mentions « codé » avec noms de modules ou de commits (ARC-020, ARC-040, ROL-029, ROL-030, JUG-014, JUG-043, JUG-044, entre autres) : vérifiées sur la pièce citée, pas sur le code.
- ROL-021 à ROL-023 et ATQ-061 : vérifiées sur SN2 seulement. JUG-026 : R-543 lu en partie.
- Limite des états : chaque statut a été comparé au registre des décisions par recherche ciblée jusqu'à R-2226, pas par relecture intégrale des 2 184 lignes. Un état périmé hors de ces recherches peut subsister.
- Trois statuts citent R-611 comme en vigueur sans être faux à la lettre (ATQ-018, ATQ-026, ATQ-047) : non comptés ; à relire avec VP-01.
- **Tranche II-b** — non vérifiées sur pièce primaire : BOU-035, VER-036 à VER-039, OUT-045, PAC-019 (C4R) ; COM-027, PAC-021 (PCO) ; BOU-037, MAT-008, OUT-049 pour leur part PCO ; VER-006, BOU-003, BOU-004, VER-009 (relais seulement) ; UNI-013 pour sa part COF ; décision D2 et « question v2 écrite » de UNI-012.
- OUT-048 : les lignes citées (R-753, R-759) ne disent pas ce que l'entrée leur fait dire ; pièce source non retrouvée, pas de couple.
- OUT-047 : verdicts des v44 et v48 à v51 absents des pièces citées (la v44 est en R-746 et R-749 ; les contre-lectures CL13 à CL16 n'ont pas été ouvertes).
- OUT-029 (« échéance du 2 novembre » : date non vérifiée) ; PAC-013 (rattachement de H-M1 à N-053 absent des lignes citées ; « v2 arrêtée » est en R-454, non citée) ; REC-001 (« pour mesurer le sur-signalement » : glose de l'inventaire) ; VER-041 (devis v2 et v3 non lus).
- États laissés tels quels faute de ligne contraire jusqu'à R-2226 : PAC-005, PAC-020, OUT-034, OUT-009, OUT-005, UNI-002, PAC-006.

### Constats conformes à noter

- Empreintes : toutes les pièces de main et du dépôt public (tête `6510199`) citées et accessibles ont l'empreinte dite.
- Décompte de la partie II (l. 1430-1456) : recompté par programme, conforme (12 familles, 7 types, total 411).
- Reprise de l'inventaire v7 (`056adb7f…`) : identique à l'octet hors colonne ajoutée et préfixe, dans les deux tranches de la partie II.
- `registres/decisions.md` est vivant : son empreinte a changé plusieurs fois pendant la vérification (dernière ligne R-2223 à 12:50 UTC, puis R-2226 à 13:03 UTC ; `cbd3f950…` à 13:15 UTC). Les tranches I-a, I-b et I-c ont lu jusqu'à R-2223 ; les tranches I-d, II-a et II-b jusqu'à R-2226. Les constats VP-10, VP-11, VP-15, VP-39 et VP-40 viennent de R-2226, postérieure au texte.

## Tranches sans résultat

Aucune : les six tranches ont rendu un résultat de vérificateur et de sceptique.
