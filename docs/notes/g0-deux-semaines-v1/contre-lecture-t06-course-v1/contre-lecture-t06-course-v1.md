# Contre-lecture d'un seul tenant de la chaîne de la course de T0.6 — v1

Fille 9, contre-lectrice neutre (R2). Écrit le 2026-11-07, de 22:15 à 22:55 UTC (heures relevées par `date -u`). Non scellé ; aucun `.sha256`.

## Message de la mère (recopié mot pour mot)

> contre-lecture d'un seul tenant de la chaîne de la course de T0.6, comme pour la v9 : le code par un sous-agent neuf de lignée Opus ; toi, les textes, l'ordre et la concurrence. Aucune clé, aucune location, aucun `vastai`. Objet : branche `prep/t06-course-v1`, tête `839183010b160f0ea6c031249b6aa89f912bff3b`, partie de `e940d4b2` (fille 10, Claude Sonnet 5.5). Code et scripts : `scripts/lancer_t06_v10.sh` (`b98e84cf…`) ; `scripts/amorce_instance_t06_v8.sh` (`29913ace…`, = v7 + étape bras B après la poussée finale) ; `src/controle_ia/t06/session_v9.py` (`d0443323…`) ; `scripts/fenetre_carte_t06_v1.sh` (`bc0a67c3…`). Bras B : module `src/controle_ia/audit_fuite_r1_v4/bras_b_v1.py` (`afacfedb…`), configuration `config-bras-b-t06-v1.json` (`4fb0da20…`), manifeste des copies (`935d93b1…`, 27 fichiers), rapport `rapport-bras-b-t06-v1.md` (`fc03ad62…`) ; texte qui fait foi : point 7 de `prereg/audit-fuite-r1-v4-v1.md` (`910a53dc…`), GO-2026-11-07-04. Essais : 180 sur 180. Textes : candidat 9-r2 (`0050ab33…`) ; brouillon d'ordre `ordre-fille-6-t06-course-v1-brouillon.md` (`f9da98f3…`) ; dans l'heure : configuration de la course brouillon 5 et candidat 10 — intègre-les avant de conclure. Ce qui doit être vrai : les 4 cas R5 et les réserves de la v9 ; `_INTROUVABLE` en « 404 » exact ; refus de plafond en code 2 avec son motif ; bras B fidèle au point 7 (W recalculée et prouvée par 114 nombres sans écart ; notation par le pli tenu à l'écart ; contrôle d'identité, au bit près sur la même carte et les mêmes versions, sinon tolérance de 2e-3) ; bras B jamais bloquant ; fenêtre conforme à GO-2026-11-07-02 ; règle « mots et coût » (GO-2026-11-07-03), seuils 0,70 et +0,05 ; l'ordre complet : plafond 200 USD, fenêtre, bras B, engagement, lecture des offres la veille. Les 7 réserves de la fille 10 à trancher : 1 bras B jamais tourné sur carte ; 2 tolérance du contrôle G4 ; 3 configuration de la course ; 4 cas R5 1 et 2 assouplis faute d'artefact reproductible ; 5 texte « introuvable » de Vast (après E3) ; 6 citations du candidat ; 7 faut-il un banc de mutations pour le bras B ? Rendu : branche `prep/contre-lecture-t06-course-v1`, verdict par pièce (prête, corriger avant la course, ou réserve) et couples pour l'ordre et le candidat. Pas de `.sha256`. Vise deux heures. La course part dès le scellement.

## Qui a lu quoi
- **Code** (lanceur v10, amorce v8, `session_v9`, fenêtre, module, configuration et copies du bras B, essais) : un sous-agent neuf de lignée Opus, qui n'avait lu aucune des pièces. Il a travaillé sur l'arbre au commit `83918301`, de 22:15 à 22:48 UTC. Il a joué des mutations dans des copies et n'a lu aucune valeur sous `donnees/`, `diag/` ou `runs/`.
- **Textes, ordre, configuration brouillon 5, candidat 10, concurrence** : moi. J'ai lu le point 7, le GO-2026-11-07-04 et les lignes R-1716 à R-1726 de `registres/decisions.md` sur `main`. J'ai rejoué le candidat 10 à l'octet avec son générateur. J'ai rejoué l'essai neuf `tests/test_t06_config_course_brouillon5.py` à `dfc032c6` : 6 passés.
- **Tête finale contre-lue : `dfc032c6ff00692182c372b4752bcc93f3ca111d`.** De `83918301` à `dfc032c6`, le diff n'ajoute que 5 fichiers : la configuration brouillon 5, son essai, le candidat 10, son générateur et son journal. Aucun code ne change, donc les comptes du sous-agent restent valables à `dfc032c6`.
- **Empreintes** : toutes celles citées par la mère sont vérifiées à `dfc032c6`, ainsi que celles du brouillon 5 (`b7a5c1ba…`) et du candidat 10 (`c4083ffc38815f99d21410c09689c83b1ccbf3751fdcabd11e000a77fd925907`).

## Verdict d'ensemble
**La chaîne de T0.6 elle-même est prête** : lanceur v10, amorce v8, `session_v9`, configuration brouillon 5 et candidat 10. **Avant la course, il faut deux choses.**
1. **Appliquer les 7 couples à l'ordre.** Ils portent sur les dossiers de la veille, l'instance arrêtée, l'instance sans surveillance, les 3 heures pleines de la fenêtre, les variables de la fenêtre, la borne de temps du bras B et l'interdit de lire `bras-b.out` ; le contrôle du `.sha256` de la configuration du bras B et l'arrêt sur redémarrage sont dans le même couple que ce dernier point.
2. **Choisir pour le bras B.** GO-2026-11-07-04 exige « code, essais et ordre contre-lus et scellés avant la course ». Or le banc ne tue qu'une mutation sur six du module, et le module écrit son issue en clair dans `traces/`. Le bras B n'est donc **pas prêt** tel quel. Deux voies :
   - **(a)** une v2 du module, avec les essais R5 1 à 5 ci-dessous, avant le scellement ;
   - **(b)** la course sans le bras B : il faut retirer la configuration du bras B du commit de la course, et l'amorce journalise alors « non lancé ». Il ne suffit pas d'omettre son `.sha256` : le bras B s'arrêterait sur la carte en code 1, et ce temps de carte serait perdu. Le bras B serait rejoué plus tard, sous devis à part.

   Je recommande (a) si la fille 10 la livre en moins d'une heure environ, sinon (b) (confiance moyenne).
3. **Écarts du bras B au point 7.** Plusieurs grandeurs du module ne sont pas écrites au point 7. Or la liste d'arrêt du texte scellé dit : « toute grandeur non écrite ici : nœud de Lazar ». **Nœud de Lazar avant toute lecture du bras B** (voir réserve 2).

## Verdict par pièce
| Pièce | Verdict | Motif |
|---|---|---|
| `scripts/lancer_t06_v10.sh` (`b98e84cf…`) | **prête** | Réserve de forme : la ligne 3 présente la v9 comme « module `session_v9.py` », alors que la v9 utilisait `session_v8`. Refus de plafond en code 2 avec son motif exact, éprouvé dans les deux sens ; « CRÉATION INCERTAINE » en code 4, éprouvé. |
| `scripts/amorce_instance_t06_v8.sh` (`29913ace…`) | **prête, avec réserve** | `bras_b()` est appelée après la poussée finale et avant l'arrêt, et rend toujours 0 ; 6 mutations sur 8 sont tuées. Deux chemins d'échec ne sont pas éprouvés (commit et poussée du bras B changés en fin anormale, mutations survivantes) ; les lire n'a pas d'effet sur T0.6. Le marqueur `t06-fin-normale` est posé avant le bras B : couple 7 de l'ordre. |
| `src/controle_ia/t06/session_v9.py` (`d0443323…`) | **prête** | `_INTROUVABLE` en « 404 » exact, 5 mutations sur 5 tuées. Réserve mineure : l'identifiant d'un message « 404 instance 999 not found » n'est pas comparé à celui demandé (essai 11, plus tard). |
| `scripts/fenetre_carte_t06_v1.sh` (`bc0a67c3…`) | **prête si l'ordre porte les couples 4 et 5** | Elle ne crée rien et ne loue rien. Elle s'arrête sans bascule sur toute réponse autre que « aucune offre conforme ». Écarts au GO-2026-11-07-02 : la sortie en code 10 tombe à `T0` + 2 h 45 et non à 3 h ; `FENETRE_N` et `FENETRE_PAS_S` ne sont pas bornés ; le repli H200 n'est gardé que par l'ordre. **Divergence déclarée** : le sous-agent dit « corriger avant la course ». Je juge que l'ordre suffit, parce que `env -i` n'hérite pas des variables et que la fille 6 attend l'heure. Une v2 du script avec `T0` consigné reste préférable si le temps le permet. |
| `src/controle_ia/audit_fuite_r1_v4/bras_b_v1.py` (`afacfedb…`) | **corriger avant la course** | (i) Ligne 513 : l'issue (`{"issue": …}`) est imprimée sur la sortie standard, qui devient `traces/bras-b-…/bras-b.out`, poussé non scellé. Il faut imprimer seulement le chemin et l'empreinte de la sortie. (ii) Banc insuffisant : 5 mutations sur 6 survivent (substitution par la même condition ; pli non tenu à l'écart ; a_SC_M contre l'honnête ; restriction de contexte retirée ; scores d'origine). Seuils 0,65 et 0,95 conformes au point 7 ; place et longueur gardées (G5 ; 51/51 et 10/10 jetons selon `P3-consignes-v1.md`, l. 70-77). |
| `config-bras-b-t06-v1.json` (`4fb0da20…`) | **prête si la mère écrit son `.sha256` au commit scellé** | `_main` appelle `verifier(config)` : sans compagnon, arrêt certain en code 1. Les 11 empreintes d'entrée sont justes. |
| Manifeste des copies (`935d93b1…`, 27 fichiers) | **prête, avec réserve** | Les 27 empreintes de l'arbre sont conformes. Côté source, 13 fichiers sur 27 sont recoupés ; les 14 autres ne le sont pas (commits `1d6bdc8d` et `05aa560f` absents en local, aucun fetch). G2 et G3 rattrapent sur la carte toute copie infidèle. |
| `rapport-bras-b-t06-v1.md` (`fc03ad62…`) | **réserve de forme** | Il annonce un « écart relatif ≤ 2e-3 ». Le code applique un écart absolu de 2e-3 × (1 + \|v\|), c'est-à-dire une tolérance mixte. Le compte de « 114 nombres » vient d'un passage de l'autrice sur les données réelles, non rejoué. Le code compare toute la sortie publiée et s'arrête au premier écart. |
| `config-t06-reel-v1-brouillon5.json` (`b7a5c1ba…`) | **prête** | Seul changement depuis le brouillon 4 : `stockage_max_usd_h` passe de 0,03 à 0,08. GO-2026-11-02-28, plafond 200 ; course A100 SXM4 80 000 Mo à 1,30 ; relance H200 NVL 140 000 Mo à 4,70. Clause de mémoire en Go : 78 et 136. |
| Candidat 10 (`c4083ffc…`) | **prêt, avec un couple** | Rejoué à l'octet. Ligne 220 : amorce v8 citée sous la forme lue par `controles`, empreinte au marqueur `<<EMPREINTE_AMORCE_T06>>`. Cela lève le point bloquant que le sous-agent avait relevé sur le candidat 9-r2 (ligne 219, amorce v7). Les sections « Hypothèses » à « Liste d'arrêt » ne sont pas touchées, et 5 marqueurs restent. Règle « mots et coût » : seuils 0,70 et +0,05, marqués « routine de la mère, contestables », conformes à GO-2026-11-07-03. |
| Brouillon d'ordre (`f9da98f3…`) | **corriger avant la course : 7 couples** | Plafond, fenêtre, bras B, engagement et lecture des offres la veille sont présents. Couples : voir plus bas. |
| Essais | **prêts pour T0.6 ; insuffisants pour le bras B** | 180 sur 180 en 494 s ; les 620 anciens `tests/test_t06_*.py` sont tous passés, en 3 lots. Le banc de mutations v9 ne voit ni `instance_seule` v9, ni `bras_b()`, ni la fenêtre, ni le module. |

## Les 7 réserves de la fille 10, tranchées
1. **Bras B jamais tourné sur carte** : réserve acceptée, non bloquante. G4 est justement le contrôle sur la carte. Le temps est borné, mais la vraie borne de l'annexe est d'environ 5 800 s, non 2 400 s : module, verrou et poussée. Cela fait environ 2 USD sur A100 et environ 7,6 USD sur H200 NVL, dans les 200 (couple 6).
2. **Tolérance de G4 : nœud de Lazar.** Le point 7 n'écrit ni contrôle d'identité ni tolérance, et sa liste d'arrêt renvoie toute grandeur non écrite à Lazar. Il faut lui soumettre ensemble, avant toute lecture du bras B, les grandeurs absentes du texte :
   - G4 et `TOLERANCE_IDENTITE` ;
   - la tolérance de 1e-9 de G3 ;
   - la restriction des actions à `contexte_conforme`, qui change la population des aires ;
   - le modèle du pli tenu à l'écart ;
   - l'issue « non tranché (signatures simultanées) » ;
   - les graines « blocs-b » et « identite-b » ;
   - les aires descriptives.

   **Recommandation** : sur A100, avec torch 2.14.1 et transformers 5.18.0, l'identité au bit s'applique et la tolérance ne sert pas. Je garde 2e-3 × (1 + |v|), coordonnée par coordonnée, pour le seul repli H200, en le déclarant (confiance moyenne). Le sous-agent préfère une tolérance sur le score de W en log-cote, la grandeur que la décision lit ; c'est l'option à soumettre en second. Le rapport doit dire « mixte » et non « relatif ».
3. **Configuration de la course** : brouillon 5, prête (voir la table).
4. **Cas R5 1 et 2 assouplis** : l'artefact est reproductible par mutation. Pour le cas 1, on retire ou change en `refus` le contrôle de l'heure de dépense épuisée (amorce v8, l. 217). Pour le cas 2, on retire le contrôle `t06-detruire` de la l. 103 et on ajoute un crochet `pre-push` qui dort. Le bras « artefact » v6, qui accepte `["DELETE"]`, ne prouve rien. Ce n'est pas bloquant : `test_t06_v7_amorce_minuterie.py` éprouve déjà v6 contre v7, et le diff v7 → v8 ne touche que le bras B. Essai 9 à ajouter.
5. **Texte « introuvable » de Vast** : tenu, « 404 » exact. Réserve mineure sur l'identifiant non comparé (essai 11) ; non bloquant, puisqu'une erreur reste non concluante et mène à l'arrêt.
6. **Citations du candidat** : le candidat 10 est juste pour la chaîne v10. Au candidat final, il faudra citer l'ordre de la course scellé, les ordres d'E3 réellement suivis (v6 à v9, R-1709 à R-1716) et la présente contre-lecture (couple du candidat).
7. **Banc de mutations du bras B : oui, avant la course.** GO-2026-11-07-04 exige des essais contre-lus avant la course, et 5 mutations sur 6 survivent. Les essais 1 à 5 ci-dessous suffisent à les tuer.

## Essais R5 à ajouter (bras B 1 à 5 avant la course ; le reste ensuite)
1. **Substitution réelle** : les identifiants du contexte contrefactuel diffèrent de l'origine sur l'empan de la note et de l'indication seulement, et sont égaux ailleurs. Artefact : substitution par la même condition.
2. **Pli tenu à l'écart** : chaque action est notée par `modeles[pli]`, vérifié par un calcul à la main. Artefact : pli décalé.
3. **Monde jouet à décalage planté** : un décalage dans la note doit donner « fuite », un décalage dans l'action « lecture du sabotage ». Cet essai tue les mutations « contre l'honnête » et « scores d'origine ».
4. **`contexte_conforme`** : comptes attendus quand une action antérieure est non conforme.
5. **Aucune issue** sur la sortie standard ni dans `traces/`.
6. **Amorce v8, poussée du bras B impossible** (crochet `pre-push`) et 7. **commit impossible** (crochet `pre-commit`). Attendus dans les deux cas : code 0, `t06-fin-normale`, aucun `t06-fin-anormale`.
8. **Échéance ou dépense épuisée pendant le bras B** : seulement `DELETE`, et le run déjà poussé reste intact.
9. Cas 1 et 2 de l'amorce, par mutation (réserve 4).
10. **Fenêtre** : pas de code 10 avant `T0` + 10 800 s ; intervalle de 900 s par défaut ; relance refusée sans fenêtre épuisée consignée (si une v2 du script est faite).
11. **`instance_seule`** : « 404 instance 999 not found » est non concluant pour l'identifiant 123.

## Couples
- Ordre : `couples-ordre-course-v1.json` (7 couples). Chaque « ancien » est unique dans `ordre-fille-6-t06-course-v1-brouillon.md` à `dfc032c6`, et les couples s'appliquent dans l'ordre (vérifié par script) :
  1. contrôles de la veille dans `$W/veille-course` et `$W/veille-relance` ;
  2. stockage de l'instance arrêtée relevé et compté au cumul ; destruction par identifiant après 72 h ;
  3. instance sans surveillance ;
  4. 3 heures pleines avant la relance H200 ;
  5. `FENETRE_N` et `FENETRE_PAS_S` jamais passés ; `fenetre.txt` vérifié ;
  6. borne de l'annexe, environ 5 800 s ;
  7. `bras-b.out` non ouvert ; `.sha256` de la configuration du bras B vérifié au commit ; arrêt par identifiant sur redémarrage ou silence pendant le bras B.
- Candidat : `couples-candidat10-v1.json` (1 couple, unique dans le candidat 10). Il ajoute à la liste des « citations définitives » l'ordre de la course scellé, les ordres d'E3 suivis et la présente contre-lecture.

## Concurrence
Rien de neuf à vérifier pour cette pièce. La course n'ouvre aucune revendication nouvelle ; celles de T0.6 et de l'audit de fuite restent sous leurs veilles respectives.
