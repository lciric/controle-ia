# Consigne : lot 3, étape 1 — écrire la consigne v1 du jeu de phrases des concepts de T0.7, accordée au module — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), autonomie de 12 heures (R-2088). Destinataire : un **rédacteur neuf** (Opus), qui n'a écrit ni T0.7, ni son module, ni ses jeux, ni la consigne brouillon 1 des concepts, ni leurs contre-lectures. Exclu ensuite de tout rôle de lecteur de P3-bis.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise**. Nommément : jamais `diag/*/lecture-sondes-t06.json` ni `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; jamais la lecture B ni `donnees/lecture-b-7a-quarantaine-v1` ; aucun `diag/`, `runs/` ni donnée de 7a, ni `essai/t06-explo-v3` ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucun texte d'action de P3. Aucun appel externe, aucune dépense, aucune écriture git.

## À lire

- Consigne brouillon 1 : `brouillons/T0.7-concepts-sans-lien-consigne-v1-brouillon1.md` (`acc7bdfb…`).
- Inventaire des jeux, sections 4.2 (format exigé par le module : `lire_phrases_concepts`, `Extracteur.phrase`, commit `8dc1cb09`) et 5, lot 3 : `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md` (`c9910a54…`) ; le module par `git -C /home/user/controle-ia-travail show 8dc1cb09:src/controle_ia/t07/sondes_neuves_v1.py` (et ce qu'il importe pour ces fonctions).
- Brouillon 20 de T0.7 (`brouillons/T0.7-sondes-v0-v1-brouillon20.md`, `9ef671ac…`) : T7-P9 (panel de concepts sans lien), sections qui citent la consigne ; décision P-013 (quatre concepts : chats, météo, sports, géographie), R-2101 (D-4 : format \`message_utilisateur\`, proposé à Lazar, défaut sous 48 heures).
- Consigne v3 des jeux synthétiques (`docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, `d9de50a6…`) : pour la forme d'une consigne scellée de ce programme.

## Mandat

Écrire `docs/procedures/consigne-concepts-sans-lien-T0.7-v1.md` (nom neuf, R12), tirée du brouillon 1 et accordée au module : un seul fichier de sortie `donnees/t07-concepts-v1/phrases-concepts-v1.jsonl` ; première ligne `format_lecture` (valeur `message_utilisateur`, D-4, réversible si Lazar choisit autrement avant le scellement de la consigne) ; quatre concepts ; 64 paires par concept ; `indice` entier unique de 1 à 64 ; phrases d'au plus 40 jetons (borne dure du module : 128) ; longueurs appariées à 15 % près en jetons du tokeniseur réel ; **annexe A** (mots interdits) et **annexe B** (lexique de chaque concept) écrites ; section de la consigne d'écriture (en anglais, deux paires d'exemple par concept, exclues du jeu) ; contrôles que le script de vérification fera (liste fermée, chacun avec son artefact) ; règles de renvoi (un renvoi par paire en défaut, retrait au second) ; contre-vérification à l'aveugle (10 % des paires de chaque concept, tirage par `SeedSequence` à entropie neuve consignée ; questions fermées ; aucun fichier de P3-bis donné au lecteur) ; provenance. **Aucune phrase du jeu n'est écrite par toi.** Puis un journal court (sources lues, choix, points ouverts).

## Sorties

La consigne et son journal (`docs/procedures/consigne-concepts-sans-lien-T0.7-v1-journal.md`), **scellés** (le scellement définitif de la consigne suivra sa contre-lecture R2 : le sceau de ta remise sert de référence). Réponse courte : chemins, empreintes, points ouverts.
