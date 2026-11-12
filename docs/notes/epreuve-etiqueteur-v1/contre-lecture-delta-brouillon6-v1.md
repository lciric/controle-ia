# Contre-lecture bornée du delta — préenregistrement « épreuve de l'étiqueteur du sabotage flou », brouillon 6

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf (R2). Je n'ai écrit ni le préenregistrement, ni son code, ni aucune des trois contre-lectures précédentes, ni leurs couples.
- **Heures** (temps universel, `date -u`) : 8 novembre 2026, de 00:05:22 à 00:16:01.
- **Objet** : arbre `/home/user/wt-etiqueteur`, branche `prep/epreuve-etiqueteur-v1`, commit `2fd7d6b3a0b7db116261e0675f9232fc400aae36` (arbre propre avant et après) ; brouillon 6 `6b4ac2c265d1ddc14dc75718632cebda7450995b31f1456619caa1059ed70ea7`, comparé au brouillon 5 `f66a3e9d5a64e021b20db747dd8bd02e905523a2d0c9981c2a6fa4a649af3ea7` ; `appliquer_couples_brouillon6_v1.py` `6fbbe95b4eac5f1363d778fb4cef901b23b6d7a2bb8e7e60bc0f75d5d8408700` ; journal `651cac0c5a0591cef08ab6050cacbbccf129441337c3dd2e938a598f314e1699` ; `lire_items_phase1_v4.py` `627ebcb7dc8f6bd334edc53562a6128f0009427a858317b6fc44d1c10ab15d37`, comparé à la v3 `3fc929873042ed627f5a9aedfa33ca6a03b75e192340c28573459bc7457cff08` ; `test_lire_items_phase1_v4.py` `a097958005d48298e1d9bbb107741f3eb55bfe3a56633a9e15b3709abaaf1f4f`.
- **Ce qui fait foi** : contre-lecture bornée du delta du brouillon 5 `6c532d0b8ba245f33011e05055b11d488f45873813898935113918f026b5b631` et ses 11 couples `bc3f2926829db0dafca48cd2a6ed70a9d9504e6ef555ed5ec3ae0ba82f6c1e82` ; GO-2026-11-07-07 (plafond de 300 USD) et GO-2026-11-07-10, lus à `registres/go.md` sur `origin/main` (`beb8c5b4e`, lignes 267 et 270). La référence locale `main` (`a364e947e`) et le registre de cette branche ne les portent pas : la session mère scelle contre `origin/main`.
- **Rendus** : ce rapport ; `couples-contre-lecture-delta-brouillon6-v1.json` (12 couples, 13 occurrences ; chaque « ancien » présent exactement `n` fois au brouillon 6, sans chevauchement ; même format que les couples précédents).

## Verdict

**Scellable après couples. Aucun bloquant.**

1. **Couples et compléments** : les 11 couples sont appliqués à l'octet (brouillon 6 et journal reproduits à l'identique par le script tel quel, à une ligne près, expliquée) ; les 22 compléments (24 occurrences) sont justifiés ; **aucun seuil, critère, issue, plafond, effectif ni graine ne change**. Deux écarts de tenue, corrigés par couples : l'annexe C donne pour `test_lire_items_phase1_v4.py` une empreinte qui n'est plus celle du disque (fichier réécrit par la session mère après le rendu, la fausse clé seule : CD6-02, CD6-03) ; l'annexe C refaite (C6-22) a ôté sans le dire la ligne des empreintes de la génération d'essai v2, dont dépend le devis (CD6-11).
2. **Contrôle de la facture de l'essai de format** : écrit à l'ordre des opérations (point 6), entre l'essai et la lecture principale, pour Argon et pour Kimi : montant hors taxes au plus égal à la dépense estimée de ce lecteur au journal de l'essai, jetons égaux à l'arrondi près, sinon arrêt avant la lecture principale et nœud du directeur. Conforme.
3. **Six chemins fermés** en v4 : rejoués par les essais du dépôt (v4 propre, v3 fautive) et par mes 14 scénarios à fausse clé ; aucun message ne recopie une valeur reçue capable de porter une clé, aucune option n'est abrégée, aucun chemin refusé n'est recopié. **Un chemin voisin, hors des six et inchangé depuis la v3** : une clé passée comme `--sortie` devient le nom du dossier créé (aucun message, aucun contenu de fichier). Écrit à la limite 14 (CD6-06), non bloquant.
4. **Comportement** : hors du masquage et de CD5-11, rien ne change, sauf trois effets de bord des refus de chemins, dont un non dit (une entrée illisible ou mal formée rend désormais le code 2 au lieu de 7 : CD6-08).
5. **Citations** : le texte cite la v4 partout où il parle de la lecture en vigueur ; les noms des fichiers de sortie restaient ceux de la v2 depuis le brouillon 4 (CD6-04) ; le marqueur `<<COMMIT_EPREUVE_ETIQUETEUR>>` existe (trois fois), et c'est le seul problème que le validateur du dépôt relève.

## Ce que j'ai fait

- Vérifié toutes les empreintes compagnons du dossier : aucun écart.
- **Reproduit le brouillon 6** dans une copie du dossier (bloc-notes de la session), brouillon 6 et journal ôtés, avec `appliquer_couples_brouillon6_v1.py` tel quel (`--heure-fin 00:02:25`) : comptes 11 couples, 13 occurrences, 22 compléments, 24 occurrences ; **une seule ligne diffère**, celle de `test_lire_items_phase1_v4.py` à l'annexe C (et, par suite, l'empreinte de sortie au journal). En défaisant la concaténation de la fausse clé (ligne 439 du fichier d'essais), je retrouve exactement l'empreinte écrite à l'annexe C, `518ee459…` : le fichier n'a pas changé autrement.
- Compté chaque couple au brouillon 5 et au brouillon 6 ; lu le diff mot à mot du brouillon 5 au brouillon 6 en entier ; lu chacun des 22 compléments du script.
- Lu en entier le diff de `lire_items_phase1_v3.py` à `lire_items_phase1_v4.py` (14 blocs) et les essais ajoutés ; comparé les essais repris de la v3 (inchangés, aux noms de version près).
- Rejoué en environnement vidé (`env -i`) les cinq jeux en vigueur : **127 passés** à 00:07:59 (18,7 s), contre le fichier d'essais tel qu'il est au commit.
- Écrit, **hors du dépôt** (bloc-notes, dossier `b6/`), sans réseau ni clé réelle :
  - `essais/scenarios_v4.py` (`ff1974d03a7054706b2b7b85ab35b94ad6670be8696354bf41cd119ccfa6e1ed`) : fausse clé de 37 caractères écrite par concaténation, à la forme d'une clé Google, sans mot ni suite de chiffres ; 15 scénarios en mode simulé, lancés en sous-processus, chacun dans un dossier de travail neuf, contre la v4 et contre la v3 ; cherche chacun des 32 fragments de 6 caractères dans la sortie standard, la sortie d'erreur, le contenu de tout fichier écrit et **le nom de tout fichier ou dossier** ; résultats `rapport-v4.json` (`8d872cd907f83feaae3c2b62c6a6eaa05b4ece7ddcbbdfba3373768765d73f8b`) et `rapport-v3.json` (`bb6d9fece733f89be92013b8e486c324d2be014cf3e73ce1a02946b9ad79ce75`) ;
  - deux entrées mal formées (JSON coupé, octets non UTF-8), contre la v3 et la v4 (codes de sortie) ;
  - `essais/couples_b6.py` : écrit et vérifie mes couples (comptes, chevauchements, application sur une copie) ; le validateur du dépôt (`controle_ia.prereg.problemes`) sur le brouillon 6 et sur la copie couples appliqués ne relève que le marqueur `<<COMMIT_EPREUVE_ETIQUETEUR>>`.

## 1. Les 11 couples et les 22 compléments

**À l'octet** : chaque « ancien » figure `n` fois au brouillon 5 (13 occurrences) ; empreintes « ancien » et « nouveau » du journal égales à celles des couples ; reproduction exacte (ci-dessus). Six « nouveaux » figurent tels quels (CD5-01, 04, 06, 07, 08, 09) ; cinq sont retouchés par des compléments journalisés, chacun à cause de la v4, sans en changer le sens : CD5-02 par C6-09 (portée : « fermés en version 4 »), CD5-03 par C6-10 (ajout final), CD5-05 par C6-20 (contrôle de la facture rendu explicite), CD5-10 par C6-21 (ajout final), CD5-11 par C6-11 (ajout final).

| compléments | objet | constat |
|---|---|---|
| C6-01 à C6-03, C6-06 | titre, rédacteur, heures, base `01cd248e5` (existe) | justes |
| C6-04, C6-05 | statut ; demande de la session mère | justes ; le statut dit « non contre-lus » (CD6-01) |
| C6-07 | pièces : 24 + 79 + 12 + 6 = 121 essais, plus 6 démonstrations = 127 | vérifié (127 passés) ; 79 = 22 fonctions simples + 6 + 42 + 9 cas paramétrés |
| C6-08 | table « depuis le brouillon 5 » : 57 scénarios = 6 + 42 + 9 | juste ; « exceptions écrites sans leur message » trop large (CD6-12) |
| C6-09 (3), C6-10, C6-11 | masquage fermé en v4 ; limite 14 ; CD5-11 corrigé au code | conformes au code ; deux temps de verbe devenus faux (CD6-05, CD6-07) ; chemin voisin à écrire (CD6-06) |
| C6-12 à C6-18 | v3 → v4 dans les renvois au code en vigueur | justes ; les mentions de la v3 qui restent sont historiques |
| C6-19 | liste d'arrêt : chemin qui n'est pas un fichier, option abrégée (code 2) | juste ; manque l'entrée illisible, passée du code 7 au code 2 (CD6-08) |
| C6-20 | contrôle de la facture à l'ordre des opérations | conforme (section 2) |
| C6-21 | traitement de la contre-lecture bornée du delta du brouillon 5 | juste ; « ne sont pas contre-lus » (CD6-10) |
| C6-22 | annexe C refaite | empreintes justes au rendu sauf celle du fichier d'essais, réécrit après (CD6-02, CD6-03) ; **ligne de la génération d'essai v2 ôtée sans le dire** (CD6-11) |

**Grandeurs gelées** : le diff mot à mot ne touche aucun seuil (C1, C1-faible, C2, C3, garde de relecture, règle des 2 %), aucun critère ni issue, ni le plafond (300 partout), ni les effectifs (396, 60, 456), ni les graines (`SeedSequence([entropie, 3]).spawn(3)`, 20261107 pour la génération d'essai) ; au code, ni `LECTEURS`, ni les barèmes, ni `PLAFOND_ACCORDE`, ni `TENTATIVES_MAX_PAR_ITEM`, ni le feu vert. Les seuls nombres qui changent sont des comptes d'essais (63 → 121, 69 → 127, 21 → 79), d'heures et d'empreintes, tous vérifiés. Les codes de sortie changent pour deux familles d'arrêts, dites sauf une (section 4).

## 2. Contrôle de la facture de l'essai de format

Ordre des opérations, point 6 : « essai de format seul … contrôle écrit par le script … ; puis, **après le contrôle des prix** sur la facture ou le relevé d'usage de chaque fournisseur pour les seuls appels de l'essai de format (montant facturé, hors taxes, au plus égal à la dépense estimée de ce lecteur au journal de l'essai de format ; jetons facturés égaux, à l'arrondi près, aux jetons écrits ; pour Argon comme pour Kimi ; sinon arrêt avant la lecture principale et nœud du directeur) …, lecture principale et relecture ». Les cinq éléments demandés y sont, à la bonne place ; « Points ouverts », prix (CD5-06), dit le même contrôle et que le second lancement attend ce relevé ; la table « depuis le brouillon 5 » le résume. Sans couple.

Note : la dépense estimée lue au journal ne comprend pas une tentative interrompue (aucune ligne de journal), que le fournisseur facture ; le contrôle échoue alors, ce qui arrête : sens prudent, et ce cas est déjà un arrêt (code 7).

## 3. Masquage : les six chemins et les autres

Les essais du dépôt rejouent les six chemins exacts en sous-processus contre la v4 (code 2, aucun fragment, pas de dossier de sortie) et contre la v3 (fuite : artefact) ; 42 erreurs d'arguments et 9 chemins du fournisseur en mode réel, réseau remplacé. Tous passent. Mes scénarios, mode simulé, sans réseau, fausse clé neuve :

| scénario | v4 : code, fragment | v3 : code, fragment |
|---|---|---|
| `--feu-vert-format <clé>` (lecture principale) | 2, aucun | 7, **sortie d'erreur** |
| `--items=<clé>` | 2, aucun | 7, **sortie d'erreur** |
| `--question <clé>`, variable non posée | 2, aucun | 7, **sortie d'erreur** |
| `--rel=<clé>` (abrégée, ambiguë) | 2, aucun | 2, **sortie d'erreur** |
| `--registre-go <clé>` en mode simulé | 2, aucun (refusé, inutilisé en simulé) | 0, aucun (ignoré) |
| `--depense-engagee <clé>`, `--entropie=<clé>`, `--lectures <clé>`, `--variable-cle-gemini=<clé>` (variable posée), `--relais-kimi=http://127.0.0.1:<clé>`, `--cle=<clé>`, `-<clé>` | 2, aucun | 2, aucun |
| cas sain, clé posée | 0, aucun | 0, aucun |
| **`--sortie <clé>`** (dossier neuf, relatif) | **0 ; aucun message ni contenu, mais le dossier créé porte la clé pour nom** | idem |
| `--depense-engagee 300` (sans clé) | 2 ; « dépense déjà engagée 300.0 » : valeur reçue recopiée | idem |

- **Fermé** : `allow_abbrev=False` ; `Parseur.error` ne recopie plus rien du message d'`argparse` et ne nomme que des options connues du script ; les six chemins d'entrée sont contrôlés par `is_file` avant toute lecture et refusés sans recopie ; les messages de sortie existante, de fichier final, de relectures inconnues et de GO absent ne recopient plus de valeur ; `__main__` n'écrit plus que le type d'une exception imprévue. Les messages de la v4 ne recopient aucune chaîne reçue.
- **Restent recopiées**, de forme contrôlée et incapables de porter une clé : le nombre de `--depense-engagee` refusé par `GardeDepense` (un `float`), le nom de la variable de la clé quand elle est absente (forme `[A-Z_][A-Z0-9_]*`, qu'une clé Google ne peut prendre).
- **Chemin voisin** : `--sortie` n'est pas un chemin d'entrée ; une clé qui y serait passée devient le nom du dossier créé, sous le dossier courant, avec toutes les sorties dedans ; en v3 comme en v4. Même classe que les six (une clé écrite dans un argument qui ne la concerne pas), mais un nom de dossier peut finir dans un commit. Couple CD6-06 : règle d'exécution (sortie copiée de l'ordre des opérations, nom relu avant commit) ; correctif recommandé à une version ultérieure : en mode réel, où la clé est connue avant la création de la sortie, refuser un chemin de sortie qui en porte un fragment.
- **Observation hors du périmètre**, inchangée depuis la v3 : le masquage par fragments de 6 caractères altère tout texte écrit qui partage un fragment avec la clé. Ma première fausse clé contenait « lecteur » : les fichiers écrits portaient « arret_[clé] ». Ce n'est pas une fuite. Avec une clé aléatoire, la probabilité qu'une réponse ou un journal en soit touché est faible, mais pas nulle.

## 4. Comportement de la v4 hors du masquage

Diff v3 → v4, 14 blocs : version, dossier et fichier final (messages), compteur `comptees_au_pire`, bloc d'une tentative (CD5-11), messages des relectures et du GO, `Parseur.error`, contrôle des chemins, `allow_abbrev=False`, lecture des entrées et du manifeste de l'essai de format sous `try`, deux champs du manifeste, `__main__`. Rien d'autre.

- **CD5-11** : le corps d'une tentative passe sous un `try … except BaseException` ; une tentative interrompue avant le règlement est réglée au pire cas et comptée ; le manifeste écrit `tentatives_interrompues_comptees_au_pire` et `reserve_restante_dollars`. Essai : v3 sous-compte, v4 compte au moins le pire cas des 20 tentatives d'Argon, réserve restante 0. Aucune double comptabilité possible (`regle` posé juste après le règlement). Conforme.
- **Effets de bord des refus**, à classer comme des changements voulus du masquage :
  - (a) une option abrégée est refusée (dit, C6-19) ;
  - (b) `--registre-go` en mode simulé, et `--feu-vert-format` avec `--lectures format`, sont refusés s'ils ne désignent pas un fichier, alors que la v3 les ignorait. C'est sans effet sur les commandes de l'ordre des opérations, et couvert par « chemin d'entrée qui n'est pas un fichier » ;
  - (c) **une entrée illisible ou mal formée** (JSON coupé, octets non UTF-8) rend le code 2 au lieu du code 7, avant tout appel et toute écriture. C'est conforme aux codes du texte (« entrées refusées »), mais ce n'était pas dit : CD6-08.
- Les essais de la v3 sont repris sans changement, aux noms de version près.

## 5. Citations de la v4 et marqueur

- Renvois au code en vigueur : réglages `LECTEURS`, section « Lecture » et ses essais (14 noms cités, tous présents), ordre des opérations (point 2), points ouverts (R1, relais, R4), liste d'arrêt, pièces, annexe C : **v4 partout**. Les mentions de la v3 qui restent sont historiques (table « depuis le brouillon 4 », traitement de la contre-lecture du delta, annexe C « remplacée, intacte »).
- **Noms des fichiers de sortie** (section « Lecture », « Sorties ») : `reponses-phase1-A-v2.jsonl`, `journal-phase1-…-v2.jsonl`, `manifeste-lecture-phase1-v2.json`, inchangés depuis le brouillon 4. Or la v4 écrit `…-v4` (et la v3 écrivait `…-v3`). Le contrôle des fichiers avant l'analyse (CD5-07) et le `--feu-vert-format` du second lancement les désignent : CD6-04.
- Marqueur `<<COMMIT_EPREUVE_ETIQUETEUR>>` : présent trois fois (en-tête, table « depuis le brouillon 1 », ordre des opérations) ; le validateur le relève seul, avant comme après mes couples.
- Le texte d'aide (`Usage`) de la v4 cite encore `lire_items_phase1_v2.py` et `manifeste-lecture-phase1-v2.json` : simple commentaire du code, sans effet. À corriger à toute version ultérieure ; aucun couple.

## Remarques non bloquantes

1. **`--sortie <clé>`** : chemin voisin des six, inchangé depuis la v3 (CD6-06).
2. **Valeurs reçues encore recopiées** : un nombre et un nom de forme contrôlée, sans clé possible (CD6-06).
3. **Code 2 au lieu de 7** pour une entrée illisible (CD6-08) ; refus nouveaux d'options inutilisées dans un mode (section 4, sans couple).
4. **Annexe C** : empreinte du fichier d'essais à jour (CD6-02, CD6-03) ; ligne de la génération d'essai rétablie (CD6-11). La session mère recalcule toute l'annexe C au scellement.
5. **Temps des verbes** à la limite 14 et à la ligne R3 de la liste d'arrêt, devenus faux en v4 (CD6-05, CD6-07).
6. **Registre des GO** : le registre local de cette branche ne porte pas GO-2026-11-07-07 ; en mode réel, `verifier_go` lit par défaut `registres/go.md` de l'arbre où tourne le script. Le lancement doit passer un registre qui le porte, soit `--registre-go`, soit un arbre à jour d'`origin/main`. Sinon : arrêt sûr, code 2.

## Couples (12, 13 occurrences)

| identifiant | objet |
|---|---|
| CD6-01 | statut : compléments et v4 contre-lus par cette contre-lecture |
| CD6-02 | annexe C : empreinte en vigueur de `test_lire_items_phase1_v4.py`, et pourquoi elle diffère du rendu |
| CD6-03 | annexe C : 127 essais rejoués contre le fichier en vigueur |
| CD6-04 | noms des fichiers de sortie : `-v2` → `-v4` (six noms, un passage) |
| CD6-05 | limite 14 : « en version 3, deux chemins écrivaient » |
| CD6-06 | limite 14 : chemin voisin `--sortie`, deux valeurs encore recopiées, règle d'exécution |
| CD6-07 | liste d'arrêt, R3 : « en version 3, … était sous-comptée » |
| CD6-08 | liste d'arrêt : entrée illisible ou mal formée, code 2 (7 en v3) |
| CD6-09 | limite 7 : quatre contre-lectures, portée de la quatrième |
| CD6-10 | section « Contre-lecture » : ce rapport, son empreinte, son verdict |
| CD6-11 | annexe C : ligne de la génération d'essai v2 rétablie |
| CD6-12 (2 occurrences) | portée exacte de « exceptions écrites sans leur message » |

Aucun couple n'exige de correctif de code.

## Limites de cette contre-lecture

- **Bornée** : je n'ai relu que les couples, les compléments, la v4 contre la v3 et ses essais, et le contrôle de la facture. Je n'ai relu ni le reste du texte, ni l'analyse, ni le générateur, ni le devis v4, ni le guide.
- Aucun appel réseau ; mes scénarios sont en mode simulé (le mode réel n'est rejoué que par les essais du dépôt, fausses ouvertures).
- Messages d'`argparse` éprouvés sous Python 3.13.18 seulement.
- Une seule génération d'entrées pour mes scénarios (graine 777, hors du dépôt).

## Interdits tenus

Aucune lecture de `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*` ni `docs/notes/bras-attaque/`. Aucune clé ni variable d'environnement du poste lue : essais et scénarios en environnement vidé, seules des valeurs factices posées. Aucun appel réseau. Aucun commit, aucune poussée, aucun fichier `.sha256`. Aucun fichier existant modifié : arbre propre avant et après, tout lancé avec `-B`. Seuls fichiers ajoutés au dossier : ce rapport et le fichier des couples. Sorties de travail dans le bloc-notes de la session (`b6/`), hors du dépôt.
