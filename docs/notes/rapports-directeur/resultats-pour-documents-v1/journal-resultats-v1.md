# Journal — sections « Résultats » pour les deux documents explicatifs — v1

- **Rédacteur** : sous-agent neuf (Claude Opus 5.5, `claude-opus-5-5`) de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Je n'ai écrit aucune des pièces lues. Je n'ai lu aucun des deux documents explicatifs, ni aucun document d'une autre session.
- **Heures** (relevées par `date -u`, 10 novembre 2026) :
  - début à 10:26:40 ;
  - dossier de sortie créé à 10:36:33 ;
  - empreintes des pièces relevées à 10:41:25 ;
  - journal écrit vers 10:46 ;
  - scellement ensuite, à l'heure donnée par la commande.
- **Interdits communs v2** : lus en premier, en entier, règle 9 comprise. Fichier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, sha256 `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, égale à la consigne.
- **Garanties** :
  - aucun appel externe, aucune dépense, aucune écriture git ;
  - aucune valeur de clé lue ;
  - aucune commande `env`, `printenv`, `set` ni `export -p`.

## 1. Fichiers écrits (dossier `docs/notes/rapports-directeur/resultats-pour-documents-v1/`)

- `section-resultats-programme-v1.html` : section A, renvois [A0] à [A54].
- `section-resultats-organisme-v1.html` : section B, renvois [B1] à [B45].
- `registre-affirmations-resultats-v1.md` : la table des pièces avec leurs empreintes, puis une ligne par renvoi (pièce et ligne, ou champ).
- `journal-resultats-v1.md` : ce fichier.

Les quatre fichiers sont scellés par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller`.

## 2. Sources lues, avec leurs empreintes

Les empreintes ont été recalculées à 10:41 UTC ; la table complète est dans le registre, section 1.

Sources nommées par la consigne :

| source | sha256 |
|---|---|
| verdict de T0.4 v3 (critère 1 de G0) | `63444faa…` |
| résultats de T0.3 v1 | `9ab618ed…` |
| verdict de P3 v2 | `05e896da…` |
| verdict de l'audit de fuite | `320463e6…` |
| verdict de l'étiqueteur, phase 1 | `9f7830b9…` |
| texte scellé de T0.6 | `ef31feff…`, égal à son compagnon ; scellé au commit `935262b1` |
| P3-bis, brouillon 10 | `9038a015…` |
| verdict de la troisième course d'A1-v3 | `7dade9ef…` |
| verdict officiel d'A1-v4 | `e6e2f170…`, égal au préfixe donné |
| verdict de validation du nul v9 | `1407e460…` |
| journal de l'essai à blanc | `627f7a4c…`, égal au préfixe donné |
| note d'antériorité Co-Scientist | `08a3738a…` |
| note d'antériorité POPPER et E-valuator | `d1ab7049…` |

L'épreuve du monde gradué a été retrouvée par `git grep -l -E "e025f108|dc0bb41a"` avec les exclusions de la règle 9. Exclus : `docs/notes/bras-attaque`, `scripts/extraire_mesures_epreuve_t06_v1.py`, `diag`, `runs`, `donnees` et `docs/notes/rapports-directeur`. Pièces trouvées :

- le texte court scellé `epreuve-w2g-dose-v2-v1.md` (`e025f108…`, égal à son compagnon) ;
- la lecture scellée `epreuve-w2g-dose-v1-rejeu-v2-lecture-v1.json` (`dc0bb41a…`, égale à son compagnon) ;
- la console de cette lecture (`d9aa3cb7…`).

Pièces lues en plus, pour définir les objets ou situer une affirmation :

- `prereg/P3-premier-test-i-a-v1.md` : l. 120-140 et l. 228-236 ;
- `prereg/audit-fuite-r1-v4-v1.md` : l. 40-75 ;
- `prereg/preenregistrement-epreuve-etiqueteur-v1.md` : sommaire et section « Hypothèse » ;
- `docs/decisions/decision-N-060-v3.md` : en entier ;
- T0.6 : en-tête l. 1-40 et l. 300-600 ;
- P3-bis, brouillon 10 : l. 452-562 et l. 987-1020 ;
- `brouillons/T0.7-sondes-v0-v1-brouillon20.md` (`9ef671ac…`) : l. 826-881 ;
- brief v2 : l. 186-202 ;
- programme v2 : l. 50-100 ;
- décisions N-055 (recherche de « H1 »), N-056 (l. 1-56), N-064 (en entier) et N-065 (l. 1-40) ;
- `docs/decisions/proposition-P-006-T0.5-v1.md` : l. 1-45 ;
- verdict des notations de T0.5 : recherche de termes ;
- texte scellé d'A1-v4 (`d306a8fa…`) : l. 191-224 et l. 374-377 ;
- épreuve W2g : texte, l. 1-60 et l. 201-214 ; lecture, champs `lambda_etoile`, `a_la_limite`, `p10`, `evaluations_impossibles`, et `par_dose` aux doses 0 et 0,4 ; console entière ;
- `registres/decisions.md` : R-212, R-1779, R-1883, R-1949, R-2032 (début), R-2044, R-2059, R-2116, R-2126, R-2128, R-2130, R-2133, R-2150 à R-2158 (débuts de ligne), et des débuts de R-2137, R-2138 et R-2141 vus par une recherche de nom de branche ;
- `registres/etat.md` : l. 1-40, tronquées, et l. 414 ;
- page 1 de quatre sources, pour les titres :
  - le PDF de POPPER, actes PMLR 267 ;
  - le PDF de 1506.02629 ;
  - le PDF de 1502.04585 ;
  - l'extraction texte de l'article de Nature sur Co-Scientist.

## 3. Ce qui a été vu sans être repris (déclaré)

- **Course 7a.** Aucune valeur de sonde de 7a n'a été vue. J'ai vu seulement :
  - des mentions de 7a dans T0.6 : la fraction de garde 0,05, un avertissement de mémoire, les catégories des grandeurs de coût retirées, sans valeur ;
  - le coût de 7a dans `registres/etat.md`.

  Rien de cela n'est repris.
- **Chiffres exploratoires.** Le texte de l'épreuve W2g contient des chiffres exploratoires (graine 20261108) et des durées d'essai. Je les ai vus ; je n'en reprends aucun. Seule la lecture scellée `dc0bb41a…` sert.
- **Textes de consignes.** Je n'ai ouvert ni les textes d'actions de P3 ni `prereg/P3-consignes-v1.md`. Deux textes lus en citent des fragments : le préenregistrement de l'audit de fuite cite une phrase de la note privée du saboteur de P3, et le brouillon 10 de P3-bis cite la phrase de persona du jeu générique. Aucune de ces phrases n'est recopiée.
- **Listings de noms.** `ls docs/notes/rapports-directeur/` m'a montré des noms de fichiers d'autres sessions ; je n'en ai ouvert aucun. `git branch -a --list` m'a montré des noms de branches ; aucune n'a été ouverte ni lue.

## 4. Choix de rédaction

- **Nom du modèle.** Il n'est pas écrit : le verdict de T0.4 (l. 454) dit qu'il a été retiré « (règle du dépôt) ». J'écris « modèle de langue ouvert de 8 milliards de paramètres ». Si la mère veut le nom, il est à P3P, l. 122.
- **« Facteur de l'ordre de 30 ».** C'est mon calcul : 10^1,5227 ≈ 33,3, arrondi vers le bas. Il est marqué comme tel au registre, [A17].
- **« Grille simplifiée ».** L'expression ne figure dans aucun fichier : `git grep` avec exclusions ne trouve rien. Je l'ai lue comme la « rubrique simplifiée » des juges locaux (N-022, R-212, verdict des notations de T0.5), et je le dis dans le texte. Si la question visait autre chose, la réponse de la section A, point 4 (ii), est à revoir.
- **Lectures bornées.** Elles sont recopiées dans leur sens, sans « validé ».
- **Recettes.** Aucune n'est donnée : ni consigne servie au proposeur, ni loi promue, ni réponse du proposeur. La loi fausse plantée de l'essai à blanc est nommée sans son contenu.
- **Citations de N-064.** Les références viennent des notes d'antériorité : auteurs, lieux, pages et identifiants. Les titres exacts de Dwork et al., de Blum et Hardt et de POPPER, ainsi que le premier auteur de Co-Scientist, ont été relus sur la page 1 des PDF empreintés. Les notes donnent ces titres en partie, ou seulement par le nom de fichier. Le registre le dit, [B42] à [B44].

## 5. Manques

1. **T0.3.** Le verdict formel du lecteur neuf est sur une autre branche (R-2126) et n'est pas fusionné. Il n'est pas lu ; la section A cite seulement la note de résultats et le statut annoncé.
2. **P3-bis.** Le brouillon 11 est en cours. Les hypothèses et prédictions citées sont celles du brouillon 10, non scellé ; elles peuvent changer avant le scellement.
3. **T0.7.** Le brouillon 21 est en rédaction. Le test de validité est cité d'après le brouillon 20.
4. **T0.8.** Le préenregistrement n'existe pas encore ; le brouillon 1 est en rédaction (`registres/etat.md`, l. 3). Rien n'est dit de son contenu.
5. **Verdict d'A1.** Le verdict de la première attaque n'est pas lu. Son issue est citée telle que la donne le texte scellé d'A1-v4, l. 193.
6. **Date de l'entretien.** Elle est visée, non confirmée avec le fonds (R-2130).
7. **Lectures avant l'entretien.** Qu'une lecture de sonde sur 7b se fasse avant le 27 novembre n'est établi par aucune pièce. La section A l'écrit « pas encore établi ».
8. **Longueur.** La section A compte environ 2 100 mots, et la section B environ 1 950. Selon la mise en page, chacune peut dépasser de peu trois pages imprimées.
9. **Registre vivant.** `registres/decisions.md` a changé pendant mon travail : la tête est passée à `a2abc8e3`, R-2150 à R-2158 ont été ajoutés. J'ai revérifié les numéros de ligne des entrées citées : ils sont inchangés.

## 6. Refus

Aucun. Aucun contrôle de permissions ni classifieur n'a refusé d'action.
