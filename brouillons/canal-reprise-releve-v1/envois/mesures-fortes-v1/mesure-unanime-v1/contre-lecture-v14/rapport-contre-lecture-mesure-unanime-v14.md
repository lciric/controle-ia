# Contre-lecture (R2, R13) : préenregistrement « mesure unanime » v14, séquence v14, garde témoin v14, tests v14, répétition générale v14

**Verdict : à corriger en v15 — texte seul, une phrase fausse sur la provenance de la donnée réelle (CV14-1), plus deux
retouches de formulation à faire au passage (CV14-2, CV14-3). Aucun défaut de plomberie, aucune modification de science :
la plomberie v14 (séquence, garde témoin, deux tests) est bonne à sceller telle quelle et ne doit pas être touchée ; les six
sections de science sont identiques au bit près à la v13 ; la répétition rejouée est identique à l'octet à celle déposée.**

Le poids de CV14-1 est faible, et je le dis : les faits qui portent la mesure (empreinte `968414fc…` codée dans la séquence
et comparée par le script, objet git `86ec9eaf…`, identité avec l'objet de `calcul/p3-reel-v1`) sont vrais. Mais la phrase
fausse est une affirmation de fait dans un texte qui sera scellé pour toujours, la question « le texte dit-il vrai sur la
provenance ? » m'est posée explicitement, et le précédent de la v12 (CV12-1, texte seul, renvoyé en v13) tranche dans le même
sens. Coût de la v15 : une proposition à réécrire (ligne 93), la répétition à refaire (une minute, sa note cite l'empreinte du
texte), une contre-lecture ciblée (diff v14 → v15 de trois lignes, répétition rejouée). Si Lazar préfère sceller la v14 avec
la phrase fausse consignée ici, c'est sa décision, pas la mienne.

## Constats

- **CV14-1** (texte, provenance ; **à corriger**) — `preenregistrement-mesure-unanime-v14.md`, ligne 93 : « objet git
  `86ec9eaf2aac32ad9b5b3e68eb8f12d4a1a8bc56`, **entré avec le commit de consolidation `9b7721c7` du 9 novembre** ». Faux sur
  deux points. (a) `9b7721c7` n'est pas un commit de consolidation : son titre est « P3-bis : compte rendu du développeur du
  code, reçu après la passation (R-2036) ». (b) Il n'introduit pas le fichier : il ajoute deux fichiers sous
  `brouillons/P3-bis-temoin-positif-v1/` et modifie `registres/decisions.md`, rien sous `donnees/` (liste des fichiers du
  commit lue sur le dépôt distant, sans patch). Cause probable : le clone de la session est superficiel
  (`git rev-parse --is-shallow-repository` → `true`, `.git/shallow` = `9b7721c7…`) ; `9b7721c7` est la borne de l'historique
  local, où tout fichier paraît « ajouté ». Ce qui est vrai et vérifié : le fichier est suivi dans l'arbre de `main`
  (`469487af` distant, `04a1b392` local) et de la branche de travail sous l'objet `86ec9eaf…`, le même objet que sur
  `calcul/p3-reel-v1` (`eb572dac`, 20 octobre) et que sur `canal/conv-audit-n04` au commit `4d1fa5c0` (28 octobre) : il était
  donc déjà dans le dépôt bien avant le 9 novembre. **Correction** : remplacer la proposition par « présent dans l'arbre de
  `main` au moins depuis `9b7721c7`, borne de l'historique du clone superficiel de la session ; le commit d'entrée n'est pas
  recherché ici », ou la retirer. Rien d'autre ne dépend de cette phrase.
- **CV14-2** (texte, formulation ; non bloquant, au passage) — ligne 80 : « la séquence refuse un chemin de données sous
  `donnees/` ». Le refus par chemin (séquence, ligne 67) ne couvre que le préfixe littéral
  `/home/claude/canal-conv-audit-n04/donnees/`. Depuis la reconstruction, ce préfixe est un lien symbolique : le chemin
  résolu `/home/user/controle-ia-travail/donnees/…` et tout chemin relatif passent le test de chemin (comparaison de chaînes
  seulement, `sortie-refus-repetition-v1.txt`, partie (c)). Le trou est fermé par la suite de la phrase (refus de l'empreinte
  annoncée égale à la réelle, ligne 68) et par le script (ligne 260 à 262 : empreinte du fichier comparée à l'annoncée avant
  tout `np.load`) ; une empreinte annoncée en majuscules passe la ligne 68 mais est refusée par le script. Aucun défaut de
  protection. **Correction** : « refuse un chemin de données sous le préfixe codé en dur
  `/home/claude/canal-conv-audit-n04/donnees/` **et** toute empreinte annoncée… ».
- **CV14-3** (texte, formulation ; non bloquant, au passage) — ligne 15 : « Python 3.13.18, numpy 2.5.4 — la version des
  répétitions d'octobre — ». Vrai pour numpy seulement ; les répétitions d'octobre tournaient sous Python 3.13.17
  (`repetition-v13/sortie-reelle-v13.json`, manifeste). Sans effet mesuré : la sortie v14 hors manifeste est égale à la
  sortie v13 hors manifeste, et les deux manifestes ne diffèrent que par `python` et `plateforme`
  (`comparaison-repetition-v14-v1.txt`). **Correction** : « numpy 2.5.4 comme en octobre ; Python 3.13.18 au lieu de 3.13.17,
  sortie de répétition identique hors manifeste ».

Remarques sans constat : (i) ligne 11, « six fichiers de sortie » : six noms distincts, huit occurrences, dont la séquence
elle-même et le journal, qui ne sont pas des sorties au sens strict ; lisible. (ii) Les quatre scripts v14 sont en mode 644
(les v12 et v13 étaient en 755) : sans effet, tout est lancé par `bash FICHIER`. (iii) Rejouer la répétition **dans le dossier
déposé** efface `repetition-v14/` scellé (séquence, ligne 69, `rm -rf`) : comportement hérité, à ne faire que sur une copie
ou pour la v15. (iv) La garde témoin répond 0 à un argument vide (`""`) : inatteignable, les trois noms sont des constantes de
la séquence. (v) `scores-p3.npz` est cité par d'autres codes du dépôt (P3, `agregation_r1_v4`, tests) : ces lectures
antérieures, hors du paquet, ne sont pas de mon périmètre ; je n'ai rien cherché de ce côté. (vi) La décision de Lazar
rappelle une vérification d'embargo DT-4 « sur les entrées avant la course » : hors de cette contre-lecture, à ne pas oublier.

## 1. Science

`scripts/verif_sections_v14_v1.py` → `sortie-sections-v13-v14-v1.json` ; `diff-texte-v13-v14.txt` (diff brut, 108 lignes).

| section | identique au bit près | octets | empreinte de la section (v13 = v14) |
|---|---|---|---|
| Hypothèse | oui | 6 075 | `d25237f8…` |
| Prédiction chiffrée et signe attendu | oui | 4 131 | `16d0ea28…` |
| Métrique | oui | 5 889 | `65ffdebf…` |
| Seuil | oui | 3 426 | `29e83a64…` |
| Critères de lecture gelés | oui | 5 210 | `3a9b0eaf…` |
| Liste d'arrêt | oui | 861 | `1ad88042…` |

Plan d'analyse : sept lignes changées, **six noms distincts, huit occurrences** (`effectifs-reel`, deux fois ;
`sortie-reelle`, deux fois ; `lecture-mecanique-reelle` ; `note-lecture-mecanique` ; `commandes-lecture-reelle` ;
`journal-lecture-reelle`), tous v13 → v14 ; après remplacement inverse des six noms, la section est **identique au bit près**
à celle de la v13 ; plus aucune occurrence de « v13 » dans le Plan de la v14. Le « huit » du brief compte les occurrences, le
« six » du texte les noms : les deux sont justes. Même ordre des neuf sections. Hors sections gelées, le diff ne touche que :
titre, lignes 3 à 19 (bloc « Version 14 », ancien auteur rétrogradé « pour mémoire »), 47 à 50 (dates, branche), 64 et 65
(noms et empreintes de la plomberie), 70 à 73 (témoin, sortie, sous-dossier), 79 à 81 (test, répétition, CV13-3, CV13-1),
92 à 95 (provenance), 459 à 480 (traitement de la contre-lecture v13). `prereg.problemes` sur la v14 : aucun ;
`exiger_prereg_scelle` : « empreinte compagnon absente » (voulu avant scellement). Empreinte recalculée du texte :
`ebc4bf7e09bf13076d9903cdd7ee5cb9bd439a4ce2a7d21219fb25908fa539e1`, celle attendue ; v13 : `f52de345…c578`, celle attendue.

## 2. Plomberie

`sortie-diff-plomberie-v13-v14-v1.txt` (diffs normalisés), `sortie-constat-test-garde-v1.txt`, `sortie-refus-repetition-v1.txt`.

| constat v13 | état | où et pourquoi |
|---|---|---|
| CV13-1 (garde témoin aveugle) | **fermé, juste** | `garde-trace-reelle-v14.sh`, lignes 9 à 12 : boucle sur `"$@"`, aucun nom codé ; sans argument → 2. Séquence, ligne 50 : `"$TEMOIN" "$SORTIE" "$SORTIE.partiel"`, les variables mêmes qu'elle écrit (lignes 52, 53, 101, 102) — la divergence garde/séquence est devenue impossible par construction. Test, lignes 10 à 12 et 20 à 24 : plante les trois noms v14 et l'état sain `repetition-v14/sortie-reelle-v14.json` ; cinq cas conformes (0, 3, 3, 3, 0). Garde essayée seule sur des noms arbitraires : 0 puis 3. |
| CV13-3 (refus par empreinte) | **fermé, juste** | séquence, ligne 68. Essayé sur une copie : empreinte annoncée = réelle → code 4 ; chemin sous le préfixe → code 4 ; les deux refus tombent avant le `rm -rf` de la ligne 69, avant `compagnons` et avant tout lancement de Python (trace `bash -x` : la seule lecture antérieure est l'empreinte du script d'analyse, ligne 36). Le chemin refusé essayé est un nom **inexistant** sous le préfixe, jamais le fichier réel. |
| CV13-4 (renvoi périmé) | **fermé** | `test-lecture-seule-v14.sh`, ligne 53 : « dans la branche LECTURE_SEULE ». |
| CV13-2 (dossiers v11 et v12 incomplets) | **non réparable, acceptable** | les bacs à sable `/tmp/claude-0/-home-claude/…` n'existent plus (vérifié : dossier absent). Les rapports v11 et v12 gardent leurs empreintes (`d654dea6…`, `a061e2a6…`, retrouvées sur disque) ; la preuve de CV11-1, la plus importante des manquantes, est rejouée à chaque répétition par le test déposé (cas A et B). Le texte le dit sans l'embellir (lignes 466 à 469). Rien à faire de plus. |

Séquence v13 → v14 : outre les noms, seuls changent le paragraphe d'en-tête, la variable `SORTIE` (ligne 40) et ses emplois,
l'appel de la garde, la ligne 68, deux messages. Test de reprise v13 → v14 : lignes 37 et 53 seulement. Les dix compagnons de
`compagnons()` (ligne 44) existent et vérifient. La plomberie versée est identique objet pour objet à celle du commit
`4d1fa5c0` de `canal/conv-audit-n04` (quatre scripts et leurs compagnons, mêmes identifiants git) ; le versement `a46d0077`
ne diffère en rien de `4d1fa5c0` sur ce dossier (569 fichiers, diff vide) et porte bien 270 compagnons.

**Constat signalé par l'auteur, `test-garde-trace-v14.sh`, lignes 28 à 30 : exact, et non bloquant au sens de R5.** Démontré
sur des copies mutées de la séquence (`sortie-constat-test-garde-v1.txt`) : (A) `TEMOIN` changé → « ÉCHEC … » puis, ligne
suivante, « OK noms du test = noms de la séquence v14 », puis « AU MOINS UN ÉCHEC », code 1 ; (B) `SORTIE` changée mais nom
encore présent dans les commentaires → « OK », code 0 (faux réconfort) ; (C) nom retiré partout → ÉCHEC, code 1. Pourquoi ce
n'est pas un repli silencieux : (1) la garde d'arrêt elle-même est testée sain et artefact, et répond juste ; (2) dans le cas
A, l'échec est dit deux fois et le code de sortie arrête la séquence (`set -e`, ligne 60) : rien n'est silencieux, une ligne
est seulement menteuse ; (3) dans le cas B, la vérification faible ne protège plus rien de nécessaire : depuis que la garde
reçoit les variables de la séquence, les noms du test n'ont pas à égaler ceux de la séquence pour que la garde soit juste ;
(4) le texte ne promet que ce que le test fait (« vérifie qu'ils figurent dans la séquence », lignes 81 et 465) et consigne
le constat (lignes 474 à 478). De même, la branche « INFO séquence absente » (ligne 32) est inatteignable depuis la séquence.
**Ne pas rouvrir la plomberie pour cela** ; si une v15 de plomberie devait un jour exister pour une autre raison : ancrer les
deux `grep` (`^TEMOIN=…$`, `^SORTIE=…$`) et mettre le « OK » sous condition.

R5 pour les deux refus de la ligne 67 et 68 : ils n'ont pas de test déposé par l'auteur ; le cas sain (répétition rejouée) et
les deux artefacts (code 4) sont maintenant déposés et scellés ici (`sortie-refus-repetition-v1.txt`,
`repetition-rejouee-v14.log`).

Compagnons `.sha256` : 72 au premier niveau, 5 dans `repetition-v14/`, 5 dans `repetition-v13/`, 19 dans
`contre-lecture-v13/` (scripts compris) : **101 vérifiés, aucun écart**.

## 3. Le texte dit-il vrai ?

| affirmation | état |
|---|---|
| `/opt/venv-essaim-sim-v1`, Python 3.13.18, numpy 2.5.4, bash 5.2.21, Linux x86_64 | vrai (lancé : `3.13.18`, `2.5.4`, `5.2.21(1)`, `Linux x86_64`) ; « version d'octobre » : numpy seulement (CV14-3) |
| lien `/home/claude/canal-conv-audit-n04` → `/home/user/controle-ia-travail` | vrai (`ls -la`) |
| `controle_ia.prereg` et `scellement` = ceux de la branche | vrai ; et identiques, objet pour objet, à ceux de `4d1fa5c0` et de `main` |
| versement depuis `4d1fa5c0`, commit `a46d0077`, 270 compagnons | vrai |
| décision de Lazar, passation `609e48f6…`, mot « a » | vrai (empreinte recalculée, fichier lu) |
| v13 « jamais scellée » | vrai (aucun compagnon du texte v13) |
| donnée réelle : chemin, empreinte `968414fc…` | chemin et empreinte = ceux de la séquence (lignes 37 et 38) et du test (ligne 19) ; **empreinte non recalculée, à dessein** (interdit de ce brief) |
| objet git `86ec9eaf…` dans `main`, identique sur `calcul/p3-reel-v1` (`eb572dac`) | vrai (`git ls-tree -r` sur `main`, `origin/main`, `origin/calcul/p3-reel-v1`, `HEAD`, `4d1fa5c0` : même identifiant ; lecture d'arbres git, jamais du fichier) |
| « entré avec le commit de consolidation `9b7721c7` » | **faux** (CV14-1) |
| « jamais ouvert par l'auteur de la v14 avant le scellement » | rien dans le paquet ni dans les deux commits de la session (`a46d0077`, `d395b66a`) ne le contredit (section 5) ; non prouvable par moi au-delà |
| gardes telles que décrites (lignes 64 à 81) | vrai, sauf la formulation large de la ligne 80 (CV14-2) ; codes 3, 4, 6, 7, 8 retrouvés dans le code et exercés |
| traitement CV13 (lignes 459 à 480) | fidèle au rapport v13 (`71ce7eea…`, empreinte recalculée) : verdict, quatre constats, corrections |

Croisement automatique (`scripts/verif_empreintes_texte_v14_v1.py` → `sortie-empreintes-texte-v14-v1.json`) : 35 empreintes
pleines et 20 courtes citées par le texte. 33 pleines et 19 courtes retrouvées sur disque ; 1 pleine
(`1518a12f…`, `conception-pari-de-signe-v3.md`, citation héritée de la v3) absente de cette branche mais **retrouvée** sur
`origin/canal/conv-audit-n04` (`git show … | sha256sum`) ; 1 pleine et 1 courte (donnée réelle) non vérifiées à dessein. Cinq
commits cités dans la partie neuve (`32de42f2`, `4d1fa5c0`, `a46d0077`, `9b7721c7`, `eb572dac`) : tous existent.

## 4. Répétition rejouée

Sur une copie isolée du dossier (bac à sable hors dépôt), `MESURE_INSTANCE=x` (ignorée, comme prévu) :
`bash commandes-lecture-reelle-v14.sh REPETITION synthetique-format-reel-repetition.npz 447dc136…b709 3 2`, de 09:16:33 à
09:17:18 UTC, code 0 (`repetition-rejouee-v14.log`). Les dix compagnons vérifiés, les deux tests de l'étape 0 passés, rien
d'écrit au premier niveau de la copie.

| fichier | déposé = rejoué |
|---|---|
| `effectifs-reel-v14.json` (`c05aa6fa…`) | identique à l'octet |
| `table-en-vigueur-v14.txt` (`f6e65b72…`) | identique à l'octet |
| `sortie-reelle-v14.json` (`aa4934d6…`) | **identique à l'octet, manifeste compris** |
| `lecture-mecanique-reelle-v14.json` (`5ee5f5ec…`) | identique à l'octet |
| `note-lecture-mecanique-v14.md` | identique hors l'heure de la ligne 3 (09:11:38 → 09:17:18) |

La note déposée cite l'empreinte `ebc4bf7e…` du texte v14 tel qu'il est sur disque (répétition faite sur le texte final),
dit « NON SCELLÉ (GardeArret) », « RÉPÉTITION GÉNÉRALE … aucune donnée réelle », données `447dc136…`. Comparée à la v13
déposée : effectifs et table identiques à l'octet ; sortie égale hors manifeste (`python`, `plateforme`) ; lecture égale hors
`sources.sortie` ; note égale hors lignes 3 et 62 (`comparaison-repetition-v14-v1.txt`). Verdicts de cet essai du code, sans
valeur de résultat, inchangés depuis la v9. Refus par chemin et par empreinte : avant toute lecture (section 2).

## 5. Règle R1

Rien dans le paquet ne montre une lecture des scores réels. Vérifié : aucune sortie JSON du dossier ne porte l'empreinte
réelle en `empreinte_donnees` ; tous les manifestes de sorties désignent le fichier synthétique `447dc136…`, un fichier
synthétique de gardes `b631b790…` (contre-lectures v5 à v7) ou le mode synthétique ; aucun témoin
`execution-reelle-v*.commencee`, aucun `journal-lecture-reelle-v*.log`, aucun `.partiel`, aucune sortie réelle au premier
niveau, ni sur disque ni dans les arbres de `HEAD`, `origin/main` et `origin/canal/conv-audit-n04` ; le test de reprise
fabrique sa sortie artefact sur un synthétique et ne retouche que le champ d'empreinte, dans un dossier temporaire effacé.

## Ce que j'ai fait et pas fait

- **Aucun fichier de `donnees/` ouvert, lu, listé, empreinté ni passé en argument.** Les identifiants d'objets viennent de
  `git ls-tree -r BRANCHE | grep` (arbres git) ; la liste des fichiers du commit `9b7721c7` vient du dépôt distant, sans
  patch. Mode réel jamais lancé ; `LECTURE_SEULE` lancé seulement par le test déposé, dans son dossier temporaire, avec
  `COMMITTEST` et `MAUVAIS_COMMIT`. Aucun fichier existant modifié ; seul `contre-lecture-v14/` est écrit. Coffre et
  `diag/*/lecture-sondes-t06.json` non lus. Aucune valeur de clé lue. Aucune dépense. Préenregistrement non scellé par moi.
- Vérifiés par moi : **101 compagnons**, **55 empreintes citées** (52 retrouvées sur disque, 1 sur une autre branche, 2 non
  vérifiées à dessein), **6 identifiants git** (5 commits, 1 objet), 6 sections au bit près et le Plan par remplacement
  inverse, 5 fichiers de répétition rejoués, 3 mutations du test de garde, 2 refus.
- **Contre-lecteur** : sous-agent neuf servi par **Fable 5.2** (identifiant `claude-fable-5-2`), tel que mon invite système
  me le donne : modèle différent de l'auteur du texte v14 (Opus 5.5). Je n'ai écrit ni le préenregistrement, ni son code, ni
  la séquence, ni les gardes, ni les tests, ni aucun rapport précédent de ce paquet.
- Heures (`date -u`) : dossier créé à 09:15:01 UTC le 10 novembre 2026, premières lectures quelques minutes avant ;
  répétition rejouée 09:16:33 → 09:17:18.

## Mes fichiers (dans ce dossier, chacun scellé)

| fichier | contenu |
|---|---|
| `heure-debut.txt` | relevé `date -u` à la création du dossier |
| `diff-texte-v13-v14.txt` | `diff` brut des deux textes |
| `scripts/verif_sections_v14_v1.py` → `sortie-sections-v13-v14-v1.json` | sections au bit près, Plan d'analyse par remplacement inverse |
| `scripts/verif_empreintes_texte_v14_v1.py` → `sortie-empreintes-texte-v14-v1.json` | empreintes citées par le texte croisées avec le disque |
| `sortie-diff-plomberie-v13-v14-v1.txt` | séquence, test de reprise, garde, test de garde : diffs normalisés |
| `sortie-refus-repetition-v1.txt` | refus par chemin et par empreinte, trace `bash -x` ; limite du test de préfixe |
| `repetition-rejouee-v14.log`, `comparaison-repetition-v14-v1.txt` | répétition rejouée, comparaison au dépôt et à la v13 |
| `sortie-constat-test-garde-v1.txt` | constat de l'auteur sur le test de garde, trois mutations ; garde seule |
