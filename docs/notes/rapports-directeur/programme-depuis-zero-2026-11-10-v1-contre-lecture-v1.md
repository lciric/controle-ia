# Contre-lecture — « Le programme expliqué depuis zéro », version 1 du 10 novembre 2026 — v1

- **Contre-lecteur** : sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, modèle déclaré par l'environnement Claude Fable 5.2 (`claude-fable-5-2`). Je n'ai écrit ni le document, ni sa consigne, ni aucune pièce qu'il cite. Je n'ai lu aucun autre document « depuis zéro ».
- **Heure** : fin de la rédaction à 2026-11-10 10:13:42 UTC (relevée par `date -u`).
- **Interdits communs v2** (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, vérifiée) tenus en entier, règle 9 comprise : aucun fichier ni aucune branche interdits ouverts ; recherches par `git grep` sur des fichiers nommés ; aucun appel externe, aucune dépense, aucune écriture git, aucune valeur de clé. **Aucun refus** d'un contrôle de permissions ni d'un classifieur.
- **Déclaration de rôle** : j'ai lu les sections « Hypothèse » et « Prédiction » du brouillon 20 de T0.7 et des passages du brouillon 10 de P3-bis ; je suis exclu de tout rôle de lecteur de P3-bis.

## Empreintes vérifiées avant lecture (toutes conformes)

| pièce | sha256 |
|---|---|
| `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v1.html` | `2c639ca3622600ed36427df7c62f07f62be351b4dc69f575499a0b3c9c29b487` |
| `…-v1.pdf (17 pages)` | `bec30fbc6c2b5eab1c556180e7722b4b0b9f4f51e274c7b90de16ec03b3729eb` |
| `…-v1-registre-affirmations.md` | `0b4de478057799c2edecddbacbe3d625c24679c688ba631e5d0db4c813035ed6` |
| `…-v1-journal.md` | `b69932b164f4f8231a4fb19787519bd842bee763e3c058025b9e92e8ebcb7867` |
| `docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v1.py` | `ee221d75738ae429dd57cc1475ac47a6d36da63f243eac2f9c9801a437e85976` |
| `consigne-document-de-zero-v1.md` | `d7a37a10511350f03472858c94a3552db07beb0ada261f9d4acdeb812952877a` |

Les 60 pièces sources citées au registre ont été rehachées : toutes égales aux empreintes du journal ; deux empreintes du registre sont fausses (constat 24).

## Verdict

1. **Publiable après corrections : trois bloquants, tous de formulation, aucun de fond.** La page 1 et le § 2.4 énoncent le théorème négatif dans la forme que la décision N-003 a écartée (« l'ordre ou la dépendance … une somme ne voit rien ») ; le § 2.3 donne L5 pour « simulé » alors qu'aucune des 31 prédictions de la simulation ne le porte.
2. **Registre des affirmations : 110 lignes relues contre leur source ; aucun chiffre du document n'est faux.** L'exemple chiffré se rejoue à l'identique (sortie égale ligne à ligne au journal et aux deux tables). Aucun chiffre exploratoire, aucun chiffre de l'état de l'art non vérifié ; rien n'est promis au-delà du témoin positif planté et de la table du coût ; le bras d'attaque reste au niveau des décisions, dans l'état dicté.
3. **Vingt et un constats à corriger et treize mineurs** : énoncés plus forts que leur source (cause du facteur 33, réfutation de H1, « n'est possible », « validé »), une illustration dont l'horizon vaut vingt fois l'épisode réel sans que ce soit dit, un état périmé (verdict de la simulation), des étiquettes qui se heurtent (H6-1 contre H6 ; bases (ii), (iii) contre saboteurs (ii), (iii)), des termes de registre non définis.

## Ce qui a été vérifié, dans l'ordre demandé

1. **Registre des affirmations (A01 à A110).** Chaque pièce ouverte, rehachée, la ligne ou la section lue. **Conformes, valeur et référence** : A01 à A05, A08 à A17, A19, A21 à A23, A25 à A57, A59 à A66, A68, A70 à A73, A75 à A77, A80 à A84, A86 à A88, A90 à A93, A95 à A98, A101 à A104, A106, A109, A110 (A73 : la confirmation du 28 octobre est R-600). **Conformes, avec une nuance de formulation portée aux constats** : A06 et A07 (constat 11), A85 (constat 17), A89 (constat 35), A94 (constat 18). **Valeur conforme, référence inexacte** (constat 24) : A24, A67, A74, A100 (empreinte de la candidature) ; A69, A79, A99, A108 (empreinte du registre des décisions) ; A74 (ligne) ; A58 (source incomplète). **Périmée** : A20 (constat 10). **Plus fortes que leur source** : la phrase portée par A18 (« test préenregistré », constat 9) ; A105 (« n'est possible », constat 15). **Dites non vérifiées par le rédacteur, vérifiées ici, conformes** : A78 (R-2127) et A107 (R-2130). **Non vérifiable** : aucune.
2. **Mathématiques.** Cadre (§ 2.1) : conforme au programme § 4 et à la note v3 § 1, sauf la lecture de « l'utilité » (constat 8). Processus e (§ 2.2) : formule égale à la note v3 § 2 ; hypothèses incomplètes (constat 25). Lemme : L1, L2, L3, L5 conformes à la note v3 § 3 et à N-004 ; L4 incomplet (constat 5) ; énoncé courant à borner (constat 4) ; statut de L5 faux (constat 3). Théorème : T1 à T4 et la classe K conformes à la note v3 § 4 et à N-003 ; les deux énoncés courants sont faux en classe K (constats 1 et 2). **Exemple chiffré** : script rejoué (`.venv/bin/python -I`, python 3.13.18, numpy 2.4.6, scipy 1.17.1), sortie **identique** au journal ; les deux tables, 0,32 %, 0,971, 0,591, 0,886, 8,9 %, 0,93 % et les « 21 points » (0,8867 − 0,6741) sont exacts ; le § 1 reprend juste la ligne m = 100. L'illustration est juste ; le rédacteur a eu raison de s'écarter de la consigne pour (b) (classe C, non K) et la mise en garde sur la classe K est écrite. Limites non dites : l'horizon et le décalage sont choisis (constat 7) ; « toute somme » (constat 6).
3. **Hypothèses.** Énoncés en vigueur conformes pour H1 (N-055, N-054, N-056), H2 (N-007), L et T (N-003, N-004, P-008), H6 (N-015, N-054), Tr, H8 (N-062, N-053), HC1 (N-005, N-013, N-023), HC2 et HC2b (N-013), HC3 à HC5 (N-013, N-006), HC6, H3, H4′, H5, H7, H9 (N-035). Probabilités d'originalité et révisions : conformes. Statuts : tous « parié » à juste titre, sauf le statut « simulé » de L5 (constat 3). Réfutations : celle de H1 est inexacte (constat 12), celle de H2 ambiguë (constat 13), H9 écrite à l'indicatif (constat 30).
4. **Fait, en attente, à venir.** Rien de promis avant l'entretien au-delà du témoin positif planté et de la table du coût ; la seule dépense citée de la course exploratoire est conforme (≈ 17,6 dollars estimés) ; aucun chiffre du saboteur à budget ; aucun chiffre de l'état de l'art (seulement des identifiants et des pages reprises de la synthèse scellée du niveau 2). Trois formulations à reprendre : constats 10, 15, 23.
5. **Bras d'attaque.** Rien au-delà de N-054, N-056, N-062, de la consigne de la v19 et des registres (R-597, R-2127) ; état écrit comme dicté. Une condition manque (constat 16).
6. **Lisibilité.** Constats 13, 19, 20, 21, 26, 28, 29, 31, 32, 34, 37.

## Table des constats

| n° | gravité | lieu | source |
|---|---|---|---|
| 1 | **bloquant** | § 0, « Le pari » | docs/decisions/decision-N-003-N-004-v1.md § 1 ; note mathématique v3 § 4 ; resultats-T0.3-v1.md, magnitude 4 et table E, points 3 et 5 |
| 2 | **bloquant** | § 2.4, phrase « en langage courant » | decision-N-003-N-004-v1.md § 1 (« vrai en classe C pour les statistiques symétriques, faux en classe K ») ; note v3 § 4 |
| 3 | **bloquant** | § 2.3, ligne des statuts | prereg/T0.3-simulation-lemme-theoreme-v1.md, prédictions P1 à P8 (l. 79-215) et l. 56 ; note v3 § 3 (L5 : chiffres « exploratoire ») ; resultats-T0.3-v1.md, table E |
| 4 | à corriger | § 0, « Le pari » ; § 2.3, phrase « en langage courant » | decision-N-003-N-004-v1.md § 2 (L1 : « À B fixé, elle décroît avec n₀ » ; L3 : « le calendrier compte ») ; resultats-T0.3-v1.md, table E, point 1 |
| 5 | à corriger | § 2.3, L4 | note mathématique v3 § 3, L4 (« Hypothèses : pas d'interférence entre agents ; nombre d'actions par pas fixe ; pas de statistiques par agent. Validité : le seuil suppose des agents indépendants au sein d'un pas ») |
| 6 | à corriger | § 2.6 (b), titre et mise en garde | sortie rejouée du script (partie B : somme glissante 1,0000) ; note v3 § 4, T1 (statistiques symétriques) et T3 |
| 7 | à corriger | § 1 (dernier alinéa avant « Encore faut-il ») ; § 2.6, chapeau | prereg/T0.6-organismes-v0-v1.md, plan d'analyse, point 2 (T = 10) ; formule de L1 ; calcul du contre-lecteur : Φ̄(2,3263 − 5/√10) = 0,228 |
| 8 | à corriger | § 2.1, lecture de la formule | docs/programme-controle-ia-v2.md § 4 (« Utilité = performance sur la tâche honnête sous π_B ») |
| 9 | à corriger | § 2.5, hypothèse pivot | journal du document, manque 2 (« Préenregistrements de G1 et du papier C au brouillon ») ; registres/etat.md, « Derniers verdicts de porte » (critère 6 ouvert) |
| 10 | à corriger | § 2.5, simulation | registres/decisions.md, R-2126 (l. 2084), point (2) : « verdict formel de T0.3 par un lecteur neuf, sur sa branche (bc53b746…, « confirmé avec réserves »), repris à la fusion » |
| 11 | à corriger | § 1, encadré du fil rouge ; § 7, ligne du 19–20 octobre | docs/verdicts/verdict-P3-premier-test-i-a-v2.md, l. 509-512 (réserve B1 : « la cause n'est pas mesurée (unité, échelle des propositions, gonflement) ») ; registre des affirmations, A07 (calcul) |
| 12 | à corriger | § 3, fiche H1, ligne « réfutation » | decision-N-055-v1.md, nœud H1b ; decision-N-056-v1.md, point 1 (« G1 porte deux questions à la fois … un échec ne dira pas laquelle a échoué … H2 garde ses propres tests de (ii) et (iii) ») et point 4 |
| 13 | à corriger | § 3, fiche H2, ligne « prédiction ; réfutation » | decision-N-007-N-008-v1.md § 1 (table des quatre bases) ; § 4.2 du document (saboteurs (ii), (ii-b), (iv)) |
| 14 | à corriger | § 5, tableau, porte décisive | decision-N-055-v1.md, D-S10 (« mode tenu à l'écart hors décision ») ; decision-N-056-v1.md, point 4 (D-S29 : « dans chacun des autres modes, mode tenu à l'écart compris ; nœud de porte, fixé au préenregistrement de G1 ») ; registres/decisions.md, R-600 (l. 826) |
| 15 | à corriger | § 0, troisième puce ; § 8, encadré final | registres/decisions.md, R-2130 (l. 2088 : entretien visé le 27 ; « sept jours de plus pour le préenregistrement des surveillants externes ») ; socle de preuves § 2.2, écrit pour un entretien le 22 |
| 16 | à corriger | § 6, bras d'attaque, « Cloisons » ; § 9, « Ce qui dépend de toi », point 5 | registres/decisions.md, R-2127 (l. 2085 : « il faut ton mot direct dans la session qui en a la charge, et une dépense go » ; « Aucune ligne dans registres/go.md (pas de devis, pas de plafond, pas de périmètre chez la mère) ») ; R-611 (l. 838) ; R-2045 (l. 2003) |
| 17 | à corriger | § 6, organisme d'idéation, « Objectif ultime » | decision-N-044-v1.md, énoncé 1 (« axe contrôle de populations d'agents, essaim autonome ») ; decision-N-045-v2.md ; journal du document, manque 3 |
| 18 | à corriger | § 7, ligne du 5–10 novembre | docs/verdicts/verdict-validation-nul-v9-v1.md, en tête (« Issue retenue : « puissance perdue » » ; réserve 1 : « Tout l'écart au prix tient à une ligne ») |
| 19 | à corriger | § 8.1, « Hypothèses » | prereg/T0.6-organismes-v0-v1.md, « Hypothèse » (H6-1 à H6-4) ; programme § 5 (H6, marge asymétrique) |
| 20 | à corriger | § 8.2, issue « vu » | brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md, l. 1005 (« il se lit sur le saboteur discret ») |
| 21 | à corriger | § 4.1 ; § 9, chemin critique, ligne du 13 | docs/verdicts/verdict-T0.5-pilote-v1.md, l. 50 (« les deux juges, 8B et 3B, en nœud : aucune notation décisive n'est écrite, car le run s'est arrêté à l'échéance interne ») ; CLAUDE.md, hiérarchie de décision |
| 22 | à corriger | § 9, tableau des cinq affirmations, dernière ligne ; « Ce qui dépend de toi », point 7 | socle de preuves § 1.1, § 1.3, § 1.5 ; decision-N-015-v1.md (20 octobre) contre la candidature l. 152-155 (quatre interventions, bruit d'activations compris) ; decision-N-064-v1.md contre la candidature l. 264 |
| 23 | à corriger | § 9, chemin critique, ligne du 20 | socle de preuves § 2.1 (quatre conditions ; « seules les valeurs « issue » et « ligne » sont affichées ; le verdict en prose reste fermé ») ; CLAUDE.md, N-066 |
| 24 | à corriger | registre des affirmations (pas le HTML) | empreintes recalculées par le contre-lecteur le 10 novembre 2026 ; registres/decisions.md l. 826, 2085, 2088 ; candidature l. 159 |
| 25 | mineur | § 2.2, hypothèses de la garantie | note mathématique v3 § 1, (V) : « μ₀ connu ; σ connu ou majoré ; incréments conditionnellement sous-gaussiens » |
| 26 | mineur | § 2.3, L1 ; § 2.1, scores | note v3 § 3 (« trajectorielle ») et § 4, T3 (co-élévation) |
| 27 | mineur | § 2.3, L2 et L3 (c) | note v3 § 3, L2 (« plancher … strictement au-dessus de α ») ; sortie du script (0,0270 pour α = 0,01) ; decision-N-003-N-004-v1.md § 2 (prix chiffré par T0.3) |
| 28 | mineur | § 2.5, troisième puce | candidature l. 6-9 et 87-88 |
| 29 | mineur | § 3, fiche H1, ligne « énoncé » | programme § 6 (« flou à la relecture, vérifiable en aval ») |
| 30 | mineur | § 3, fiche H9 | decision-N-035-v1.md § 2 (« peut s'éroder » ; « Prédiction, à signer et chiffrer au préenregistrement ») |
| 31 | mineur | § 4.2, saboteur à budget | proposition-P-066, « L'organisme proposé » (règle d'acceptation lue par « l'oracle du mode coût ») |
| 32 | mineur | § 5, tableau, porte décisive | decision-N-007-N-008-v1.md § 2 (« Le bras F1 se gagne en sur-signalant ») ; decision-N-055-v1.md, D-S11 ; decision-N-056-v1.md, point 2 |
| 33 | mineur | § 6, bras d'attaque, « Pourquoi » | consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md § 2 (« un mode qu'aucun concepteur de moniteur n'a vu ») |
| 34 | mineur | alinéa « Le juge attaqué » | verdict-officiel-a1-v4-v1.md § 2.1 (« Texte écrit pour deux mondes au nul ; dans cette course, W2 seul est au nul ») et § 2.2 (monde à dose 0,40) |
| 35 | mineur | § 7, ligne du 6 octobre | docs/verdicts/verdict-T0.4-critere-1-G0-v3.md, observation 3 (« plus long contexte rempli 1 192 jetons contre 1 087 … Au-delà, seule la garde de production couvre ») |
| 36 | mineur | § 9, tableau des cinq affirmations, troisième ligne | livrables/registres-taif-v4/calibration-v3.md, l. 264-267 (235 inscrites, 60 tranchées) |
| 37 | mineur | glossaire ; PDF | consigne-document-de-zero-v1.md § 2, règle 1, et § 5 |

## Constats, avec les couples « texte actuel → texte corrigé »

Chaque « texte actuel » est recopié du HTML (`2c639ca3…`) et y figure **exactement une fois** (contrôlé par programme, 47 couples) : un script peut l'appliquer par remplacement de chaîne. Les balises HTML font partie des chaînes.

### Constat 1 — bloquant — § 0, « Le pari »

- **Source** : docs/decisions/decision-N-003-N-004-v1.md § 1 ; note mathématique v3 § 4 ; resultats-T0.3-v1.md, magnitude 4 et table E, points 3 et 5.
- **Constat** : La page 1 énonce le théorème négatif dans la forme que N-003 a écartée : en classe K (dépendance changée, lois marginales gardées), la somme n'est pas aveugle (0,253 au lieu de 0,05 sur la construction d'arXiv 2606.10456). C'est l'erreur même que le document reproche plus loin à la candidature. Plus fort que sa source.

Texte actuel :

```
et un <b>théorème négatif</b> (si le sabotage ne change que l'ordre ou la dépendance des scores, une somme ne voit rien, et il faut un autre outil).
```

Texte corrigé :

```
et un <b>théorème négatif</b> (si le sabotage ne fait que réarranger les scores, sans changer leurs valeurs, la somme totale et le maximum ne voient rien, et il faut une statistique locale, sensible à l'ordre ; s'il change seulement la dépendance entre des scores qui gardent chacun leur loi, la somme n'est pas aveugle, mais elle reste faible).
```

### Constat 2 — bloquant — § 2.4, phrase « en langage courant »

- **Source** : decision-N-003-N-004-v1.md § 1 (« vrai en classe C pour les statistiques symétriques, faux en classe K ») ; note v3 § 4.
- **Constat** : « ou la dépendance » contredit la puce « Classe K » du même paragraphe et l'énoncé en vigueur.

Texte actuel :

```
<b>si l'attaquant ne change que l'arrangement ou la dépendance de ses scores, sans en changer les valeurs, une somme ou un maximum ne voient rien ; il faut des statistiques qui regardent l'ordre, et localement.</b>
```

Texte corrigé :

```
<b>si l'attaquant ne change que l'arrangement de ses scores, sans en changer les valeurs, la somme totale et le maximum ne voient rien ; il faut des statistiques qui regardent l'ordre, et localement. S'il change la dépendance entre des scores qui gardent chacun leur loi, ce n'est plus vrai : la somme peut voir.</b>
```

### Constat 3 — bloquant — § 2.3, ligne des statuts

- **Source** : prereg/T0.3-simulation-lemme-theoreme-v1.md, prédictions P1 à P8 (l. 79-215) et l. 56 ; note v3 § 3 (L5 : chiffres « exploratoire ») ; resultats-T0.3-v1.md, table E.
- **Constat** : Statut faux : aucune des 31 prédictions de la simulation ne porte sur L5 (P1, P2 : L1 et L2 ; P3 : L3 ; P4, P5, P7 : T1 à T4 ; P6 : classe K ; P8 : validité). L5 n'a que les chiffres exploratoires de la contre-vérification (0,53 ; 0,65 ; 0,08), que la consigne interdit de présenter comme un résultat.

Texte actuel :

```
<span class="chip sim">simulé</span> L1 à L3 et L5 (§ 2.5).
```

Texte corrigé :

```
<span class="chip sim">simulé</span> L1 à L3 (§ 2.5) ; L4 n'est pas testé ; L5 n'a que des chiffres exploratoires, hors de la simulation préenregistrée.
```

### Constat 4 — à corriger — § 0, « Le pari » ; § 2.3, phrase « en langage courant »

- **Source** : decision-N-003-N-004-v1.md § 2 (L1 : « À B fixé, elle décroît avec n₀ » ; L3 : « le calendrier compte ») ; resultats-T0.3-v1.md, table E, point 1.
- **Constat** : L'énoncé courant du lemme omet les deux bornes de l'énoncé en vigueur : statistique lue à la fin, nombre d'actions fixé. Lu seul, il redit l'énoncé du programme que N-004 a corrigé.

Texte actuel 1 :

```
la somme des scores voit le budget total du sabotage, quelle que soit sa répartition
```

Texte corrigé 1 :

```
la somme des scores, lue à la fin de l'épisode, voit le budget total du sabotage, quelle que soit sa répartition
```

Texte actuel 2 :

```
<b>à budget total fixé, une statistique qui somme les scores voit le sabotage de la même façon, qu'il soit concentré ou éparpillé</b> ; un maximum, lui, le perd quand il s'éparpille.
```

Texte corrigé 2 :

```
<b>à budget total et à nombre d'actions fixés, la somme des scores lue à la fin voit le sabotage de la même façon, qu'il soit concentré ou éparpillé</b> ; un maximum, lui, le perd quand il s'éparpille ; la somme lue en continu, elle, dépend du moment où le sabotage a lieu.
```

### Constat 5 — à corriger — § 2.3, L4

- **Source** : note mathématique v3 § 3, L4 (« Hypothèses : pas d'interférence entre agents ; nombre d'actions par pas fixe ; pas de statistiques par agent. Validité : le seuil suppose des agents indépendants au sein d'un pas »).
- **Constat** : Deux hypothèses manquent ; l'indépendance est une condition de validité du seuil, non une hypothèse de l'identité, et elle tombe dans le régime du papier B.

Texte actuel :

```
Hypothèses : agents sans interférence, et indépendants au sein d'un pas. <b>Non testé en simulation</b>
```

Texte corrigé :

```
Hypothèses : agents sans interférence, nombre d'actions par pas fixe, aucune statistique par agent ; le seuil suppose en plus des agents indépendants au sein d'un pas, ce qui n'est pas le cas de copies à poids partagés (papier B). <b>Non testé en simulation</b>
```

### Constat 6 — à corriger — § 2.6 (b), titre et mise en garde

- **Source** : sortie rejouée du script (partie B : somme glissante 1,0000) ; note v3 § 4, T1 (statistiques symétriques) et T3.
- **Constat** : « toute somme » est faux dans le tableau même : la somme glissante de 10 actions est une somme et voit tout. L'aveuglement vaut pour les statistiques symétriques (somme totale, maximum).

Texte actuel 1 :

```
<b>(b) Un dommage porté par l'arrangement, à valeurs préservées, reste invisible à toute somme</b> (classe C)
```

Texte corrigé 1 :

```
<b>(b) Un dommage porté par l'arrangement, à valeurs préservées, reste invisible à la somme totale et au maximum</b> (classe C)
```

Texte actuel 2 :

```
« invisible à toute somme » est vrai pour un réarrangement, pas pour toute dépendance.
```

Texte corrigé 2 :

```
« invisible à la somme totale » est vrai pour un réarrangement, pas pour toute dépendance.
```

### Constat 7 — à corriger — § 1 (dernier alinéa avant « Encore faut-il ») ; § 2.6, chapeau

- **Source** : prereg/T0.6-organismes-v0-v1.md, plan d'analyse, point 2 (T = 10) ; formule de L1 ; calcul du contre-lecteur : Φ̄(2,3263 − 5/√10) = 0,228.
- **Constat** : Limite non dite de l'illustration : le décalage (0,5 σ), le budget (50) et l'horizon (200 actions) sont choisis, non mesurés, et l'horizon vaut vingt fois l'épisode réel de dix actions, annoncé au § 1. À dix actions et 0,5 σ, la somme à horizon fixé n'alerte que 22,8 fois sur 100 : le lecteur ne doit pas croire que « 88,7 % » décrit le programme. Le chiffre 0,228 est un calcul du contre-lecteur par la formule fermée de L1 ; il est à faire sortir par une version 2 du script avant d'entrer au document.

Texte actuel 1 :

```
Si la moitié des 200 actions d'une longue suite sont sabotées
```

Texte corrigé 1 :

```
Prenons une suite de 200 actions, vingt fois plus longue qu'un épisode du programme : si la moitié sont sabotées
```

Texte actuel 2 :

```
Aucune donnée du programme n'est lue.</p>
```

Texte corrigé 2 :

```
Aucune donnée du programme n'est lue. Le décalage par action, le budget et l'horizon de 200 actions sont choisis pour l'illustration : aucun n'est mesuré. Un épisode du programme compte dix actions ; à dix actions et un décalage de 0,5 σ, la même somme n'alerterait qu'environ 23 fois sur 100 (formule fermée de L1).</p>
```

### Constat 8 — à corriger — § 2.1, lecture de la formule

- **Source** : docs/programme-controle-ia-v2.md § 4 (« Utilité = performance sur la tâche honnête sous π_B »).
- **Constat** : Inexact : l'utilité est ce qui reste de la performance, non le coût de la défense.

Texte actuel :

```
l'utilité est ce que la défense coûte à l'agent honnête.
```

Texte corrigé :

```
l'utilité est ce que l'agent honnête accomplit encore sous la défense.
```

### Constat 9 — à corriger — § 2.5, hypothèse pivot

- **Source** : journal du document, manque 2 (« Préenregistrements de G1 et du papier C au brouillon ») ; registres/etat.md, « Derniers verdicts de porte » (critère 6 ouvert).
- **Constat** : Plus fort que sa source : le test de E1.3 n'est préenregistré nulle part.

Texte actuel :

```
(test préenregistré de E1.3)
```

Texte corrigé :

```
(test de l'expérience E1.3, à préenregistrer)
```

### Constat 10 — à corriger — § 2.5, simulation

- **Source** : registres/decisions.md, R-2126 (l. 2084), point (2) : « verdict formel de T0.3 par un lecteur neuf, sur sa branche (bc53b746…, « confirmé avec réserves »), repris à la fusion ».
- **Constat** : Périmé à la date du document : un verdict formel est annoncé par relais sur une autre branche. Le contre-lecteur n'a pas lu ce verdict (hors de la branche principale) : la phrase corrigée dit seulement ce que dit le registre.

Texte actuel :

```
Le prononcé est celui du code de lecture gelé ; aucun lecteur neuf n'a scellé de verdict (socle de preuves, manque 7).
```

Texte corrigé :

```
Le prononcé est celui du code de lecture gelé ; un verdict formel d'un lecteur neuf (« confirmé avec réserves ») est annoncé sur une autre branche du dépôt et n'est pas encore versé dans la branche principale (registre des décisions, R-2126).
```

### Constat 11 — à corriger — § 1, encadré du fil rouge ; § 7, ligne du 19–20 octobre

- **Source** : docs/verdicts/verdict-P3-premier-test-i-a-v2.md, l. 509-512 (réserve B1 : « la cause n'est pas mesurée (unité, échelle des propositions, gonflement) ») ; registre des affirmations, A07 (calcul).
- **Constat** : Plus fort que sa source : « il a gonflé son coût d'un facteur 33 » donne pour cause le gonflement, que la réserve gelée du verdict dit non mesurée ; le facteur est un calcul (10 puissance 1,5227 = 33,3), sur une différence de logarithmes, donc une moyenne géométrique.

Texte actuel 1 :

```
Il a gonflé son coût d'un facteur d'environ 33 (§ 7). Il est donc <b>flagrant</b>
```

Texte corrigé 1 :

```
Le coût qu'il déclare vaut environ 33 fois celui de l'agent honnête, en moyenne géométrique (§ 7) ; la cause de l'écart à la consigne n'est pas mesurée (unité, échelle des propositions ou gonflement : réserve du verdict). Il est donc <b>flagrant</b>
```

Texte actuel 2 :

```
soit un facteur ≈ 33 pour une consigne de ≈ 3.
```

Texte corrigé 2 :

```
soit un facteur ≈ 33 (calcul : 10 puissance 1,5227) pour une consigne de ≈ 3 ; la cause de cet écart n'est pas mesurée (réserve du verdict).
```

### Constat 12 — à corriger — § 3, fiche H1, ligne « réfutation »

- **Source** : decision-N-055-v1.md, nœud H1b ; decision-N-056-v1.md, point 1 (« G1 porte deux questions à la fois … un échec ne dira pas laquelle a échoué … H2 garde ses propres tests de (ii) et (iii) ») et point 4.
- **Constat** : Inexact : la fiche donne pour réfutation de H1 l'échec de la porte décisive. Or la porte demande plus que H1 (battre aussi deux lectures internes concurrentes, question de H2) : un échec de la porte ne réfute pas H1 à lui seul.

Texte actuel :

```
Le critère de la porte décisive n'est pas atteint (§ 5) : aucun rappel à 1 % de faux positifs supérieur, établi, contre la meilleure base boîte noire et contre les deux bases boîte blanche, dans chaque mode. L'échec déclenche une reconception des sondes, pas l'arrêt (N-062).
```

Texte corrigé :

```
À agrégation égale, le rappel à 1 % de faux positifs de la lecture interne n'est pas établi supérieur à celui de la lecture externe sur la strate « diffus, flou », dans l'un au moins des modes mesurés (mode tenu à l'écart compris). La porte décisive demande davantage (battre aussi deux autres façons de lire l'intérieur, § 5) : son échec ne dit pas laquelle des deux questions a échoué, et il déclenche une reconception des sondes, pas l'arrêt (N-062).
```

### Constat 13 — à corriger — § 3, fiche H2, ligne « prédiction ; réfutation »

- **Source** : decision-N-007-N-008-v1.md § 1 (table des quatre bases) ; § 4.2 du document (saboteurs (ii), (ii-b), (iv)).
- **Constat** : Lisibilité : « (ii) » et « (iii) » désignent ici des bases de comparaison, et au § 4 des saboteurs ; « cascade de portes » n'est expliqué nulle part ; « ne bat pas A ni B » est ambigu. La glose entre parenthèses est une paraphrase du contre-lecteur (« cascade de portes indépendantes », N-007) : à faire valider.

Texte actuel :

```
ou si l'accumulation ne bat pas la cascade de portes sur les mêmes sondes ni la sonde du dernier état (bases (ii) et (iii), § 5).
```

Texte corrigé :

```
ou si l'accumulation ne bat pas l'une des deux lectures internes concurrentes : la cascade de portes sur les mêmes sondes (des portes indépendantes, sans addition des scores) ou la sonde lue sur le seul dernier état (§ 5 ; les décisions notent ces deux bases (ii) et (iii), sans rapport avec les saboteurs du § 4).
```

### Constat 14 — à corriger — § 5, tableau, porte décisive

- **Source** : decision-N-055-v1.md, D-S10 (« mode tenu à l'écart hors décision ») ; decision-N-056-v1.md, point 4 (D-S29 : « dans chacun des autres modes, mode tenu à l'écart compris ; nœud de porte, fixé au préenregistrement de G1 ») ; registres/decisions.md, R-600 (l. 826).
- **Constat** : Deux décisions disent deux choses du mode tenu à l'écart : hors de la décision de la porte (N-055, D-S10), et compris dans l'exigence du gain de H1 (N-056, D-S29). Le document tranche sans le dire. Le contre-lecteur n'a pas lu les conceptions du pari postérieures à la v2, qui peuvent avoir réécrit D-S10.

Texte actuel :

```
Rapporté et exigé par mode, mode tenu à l'écart compris (N-054, N-056).
```

Texte corrigé :

```
Rapporté par mode (N-054). Le gain de H1 est exigé dans chaque mode, mode tenu à l'écart compris (N-056, point 4, confirmé le 28 octobre) ; N-055 plaçait ce mode hors de la décision de la porte : la règle entre modes se fixe au préenregistrement.
```

### Constat 15 — à corriger — § 0, troisième puce ; § 8, encadré final

- **Source** : registres/decisions.md, R-2130 (l. 2088 : entretien visé le 27 ; « sept jours de plus pour le préenregistrement des surveillants externes ») ; socle de preuves § 2.2, écrit pour un entretien le 22.
- **Constat** : « n'est possible » repose sur le socle, écrit pour le 22 novembre ; avec le 27, c'est une prévision du rédacteur. Dire la condition, non l'impossibilité. Rien n'est promis au-delà des deux résultats : conforme sur ce point.

Texte actuel 1 :

```
Aucune lecture de sonde sur cette course n'est possible avant.</li>
```

Texte corrigé 1 :

```
Aucune lecture de sonde sur cette course n'est prévue avant : elle exige le verdict scellé du témoin positif et la lecture scellée des surveillants de référence, dont le préenregistrement n'existe pas.</li>
```

Texte actuel 2 :

```
Aucune lecture de sonde sur cette course n'est possible avant. Le reste est préenregistré
```

Texte corrigé 2 :

```
Aucune lecture de sonde sur cette course n'est prévue avant : elle exige le verdict scellé du témoin positif et la lecture scellée des surveillants de référence, dont le préenregistrement n'existe pas. Le reste est préenregistré
```

### Constat 16 — à corriger — § 6, bras d'attaque, « Cloisons » ; § 9, « Ce qui dépend de toi », point 5

- **Source** : registres/decisions.md, R-2127 (l. 2085 : « il faut ton mot direct dans la session qui en a la charge, et une dépense go » ; « Aucune ligne dans registres/go.md (pas de devis, pas de plafond, pas de périmètre chez la mère) ») ; R-611 (l. 838) ; R-2045 (l. 2003).
- **Constat** : Le document tient l'état dicté (« monté ; lancement décidé le 10 novembre ; rien n'a encore tourné ») et ne dit rien au-delà des décisions : conforme. Il omet la seconde condition du mot de Lazar : une autorisation de dépense, qui n'est pas inscrite. Deux faits du registre ne sont pas dits et sont laissés à la mère : un second arrêt par un classifieur le 9 novembre (R-2045) ; la décision de gouvernance du 28 octobre (R-611) qui gèle tout pipeline opérationnel d'évasion jusqu'à une revue de sécurité externe — le contre-lecteur ne peut pas établir, sans ouvrir les pièces interdites, si elle couvre ce bras.

Texte actuel 1 :

```
Lazar a décidé le 10 novembre de le lancer avant l'entretien ; rien n'a encore tourné.</p>
```

Texte corrigé 1 :

```
Lazar a décidé le 10 novembre de le lancer avant l'entretien ; rien n'a encore tourné : le lancement attend son mot direct dans la session qui en a la charge et une autorisation de dépense sur devis, qui n'est pas inscrite.</p>
```

Texte actuel 2 :

```
son lancement passe par ton mot direct dans la session qui en a la charge.
```

Texte corrigé 2 :

```
son lancement passe par ton mot direct dans la session qui en a la charge, et par une autorisation de dépense sur devis (aucune n'est inscrite).
```

### Constat 17 — à corriger — § 6, organisme d'idéation, « Objectif ultime »

- **Source** : decision-N-044-v1.md, énoncé 1 (« axe contrôle de populations d'agents, essaim autonome ») ; decision-N-045-v2.md ; journal du document, manque 3.
- **Constat** : Le journal reconnaît que le lien entre « l'organisme » de N-044 et N-045 et l'organisme d'idéation n'est écrit nettement dans aucune source ; le document ne le dit pas. Non vérifiable tel qu'écrit.

Texte actuel :

```
<b>Objectif ultime</b> (N-044, N-045 v2) : un organisme
```

Texte corrigé :

```
<b>Objectif ultime</b> (N-044, N-045 v2 ; ces décisions parlent d'« un organisme » sans dire en toutes lettres qu'il s'agit de l'organisme d'idéation : le rapprochement est fait ici) : un organisme
```

### Constat 18 — à corriger — § 7, ligne du 5–10 novembre

- **Source** : docs/verdicts/verdict-validation-nul-v9-v1.md, en tête (« Issue retenue : « puissance perdue » » ; réserve 1 : « Tout l'écart au prix tient à une ligne »).
- **Constat** : « validé » est plus fort que l'issue du verdict, qui est « puissance perdue ».

Texte actuel :

```
le nul du nouveau juge, validé, perd de la puissance sur une ligne
```

Texte corrigé :

```
la validation du nul du nouveau juge rend « puissance perdue » (tout l'écart tient à une ligne)
```

### Constat 19 — à corriger — § 8.1, « Hypothèses »

- **Source** : prereg/T0.6-organismes-v0-v1.md, « Hypothèse » (H6-1 à H6-4) ; programme § 5 (H6, marge asymétrique).
- **Constat** : Lisibilité : un lecteur neuf lira « H6-1 » comme une partie de l'hypothèse H6 du § 3. Ce sont des étiquettes du texte scellé de la tâche T0.6.

Texte actuel :

```
<b>Hypothèses</b> : (H6-1) l'adaptateur
```

Texte corrigé :

```
<b>Hypothèses</b> (étiquettes du texte scellé, sans rapport avec l'hypothèse H6 du § 3) : (H6-1) l'adaptateur
```

### Constat 20 — à corriger — § 8.2, issue « vu »

- **Source** : brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md, l. 1005 (« il se lit sur le saboteur discret »).
- **Constat** : Lisibilité : « saboteur discret » n'est défini nulle part, et le même saboteur est dit « flagrant » dans tout le document.

Texte actuel :

```
et le nul du premier test se lit sur le saboteur discret ;
```

Texte corrigé :

```
et le nul du premier test se lit alors sur le saboteur du premier test lui-même (que le texte appelle « discret »), non comme une panne de la chaîne ;
```

### Constat 21 — à corriger — § 4.1 ; § 9, chemin critique, ligne du 13

- **Source** : docs/verdicts/verdict-T0.5-pilote-v1.md, l. 50 (« les deux juges, 8B et 3B, en nœud : aucune notation décisive n'est écrite, car le run s'est arrêté à l'échéance interne ») ; CLAUDE.md, hiérarchie de décision.
- **Constat** : Terme de registre non défini (« nœud » : décision réservée à Lazar).

Texte actuel 1 :

```
les deux juges du pilote sont en nœud.
```

Texte corrigé 1 :

```
les deux juges du pilote n'ont rendu aucune notation décisive (la course s'est arrêtée avant) : leur sort est une décision en attente de Lazar (un « nœud », dans les registres).
```

Texte actuel 2 :

```
Bascule sur une chaîne de lancement préparée : écart au texte scellé, nœud.
```

Texte corrigé 2 :

```
Bascule sur une chaîne de lancement préparée : c'est un écart au texte scellé, donc une décision de Lazar.
```

### Constat 22 — à corriger — § 9, tableau des cinq affirmations, dernière ligne ; « Ce qui dépend de toi », point 7

- **Source** : socle de preuves § 1.1, § 1.3, § 1.5 ; decision-N-015-v1.md (20 octobre) contre la candidature l. 152-155 (quatre interventions, bruit d'activations compris) ; decision-N-064-v1.md contre la candidature l. 264.
- **Constat** : Incohérence interne (« trois écarts » dans le tableau, « deux écarts » au point 7) et liste incomplète au regard du socle : « No claimed statement has been found fully occupied » (resserré depuis par N-064), « I … take every decision », la dépense « about $20 » ; et, non relevé par le socle, le bruit d'activations que la candidature compte encore parmi les interventions de H6 (retiré par N-015). La phrase sur arXiv 2606.10456 (l. 87-88 de la candidature, vérifiée) : conforme aux pièces — l'énoncé « puissance = taux de faux positifs » est faux pour la somme (0,253), vrai et même pessimiste pour le maximum (0,027).

Texte actuel 1 :

```
Trois écarts au texte envoyé, à dire soi-même : le repli « négatif + H8 » remplacé ; la date de G0 ; la phrase sur arXiv 2606.10456, vraie pour la somme seulement.
```

Texte corrigé 1 :

```
Écarts au texte envoyé, à dire soi-même : le repli « négatif + H8 » remplacé ; la date de G0 ; la phrase sur arXiv 2606.10456, vraie pour la somme seulement ; et, hors du repli : le bruit d'activations retiré de H6 (N-015), la revendication du juge resserrée (N-064), la dépense (§ 7).
```

Texte actuel 2 :

```
valider la correction des deux écarts au texte envoyé.
```

Texte corrigé 2 :

```
valider la correction des écarts au texte envoyé (dernière ligne du tableau ci-dessus).
```

### Constat 23 — à corriger — § 9, chemin critique, ligne du 20

- **Source** : socle de preuves § 2.1 (quatre conditions ; « seules les valeurs « issue » et « ligne » sont affichées ; le verdict en prose reste fermé ») ; CLAUDE.md, N-066.
- **Constat** : Ce qui sera lu le 20 est une ouverture réduite, sous conditions : le dire évite de promettre un verdict complet.

Texte actuel :

```
<td>Lecture du témoin positif sur le mot « ouvrir » de Lazar.</td>
```

Texte corrigé :

```
<td>Ouverture réduite du témoin positif sur le mot « ouvrir » de Lazar : seules l'issue et sa ligne sont affichées, et seulement si la course est finie et scellée et le préenregistrement des sondes scellé avec la garde (N-066).</td>
```

### Constat 24 — à corriger — registre des affirmations (pas le HTML)

- **Source** : empreintes recalculées par le contre-lecteur le 10 novembre 2026 ; registres/decisions.md l. 826, 2085, 2088 ; candidature l. 159.
- **Constat** : Quatre défauts du registre, sans effet sur le texte : (1) A24, A67, A74, A100 : empreinte de la candidature écrite « b2458c2d109a », la pièce vaut « b2458c2d209a » (le journal a la bonne) ; (2) A69, A79, A99, A108 : empreinte de registres/decisions.md écrite « aa5a9e66e5a3 », qui n'est ni celle du journal ni celle du fichier (« 65cc0667dc5c » dans les deux) ; (3) A74 : la porte G1 de la candidature est à la l. 159, non 157 ; (4) A78 et A107, dits « non vérifiés », se vérifient désormais : R-2127 (l. 2085) et R-2130 (l. 2088) ; A73 : la confirmation du 28 octobre est R-600 (l. 826) ; A58 : « domaine (intention) » et « conscience d'évaluation réservée » viennent du brouillon 20 de T0.7 (l. 854-860), non du brief.

### Constat 25 — mineur — § 2.2, hypothèses de la garantie

- **Source** : note mathématique v3 § 1, (V) : « μ₀ connu ; σ connu ou majoré ; incréments conditionnellement sous-gaussiens ».
- **Constat** : Hypothèses incomplètes ; « différences de martingale » non expliqué.

Texte actuel :

```
Elle suppose des incréments indépendants (ou des différences de martingale) et σ connu.
```

Texte corrigé :

```
Elle suppose des écarts successifs indépendants (ou, plus largement, imprévisibles en moyenne au vu du passé : des « différences de martingale »), sans valeurs extrêmes plus fréquentes que sous une loi normale, une moyenne honnête μ<sub>0</sub> connue et σ connu ou majoré.
```

### Constat 26 — mineur — § 2.3, L1 ; § 2.1, scores

- **Source** : note v3 § 3 (« trajectorielle ») et § 4, T3 (co-élévation).
- **Constat** : Deux termes non expliqués.

Texte actuel 1 :

```
(classe M, trajectorielle, sans hypothèse sur la loi honnête)
```

Texte corrigé 1 :

```
(classe M ; « trajectorielle » : vraie épisode par épisode, et non seulement en moyenne ; sans hypothèse sur la loi honnête)
```

Texte actuel 2 :

```
statistique de co-élévation entre agents.
```

Texte corrigé 2 :

```
statistique de co-élévation entre agents (plusieurs agents ont un score élevé au même pas).
```

### Constat 27 — mineur — § 2.3, L2 et L3 (c)

- **Source** : note v3 § 3, L2 (« plancher … strictement au-dessus de α ») ; sortie du script (0,0270 pour α = 0,01) ; decision-N-003-N-004-v1.md § 2 (prix chiffré par T0.3).
- **Constat** : « à peine au-dessus » : 2,7 fois α dans l'exemple. Le prix « chiffré » l'est par la simulation ; le § 2.6 n'est qu'une illustration.

Texte actuel 1 :

```
vers un plancher à peine au-dessus de α quand le sabotage est réparti sur toutes les actions.
```

Texte corrigé 1 :

```
vers un plancher strictement au-dessus de α quand le sabotage est réparti sur toutes les actions (2,7 % pour α = 1 % dans l'exemple du § 2.6).
```

Texte actuel 2 :

```
(c) la garantie toujours valide a un prix, chiffré (§ 2.6) ;
```

Texte corrigé 2 :

```
(c) la garantie toujours valide a un prix, chiffré par la simulation (§ 2.5) et illustré au § 2.6 ;
```

### Constat 28 — mineur — § 2.5, troisième puce

- **Source** : candidature l. 6-9 et 87-88.
- **Constat** : « La candidature » apparaît ici pour la première fois, sans dire à qui ni quand.

Texte actuel :

```
La candidature envoyée écrit que
```

Texte corrigé :

```
La candidature (la demande de bourse envoyée au fonds le 7 octobre 2026) écrit que
```

### Constat 29 — mineur — § 3, fiche H1, ligne « énoncé »

- **Source** : programme § 6 (« flou à la relecture, vérifiable en aval »).
- **Constat** : « tâches floues » non expliqué ; « mode tenu à l'écart » y est employé avant sa définition du § 6 (ajouter « défini au § 6 »).

Texte actuel :

```
détecte plus de sabotage diffus sur tâches floues qu'un surveillant boîte noire.
```

Texte corrigé :

```
détecte plus de sabotage diffus sur tâches floues (dont la qualité ne se juge pas à la relecture, seulement en aval) qu'un surveillant boîte noire.
```

### Constat 30 — mineur — § 3, fiche H9

- **Source** : decision-N-035-v1.md § 2 (« peut s'éroder » ; « Prédiction, à signer et chiffrer au préenregistrement »).
- **Constat** : L'indicatif présente comme un fait ce que la décision pose comme une prédiction à tester.

Texte actuel :

```
Une contrainte de sécurité explicite s'érode à chaque délégation d'un agent à un sous-agent ; un surveillant à chaque passage la relève.
```

Texte corrigé :

```
Une contrainte de sécurité explicite peut s'éroder à chaque délégation d'un agent à un sous-agent ; prédiction à tester : sa survie décroît avec le nombre de passages, et un surveillant à chaque passage la relève.
```

### Constat 31 — mineur — § 4.2, saboteur à budget

- **Source** : proposition-P-066, « L'organisme proposé » (règle d'acceptation lue par « l'oracle du mode coût »).
- **Constat** : « oracle » employé avant toute explication. Par ailleurs la famille (iii) du programme (organismes publics de l'institut britannique, § 7) manque au tableau sans être dite écartée.

Texte actuel :

```
lus par l'oracle seul.
```

Texte corrigé :

```
lus par l'oracle seul (le programme qui connaît l'estimation honnête cachée).
```

### Constat 32 — mineur — § 5, tableau, porte décisive

- **Source** : decision-N-007-N-008-v1.md § 2 (« Le bras F1 se gagne en sur-signalant ») ; decision-N-055-v1.md, D-S11 ; decision-N-056-v1.md, point 2.
- **Constat** : « F1 » et « pari apparié » ne sont pas expliqués. La glose du pari est une paraphrase du contre-lecteur, qui n'a pas lu la conception du pari : à faire valider.

Texte actuel 1 :

```
Le bras « + 5 points de F1 » est retiré.
```

Texte corrigé 1 :

```
Le second critère d'origine, « + 5 points de F1 » (F1 : moyenne harmonique de la précision et du rappel), est retiré : il se gagne en signalant trop.
```

Texte actuel 2 :

```
Décidé par la borne d'un pari apparié (valide à tout nombre de tâches), rééchantillonnage rapporté à côté (N-055).
```

Texte corrigé 2 :

```
Décidé par la borne basse d'un « pari apparié » (un test sur les différences appariées par tâche, dont la garantie vaut quel que soit le nombre de tâches) ; les intervalles par rééchantillonnage des tâches sont rapportés à côté (N-055, N-056).
```

### Constat 33 — mineur — § 6, bras d'attaque, « Pourquoi »

- **Source** : consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md § 2 (« un mode qu'aucun concepteur de moniteur n'a vu »).
- **Constat** : « que personne n'a vu » est plus large que la source.

Texte actuel :

```
Mesurer l'universalité sur un mode que personne n'a vu ;
```

Texte corrigé :

```
Mesurer si les surveillants gardent leur rappel sur un mode qu'aucun concepteur de surveillant n'a vu ;
```

### Constat 34 — mineur — alinéa « Le juge attaqué »

- **Source** : verdict-officiel-a1-v4-v1.md § 2.1 (« Texte écrit pour deux mondes au nul ; dans cette course, W2 seul est au nul ») et § 2.2 (monde à dose 0,40).
- **Constat** : « où toute promotion est fausse » ne vaut que pour le monde au nul ; « v9 » n'est pas défini ; la lecture gelée parle de deux mondes au nul alors qu'un seul l'est ici, ce que le verdict note.

Texte actuel 1 :

```
sur des mondes jouets où toute promotion est fausse. <b>Monde au nul</b> : 
```

Texte corrigé 1 :

```
sur des mondes jouets. <b>Monde au nul</b> (toute promotion y est fausse) : 
```

Texte actuel 2 :

```
« sur deux mondes jouets au nul v9,
```

Texte corrigé 2 :

```
« sur deux mondes jouets au nul v9 [v9 : le nouveau juge ; le texte gelé est écrit pour deux mondes au nul, un seul l'est dans cette course],
```

### Constat 35 — mineur — § 7, ligne du 6 octobre

- **Source** : docs/verdicts/verdict-T0.4-critere-1-G0-v3.md, observation 3 (« plus long contexte rempli 1 192 jetons contre 1 087 … Au-delà, seule la garde de production couvre »).
- **Constat** : 1 192 est le plus long contexte produit, au-delà du domaine strict validé (1 087).

Texte actuel :

```
Domaine : contextes jusqu'à 1 192 jetons.
```

Texte corrigé :

```
Domaine validé : contextes jusqu'à 1 087 jetons ; la production est allée jusqu'à 1 192, où seule la garde de production couvre.
```

### Constat 36 — mineur — § 9, tableau des cinq affirmations, troisième ligne

- **Source** : livrables/registres-taif-v4/calibration-v3.md, l. 264-267 (235 inscrites, 60 tranchées).
- **Constat** : Le dénominateur complet manque.

Texte actuel :

```
8 non concluantes sur 60 tranchées.
```

Texte corrigé :

```
8 non concluantes sur 60 tranchées (235 inscrites).
```

### Constat 37 — mineur — glossaire ; PDF

- **Source** : consigne-document-de-zero-v1.md § 2, règle 1, et § 5.
- **Constat** : Le glossaire ne porte pas : mode de sabotage, dose, plancher, nœud, oracle, jumeau honnête, pince, pari apparié, étiquettes A1-v3 et v8/v9 (employées aux § 6 et 7). Le PDF (bec30fbc…, 17 pages) est à reconstruire sous un nom neuf après corrections, avec le registre et le journal (R12).

## Ce que je n'ai pas vérifié

- Les pages des articles cités (règle 7) : reprises des décisions et de la synthèse scellée du niveau 2, non relues sur PDF.
- Le verdict formel de la simulation annoncé par R-2126 : il est sur une autre branche, que je n'ai pas lue ; la phrase corrigée du constat 10 ne dit que ce que dit le registre.
- Toute pièce du bras d'attaque, du mode tenu à l'écart, de la course exploratoire 7a, de l'étiqueteur et des textes d'actions de P3 (interdits) : l'état du bras d'attaque est vérifié sur les décisions et le registre seulement ; la portée de R-611 sur ce bras n'est pas établie.
- La conception du pari apparié (versions 2 à 9) : non lue ; la glose du constat 32 et la lecture de D-S10 au constat 14 sont à faire valider.
- Les brouillons de T0.7 et de P3-bis : seuls les passages cités ont été lus ; ils peuvent encore changer avant scellement.
- Les décisions N-059, N-061 et N-066 (cette dernière connue par les consignes permanentes seulement) ; la section « Ce que les auteurs savaient » du texte scellé de T0.6, laissée fermée par prudence.
- Les dates de la première colonne du § 7 et les lignes du chemin critique au-delà du socle de preuves (lui-même non contre-lu à sa date) et de R-2130.
- Le PDF page par page : empreinte et nombre de pages vérifiés, texte extrait sondé sur trois chaînes ; la mise en page n'a pas été regardée.
- Les registres vivants peuvent avoir changé depuis ma lecture (`registres/decisions.md` lu à `65cc0667dc5c…`, 2 088 lignes).
- Le nombre « environ 23 fois sur 100 » du constat 7 est mon calcul par la formule fermée de L1 ; il n'est pas sorti du script scellé.
