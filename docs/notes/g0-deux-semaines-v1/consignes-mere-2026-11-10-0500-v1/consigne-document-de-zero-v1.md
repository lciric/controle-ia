# Consigne : le programme expliqué depuis zéro, en PDF — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026 (heure au registre, R-2120 et suivant), sur le mot de Lazar (R-2120, message 2) : « pour le pdf, je veux que tu detailles tout comme si tu t'adressais a un lecteur qui ne connait rien du programme, en repartant de zero, en precisant les hypotheses, les lemmes theormes etc, les predictions, bref imagine que je ne connaisse RIEN du programme et de ce qui a ete fait. Je souhaite une version plus approfondie de cette tâche, pas une version plus longue. »

Destinataire : un **rédacteur neuf**, qui n'a écrit ni le programme, ni ses décisions, ni le rapport court du jour. Sa sortie sera vérifiée par deux lecteurs neufs qu'il ne connaît pas : un contre-lecteur qui confronte chaque affirmation à sa source, et un lecteur naïf qui ne lira que le PDF et devra restituer le programme.

## 1. Le lecteur visé, et ce que « approfondi, pas plus long » veut dire

- **Lecteur** : une personne intelligente, de formation scientifique, qui n'a **jamais** entendu parler du programme, ni du contrôle des agents d'intelligence artificielle, ni de nos noms de tâches. Elle lit en français. Elle doit pouvoir, après lecture, expliquer à un tiers : le problème, le pari, sa forme mathématique, chaque hypothèse et ce qui la réfuterait, ce qui a été fait, ce qui reste, et ce qu'on peut dire à un financeur.
- **Approfondi** : chaque objet est donné sous sa forme **exacte et actuelle** (énoncé, hypothèses, prédiction chiffrée et signe, seuil, ce qui réfute, statut, pièce), précédée d'une phrase en langage courant. Rien n'est résumé au point de ne plus être vérifiable.
- **Pas plus long** : aucune phrase de remplissage, aucune redite, aucun historique de versions, aucun nom de session, aucune liste de brouillons. Cible : **16 à 20 pages A4** dans la mise en page fournie. Si une section dépasse son budget, coupe ce qui n'aide pas le lecteur visé.

## 2. Règles d'écriture

1. **Aucun acronyme, aucun sigle, aucun nom de code sans définition.** À la première apparition, le nom en clair, puis l'étiquette du registre entre parenthèses si elle sert à retrouver la pièce : « la porte de sortie de la phase des instruments (G0 dans les registres) ». Ensuite, le nom en clair seulement. Les termes anglais du domaine sont traduits et le terme anglais donné une fois entre parenthèses.
2. **Un seul exemple fil rouge**, repris dans tout le document : l'agent qui rédige des propositions d'expériences et gonfle discrètement leur coût (l'environnement du programme, § 6 du programme ; le saboteur de P3).
3. **Trois statuts, toujours dits** : *démontré* (preuve mathématique écrite), *simulé* (vérifié sur données synthétiques), *mesuré* (résultat scellé sur un vrai modèle), *parié* (hypothèse non encore testée), *exploratoire* (ne décide rien). Ne jamais écrire un pari comme un fait. Si le statut d'un énoncé mathématique n'est pas clair dans les sources (lemme « candidat », preuve complète ou non), le dire tel quel.
4. **Chaque formule est suivie de sa lecture en une phrase.** Les symboles sont définis là où ils apparaissent.
5. **Chaque chiffre vient d'une pièce**, citée par chemin et empreinte dans le registre des affirmations (§ 5). Aucun chiffre de l'état de l'art sans vérification sur sa source, page citée (règle R7) : à défaut, cite le travail sans chiffre.
6. Phrases courtes. Un tableau quand on compare, une liste quand on énumère, de la prose quand on explique. Tutoiement de Lazar seulement dans la section « ce qui dépend de toi » ; ailleurs, le document parle à un lecteur quelconque.
7. Exactitude d'abord : là où une pièce manque, où deux textes se contredisent, où un énoncé a changé par une décision, écris-le. Les décisions de `docs/decisions/` priment sur le texte du programme v2 qu'elles corrigent : donne l'énoncé **en vigueur** et dis en une ligne ce qui a changé.

## 3. Plan imposé (budgets indicatifs en pages)

0. **Page 1 : le document en une page** (1). Le problème, le pari, où on en est, ce que le lecteur trouvera, les statuts.
1. **Le problème, depuis zéro** (1,5). Ce qu'est un agent ; ce qu'est le contrôle (surveiller un agent dont on ne peut pas garantir les intentions) ; ce qu'est un surveillant ; lire les sorties (boîte noire) ou lire aussi l'activité interne (boîte blanche) ; ce qu'est une activation, une sonde ; l'exemple fil rouge ; pourquoi la surveillance action par action échoue sur le sabotage diffus.
2. **L'idée, et sa forme mathématique** (2,5). Le cadre formel (jeu de contrôle, budget de sabotage, sécurité, utilité, score par action, agrégateurs) ; le **lemme d'additivité** avec ses hypothèses et son énoncé en vigueur (programme § 3 et § 4, note mathématique v3, décisions N-003 et N-004) ; le **théorème négatif** ; l'hypothèse empirique pivot ; ce que la simulation a vérifié (31 prédictions, avec sa réserve). **Un exemple chiffré, calculé par un script que tu écris** (formule fermée ou simulation à graines dérivées par `numpy.random.SeedSequence`), présenté comme une illustration et non comme un résultat : (a) un petit déplacement par action, invisible action par action au seuil de 1 % de fausses alertes, devient visible une fois accumulé ; (b) un dommage porté par la seule corrélation, à loi marginale préservée, reste invisible à toute somme. Dire ce que le test du programme (toujours valide, séquentiel) paie par rapport à un test à horizon fixe.
3. **Les hypothèses, une par une** (4). Les trois papiers (le temps, l'instrument, l'essaim). Pour chaque hypothèse en vigueur (H1 avec H1a et H1b, H2, lemme, théorème, H6, transposition, H8, H9 ; HC1 à HC6 avec HC2b ; H3, H4′, H5, H7) : nom en clair ; énoncé courant ; énoncé précis ; prédiction (chiffre, signe) si elle est préenregistrée, sinon « pas encore préenregistrée » ; ce qui la réfuterait ; probabilité d'originalité que le programme lui donnait ; ce qui est revendiqué et ce qui est déjà occupé par d'autres ; statut du jour. Format de fiche régulier, dense.
4. **Les instruments** (2,5). L'environnement ; les saboteurs d'épreuve (instruit, distillé à dose réglable, à budget) et la prédiction de validité qui les distingue ; les sondes (familles, agrégation par maximum ou attention et pourquoi jamais la moyenne, plancher aléatoire apparié) ; les surveillants de référence ; les invariants de protocole ; la vérité du dommage ; la méthode (préenregistrement scellé, contre-lecture, témoins, verdict par un lecteur neuf), dite en clair.
5. **Les portes** (1). Porte des instruments et ses huit critères ; porte décisive et son critère en vigueur (N-007, N-008, N-054, N-055, N-056, N-062, N-063 v2) ; les autres portes ; les bascules écrites d'avance.
6. **Le bras d'attaque et l'organisme d'idéation** (1,5). Ce qu'ils sont, pourquoi ils existent, leurs cloisons, leur place dans les trois papiers, l'objectif ultime (N-044, N-045 v2), le juge statistique et son attaque (N-064, N-065), leur état. **Bras d'attaque : au seul niveau des décisions ; son état est « monté, jamais lancé ».**
7. **Ce qui a été fait, dans l'ordre** (2,5). Chaque résultat scellé avec son chiffre, sa portée et ses réserves, négatifs compris ; les erreurs et incidents déclarés ; ce qui est exploratoire et ne décide rien.
8. **Les expériences préenregistrées en attente, et leurs prédictions** (1,5). La course de confirmation des saboteurs (texte scellé), le témoin positif planté, les sondes : hypothèse, prédictions chiffrées, critère, issue écrite d'avance.
9. **Ce qui reste, le calendrier, et ce qu'on peut dire à un financeur** (1,5). Chemin critique daté ; ce qui ne sera pas prêt ; les cinq affirmations et leurs preuves (reprendre le socle, sans le recopier) ; ce qu'on ne dit pas ; ce qui dépend de Lazar.
10. **Glossaire** (nom en clair, définition en une ligne, étiquette du registre) **et sources** (1).

## 4. Sources : partir des textes qui font foi, pas des résumés

Vérifie l'empreinte de chaque pièce que tu cites. À lire :

- **Le fond** : `docs/programme-controle-ia-v2.md` (`2fd63bad…`) ; `docs/brief-claude-code-programme-complet-v2.md` (portes, critères) ; `docs/notes/note-mathematique-lemme-theoreme-v3.md` ; **toutes** les décisions de `docs/decisions/decision-*.md` que nomme le fichier `CLAUDE.md` à la racine (elles fixent la lecture du programme) ; `docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md`.
- **Les résultats** : `docs/notes/resultats-T0.3-v1.md` ; tout `docs/verdicts/` ; le verdict officiel de l'attaque du juge `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` (`e6e2f170…`), **dans sa lecture bornée gelée, rien au-delà**.
- **Les préenregistrements** : `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`, scellé) ; `brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md` (`9038a015…`, brouillon) ; `brouillons/T0.7-sondes-v0-v1-brouillon20.md` (brouillon ; le lire t'exclut ensuite de tout rôle de lecteur de P3-bis : déclare-le).
- **L'état de l'art** : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` et le niveau 1 ; N-064 pour les citations obligatoires de l'organisme.
- **L'état du jour et l'entretien** : `brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md` (`b8a97629…`, non contre-lu : vérifie ce que tu en reprends) ; `docs/notes/rapports-directeur/rapport-programme-complet-entretien-2026-11-10-v3.html` (`7d610de1…` : le rapport court du jour, pour l'état, le vocabulaire en clair et la mise en page) ; `brouillons/entretien-taif-v3/consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md` ; `registres/etat.md` (les 30 premières lignes et les sections « Phase en cours » à « Derniers verdicts de porte ») ; `registres/go.md` (lignes du 10 novembre) ; `registres/scellements-v1.md` ; `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt`.

## 5. Sorties

Trois fichiers, noms neufs, scellés (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichiers>`), et rien d'autre :

1. `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v1.html` : le document. **Reprends tel quel le bloc `<style>` du rapport court v3** et ses classes (`box`, `chip ok|run|todo|hold|you`, `map`, `node`, `two`, `ref`, `small`, tableaux avec `<thead>`), ajoute ce qu'il te faut (fiches d'hypothèses, formules en HTML simple, sans bibliothèque externe ni image distante). Typographie : écris avec des espaces ordinaires ; le script de construction pose les insécables.
2. `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v1-registre-affirmations.md` : une ligne par chiffre ou fait vérifiable du document (identifiant, phrase, valeur, chemin de la source, empreinte, ligne ou section). Le contre-lecteur s'en servira.
3. `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v1-journal.md` : sources lues avec empreintes, choix, manques, contradictions trouvées, le script de l'exemple chiffré (ou son chemin) et sa sortie.

Tu peux construire le PDF pour contrôler ta mise en page, dans un dossier temporaire à toi, sans le déposer : `.venv/bin/python -I docs/notes/rapports-directeur/construire-rapport-pdf-v1.py <source.html> <sortie.pdf> <dossier temporaire> "<pied de page>"`, puis `pdfinfo` et `pdftoppm` pour compter et regarder les pages. Le script de l'exemple chiffré va dans `docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v1.py` (scellé, quatrième fichier admis).

## 6. Interdits

Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), en entier, règle 9 comprise. En particulier : jamais `diag/*/lecture-sondes-t06.json`, ni la lecture B de la course 7a, ni sa branche de quarantaine, ni aucun `diag/` ou `runs/` de 7a ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; jamais l'étiqueteur ; jamais `scripts/extraire_mesures_epreuve_t06_v1.py`. Aucun chiffre de la course exploratoire 7a autre que sa dépense. Aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé (ni `env`, ni `printenv`, ni `set` sans argument, ni `export -p`, ni `/proc/*/environ`). Aucune recherche récursive qui traverse les chemins interdits : `git grep` avec exclusions. Si un contrôle de permissions ou un classifieur refuse une action, arrête-toi sur ce point et rapporte-le tel quel.

## 7. Réponse à la mère

Courte : chemins et empreintes des sorties ; nombre de pages ; les contradictions et manques trouvés dans les sources ; ce que tu n'as pas pu vérifier ; tout refus.
