# Addendum 2 à l'ordre de la course de dose-réponse exploratoire (fille clés 2) — v1

- **Ordre amendé** : `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` (`4c6c70d4e496bf2fd009cc25133a319151af600ec64065eb33903963fbda17a0`, scellé, inchangé, R12) ; addendum 1 (`8075ae07…`, scellé, inchangé, toujours en vigueur).
- **Écrit par la session mère** le 9 novembre 2026 vers 01:30 UTC (`date -u` au registre, R-1956), après l'arrêt de la première instance pendant la suite ciblée (R-1920 à R-1922) et la correction de la chaîne (R-1941, R-1943).

## Cause

Première instance 59755494 : suite ciblée **3 échecs sur 2 015** (deux gardes « cibles invisibles » qui ne connaissaient pas `lanceur_v6.py`, un aléa de la configuration jouet d'un essai), arrêt par l'amorce avant tout run, traces rapatriées (`essai/t06-explo-v1`, `3cdd22ce`), instance détruite par son identifiant. Aucune ligne de code de production n'était en cause.

## Ce qui change (et seulement cela)

1. **Commit d'épreuve** : **`1609a4bf2c1572f72bb8542d81d963ac6a8481c4`** sur la branche **`prep/t06-explo-v2`** poussée (`T06_BRANCHE_CODE=prep/t06-explo-v2`) = `035423ad0c9f977a6e984a87c51e32f72bf15dda` + deux commits (`e82aa7c5`, `1609a4bf`) qui ne touchent **que six fichiers d'essais** : `tests/test_cibles_invisibles_v2.py`, `tests/test_t06_cibles_invisibles_v2.py`, `tests/test_t06_lanceur_jouet.py`, `tests/test_t06_v2_lanceur_jouet.py`, `tests/test_t06_v3_lanceur_jouet.py`, `tests/test_t06_v11_lanceur_jouet.py` (`git diff --name-only 035423ad 1609a4bf`, vérifié par la mère). **Les quatorze fichiers de la chaîne du § 1 de l'ordre sont inchangés** : leurs empreintes se recalculent à l'identique au nouveau commit (`git show 1609a4bf…:<chemin> | sha256sum`), et la liste figée v3 garde `e76d5e6b7c32140b549de20f061a2e562df9201c5daab4060fd1ca54a05f42e2`.
2. **Liste ciblée rejouée par la mère** au commit `1609a4bf` : **2 022 passés, 0 échoué, 0 sauté** (46 min 49 s, 9 novembre, R-1956).
3. **Noms neufs (R12)** : dossier de travail `$W/explo-a2` (jamais `explo-a1`) ; branche poussée par l'instance `T06_BRANCHE=essai/t06-explo-v3` (jamais `essai/t06-explo-v1` ni `-v2`).
4. **Dépense antérieure** : `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` = **2,14** (première instance, estimation de la fille, R-1921 ; la facture relevée la remplace si elle est connue avant la création).
5. **Calendrier** : `calendrier.dernier_jour_creation` = 2026-11-09 dans les deux configurations : la création doit avoir lieu **le 9 novembre UTC au plus tard** ; sinon arrêt, compte rendu, nouvelle configuration (hors de cet addendum).
6. **Mot de Lazar** : toute création après le 8 novembre 21:34Z exige le **mot de Lazar écrit dans la session de la fille** (§ 5 de l'ordre, « Bascule à ≈ 21:34Z »). Sans ce mot, rien n'est créé.
7. Le reste de l'ordre et de l'addendum 1 est inchangé : `controles-epreuve` (code 0 attendu), puis `creation auto course 0 "$W/explo-a2"`, fenêtre à 1,30 USD/h (douze essais à quinze minutes), configuration v2 à 2,10 sur décision de la mère, commande imprimée contrôlée avant exécution, surveillance, rapatriement, destruction par l'identifiant du seul identifiant créé ; les instances 58936096, 58936099, 58936100 restent intouchables.
