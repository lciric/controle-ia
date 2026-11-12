# Contre-lecture neuve (R2) de la v9 de la chaîne de T0.6 : amorce v7, lanceur v9, session_v8, ordres E3 v6 et E2-6 v1, configurations v3 — v1

## Consigne (message de la session mère, recopié mot pour mot)

> Mère — 20:25 UTC. **Contre-lecture de la v9 de la chaîne de T0.6**, d'un seul tenant, comme pour la v8 : un sous-agent neuf de lignée Opus lit le code ; toi, tu lis les ordres, les configurations et la concurrence. Aucune clé, aucune location, aucun `vastai`.
> **Objet** : branche `prep/t06-lanceur-v2`, commit `e940d4b2` (avance rapide depuis `1921fc3e`). Rapport du développeur (fille 10, Claude Sonnet 5.5) : `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v9.md` (`165a8684…`).
> - Code : `scripts/amorce_instance_t06_v7.sh` (`912d2c59…`), `scripts/lancer_t06_v9.sh` (`bda9f38c…`), `src/controle_ia/t06/session_v8.py` (`8069841a…`).
> - Banc de mutations v9 (`2b3b672a…`) et essais : v7_amorce, v9_scripts, v9_session, v9_nouveaux, v9_prix, v7_amorce_minuterie.
> - Ordres en brouillon : `docs/notes/g0-deux-semaines-v1/ordres-t06-e2-e3-v6/ordre-fille-6-t06-e3-v6.md` (`74c9502d…`, parti de l'ordre E3 v5 scellé, `docs/procedures/ordre-fille-6-t06-e3-v5.md`, `db0ad520…`) et `…/ordre-fille-6-t06-e2-6-v1.md` (`cd8e03f6…`, parti de l'ordre E2 v4 scellé, `4c1113cd…`), avec leur générateur `pieces/generer_ordres_v6.py` (`805e63ab…`).
> - Configurations : `config-t06-epreuve-e3-v3.json` (`30496584…`, seule différence attendue : plafond 4,3) et `config-t06-epreuve-e2-v3.json` (`e3b82b63…`, seule différence attendue : plafond 0,1).
> **Ce que la v9 doit faire** : tout le plan de la v9 dans R-1693, plus les décisions R-1696 à R-1701 (`registres/decisions.md` sur `main`). En particulier :
> - le correctif de concurrence C08 ;
> - `instance_seule` ;
> - le masquage, `set -u` et le refus de NaN ;
> - le stockage compté une seule fois ;
> - E2-3 (une initialisation et 3 commits) et E2-6 (journal d'échéance sur la branche) ;
> - la clause `gpu_ram` en Go ;
> - le plafond d'épreuve lu dans la configuration et borné par le reste du GO-2026-11-06-01 ;
> - le chemin de relance H200 NVL (GO-2026-11-07-02).
> **Quatre réserves du développeur à trancher par toi** :
> (1) la clause de relance vaut 136 Go (140000//1024), pas 140 : vérifie que `verifier_offre` refuse bien en dessous de 140000 Mo bruts ;
> (2) le texte de Vast pour une instance détruite est inconnu, alors que l'ordre E3 v6 demande de le recopier ;
> (3) pour E2-6, l'échéance devient « maintenant + 600 s » et la suite complète est jouée exprès ; le plafond de 0,10 est serré ; la borne du lanceur est ≤ 4,9, plus stricte que le GO ;
> (4) la cohérence de l'ensemble.
> **Rendu** : branche `prep/contre-lecture-t06-v9` partie de `e940d4b2`, contenant :
> - `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v9/contre-lecture-lanceur-T0.6-v9-v1.md`, avec un verdict par pièce : prêt, corriger avant E3, ou réserve ;
> - `couples-ordre-e3-v6.json` et `couples-ordre-e2-6-v1.json`.
> Aucun `.sha256` : je scelle. E3 doit partir avant le 10 novembre ; vise deux heures.

## Verdict par pièce

| pièce | verdict | motif |
|---|---|---|
| amorce v7 (`912d2c59…`) | **prêt** | correctif C08 en deux lignes, éprouvé, défaut reproduit sur la v6 ; aucun chemin vers un sommeil ou un arrêt quand l'heure d'épuisement est passée |
| lanceur v9 (`bda9f38c…`) | **réserve** (rien ne bloque E3) | refus de plafond en code 2 au lieu de 3 ; `creation-brute.json` brut, mais effacé aussitôt |
| `session_v8` (`8069841a…`) | **réserve** (rien ne bloque E3) | `_INTROUVABLE` (l. 84) accepte un nombre quelconque devant « not found » : « error: 500 not found » est lu comme une absence (vérifié). Faux `ARRET mort` possible si Vast répond ce texte deux fois ; couvert par la vérification à la main des ordres |
| essais | **réserve** | justes et verts ; 4 cas R5 manquants (ci-dessous) |
| banc v9 (`2b3b672a…`) | **prêt** | **passage complet unique rejoué** : 94 mutations tuées sur 94, 6 témoins verts |
| `config-t06-epreuve-e3-v3.json`, `config-t06-epreuve-e2-v3.json` | **prêt** | seule différence avec les v2 : `plafond_usd` (3,5 → 4,3 ; 1,5 → 0,1) ; **sans compagnon** au commit, à sceller |
| ordre E3 v6 (`74c9502d…`) | **scellable après 1 couple** (`couples-ordre-e3-v6.json`) | produit à l'octet par le générateur depuis l'ordre scellé v5 (`db0ad520…`) |
| ordre E2-6 v1 (`cd8e03f6…`) | **scellable après 3 couples** (`couples-ordre-e2-6-v1.json`) | produit à l'octet par le générateur depuis l'ordre scellé E2 v4 (`4c1113cd…`) |
| `<<COMMIT_EPREUVES>>` | **un commit de la mère sur `prep/t06-lanceur-v2`, descendant de `e940d4b2`**, qui ajoute les compagnons des deux configurations v3, sans toucher au code | à `e940d4b2` : le registre porte GO-2026-11-06-01 ; les quatre fichiers de tâches ont des compagnons justes ; les configurations v3 n'en ont pas, et `controles-epreuve` les exige |

### Qui lit quoi
- **Code, essais, banc** : sous-agent neuf de **lignée Claude Opus**, qui n'a lu ni ces pièces ni leurs versions antérieures, ni mes contre-lectures. Il a lu de 20:25 à 20:49 UTC. J'ai recoupé dans le code sa réserve sur `_INTROUVABLE` (appel direct : « error: 500 not found » et « http 500 not found » rendent Vrai).
- **Ordres, générateur, configurations, commit, concurrence, réserves du développeur** : fille 9, **lignée Claude Opus 5.5**. Le 7 novembre 2026, de 20:24 à 20:51 UTC (`date -u`). L'autrice est la fille 10, Sonnet 5.5.
- Rien de loué, aucune clé lue, aucun appel à `vastai`, aucune donnée réelle.

## 1. Code (sous-agent Opus)
1. **C08** (`amorce_instance_t06_v7.sh`, l. 191-193 et 102-103) : juste. Rejoué hors essai local avec un faux `curl`, sur trois cas :
   - second démarrage après une fin normale : la v6 envoie `PUT`, la v7 seulement `DELETE` ;
   - premier démarrage après l'heure : la v7 envoie seulement `DELETE` (sur la v6, le défaut dépend du minutage) ;
   - run interrompu redémarré : la v7 envoie seulement `DELETE`, sans les 180 s (effet de bord déclaré).
   - C08 est inchangée quand l'argent s'épuise en cours de marche.
   - Fenêtre résiduelle de l'ordre de la milliseconde, non bloquante.
2. **`instance_seule`** (`session_v8.py`, l. 54-96) : un objet sans `id` et un « 500 … 4040404 » sont non concluants ; un « 404 » avec « not found » est une absence ; une liste vide suivie de réponses illisibles donne `ARRET inventaire`. **Réserve** : l'expression `_INTROUVABLE` (l. 84) est trop large, et `{"id": null}` est lu comme une absence.
3. **Masquage** :
   - tout `PIPESTATUS` est lu, et un échec donne une ALERTE ;
   - `vast_masque` masque avant d'écrire, sans aucun fichier brut ;
   - les quatre clés sont couvertes ;
   - `set -u` donne le code 2.
4. **CUDA** : `nan`, `inf`, `-inf` et « nan » sont refusés.
5. **Stockage compté une fois** : avec 3,3617 et 0,0417, le prix de la carte vaut 3,3200 et la somme 3,3617. Pour E3 à 1,1083 avec un plafond de 4,3, l'épuisement tombe à 3,77 h, et la règle des 3 h passe.
6. **E2-3 et E2-6** : initialisation et 3 commits ; 5e commit « journal de l'instance (échéance) » ; tout est éprouvé localement, à 0 USD.
7. **Clause de mémoire** : voir la réserve 1 ci-dessous.
8. **Plafond** : borne en décimaux exacts (4,3 + 0,6 passe ; 4,31 + 0,6 est refusé). Écart : le code de refus est 2, et l'essai n'exige ni le code ni le motif.
9. **Relance H200 NVL** : filtre et choix sur les valeurs de R-1699 (rang 2 à 3,3617, derrière une offre au stockage de 0,097 refusée). **Le basculement « après 3 heures » n'est pas dans le code** : il revient à l'ordre de la course (argument `relance`).

**Comptes.** Suites `tests/test_t06_*.py` : **620 réussis sur 620**, en trois lots. Le rapport annonce 641 = 620 + 21 essais de `tests/test_cibles_invisibles_v1.py`, et l'écart 439 / 460 de la v8 s'explique de la même façon. Banc : 94 sur 94.

## 2. Ordres (fille 9)
- **Générateur rejoué** : `e3_v6` produit l'ordre E3 v6 **à l'octet** (`74c9502d…`) depuis l'ordre scellé E3 v5 (`db0ad520…`), par 30 remplacements tous trouvés. `e2_v5` produit l'ordre E2-6 **à l'octet** (`cd8e03f6…`) depuis l'ordre scellé E2 v4 (`4c1113cd…`).
- **Filtres** : ils sont lus dans `session_v8.filtre_recherche`, avec la clause en Go : A100 `gpu_ram>=78`, modeste `gpu_ram>=19`.
- **Ordre E3 v6** : le diff avec la v5 scellée ne porte que sur l'annoncé :
  - lanceur v9 et amorce v7, configuration v3, plafond 4,3 et condition « E2 finale + 4,3 ≤ 4,9 » ;
  - `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` ;
  - branche `essai/t06-e3-v4` ;
  - règle des 3 h sous 4,3 avec `dph_total` seul ;
  - 3 commits attendus ;
  - conduites : masquage, échéance, réponse sans `id`.
  - Les 3 couples de ma v8 et ceux de la mère sont conservés.
- **Couple E3-1** : sur trois ALERTE de masquage de suite, l'ordre dit « arrête la surveillance ». Or cela laisserait l'instance sans garde de dépense. Le couple dit : ne pas l'arrêter ; vérifier à la main ; message ; si elle s'arrête d'elle-même, la relancer ou relever soi-même toutes les 10 minutes.
- **Ordre E2-6 v1** : cadre, interdits et registre repris d'E2 v4 ; lanceur v9, configuration v3, branche `essai/t06-e26-v1`, `HF_TOKEN` non transmis.
  - **Couple 1** : la phrase « le lanceur refuse une échéance à moins de 600 s » est fausse. Le lanceur v9 n'exige qu'une échéance future et au plus la fin du GO (`lancer_t06_v9.sh`, l. 188) ; c'est l'ordre E2 v4 qui exige 600 s.
  - **Couple 2 (concurrence)** : avec un plafond de 0,10, l'heure d'épuisement calculée à la création peut tomber **avant** l'échéance si le prix est haut. La minuterie prendrait alors C08 (consignation, puis arrêt « stopped »), et E2-6 ne serait pas exercé. La règle de l'ordre (15 minutes de prix + forfait < 0,10) l'évite déjà en pratique ; le couple l'écrit en clair : `DEPENSE_EPUISEE_UTC_S` doit dépasser l'échéance d'au moins 120 s, sinon on n'exécute pas la création.
  - **Couple 3** (réserve 2 du développeur) : après la destruction, la v9 peut rendre `ARRET inventaire` plutôt qu'`ARRET mort`, si le texte de Vast pour une instance détruite n'est pas reconnu. Les deux issues sont attendues. On vérifie par la liste non vide et par `show instance`, et l'on recopie le texte exact, qui fixera les motifs de la version suivante.

## 3. Les quatre réserves du développeur
1. **Clause de relance à 136 Go : levée.** La garde locale juge en Mo bruts. Appel direct : 139 999 refusé, 143 771 accepté ; 79 999 refusé, 81 920 accepté, 40 960 refusé.
   - La clause `int(mo // 1024)` (78 et 136) peut laisser Vast rendre des offres que la garde refuse. Elles sont sautées sans consommer d'essai de création ; au pire, elles mènent à « aucune offre conforme », code 3.
   - Recommandation pour la version suivante : `ceil(mo/1000)` (80 et 140), sûr quelle que soit l'unité de Vast ; les offres de 81 920 et 143 771 Mo passent encore.
2. **Texte de Vast pour une instance détruite : réserve, traitée par le couple 3 d'E2-6.** Le relevé n'est pas un attendu. Le texte recopié servira à fixer les motifs, et à resserrer `_INTROUVABLE` (§ 1, point 2).
3. **E2-6** :
   - l'échéance à maintenant + 600 s, avec la suite complète jouée exprès, est cohérente : à E2, l'échéance de 10 minutes était tombée pendant l'installation ;
   - le plafond de 0,10 est serré, mais borné par la règle des 15 minutes et par le couple 2 ;
   - la borne de 4,9 est plus stricte que le GO (5), et à garder : marge de 0,10 pour les écarts que la garde ne borne pas. Conséquence à connaître : E2-6 sera refusé si E3 dépense plus de 4,2 USD (0,6 + 4,2 + 0,1 = 4,9).
   - **E2-6 se joue après E3** (R-1698).
4. **Cohérence de l'ensemble** : cohérent. Code, configurations, ordres et générateur se répondent ; les filtres viennent d'une seule source ; les conditions de dépense se répondent (E3 : E2 + 4,3 ≤ 4,9 ; E2-6 : E2 + E3 + 0,1 ≤ 4,9). Trois remarques :
   - **R12** : le commit `00387acc` modifie sur place `brouillons/ordres-t06-e2-e3-v5/ordre-fille-6-t06-e3-v5.md` et son générateur (régénérés depuis la v4). L'ordre scellé v5 (`docs/procedures/…-e3-v5.md`, `db0ad520…`) reste la référence et n'est pas touché, mais le brouillon d'origine (`f00e143d…`) n'est plus à la tête de la branche : à consigner.
   - `tests/test_t06_v9_nouveaux.py` est retouché après le commit du code (`47f316f6` → `e940d4b2`). Les comptes ci-dessus valent pour `e940d4b2`.
   - Le basculement de la relance H200 NVL « après 3 heures » est à écrire dans l'ordre de la course et dans le candidat final : le code ne le porte pas.

## Essais R5 à ajouter (version suivante)
1. Premier démarrage après l'heure de dépense épuisée, sans aucun run : seulement `DELETE`.
2. Run interrompu redémarré après cette heure : seulement `DELETE`, sans `PUT` ni 180 s ; artefact sur la v6 (`PUT` puis `DELETE`).
3. `instance_seule` : « error: 500 not found » et `{"id": null}` doivent être non concluants (échouent aujourd'hui) ; resserrer `_INTROUVABLE` sur « 404 » exact.
4. Lanceur :
   - refus de plafond avec code et motif exigés (code 3, si c'est le code voulu) ;
   - échec du masquage dans `apres-creation` → « CRÉATION INCERTAINE », sans fichier brut.
