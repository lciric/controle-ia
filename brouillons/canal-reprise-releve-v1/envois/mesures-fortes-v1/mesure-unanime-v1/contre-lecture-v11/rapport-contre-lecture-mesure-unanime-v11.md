# Contre-lecture (R2) : préenregistrement « mesure unanime » v11, lecture mécanique v7 et son essai brut, rédaction v5, séquence v11, garde isolée et son test, répétition générale v11

**Verdict : à corriger en v12.** Un constat sérieux sur la séquence seule (CV11-1) ; la logique de lecture, la table, le script,
la garde « une seule exécution » et la répétition tiennent.
- **CV11-1, le mode `LECTURE_SEULE` ne peut jamais atteindre l'étape (3) : il sort avec le code 1, sans message.** La ligne 50 de
  `commandes-lecture-reelle-v11.sh`, dernière commande de la branche `LECTURE_SEULE` de la fonction `etape_0`, est
  `[ -e note-lecture-mecanique-v11.md.sha256 ] && { … exit 7; }` : quand la note n'est **pas** scellée (le cas même que la reprise
  doit traiter), ce test rend 1, la fonction rend 1, et `set -e` (ligne 23) arrête le script au retour de `etape_0 LECTURE_SEULE`
  (ligne 66), juste après « OK … sortie-reelle-v11.json », sans un mot. Vérifié en lançant sur une copie (cas D1, D2, D3, E :
  code 1, journal muet) et par une reproduction minimale du mécanisme (`scripts/repro_set_e_v1.sh`). Le mode réel et la
  répétition ne sont pas touchés (leurs branches finissent par une commande qui rend 0). Mais le texte (lignes 58 à 61) et la
  séquence (lignes 15 à 18) promettent une reprise qui n'existe pas, et c'est un repli silencieux (R5). Une interruption après
  l'étape (2) obligerait à rejouer (3) et (4) à la main : un écart au préenregistrement scellé. Avec la seule ligne 50 réécrite
  en `if … fi` (dans ma copie), tout ce que CV10-2 demandait se vérifie : code 8 si le commit diffère du manifeste, code 1 à
  l'étape (3) si l'empreinte des données diffère, code 0 puis **code 7 au second appel** sans rien réécrire, note refaite et
  lecture scellée intacte après une interruption simulée avant l'étape (4). Comme pour CV10-1, le défaut vient d'un mode que la
  répétition ne traverse pas et qu'aucun test déposé n'exerce.

Le reste est mineur (CV11-2 : restes de v10 et incohérences du texte ; CV11-3 : détails des outils). Je ne trouve **aucun faux
« confirmé »** ni faux blocage d'un verdict : l'arbre de M2 ter, l'excès apparié, les seuils de M4, les audits, les gardes et
les refus sont justes et stricts aux bornes ; la répétition se rejoue à l'identique ; CV10-1 est fermé.

Vérifié en lançant, et conforme :
- **Le test déposé de la garde** (`bash test-garde-trace-v11.sh`) : cinq cas conformes (sain avec `repetition-v11/`, témoin, sortie
  finale, `.partiel`, dossier vide). **La garde en place**, sur l'état réel du dossier déposé (lecture seule) : **code 0** ; depuis
  `repetition-v11/`, où `sortie-reelle-v11.json` existe : code 3. Aucun des trois noms qu'elle regarde n'existe au premier
  niveau ; `ls -d sortie-reelle-v11*` n'y rend rien non plus. Le témoin `noclobber` (lignes 44 et 45 extraites) se pose une fois
  (code 0), refuse la seconde (code 3), et la garde isolée bloque ensuite (code 3).
- **La répétition, rejouée** depuis une copie du dossier (`MESURE_INSTANCE=x bash commandes-lecture-reelle-v11.sh REPETITION … 447dc136… 3 2`) :
  30,5 secondes, code 0. Effectifs, lecture mécanique et table en vigueur **identiques à l'octet** au dépôt ; la sortie ne
  diffère que par `manifeste.donnees` (le chemin du fichier lu) ; la note, par sa ligne 3 (heure et empreinte de la sortie). La
  note déposée cite `b1c1dd69…`, **l'empreinte de la v11 sur disque** : la répétition a été faite sur le texte final. Les
  verdicts : M1 confirmé, M2 attendu, M2 ter (1) avec Ville à 0,050, M3 tenu, M4 confirmé (excès 0,047), première ligne — un
  essai du code sur des scores synthétiques, sans valeur de résultat.
- **`LECTURE_SEULE`** sur une copie (cas 0 et A à H, puis D2 à G avec la ligne 50 corrigée dans la copie seulement) : voir CV11-1.
- **La branche E ≠ 60 de la séquence v11**, en répétition sur un fichier au format réel où E = 52 : au bout, code 0, 8 minutes
  45 secondes ; table refaite au E et aux longueurs observés, scellée, désignée par la table en vigueur scellée, vérifiée par la
  lecture ; note scellée (section 2).
- **L'arbre de M2 ter** : 64 combinaisons, deux r₀ (0,1 et 0,7), bornes à 10⁻⁹ ; aucun désaccord de feuille ni d'étiquette avec
  le Seuil réécrit depuis le texte seul ; r₀ n'est condition nulle part.
- **L'essai brut de la lecture v7**, reproduit à l'octet (`0745cc20…`) ; **`--test-gardes`** : quinze entrées ; **neuf refus du
  mode réel**, sans un octet écrit ; le cas sain écrit 807 octets identiques aux effectifs déposés ; `verifier_scores_invalides`
  appelée 705 fois pendant un `main()` en mode réel sur le fichier de la répétition ; **le mélange à pas fixé** par simulation ;
  **toutes les empreintes de l'en-tête** et tous les compagnons ; les chiffres de la table et les formules.

- Contre-lecteur : sous-agent neuf **Fable 5.1** (l'auteur de la v11 est Opus 4.8 : modèle différent, R13). Je n'ai écrit ni le
  préenregistrement, ni le script, ni la table, ni la lecture, ni la rédaction, ni la séquence, ni la garde, ni aucun des
  rapports précédents. Le brief qui m'a été remis dit « Opus 5.5 » dans sa première ligne ; le message de lancement dit
  Fable 5.1, et c'est le modèle qui me sert.
- Début : 2026-10-28 03:39:47 UTC (`date -u`, appel séparé). Fin : dernière ligne. Les heures d'`ls` sont à l'heure de Paris
  (UTC + 1) : les fichiers v11 déposés datent de 03:37 et 03:38 UTC.
- Processeur seul. Je n'ai ouvert, chargé ni empreinté **aucun fichier de `donnees/`** : l'empreinte `968414fc…` n'est donc pas
  vérifiée par moi. `commandes-lecture-reelle-v11.sh` n'a été lancé qu'en `REPETITION` et en `LECTURE_SEULE` (avec un deuxième
  argument `pas-un-commit`, `repetition-generale` ou `abc1234`, jamais un commit réel), toujours sur des copies du dossier dans
  mon bac à sable ; le mode réel n'a jamais été lancé (sur une copie scellée, il lirait les données réelles) ; pour son étape 0,
  j'ai lancé la garde isolée en place (elle ne fait que tester l'existence de trois noms) et le témoin extrait dans un dossier
  temporaire. `test-garde-trace-v11.sh` et `garde-trace-reelle-v11.sh` ont été lancés tels quels.
- Je n'ai modifié aucun fichier du dépôt et je n'ai fait aucun commit (`git status` : seul un dossier étranger non suivi,
  `theorie-v1/…/anteriorite-v1/`, déjà là avant moi). Aucune clé ni jeton lu. Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`,
  numpy 2.5.4, bash 5.2.21. Mes vérifications importent le script v8 et la lecture v7 **sans modification** depuis la copie
  (identique à l'octet au dépôt) ; la seule enveloppe posée l'est sur un nom du module (compteur d'appels), jamais sur le fichier.
  La seule modification de code, la ligne 50 de la séquence réécrite en `if … fi`, l'a été dans ma copie `copie-lecture-seule/`
  (séquence rescellée là, et là seulement), pour vérifier la logique de CV10-2.

## Empreintes lues

| fichier | empreinte | état |
|---|---|---|
| `preenregistrement-mesure-unanime-v11.md` | `b1c1dd69413c824551500cb46310c15c4a809f5b05559b45e407a34d2157791c` | objet ; identique dans `50208ab1` ; pas de compagnon (normal) ; aucun « ⟨…⟩ » ; cité par la note de répétition déposée ; `prereg.exiger_prereg_scelle` passe sur une copie scellée par moi |
| `preenregistrement-mesure-unanime-v10.md`, `-v9.md` | `785a33fa…1c3c2`, `9206956b…bd35e7` | conformes à l'en-tête |
| `analyse_fausses_alertes_v8.py` | `52b1760a…5400` | conforme ; compagnon conforme ; identique dans `32de42f2` et `50208ab1` |
| `sortie-synthetique-essai-v8.json` | `f83456be…fe62` | conforme ; compagnon conforme |
| `table_m2bis_m4_v8.py` → `table-m2bis-m4-v8.json` | `7e512516…e0d3` → `f63faada…b120` | conformes ; compagnons conformes ; chiffres cités = ceux de la table |
| `lecture_mecanique_v7.py` | `af45f5d1…8f15` | conforme ; compagnon conforme ; ne diffère de la v6 que par un mot de docstring (`diff`) |
| `essai_lecture_mecanique_v7.py` → `essai-lecture-mecanique-v7.json` | `e287f246…cabb95` → `0745cc20…bbdef` | conformes ; compagnons conformes ; sortie **reproduite à l'octet** ; identique à l'essai v6 déposé |
| `rediger_note_lecture_v5.py` | `bd41880e…2818` | conforme ; compagnon conforme ; ne diffère de la v4 que par `--instance` obligatoire et la docstring |
| `commandes-lecture-reelle-v11.sh` | `160e0477…8d93` | conforme ; compagnon conforme ; identique dans `50208ab1` ; **autre contenu dans `32de42f2`** (`332ea15f…`, CV11-2 (c)) |
| `garde-trace-reelle-v11.sh`, `test-garde-trace-v11.sh` | `ef8c7bfc…139d`, `4278a5ff…154d` | compagnons conformes ; dans `50208ab1`, **absents de `32de42f2`** |
| `synthetique-format-reel-repetition.npz` | `447dc136…b709` | compagnon conforme |
| `repetition-v11/` : effectifs, sortie, lecture, note, table en vigueur | `c05aa6fa…`, `d36a7508…`, `621bbe71…`, `1664d9b9…`, `f6e65b72…` | cinq compagnons conformes (celui de la table en vigueur existe : reste de CV10-3 fermé) ; dans `50208ab1` ; rejoués (section 2) |
| `contre-lecture-v10/rapport-contre-lecture-mesure-unanime-v10.md` | `c401043b…32b0e` | conforme à l'en-tête (`c401043b…`) ; onze compagnons conformes ; `scripts/` versé (reste de CV10-3 fermé) |
| rapports v9 à v1, complément v2 | `aeeca90d…`, `989c02de…`, `7783ab01…`, `23ce5f93…`, `912dd47a…`, `ef6b8770…`, `0fb0734a…`, `5d47ae52…`, `e5ca74bb…` | conformes à l'en-tête |
| `src/controle_ia/bases/sequentiel.py` | `35a09834…11ba8` | conforme |

## 1. Fermeture de CV10-1 à CV10-3 (et des restes de CV4-1, CV4-4)

| constat | état | où et pourquoi |
|---|---|---|
| CV10-1 (la garde « toute trace bloque » attrapait la répétition déposée) | **fermé** | Garde isolée `garde-trace-reelle-v11.sh`, lignes 7 et 8 : trois noms explicites (témoin, sortie finale, `.partiel`), aucun préfixe ; répétition dans `repetition-v11/` (séquence, ligne 59) ; témoin `noclobber` jamais effacé (lignes 44 et 45) ; test déposé (R5) qui passe sur un état planté avec `repetition-v11/sortie-reelle-v11.json` et bloque sur les trois traces. **Lancée en place sur l'état déposé : code 0** ; le témoin se pose une fois et refuse la seconde. Ordre de l'étape 0 : garde, puis scellement du préenregistrement, puis témoin — un lancement avant scellement ne laisse aucune trace. Nuance de formulation (CV11-2 (g)) : le texte dit « exercée sur l'état déposé », le test ne l'exerce que sur un état planté qui l'imite ; en répétition, `etape_0` ne lance que le test, pas la garde sur le dossier courant (CV11-3 (f)). |
| CV10-2 (`LECTURE_SEULE` réécrivait une note scellée ; table en vigueur et commit non vérifiés) | **à moitié : la logique voulue est écrite, mais le mode ne s'exécute pas** | Écrit : refus si la note est scellée (ligne 50, code 7) ; `sceller` qui ne réécrit jamais un compagnon (ligne 35, et le module refuse une autre empreinte) ; étapes (3) et (4) sautées si déjà scellées (lignes 97 et 102) ; compagnon de la table en vigueur et de la table vérifiés (ligne 67) ; `table-en-vigueur-v11.txt` scellé à l'étape (2) (ligne 92) ; commit comparé au manifeste (ligne 68, code 8). **Ouvert** : la ligne 50 tue le mode avant l'étape (3) (CV11-1) ; une lecture déjà scellée n'est pas vérifiée avant d'écrire la note (cas G ter : un octet changé passe), alors que CV10-2 demandait « la vérifier au lieu de la réécrire » (CV11-1, correction). Le texte (lignes 58 à 61) décrit la logique voulue, pas le comportement. |
| CV10-3 (instance en dur ; mois ; docstrings ; renvoi ; compagnon ; provenance ; versement) | **presque fermé** | Fermé : `--instance` obligatoire sans défaut (rédaction, ligne 29 ; séquence, lignes 64, 71, 104) ; mois complets (ligne 103) ; renvoi « v8 et v9 ont exercé … » retiré ; compagnon de la table en vigueur ; `contre-lecture-v10/scripts/` versé. Reste : docstring de la lecture v7, ligne 1, « préenregistrement **v8** » (seul « v10 » → « v11 » a été changé) et ligne 15 « `lecture_mecanique_v6.py` » ; rédaction v5, ligne 1 « `lecture_mecanique_v6.py` », ligne 6 « `rediger_note_lecture_v4.py` » ; la provenance de la répétition déposée (copie du fichier dans le bac à sable) n'est toujours pas dite (CV11-2 (f)). |
| CV4-1 (deux définitions de M2 ter) | **fermé** | Une seule définition (lignes 217 à 231), sans r₀ : même feuille à r₀ = 0,1 et à 0,7 sur les 64 combinaisons. |
| CV4-4 (attributions trop larges) | **fermé** | Mélange à pas fixé vérifié (point 4) ; « dérive » n'est écrit qu'en (4c), où elle est mesurée (bb > 0). |

## 2. Réponses aux points du brief

**Répétition générale.** Rejouée depuis `copie-dossier/` (la séquence efface et recrée elle-même `repetition-v11/`, ligne 59) :
30,5 secondes, code 0 (`repetition-rejouee-v11.log`, début 03:46:57 UTC).
- `effectifs-reel-v11.json` (`c05aa6fa…`), `lecture-mecanique-reelle-v11.json` (`621bbe71…`), `table-en-vigueur-v11.txt`
  (`f6e65b72…`) : identiques à l'octet aux fichiers déposés ; les cinq compagnons produits par la séquence sont conformes.
- `sortie-reelle-v11.json` : identique en tout sauf `manifeste.donnees` (`comparaison-repetition-v1.txt`). La répétition déposée a
  lu `/tmp/…/scratchpad/repetition-generale/synthetique-format-reel.npz`, pas le fichier déposé ; même empreinte `447dc136…`,
  donc même contenu (CV11-2 (f)).
- La note ne diffère que par sa ligne 3 (heure, empreinte de la sortie). Elle dit « Préenregistrement **NON SCELLÉ** (GardeArret) »
  et « **RÉPÉTITION GÉNÉRALE ou essai : aucune donnée réelle** ». Elle commence par « x, écrite après… » : l'instance passée
  (`MESURE_INSTANCE=x`) est reprise telle quelle en répétition (CV11-3 (d)). Aucun témoin, aucun journal, aucune trace
  `sortie-reelle-v11*` au premier niveau après la répétition.
- Le journal porte un avertissement `DeprecationWarning: datetime.datetime.utcnow()` à l'étape (4) (CV11-3 (b)).

**Le test de la garde et la garde en place** (`sortie-test-garde-trace-v1.txt`) : cinq cas conformes ; garde en place : 0 ;
depuis `repetition-v11/` : 3. La garde CV10-1 est fermée.

**`LECTURE_SEULE`** (`sortie-lecture-seule-v1.txt`, copie `copie-lecture-seule/`) :
- cas 0, sans `MESURE_INSTANCE` : code 1, « MESURE_INSTANCE obligatoire » ;
- A, préenregistrement non scellé : code 1 (`GardeArret`, compagnon absent) ;
- B, scellé (copie scellée par moi), sans sortie : code 6 ; C, sortie non scellée : code 6 (la ligne 48 couvre les deux) ;
- **D1, D2, D3, E, F, G : code 1 sans message, après « OK … sortie-reelle-v11.json »** — la ligne 50 (CV11-1) ; rien n'est écrit ;
- H, témoin extrait : pose 1 → 0, pose 2 → 3, garde isolée ensuite → 3.
Puis, ligne 50 réécrite en `if … fi` dans la copie (`sortie-lecture-seule-corrigee-v1.txt`) : D2 (commit ≠ manifeste) → 8 ;
D3 (empreinte des données ≠ réelle) → 1 à l'étape (3), un `.partiel` vide reste ; E (artefact : manifeste retouché, scellé sous
le nom réel) → 0, lecture et note scellées, note « une seule exécution réelle (R1) » ; F, second appel → **7**, les quatre
fichiers (lecture, note, compagnons) inchangés ; G (note et compagnon retirés) → 0, note refaite, lecture et son compagnon
intacts (date 2000-01-01 conservée) ; G ter (lecture scellée puis corrompue d'un octet) → 0 : la note est écrite depuis une
lecture dont l'empreinte ne correspond plus au compagnon.

**La branche E ≠ 60 de la séquence v11** (`repetition-E52-v11.log`, `copie-dossier-E52/`, fichier au format réel où E = 52 écrit
par `ecrire_npz_E52_v10.py` de la contre-lecture v10, qui importe `ecrire_npz_synthetique` sans modification ; empreinte du
fichier `106cb7a1…`, la même qu'en v10 ; lancé en arrière-plan avec un délai long, comme la consigne le veut) : la séquence v11 va
**au bout, code 0**, de 03:57:05 à 04:05:50 UTC (8 minutes 45 secondes, dont la table). E = 52 est lu par `--effectifs-seulement`
(K par pli 31 ou 32, L = 0,0305) ; aucun `.partiel` au départ, la ligne 84 laisse passer ; la table est refaite au E et aux
longueurs observés (manifeste : E 52, « longueurs réelles (repetition-v11/effectifs-reel-v11.json) »), écrite en `.partiel`,
renommée et scellée (`repetition-v11/table-m2bis-m4-v8-E52.json`) ; `table-en-vigueur-v11.txt` la désigne et est scellé ; la
lecture vérifie E = 52 dans la table comme dans la sortie (`manifeste_verifie`) ; la note cite la table refaite et dit « NON
SCELLÉ » et « RÉPÉTITION GÉNÉRALE » ; les six compagnons produits sont conformes (`sortie-E52-resume-v1.txt`). Verdicts de cet
essai : M1 non concluant, M2 ter (1), M3 tenu, M4 confirmé — un essai du code, sans valeur de résultat.

**La consigne de lancement** (outil en arrière-plan, 7 200 000 ms, jamais `nohup … &`, `MESURE_INSTANCE` obligatoire) est écrite
dans l'en-tête (lignes 49 à 51), le Plan d'analyse (lignes 261 et 262), l'en-tête de la séquence (lignes 4 à 7, 21 et 22) et
exigée par le code (lignes 64 et 71). Elle **suffit** : 30,5 secondes pour 5 sondes, soit au plus 6,1 secondes par sonde, frais
fixes compris : 430 sondes prendraient au plus 44 minutes, plus 10 minutes de table si E ≠ 60 ; le délai de deux heures garde
plus du double. La seule nuance : le Plan dit « ≈ 30 à 40 minutes » pour le tout, l'en-tête « environ 40 minutes » pour l'étape (2)
seule (CV11-2 (d)).

**Point 2 : M2 ter, un arbre à neuf feuilles** (`sortie-verif-cv11-arbre-v1.json`, base : la sortie de la répétition v11).
- **Partition exhaustive et sans recouvrement**, par construction : des « sinon » emboîtés sur six conditions binaires (Ville
  réelles ≤ 0,05 ; bb(D) ≤ 0 ; Ville mélange > α ; bb(D′) > 0 ; Ville pas fixé ≤ α ; bb(dérive) > 0) ; toute combinaison tombe dans
  exactement une feuille. J'ai réécrit le Seuil depuis le texte seul (lignes 220 à 230) et comparé à `lecture_mecanique_v7.lire`
  sur les 64 combinaisons × deux r₀ : **aucun désaccord de feuille, aucun désaccord d'étiquette** (les étiquettes du code sont
  mot pour mot celles du Seuil) ; feuilles atteintes : (1) 32 ; (2a) 8 ; (2b) 8 ; (3a) 4 ; (3b) 4 ; (4a) à (4d) 2 chacune.
- **Bornes** (CV6-4) : 0,05 et 0,05 + 10⁻¹² donnent (1), 0,05 + 2 × 10⁻⁹ la suite ; bb(D) = 0 ou 10⁻¹² se lit ≤ 0 ; mélange à 0,05
  n'est pas > α ; pas fixé à 0,05 est ≤ α ; bb(D′) = 0 et bb(dérive) = 0 donnent (4d), bb(dérive) = 10⁻⁹ donne (4c).
- **Réserve d'incohérence** (CV8-4, CV9-3) : posée en (2a) et en (2b) quand bb(D′) > 0, nulle part ailleurs.
- **Critères** : chaque feuille a sa ligne (M2 ter (1), (2a), (2b) deux fois, (3a), (3b), (4a), (4b), (4c), (4d) : lignes 273 à 285) ;
  chaque issue des autres énoncés aussi (M1 trois issues ; M2 contrôle ; M2 bis réfutée ; M3 fragile, audit ; M4 confirmé, non
  concluant ou réfuté, non lisible, maximum ; placebo ; cellule à zéro dans M3 et dans un bras).
- **r₀** n'est condition nulle part (même feuille à 0,1 et à 0,7).
- **Attributions** (CV6-2) : D = D′ + dérive exactement (trois différences des mêmes médianes sur le même tirage, script, lignes
  554 à 568 : `diffm`, `diffp`, `derive` sur le même `idx`, ligne 560) ; (4c) n'écrit « dérive » que si elle est mesurée ; les autres feuilles n'affirment que ce qui est mesuré.

**Point 3 : excès apparié de M4.** Le script est inchangé depuis la v8 (même empreinte, identique dans `32de42f2` et `50208ab1`).
Relu : différence **par sonde** puis médiane sur les sondes (ligne 541, point ; ligne 545, rééchantillonnage, le **même `idx`**
pour les deux termes) ; même calibrage (à τ = 0 comme dans le bras, le calibrage lit X sans effet : `calibrage_sans_effet=True`,
mêmes `perm` et `plis`, donc mêmes μ₀, σ et seuils) ; la table calcule le même excès (manifeste : « par sonde, quantité de M4
moins la même quantité à τ = 0 (même calibrage) ; médiane ») ; ses chiffres cités sont exacts : excès 0,1429 ; 0,0732 ; 0,0274 ;
0,0059 ; quantité brute (`M4_sommes_median`) 0,1937 ; 0,1238 ; 0,0748 ; 0,0545 ; maximum 0,0192 à 0,0263. Le seuil « excès > 0,02
et borne basse > 0 » ferme le faux « confirmé » de CV4-2 : un défaut de niveau commun aux deux termes s'annule sonde par sonde.
Aux bornes (`M4_bornes`) : excès 0,02 ou 0,02 + 10⁻¹² → non concluant ; borne basse 0 → non concluant, 10⁻⁹ → confirmé ; maximum
0,08 → confirmé, 0,081 → non concluant ; excès 0 ou −10⁻¹² → réfuté ; maximum 0,10 → non concluant, 0,10 + 2 × 10⁻⁹ → audit, à
r₀ = 0,5 aussi ; r₀ = 0,5 → non lisible. **Aucun nouveau faux « confirmé » ni faux blocage.** L'excès de la répétition rejouée par
`main()` (0,0473) est celui de la note déposée (0,047).

**Point 4 : mélange à pas fixé** (`sortie-verif-cv11-pas_fixe-v1.json` ; 12 sondes, E = 60, longueurs de 5 à 10 avec une invalide
au milieu des épisodes longs, pour que le « pas » soit l'indice brut). Marges par pas et masque gardés **exactement** (valeurs
triées égales à chaque pas ; moyenne par pas identique à l'origine). **Dépendance r₀ = 0,3 sans dérive** : r₀ 0,300 à l'origine,
0,003 sur le pas fixé, −0,001 sur le mélange : détruite. **Dérive linéaire (0,3 par pas) sans effet épisode** : la moyenne par
pas survit au pas fixé (−0,13 … 3,17, identique) et s'aplatit sur le mélange complet (≈ 1) ; r₀ −0,019 à l'origine (la dérive
biaise r₀ vers le bas, comme le texte le dit), −0,005 sur le pas fixé. **Rien** : r₀ ≈ 0 partout. La feuille (4c) ne peut
donc écrire « dérive » que si le mélange à pas fixé dépasse le mélange complet, ce que seule une dérive de pas produit.

**Point 5 : gardes** (`sortie-gardes-refus-essai-v1.txt`, `sortie-test-gardes-v11.json`, `sortie-verif-cv11-gardes-v1.json`).
- `--test-gardes` : **quinze entrées** (quatorze gardes et `correlation_saine`) ; le décompte de l'en-tête est exact.
- `verifier_scores_invalides` : **705 appels** pendant un `main()` en mode réel sur le fichier de la répétition (5 sondes × 141
  passages) : elle est sur le chemin réel (script, ligne 199), pas seulement dans le test.
- Refus du mode réel, vérifiés en lançant sur le fichier synthétique au format réel, **aucun octet sur la sortie standard** :
  `--effectifs-seulement` sans empreinte ou avec une empreinte fausse ; `--tirages 5` ; `--bootstrap 300` ; `--tirages 5` avec
  `--effectifs-seulement` ; sans `--commit` ; sans `--sondes-placebo` ; effectifs faux (4, 2) ; `--reel` avec `--synthetique`.
  Le cas sain écrit 807 octets identiques aux effectifs déposés.

**Point 6 : chiffres cités** (`sortie-verif-cv11-chiffres-v1.json`). Recalculés et conformes : 1 − 0,99⁵⁰ = 0,395 ; 0,0725 (T
uniforme de 5 à 10) ; 0,077 (0,0773 pour T = 8) ; 2/40 = 0,05 et rang 38 pour K = 39 ; Ville à τ = 0 : 0 ; 0,0333 ; 0,0833 ; 0,1333 ;
Ville à τ = 2 : 0,1375 à 0,1521 (« 0,138 à 0,152 ») ; M2 bis : 0,1383 ; 0,1042 ; 0,0646 ; 0,0188 ; excès, quantité brute et
maximum (point 3) ; « synthétique v8 : ≈ +0,03 pour les deux à r₀ = 0,2 » (essai v8 : r₀ 0,2015, D = D′ = 0,030) ; « quinze
entrées », « six audits », « six refus », « 3 sondes réelles, 2 placebo, E = 60 ». Toutes les empreintes de l'en-tête
correspondent aux fichiers ; tous les compagnons existent (le préenregistrement n'en a pas encore, normal). Le texte ne contient
aucun « ⟨…⟩ » ; la rédaction en écrit un seul, voulu (« ⟨À ÉCRIRE … ⟩ »).

**Point 7 : ce que je n'avais pas vu venir.** Le mode `LECTURE_SEULE` mort (CV11-1) : comme CV10-1, un mode que la répétition ne
traverse pas et qu'aucun test déposé n'exerce ; la contre-lecture v10 l'avait exercé sur la séquence v10, où il marchait, et la
correction de CV10-2 l'a cassé. Pour information, sans constat : la répétition tombe encore en (1) avec Ville à 0,050 et
bb(D) = 0,012 > 0 ; la feuille (1) se joue à une alerte près (déjà dit en v9 et v10).

## 3. Constats

### CV11-1 : `LECTURE_SEULE` sort avec le code 1, sans message, avant l'étape (3) — la reprise promise n'existe pas (sérieux ; impose une v12)

- **Où** : séquence, ligne 50 (`[ -e note-lecture-mecanique-v11.md.sha256 ] && { echo … ; exit 7; }`), dernière commande de la
  branche `LECTURE_SEULE` de `etape_0` ; ligne 23 (`set -euo pipefail`) ; ligne 66 (`compagnons; etape_0 LECTURE_SEULE`) ; texte,
  lignes 58 à 61 (« interrompue après l'étape (2) → reprise par `LECTURE_SEULE COMMIT`, qui rejoue les seules étapes (3) et (4) ») ;
  séquence, lignes 15 à 18 ; en-tête, ligne 60 (« refuse si la note est déjà scellée (CV10-2) »).
- **Problème** : quand la note n'est pas scellée — le cas pour lequel la reprise existe — le test `[ -e … ]` rend 1 ; c'est la
  dernière commande de la fonction, donc son code de retour ; l'appel `etape_0 LECTURE_SEULE` est une commande simple qui rend 1,
  et `set -e` arrête le script, code 1, sans aucun message (bash 5.2.21). Vérifié : cas D1, D2, D3, E, F, G de
  `sortie-lecture-seule-v1.txt` (le journal s'arrête à « OK … sortie-reelle-v11.json ») ; reproduction minimale dans
  `scripts/repro_set_e_v1.sh` → `sortie-repro-set-e-v1.txt` (la même fonction en `if … fi` laisse la suite s'exécuter). Quand la
  note **est** scellée, le code 7 et son message sortent bien ; mais ce cas-là n'a rien à reprendre. Le mode réel et la
  répétition ne sont pas touchés : leurs branches finissent par `printf … >> "$TEMOIN"` et `bash test-garde-trace-v11.sh`, qui
  rendent 0. Conséquences : (a) repli silencieux (R5) ; (b) une interruption après l'étape (2) ne peut pas être reprise par la
  séquence gelée ; rejouer (3) et (4) à la main serait un écart au préenregistrement scellé (nœud de décision) ; (c) le texte
  affirme un comportement que la séquence n'a pas. Rien n'est lu ni perdu (R1 tient) ; l'unique exécution n'est pas en danger.
  Second point, lié : à l'étape (3), si la lecture est déjà scellée (ligne 97), elle n'est **pas vérifiée** avant que la note
  soit écrite depuis elle (cas G ter : un octet changé passe), alors que CV10-2 demandait « la vérifier au lieu de la réécrire ».
- **Correction** (séquence v12, texte v12) : ligne 50 en `if [ -e note-lecture-mecanique-v11.md.sha256 ]; then echo … >&2; exit 7; fi`
  (vérifié dans ma copie : D2 → 8, D3 → 1, E → 0, F → 7 sans réécriture, G → note refaite, lecture intacte) — ou terminer chaque
  branche de `etape_0` par `return 0` ; relire la séquence pour tout autre `… && { …; }` en fin de fonction (il n'y en a pas
  d'autre : les lignes 44 et 48 finissent par `||`). À l'étape (3), dans le cas « déjà scellée », `verifier` la lecture avant
  l'étape (4). **Déposer un test de `LECTURE_SEULE`** (R5), comme pour la garde : sur une copie temporaire avec une sortie
  artefact scellée, cas sain (note refaite, code 0), note déjà scellée (code 7), commit ≠ manifeste (code 8) — et le faire
  lancer par la répétition. L'empreinte de la séquence change, donc l'en-tête (ligne 48) aussi : une v12 de toute façon.

### CV11-2 : restes de v10 et incohérences du texte (mineur)

- (a) Plan d'analyse, lignes 252 et 253 : la commande (1) écrit `> effectifs-reel-v10.json` et passe `--longueurs-json
  effectifs-reel-v10.json`, alors que la séquence écrit et lit `effectifs-reel-v11.json` (lignes 78, 79, 85) : le texte gelé nomme
  un fichier qui n'existera pas. Écrire `effectifs-reel-v11.json`.
- (b) Ligne 4 : « remplaçait la v9** » — un `**` orphelin ; et « selon neuf contre-lectures » (lignes 5 et 6) dans une phrase « pour
  mémoire » qui décrit la v10 : acceptable, mais le titre dit « après dix contre-lectures » ; une phrase plus courte éviterait
  la confusion.
- (c) Ligne 32 : « Commit du code d'analyse : `32de42f2` » — ce commit contient le script v8 (identique), la lecture v7, l'essai v7 et
  la rédaction v5, **mais une séquence v11 antérieure** (`332ea15f…`, différente de l'empreinte `160e0477…` citée ligne 48) et **ni la
  garde ni le test**. Les outils v11 cités par empreinte sont dans `50208ab1`, le commit du texte. Dire : « script v8 inchangé
  dans `32de42f2` ; séquence, garde, test et répétition dans le commit qui porte ce texte ».
- (d) Ligne 262 : « ≈ 30 à 40 minutes » pour toute la séquence, contre « environ 40 minutes » pour l'étape (2) seule et « environ
  10 minutes pour la table si E ≠ 60 » (ligne 52) : écrire « ≈ 40 à 50 minutes », ou ne garder que la durée de l'en-tête.
- (e) Ligne 408 : « dixième sous-agent neuf » — le contre-lecteur de la v9 est dit « huitième » (ligne 6), celui de la v10 est donc le
  neuvième (le complément v2 est du même contre-lecteur que la v1).
- (f) Reste de CV10-3 : la répétition déposée a lu `/tmp/…/scratchpad/repetition-generale/synthetique-format-reel.npz` (note déposée,
  ligne 3 ; `manifeste.donnees`), copie de `synthetique-format-reel-repetition.npz` de même empreinte `447dc136…` ; le dire en une
  demi-ligne (lignes 61 à 63), ou refaire la répétition sur le fichier déposé lui-même.
- (g) Ligne 63 : « la garde « témoin » est exercée sur l'état déposé (test déposé, R5) » — le test l'exerce sur un état **planté** qui
  imite le dépôt (dossier temporaire avec `repetition-v11/sortie-reelle-v11.json`), jamais sur le dossier déposé. Je l'ai lancée
  en place : code 0. Écrire « sur un état planté qui reproduit l'état déposé », ou ajouter au test un cas en place (voir CV11-3 (f)).

### CV11-3 : détails des outils (mineur)

- (a) Docstrings : `lecture_mecanique_v7.py`, ligne 1, « seuils gelés du préenregistrement **v8** » (écrire v11 : CV10-3 ne l'a changé
  que dans la parenthèse) et ligne 15, « `lecture_mecanique_v6.py` » ; `rediger_note_lecture_v5.py`, ligne 1, « `lecture_mecanique_v6.py` »
  (v7), ligne 6, « `rediger_note_lecture_v4.py` » ; ligne 30, défaut en dur `--date "le 28 octobre 2026"` (la séquence passe
  toujours la date, mais CV9-4 (a) visait aussi la date : le rendre obligatoire comme `--instance`).
- (b) Séquence, ligne 103 : `datetime.datetime.utcnow()` est déprécié ; un avertissement s'écrit dans le journal à chaque étape (4)
  (vu dans ma répétition). `datetime.datetime.now(datetime.timezone.utc)`.
- (c) Séquence, ligne 35 : `rm -f "$1.sha256.interdit-ecrasement"` ne correspond à rien dans `controle_ia.scellement` (qui refuse
  déjà d'écraser une empreinte différente, et est idempotent) : à retirer.
- (d) Séquence, ligne 60 : en `REPETITION`, `MESURE_INSTANCE` n'est remplacé par « répétition générale (aucune instance réelle) »
  que s'il est absent ; la note déposée commence par « x, écrite après… ». Forcer l'étiquette de répétition en mode `REPETITION`
  (`MESURE_INSTANCE="répétition générale (aucune instance réelle)"`), pour qu'une note de répétition ne puisse jamais porter une
  provenance qui ressemble à une vraie.
- (e) Séquence, lignes 91 et 92 : `table-en-vigueur-v11.txt` est écrit et scellé **après** la sortie ; une coupure entre les deux
  laisse une sortie scellée sans table en vigueur, et `LECTURE_SEULE` tombe alors sur `cat` (ligne 67) avec le seul message de
  `cat`. La table en vigueur est connue dès l'étape (1) : l'écrire et la sceller là.
- (f) Séquence, ligne 52 : en `REPETITION`, `etape_0` ne lance que le test, jamais la garde sur le dossier courant ; la phrase « passe
  par la même étape 0 … pour que la garde soit exercée » (texte, ligne 56 ; séquence, ligne 13) ne vaut que par le test. Ajouter
  `bash garde-trace-reelle-v11.sh` avant le test (en répétition, une trace réelle au premier niveau est aussi une anomalie), ou un
  cas « en place, code 0 attendu » dans le test.

## 4. Mes scripts et sorties

Tout est dans ce dossier (`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-mesure-unanime-v11/`).
Chaque script et chaque sortie a un compagnon `.sha256`. Les copies du dossier (`copie-dossier/`, `copie-lecture-seule/`,
`copie-dossier-E52/`) et les dossiers de données et de fichiers temporaires ne reçoivent pas de compagnon : la séquence scelle
elle-même ce qu'elle produit, et le reste est de travail.

| fichier | contenu |
|---|---|
| `sortie-empreintes-v1.txt` | empreintes sur disque de tout ce qui est cité ; `sha256sum -c` de tous les compagnons (dossier, `repetition-v11/`, `contre-lecture-v10/`) |
| `sortie-test-garde-trace-v1.txt` | `test-garde-trace-v11.sh` déposé ; garde en place (0) ; garde depuis `repetition-v11/` (3) |
| `heure-debut-repetition.txt`, `repetition-rejouee-v11.log`, `comparaison-repetition-v1.txt`, `depose-v11/`, `donnees-repetition/` | répétition rejouée (copie-dossier), comparaison au dépôt (copie des fichiers déposés dans `depose-v11/`) |
| `scripts/lecture_seule_cv11_v1.sh` → `sortie-lecture-seule-v1.txt` | `LECTURE_SEULE`, cas 0 et A à H, sur `copie-lecture-seule/` (scellée par moi) ; `ls-*.out` : sorties complètes de chaque cas |
| `sortie-lecture-seule-corrigee-v1.txt` | cas D2 à G ter, avec la ligne 50 réécrite en `if … fi` dans la copie seulement ; `ls2-*.out` |
| `scripts/repro_set_e_v1.sh` → `sortie-repro-set-e-v1.txt` | reproduction minimale du mécanisme de CV11-1 |
| `scripts/verif_cv11_v1.py` → `sortie-verif-cv11-arbre-v1.json`, `-chiffres-`, `-pas_fixe-`, `-gardes-` (et `.err`) | arbre (64 combinaisons, bornes, r₀, réserve, critères, bornes de M4), chiffres de la table et formules, mélange à pas fixé, compteur d'appels de la garde ; script v8 et lecture v7 importés sans modification ; graines `SeedSequence(2810202611, …)` |
| `sortie-gardes-refus-essai-v1.txt`, `sortie-test-gardes-v11.json`, `essai-lecture-mecanique-v7-reproduit.json` | `--test-gardes` (quinze entrées ; fichiers du test dans `gardes-tmp/`), neuf refus et un cas sain, essai brut reproduit à l'octet |
| `scripts/ecrire_npz_E52_v10.py` (copie du script de la contre-lecture v10) → `sortie-ecrire-npz-E52-v1.json`, `donnees-E52/`, `empreinte-E52.txt`, `heure-debut-E52.txt`, `repetition-E52-v11.log`, `sortie-E52-resume-v1.txt`, `copie-dossier-E52/` | branche E ≠ 60 de la séquence v11 en répétition (début et fin dans `heure-debut-E52.txt`) |

Empreinte de ce rapport : dans `rapport-contre-lecture-mesure-unanime-v11.md.sha256`, à côté (un fichier ne peut pas contenir sa
propre empreinte). Durée : 26 minutes 50 secondes, de 03:39:47 à 04:06:37 UTC, la branche E ≠ 60 comprise.

Fin : 2026-10-28 04:06:37 UTC (`date -u`, relevé dans un appel séparé avant l'écriture de cette ligne).
