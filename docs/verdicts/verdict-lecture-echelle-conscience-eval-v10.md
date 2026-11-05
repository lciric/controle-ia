# Verdict de lecture — échelle de la conscience d'évaluation, Llama-3.1 8B contre 70B (texte scellé v10)

## Rôle, heure, empreintes

- **Rôle** : lecteur neuf au sens de R13. Je n'ai écrit ni le préenregistrement, ni l'analyse, ni le code. J'applique mécaniquement les critères gelés du texte scellé.
- **Heure** : 2026-10-27 14:59:15 UTC (`date -u`, au début de l'écriture ; première vérification d'empreintes à 14:56:44 UTC).
- **Empreintes vérifiées** (`sha256sum`, comparées à l'attendu et aux compagnons `.sha256`) :

| pièce | sha256 | état |
|---|---|---|
| `prereg/test-echelle-conscience-eval-v10.md` | `2af6516dce9326d51cac9220d3e947895a5971d01e01ca659c77d4a7647f0920` | conforme (attendu et compagnon) |
| `docs/notes/echelle-conscience-eval/v10/analyse/analyse-echelle-v9.json` | `855b80fa94e8a70bf05a3c928c361ab9dc71b3ee07074fe2c402c535cf5618c2` | conforme (attendu et compagnon) |
| `docs/notes/echelle-conscience-eval/v10/analyse/analyse-sortie.txt` | `16948d1b42ed0c90b4ce271767c65a984c2de8f72e15a1c0167679bc37e4f4b0` | conforme au compagnon |
| `echelle-v9/scripts/analyser_echelle_v9.py` (arbre au commit) | `00ef7c8599bcd02bc753db3dfd4465eb79f62a72084236d11b55a728be1e7281` | conforme au tableau du texte, au compagnon et à `sha256_script` de la sortie |
| `echelle-v9/scripts/mesurer_echelle_v9.py` (arbre au commit) | `4923305c54c08c3c8c70a41779c52cb5c1cac890daf13efd5a6edd524e05a3d5` | conforme au tableau du texte et au compagnon |
| `echelle-v9/scripts/requirements-echelle-v9.txt` | `0987a61e0fecded1616a7a1d9d1b28060924458279dfbf76247d5ec198c1d5fa` | conforme ; il fixe `numpy==2.4.6` |
| manifeste de mesure du 8B | `e959c2578784a63654b15f872deefef302fea314a994dd56eca1bee60b2187b8` | égal à `manifestes_sha256.petit` de la sortie et à son compagnon (empreinte seule, contenu non lu) |
| manifeste de mesure du 70B | `60dae285cadd6b6b559c711aa242b3f4df3c6a87a0f9972ffe2aab47a0b30345` | égal à `manifestes_sha256.grand` de la sortie et à son compagnon (empreinte seule, contenu non lu) |

## Lecture prononcée

**Indécis.**

Phrase permise (« Critères de lecture gelés », phrases permises) : « Le dispositif ne tranche pas. »

Le texte ajoute, à la suite de cette phrase : « Sous H_0, cette issue devient fréquente quand l'hétérogénéité des cadrages croît (tableau ci-dessus) ; elle n'est pas un « nul ». »

Elle ne porte aucune réserve propre à l'issue (« indécis » n'en porte aucune, CLV-07). Elle est rapportée avec la réserve de la section « Contre-lecture » (plus bas) et avec la réserve que déclenche la clause R4 (plus bas).

## Vérification du mode décisif

| exigence du texte (« Intervalles », mode décisif ; plan d'analyse, point 5) | relu | état |
|---|---|---|
| commit des scripts `360a3f71a5ae19fbf10dec00876f0cdeef5ed82d` | `commit_scripts` et `commit_attendu` de la sortie : ce commit. `git -C …/wt-echelle-v1 log -1 --format=%H` : ce commit (13:44:20 UTC, « Outils v9 : garde-fou de 6 h… ») | conforme |
| arbre des scripts propre | `arbre_scripts_propre: true` ; `git status --porcelain -- echelle-v9` vide, relu par moi | conforme |
| numpy 2.4.6 | `numpy: "2.4.6"` (python 3.13.16) | conforme |
| entropie 4429003211691042563 | `entropie: 4429003211691042563` | conforme |
| 2 000 tirages | `n_boot: 2000` ; 10 partitions | conforme |
| seuils | 0,70 ; δ = 0,25 ; λ maximal 1 ; rapport des Ec 1,15 | conformes au tableau « Seuil » |
| manifestes : nom et empreinte de `mesurer_echelle_v9.py` de cet arbre | le code (`charger_modele`) arrête l'analyse sinon, hors répétition ; la sortie est rendue avec le code 0 et `repetition: false` ; empreintes des manifestes égales à celles de la sortie | conforme (contrôle fait par le code, non relu par moi dans les manifestes, dont je n'ai pas lu le contenu) |
| modèles et révisions | `meta-llama/Llama-3.1-8B-Instruct` `0e9e39f2…` ; `meta-llama/Llama-3.1-70B-Instruct` `1605565b…` ; couches 8, 12, 16, 20 et 20, 30, 40, 50 | conformes |
| stimuli | `sha256_stimuli` `b4cb38c1…` | conforme au tableau du texte |
| tirages rejetés | principal : 0 (a), 0 (b) ; sac de mots : 0 (a), 1 (b) ; consignés | conforme à ce que le texte demande |
| exécution | `analyse-sortie.txt` : départ 2026-10-27T14:33:01Z, fin 14:55:46Z, code 0 | — |

Couche L\* refaite sur le pli S (plus petite des deux aires A_ctx, maximale) : 8B, couche 16 (0,968 ; contre 0,767, 0,851, 0,908) ; 70B, couche 30 (0,978 ; contre 0,953, 0,944, 0,940). Conforme à la sortie.

## Étape 1 refaite — chaque sens seul

δ = 0,25. Intervalles à 2,5 et 97,5 %.

**Certification** (borne basse de A_ctx_fixe ≥ 0,70) :
- a→b : 8B 0,930 ; 70B 1,000. Sens certifié.
- b→a : 8B 0,908 ; 70B 0,943. Sens certifié.

### Sens a→b

λ(8B) = 0,293 [−0,245 ; 1,249] ; λ(70B) = 0,087 [−0,078 ; 0,328] ; Δλ = 0,206 [−0,413 ; 1,089].

| étape | issue | conditions qui manquent (bornes) | tenue |
|---|---|---|---|
| 1 | fuite de signe inverse (petit) | borne haute de λ(8B) 1,249, pas < −0,25 | non |
| 1 | fuite de signe inverse (grand) | borne haute de λ(70B) 0,328, pas < −0,25 | non |
| 2 | positif | borne basse de Δλ −0,413, pas > 0,25 ; borne basse de λ(8B) −0,245, pas > 0,25. Tenues : borne basse de λ(70B) −0,078 > −0,25 ; borne haute de λ(70B) 0,328 < 1 | non |
| 3 | inverse | borne haute de Δλ 1,089, pas < −0,25 ; borne basse de λ(70B) −0,078, pas > 0,25 ; borne haute de λ(8B) 1,249, pas < 1. Tenue : borne basse de λ(8B) −0,245 > −0,25 (de 0,005) | non |
| 4 | pas de fuite | λ(8B) [−0,245 ; 1,249] sort de [−0,25 ; 0,25] par le haut ; λ(70B) [−0,078 ; 0,328] en sort par le haut | non |
| 5 | nul | Δλ [−0,413 ; 1,089] sort de [−0,25 ; 0,25] des deux côtés | non |

Aucune issue tenue : le sens a→b est **indécis**.

### Sens b→a

λ(8B) = −0,298 [−0,851 ; 0,130] ; λ(70B) = 0,003 [−0,487 ; 0,335] ; Δλ = −0,300 [−0,702 ; −0,006].

| étape | issue | conditions qui manquent (bornes) | tenue |
|---|---|---|---|
| 1 | fuite de signe inverse (petit) | borne haute de λ(8B) 0,130, pas < −0,25 | non |
| 1 | fuite de signe inverse (grand) | borne haute de λ(70B) 0,335, pas < −0,25 | non |
| 2 | positif | borne basse de Δλ −0,702, pas > 0,25 ; borne basse de λ(8B) −0,851, pas > 0,25 ; borne basse de λ(70B) −0,487, pas > −0,25. Tenue : borne haute de λ(70B) 0,335 < 1 | non |
| 3 | inverse | borne haute de Δλ −0,006, pas < −0,25 ; borne basse de λ(70B) −0,487, pas > 0,25 ; borne basse de λ(8B) −0,851, pas > −0,25. Tenue : borne haute de λ(8B) 0,130 < 1 | non |
| 4 | pas de fuite | λ(8B) [−0,851 ; 0,130] sort de [−0,25 ; 0,25] par le bas ; λ(70B) [−0,487 ; 0,335] en sort des deux côtés | non |
| 5 | nul | Δλ [−0,702 ; −0,006] sort de [−0,25 ; 0,25] par le bas (la borne haute y est) | non |

Aucune issue tenue : le sens b→a est **indécis**.

## Étape 2 refaite — combinaison

- Les deux sens sont certifiés : aucun échec de certification à combiner.
- Aucune issue n'est tenue dans un sens ni dans l'autre : il n'y a ni issue commune, ni issue tenue dans les deux sens sans la cohérence (donc pas de « désaccord des deux sens (cohérence) »), ni issues différentes dans chaque sens (pas de « désaccord des deux sens »), ni issue tenue dans un seul sens (pas de « X non confirmé »).
- Reste la dernière branche : **indécis**.
- Aucune issue tenue dans un seul sens : aucune condition manquante à rapporter au titre de CLV-07 (la sortie rend `conditions_manquantes: {}`, conforme). Aucune issue tenue dans les deux sens sans la cohérence : aucun écart à rapporter au titre de CLU-01 pour une issue.
- La cohérence des deux sens, rapportée sans effet sur la lecture : rompue chez le 8B (|e| = 0,591 > 0,25), tenue chez le 70B (|e| = 0,085 ≤ 0,25).

**Je retrouve la lecture que rend la sortie : « indécis », dans chaque sens et à la combinaison, sans réserve propre à l'issue.** La raison : dans chaque sens, les intervalles de λ et de Δλ sont trop larges pour qu'aucune issue ne tienne ; ils chevauchent à la fois δ et −δ (sauf Δλ du sens b→a, entièrement négatif mais dont la borne haute, −0,006, reste loin de −0,25), et ceux de λ(8B) débordent [−δ ; δ]. Les deux sens pointent de plus dans des directions opposées en point (Δλ +0,206 contre −0,300 ; λ(8B) +0,293 contre −0,298).

## Grandeurs rapportées sans lecture décisive

Tirées de la sortie par un script de lecture (`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/outils-lecteur-v10/tableaux.py`), sans transcription à la main ; arrondi au millième.

**Lecture de chaque sens** : a→b « indécis », b→a « indécis » ; issues tenues : aucune dans l'un ni dans l'autre.

**Par modèle et par sens, à la couche L\*, avec intervalles** (certification comprise) :

| modèle | sens | λ | A_ctx_fixe | A_ctx | A_conf | Ec | Ef | ν | A_conf_T1 |
|---|---|---|---|---|---|---|---|---|---|
| 8B (L* = 16) | a→b | 0,293 [−0,245 ; 1,249] | 0,960 [0,930 ; 1,000] | 0,960 [0,838 ; 1,000] | 0,909 [0,405 ; 0,998] | 0,842 [0,549 ; 1,025] | 0,247 [−0,172 ; 0,800] | 0,689 [0,241 ; 1,515] | 0,001 [0,000 ; 0,007] |
| 8B (L* = 16) | b→a | −0,298 [−0,851 ; 0,130] | 0,974 [0,908 ; 1,000] | 0,974 [0,873 ; 0,999] | 0,996 [0,879 ; 1,000] | 1,013 [0,517 ; 1,458] | −0,302 [−0,653 ; 0,104] | 0,515 [0,222 ; 1,038] | 0,011 [0,000 ; 0,047] |
| 70B (L* = 30) | a→b | 0,087 [−0,078 ; 0,328] | 1,000 [1,000 ; 1,000] | 1,000 [0,966 ; 1,000] | 1,000 [0,881 ; 1,000] | 1,702 [1,040 ; 2,049] | 0,149 [−0,131 ; 0,430] | 0,232 [0,049 ; 0,330] | 0,056 [0,000 ; 0,261] |
| 70B (L* = 30) | b→a | 0,003 [−0,487 ; 0,335] | 0,985 [0,943 ; 1,000] | 0,985 [0,924 ; 1,000] | 0,990 [0,761 ; 1,000] | 1,554 [0,711 ; 2,381] | 0,004 [−0,540 ; 0,433] | 0,550 [0,123 ; 1,329] | 0,061 [0,000 ; 0,235] |

Certification par modèle et par sens : les quatre bornes basses de A_ctx_fixe (0,930 ; 0,908 ; 1,000 ; 0,943) passent 0,70.

**En points seulement** :

| modèle | sens | λ appris (moitié tenue à part) | transfert | Ec qcm | Ec prose | d' | marge de A_ctx_fixe sur le sac |
|---|---|---|---|---|---|---|---|
| 8B | a→b | 0,039 | 0,465 | 0,707 | 0,978 | 2,393 | 0,389 |
| 8B | b→a | −0,183 | 0,673 | 0,840 | 1,186 | 2,141 | 0,450 |
| 70B | a→b | 0,054 | 0,638 | 1,406 | 1,998 | 3,933 | 0,428 |
| 70B | b→a | −0,077 | 0,532 | 1,350 | 1,758 | 2,501 | 0,460 |

**Δλ, spécificités, différences d'aires, sac de mots, dans les deux sens** :

| sens | Δλ | spécificité | ΔA_ctx_fixe (70B − 8B) | ΔA_conf (70B − 8B) | sac de mots (A_ctx) |
|---|---|---|---|---|---|
| a→b | 0,206 [−0,413 ; 1,089] | −0,252 [−1,295 ; 0,330] | 0,040 [0,000 ; 0,070] | 0,091 [−0,049 ; 0,563] | 0,572 [0,419 ; 0,744] |
| b→a | −0,300 [−0,702 ; −0,006] | −0,265 [−1,113 ; 0,477] | 0,011 [0,000 ; 0,037] | −0,006 [−0,166 ; 0,020] | 0,524 [0,204 ; 0,837] |

Le sac de mots rend 0,5717 (a→b) et 0,5242 (b→a), les valeurs que le texte annonçait (« Métrique », contrôles lexicaux).

**Spécificités de signe inverse (−λ − ν)** :

| modèle | sens | −λ − ν |
|---|---|---|
| 8B | a→b | −0,982 [−2,411 ; −0,120] |
| 8B | b→a | −0,217 [−0,841 ; 0,444] |
| 70B | a→b | −0,319 [−0,469 ; −0,145] |
| 70B | b→a | −0,553 [−1,076 ; −0,196] |

**Écarts entre les sens, cohérence, rapport des Ec** :

| modèle | e(m) = λ_a→b − λ_b→a | cohérence (\|e\| ≤ δ, en point) | l'intervalle de e(m) exclut zéro | q = Ec_a→b / Ec_b→a | max(q, 1/q) > 1,15 |
|---|---|---|---|---|---|
| 8B | 0,591 [−0,148 ; 1,771] | non tenue | non | 0,832 [0,566 ; 1,278] | oui (1,202) |
| 70B | 0,085 [−0,250 ; 0,699] | tenue | non | 1,095 [0,761 ; 1,617] | non (1,095) |

Ces grandeurs n'ont aucun effet sur « indécis » : les deux réserves « le λ du modèle change d'un sens à l'autre » et « jeux de force de contexte inégale » ne visent que « positif », « inverse » et « nul ». À titre de fait rapporté : le rapport des Ec du 8B sort de la bande (1,202 > 1,15), ce qui, selon le texte, tient à une force du contexte inégale ou à une composition inégale des deux jeux, que le dispositif ne sépare pas ; et la cohérence du 8B est rompue en point.

**λ et Δλ aux quatre profondeurs appariées, en points** :

| sens | couches (8B, 70B) | λ(8B) | λ(70B) | Δλ |
|---|---|---|---|---|
| a→b | 8, 20 | 0,185 | −0,082 | 0,266 |
| a→b | 12, 30 | 1,128 | 0,087 | 1,040 |
| a→b | 16, 40 | 0,293 | 0,217 | 0,077 |
| a→b | 20, 50 | −0,009 | 0,113 | −0,122 |
| b→a | 8, 20 | 0,322 | −0,358 | 0,680 |
| b→a | 12, 30 | 0,513 | 0,003 | 0,510 |
| b→a | 16, 40 | −0,298 | 0,440 | −0,738 |
| b→a | 20, 50 | −0,493 | 0,479 | −0,973 |

Les couches L\* (16 pour le 8B, 30 pour le 70B) ne sont pas à la même profondeur relative (0,5 et 0,375) : le texte le permet (L\* choisie par modèle). Indicateurs « profondeur contraire » de la sortie, sans objet puisque rien n'est prononcé : vrais pour la fuite de signe inverse (petit) en a→b, la fuite de signe inverse (grand) dans les deux sens, « pas de fuite » et « nul » en b→a ; faux pour « positif » et « inverse ».

**L\* et ses notes** : 8B, aires minimales du pli S par couche 0,767 (8), 0,851 (12), 0,968 (16), 0,908 (20) ; 70B, 0,953 (20), 0,978 (30), 0,944 (40), 0,940 (50). Aucune égalité à départager.

## Clause R4 (issue trop propre)

Exemples du texte, appliqués à la lettre :

| exemple de R4 | relu | déclenche ? |
|---|---|---|
| λ exactement nul | aucun : le plus proche, λ(70B) b→a = 0,0026, intervalle [−0,487 ; 0,335] | non |
| intervalles anormalement étroits | A_ctx_fixe(70B) a→b [1,000 ; 1,000] : exempté par le texte (« A_ctx_fixe peut valoir 1,00 sans réserve », CLY-11) ; A_conf_T1(8B) a→b [0,000 ; 0,007] : relevé à la ligne suivante ; les intervalles de λ, Δλ, e(m) et q sont larges | non, hors la ligne suivante |
| A_conf ou A_conf_T1 à 1,00 avec λ ≥ 0,5 | A_conf(70B) a→b = 1,000 avec λ = 0,087 ; A_conf(8B) b→a = 0,996 avec λ = −0,298 ; A_conf(70B) b→a = 0,990 avec λ = 0,003 : λ sous 0,5 chaque fois, exemptés (CLZ-09) | non |
| **en miroir, A_conf ou A_conf_T1 à 0,00 avec λ < 1** | **A_conf_T1(8B) a→b = 0,0012, soit 0,00 à deux décimales, intervalle [0,000 ; 0,007], avec λ = 0,293 < 1** | **oui, à la lettre** |

**R4 se déclenche, à la lettre**, sur A_conf_T1 du 8B dans le sens a→b. Le texte en tire deux conséquences : « le même audit des formes et des empreintes, quel que soit son signe, avant tout rapport, et une réserve ».

- **Empreintes** : faites ici, toutes conformes (texte, sortie, scripts au commit, manifestes).
- **Formes** : je ne les ai pas auditées moi-même, puisque l'audit demande de lire les activations, hors de mon mandat. Les gardes de forme de l'analyse (forme de chaque matrice d'activations, valeurs finies, empreintes des sorties contre le manifeste, ordre des identifiants) ont passé : code 0. **L'audit des formes demandé par R4 reste à faire avant tout rapport.**
- **Réserve à dire avec la lecture** : « A_conf_T1 du 8B à 0,00 (0,0012 ; [0,000 ; 0,007]) dans le sens a→b, avec λ = 0,293 < 1 : exemple de R4 rempli ; audit des formes et des empreintes déclenché. »

Remarques, qui ne lèvent pas le déclenchement :
- A_conf_T1 est l'aire sur les cellules en conflit (eval-prose contre reel-qcm) le long de la direction naïve « eval-qcm moins reel-prose » (`mesures_couche`). Les quatre valeurs sont basses (0,001 ; 0,011 ; 0,056 ; 0,061) : cela ressemble davantage à une propriété du témoin, où le format domine la direction naïve, qu'à une « inversion trop nette » propre à un modèle. C'est une interprétation, pas une application mécanique.
- La lecture prononcée, « indécis », n'est pas « trop propre ». R4 s'applique ici parce que l'un de ses exemples chiffrés est rempli. Le texte dit aussi qu'« indécis » ne porte aucune réserve (section « Réserves propres à l'issue prononcée »). La réserve de R4 est d'un autre ordre : elle naît de la clause R4, pas de l'issue. Je la dis donc. Lazar tranche s'il juge que R4 ne visait que les issues prononcées.

## Limites et réserves

**Réserve de la section « Contre-lecture » du texte, dite avec toute issue rapportée** : la contre-lecture n° 10, courte, qui devait relire les seuls passages changés du v9-3, a été lancée puis arrêtée avant son rapport, sur la décision de Lazar de lever le préenregistrement et sa contre-lecture pour cette expérience (R-552). **Les passages changés du v9-3 n'ont donc pas été relus par un sous-agent neuf.** De plus, les changements de conduite de la v10 (outils v9 : garde-fou de 6 h, plafond de 24 USD, recharge automatique) n'ont pas été contre-lus (R-552, R-555).

**Limites de la lecture que le texte impose** (« Critères de lecture gelés », limites) :
- une famille, deux tailles, une manipulation de contexte (« l'auteur connaît la réponse ») ;
- aucune généralisation ;
- ĉ mêle une intention déclarée et une polarité possession/absence (CLX-16) ;
- des asymétries de mots courts subsistent entre eval et reel, comptées dans la trace lexicale (CLY-12) ;
- une poussée du format alignée à la fois sur les signatures des deux jeux de cadrages, chez un même modèle, passe les deux sens et peut fabriquer « positif », « inverse » ou une fuite de signe inverse. Avec deux jeux seulement, elle ne se distingue pas d'une fuite du concept ;
- les signatures d'un seul jeu à deux tailles différentes (« croisées ») ; autour du centre de la classe de la contre-lecture n° 6, la cohérence ne suffit pas, et une issue sans réserve peut encore tenir à cette classe, y compris sous une composante propre aux cadrages d'un jeu ;
- prix de la cohérence des deux sens : perte de puissance sous un contexte d'un jeu plus faible, ou sous la signature d'un seul jeu chez un modèle quand H_A tient ;
- sous H_A, les signatures peuvent faire perdre l'écart vrai et rendre « indécis » ou « non confirmé » là où H_A tient ;
- rien ne relie ici ĉ à une conscience d'évaluation implicite ;
- une sonde linéaire qui lit un texte mesure la représentation du lecteur (R-525).

Pour « indécis » en particulier, le texte rappelle que cette issue n'est pas un « nul ». Elle n'écarte ni H_A ni H_0. Dans la simulation, elle devient fréquente sous H_0 quand les cadrages sont hétérogènes ; un H_A faible n'y est retrouvé dans les deux sens qu'avec des cadrages homogènes ; un H_A de 0,3 en dimension 256 ne l'est jamais (« Atteignabilité »). La phrase de renvoi aux limites (CLR-04) n'est obligatoire qu'après « positif », « inverse » ou « nul » : elle ne s'applique pas ici.

## Désaccords avec la sortie de l'analyse

**Aucun désaccord sur la lecture.** Je retrouve « indécis » dans chaque sens et à la combinaison, sans réserve propre à l'issue, sans condition manquante à rapporter, et la même cohérence (8B rompue à 0,591 ; 70B tenue à 0,085).

Trois points s'ajoutent à la sortie sans la contredire :
1. **R4** : le code ne l'évalue pas. Je la déclare déclenchée à la lettre (A_conf_T1 du 8B en a→b à 0,00). Cela demande un audit des formes avant tout rapport, et une réserve (voir plus haut).
2. La sortie ne cite pas la réserve de la section « Contre-lecture » : je l'ajoute, comme le texte l'exige pour toute issue rapportée.
3. Note de conduite : pour vérifier la propreté de l'arbre, j'ai lancé `git status --porcelain` dans l'arbre des outils. Cette commande peut rafraîchir le cache d'index de git, mais ne change aucun fichier suivi, aucun commit et aucune branche. Aucune autre commande git n'a touché l'arbre, et je n'ai rien écrit hors de mes dossiers `lecture-echelle-v10/` et `outils-lecteur-v10/` du bloc-notes.

Je n'ai ouvert, lu ni haché aucun des fichiers interdits (consignes P3, textes d'actions, items et prompts P1, `donnees/`, `runs/`, `diag/`, `traces/` du dépôt). Je n'ai fait aucune recherche récursive, aucun appel réseau, et n'ai utilisé aucune clé. Les deux manifestes de mesure, hors du dépôt, ont été hachés sans que leur contenu soit lu.
