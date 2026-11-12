# Dossier de l'entretien du 27 novembre 2026 (Transformative AI Fund) — v1

Point d'entrée unique, déposé le 10 novembre 2026 à 11:00 UTC (heure relevée par `date -u`) par la session mère, sur le mot de Lazar : « depose bien sur github tout le prog pour l'entretien, les questions a traiter en priorite, idealement etc ». Date de l'entretien : visée le 27, à confirmer avec le fonds (R-2130). Ce dossier ne contient aucun résultat de sonde : aucune sonde n'a encore battu un surveillant de référence, et l'existence d'une trace interne du sabotage n'est pas établie.

## 1. À lire, dans cet ordre

| # | Pièce | Pour quoi | Empreinte (début) |
|---|---|---|---|
| 1 | [Le programme expliqué depuis zéro, v2 (PDF, 20 pages)](../programme-depuis-zero-2026-11-10-v2.pdf) — [version HTML](../programme-depuis-zero-2026-11-10-v2.html) | Hypothèses, lemme, théorème, prédictions, ce qui est fait et ce qui reste, pour un lecteur qui ne sait rien | `a11b7bcc` / `d6d5d448` |
| 2 | [Rapport court du programme complet, v3 (PDF)](../rapport-programme-complet-entretien-2026-11-10-v3.pdf) | Vue d'ensemble : programme, bras d'attaque, organisme d'idéation, ce qu'il faut produire | `7d7b33e6` |
| 3 | [Programme de l'entretien, v18](../../../../brouillons/entretien-taif-v3/programme-entretien-taif-v18.md) et [sa version condensée en 30 minutes, v3](../../../../brouillons/entretien-taif-v3/programme-entretien-condense-30min-v3.md) | Déroulé, réponses préparées aux questions du jury | `e58ccfed` / `c96243f4` |
| 4 | [Socle de preuves, v2](../../../../brouillons/entretien-taif-v3/socle-preuves-entretien-v2.md) | Chaque affirmation dite au jury, avec sa pièce (non encore contre-lu) | `3f078bca` |
| 5 | [Ce qui manque pour « l'approche peut marcher »](../ce-qui-manque-approche-peut-marcher-v1.md) | Les onze manques, avec date et état | `edb0bf03` |
| 6 | [Les prémisses de la trace interne](../premisses-trace-interne-v1.md) et [la note sur l'artefact d'adaptateur](../premisses-trace-interne-v1-point-2a.md) | Échelle des affirmations, arbre des prémisses, ce qu'on dit au jury dans chaque issue (§ 4) | `2638558e` / `2db916aa` |
| 7 | [Principes, état et goulots de l'organisme d'idéation (9 novembre)](../rapport-principes-etat-goulots-entretien-organisme-2026-11-09-v1.md) | Le second terrain : le juge de l'organisme comme surveillant | `22263fce` |

Les deux documents écrits par la session du bras d'attaque (programme v4, organisme v3), complétés de nos sections de résultats ([`resultats-pour-documents-v1/`](../resultats-pour-documents-v1/)), sont assemblés par la session-dépôt ; ils rejoindront ce dossier à leur versement sur `main`.

## 2. Les questions à traiter en priorité

L'échelle va de l'affirmation la plus faible à la plus forte ; chaque barreau a son expérience préenregistrée, dont l'issue est écrite d'avance dans les deux sens. Priorités de Lazar (10 novembre) : **5 d'abord**, puis 4, 7, 8 ; 6 ajoutée le 10 (R-2175).

| Barreau | Question | Ce qui la traite | Décision du 10 novembre | Lisible vers |
|---|---|---|---|---|
| 1 | La chaîne de mesure voit-elle un signal planté, et se tait-elle sur son jumeau honnête ? | Témoin positif (P3-bis), course créée au plus tard le 18 | — | 20 novembre au plus tard |
| 2 | Existe-t-il un saboteur sans consigne dont le dommage croît avec la dose ? | Course de confirmation 7b (texte scellé de T0.6), créée au plus tard le 15 | — | 16 au 18 |
| 3 | À ces doses, le texte seul échoue-t-il à repérer le sabotage ? | Base « mots et coût » (T0.8, base A), règle scellée **à part, avant la course 7b** | D-2 : oui | vers le 18 |
| 4 | À ces doses, une sonde entraînée ailleurs est-elle au-dessus du hasard ? | Texte des sondes T0.7, scellé avant le 13 à 12:00 UTC | — | 20 au 22, sans marge |
| **5** | **La sonde lit-elle le sabotage, et non la seule présence d'un adaptateur ?** | Texte court « validité adaptateur » (contraste dans la dose, tendance, différences en différences, relecture à texte constant) **et** témoin distillé honnête | D-1 : option (b), plafond 30 USD (GO-2026-11-10-07) | 21 au 23 |
| 6 | Accumuler sur l'épisode bat-il le score action par action ? | Texte court neuf, lu sur les scores déjà prévus, sans dépense nouvelle ; ne touche pas la porte G1 | demandé le 10 (R-2175) | avec la lecture des sondes |
| 7 | Notre chaîne reproduit-elle un résultat positif déjà publié ? | Nos sondes sur les activations publiées par les auteurs du banc NARCBench, au processeur | D-3 : oui, 0 USD | à fixer avec le code |
| 8 | Un sabotage vraiment diffus (chaque action dans la plage honnête) laisse-t-il une trace ? | Saboteur à budget, avec l'activité interne enregistrée | D-4 : go après code et devis (GO-2026-11-10-08, plafond 60 USD) | 18 au 19 pour l'objet ; sondes ensuite |

Contrôles de validité qui accompagnent : témoins de concepts (consigne v3, lot neuf en cours ; repli écrit sans eux), jeu d'entraînement « coût gonflé » (une dernière réécriture permise), puissance écrite avant lecture, preuve datée chez un tiers que chaque préenregistrement précède ses données (empreintes à rendre publiques et à geler).

## 3. Calendrier idéal jusqu'au 27

| Date | Étape |
|---|---|
| 12-13 nov. | Règle « mots et coût » scellée à part ; T0.7 scellé (avant le 13, 12:00 UTC) ; textes « validité adaptateur » et « accumulation » contre-lus et scellés avant l'étape B de T0.7 |
| ≤ 15 nov. | Course de confirmation 7b créée ; étape A des sondes sur son instance |
| 16-18 nov. | Verdict de la course (table A) ; issue de la règle « mots et coût » ; témoin positif créé au plus tard le 18 ; saboteur à budget |
| 20 nov. | Lecture du témoin positif (au plus tard, rendez-vous de 12:00 UTC) |
| 20-23 nov. | Lecture des sondes aux doses jugées ; contrôle de l'adaptateur ; accumulation |
| 24-26 nov. | Verdicts par lecteurs neufs, intégration dans les documents, répétition |
| 27 nov. | Entretien |

Aucune relance n'est possible dans ce calendrier : une étape qui glisse se dit au jury comme « non lue à temps », avec ce qui a été scellé.

## 4. Ce qu'on dira au jury, selon l'issue

Voir la section 4 des [prémisses](../premisses-trace-interne-v1.md) : une phrase pour l'issue positive, une pour l'issue nulle avec la puissance, une pour « non lu à temps ». Rien de plus fort que la pièce.

## 5. Encore ouvert

Confirmation de la date avec le fonds ; contre-lecture du socle de preuves v2 ; programme de l'entretien v19 (aligné sur la levée de la restriction de R-611, R-2146, et sur les trois questions de jury relevées par la session du bras d'attaque, R-2164) ; correction croisée des trois documents « depuis zéro » par le questionnaire commun.

Registres : décisions R-2116 à R-2175 de [`registres/decisions.md`](../../../../registres/decisions.md) ; GO dans [`registres/go.md`](../../../../registres/go.md).
