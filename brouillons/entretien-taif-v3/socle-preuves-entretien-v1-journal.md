# Journal — socle de preuves pour l'entretien avec le Transformative AI Fund — v1

- Rédacteur : sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5 (`claude-opus-5-5`).
- Heures (`date -u`) : vérification des empreintes de la consigne 2026-11-10 09:16:10 ; début de la rédaction 09:25:24 ;
  registres rehachés 09:29:10 ; fin : dernière ligne de ce journal.
- Sortie : `brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md` (nom neuf), et ce journal ; tous deux scellés par
  `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller`. Aucune autre écriture.

## Sources lues, avec empreintes (toutes recalculées par `sha256sum` ; celles qui ont un compagnon vérifiées par `controle_ia.scellement verifier` : OK)

| pièce | chemin | sha256 | lu |
|---|---|---|---|
| consigne | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-socle-preuves-entretien-taif-v1.md` | `a961fef642c128929390db50025011bd8f41489a03e25fd0fd82abaa013f4783` | en entier, après vérification |
| interdits communs v2 | `…/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | en entier |
| programme d'entretien v18 | `brouillons/entretien-taif-v3/programme-entretien-taif-v18.md` | `e58ccfedf959748c7dfc9b987f2c7d3c7aa72492e9a5847ac0ceecc7b5a68643` | en entier (correction de la mère : `e58ccfed…`, non « 24e… ») |
| contre-lecture v17 | `brouillons/entretien-taif-v3/contre-lecture-v17-v1.md` | `ea256783988605e236f537e26ec779435ff0293f18e0bb867859da64e7215d90` | en entier |
| texte de candidature envoyé | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` | `b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0` | en entier (420 l.) |
| budget envoyé | `docs/sources/candidature-taif-2026-10-07/budget_v3_TAIF_2026-10-07.txt` | `caec18b296c7a7cbda35ffc993667a339f891fe322f512a9731bc7a3bb7f92c7` | en entier |
| verdict officiel d'A1-v4 | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` | en entier |
| verdict du critère 1 de G0 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | `63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13` | § 1 et § 2 (début) |
| verdict P3 v2 | `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751` | l. 1-60 |
| verdict de l'audit de fuite | `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` | `320463e6c03189178a2436742fe78e1edeae59d6a738a52de581924d837929d7` | en entier |
| verdict de l'étiqueteur, phase 1 | `docs/verdicts/verdict-etiqueteur-phase1-v1.md` | `9f7830b95cc0238d09d5846798c4ff12dba07644271330d4ed6ec43d555c6eae` | l. 1-30 |
| verdict A1-v3 | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135` | l. 1-25 |
| verdict de validation du nul v9 | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` | l. 1-20 (non cité au socle) |
| autres verdicts de `docs/verdicts/` | 17 fichiers `.md` | sceaux tous OK | empreintes seulement |
| T0.6 scellé | `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | l. 373-635 (Hypothèse à Puissance), l. 710-772 (plan, concordance) ; section « Ce que les auteurs savaient » non lue |
| P3 | `prereg/P3-premier-test-i-a-v1.md` | `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672` | sceau seulement |
| T0.4 v3, T0.3 | `prereg/T0.4-validation-modele-reel-v3.md`, `prereg/T0.3-simulation-lemme-theoreme-v1.md` | `4f711cd3…`, `7474743a0fa2a9db5da85bcedb0087ea57114fcca0fbb3415c7a97bf1b78d1fb` | sceaux seulement |
| P3-bis brouillon 10 (non scellé) | `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` | `9038a015c5756a289bebd2f08b1c33b1f2a26eb829bb2c4bc2afec04648fd1f9` | l. 1-40, 452-662, 910-960, 987-1048, 1337-1374 |
| ordre de la course 7a | `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` | `4c6c70d4e496bf2fd009cc25133a319151af600ec64065eb33903963fbda17a0` | l. 3, par motif seulement |
| registre des décisions (vivant) | `registres/decisions.md` | `b3d96dfe03e5b292d846b6757734a3264269327dcb3f4fa714f14386f58a2a05` | R-2050 à R-2115 (l. 2008-2073) en entier ; R-327, R-522, R-749, R-765, N-027, R-1579, R-1580, R-1757, R-1834, R-1836, R-2021, R-2039, R-2040 (début) |
| registre des GO (vivant) | `registres/go.md` | `e682abb0db3a0da37c0d764a7c659f638d449df266f6c9580d3ec481c8d44155` | en-tête ; l. 210, 216, 217, 256, 262, 264, 267, 282, 283, 290-296 |
| registre des dépenses (vivant) | `registres/depenses.md` | `e7b83d372f4795e073bf5fda6d23bb9d74743aca9df2777c15e3186642740f1b` | l. 1-20, 395-413 |
| registre des scellements | `registres/scellements-v1.md` | `d48af4f5d7682c2a5051cb9ed8ef31ece6aaf063a787bd0c4357f2fad559c046` | en entier (4 l.) |
| état vivant | `registres/etat.md` | `ae1f31362c047a062949b6172ed20d4224e176bbfb100c8deb169895e0b909c7` | lignes de G0 par motif (l. 162, 180) |
| table scellée des dépenses | `livrables/registres-taif-v4/total-depenses-v3.md` | `123be1a7e1c345574d451a0e4ee31f3193f6b7fc1a522f2e293934e03b94ea21` | l. 1-30, 51, 53, 58 |
| calibration | `livrables/registres-taif-v4/calibration-v3.md` | `0f1bca5aa900bffed944b9f7c0b2b5f1b2a137b2b3c8337c9b0b28e3d881c0f4` | l. 70-76, 262-270 |
| résultats de T0.3 | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757ab83d5de7a346ebf08bebf89aef61e4337cb5c067e5fd545` | sceau seulement |
| dépôt chez le tiers | `livrables/osf-manifeste-v1/manifeste-v1.json` ; `livrables/osf-depot-epreuve-etiqueteur-phase1-v1/depot-epreuve-etiqueteur-phase1-v1.json` | `dd87b23ebc03dbb6b6d00aeeadc6685174aad04cccf72f93b72332a113e061c6` ; `ab240b401de2f9a6edb69dfc14ac9dfdc828f50542dc8a543f5473d13ce8707a` | empreintes seulement (contenu par R-1580 et R-1757) |
| décisions | N-029 `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4` ; N-054 `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` ; N-055 `371879d5bd44f5fdd7f2ff2fe068065776000e0b2acc9118fa94b41f687340b6` ; N-056 `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` ; N-060 v3 `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` ; N-062 `63f426903e6d0774085a628ec019d2022d3107f6bd8e56eebbe75c0eeb0f3ccc` ; N-063 v2 `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` ; N-064 `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` ; N-065 `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` ; N-066 `21e83ed58c7498c65b7f9ae78613bc38301acdf0dd15a9890af13e6c0edbd351` | `docs/decisions/` | N-062 l. 1-40 ; N-063 v2 points 1-2 ; N-066 points 1-3 ; N-054 l. 33-39 ; N-060 v3 titres des points ; N-029 l. 20-30 ; les autres : sceaux |
| notes d'antériorité | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md` ; `…/note-anteriorite-popper-evaluator-v1.md` | `08a3738af518f59790936995cda714210c749f20e1891195343b2c3e2b132312` ; `d1ab704927b938aab631451b01ea2f197969f627dec32dcf63087bbc42ad0998` | empreintes seulement (non lues) |
| comparaison des verdicts d'A1-v4 | `…/verdict-a1-v4-v1/comparaison-verdicts-a1-v4-v1.md` | `4152fd2af18a38f8b2c86d6d715daceb1f6d464f7c8bc911371b5ad4e3579751` | empreinte seulement (non lue) |

**Non lus** (interdits ou hors besoin) : tout `lecture-sondes-t06.json` ; tout `diag/` et `runs/` de 7a ; la branche
`donnees/lecture-b-7a-quarantaine-v1` ; `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
`docs/notes/bras-attaque/` ; l'étiqueteur (items, clés, réponses, branche) ; `scripts/extraire_mesures_epreuve_t06_v1.py` ;
**aucun fichier de T0.7** (ses états sont pris dans le registre) ; le verdict provisoire d'A1-v4 ; les PDF de la littérature ;
les consoles de facturation ; la dernière passation.

## Choix

1. **Sources brutes d'abord** : chaque chiffre du socle est repris d'un verdict, d'un préenregistrement, d'un registre ou du
   texte envoyé, non du programme v18 ; le v18 sert de carte et de renvoi pour les réponses parlées en anglais.
2. **Cinq affirmations** : les cinq de la consigne (question, approche, rigueur, budget, repli) ; aucune fusionnée.
3. **Cinq questions** : une par affirmation, celle qui la fait tomber le plus sûrement ; la question de l'antériorité est
   rangée sous Q5 (avec l'organisme diffus), parce que le programme v18 § 3.5 y répond déjà.
4. **P3-bis cité au brouillon 10** (non scellé) : c'est la seule version disponible ; marqué [BROUILLON], avec ses phrases
   pour l'extérieur, gelées seulement au scellement.
5. **7b** : seule la table A est présentée comme lisible avant l'entretien, parce que les tables B et C et la règle
   « mots et coût » attendent T0.8 (R-2070, constat D11 ; texte scellé, plan, point 7 et concordance, point 2).
6. **Dépense** : aucun total neuf n'est proposé ; la dépense d'A1-v4 est signalée comme absente du registre (vérifié :
   aucune occurrence de GO-2026-11-02-22 ni de GO-2026-11-08-12 dans `registres/depenses.md`). Le « facteur ≈ 33 »
   (10 puissance 1,5227) et la « borne basse vraisemblablement au-dessus de 850 » (≈ 742 du v18 + 114) sont des calculs de
   ce rédacteur, déclarés non scellés.
7. **Sans acronymes** : noms de tâches dits en clair à la première mention ; « dollars » pour la monnaie ; heures « en temps
   universel coordonné » déclarées une fois. Restent des identifiants (GO-…, R-…, N-…, T6-1, PB-1, W2) et des noms propres
   (cartes, Open Science Framework, POPPER, HELIOS).
8. **Aucune valeur de sonde de 7a** ; de 7a ne sont cités que son statut (exploratoire, finie, instance détruite), une
   phrase de son ordre et sa dépense estimée (≈ 17,6, `registres/depenses.md` l. 413).

## Manques (repris au § 6 du socle)

Dépense d'A1-v4 hors registre ; aucun total ni facture ; dépôt chez le tiers privé et non gelé, rien de scellé depuis le
5 novembre déposé ; préenregistrement de T0.8 inexistant ; T0.7, P3-bis, phrases des concepts et J-C non scellés ; aucune
réexécution par un tiers, contenu de la copie publique non vérifié ; T0.3 sans verdict d'un lecteur neuf ; borne du
31 janvier relayée ; date de l'entretien non confirmée ; pages de la littérature non revérifiées.

## Écarts et gestes à déclarer

1. Aucune recherche récursive sur un dossier qui contient un chemin interdit ; les outils de recherche du harnais (recherche
   et motifs récursifs) n'ont pas été utilisés ; `git grep` seulement sur des fichiers nommés ; `ls` non récursif de
   `docs/verdicts/`, `prereg/`, `livrables/`, `docs/decisions/`, `brouillons/entretien-taif-v3/`,
   `docs/sources/candidature-taif-2026-10-07/`, `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/`.
2. `git ls-files -- prereg brouillons docs/procedures`, filtré aussitôt par motif (T0.8, G1, papier C) : noms seulement,
   aucun contenu ; aucun nom interdit sorti.
3. Une commande `git grep -l "6b51dbf5" -- registres/decisions.md brouillons/entretien-taif-v3` a parcouru mécaniquement ce
   dossier, qui contient `consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md` (fichier non listé parmi les interdits ;
   aucune ligne affichée ; trois noms de fichiers de contre-lecture rendus). Déclaré par prudence.
4. Aucun appel externe, aucune dépense, aucune écriture git, aucune commande d'environnement (`env`, `printenv`, `set`,
   `export -p`, `/proc/*/environ`), aucune valeur de clé. Aucun refus de permission ni de classifieur rencontré.
5. J'ai lu P3-bis brouillon 10 et aucun fichier de T0.7 ; je n'ai été ni lecteur de 7a, ni auteur d'une pièce citée. La mère
   jugera si ce rôle m'exclut d'un rôle de lecteur de P3-bis.
6. La suite d'essais n'a pas été lancée (interdit 5).

Fin de l'écriture : heure relevée au scellement (réponse à la mère).
