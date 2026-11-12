# Épreuve hors ligne « W2 gradué » : choix de la dose λ\* d'A1-v4 (texte court, brouillon 1)

**Statut : brouillon 1, non contre-lu, non scellé ; un marqueur restant (annexe).** Nom de la version scellée : `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-v1.md`, compagnon `epreuve-w2g-dose-v1-v1.md.sha256` écrit par `python -m controle_ia.scellement sceller` (format « empreinte, deux espaces, nom », lu par `pole/outils.verifier_scelle`). **Un scellement, un rejeu.**

Rédigé le 8 novembre 2026 à partir de 19:22 UTC (heures par `date -u`) par un rédacteur neuf de la session mère `session_016QhUrrLeN21G7Z9KZobE42` (Opus 5.5), qui n'a écrit ni le brouillon 3, ni le code v5, ni l'épreuve exploratoire. Aucun appel de modèle, aucune clé, aucun réseau, aucune dépense, aucun commit ; aucun fichier existant modifié ; rien lu sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`. **L'épreuve n'a pas été jouée par ce rédacteur.** Gestes faits : lecture des sources (tableau final), `sha256sum` des sorties exploratoires, une répétition de la préparation de la copie de travail (clone, patch, empreintes, `--help` du script, sans aucune répétition de l'épreuve ; copie effacée ensuite), un calcul de Wilson sur les comptes exploratoires (section 3).

## 1. Objet

Choisir **λ\***, la dose du monde W2 gradué (W2g) de l'attaque A1-v4, par une **règle mécanique** écrite avant toute épreuve. Ce n'est **pas** une expérience décisive : aucune hypothèse n'est tranchée ici. Mais le choix de la dose **conditionne la course décisive** : λ\* remplit le marqueur `DOSE_LAMBDA` (entre doubles chevrons) du préenregistrement (brouillon 3, l. 288 : « dose λ\* fixée par le texte scellé et la sortie de l'épreuve hors ligne « W2 gradué » […] ; sans λ\*, le texte n'est pas scellable »), et les lectures 2′ à 5′ et les prédictions P7 à P11 se lisent à cette dose (brouillon 3, l. 71, 115–119). D'où ce texte, contre-lu et scellé avant le rejeu (brouillon 3, l. 262 : « texte court écrit, contre-lu, scellé, joué (0 USD) »), comme un préenregistrement (R1, R2).

## 2. Règle de choix (recopiée telle quelle, non modifiée)

Brouillon 3 (`preenregistrement-attaque-goodhart-v4-brouillon3.md`, sha256 `c44f52cc0fa53e1bbd621c56a06f6c65860487fc6afe30d52ed2d6b81adc8dac`), l. 126, écrite le 8 novembre entre 16:34 et 16:48 UTC, **avant toute épreuve** (la première épreuve, coupée, part à 17:19 UTC ; rapport du code v5, l. 59) :

> « la plus petite dose de la grille de l'épreuve à laquelle la **loi du monde** (avec N) est promue par le v9 avec une probabilité ≥ 0,80 sur 1 000 répétitions **et** la recombinaison pure S1, S2 n'est jamais promue sous v9 (0 sur 1 000) ; si aucune dose de la grille ne satisfait les deux, le texte n'est pas scellable et Lazar décide (annexe B, point 5). »

Ce texte fixe seulement ce que la règle laisse ouvert, sans en changer le sens :
- **grille de l'épreuve** = la grille gelée `GRILLE_DOSES_W2G` du code v5 (`pole/attaque_goodhart_v5.py` l. 74) : 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 ; 0,40 ; 0,50 ; 0,75 ; 1 — plus la dose 0, jouée comme **contrôle** et jamais choisissable (λ\* > 0, brouillon 3 l. 71 ; le plan de course la refuse) ;
- **« probabilité ≥ 0,80 sur 1 000 répétitions »** = fréquence observée : promues(a) / 1 000 ≥ 0,80, soit **au moins 800 sur 1 000** ; c'est ce qu'applique `choisir_dose` du script (`taux ≥ SEUIL_PROMOTION_MONDE`, l. 139–148), écrit avant l'épreuve exploratoire ;
- **« jamais promue (0 sur 1 000) »** = promues(b) = 0 (`PROMOTIONS_RECOMBINAISON_MAX = 0`, l. 54) ; les deux conditions à la **même** dose ; seules les doses complètes (1 000 répétitions) comptent ;
- **aucune dose ne satisfait** → **pas de λ\***, le préenregistrement reste non scellable, **nœud de Lazar**.

**Variante envisagée et écartée.** Le rapport du code v5 (réserve 2 bis, l. 82) propose une règle sur la **borne basse** de l'intervalle (≥ 0,80), qui donnerait **une autre dose** (0,50 au lieu de 0,40 sur les chiffres exploratoires). Elle a été proposée **après lecture des chiffres exploratoires** ; elle est **écartée pour cette raison** (R1, R4 ; décision de la mère R-1923, `registres/decisions.md` l. 1881 : « la règle de choix reste celle du brouillon 3, écrite avant […], non modifiée après lecture »). Le fait qu'à 1 000 répétitions une dose « juste au-dessus » de 0,80 ne se distingue pas d'une dose juste en dessous est **rapporté** (section 5), il ne change pas la règle.

## 3. Déclaration d'information préalable (ce qui a été vu)

Une **épreuve exploratoire non scellée** a été jouée le 8 novembre (rapport du code v5, `code-v5/rapport-code-v5-w2g-v1.md`, sha256 `c31d23b84e8406aeef1b72f2146065c854b29ee5c7cd2c84e441eaa9c8fa77a1`, section 5 ; R-1923) : graine exploratoire **20261108** (espace < 2⁶⁴), 2 processus, script `epreuve_w2g_dose_v1.py` `c691a43d…` et cœur `attaque_goodhart_v5.py` `8692746a…` (empreintes du manifeste, égales aux fichiers livrés), **grille réduite choisie après un pilote** vu : doses 0,30 ; 0,40 ; 0,50 ; 0,75 à 1 000 répétitions (18:19 à 19:13 UTC, 3 219,4 s), puis la dose 0 à 200 répétitions (193,0 s). Comptes recopiés des sorties (vérifiés sur les fichiers ci-dessous) ; Wilson à 95 % calculé par ce rédacteur avec `attaque_goodhart_v2.wilson` (l. 750) ; Clopper-Pearson de (a) tel qu'imprimé par le script.

| dose | écart moyen (nats) | (a) monde sous v9 | (a) Wilson | (a) Clopper-Pearson | (b) recombinaison sous v9 | (c) recombinaison sous v8 | (d) monde sous v8 |
|---|---|---|---|---|---|---|---|
| 0 (200 rép.) | 0,0 | 0/200 | [0,000 ; 0,019] | [0,000 ; 0,015] | 0/200 [0,000 ; 0,019] | 200/200 [0,981 ; 1,000] | 200/200 [0,981 ; 1,000] |
| 0,30 | 0,112479 | 641/1 000 | [0,611 ; 0,670] | [0,615 ; 0,666] | 0/1 000 [0,000 ; 0,004] | 762/1 000 [0,735 ; 0,787] | 992/1 000 [0,984 ; 0,996] |
| 0,40 | 0,169507 | 809/1 000 | [0,783 ; 0,832] | [0,787 ; 0,829] | 0/1 000 [0,000 ; 0,004] | 621/1 000 [0,591 ; 0,651] | 990/1 000 [0,982 ; 0,995] |
| 0,50 | 0,233694 | 890/1 000 | [0,869 ; 0,908] | [0,872 ; 0,906] | 0/1 000 [0,000 ; 0,004] | 499/1 000 [0,468 ; 0,530] | 992/1 000 [0,984 ; 0,996] |
| 0,75 | 0,425176 | 965/1 000 | [0,952 ; 0,975] | [0,954 ; 0,974] | 0/1 000 [0,000 ; 0,004] | 311/1 000 [0,283 ; 0,340] | 997/1 000 [0,991 ; 0,999] |

Règle appliquée par le script sur cette grille réduite : λ\* imprimé **0,40**. Aucune évaluation impossible, aucune loi du monde refusée par la grammaire servie.

Fichiers (dossier `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/code-v5/`, `sha256sum` relevé le 8 novembre à 19:24 UTC, égal au rapport l. 109–114) :

| fichier | sha256 |
|---|---|
| `epreuve-w2g-dose-v1-exploratoire-doses-030-075.json` | `c85e59b3594050e6c7ce162721e42c19b55d890acd752ef39b268617b279b2b9` |
| `epreuve-w2g-dose-v1-exploratoire-doses-030-075-table.txt` | `91b06e77b36bdadaaf84d9b302bda859e486710073a9f675323f2808e017fe96` |
| `epreuve-w2g-dose-v1-exploratoire-dose-000.json` | `a4821262e5b9507d4275c81050af2034b3f9bdb0364b97513d30bdf2cb56748e` |
| `epreuve-w2g-dose-v1-exploratoire-dose-000-table.txt` | `30b5736fba7d3e13f65ff7562474ede92caf47ef6bf5e7b7822bf0e9193569af` |
| `epreuve-w2g-dose-v1-pilote-vitesse-table.txt` | `30c09d3392e5b6e8ab509f790574cc11c77a3162d494ea1659e51f11f7efb2a2` |
| `epreuve-w2g-dose-v1-sortie-console.txt` | `85506f1cb51ab373e1e92fa3e8fe84b0fdaa8019c1a0da4d7698c99dbcca15c7` |

Les compagnons d'origine (dossier de brouillon `…/scratchpad/epreuve-w2g-v1-a/`) se vérifient (`sha256sum -c` : OK pour la sortie, la table et le manifeste de la grille réduite).

Vus aussi : le **pilote de vitesse** (graine 5, 50 répétitions, doses 0,10 et 0,50 : (a) 5/50 et 43/50 ; (b) 0/50 ; (c) 0,900 et 0,480 ; (d) 0,940 et 1,000), vu **avant** le choix de la grille réduite ; une **première épreuve** sur la grille entière, coupée par le délai externe à 18:17 UTC (code 124) **sans sortie** (son dossier de brouillon ne contient qu'un manifeste, non lu par ce rédacteur) ; la recommandation « borne basse » du rapport (section 2). Ont vu ces chiffres : le développeur du code v5, la mère, ce rédacteur ; le contre-lecteur les verra.

**Usage** : ces chiffres servent **à information seulement**. Ils ne fixent ni la règle, ni la grille, ni le nombre de répétitions, ni aucun seuil ; ils ne départagent rien ; ils ne sont **jamais combinés** à ceux du rejeu (ni sommés, ni moyennés, ni pris pour confirmer une dose). Les cartes du rejeu sont neuves (entropie neuve, section 4) : aucune répétition n'est commune.

## 4. Rejeu

**Grille** : la grille gelée entière, 11 doses (0 ; 0,05 ; 0,10 ; 0,15 ; 0,20 ; 0,25 ; 0,30 ; 0,40 ; 0,50 ; 0,75 ; 1), **en un seul appel** (option `--doses` omise : le script prend alors `GRILLE_DOSES_W2G`, l. 67–69, 175). **1 000 répétitions à chaque dose, dose 0 comprise** : le script n'a qu'un nombre de répétitions par appel (`--repetitions`, l. 173, 208–209) ; il ne fait pas 200 répétitions à la dose 0 dans le même appel. Plutôt qu'un second appel (deux sorties, deux lectures), la dose 0 est jouée à 1 000 dans le même appel (≈ 1 900 secondes-processus de plus).

**Entropie** : `<<ENTROPIE_EPREUVE>>`. Recommandation (sans changement de code) : l'entropie est l'entier gros-boutiste de l'empreinte SHA-256 du **présent fichier scellé**, lue par le mode décisif du script `--entropie-texte CHEMIN` (l. 172, 188–192 : refus si le compagnon `.sha256` manque ou ne correspond pas ; `verifier_entropie(…, decisif=True)` refuse toute entropie < 2⁶⁴, donc la graine exploratoire 20261108). L'empreinte n'existe qu'au scellement : elle est **fixée par le scellement** et **neuve** par construction. Toutes les graines en dérivent par `numpy.random.SeedSequence(entropie, spawn_key=(clé de l'étiquette, indices…))` (`attaque_goodhart_v2.graine`, l. 104–108, R9) : cartes par `carte_w2g(entropie, r, dose)` (étiquettes « monde|W2g », « developpement|W2g », indice r), juge par les étiquettes « epreuve-w2g|<loi>|<juge>|dose=<λ> », indices (r, 1) ; la carte r est la même à toutes les doses (plan apparié en λ). Cette entropie est distincte de celle de la course décisive (empreinte du préenregistrement scellé) : les cartes de l'épreuve ne sont pas celles de la course.

**Processus** : 4 (`nproc` = 4 le 8 novembre). **Durée attendue** : 3 219,4 s pour 4 000 répétitions sur 2 processus (1,61 seconde-processus par répétition), 193,0 s pour 200 à la dose 0 (1,93) ; 10 000 × 1,61 + 1 000 × 1,93 ≈ 18 000 secondes-processus, soit **≈ 4 500 s (75 min) sur 4 processus** si l'échelle est linéaire (non mesurée à 4 processus : réserve). Le brouillon 3 (l. 256 : « 29 à 58 min sur un cœur ») sous-estime ; correction au brouillon 4.

**Durée maximale** : `--duree-max-s 6300` (marge × 1,4 sur l'attendu), sous un délai externe `timeout 7000` (700 s de marge pour l'arrêt propre et l'écriture), la commande étant lancée en arrière-plan avec un délai d'outil de 7 200 s.

**Préalables** (dans l'ordre ; un seul manque : rien ne part) :
1. ce texte scellé, contre-lu (section 7), `sha256sum -c` OK sur son compagnon ; empreinte écrite au registre des décisions avant le lancement ;
2. dossier de sortie **absent** : `test ! -e "$DOSSIER"` ;
3. copie de travail neuve, sans toucher au dépôt public :
   ```
   COPIE=/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/epreuve-w2g-dose-v1-rejeu-v1-copie
   PATCH=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/code-v5/patch-public-code-v5.diff
   test ! -e "$COPIE" && mkdir "$COPIE" && git clone -q --no-hardlinks /home/user/ideation-organism "$COPIE/ideation-organism"
   cd "$COPIE/ideation-organism" && git checkout -q --detach 8947bc80a5c2fee0cfee4f3cafbdaaca8ed77f3e
   sha256sum "$PATCH"            # attendu 12c39347e47fec599da21ef00f8d0534b661d2dd982b7f8c7ca9ac2169a660d2
   git apply --check "$PATCH" && git apply "$PATCH"
   git rev-parse HEAD ; git status --porcelain   # exactement les cinq lignes « ?? » des fichiers v5
   ```
   puis, depuis `orchestrator/`, les empreintes des huit modules que le manifeste du script relève (`MODULES`, l. 58–60), égales à : `pole/attaque_goodhart_v5.py` `8692746a1b02b15465062423d1f05e2084ce1d1861c979316ce1a5ef4384ba15` ; `pole/attaque_goodhart_v4.py` `0077a6470781b8cd9e0599232ddd52e3601c8c4c8735a5cfcf817800bda3bb5c` ; `pole/attaque_goodhart_v2.py` `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` ; `pole/nul_v9.py` `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` ; `demonstrations/banc_tricheurs_v9.py` `7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44` ; `demonstrations/banc_tricheurs_v8.py` `0be47e4b5916a98499faf9c40d65369b41e3a5463d7ab444ed18ba18bba08c03` ; `demonstrations/banc_tricheurs_v7.py` `ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12` ; `demonstrations/epreuve_w2g_dose_v1.py` `c691a43d9905e91a0ba91ddfef785e53a091768fa7dcd3007f03066aeef10dda` (celles de l'épreuve exploratoire) ;
4. `python3` 3.13.18 et numpy 2.5.3 (ceux de l'épreuve exploratoire) ;
5. charge de la machine relevée (`cat /proc/loadavg`) : moyenne sur une minute **< 1,0**, et aucun autre calcul long lancé par la session pendant la fenêtre (la mère s'en assure) ;
6. le script de lecture (changement C1, annexe) écrit, essayé sur ses cas sains et ses artefacts (section 6).

**Commande exacte** (aucune instance louée, 0 USD) :
```
COPIE=/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/epreuve-w2g-dose-v1-rejeu-v1-copie
DOSSIER=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-rejeu-v1
TEXTE=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/epreuve-w2g-dose-v1-v1.md
cd "$COPIE/ideation-organism/orchestrator" && { date -u; cat /proc/loadavg; } > "$COPIE/console-rejeu-v1.txt" && \
timeout 7000 nice -n 10 python3 -I -B demonstrations/epreuve_w2g_dose_v1.py "$DOSSIER" \
    --entropie-texte "$TEXTE" --repetitions 1000 --processus 4 --duree-max-s 6300 \
    >> "$COPIE/console-rejeu-v1.txt" 2>&1 ; echo "code $?" >> "$COPIE/console-rejeu-v1.txt" ; date -u >> "$COPIE/console-rejeu-v1.txt"
```
Sorties, **scellées par le script à l'écriture** (`ecrire_json_scelle`, `ecrire_scelle` : compagnons `.sha256`, refus d'écraser) dans le dossier neuf `epreuve-w2g-dose-v1-rejeu-v1/` : `manifeste.json` (avant la première répétition : mode, entropie, texte et son empreinte, grille, répétitions, processus, durée maximale, règle, versions, empreintes des modules, règle des graines), `epreuve-w2g-dose-v1.json`, `epreuve-w2g-dose-v1-table.txt`. La console est recopiée à côté sous `epreuve-w2g-dose-v1-rejeu-v1-console.txt` et scellée. Code 0 : complet ; 3 : arrêt à la durée maximale ; 2 : refus.

## 5. Ce qui est rapporté

Lecture **après** le scellement de la sortie, par le script de lecture (C1), sans autre calcul :
- **par dose** (les 11) : (a) loi du monde sous v9, (b) recombinaison pure sous v9, (c) recombinaison pure sous v8, (d) loi du monde sous v8 : promues / 1 000, taux, **intervalle de Wilson à 95 %** (`attaque_goodhart_v2.wilson`, z = 1,959963984540054) ; Clopper-Pearson tel qu'imprimé par le script ; écart moyen ; médiane du logarithme de la richesse de (a) ; évaluations impossibles par ligne ; lois du monde refusées par la grammaire servie ; « complète » ;
- **λ\* imprimé par le script** (`dose_proposee_par_la_regle`) et le même λ\* recalculé par le script de lecture depuis les comptes (au moins 800 sur 1 000 en (a), 0 en (b)) ; s'ils diffèrent : arrêt (section 6) ;
- si la borne basse de Wilson de (a) à λ\* est sous 0,80 : « λ\* à la limite » est écrit ; **λ\* ne change pas** ;
- **tension avec P10** (brouillon 3 l. 118 : taux(v8, témoin, 1) ≥ 0,50) : à λ\*, le taux (c) et son Wilson sont rapportés, avec la mention « P10 tenue par l'oracle » si (c) ≥ 0,50, « P10 en tension à λ\* » sinon ; (c) est un analogue hors ligne (la recombinaison soumise une fois), non la mesure de P10 en course. **Cette tension est rapportée ; elle ne change pas λ\*** ; elle va au brouillon 4 du préenregistrement (R-1923) ;
- les chiffres exploratoires (section 3) peuvent être cités à côté, marqués « exploratoire, graine 20261108 », **jamais combinés**.
λ\* ainsi obtenu remplit le marqueur `DOSE_LAMBDA` du préenregistrement ; « aucune dose » → nœud de Lazar.

## 6. Liste d'arrêt et gardes (R5 : chaque garde essayée sur un cas sain et un artefact avant le rejeu)

Toute garde qui refuse : **arrêt sans λ\***, sortie (ou trace partielle) scellée telle quelle et rapportée, aucun chiffre lu pour choisir une dose.
1. **Sortie absente** : `epreuve-w2g-dose-v1.json` ou `manifeste.json` absent, ou compagnon non conforme (`verifier_scelle` faux), ou code de sortie ≠ 0.
2. **Durée dépassée** : code 3, `arret` non nul, ou une dose incomplète (le script ne propose alors aucune dose, l. 231) ; délai externe atteint (code 124).
3. **Graine non dérivée** : `mode` ≠ « décisif (graine = empreinte du texte scellé) », `entropie_racine` ≠ l'entier de l'empreinte du texte scellé, `texte.sha256` du manifeste ≠ cette empreinte, entropie < 2⁶⁴ ; ou grille, répétitions, processus, durée maximale, versions ou empreintes des modules du manifeste différents de la section 4.
4. **Vérité servie** : l'épreuve n'appelle aucun proposeur et ne sert aucune consigne (la garde `verifier_verite_non_servie` de la course n'est pas sur son chemin ; (a) use la loi du monde **par construction**, comme oracle) ; la garde porte donc sur ce qui sort : la sortie ne contient aucune clé « verite » ni « N » ; et l'empreinte du script et du cœur égale à la section 4 (aucun chemin neuf vers un proposeur).
5. **Défaut du certificat** (garde, pas une règle de choix) : à la dose 0, (a) ou (b) > 0 ; à une dose quelconque, (b) > 0 (membre du nul v9 promu : défaut du code ou du certificat). Arrêt, rapport, nœud de Lazar.
6. **Instrument** : une loi du monde refusée par la grammaire servie à une dose (l'oracle ne borne plus ce qu'un attaquant peut écrire) ; désaccord entre le λ\* du script et celui recalculé. Des évaluations impossibles ne sont pas un arrêt : comptées, rapportées, et un audit écrit précède le report de λ\* au préenregistrement (λ\* inchangé).
**Aucun rejeu partiel combiné** : une trace arrêtée n'est jamais complétée par un second appel ; une nouvelle tentative demande un texte neuf (`…-v2.md`, R12), donc une entropie neuve, contre-lu et scellé ; rien de la trace arrêtée n'y entre.
**Essais des gardes** (avant le rejeu, par le script de lecture C1) : cas sain = une course de chaîne de 2 répétitions sur toutes les doses, `--processus 1`, sous un texte factice scellé dans le brouillon de session (chiffres non lus au-delà des gardes), lue avec 2 répétitions et 1 processus attendus ; artefacts = les sorties exploratoires (doivent refuser : graine non dérivée, grille réduite), un dossier vide (sortie absente), une copie de la course de chaîne avec `arret` non nul, avec une clé « verite » ajoutée, avec (b) = 1 à une dose, avec une empreinte de module changée (chacune rescellée dans le brouillon de session). Chaque artefact doit refuser pour son motif.

## 7. Contre-lecture (R2)

Par un **sous-agent neuf d'un autre modèle** que ce rédacteur (Opus 5.5) — Fable 5.1 (N-052) —, qui n'a écrit ni ce texte, ni le brouillon 3, ni le code v5, **avant scellement**. Fichiers à lui donner : ce texte ; le brouillon 3 (l. 71, 115–119, 126, 256, 262, 288) ; le rapport du code v5 (sections 2, 5, 6) ; `code-v5/orchestrator/demonstrations/epreuve_w2g_dose_v1.py` ; `code-v5/orchestrator/pole/attaque_goodhart_v5.py` (l. 74, `carte_w2g`, `juger`) ; `/home/user/ideation-organism/orchestrator/pole/attaque_goodhart_v2.py` (`graine`, `verifier_entropie`, `wilson`) et `pole/outils.py` (`verifier_scelle`) ; R-1923 (`registres/decisions.md` l. 1881) ; les sorties exploratoires (section 3). À vérifier : la règle recopiée mot pour mot, et que les précisions de la section 2 n'en changent pas le sens ; que la variante « borne basse » est écartée et pourquoi ; que les chiffres exploratoires ne fixent rien ; les options de la commande contre le script ; la durée ; la totalité de la liste d'arrêt ; les changements de code demandés.

## Annexe. Marqueur, changements de code demandés

**Marqueur restant** : `ENTROPIE_EPREUVE` (entre doubles chevrons, section 4), levé au scellement par les mots « l'entier gros-boutiste de l'empreinte SHA-256 du présent fichier scellé, lue par `--entropie-texte` » (recommandé, confiance 0,8 : option existante et gardée) ; ou par un entier ≥ 2⁶⁴ écrit ici, ce qui demande le changement C2. Le motif `<<[A-Z0-9_]+>>` est cherché par programme dans le fichier final : zéro occurrence, sinon pas de scellement.

**Changements de code demandés** (fichiers neufs, R12 ; le script de l'épreuve n'est pas modifié) :
- **C1 (exigé avant le rejeu)** : un script de lecture neuf, `demonstrations/lecture_epreuve_w2g_dose_v1.py` (hors de la fermeture gelée), qui lit la sortie scellée et le texte scellé, applique les gardes 1 à 6 de la section 6, calcule Wilson par `attaque_goodhart_v2.wilson`, recalcule λ\* depuis les comptes, écrit la table de la section 5, et refuse (code 2, motif nommé) sur toute garde ; avec deux paramètres, « répétitions attendues » et « processus attendus » (1 000 et 4 par défaut ; 2 et 1 pour la course de chaîne), tout le reste de la section 4 étant comparé tel quel ; essayé sur les cas sains et artefacts de la section 6. Raison : le script de l'épreuve ne donne pas Wilson (Clopper-Pearson seulement, l. 131) et ne vérifie pas la sortie après coup.
- **C2 (seulement si l'on veut une entropie écrite dans le texte)** : une option décisive `--entropie N` (entier ≥ 2⁶⁴) ; absente du script (`--graine` est exploratoire, < 2⁶⁴). Non demandée si la recommandation du marqueur est retenue.
- **Non demandé** : 200 répétitions à la dose 0 dans le même appel (il faudrait des répétitions par dose ; la dose 0 est jouée à 1 000) ; la grille entière en un appel et la graine dérivée existent déjà.

## Sources lues

| pièce | chemin | sha256 |
|---|---|---|
| préenregistrement, brouillon 3 | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v4-brouillon3.md` | `c44f52cc0fa53e1bbd621c56a06f6c65860487fc6afe30d52ed2d6b81adc8dac` |
| rapport du code v5 | `…/code-v5/rapport-code-v5-w2g-v1.md` | `c31d23b84e8406aeef1b72f2146065c854b29ee5c7cd2c84e441eaa9c8fa77a1` |
| script de l'épreuve | `…/code-v5/orchestrator/demonstrations/epreuve_w2g_dose_v1.py` | `c691a43d9905e91a0ba91ddfef785e53a091768fa7dcd3007f03066aeef10dda` |
| cœur v5 | `…/code-v5/orchestrator/pole/attaque_goodhart_v5.py` | `8692746a1b02b15465062423d1f05e2084ce1d1861c979316ce1a5ef4384ba15` |
| patch public | `…/code-v5/patch-public-code-v5.diff` | `12c39347e47fec599da21ef00f8d0534b661d2dd982b7f8c7ca9ac2169a660d2` |
| cœur v2 et outils (dépôt public, commit `8947bc8`) | `/home/user/ideation-organism/orchestrator/pole/attaque_goodhart_v2.py` ; `pole/outils.py` | `3c9de8b8…` ; `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` |
| décision R-1923 | `registres/decisions.md` l. 1881 (fichier vivant) | non empreinté |
