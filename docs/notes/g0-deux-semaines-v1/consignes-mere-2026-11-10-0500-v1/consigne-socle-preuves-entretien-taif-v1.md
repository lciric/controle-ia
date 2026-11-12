# Consigne : socle de preuves pour l'entretien avec le Transformative AI Fund — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`), sur le « go » de Lazar (R-2115). Destinataire : un **rédacteur neuf** (Opus), qui n'a écrit ni le programme d'entretien (versions 1 à 18), ni ses contre-lectures. Langue : français, **sans acronymes** (les noms de tâches comme T0.6 ou G0 sont dits en clair à leur première mention : « la course des organismes saboteurs (T0.6) », « la porte de sortie de la phase 0 (G0) »). Chaque chiffre renvoie à un chemin et une empreinte (règles R6, R7) ; aucun chiffre de l'état de l'art sans vérification sur sa source.

## Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, **règle 9 comprise** : jamais `diag/*/lecture-sondes-t06.json` ni la lecture B de 7a ni sa branche de quarantaine ; aucun `diag/`, `runs/` ni donnée de 7a ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py`. Aucun appel externe, aucune dépense, aucune écriture git ; aucune valeur de clé.

## La demande, telle que Lazar l'a validée (R-2115)

Pour l'entretien avec le Transformative AI Fund (vers le 22 novembre, date à confirmer ; demande de 58 630 dollars), établir à partir des **sources brutes** — texte de candidature envoyé (`docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` et son budget), verdicts scellés (`docs/verdicts/`, dossiers de verdict), registres (`registres/decisions.md`, `registres/go.md`, `registres/depenses.md`, `registres/scellements-v1.md`), préenregistrements scellés (`prereg/`) — et non des résumés :

1. les **trois à cinq affirmations** que l'entretien doit soutenir (la question compte ; l'approche peut marcher ; l'équipe exécute avec rigueur ; le budget est tenu ; le plan de repli existe), et pour chacune : le résultat qui la soutiendrait, celui qui la réfuterait, la pièce qui la prouve (chemin, empreinte) et le chiffre exact avec sa source ;
2. la **démonstration minimale crédible** atteignable **scellée et lue avant le jour J** : témoin positif planté (P3-bis), organisme à dose croissante (course de confirmation 7b), résultats nuls avec leur puissance (P3), juge de l'organisme d'idéation attaqué (verdict officiel d'A1-v4, R-2111) ; pour chacune : critère gelé, témoins positif et négatif, puissance, issue écrite d'avance en cas d'échec, date réaliste, et **ce qu'on dira si elle n'est pas prête** ;
3. ce qu'un **tiers** peut déjà vérifier, et ce qu'il faut rendre vérifiable avant l'entretien (dépôt public gelé des préenregistrements chez un tiers, réexécution indépendante, relevés de facturation des fournisseurs, page publique d'A1-v4) ;
4. le **chemin critique jour par jour** jusqu'à l'entretien, en trois colonnes : fini, en cours, plan (calendrier réel : création de 7b au plus tard le 15 sous la chaîne v13, bascule éventuelle sur v14 décidée le 13 à 12:00 UTC ; P3-bis créé au plus tard le 18, rendez-vous le 20 à 12:00 UTC ; étape A de T0.7 en variante B, GO-2026-11-10-06 ; jeux de T0.7 en cours) ;
5. les **cinq questions** qui peuvent faire tomber le dossier, chacune avec sa réponse ou son aveu préparé.

## À lire en plus

Programme d'entretien v18 (`brouillons/entretien-taif-v3/programme-entretien-taif-v18.md`, `24e…` à vérifier ; ses §§ 2 et 3) et sa contre-lecture v17 ; verdict officiel d'A1-v4 (`docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md`, `e6e2f170…`, et sa **lecture bornée gelée** : ne rien dire au-delà) ; registre R-2051 à R-2115 (état du jour). **Exactitude d'abord** : là où une pièce manque ou un chiffre n'est pas vérifiable, l'écrire comme manque.

## Sortie

`brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md` (nom neuf), scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`), et un journal court `…-journal.md` (sources lues avec empreintes, choix, manques), scellé. Aucune autre écriture. Réponse courte : chemins, empreintes, les cinq affirmations en une ligne chacune, les manques.
