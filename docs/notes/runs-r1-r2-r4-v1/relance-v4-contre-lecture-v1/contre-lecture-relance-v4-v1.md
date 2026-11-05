# Contre-lecture neuve (R2) de la relance v4 de R1 — addendum v4 brouillon 1, code, scripts, devis — v1

- Contre-lecteur neuf (sous-agent, Opus 5.5) : je n'ai écrit ni R1, ni ses addenda, ni son code, ni le diagnostic, ni le
  brouillon v4. Consigne `docs/notes/runs-r1-r2-r4-v1/consigne-contre-lecture-r1-v4-v1.md`
  (`5a1523c0ea34afbc0fe6b454f362908be5405e3fc2756f831076301425fd47c1`, vérifiée par `sha256sum` avant lecture).
- Dates (UTC, `date -u`) : début 2026-11-04 06:04:59 ; fin de rédaction 06:19 (dernière ligne).
- Pièces : branche `prep/r1-relance-v4`, commit `e395c72e813b26592e97da34616b1a56e8045dec`, arbre `/home/claude/wt/r1-v4/`
  (lecture seule, arbre propre). Les dix compagnons `.sha256` du commit sont conformes (`sha256sum -c`) ; les empreintes
  du rapport de rédaction, § 7, égalent celles des fichiers ; empreintes canoniques recalculées : réparation
  `a5a61077…`, rejeu `a3ef1bac…` (égales à l'addendum) ; les deux configurations réelles passent leurs gardes
  (`exiger_config`).
- Recoupement par le seul `fetch` permis : `git fetch origin 4b47db7b` refusé (abrégé) ; refait avec l'empreinte
  complète `4b47db7b376494017e9094276ae4fa027dfdf3f9` (même objet, trouvée dans `registres/`) ; texte scellé du
  complément `049f20ba98da75539220bd4a520dd03a3df8c16a81193cc6a4e1a650783f62ca` et configuration `1b6f943c…`, égaux à
  leurs compagnons.
- Essais rejoués dans une copie (`…/scratchpad/r1-v4-copie`) : `tests/test_resolution_graine_lot_v2.py` et
  `tests/test_rejeu_activations_v4.py` : **16 passed** (176,7 s) ; collecte des 23 fichiers de `CIBLES` : **358
  collectés** (sans tokeniseur de Llama 3.1 : le nombre passé reste à établir).
- **Exposition déclarée** : en lisant le § 6 du rapport Fable (demandé par la consigne), j'ai vu des bornes basses et un
  compte « mention par épisode » de la v3 (condition 3 de ce paragraphe). J'ai lu aussi les critères de lecture du texte
  scellé `prereg/analyse-par-episode-v1.md` (`26a3ff72…`, l. 25-35 et 100-135 ; un texte d'analyse, non une sortie).
  Aucun tableau d'activations, score, sortie d'analyse ni verdict R13 n'a été ouvert. Rien de cela n'entre dans un seuil.

## Verdict

**Scellable après couples** (15 couples, `couples-contre-lecture-relance-v4-v1.json`, chaque « ancien » unique dans le
brouillon 1, libellés lus par le script et marqueur « À REMPLIR » intacts après application), **plus quatre ajouts de
code et les épreuves d'avant le scellement** (I1, I2, I4, I5 ci-dessous). Un bloquant (B1, lecture de « Confondu »)
se corrige par deux couples ; aucun seuil, aucune analyse ni hypothèse n'a besoin de changer.

## Bloquant

**B1. « Confondu » par épisode promu après coup.** Le brouillon le déclare « issue **conclusive**, rapportée **à
égalité** avec la lecture par action » (l. 138-140, et ligne des critères, l. 221). Le texte scellé de l'analyse par
épisode dit l'inverse : « Classe par épisode ≠ classe par action de la principale : lectures divergentes : les deux
rapportées ensemble ; **la principale reste la lecture principale** », et « ce qu'aucune issue ne permet : […] promouvoir
une descriptive ». C'est une règle de lecture changée, contraire à un texte scellé et à la propre phrase du brouillon
(« textes des trois analyses scellées […] inchangés »), écrite après que le signe de la v3 est connu (V4-E2) : c'est
exactement ce que R1 interdit. La consigne demandait seulement « « Confondu » par épisode comme issue possible ».
Correction : couples 1 et 2 (issue possible, lue selon l'analyse scellée, préséance comprise ; rien d'ajouté).

## Importants

**I1. Risque 1, empreinte de la table v4 (question 2). La règle juste** : une entrée d'un run décisif dont l'empreinte ne
peut pas être citée d'avance reste sous le même texte si (a) c'est la sortie d'un code scellé appliqué à des pièces citées
d'avance, sans paramètre libre ; (b) construction et usage s'enchaînent sans lecture ni décision humaine ; (c) l'usage
vérifie, avant toute lecture, chaque élément contre un oracle fixé d'avance **et** la chaîne vers sa source ; (d) la
réception recalcule l'entrée depuis sa source scellée et exige l'égalité à l'octet. Alors une troisième session sous texte
neuf n'ajoute rien : elle insérerait même une décision humaine entre la table et le rejeu. Elle ne s'impose que si
l'enchaînement est rompu. **Ce qui manque ici** : (a) et (b) tiennent (script d'une seule traite, réparation → table →
rejeu) ; (c) tient pour les identifiants (empreinte de P3), **pas pour l'ensemble `non_resolu`** : ni
`rejeu_activations_v4` ni le script ne comparent `resultat_reparation_sha256` au résultat de la session, ni les entrées
aux retrouvées. Une retrouvée rétrogradée en `non_resolu` passerait (essai absent de `test_rejeu_activations_v4.py`) ;
(d) n'est pas écrit. Correction : couple 3 (garde de chaîne, recalcul à la réception) et le code de la garde, cas sain et
artefact.

**I2. Gardes de dépense (question 5) : non éprouvées, voie impossible telle qu'écrite.** V4-E12 prévoit « TERM au processus
par son PID, poussée, destruction ». Or le complément scellé établit : « Aucun signal par numéro de processus dans ce
texte, fait constaté : […] aucune clé d'accès au conteneur […] aucun accès à l'instance n'a été éprouvé » (mode « args »).
Les deux tâches n'ont ni armement écrit, ni formule d'heure de destruction, ni épreuve R5 (le complément en exigeait
quatre, C-3 et C-4, plus une lecture filtrée des journaux, C-5). Aucun code ne les porte, aucun essai ne les éprouve. Le
plafond d'amorce (2 200 min) ne borne pas la dépense : l'instance survit à son amorce. Correction : couples 4 à 6
(destruction par l'identifiant seulement ; `H` calculé sur 57 USD moins les dépenses imputées, sessions et reprises
comprises ; armement, épreuves et filtre du complément, seuils 45 et 57 ; perte de ce qui n'est pas poussé, déclarée).
Les épreuves se font avant chaque création. Chiffres du devis vérifiés : 215/60 × 1,40 = 5,02 ; 2 235/60 × 1,40 =
52,15 ; somme 57,17 ; central 6,5 à 8 et témoin non exact ≈ 11 cohérents avec le diagnostic (95 403 passes × 89,6 ms ≈
2,37 h). Aucune dépense n'est encore imputée à GO-2026-11-03-03 (`registres/depenses.md`).

**I3. Surveillance.** Le brouillon ne réécrit pas la surveillance ; « ce que cette section ne cite pas vaut tel quel » ferait
valoir la règle de la v3 (« une autre valeur lue au journal [que 600 et 720] fait détruire l'instance »), qui détruirait
une instance v4 saine. Correction : couple 7 (valeurs v4 : 180/120, 2 200/2 100, 358, 89 et 28, ligne de la table).

**I4. Ce qui manque avant le scellement (question 4).** (1) Pré-vol sur les vraies pièces (89 cibles, 28 lots, lots 2 et 13
entièrement connus, captures recalculées égales aux fiches, 8 captures dans le lot 2) : non fait. (2) « 358 passed » avec
le tokeniseur au commit cité : non établi (358 collectés, vérifié). (3) C1 et C2 recoupés avec le texte scellé
`4b47db7b` : **concordants** (272 pour `combinaisons_max`, `_validation` et `_lot`, 16 et 2 ; 14 400 et 259 200 s pour le
cœur et le lot) ; la configuration diffère de celle du complément scellé par les clés v4, et aussi par
`episodes_resolution` vidée et `episodes_resolution_lot` retirée, non déclarées (couple 13) ; V4-E3 dit le texte
« non lisible » (couple 12). (4) Répétition jouet de bout en bout des deux sessions : non faite (la v3 l'avait avant son
scellement) ; aucun cas sain de la session 2 au niveau du script, aucun essai de l'amorce (plafond hors bornes, `SESSION`
inconnue, seconde exécution), aucun artefact « témoin arrêté » ou « sceau du témoin faux ». (5) Banc rejoué en entier sur
les essais finaux (la passe 4 tournait sur 15 essais, non 16). Correction : couple 8 (conditions d'avant le scellement).

**I5. Risque 2, lecture « exact » et indépendance des lignes (question 3).** « Exact » repose sur des égalités de jetons
(argmax de p / q, choix contraints) et sur les seules 8 captures au bit du lot 2 ; le lot 13 n'en a aucune. C'est assez
pour **choisir une voie** (l'empreinte de P3 reste le seul juge : une lecture fausse coûte du temps, jamais une entrée
fausse), pas pour dire le calcul en lot égal au bit. L'indépendance d'une ligne par rapport au contenu des autres n'est
éprouvée que sur processeur, et le code de réparation ne garde que des agrégats par lot (`lots_rapport`), d'où rien ne
peut la contredire sur la carte. **Le texte doit dire d'avance** : l'indépendance est une hypothèse d'efficacité, non de
validité ; elle est mesurée (accord des lignes connues et captures, avant et après le premier échec d'une cible) ; sa
contradiction, ou celle de la lecture « exact » pendant la réparation, donne une réserve d'instrument rapportée par
lot, sans changer aucune entrée ni aucune classe, sans changer de voie en cours de route, et sans course de plus sous ce
texte. Correction : couples 9 à 11 et la mesure dans `lots_rapport` (code).

## Mineurs

- **M1.** V4-E1 : l'option citée vient de la consigne du développeur, non du mot de Lazar ; citer n° 404 (`4a525a52…`)
  (couple 15). Le verbatim et la ligne v3 l. 234-235 sont exacts (vérifiés).
- **M2.** P-R5 à 97 % ; la clé `p_r5_au_moins_90_pour_cent` du code reste à 90 % : dire laquelle porte la réserve
  (couple 14).
- **M3.** Session 2 : le délai externe de chaque étape (2 100 min) laisse moins de 100 min à la table et au rejeu sous le
  plafond de 2 200 min si la réparation l'épuise ; une coupe donnerait « echec » et un texte neuf. À déclarer, ou à
  abaisser à ≈ 2 000 min pour la réparation.
- **M4.** Le script ne pousse qu'à la fin d'une étape ; une destruction pendant une réparation longue perd tous les
  épisodes consignés. Une poussée par lot serait plus sûre (hors couples).
- **M5.** R3 par configuration (`exiger_execution_unique`) ne voit que les manifestes du clone ; entre instances, ce sont
  la branche neuve et V4-E16 qui protègent. V4-E16 : dire quel signe montre qu'un manifeste a été écrit (ligne
  « étape reparation : run … » du journal).
- **M6.** Banc : ajouter des mutations des gardes non couvertes (`exiger_temoin`, `exiger_comptes_attendus`,
  `exiger_execution_unique`, « en trop » de `classer_episodes_v4`, version de `charger_table_v4`, et la future garde de
  chaîne).
- **M7 (remarque, sans couple).** « Témoin non exact → passe forcée seule » est dominé en couverture par « lot, puis
  repli à une cible, puis passe forcée » (qui contient la passe forcée), pour ≈ 2,5 h de plus. Le diagnostic (§ 6.1)
  proposait de garder le lot. La consigne a fixé l'autre règle ; c'est à conv-audit de trancher avant le scellement.

## Question 6 — banc de mutations

**Oui, neutralisée.** Le cas sain obligatoire (copie non mutée : tous les essais visés passent, sans « error » ni
« skipped », sinon « banc faux », code 2) est construit comme chaque mutante (`copier`). Une erreur d'installation
arrête donc le banc au lieu de passer pour des « tuées ». En plus, « tuée » exige « failed », non « error » : une
mutante qui casse l'import compte comme survivante, ce qui va dans le sens prudent. La passe 1 est rapportée, et le
défaut est corrigé dans le banc. Reste : le bilan « 15 sur 15 » combine deux passes (4 et 5) faites sur des essais
différents (15 puis 16). Il faut une passe entière au commit cité (I4).

## Question 5 — gardes, graines, arrêts

- R5 : les gardes du module ont leurs cas sain et artefact dans les essais (16 passés). Les gardes du script : un cas
  sain (session 1, jusqu'aux tests) et huit artefacts. Il manque le cas sain de la session 2, l'amorce et les tâches de
  dépense (I2, I4).
- R9 : aucun tirage propre (graines de P3 redérivées par `SeedSequence`, échantillon d'équivalence recalculé et
  comparé) ; l'échantillon de fidélité prend l'entropie et la clé de la v3, et son changement est déclaré (V4-E9).
- R10 : `kill -TERM "$PID_RUN"`, `timeout` par étape, destruction par l'identifiant : conformes. La voie « TERM par PID
  depuis une tâche planifiée » n'existe pas (I2).

Fin de rédaction : 2026-11-04 06:19:22 UTC (`date -u`).
