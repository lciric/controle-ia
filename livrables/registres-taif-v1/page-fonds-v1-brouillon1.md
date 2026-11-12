# Page de mise à jour pour le fonds — brouillon 1 (mère, 5 novembre 2026, 21:10 UTC, `date -u`)

Tout chiffre renvoie à un chemin du dépôt privé `lciric/controle-ia-travail` (`main`) et à l'empreinte de la pièce (R6, R7). Aucune estimation : ce qui n'est pas relevé porte un marqueur `<<…>>`. Langue de travail : français ; à traduire pour l'entretien.

## 1. Où en est la porte G0 (programme v2, 8 critères ; échéance reportée à fin novembre 2026, N-027)
- **Prouvés : 2 sur 8.** Critère 1, harnais d'activations validé sur le modèle réel (`docs/verdicts/verdict-T0.4-critere-1-G0-v3.md`, `63444faa…`). Critère 5, agrégateurs validés en simulation, 31 prédictions sur 31 (`runs/20261004-080257-t03/manifeste.json`, `c9bba5e1…` ; réserve : lu au registre, aucun verdict scellé à part).
- **Restent : 6** — organismes à dose–réponse (T0.6, course visée le 11 novembre), sondes au-dessus du plancher (T0.7, jeux synthétiques en écriture : 14 tâches sur 32 au 5 novembre), base boîte noire, préenregistrements de G1 (brouillon 6) et du papier C scellés et contre-lus, état de l'art clos. Source : `livrables/registres-taif-v1/promis-livre-v1.md` (`a2bbb9fe…`).

## 2. Calibration : ce que nous avions prédit, ce qui est arrivé
- 30 préenregistrements scellés, 11 verdicts scellés par un lecteur d'une autre lignée, 181 prédictions chiffrées relevées par script (`calibration-v1.md`, `b4d7968a…`).
- **Parmi les 59 prédictions tranchées par un verdict : 47 confirmées, 4 réfutées, 8 non concluantes** (taux de confirmation 0,797 ; `lecture-a-la-main-calibration-v1.md`, `3dbbe51a…`). 23 non atteintes (expérience non jouée), 31 de T0.3 et 15 de la convergence sans verdict scellé, 53 sans run décisif.
- Les réfutations sont rapportées comme les confirmations (R3, R4) : le registre les nomme.

## 3. Résultat du jour : attaque de Goodhart contre le juge statistique (A1-v3, troisième course, verdict R13 scellé)
- Texte v4 scellé avant la course (`prereg/preenregistrement-attaque-goodhart-v3-v4.md`, `0b35494b…`) ; course conforme, 960 appels, aucune garde déclenchée.
- **W1 : « résiste (à cette taille) »** — 1 promotion sur 24 sous le nul v8 (borne haute de Wilson 0,202 < ε = 0,25). **W2 : « infirmée (brèche sous v8) », par classe non couverte** — 24 sur 24. Réserves R4 : course trop propre ; W1 tient sur une unité ; se rapporte avec les deux courses interrompues et avec A1, jamais seul. (`docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md`, `7dade9ef…`.)
- Ce que cela ne dit pas : rien sur la production ; « résiste » n'est pas « taux sous 0,05 ».

## 4. Données réelles déjà acquises, lectures en attente
- R1 v4 (sondes sur 2 400 actions, trois couches, modèle 8B) : fini, reçu, fiche de réception conforme (`docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/fiche-reception-r1-v4-v2.md`, `605931f3…`) ; lecture par les trois analyses préenregistrées sous un addendum des gardes contre-lu deux fois (brouillon 3, `81a04e7b…`), en attente du GO du directeur sur un écart déclaré.

## 5. Les deux prochaines semaines (plan daté, `docs/notes/g0-deux-semaines-v1/`)
- T0.6 dose–réponse : lanceur v2 (143 essais, 41 mutations tuées sur 41), brouillon 5, contre-lecture en cours ; course le 11 novembre (devis `devis-T0.6-dose-reponse-v1.md`).
- T0.7 sondes : jeux synthétiques et script de vérification ; G1 : brouillon 6, banc de 480 tâches ; SPARKS : tir de diagnostic de l'environnement.

## 6. Méthode et validation externe
Règles gelées R1 à R14 ; préenregistrement scellé avant toute lecture ; contre-lecture par un agent neuf ; verdict par une autre lignée de modèle ; registres de décisions (R-1 à R-1615), de GO, de dépenses, d'arrêts ; projet Open Science Framework privé `dr57c` (118 fichiers scellés, `livrables/osf-manifeste-v1/`) prêt à rendre public ; copie publique expurgée (`lciric/controle-ia`, script `scripts/depot_expurge_v5.py`).

## 7. Dépense
Par résultat : `livrables/registres-taif-v1/cout-par-resultat-v1.md` (`b16af955…`). Du jour : A1-v3 troisième course 58,45 USD (Argon) + 0,284 USD (machine) ; R1 v4 ≈ 7,7 USD. **Total de la phase 0 : `<<TOTAL_DEPENSES_PHASE0>>`** (sommé par le script v2 des registres, à venir).
