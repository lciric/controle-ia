# Contre-lecture 2 (différentiel) — procédure d'extraction de T0.5, v1, et son outillage — rapport v1

Contre-lecteur : sous-agent neuf. Il n'a rien écrit de ce qu'il relit et n'a pas fait la contre-lecture 1. Rapport du 2026-10-07, vers 05:30 UTC. Aucun fichier du dépôt n'a été modifié. Les essais ont tourné dans `…/scratchpad/contre-lecture-extraction-v2/essais/`, sur des dépôts jetables et des textes synthétiques ; aucun texte de papier n'a été lu. Les versions relues et les essais sont listés en annexe.

## Verdict

**Non scellable en l'état, mais scellable après trois corrections courtes, sans refonte.** Les 30 remarques sont traitées : 24 pleinement, 6 en partie, et les deux déclins sont acceptables. La machine d'états est juste sur tous les déroulés éprouvés, et les 62 gardes sont exercées.

Restent deux fautes nouvelles dans des fichiers qui seront scellés :
- **D-1** : le contrôle des formules rejette un énoncé qui cite deux montants en dollars dans deux paragraphes ;
- **D-2** : un « OK » mal rapporté par un seul sous-agent bloque toute la tentative, et aucune suite n'est écrite.

S'y ajoute une condition de lancement, **D-3** : tant que N-014 n'est pas tranché, les sorties irreproductibles vivent sur un disque éphémère, et aucune règle ne dit quoi faire en cas de perte.

Échelle, celle de la contre-lecture 1 :
- **bloquante** : la procédure scellée produirait en silence des données fausses ;
- **majeure** : à corriger ou à trancher avant le scellement, parce qu'un fichier scellé est touché ou qu'une garantie annoncée n'est pas tenue ;
- **mineure** : correction simple, avant le lancement ;
- **suggestion** : facultatif.

Les modules de décision sont épinglés dès l'ouverture du run. Toute correction de code, même mineure, doit donc précéder `preparer --tentative 1`.

## A. Les 30 remarques de la contre-lecture 1

Les lignes citées renvoient au texte final `docs/procedures/T0.5-extraction-v1.md` (« texte »), à `extraction.py` (« ex ») et à `extraire_t05.py` (« et »).

| remarque | état | justification |
|---|---|---|
| CL-1 | traitée | `anomalies_texte` (ex l. 69-84) s'applique aux trois sorties et aux avis (ex l. 110, 133, 186, 364). Même contrôle dans les deux scripts (l. 60-70 et 55-65). Consignes : l. 24 et l. 31. Tests d'accord sur \theta, \nabla et \beta. Fautes nouvelles introduites par la correction : D-1 et D-4. |
| CL-2 | traitée | Rondes nouvelles limitées aux papiers nommés et encore sans avis lisible (et l. 521-532 ; texte l. 148 et 164). Le test du dépôt s'arrête sur « audit R4 requis » (test l. 497-498). Mon déroulé s1 (avis refait, audit, assemblage) va jusqu'au bilan sans arrêt. |
| CL-3 | en partie | Le code désigne les papiers d'audit des deux côtés (et l. 439-447). Un échec à l'audit rend la reprise due (et l. 469-474). La réserve est inscrite au bilan (et l. 676). En revanche, l'accord n'est calculé que du côté propre : D-6. |
| CL-4 | traitée | Rondes numérotées par le code (et l. 496-498). `_rondes` arrête sur une ronde préparée et non lue, ou lue sans préparation (et l. 385-395). Deux tests. |
| CL-5 | traitée | Toutes les entrées sont empreintées (et l. 185-192, 238). Une entrée modifiée devient l'anomalie de son seul papier (et l. 313-315 et 579-580). Restauration interdite (texte l. 77). Consignes : l. 3. Un test. |
| CL-6 | traitée | Phrase de préséance dans l'invite fixe (et l. 43-45 ; texte l. 72). Le fait est déclaré (texte l. 75), mais sa portée est sous-estimée : D-12. |
| CL-7 | traitée | 62 gardes : 19 dans `extraction.py`, 43 dans `extraire_t05.py`. Mon traçage des lignes exécutées sur les 99 tests n'en trouve aucune non exercée. |
| CL-8 | en partie, déclin acceptable | Modules épinglés (et l. 62 et 84-85), contrôlés à chaque étape (et l. 131-136). Commit et propreté de l'arbre dans chaque résultat (et l. 126-128 et 140). Les dépendances de décision ne sont pas épinglées : D-8. Le déclin sur l'identifiant du modèle doit être reformulé : D-14. |
| CL-9 | traitée | Invite des cibles l. 5 et 12. Consigne du contre-vérificateur l. 13 (« follows prompt T's definition of its family »). |
| CL-10 | traitée | Motif 2 restreint (ex l. 374-378, testé). J'ai recalculé les probabilités du texte (l. 174) : 0,017, 0,079 et 0,37, justes. Les mots et un taux estimé sont discutables : D-18. |
| CL-11 | en partie | Archives scellées à chaque validation et à chaque lecture (et l. 327 et 601). L'assemblage lit les archives (et l. 684-696). La persistance n'est pas réglée : D-3. |
| CL-12 | traitée | Gardes avant le manifeste (et l. 251-269 ; testé). Tentatives 2 et 3 limitées exactement aux papiers dus (et l. 277-284). Seuil contrôlé dès la lecture (et l. 611-618). Ordre écrit (texte, section 7). |
| CL-13 | traitée | Retours exigés (et l. 195-204). « OK » face à une anomalie : arrêt (et l. 316-318 et 584-586). Relance comptée. Ce contrôle, recommandé par la contre-lecture 1, crée un arrêt global sans suite : D-2. |
| CL-14 | traitée | Identifiant textuel non vide (ex l. 166). `nombre_positif` sans dépassement (ex l. 139-146). Statuts exactement égaux au pilote et à la réserve (ex l. 474-475). |
| CL-15 | en partie | Plus aucune ligne coupée. Codes stables comparés en liste. Mais la lecture d'un avis donne `[avis.illisible]` là où le script donne `[fichier.absent]` ou `[json.illisible]`, et une partie de la typographie n'est jamais éprouvée : D-11. |
| CL-16 | en partie | Bilan élargi (et l. 713-736). Arrêts scellés (et l. 614-616 et 681). Il manque le dénominateur des cibles défectueuses, et les références nulles sont comptées par base : D-7. |
| CL-17 | traitée | Sections 1, 3 et 5. « Retrouvée » et « fondée » sont employés avec cohérence ; « ancré » a disparu. Mais trois renvois de section sont faux : D-9. |
| CL-18 | traitée | Section 0 : les cinq écarts manquants sont listés. |
| CL-19 | traitée | Fichier présent ; 403 parties, de 2 à 9 par papier, et ligne maximale de 3 775 caractères, conformes au résumé du fichier. Pas encore d'empreinte compagnon, provenance incomplète : D-19. |
| CL-20 | traitée | Parties de 25 000 caractères au plus, aucune coupe (ex l. 231-263). Mon essai avec l'outil de lecture des sous-agents rend entière une ligne de 4 000 caractères. |
| CL-21 | traitée | Même périmètre pour les deux bases (invite l. 7). Comparaison renvoyée au pilote (texte l. 135). |
| CL-22 | traitée | Invite l. 9 et 15. |
| CL-23 | traitée | N-014 porté à Lazar. Aucun texte de papier dans `diag/`, vérifié dans le code et sur un déroulé complet. Un canal résiduel subsiste : D-13. |
| CL-24 | traitée | Consigne de l'extracteur l. 19 et 21. |
| CL-25 | en partie, déclin acceptable | Rôle « theorie » et intervalle de Clopper-Pearson au bilan (et l. 731). La justification du déclin est surestimée : D-15. |
| CL-26 | traitée | Module ex l. 194-207, script l. 161-172, un test. |
| CL-27 | traitée | Table typographique (ex l. 29-30). Clés de H.10 à tiret bas échappé (ex l. 117-119). Les tests ne couvrent pas tout : D-11. |
| CL-28 | traitée | Texte, section 0, « Graine ». |
| CL-29 | traitée | Texte l. 71 et 36-39. |
| CL-30 | traitée | `citations_de_tableau` (et l. 637-648), compté au bilan. |

**Les deux déclins.**
- **CL-8, identifiant du modèle** : acceptable si deux points sont repris.
  - « Le même pour tous » (texte l. 213) est une hypothèse, pas un fait vérifié : la plateforme peut servir un modèle de repli.
  - La « règle de la plateforme » n'est sourcée nulle part dans le dépôt. Les lignes d'attribution des commits nomment déjà le modèle (« Co-Authored-By: Claude Opus 5.5 », sur les 20 derniers commits). Voir D-14.
- **CL-25, contre-vérification des 96 papiers** : acceptable. P-006 a fixé « sur échantillon », et la contre-lecture 1 n'en faisait qu'une option à proposer. La justification écrite dans le traitement est trop forte : D-15.

## B à D. Remarques nouvelles

### D-1 — majeure — faux positif du contrôle des formules : les montants en dollars

**Où**
- `verifier-sortie-v1.py` l. 24 et 66-68 ; `verifier-avis-v1.py` l. 17 et 61-63 ;
- `extraction.py` l. 39 et 80-83 ;
- consigne de l'extracteur l. 19 et 21.

**Problème**

Le motif `\$[^$]*\$` apparie le « $ » d'un montant avec le « $ » suivant, celui d'un autre montant ou d'une formule. Si un saut de paragraphe les sépare, l'énoncé, qui est une introduction réécrite en plusieurs paragraphes, est rejeté. Essai `essai_barres.py`, au module comme au script, sur trois énoncés :
- « …costs over $100M.\n\nLet $\\theta$ denote… » : `[texte.formule]` ;
- deux montants dans deux paragraphes : `[texte.formule]` ;
- les mêmes montants échappés en « \$ », comme le texte converti les porte souvent : `[texte.formule]`.

Les mêmes montants dans un seul paragraphe passent.

Le message envoie le sous-agent vers les barres obliques, qui ne sont pas en cause. Pour corriger, il doit retoucher l'énoncé, alors que la consigne (l. 21) limite les retouches à ce qui enfreint H.9. S'il applique l'exception de la l. 19 (« leave it »), le papier part en reprise, puis il est exclu.

Les papiers exposés sont ceux dont l'introduction chiffre des coûts en dollars, c'est-à-dire ceux qui intéressent le plus la famille « coût ». Le biais est faible en nombre, mais il est dirigé.

**Correction**, avant le scellement, dans les deux scripts, le module et les tests :
- ne compter qu'un saut de ligne suivi directement d'une minuscule (reste de \nabla, \nu, \neq, \not…), dans un segment `$…$` sans ligne vide ;
- compter aussi « \n » suivi de « abla » partout.

Mon essai de cette règle (`essai_regle_proposee.py`) : 0 faux positif sur les trois cas de dollars, et \nabla, \nu, \neq détectés, y compris \nabla dans `$$…$$`.

Compléter le message : « if the $ signs are amounts, not a formula, write the amounts without $ ».

Ajouter aux deux consignes : « an ERROR about formatting may be fixed by rephrasing, without changing the content ».

### D-2 — majeure — un « OK » rapporté face à une anomalie arrête toute la tentative, sans suite écrite

**Où**
- `extraire_t05.py` l. 316-318 (validation) et 584-586 (lecture d'une ronde) ;
- texte l. 116 ;
- consigne de l'extracteur l. 17-22 ; consigne du contre-vérificateur l. 31.

**Problème**

La cause la plus probable d'un « OK » face à une anomalie n'est pas un désaccord entre le script et le module, que les tests rendent improbable. C'est un sous-agent qui retouche ses sorties après son dernier contrôle, ou une ligne mal rapportée. Or la consigne invite à retoucher l'énoncé après un avertissement sans relancer le script : l. 20, aucun « run it again » dans ce cas.

Un seul sous-agent sur une centaine suffit alors à arrêter tout.

Essai s5 :
- la validation lève l'arrêt, et le refait à l'identique ;
- `echantillonner` répond « tentative 1 préparée et non validée » ;
- la tentative 2 est refusée, faute de résultat de validation.

Le run est bloqué, et le texte ne dit pas quoi faire ensuite. Sur un disque éphémère (D-3), attendre une décision équivaut à perdre les sorties.

Même chose pour une ronde (essai s18) : l'avis à refaire est refusé, avec « ronde(s) … préparée(s) et non lue(s) ».

Le contrôle est aussi asymétrique : un « NOT OK » face à zéro anomalie n'est pas vu.

**Correction**
- À la validation et à la lecture, le module exécute lui-même la copie scellée du script (`sys.executable -I docs/procedures/…/verifier-*-v1.py <dossier>`) et compare les deux listes de codes. Un écart est le vrai désaccord en production, et c'est lui qui arrête.
- La ligne rendue par le sous-agent est seulement consignée, dans les deux sens. Le papier en anomalie suit déjà la reprise, et l'avis en anomalie est déjà refait.
- Ajouter aux deux consignes : « After any change to an output file, run the checker again; reply with the last line of that final run. »
- Corriger le texte l. 116.

### D-3 — majeure, empêche de lancer, pas de rédiger — sorties irreproductibles sur un disque éphémère, sans règle de perte

**Où**
- texte l. 78 et 226-234 ;
- `extraire_t05.py` l. 143-153 et 163-175 ;
- proposition N-014, l. 18, 28 et 34-35.

**Problème**

Archives, détails et tâches assemblées n'existent que dans `donnees/<run>/`, ignoré par git et jamais poussé. Le dossier de travail vit dans le dossier temporaire de la session, propre à la session. Après l'assemblage, `taches-evaluation.json` y est la seule copie de l'instrument : énoncés et cibles.

La proposition N-014 le dit elle-même :
- « le disque de la session est éphémère ; il est repris quand la session se termine ou reste inactive » ;
- option sans exception : « perte probable à la fin de la session » ;
- et pourtant, en attendant la réponse, « l'extraction tourne ».

En cas de perte, `diag/` renvoie à des archives absentes, et chaque étape suivante s'arrête sur « fichier absent ». Aucune règle ne dit s'il faut abandonner, relancer, ni sous quel nom. C'est exactement le risque de CL-11 : refaire un tirage après avoir vu des codes et des avis.

**Correction**

Au choix :
1. lancer après la décision N-014 (recommandé) ;
2. écrire dans le texte :
   - le run va de la tentative 1 à l'assemblage dans une seule session qui reste active ;
   - toute perte de `donnees/<run>/` ou du dossier de travail avant la copie dans le dépôt est un arrêt, consigné par un résultat scellé dans `diag/` ;
   - aucune sortie du run perdu n'est relue ;
   - un run nouveau, sous la même procédure, reprend à la tentative 1.

### D-4 — mineure — contrôle des barres obliques : faux négatif résiduel et messages sans position (scripts scellés)

**Où** : `verifier-sortie-v1.py` l. 64 et 68 ; `verifier-avis-v1.py` l. 59 et 63 ; `extraction.py` l. 77-78 et 82.

**Problème**
- `$$\nabla_\\theta L$$` et `$$a \neq b$$` se lisent sans erreur : l'énoncé lu contient un vrai saut de ligne suivi de « abla » (essai). Le motif `\$[^$]*\$` n'entre jamais dans `$$…$$`. Le cas est étroit : il faut qu'aucune autre commande à barre simple ne rende le fichier illisible.
- Le message de `texte.controle` affiche les 40 premiers caractères de la chaîne, pas l'endroit du caractère de contrôle. Essai : pour un \t non doublé vers le 1 550e caractère, le message montre « Mixture-of-experts models route tokens t ».
- `texte.formule` ne donne aucune position.
- Une tabulation copiée d'un tableau du papier produit le même message, qui parle de LaTeX.

**Correction**
- Avec la règle de D-1, \nabla est couvert partout. Déclarer le résidu restant (\neq, \nu dans `$$…$$`).
- Afficher environ 30 caractères autour de la première occurrence.
- Ajouter au message : « a tab copied from the paper can be replaced by a space ».

### D-5 — mineure — une tentative 3 « theory_only » exclut sans avis « theorie » un papier jamais classé théorique

**Où** : `extraction.py` l. 450-451 ; texte l. 122, 163 et 200.

**Problème** — Essai s4 :
- un papier classé « experiments_only » à la tentative 1, classification jugée juste par son contre-vérificateur ;
- en échec pour une fuite, il est repris ;
- sa tentative 3 dit « theory_only » : il est exclu, motif « theory_only (reprise) » ;
- aucune ronde n'est possible pour lui (« aucun papier à contre-vérifier » en rôle « reprise » comme en rôle « theorie »).

Le texte l. 200 dit qu'une exclusion « theory_only » n'est acquise qu'après son avis « theorie ». Le « de nouveau » de la l. 163 ne couvre pas ce cas.

**Correction** : écrire « toute tentative 3 classée « theory_only » exclut le papier, sans contre-vérification », ou faire passer ces papiers par une ronde « theorie » sur la tentative 3.

### D-6 — mineure — audit du côté sale : l'accord n'est jamais calculé (CL-3, point 3)

**Où** : `extraire_t05.py` l. 611-618 ; texte l. 166.

**Problème** : après l'arrêt de seuil, la ronde d'audit se prépare et se lit, mais rien ne calcule l'accord entre l'audit et l'échantillon. Essai s6 : aucun « accord » dans `diag/`, et l'assemblage s'arrête avant.

**Correction** : à la lecture d'une ronde « audit » ouverte après l'arrêt de seuil, écrire un résultat scellé d'accord, comme du côté propre (et l. 672-676).

### D-7 — mineure — bilan en deçà du texte

**Où** : `extraire_t05.py` l. 700-701, 713-724 et 732 ; texte l. 135 et 181.

**Problème**
- « Cibles défectueuses sur cibles contrôlées » (l. 181) : le bilan ne donne que le numérateur.
- « Nombre de références par base » (l. 135) : `compte["base"]` compte aussi les références nulles. Essai s19 : 6 références nulles comptées en « estimated ».
- Les désaccords de classification mêlent les avis « echantillon », « audit » et « reprise ».

**Correction** : ajouter le dénominateur, compter les bases sur les seules références non nulles, et ventiler les désaccords par rôle.

### D-8 — mineure — dépendances de décision non épinglées

**Où** : `extraire_t05.py` l. 62 ; `extraction.py` l. 23 et 374.

**Problème** : l'échelle du motif 2 est l'ordre des clés de `propositions.TYPES_PAPIER`, et le tirage passe par `manifeste.generateur`. Ni `propositions.py`, qui appartient au code du pilote, en chantier, ni `manifeste.py` ne sont épinglés. Le commit est consigné, mais il n'arrête rien.

**Correction** : ajouter ces deux fichiers à `Chemins.modules`, ou copier les deux constantes dans `extraction.py`.

### D-9 — mineure — renvois faux

**Où** : texte l. 6, 41, 122 et 124 ; `extraction.py` l. 32 et 368.

**Problème**
- « (section 5) » aux l. 41, 122 et 124 désigne la contre-vérification, qui est la section 6.
- La l. 6 renvoie au « registre des décisions » au lieu du fichier `contre-lecture/traitement-contre-lecture-1-v1.md`, qui existe et sera scellé.
- Docstrings : « section 2 » doit devenir 3, « section 5 » doit devenir 6.

**Correction** : corriger les cinq renvois.

### D-10 — mineure — écritures non atomiques : un échec entre l'archive et le résultat bloque l'étape pour toujours (R12)

**Où** : `extraire_t05.py` l. 148-152, 165-166, 327-334, 601-610 et 709-737 ; `extraction.py` l. 69-84.

**Problème**
- Si une exception survient après `archiver` ou `ecrire_donnees` et avant `_ecrire`, l'étape ne se refait plus : « existe déjà ».
- Cas concret : un substitut isolé (`\ud835`) passe `anomalies_texte`. `write_text` lève ensuite une erreur d'encodage et laisse un fichier vide (essai : taille 0), qui bloque l'étape.
- Les octets sont lus deux fois : une fois pour l'empreinte, une fois pour l'archive (et l. 322 ; et l. 575-576).

**Correction**
- Refuser les substituts dans `anomalies_texte` et dans les scripts.
- Rendre `archiver` et `ecrire_donnees` idempotents sur un contenu identique (leurs sorties sont déterministes), à la manière de `sceller`, ou écrire sous un nom provisoire puis renommer.
- Archiver les octets mêmes qui ont été empreintés.

### D-11 — mineure — tests d'accord incomplets

**Où** : `tests/test_extraire_t05.py` l. 131, 136, 171, 211 et 216 ; `extraire_t05.py` l. 578.

**Problème**
- Le script ne voit passer que l'espace insécable et U+2212 (l. 136). Guillemets et tirets typographiques n'y passent jamais. U+2010 à U+2012 et U+00AD ne sont éprouvés nulle part (CL-15, CL-27).
- L'attente `"calcul 1000000000"` (l. 171) est morte : le cas s'appelle `calcul 100000000000` (l. 131).
- Les codes « absent » et « illisible » des avis sont écrits à la main (l. 211 et 216). La vraie lecture rend `[avis.illisible]` (et l. 578), là où le script rend `[fichier.absent]` ou `[json.illisible]`. « Mêmes codes » est donc faux sur ce chemin.

**Correction** : ajouter ces cas, corriger la clé, et aligner les codes, ou déclarer l'écart.

### D-12 — mineure — isolement : le fait déclaré sous-estime ce que révèle `CLAUDE.md`

**Où** : texte l. 75.

**Problème** : le texte dit que se devine « le but général (juger des plans d'expériences) ». Or `CLAUDE.md` nomme le programme « Contrôle boîte blanche des menaces diffuses », terme qui désigne en contrôle de l'intelligence artificielle le sabotage diffus. La contre-lecture 1 écrivait : « le but, mesurer un sabotage de recherche, se devine ».

**Correction** : aligner la déclaration. Suggestion : ajouter « Write all answers in English » aux consignes, puisque `CLAUDE.md` dit « Langue : français ».

### D-13 — mineure — retours : du texte libre entre dans `diag/`

**Où** : `extraire_t05.py` l. 195-204, 325 et 571.

**Problème** : `derniere_ligne` est une chaîne libre, recopiée dans `diag/`. Un sous-agent qui répond hors format (« I could not find a third control: the paper only… ») y fait entrer du texte du papier, ce que N-014 et la section 8 excluent. Les retours acceptent aussi des clés libres.

**Correction**
- Exiger le format `^(NOT )?OK: \d+ error\(s\)` ; à défaut, inscrire le code `retour.hors_format` dans `diag/` et la ligne brute dans `donnees/`.
- Limiter les retours à leurs deux clés.

### D-14 — mineure — déclin de CL-8 : formulation

**Où** : texte l. 213.

**Problème** : « c'est le modèle de la session, le même pour tous » est une hypothèse. La règle invoquée n'est pas sourcée dans le dépôt, alors que les commits nomment déjà le modèle.

**Correction**
- Écrire « supposé identique (sous-agents lancés sans choix de modèle) ».
- Consigner à chaque étape un booléen « repli de modèle constaté », lu dans les événements de la session, sans écrire l'identifiant si la règle existe.

### D-15 — suggestion — justification du déclin de CL-25 ; contournement de la fuite mécanique

**Où** : `traitement-contre-lecture-1-v1.md` (ligne de CL-25) ; message de `h9.fuite_citation`.

**Problème**
- La fuite mécanique ne couvre que la reprise mot pour mot, sur 8 mots, des 1 à 3 citations de directions fécondes. Elle ne « couvre » pas les 96 papiers.
- L'extracteur voit le contrôle et peut le satisfaire en changeant de citation plutôt que d'énoncé.

**Correction** : ramener la phrase à ce qu'elle garantit, et ajouter au message « edit the statement, not the quote ».

### D-16 — suggestion — relances et avis refaits sans borne

**Où** : texte l. 117 et 164.

**Problème**
- Aucune borne, ni aux relances ni aux avis refaits.
- La l. 117 ne parle que de « tentative ». Pour un contre-vérificateur en panne sans avis, deux chemins existent : relance dans la même ronde, ou avis illisible refait dans une ronde nouvelle.

**Correction** : écrire « même tentative ou même ronde », et borner, par exemple deux avis refaits, puis arrêt.

### D-17 — suggestion — R4 du côté sale à la validation

**Problème** : aucun seuil sur les invalides de la tentative 1 ni sur les exclusions de la tentative 2. Un faux positif systématique, comme D-1, userait la réserve avant l'arrêt « réserve épuisée » à l'assemblage.

**Correction** : un arrêt avec audit si plus de N papiers sont exclus après la tentative 2, avant `echantillonner`.

### D-18 — suggestion — section 6 : mots et taux

**Où** : texte l. 169 et 174.

**Problème**
- « Souvent » pour une probabilité de 0,37 : écrire « environ une fois sur trois ».
- Le taux de 5 % du motif 3 est sans doute optimiste depuis CL-9. Le contre-vérificateur juge désormais la conformité à la définition de la famille, et les ablations propres à la méthode, fréquentes dans les papiers, ne comptent plus. Le seuil n'a pas été recalé.
- Le « calcul de la session » n'est rattaché à aucun chemin (R6) : citer la formule ou un script.

### D-19 — suggestion — essai à blanc

**Où** : `essai-a-blanc-copie-de-lecture-v1.json`.

**Problème** : pas encore d'empreinte compagnon, ce qui est normal avant le scellement. Le fichier ne porte ni l'empreinte du corpus ni celle du code de découpage, ni le commit.

**Correction** : les ajouter, ou les citer dans le texte (l. 32).

## Réponses courtes aux questions B, C et D

**B. Fautes introduites.**
- **Machine d'états** : juste sur tous mes déroulés.
  - s1 : avis refait, audit, assemblage sans arrêt.
  - s12 : rondes « echantillon » et « theorie » parallèles, avis refait pendant que la ronde « theorie » n'est pas lue, assemblage juste.
  - s13 : seuil atteint par un avis refait, arrêt scellé.
  - Les gardes de `statut_papier` et de `reprises_dues` tiennent.
  - Fautes : D-2, D-5, D-6.
- **Assemblage** : juste ; bilan incomplet (D-7).
- **Rangement** : aucun texte de papier dans `diag/` ni dans les manifestes, par construction (champs relus un à un) et sur un déroulé complet. L'archive tar de la contre-lecture 1, versée dans `docs/`, ne contient que des fichiers synthétiques (vérifié). Canal résiduel : D-13.
- **Archives** : déterministes et scellées, relues contre l'empreinte de chaque sortie. Fragilité : D-10.
- **Épinglage** : D-8.
- **Accord des scripts et du module** : codes identiques sur tous les cas des tests (D-11 pour les manques).
- **Copie de lecture** : juste, la concaténation est le texte (garde).
- **Fuite mécanique** : D-15.
- **Barres obliques** : faux positifs probables, D-1 ; faux négatif résiduel, D-4.
- **Classification (motif 2)** : conforme au texte et testée.
- **Seuil et audit** : conformes, sauf D-6.

**C. Texte et code.** Ils disent la même chose, sauf D-5, D-6, D-7 et D-9.
- Chiffres vérifiés :
  - empreintes 57f0aa47, 8f43dcae, 6fe36296, 15a3d48b et 9cced274 : justes ;
  - 403 parties, de 2 à 9 par papier, ligne maximale de 3 775 caractères : conformes au fichier ;
  - probabilités 0,017, 0,079 et 0,37 : recalculées ;
  - intervalles de 0 à 0,206 et de 0,073 à 0,524 : justes ;
  - 62 gardes : justes.
- Non sourcés :
  - taux par motif, déclarés comme estimations ;
  - calcul binomial (D-18) ;
  - « règle de la plateforme » (D-14).

**D. Ce qui empêche.**
- **Pour sceller** : corriger d'abord D-1 et D-2, puis D-4, D-9 et D-12, qui touchent le texte, les scripts ou les consignes scellés. Il faudra aussi poser les empreintes compagnons, dont aucune n'existe encore pour les fichiers de la procédure.
- **Pour lancer** :
  - D-3 : décision N-014, ou règle de perte écrite ;
  - toutes les corrections de code (D-5 à D-8, D-10, D-11, D-13), puisque les modules sont épinglés dès l'ouverture du run ;
  - un arbre propre, exigé par `creer_manifeste`, alors que d'autres fichiers du pilote sont en cours de modification.

## Annexe — lectures et essais

**Fichiers relus** (8 premiers chiffres de l'empreinte) :

| fichier | empreinte |
|---|---|
| rapport de la contre-lecture 1 | 9263c6a5 |
| traitement de la contre-lecture 1 | 2ea3112b |
| archive tar de la contre-lecture 1 (liste et 3 fichiers synthétiques) | 6a5520b4 |
| brouillon 3 (= version relue par la contre-lecture 1) | ba951ce9 |
| texte final | 8e06c4b4 |
| invite des cibles | 8fc41e48 |
| consigne de l'extracteur | b1fb87b3 |
| consigne du contre-vérificateur | 695ff130 |
| `verifier-sortie-v1.py` | 4c4d2902 |
| `verifier-avis-v1.py` | 8b5957e0 |
| essai à blanc | 796ba265 |
| `extraction.py` | ac183502 |
| `extraire_t05.py` | 0c8e9530 |
| `test_extraire_t05.py` | eb526901 |
| `test_extraction.py` | b12e5608 |

**Lus en plus**, parce que cités et utiles :
- H9, H10, et les sections 8 et 9 de la règle de sélection ;
- `manifeste.py`, `scellement.py`, `gardes.py`, `invites.py`, `conftest.py` ;
- `proposition-N-014-v1.md` (34725463), cité par le texte (D-3) ;
- le différentiel git de `extraction.py`.

Je n'ai lu ni `donnees/` ni `registres/`.

**Essais**, hors du dépôt, sans écrire de cache :
- les deux fichiers de tests demandés : 99 réussis ;
- greffon de traçage : 62 gardes, 0 non exercée ;
- `essai_barres.py` : D-1 et D-4 ;
- règle proposée pour D-1, sur neuf cas ;
- `essai_message.py` : D-4 ;
- substitut isolé : D-10 ;
- probabilités binomiales et intervalles recalculés ;
- outil de lecture des sous-agents sur une ligne synthétique de 4 000 caractères : rendue entière ;
- `harnais2.py`, `scenarios.py`, `scenarios2.py` : déroulés s1, s4, s5, s6, s12, s13, s18 et s19, dans des dépôts git jetables construits avec les fonctions des tests du dépôt, en lecture seule.

Pendant la relecture, le dépôt a reçu d'autres modifications : fichiers indexés, `lire_pilote.py` et ses tests, caches du pilote. Elles ne viennent pas de moi. Les quinze fichiers relus, plus `propositions.py`, ont été empreintés de nouveau à la fin : ils n'ont pas changé.
