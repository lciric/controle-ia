# Contre-lecture neuve (R2) de l'amorce v5, du lanceur v7, des essais « cibles invisibles », des ordres E2/E3 v4 et du candidat 6 de T0.6 — v1

## Consigne (message de la session mère, recopié mot pour mot)

> Mère — 14:05 UTC. **Contre-lecture d'un seul tenant : amorce v5, lanceur v7, essais « cibles invisibles » de T0.6, ordres E2/E3 v4, candidat 6** (R-1677 à R-1679). Rectification d'abord (R-1666) : l'autrice, la fille 10, est **Sonnet 5.5**, pas Opus comme je te l'avais écrit. Cette fois, tout lecteur est de lignée **Opus**. Le code va à un **sous-agent neuf** (`model: opus`), qui n'a lu ni ces pièces ni leurs versions antérieures. Les ordres et le candidat, tu peux les lire toi-même. Déclare qui lit quoi.
> Contexte : E2 s'est arrêtée à 10:55 environ, sans trace. L'amorce v4 clonait ≈ 3,9 Go ; l'hôte n'a reçu que 1,4 Go, soit ≈ 10 Mb/s effectifs ; refus puis destruction en 5 s, ligne de refus perdue ; la `surveillance` v6 était aveugle à la disparition (R-1676, R-1677).
> **Pièces** (empreintes vérifiées par la mère) :
> - `prep/t06-lanceur-v2` à **`04d89122`** (code à `c356b836`, descendant de `f16bcffa`) : `scripts/amorce_instance_t06_v5.sh` (`c4395338…`), `scripts/lancer_t06_v7.sh` (`5ff2629c…`), `src/controle_ia/t06/session_v6.py` (`38a61232…`), `tests/test_t06_v5_amorce.py`, `tests/test_t06_v7_scripts.py`, `tests/test_t06_cibles_invisibles_v1.py` (`0eada746…`) ;
> - `tests/test_cibles_invisibles_v1.py` (`b5fd257b…`), **seul fichier changé hors de T0.6** (registre : 12 « couvert », 5 lecteurs admis) ;
> - `scripts/banc_mutations_t06_v7.py`, le journal d'E1 v7, le journal d'essai local de l'amorce, `rapport-developpeur-lanceur-T0.6-v7.md` (`9026cccf…`) ;
> - ordres `brouillons/ordres-t06-e2-e3-v4/` (E2 `8a79079f…`, E3 `63b2fcac…`, générateur `92dd7580…`) ;
> - `prep/t06-candidat2-v1` à `2a55adc6` : `brouillons/T0.6-organismes-v0-v1-candidat6.md` (`3250b1f8…`) et ses pièces.
> **Questions** :
> 1. **Différences** amorce v4 → v5 et lanceur v6 → v7 : seulement ce qui est annoncé ? Clonage partiel à 27 motifs, ligne `CLONAGE`, attente de 180 s sur `refus` et `refus_precoce`, `ARRET mort` (deux relevés à 15 s, ALERTE sur inventaire vide ou appel en échec), copie masquée du journal entier, `inet_down>=500`.
> 2. **Liste des chemins extraits** : couvre-t-elle tout ce que l'instance lit, dans les **deux modes** (épreuve jouet et course réelle), y compris la suite complète d'essais ? Rien de nécessaire n'est-il exclu ? Rejoue la suite complète sur un clone allégé (la fille 10 annonce 2 920 réussis, 0 échec, 0 sauté), les suites t06 (347) et le banc (38 sur 38). Aucun secret dans le journal copié ?
> 3. **Cibles invisibles (N-060)** : les 5 « lecteurs » ne lisent-ils vraiment que `config["adaptateur"]["cibles"]`, les modules de l'adaptateur, et jamais la référence cachée ? L'essai à marqueur couvre-t-il réellement les 12 constructeurs, sur les tâches d'évaluation et de distillation, avec ses artefacts ? Réserve déclarée : modèle jouet seulement. Le changement du registre existant est-il minimal et juste ?
> 4. **Ordres v4** : issus des ordres scellés v2, à l'octet hors couples ? Commandes v7 ; branches `essai/t06-e2-v2` et `essai/t06-e3-v2` ; ligne `CLONAGE` attendue (≤ 600 Mo ; 20 minutes sans ligne neuve → destruction par l'identifiant) ; conduite sur `refus` et `ARRET mort` ; plafonds et condition d'E3 (≤ 4,9) inchangés ; filtres égaux à ceux du lanceur ; seul marqueur `<<COMMIT_EPREUVES>>`. Dis par quel commit le remplir.
> 5. **Candidat 6** = candidat 5 + O1–O11, par script, à l'octet ; cinq marqueurs restants ; citations cohérentes.
> 6. **Verdict** : scellable ou couples résiduels, par pièce.
> Rendu sur `prep/fille-9-contre-lectures-v2`, dossier `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v7/`, puis message. Aucune donnée réelle, aucune clé, aucune location. C'est le chemin critique de la course du 11 : vise une heure.

## Verdict par pièce

| pièce | verdict |
|---|---|
| ordres E2 et E3 v4 | **scellables après couples résiduels** (E2 : 2, `couples-ordre-e2-v4.json` ; E3 : 2, `couples-ordre-e3-v4.json`), puis `<<COMMIT_EPREUVES>>` = **`04d89122`** (le même pour les deux) |
| amorce v5 | conforme pour E2 et E3 ; deux réserves mineures (message de `sparse-checkout` jeté ; délai de `checkout` passé de 600 à 900 s, non annoncé) |
| lanceur v7 et `session_v6` | **utilisables pour E2 et E3 avec les couples des ordres** ; **corrections exigées avant la course** (v8) : inventaire vide lu comme absence, `--tail 2000`, alertes d'inventaire silencieuses, journal brut écrit avant masquage |
| essais « cibles invisibles » | conformes sur les 5 lecteurs et les 12 constructeurs ; trois corrections mineures de l'essai à marqueur |
| registre `tests/test_cibles_invisibles_v1.py` | conforme (purement additif) ; admission par fonction plutôt que par expression : recommandation |
| candidat 6 | **prêt pour les marqueurs finaux** ; si les couples des ordres sont appliqués, les deux empreintes d'ordres qu'il cite sont à remettre à jour par son script |

### Qui lit quoi
- **Code, essais, banc, cibles invisibles** (questions 1 à 3) : sous-agent neuf de **lignée Claude Opus**, qui n'a lu ni ces pièces ni leurs versions antérieures, ni mes contre-lectures. Il a lu de 14:04 à 15:03 UTC. J'ai recoupé ses deux constats principaux dans le code (`session_v6.py`, l. 48-50 ; `lancer_t06_v7.sh`, l. 244 contre la v6, l. 240).
- **Ordres, commit d'épreuve, candidat 6** (questions 4 à 6) : fille 9, **lignée Claude Opus 5.5**. L'autrice est la fille 10, de lignée Sonnet 5.5 (rectification R-1666). Le 7 novembre 2026, de 14:03 à 15:05 UTC (`date -u`).
- Rien loué, aucune clé lue, aucun `vastai`, aucune donnée réelle.

## 1. Différences (sous-agent Opus)
- **Amorce v4 → v5** : tout ce qui est annoncé est présent. Trois écarts ne sont pas annoncés :
  - le `checkout` passe de 600 à 900 s, soit un pire cas de clonage de 1 800 s ;
  - `sparse-checkout … 2>/dev/null` jette le message de git, et le refus ne donne qu'une cause générique (demi-repli muet, R5) ;
  - la ligne « début v4 » n'est pas renommée.
- **Attente de 180 s** : bornée. Elle ne franchit aucun plafond, car la minuterie et l'épuisement de la dépense restent actifs pendant `refus`. Réserve d'exploitation : avec `INTERVALLE=120`, un relevé peut durer plus de 180 s, et la ligne de refus peut lui échapper.
- **Lanceur v6 → v7** :
  - **non annoncé** : `logs --tail 20000` devient `--tail 2000` (l. 244) ; la copie n'est donc pas « le journal entier » ;
  - **repli trompeur** : `instance_presente` (`session_v6.py`, l. 48-50) lit un inventaire `[]` ou `null` comme une absence. Deux listes vides à 15 s d'écart donnent `ARRET mort … rien à arrêter`, et la surveillance s'arrête, contrairement à l'annonce « ALERTE sur inventaire vide ». La dépense reste bornée par la minuterie de l'instance (heure d'épuisement calculée à la création), mais l'instance n'est plus surveillée ;
  - les ALERTE d'inventaire ne vont que dans `surveillance.txt`, sans compteur de répétition ;
  - le journal brut `journal-tour.txt` est écrit avant masquage (défaut hérité de la v6). Les valeurs de clé courtes (6 caractères ou moins) ne sont pas masquées, et seul le jeton GitHub est éprouvé ;
  - `session_v5` → `v6` : `inet_down>=500` et `instance_presente`, comme annoncé.

## 2. Les 27 motifs (sous-agent Opus)
- **Clone allégé du commit `04d89122`** (`--no-checkout`, puis `sparse-checkout --no-cone`, avec les 27 motifs du script) : 328 Mo et 2 920 essais collectés.
- **Suite complète** : **2 917 réussis, 3 échecs, 0 sauté**. Les 3 échecs sont dans `test_corpus_arxiv.py` : il manque `pypandoc` dans l'environnement local ; l'instance l'installe par `requirements-donnees.txt` (non vérifié sur une instance ; R-1679 b).
  - La suite a été jouée par tranches. Sous charge, quelques « F » sans nom sont apparus dans des tranches coupées à 900 s, et tous les fichiers en cause repassent ensuite. **Réserve** : essais peut-être sensibles à la charge, à surveiller à E3-2.
- **Mode réel** : `prereg/`, `donnees/`, `requirements-*.txt`, `registres/go.md` et les configurations sont extraits. Rien de nécessaire n'est exclu d'après ce jeu. Note : `--no-cone` exige git 2.35 ou plus ; l'image `python:3.11-bookworm` porte git 2.39.
- **Suites t06** : **354 réussis** (les 347 annoncés, plus les essais « cibles invisibles »).
- **Banc** : non rejoué. Son journal compte 38 mutations tuées sur 38, avec 2 témoins verts ; aucune ne couvre l'inventaire vide, `tail` ni le masquage des clés autres que GitHub.

## 3. Cibles invisibles, N-060 (sous-agent Opus)
- **Les 5 lecteurs** ne lisent que `config["adaptateur"]["cibles"]` : `configuration.py` l. 87-95 ; `lanceur.py` l. 495-496 ; `lanceur_v2.py` l. 282-283 ; `lanceur_v3.py` l. 289-290 ; `lanceur_v4.py` l. 236-237.
  - L'admission se fait par fonction entière : une future lecture de `tache["cibles"]` dans la même fonction passerait le contrôle statique. Recommandation : admettre par expression.
- **Les 12 constructeurs** sont tous exercés : un compteur sur la répétition jouet des 4 versions le montre. Le marqueur est posé dans les tâches d'évaluation et de distillation.
- **Trois défauts mineurs de l'essai** :
  - les champs numériques des cibles ne portent pas de marqueur ;
  - l'artefact n'est joué que sur la v4, et il n'affirme pas les fichiers écrits ;
  - aucun artefact ne vise un constructeur qui lirait `tache["cibles"]` directement.
- **Réserve « modèle jouet »** : restent ouverts la fuite par un vrai modèle (poids, distillation sur de vraies transcriptions) et les fichiers binaires, qui ne sont pas balayés.
- **Registre** : +24 lignes, purement additives (12 « couvert », 5 lecteurs admis avec raison) ; aucun contrôle existant affaibli.

## 4. Ordres v4 (fille 9)
- **Générateur rejoué** : il lit les ordres scellés de `main` (`docs/procedures/ordre-fille-6-t06-e2-v1.md` `8ad0ca95…`, `…-e3-v1.md` `97a45a31…`, empreintes vérifiées) et produit les deux ordres **à l'octet** (`8a79079f…`, `63b2fcac…`) par 12 remplacements uniques.
  - Le diff avec les ordres scellés ne porte que sur ce qui est annoncé : en-tête, section « Scellement » retirée, `lancer_t06_v7.sh`, `amorce v5`, configurations v2, branches `essai/t06-e2-v2-a|b|c` et `essai/t06-e3-v2`, ligne `CLONAGE` (au plus 600 Mo, 20 minutes), règle des 20 minutes sans ligne `AMORCE` (destruction par l'identifiant), `refus` (180 s) et `ARRET mort` (absence), et filtres.
- **Filtres** : égaux à `session_v6.filtre_recherche` (`… reliability>=0.98 inet_down>=500 …`), lus à une seule source.
- **Inchangés** : plafonds (1,5 / 3,5 / 5) et condition d'E3 « dépense réelle d'E2 + 3,5 ≤ 4,9 ».
- **Restes** : aucun reste de v3 à v6, aucun `<OFFRE>`. Seul marqueur : `<<COMMIT_EPREUVES>>`, deux fois par ordre.
- **`<<COMMIT_EPREUVES>>` = `04d89122`** :
  - il contient le code `c356b836` (de `c356b836` à `04d89122`, seuls le rapport v7 et le journal d'essai changent) ;
  - `registres/go.md` porte GO-2026-11-06-01 ;
  - les deux configurations v2 ont leur compagnon, égal à l'empreinte : e2 `ad527fa1…`, e3 `f41ea5e8…`.
  - Si le lanceur est corrigé en v8 avant E2, il faudra un nouveau commit.
- **Couple résiduel E2-1 (argent)** : l'instance A part avec une dépense antérieure de `0`, alors que la tentative d'E2 de ce matin (instance 59555071, environ 40 minutes, R-1671 à R-1677) a coûté. Ce coût ne figure pas dans `registres/depenses.md` de `main`. Couple : `ANT_A` = ce coût (la facture, sinon prix × heures + forfait), écrit. **Couple E3-2** : la condition d'E3 le compte explicitement.
- **Couples E2-2 et E3-1 (argent)** : sur `ARRET mort : absente de l'inventaire`, l'ordre dit « rien à détruire ». Or le lanceur v7 lit un inventaire vide comme une absence (point 1). Couple : confirmer par `show instance <ID>` (l'instance seule, pas la liste) ; si elle répond, destruction par l'identifiant ; si l'appel échoue sans dire « introuvable », message avant toute autre création.
- **Note, sans couple** : la règle « relève la ligne de refus pendant 180 s » est fragile avec `INTERVALLE=120`. La copie `journal-instance.txt` du dernier relevé reste la source. La mère peut abaisser `INTERVALLE` à 60 pendant le clonage.
- **À inscrire** : la dépense de la tentative d'E2 du 7 novembre, dans `registres/depenses.md`.

## 5. Candidat 6 (fille 9)
- Rejoué par script : le candidat 5 plus les 11 couples O1 à O11 donnent le candidat 6 **à l'octet** (`3250b1f8…`). Les valeurs du script sont remplies, avec l'heure 14:01 et les 13 empreintes **recalculées sur les fichiers de `04d89122`** : amorce v5, lanceur v7, `session_v6`, rapport v7, essais, banc, E1, journal d'essai, ordres v4. Chaque « ancien » est unique.
- Cinq marqueurs restants présents ; aucun `<OFFRE>`. `<<EMPREINTE_AMORCE_T06>>` vise `amorce_instance_t06_v5.sh`. Les mentions du lanceur v4 et v6 et de l'amorce v4 sont historiques (l. 15, 149, 167, 650).

## Corrections de code proposées pour la course (v8 ; essais R5)
1. `instance_presente` : une liste vide ou `null` n'est pas une absence. Sur une liste vide, ALERTE et confirmation par `show instance <ID>`. Essais : `[]` deux fois → ALERTE et poursuite ; liste non vide sans l'identifiant → `ARRET mort`.
2. `--tail 20000`, ou l'annonce « 2 000 dernières lignes ». Mutation au banc.
3. ALERTE d'inventaire sur la sortie standard, avec un compteur de trois répétitions, puis escalade.
4. Masquage par un tube, sans fichier brut ; refus de toute clé présente de moins de 8 caractères ; essai qui couvre les quatre clés.
5. Amorce : citer le message de `sparse-checkout` dans le refus ; annoncer les 900 s.
6. Essai à marqueur : champs numériques marqués ; artefact sur les 4 versions, avec les fichiers écrits ; constructeur muté qui lit `tache["cibles"]`.
