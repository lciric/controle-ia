# Gabarits d'invites publiés dans « TRACE » (annexe B) — transcription vérifiée

## En bref

- **Source** : `/home/user/controle-ia/docs/sources/pdf/2606.07054v1.pdf`.
  - Article : « TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents » (Mittapalli et al.), arXiv 2606.07054v1, 18 pages.
  - Empreinte sha256 vérifiée avant tout travail : `9e169bb5eced6fb2079c14804efcda54ad5e4a4ab9392b6c3b148c4ea6405fee`, conforme à l'empreinte attendue.
- **7 gabarits transcrits**, tirés de l'annexe B « TRACE Monitor Prompt Templates », pages 12 et 13 :
  - triage (B.1) ;
  - investigation, c'est-à-dire le contrôleur qui choisit l'action (B.2) ;
  - quatre actions : InspectStep (B.3.1), CompareSteps (B.3.2), CheckPolicy (B.3.3), AnalyzeDecisions (B.3.4) ;
  - verdict (B.4).

  Le document ne contient pas d'autre encadré d'invite.
- **Vérification par script : 7 gabarits sur 7 conformes**, au contrôle de contenu (A) et au contrôle de structure (B), avec empreinte et fin de ligne conformes (`verification.txt`).
- **Test du vérificateur : 33 cas sur 33 conformes à l'attente** (`test-verificateur.txt`).
  - Le cas sain est accepté.
  - Les 15 transcriptions altérées et les 7 déclarations altérées sont toutes refusées.
  - La règle de classement des lignes a été testée sur 10 lignes, artefacts et lignes réelles.
- **Recoupement par une troisième voie d'extraction** (`pdftotext -raw`) : les 7 gabarits sont retrouvés.
- **Aucune élision** dans les gabarits.
- **Doutes : 3 propres à un gabarit et 4 communs** (détail plus bas) :
  1. B.1 : « Intent: ...Scope: ... » est imprimé sans espace entre « ... » et « Scope: » ;
  2. B.1 : « Local window » et « Pattern window » sont en gras, et le gras n'est pas transcrit ;
  3. B.3.3 : dans « monitor-targeted », le trait d'union de fin de ligne est gardé (mot composé probable) ;
  4. apostrophes « ’ » (7) : probablement « ' » dans l'original ;
  5. tirets « – » dans les intervalles de nombres (9) : peut-être « - » dans l'original ;
  6. puces « • » (6) : la marque de liste de l'original est inconnue ;
  7. structure des lignes : le PDF (Portable Document Format) ne montre ni les lignes vides ni les retours à la ligne internes de l'invite d'origine.
- Le PDF a été traité comme une donnée : il n'a été lu que par `pdftotext` et `pdftohtml`. Rien n'a été modifié sous `/home/user/controle-ia`.

## Fichiers

```
invites-trace-v1/
  LISEZMOI.md (+ .sha256)            ce fichier
  invites/<id>.txt (+ .sha256)       les 7 transcriptions : B1, B2, B3-1, B3-2, B3-3, B3-4, B4
                                     (UTF-8, une seule fin de ligne finale)
  index.json (+ .sha256)             source, outils, méthode, géométrie mesurée, doutes communs ; pour chaque gabarit :
                                     section, titre, titre de l'encadré, pages et colonnes, caractères, octets, lignes,
                                     sha256, retraits, normalisations (césures, ligatures, guillemets, listes), doutes,
                                     élisions, remarques, passages de colonne, bords du bloc, données de vérification
                                     (bornes et substitutions du contrôle A, zones du contrôle B)
  verification.txt (+ .sha256)       sortie de scripts/verifier.py
  test-verificateur.txt (+ .sha256)  sortie de scripts/tester_verifier.py
  scripts/ (chaque fichier + .sha256)
    construire.py                    construction (voie pdftohtml -xml)
    config_invites.json              segments, décisions non mécaniques et leurs justifications, doutes, bornes
    verifier.py                      vérification (contrôles A et B, voie pdftotext)
    tester_verifier.py               test du vérificateur
    recoupement_raw.py               recoupement par pdftotext -raw (diagnostic)
    lignes_bbox.py                   diagnostic : lignes et espaces mesurées (pdftotext -bbox)
  extrait/                           extraits du PDF (empreintes : extrait/empreintes.sha256)
    texte/                           pdftotext par page, pages 11 à 14, mode par défaut et -layout
    xml/                             pdftohtml -xml, pages 11 à 13 (XML : Extensible Markup Language)
    bbox/                            pdftotext -bbox, pages 12 et 13
    construction.json                journal de construction : lignes physiques, césures, bords
    recoupement-raw.txt              sortie de scripts/recoupement_raw.py
    essais/                          sorties intermédiaires de la vérification et du test (voir « Historique »)
```

## Les gabarits

| Fichier | Section et titre | Titre de l'encadré | Emplacement | Caractères | Lignes (PDF → transcrites) | sha256 (16 premiers) | Doutes |
|---|---|---|---|---|---|---|---|
| `invites/B1.txt` | B.1 — Triage Prompt (Phase 1) | Triage Prompt | p. 12, colonne gauche | 1288 | 38 → 11 | `d6f532d003f25278` | 6 |
| `invites/B2.txt` | B.2 — Investigation Prompt (Phase 2) | Investigation Prompt | p. 12, colonne gauche puis droite | 866 | 25 → 12 | `b4a0fc6c2b2570bf` | 1 |
| `invites/B3-1.txt` | B.3.1 — InspectStep | InspectStep | p. 12, colonne droite | 561 | 17 → 8 | `6b2b23477e56ad1f` | 3 |
| `invites/B3-2.txt` | B.3.2 — CompareSteps | CompareSteps | p. 13, colonne gauche | 352 | 11 → 6 | `53a39114e3e114e5` | 3 |
| `invites/B3-3.txt` | B.3.3 — CheckPolicy | CheckPolicy | p. 13, colonne gauche | 447 | 13 → 6 | `9240dfdfa24600d3` | 2 |
| `invites/B3-4.txt` | B.3.4 — AnalyzeDecisions | AnalyzeDecisions | p. 13, colonne gauche puis droite | 613 | 18 → 7 | `c91b45da094e0494` | 3 |
| `invites/B4.txt` | B.4 — Verdict Prompt (Phase 3) | Verdict Prompt | p. 13, colonne droite | 658 | 21 → 10 | `840d5a80d4273587` | 4 |

Lecture du tableau :
- « Doutes » compte les entrées du champ `doutes` de `index.json`, c'est-à-dire les doutes propres au gabarit et les doutes communs qui s'y appliquent.
- Les empreintes complètes sont dans `index.json` et dans les fichiers `.sha256`.
- « Caractères » compte les points de code Unicode, fins de ligne comprises.
- Les pages sont numérotées comme dans le fichier ; aucun numéro n'est imprimé sur les pages 12 et 13.

**Identifiants.** Ils suivent la numérotation de l'annexe : B1, B2, B3-1 à B3-4, B4, plutôt que B1 à B7. La section B.3 « Action Execution Prompts » n'a pas d'encadré propre : seulement un intitulé suivi de ses quatre sous-sections.

**Pas d'introduction.** L'annexe B ne contient aucune phrase des auteurs. Chaque sous-section est un intitulé suivi d'un encadré titré (titre blanc sur bandeau). Le champ `introduction` est donc vide. Ni les intitulés ni les titres d'encadré ne sont transcrits ; ils figurent dans `index.json`.

## Ce que la transcription restitue

Les gabarits ne sont pas en police à chasse fixe. Ils sont composés en Times, en paragraphes justifiés à la largeur de la colonne, avec des césures. Les retours à la ligne du PDF viennent donc de la composition, pas de l'invite d'origine.

Convention retenue :
- **Une ligne transcrite = un paragraphe du PDF** (ou une ligne terminée par un retour forcé). Les lignes de composition sont recollées par une espace simple : 143 lignes physiques donnent 60 lignes transcrites.
- **Césures résolues.** 19 traits d'union de fin de ligne sont retirés (liste par gabarit dans `index.json`). Un seul est conservé : « monitor-targeted » (B.3.3).
- **Listes.** Chaque élément est sur sa ligne et commence par « • » suivi d'une espace. Le retrait de la liste n'est pas transcrit.
- **Aucune ligne vide.** Le PDF n'en montre aucune dans les encadrés. Les écarts verticaux sont réguliers : 13,55 pt entre deux lignes, 15,54 pt autour des listes.
- **Caractères tels qu'imprimés, rien n'est corrigé** :
  - guillemets droits « " » (50), apostrophes « ’ » (7), tirets demi-cadratins « – » (9), puces « • » (6) ;
  - « ... », « {} », « <step_index> » ; « [19,20] » sans espace après la virgule.
- **Ligatures.** Aucune dans le texte extrait : les deux outils rendent déjà les lettres.

Points établis par mesure sur les positions des mots (`pdftotext -bbox`). Ce ne sont pas des doutes :
- **Espaces avant les deux-points** (« STEP 1 : », « InspectStep : », « Done : »…) : ce sont de vraies espaces. Dans les lignes justifiées, elles sont étirées comme les autres espaces de la ligne (par exemple 8,16 pt dans « STEP 2 : IDENTIFY PERMITTED »).
- **B.2, passage de colonne (p. 12).** « WHY THIS WINDOW WAS FLAGGED: » termine la colonne gauche. C'est une ligne justifiée : ses espaces mesurent 2,849 pt au lieu de 2,727, et elle finit à la marge. Le paragraphe continue donc par « {reason} » en haut de la colonne droite.
- **B.3.4, passage de colonne (p. 13).** Césure « ob- » / « ject », d'où « object ».
- **B.2, InspectStep.** « InspectStep : … paired. Arguments: {"k": <step_index>} » forme un seul paragraphe, comme les quatre autres actions. La ligne « …tool results paired. » est justifiée : ses espaces mesurent 2,7298 pt, pas 2,7273.
- **B.3.1, fin de paragraphe.** La ligne « …behaviour the user would have objected to. » clôt un paragraphe :
  - elle finit à 508,56 pt, soit 2,17 pt avant la position d'une ligne justifiée terminée par un point ;
  - ses espaces ont exactement la largeur naturelle.

  « Return plain text only. » est donc une ligne à part, comme dans les trois autres actions.

## Méthode de transcription (scripts/construire.py)

Le texte n'est pas recopié à la main : il est reconstruit par script, puis relu en entier.

1. **Repérage des encadrés.** `pdftohtml -xml` (pages 12 et 13) donne chaque fragment de texte avec sa police, sa couleur et sa position, à 0,67 pt près (le zoom de pdftohtml est plafonné).
   - Le texte des encadrés et celui des auteurs sont dans la même police, NimbusRomNo9L (Times).
   - Un encadré se repère donc à son titre blanc et à sa marge gauche : 86,5 pt (colonne gauche) et 321,7 pt (colonne droite), contre 70,9 pt et 306,1 pt pour le texte des auteurs.
   - Le script s'arrête si une ligne du bloc sort de l'encadré, si le bloc n'est pas précédé du titre blanc attendu, ou s'il n'est pas suivi d'un intitulé ou du bas de la colonne.
2. **Lignes physiques.** Les fragments sont regroupés par ordonnée dans chaque colonne, et joints par une espace si leur écart dépasse 1 pt.
3. **Recollement.**
   - Une ligne finie par « - » est une césure : le trait d'union est retiré et le mot recollé, sauf pour un mot composé déclaré.
   - Une ligne pleine (qui finit à moins de 1,33 pt de la marge droite) est recollée à la suivante par une espace.
   - Une ligne courte termine la ligne transcrite.
   - Une seule décision n'est pas lisible à la résolution du XML : la ligne « behaviour the user would have objected to. » (B.3.1) y paraît pleine. Elle est déclarée fin de paragraphe dans `scripts/config_invites.json`, avec sa justification mesurée. Le contrôle B la retrouve de façon indépendante.
4. **Écarts verticaux.** Ils sont contrôlés : aucune ligne vide, aucun saut anormal.
5. **Caractères.** Le script recherche les caractères de contrôle, les espaces insécables, les traits d'union conditionnels et les ligatures : aucun trouvé. Il vérifie aussi l'absence de double espace.

## Vérification (scripts/verifier.py)

Commande : `python3 -I scripts/verifier.py > verification.txt`.
- Le script lit `index.json` et `invites/`, et n'utilise que pdftotext et la bibliothèque standard de Python.
- Il vérifie d'abord l'empreinte du PDF, puis, pour chaque gabarit, l'empreinte du fichier et l'unicité de la fin de ligne finale.
- Le code de sortie vaut 0 seulement si tout est conforme.

**Contrôle A — contenu.**
- *Extraction.* Le texte des pages 12 et 13 est extrait à nouveau par `pdftotext` en mode par défaut, colonne par colonne : un rognage isole la moitié gauche, puis la moitié droite de chaque page. Les morceaux sont mis bout à bout dans l'ordre de lecture.
  - Le rognage est nécessaire : sur la page entière, pdftotext entremêle les deux colonnes (page 13).
  - Le script vérifie qu'aucun mot n'est à cheval sur la séparation des colonnes.
- *Normalisation des deux côtés.* Les ligatures sont remplacées par leurs lettres, et toute suite de blancs est réduite à une espace.
- *Exigence.* « Contexte avant + transcription + contexte après » doit apparaître exactement une fois, tel quel.
  - Contexte avant : l'intitulé de section et le titre de l'encadré.
  - Contexte après : l'intitulé suivant (pour B.3.1, celui du haut de la page 13).
- *Césures.* pdftotext retire lui-même les traits d'union de fin de ligne : le contrôle A confirme donc les 19 césures.
- *Substitutions.* Deux substitutions sont déclarées (forme transcrite → forme produite par pdftotext), et chacune doit s'appliquer :
  - B.3.3 : « monitor-targeted » → « monitortargeted », car pdftotext retire aussi ce trait d'union de fin de ligne ;
  - B.3.4 : « reasonable user object if » → « reasonable user ob- ject if », car la césure tombe au passage de colonne et les colonnes sont extraites séparément.

**Contrôle B — structure.** Le contrôle A ne voit ni les blancs ni les retours à la ligne. Le contrôle B les vérifie par une voie indépendante de la construction : les positions des mots données par `pdftotext -bbox`. Il utilise ses propres constantes, mesurées sur le PDF, et une règle plus stricte, sans reprendre la décision déclarée :
- *Césure* : une ligne finie par « - » et pleine. Le trait d'union est retiré, sauf mot composé déclaré.
- *Ligne justifiée* : elle finit à la marge droite de l'encadré (à 0,05 pt près) et ses espaces diffèrent de la largeur naturelle. Elle est recollée à la suivante par une espace.
- *Fin de paragraphe* : une ligne courte dont toutes les espaces ont exactement la largeur naturelle, à 0,0006 pt près (2,72727 pt, ou 3,38182 pt après une ponctuation forte).
- *Tout autre cas* : ligne indécidable, et le gabarit est non conforme. La dernière ligne d'un gabarit doit être une fin de paragraphe.

Le contrôle B vérifie aussi :
- les bords des zones : titre blanc juste au-dessus ; intitulé ou bas de colonne en dessous ; haut de colonne au passage de colonne ;
- la marge gauche : aucun texte des auteurs dans la zone ;
- les écarts verticaux : 13,549 pt ou 15,545 pt, à 0,1 pt près.

Le texte reconstruit doit être identique, caractère pour caractère, à la transcription.

**Marges de la règle**, mesurées sur les 143 lignes physiques :
- Parmi les 63 lignes justifiées qui ne finissent pas par « - », l'espace la plus proche de la largeur naturelle s'en écarte de 0,0026 pt, soit 4 fois la tolérance.
- Parmi les 53 fins de paragraphe (dernières lignes des gabarits exclues), l'écart maximal à la largeur naturelle est de 0,000005 pt.
- La fin de paragraphe la plus proche de la marge droite en reste à 0,25 pt, soit 5 fois la tolérance.
- Aucune ligne indécidable.

**Test du vérificateur (scripts/tester_verifier.py).** Il travaille sur des copies, jamais sur les vrais fichiers. Résultat : 33 cas sur 33 conformes à l'attente.
- Le cas sain est accepté.
- Refusés par les contrôles A et B :
  - mot changé ;
  - ligne supprimée ;
  - espace ajoutée dans un mot ;
  - deux lignes interverties ;
  - premier mot retiré ;
  - dernier caractère retiré ;
  - césure réintroduite ;
  - trait d'union du mot composé retiré ;
  - « ’ » remplacé par « ' » ;
  - « – » remplacé par « - » ;
  - puce supprimée.
- Refusés par le contrôle B :
  - double espace ;
  - retour à la ligne à la place d'une espace ;
  - deux lignes fusionnées ;
  - fin de ligne finale doublée (aussi refusée par le contrôle de fin de ligne).
- Déclarations de l'index altérées, toutes refusées :
  - zone tronquée en haut, zone tronquée en bas, zone étendue jusqu'à l'intitulé suivant, zone de la colonne suivante omise (contrôle B) ;
  - trait d'union conservé non déclaré (contrôle B) ;
  - substitution du passage de colonne retirée (contrôle A) ;
  - empreinte fausse.
- Règle de classement des lignes, testée sur 10 lignes :
  - 3 cas sains et 1 cas limite, correctement classés ;
  - 4 artefacts déclarés indécidables : ligne pleine à espaces naturelles, ligne courte à espaces étirées, ligne courte finie par « - », espace décalée de 0,001 pt ;
  - 2 lignes réelles du PDF, bien classées.

**Recoupement (scripts/recoupement_raw.py, diagnostic).** Troisième voie d'extraction : `pdftotext -raw`, qui suit l'ordre du flux de contenu, sur les pages entières et sans rognage. Les traits d'union de fin de ligne y sont retirés, sauf pour le mot composé déclaré. Les 7 transcriptions s'y retrouvent, une fois chacune (`extrait/recoupement-raw.txt`).

**Historique.** Les transcriptions n'ont jamais changé au cours de la vérification.
1. Premier passage : le contrôle A était conforme pour les 7 gabarits. Le contrôle B refusait B.1, à cause d'une mesure du vérificateur : l'écart vertical prenait le haut de la boîte du premier mot de la ligne, et cette boîte est plus haute de 0,13 pt pour les mots en gras (« • Local window »). Le vérificateur prend désormais l'ordonnée médiane des mots de la ligne.
2. Ensuite, la règle de classement a été isolée dans une fonction testable, et une garde a été ajoutée : la dernière ligne d'un gabarit doit être une fin de paragraphe.

Les sorties intermédiaires sont dans `extrait/essais/`. La sortie du premier passage n'a pas été conservée.

## Résultat de la vérification

```
sha256 : 9e169bb5eced6fb2079c14804efcda54ad5e4a4ab9392b6c3b148c4ea6405fee (conforme)
Outil  : pdftotext version 24.02.0 ; Python 3.11.15
Colonnes : page 12 : aucun mot à cheval sur la séparation des colonnes (x = 298 pt)
Colonnes : page 13 : aucun mot à cheval sur la séparation des colonnes (x = 298 pt)
== B1 (B.1 Triage Prompt (Phase 1), p. 12-12) : CONFORME
== B2 (B.2 Investigation Prompt (Phase 2), p. 12-12) : CONFORME
== B3-1 (B.3.1 InspectStep, p. 12-12) : CONFORME
== B3-2 (B.3.2 CompareSteps, p. 13-13) : CONFORME
== B3-3 (B.3.3 CheckPolicy, p. 13-13) : CONFORME
== B3-4 (B.3.4 AnalyzeDecisions, p. 13-13) : CONFORME
== B4 (B.4 Verdict Prompt (Phase 3), p. 13-13) : CONFORME
BILAN : 7/7 gabarits conformes
```

Chaque gabarit est conforme aux deux contrôles (A et B), avec une empreinte et une fin de ligne conformes. Le détail (substitutions, bords, nombre de lignes recollées et de césures) est dans `verification.txt`.

## Élisions

Aucune. Les « ... » de B.1 (« Intent: ...Scope: ... », « "reason": "..." ») et de B.2 (« "..." », « [<index>, ...] ») sont imprimés dans les encadrés. Ce sont les marques de remplissage des exemples JSON (JavaScript Object Notation), pas des coupures faites par les auteurs.

## Doutes

Propres à un gabarit :

1. **B.1, « "Intent: ...Scope: ..." ».** Aucune espace n'est imprimée entre « ... » et « Scope: ».
   - pdftotext et pdftohtml en font un seul mot : l'écart est sous le seuil de coupure de mot (environ 1,1 pt), alors que la plus petite espace mesurée dans les encadrés vaut 2,08 pt.
   - L'invite d'origine portait peut-être une espace, ou un retour à la ligne (« \n ») dans la chaîne de l'exemple JSON.
   - Transcrit tel qu'imprimé.
2. **B.1, gras.** « Local window » et « Pattern window » sont composés en gras. L'invite d'origine portait peut-être un balisage (par exemple « **…** »). Le gras n'est pas transcrit.
3. **B.3.3, « monitor-targeted ».** Le trait d'union de fin de ligne est gardé, car c'est un adjectif composé. Une césure de « monitortargeted », qui n'est pas un mot, est improbable, mais le PDF ne permet pas de l'exclure.

Communs, consignés dans chaque gabarit concerné :

4. **Apostrophes « ’ »** (7 : une dans B.1, B.3.1 et B.3.2 ; deux dans B.3.4 et B.4). LaTeX compose « ' » en « ’ » : l'invite d'origine portait probablement « ' ».
5. **Tirets demi-cadratins « – »** (9 : 1–2, 1–3, 3–4, 3–8 dans B.1 ; 1–5 dans B.3.1, B.3.2 et B.3.4 ; 4–5 et 2–3 dans B.4). Ils viennent de « -- » ou de « – » dans la source LaTeX ; l'original portait peut-être « - ».
6. **Puces « • »** (6 : deux dans B.1, quatre dans B.4). Ce sont les marques de liste de LaTeX ; la marque de l'invite d'origine est inconnue.
7. **Structure des lignes** (tous les gabarits). Une ligne transcrite correspond à un paragraphe ou à un retour forcé du PDF. Les lignes vides et les retours à la ligne internes de l'invite d'origine, s'il y en avait, sont invisibles.

## Remarques

- Les titres d'encadré diffèrent parfois des intitulés de section : par exemple, l'encadré « Triage Prompt » suit l'intitulé « B.1 Triage Prompt (Phase 1) ».
- Page 11, en bas de la colonne droite (fin de l'annexe A) : une ligne de « = » déborde de la page. C'est un artefact de composition, hors de l'annexe B, non transcrit.

## Réserves

- **Fidélité au PDF, pas aux invites réellement utilisées.** Le code n'est pas publié. L'article a pu mettre les invites en forme pour la publication : justification, gras, puces, tirets.
- **Un seul outil d'extraction.** Toutes les voies passent par poppler 24.02.0 (pdftotext, pdftohtml). Une erreur de la table de correspondance entre glyphes et caractères du PDF serait donc commune à toutes. Il n'y a pas eu de relecture sur une image rendue de la page, la consigne limitant l'extraction à pdftotext et pdftohtml. Les trois voies textuelles concordent.
- **Hypothèses de la règle du contrôle B.** Elle repose sur le comportement de TeX (lignes justifiées étirées, espaces naturelles en fin de paragraphe) et du paquet microtype (débord de la ponctuation dans la marge). Ses marges sont mesurées plus haut.
- **Espaces de fin de ligne.** Elles sont invisibles dans le PDF ; les transcriptions n'en ont pas.

## Reproduire

```
ESPACE=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/invites-trace-v1
PDF=/home/user/controle-ia/docs/sources/pdf/2606.07054v1.pdf
python3 -I $ESPACE/scripts/construire.py $PDF $ESPACE                               # reconstruit invites/ et index.json
python3 -I $ESPACE/scripts/verifier.py > $ESPACE/verification.txt                   # vérifie (code 0 si tout est conforme)
python3 -I $ESPACE/scripts/tester_verifier.py $ESPACE > $ESPACE/test-verificateur.txt   # teste le vérificateur
python3 -I $ESPACE/scripts/recoupement_raw.py $ESPACE                               # recoupement par pdftotext -raw
```

La reconstruction redonne des fichiers identiques octet pour octet ; c'est vérifié, et le script signale toute différence.
