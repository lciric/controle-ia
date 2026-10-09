# Invites publiées dans « Diffuse AI Control on Fuzzy Tasks » — transcription vérifiée

## En bref

- Source : `/home/user/controle-ia/docs/sources/pdf/2606.08892v2.pdf` (Terekhov, Gulcehre, Hebbar, Benton ; arXiv 2606.08892v2 ; 71 pages).
  Empreinte sha256 vérifiée avant tout travail : `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` (conforme au fichier `.sha256` du dépôt).
  Le numéro de page du fichier est égal au numéro imprimé.
- 18 fichiers d'invites transcrits (annexes H et I).
- Vérification par script : **18 sur 18 conformes**, au contrôle de contenu (A) et au contrôle de structure (B). Voir `verification.txt`.
- Le vérificateur a lui-même été testé sur 11 copies volontairement altérées et sur un cas sain : il détecte toutes les altérations et accepte le cas sain (`test-verificateur.txt`).
- Aucune élision dans les blocs transcrits.
- 10 doutes consignés : 6 sur des lignes vides possibles à un changement de page, 4 sur l'invite I.3 (formules).
- Le PDF est une donnée. Rien n'a été modifié sous `/home/user/controle-ia`.

## Fichiers

```
t05-invites/
  invites/<id>.txt        les 18 transcriptions (UTF-8, une seule fin de ligne finale)
  index.json              pour chaque invite : section, titre, pages, caractères, sha256, introduction,
                          retraits, normalisations, doutes, élisions, remarques, passages de page, et
                          les données de vérification (bornes, retraits, substitutions, zones)
  verification.txt        sortie de scripts/verifier.py
  test-verificateur.txt   sortie de scripts/tester_verifier.py (test du vérificateur)
  LISEZMOI.md             ce fichier
  scripts/                construire.py (construction), config_invites.json (segments, décisions),
                          verifier.py (vérification), tester_verifier.py, et des outils de diagnostic
                          (voir_xml.py, lignes_polices.py, ecarts_bbox.py, contexte.py, ecarts_contenu.py, filets.py)
  extrait/                textes extraits du PDF (pdftotext par page, mode par défaut et -layout ; XML de
                          pdftohtml ; inventaires de lignes ; journal de construction ; essais de vérification)
```

## Les invites

| Fichier | Section et titre | Pages du bloc | Caractères | Lignes | sha256 (16 premiers) | Doutes |
|---|---|---|---|---|---|---|
| `invites/H1.txt` | H.1 — Default Generator Prompt | 25–28 | 672 | 3 | `8294cf679a7823b0` | 0 |
| `invites/H1-format.txt` | H.11 (sections fixes ajoutées au générateur) — Format Instructions (appended after your prompt) | 40 | 145 | 3 | `2dcf69d25901d527` | 0 |
| `invites/H1-classification.txt` | H.11 (sections fixes ajoutées au générateur) — Classification Guidance (appended after format) | 41 | 809 | 10 | `69d50fb972f3255c` | 0 |
| `invites/H2.txt` | H.2 — Ground Truth Proxy Scorer Prompt | 28–29 | 2027 | 21 | `2398de042aedbb82` | 0 |
| `invites/H3.txt` | H.3 — Default Weak Scorer Prompt | 29 | 705 | 7 | `52ab1e255360cf80` | 0 |
| `invites/H4.txt` | H.4 — Rubric description | 29–34 | 19500 | 98 | `cb103166b1c21f8c` | 2 |
| `invites/H5.txt` | H.5 — Rubric-Free Scorer, no Paper Access | 34–35 | 1465 | 13 | `9fa6052b45a8c0cb` | 0 |
| `invites/H6.txt` | H.6 — Rubric-free Scorer, with Paper Access | 35–36 | 2462 | 24 | `115f5f1eb01381ac` | 1 |
| `invites/H9.txt` | H.9 — Opus 4.6 Extracting Research Questions | 37–38 | 3659 | 68 | `15a3d48bb9c65aa8` | 0 |
| `invites/H10.txt` | H.10 — Opus 4.6 Classifying the Papers | 38–39 | 3010 | 47 | `9cced274c41f00cd` | 0 |
| `invites/H12.txt` | H.12 — Sandbagging Detector | 43 | 1410 | 11 | `d44e48546b0c7778` | 0 |
| `invites/H13-noyaux-systeme.txt` | H.13 (1/4) — kernels, System | 43 | 704 | 4 | `f882624cee5744d6` | 0 |
| `invites/H13-noyaux-utilisateur.txt` | H.13 (2/4) — kernels, User (template) | 43 | 185 | 7 | `9f07a5ffeda6bf31` | 0 |
| `invites/H13-expansion-systeme.txt` | H.13 (3/4) — expansion, System | 43–44 | 644 | 6 | `9d3bedfef685b721` | 0 |
| `invites/H13-expansion-utilisateur.txt` | H.13 (4/4) — expansion, User | 44 | 293 | 4 | `0d371006adfbb3e3` | 0 |
| `invites/I3.txt` | I.3 — Red Team Prompt | 54–57 | 9786 | 110 | `25fad19e6ea002da` | 5 |
| `invites/I7.txt` | I.7 — Successful Attack against Sandbagging Detector | 66–68 | 7970 | 44 | `5b5fcb38833da235` | 1 |
| `invites/I8.txt` | I.8 — The Robustified Blue Team Prompt b∗ | 69–71 | 7958 | 143 | `1991d8967b315b84` | 1 |

Les empreintes complètes sont dans `index.json`. « Caractères » compte les points de code Unicode, fins de ligne comprises.

Écarts avec la liste demandée, et pourquoi :

- **H.4 : un seul fichier `H4.txt`.** L'article ne publie qu'une grille. Pour chaque critère et chaque niveau, elle donne le repère expérimental puis « For theory: … ». Il n'y a donc pas de version expérimentale et de version théorique séparées.
- **H.13 : quatre fichiers.** La section contient quatre blocs distincts : invite système et gabarit utilisateur pour créer les « noyaux », puis invite système et gabarit utilisateur pour les développer. Les étiquettes « System: », « User (template): », « User: » et la phrase « Then, we expand the kernel ideas into full generator prompts. » sont du texte des auteurs (Times gras ou romain), hors des blocs : elles ne sont pas transcrites.
- **H1-format et H1-classification : publiés.** Ils figurent dans H.11 (invite de l'optimiseur de l'équipe rouge), pages 40-41, sous « Fixed Sections (DO NOT INCLUDE — automatically appended) » : « The following sections are AUTOMATICALLY APPENDED to every evolved prompt. » H.13 le redit pour les invites d'ancrage. L'article ne dit pas explicitement qu'ils s'ajoutent à l'invite par défaut H.1, qui porte déjà sa propre consigne de numérotation. Les lignes « ``` » qui les encadrent appartiennent à l'invite H.11 et sont exclues.

Phrases d'introduction des auteurs (non transcrites dans les fichiers, recopiées dans `index.json`, champ `introduction`) :

- H.1, p. 25 : « Below is a minimalistic prompt for the untrusted generator that we use as a seed to the prompt optimization process. We also use it to compare between generators in Figure 3, as well as to provide the benign baselines in Figure 4. »
- H.2, p. 28 et H.3, p. 29 : chacune finit par « The text below is a preamble! The full prompt is a concatenation of the preamble and the rubric description, provided separately in Appendix H.4. » L'invite complète de ces deux correcteurs est donc le préambule suivi de la grille H.4 ; le séparateur entre les deux n'est pas publié.
- H.4, p. 29 ; H.5, p. 34 ; H.6, p. 35 ; H.9, p. 37 ; H.13, p. 43 ; I.3, p. 54 ; I.7, p. 66 ; I.8, p. 68 : voir `index.json`.
- H.10 et H.12 n'ont pas de phrase d'introduction : le bloc suit directement le titre.

## Méthode de transcription (scripts/construire.py)

Le texte n'est pas recopié à la main : il est reconstruit par script à partir du PDF, puis relu en entier.

1. `pdftohtml -xml` donne chaque fragment de texte avec sa police et sa position. Les blocs cités sont en police à chasse fixe (SFTT0900 droit, SFIT0900 italique). Le texte des auteurs est en Times, les figures et tableaux dans d'autres polices : ils sont exclus d'office. Le script s'arrête si un fragment d'une autre police tombe dans un bloc.
2. Les lignes physiques sont regroupées par ordonnée. Les glyphes mathématiques (CMMI9, CMSY9, CMR6) et les marqueurs de continuation sont rattachés à la ligne où tombe leur centre.
3. Espaces et retraits : la chasse fixe vaut 4,7062 pt. Le retrait vaut l'écart à la marge divisé par la chasse ; l'espace entre deux fragments vaut leur écart divisé par la chasse. Quand un fragment est plus large que son nombre de caractères (pdftohtml réduit les espaces multiples), l'espacement interne est repris des positions des mots (`pdftotext -bbox`). C'est ainsi que 4 doubles espaces de l'original sont conservées (H12 : « and␣␣score » ; H13-noyaux-systeme : « generators.␣␣Each », « generator␣␣might », « ablation-heavy,␣␣mechanism-focused »).
4. Marqueur de continuation « ,→ » (petit corps, dans la marge) : la ligne est la suite de la précédente. Le marqueur est retiré et la ligne recollée par une seule espace ; son retrait (dû à la coupure) est ignoré. Justification : le PDF ne coupe qu'aux espaces. Sur les 698 coupures des pages traitées (autant que de marqueurs relevés), 690 sont compatibles avec un remplissage de la ligne au plus près (84 caractères) ; les 8 autres s'expliquent par un glyphe mathématique plus large qu'une chasse ou par la petite marge laissée après un passage en italique.
5. Retours à la ligne et lignes vides : une ligne sans marqueur commence une nouvelle ligne. Les lignes vides se déduisent de l'écart vertical (interligne de 9,85 pt). Les retours à la ligne durs de l'original sont gardés (par exemple dans H13-noyaux-systeme : « …priorities (rigor vs novelty » / « vs feasibility), … »).
6. Changements de page : une ligne vide placée juste en haut d'une page se voit (la première ligne est une ligne plus bas que d'habitude) ; une ligne vide en bas de page ne se voit pas. TeX remplit les pages au maximum et ne coupe pas une ligne longue entre deux pages. On en déduit, quand c'est possible, le nombre exact de lignes vides ; sinon on retient la lecture la plus simple et on la consigne en doute. Chaque décision est justifiée dans `index.json` (champ `sauts_de_page`).
7. Caractères : rien n'est corrigé. Fautes, guillemets droits, tirets (« — », « – », « -- »), symboles et variables de gabarit (`{n}`, `{{ }}`, `<score>`, `[quantity]`…) restent tels quels. Les glyphes composés en police mathématique sont gardés tels que pdftotext les décode (± × α β δ ε η λ σ → ∈ √ ∝ ∞ ∼ ≤ ≥). Seule exception, dans I3 : les chiffres composés en indice ou en exposant sont rendus par les caractères Unicode correspondants (β₁, β₂, H₁, σ²), et la fraction empilée 1 sur 2 par « ½ ». Chaque cas est listé dans `index.json`.
8. Ligatures : aucune dans le texte extrait de ces pages (ni dans les blocs, ni dans le texte des auteurs). La normalisation est prévue mais sans effet ici.

Retraits (détail par invite dans `index.json`, champ `retraits`) : 579 marqueurs « ,→ » dans les 18 blocs (698 sur l'ensemble des pages lues, autres blocs compris) ; les numéros de page placés entre deux parties d'un bloc ; pour H1, la note de bas de page n° 3 (p. 25), les deux pages de figures 26 et 27, l'algorithme 1 et le tableau 3 (p. 28) ; les lignes « ``` » qui encadrent H1-format et H1-classification ; les étiquettes des auteurs autour des blocs de H.13.

## Vérification (scripts/verifier.py)

Commande : `python3 -I scripts/verifier.py > verification.txt` (lancée depuis n'importe quel dossier ; elle lit `index.json` et `invites/`, n'utilise que pdftotext et la bibliothèque standard). Le script vérifie d'abord l'empreinte du PDF, puis pour chaque invite l'empreinte du fichier et la fin de ligne finale unique. Code de sortie 0 seulement si tout est conforme.

**Contrôle A — contenu (exigé).** Le texte des pages citées est extrait à nouveau par `pdftotext -f N -l N` (mode par défaut). Les deux côtés sont normalisés de la même façon :

1. ligatures ﬀ ﬁ ﬂ ﬃ ﬄ ﬅ ﬆ remplacées par leurs lettres ;
2. « , » suivi de « → » (avec ou sans blancs entre les deux) remplacé par une espace ;
3. toute suite de blancs ASCII (espace, tabulation, retours, saut de page) réduite à une espace ; bords rognés.

Côté PDF, on retire d'abord le numéro de page (la dernière ligne isolée égale au numéro ; sur la page 41, pdftotext la place avant la dernière ligne, le journal le signale), puis les intrusions déclarées dans `index.json` (page entière, ou passage borné par un début et une fin uniques sur la page). Côté transcription, on applique les substitutions déclarées (voir plus bas). On exige alors que « contexte avant + transcription + contexte après » figure tel quel dans le texte des pages. C'est une correspondance exacte, en entier et dans l'ordre, pas une similarité. Les deux contextes (fin de la phrase d'introduction ou étiquette, titre de la section suivante ou étiquette suivante) prouvent qu'il ne manque rien au début ni à la fin. Pour I8, le contexte après est la fin du document. En cas d'écart, le script imprime la position et le contexte du premier écart des deux côtés.

Substitutions déclarées (7 au total, toutes justifiées dans `index.json`, chacune doit s'appliquer au moins une fois) :

- H4 : « ---␤␤## Output Format » vers « --## Output Format ». En mode par défaut, pdftotext prend le dernier « - » de la ligne « --- » pour un trait d'union de fin de ligne : il le supprime et colle la ligne suivante. « --- » seul sur sa ligne est confirmé par `pdftotext -bbox`, `pdftotext -layout` et le contrôle B.
- I3 : les chiffres en indice ou en exposant et la fraction sortent de pdftotext en chiffres simples entourés d'espaces : « (β₁=0.9, β₂=0.999, » vers « (β 1 =0.9, β 2 =0.999, » ; « "H₁: [quantity] » vers « "H1 : [quantity] » ; « disproving H₁ » vers « disproving H1 » ; « R(D)=½log(σ²/D). » vers « R(D)= 12 log(σ 2 /D). » ; le radical est séparé : « √N » vers « √ N » ; après un passage en italique, la petite marge de LaTeX (1,7 pt, 0,4 chasse) est lue comme une espace : « r_eff/d » vers « r_ eff/d ».

**Contrôle B — structure (complément).** Le contrôle A ne voit pas les blancs (il les réduit). Le contrôle B les vérifie par une voie indépendante de la construction : les positions des mots données par `pdftotext -bbox` (et non le XML de pdftohtml). Dans les zones déclarées, il reconstruit les lignes sur la grille à chasse fixe : retraits et espaces, lignes de continuation recollées, lignes vides d'après l'écart vertical, lignes vides aux changements de page d'après les valeurs déclarées. Les chiffres en indice, en exposant ou en fraction sont comparés en chiffres simples (₁ vers 1, ² vers 2, ½ vers 12). Le texte reconstruit doit être identique, caractère pour caractère, au fichier.

**Test du vérificateur (scripts/tester_verifier.py).** Sur des copies (les vraies transcriptions ne sont pas touchées), on altère un fichier et on relance le vérificateur. Résultat (`test-verificateur.txt`) : cas sain accepté ; mot changé, première ou dernière phrase tronquée, guillemet droit remplacé par un guillemet courbe, deux lignes interverties : détectés par A et B ; ligne vide supprimée, retrait modifié, double espace réduite, retour à la ligne à la place d'une espace : détectés par B ; indice remplacé par un chiffre simple : détecté par A ; fin de ligne doublée : détectée. 12 cas sur 12 conformes à l'attente.

## Résultat de la vérification

```
sha256 : aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a (conforme)
Outil  : pdftotext version 24.02.0 ; Python 3.11.15
== H1 (H.1, p. 25-28) : CONFORME
== H1-format (H.11 (sections fixes ajoutées au générateur), p. 40-40) : CONFORME
== H1-classification (H.11 (sections fixes ajoutées au générateur), p. 41-41) : CONFORME
== H2 (H.2, p. 28-29) : CONFORME
== H3 (H.3, p. 29-29) : CONFORME
== H4 (H.4, p. 29-34) : CONFORME
== H5 (H.5, p. 34-35) : CONFORME
== H6 (H.6, p. 35-36) : CONFORME
== H9 (H.9, p. 37-38) : CONFORME
== H10 (H.10, p. 38-39) : CONFORME
== H12 (H.12, p. 43-43) : CONFORME
== H13-noyaux-systeme (H.13 (1/4), p. 43-43) : CONFORME
== H13-noyaux-utilisateur (H.13 (2/4), p. 43-43) : CONFORME
== H13-expansion-systeme (H.13 (3/4), p. 43-44) : CONFORME
== H13-expansion-utilisateur (H.13 (4/4), p. 44-44) : CONFORME
== I3 (I.3, p. 54-57) : CONFORME
== I7 (I.7, p. 66-68) : CONFORME
== I8 (I.8, p. 69-71) : CONFORME
BILAN : 18/18 invites conformes
```

Chaque invite est conforme aux deux contrôles (A et B), avec empreinte et fin de ligne conformes. Le détail (retraits appliqués, substitutions, nombre de lignes) est dans `verification.txt`. Au premier passage, 16 invites sur 18 étaient déjà conformes ; H4 et I3 l'ont été après déclaration des 7 substitutions ci-dessus (essais conservés dans `extrait/essais/`).

Recoupement indépendant : la fin de l'invite I.3 (p. 57) est identique, caractère pour caractère, à H1-format, deux lignes vides, puis H1-classification (p. 40-41).

## Élisions

Aucune mention d'élision dans les blocs transcrits. Les « ... » présents (exemples JSON de H9 et H13-noyaux-utilisateur, « what about...? » dans H4, « {{A1}: ..., A2: ...} » dans I3, etc.) font partie des invites. Les élisions de l'article se trouvent dans H.11 (« _26 score lines elided._ », « _[full prompt body elided — 9084 chars]_ »…) et H.14 (« … chars omitted._ »), qui ne font pas partie des invites demandées.

## Doutes

Lignes vides à un changement de page (la place libre en bas de page ne permet pas de trancher ; lecture la plus simple retenue) :

1. H4, p. 30 vers 31 : 0 ligne vide retenue (0 à 3 possibles) ; les niveaux d'un critère se suivent sans ligne vide partout ailleurs.
2. H4, p. 32 vers 33 : 0 retenue (0 à 3 possibles) ; même raison.
3. H6, p. 35 vers 36 : 1 retenue (0 ou 1 possible) ; nouveau paragraphe, et le même passage de H.2 porte une ligne vide visible.
4. I3, p. 55 vers 56 : 0 retenue (0 ou 1 possible) ; éléments numérotés consécutifs.
5. I7, p. 66 vers 67 : 1 retenue (0 ou 1 possible) ; nouveau paragraphe, et tous les paragraphes de cette invite sont séparés par une ligne vide.
6. I8, p. 69 vers 70 : 0 retenue (0 à 4 possibles) ; niveaux d'un critère consécutifs.

Invite I.3 (formules) :

7. « σ^ » et « β^ » : le PDF montre un « ^ » collé après la lettre grecque, dans la police du texte. L'original portait peut-être une lettre surmontée d'un accent (σ̂, β̂). Transcrit tel que visible.
8. β₁, β₂, H₁ (deux fois), σ², ½ : composés en mode mathématique dans le PDF, rendus par les caractères Unicode correspondants. L'original contenait probablement ces caractères, mais le PDF ne permet pas de le prouver.
9. « {{A1}: ..., A2: ...} » : transcrit tel qu'imprimé (probable reste d'échappement de gabarit), sans correction.
10. « √N » : le trait horizontal du radical est un filet graphique, pas du texte.

Lignes vides établies par mesure (pas des doutes, mais des déductions ; détail dans `index.json`) :

- H1, entre « …where things might fail. » (p. 25) et « Number your proposals… » (p. 28) : **1 ligne vide**. La page 25 est pleine (note de bas de page). Sur la page 28, la ligne de base de « Number your proposals… » est à 516,65 pt, soit 40,1 pt sous le filet bas du tableau 3 (476,6 pt, mesuré sur un rendu de la page à 300 dpi). Sans ligne vide, on attendrait 20 pt (séparation flottant-texte) + 10 pt (`\topskip`) = 30 pt. L'excédent, environ 10 pt, vaut une ligne de verbatim (9,85 pt). La page 28 est pleine (la ligne vide suivante de H.2 est reportée en haut de la page 29), donc l'écart n'est pas un étirement.
- I3, entre « …by standard ML analysis. » (p. 56) et « P9: FORMAL THEOREM » (p. 57) : **2 lignes vides**. Il reste deux places en bas de la page 56 et la ligne suivante n'en occupe qu'une : avec 0 ou 1 ligne vide, TeX l'aurait placée en page 56 ; avec 3, la troisième serait en haut de la page 57, qui commence à la position normale.
- H4 (p. 33 vers 34) et I8 (p. 70 vers 71) : 1 ligne vide, même raisonnement.
- H2 (p. 28-29), H9 (p. 37-38), I3 (p. 54-55), I7 (p. 67-68) : 1 ligne vide, visible en haut de la page suivante.

## Remarques utiles

- Fautes et bizarreries de l'original conservées, par exemple dans H12 : « score of a 100 -- to extreme complete that they were », « high-grained scores », et la double espace « and␣␣score ».
- H10 : les « \_ » (barre oblique inverse devant le tiret bas) du format de sortie sont imprimés ainsi ; conservés.
- H9 : les retraits du JSON valent 2, 4 et 8 espaces sur la grille ; `pdftotext -layout` affiche à tort 5 au lieu de 4.
- I7 : les « *…* » sont les balises markdown d'origine (rendues en italique dans le PDF) ; conservées.

## Réserves

- La fidélité est établie par rapport au PDF, pas par rapport aux invites réellement utilisées dans les expériences : l'article peut les avoir mises en forme pour la publication.
- Toutes les extractions passent par poppler (pdftotext, pdftohtml, version 24.02.0). Une erreur de la table de correspondance glyphe-caractère du PDF serait commune à toutes les voies. La relecture visuelle n'a rien montré de tel.
- Le contrôle B confirme les lignes vides déclarées aux changements de page ; il ne tranche pas les 6 cas indécidables listés plus haut.
- Le recollement d'une ligne coupée par une seule espace est une règle (justifiée par les 698 coupures). Une double espace qui tomberait exactement sur une coupure serait invisible.
- Les espaces de fin de ligne sont invisibles dans le PDF ; les transcriptions n'en ont pas.
- La représentation de β₁, β₂, H₁, σ² et ½ par des caractères Unicode est un choix (doute 8).

## Reproduire

```
ESPACE=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/t05-invites
PDF=/home/user/controle-ia/docs/sources/pdf/2606.08892v2.pdf
python3 -I $ESPACE/scripts/construire.py $PDF $ESPACE              # reconstruit invites/ et index.json
python3 -I $ESPACE/scripts/verifier.py > $ESPACE/verification.txt  # vérifie (code 0 si tout est conforme)
python3 -I $ESPACE/scripts/tester_verifier.py $ESPACE              # teste le vérificateur
```

La reconstruction redonne des fichiers identiques octet pour octet (le script signale toute différence avec un fichier existant). La mesure du filet du tableau 3 se refait avec `pdftoppm -f 28 -l 28 -r 300 -gray $PDF rendu` puis `python3 -I scripts/filets.py rendu-28.pgm 300 440 530`.
