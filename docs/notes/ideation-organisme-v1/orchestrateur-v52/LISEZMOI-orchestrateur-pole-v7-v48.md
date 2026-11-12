# Orchestrateur du pôle, v7 — version 48 : étage de tests de mort sur processeur seul (décision de Lazar R-776 (a))

Lignée conv-audit (sous-agent), 29 octobre 2026. v1 à v47 gardées (R12) : LISEZMOI et EMPREINTES v1 à v47 intacts.
Source : décision de Lazar R-776 (a) — les cinq meilleures fiches du classement passent à des agents expérimentateurs qui
exécutent, sur processeur et sur les données déjà là, le test de mort de la fiche ; prédiction scellée avant exécution,
lecteur neuf, résultat **exploratoire**. Reprise d'un travail interrompu (section dédiée plus bas).

**v48 n'est pas contre-lue.**

**Aucune session réelle, aucune dépense, aucun réseau, aucune clé, aucun `bwrap` exercé** : faux kit, faux exécuteurs et
garde-fou d'essai qui refuse toute connexion hors boucle locale. Le bac à sable réel (`bwrap`) n'est pas installé sur la
machine de cette version : sa commande est vérifiée en structure seulement (voir « Ce qui n'est pas vérifié en réel »).

**Rétrocompatibilité (prouvée par empreintes).** Sans `--tests-de-mort` (défaut 0 = étage absent), les sorties de la v48 sont
celles de la v47 **octet pour octet**. Preuve rejouée à la reprise : l'arbre de la v47 (`EMPREINTES-…-v47.txt` vérifiées, 169
lignes OK, 444 essais OK) a été copié hors du dépôt ; la même course de référence (faux adaptateur, deux proposeurs, deux
juges, seconde passe, sans l'option) a été jouée avec la v47 gardée puis avec la v48, dans deux dossiers provisoires
différents ; chaque fichier de la sortie (50 dans chacune, mêmes chemins) a été haché, le chemin du dossier provisoire étant remplacé par un
jeton : **tous les fichiers sont identiques, sauf `manifeste-depart.json` et `manifeste-fin.json`** (et leurs `.sha256`),
dont seules diffèrent la table `code_sha256` (empreintes des modules `adaptateurs.py`, `ideation.py`, `protocole_outils.py` ;
nouvelle entrée `tests_de_mort.py`) et l'empreinte de `liste-blanche.json`, qui contient le chemin du dossier provisoire et
change d'une course à l'autre, v47 contre v47 comprise. Les empreintes de `classement.json`, `fiches-validees.json`,
`notes-par-juge.json`, `lecture.json`, `classements-par-juge.json`, `noyau/modeles.json`, des consignes des proposeurs (passes
1 et 2) et des juges, et du dictionnaire `reglages_kit` du manifeste de départ sont de plus gelées dans `TestV48`
(`SORTIES_V47_SHA256`, `CONSIGNES_V47_SHA256`, `REGLAGES_KIT_V47_SHA256` ; essai `test_v48_11`). Aucune clé de l'étage
n'apparaît aux manifestes de départ et de fin sans l'option (`tests_de_mort`, `tests_de_mort_exploratoires`,
`cout_etage_tests_usd`, `etage_tests_*` des sommes). Les rôles de l'étage vivent dans `ROLES_ETAGE_TESTS`, **hors de
`ROLES`** : le jeu de rôles du kit de la v47 est inchangé.

## Ce que fait la v48

| point | ce qui est fait | essai |
|---|---|---|
| option | `--tests-de-mort N` (0 à 12, défaut 0) : l'étage joue sur les **N premières fiches éligibles du classement figé**, dans l'ordre du classement ; jamais sur le verdict d'un test (N-053) | `test_v48_01`, `test_v48_11` |
| classement figé | avant la première session, `noyau/tests-de-mort/classement-fige.json` : empreinte du classement scellé, fiches retenues dans l'ordre ; après l'étage, le classement doit avoir la même empreinte et le sceau intact ; sinon **arrêt** « classement.json modifié pendant l'étage » (manifeste de l'étage et de fin le disent) ; l'étage ne relit jamais le classement pour choisir | `test_v48_01`, `test_v48_09` |
| préenregistrement court | par fiche, **écrit et scellé par le noyau** (`prereg-court.json`) avant toute session : hypothèse, prédiction (valeur et signe), métrique, seuil gelé (comparateur et valeur lus du texte du seuil, sinon donnés par le signe de la prédiction), données (chemins et empreintes dans la tranche), plan d'analyse, liste d'arrêt, extraits de la fiche. **Refus à l'étage, motif consigné, aucune session** si un champ manque, si le seuil ou la prédiction n'est pas chiffré, ou si une donnée n'est pas dans la tranche exploratoire. Ordre prouvé par le journal numéroté (`prereg-court-scelle` avant `session`), par les dates des fichiers et par l'empreinte du préenregistrement écrite dans la consigne de l'expérimentateur | `test_v48_01`, `_02`, `_03`, `_16` |
| champ de la fiche | champ facultatif `test_de_mort` `{seuil, test, donnees}` au gabarit **seulement sous l'option** (gabarit, fiche maximale et consigne de proposition portent alors la tranche) ; hors option, le champ est « hors gabarit » comme avant ; borné (seuil 200, test 3 000, 12 données, chemin 300) | `test_v48_15`, `test_v48_11` |
| tranche exploratoire | `--tranche-exploratoire DOSSIER`, **lecture seule**, chargée comme un dossier fermé : `index.json` scellé et présent dans la liste blanche, empreintes des fichiers, fragments interdits (dont `donnees`) ; son empreinte d'index entre au manifeste de départ ; l'étage refuse si elle diffère de celle de la course | `test_v48_03`, `_13` |
| rôle expérimentateur | Claude par le kit (`--experimentateur ETIQUETTE=MODELE`) ou Argon par protocole (`--experimentateur-externe`, commande externe) ; **même consigne** pour les deux (essai de comparaison octet pour octet) ; **aucun outil du kit** (`tools=[]`, effort `high`) ; il demande au noyau, par un bloc `{"experience": […]}`, de lire un fichier de la tranche, de lire une page du dossier fermé, ou d'**exécuter un script** ; les réponses reviennent au tour suivant entre délimiteurs (données, jamais consigne) ; fin par `{"fin": …}` | `test_v48_01`, `_18`, `_19` |
| exécution | le script est exécuté **par le noyau**, sous `bwrap` : `--unshare-all --unshare-net --clearenv --die-with-parent`, système de fichiers du conteneur en lecture seule (`--ro-bind /usr`, `--remount-ro /`), **un seul dossier inscriptible** (le dossier de travail de la fiche), la tranche liée en lecture seule, `python3 -I -B`, `RLIMIT_AS` et `RLIMIT_FSIZE`, groupe de processus tué au délai. **Sans `bwrap` : refus de l'étage avant tout appel, aucun repli** sur un autre exécuteur. Script, sortie standard, sortie d'erreur, résultat et fichiers produits sont scellés par exécution | `test_v48_04`, `_05`, `_07`, `_12` |
| quotas | par fiche : 3 exécutions (`--executions-par-fiche`), 120 secondes chacune (`--delai-execution-s`), plafond de session `--budget-test-usd` (0,5) ; une seule exécution par tour (la seconde du tour est refusée et comptée) ; une demande refusée compte ; clé étrangère, type inconnu, script vide, trop long (20 000 caractères) ou à caractère nul refusés avec leur motif ; plafond de la fiche atteint → fin des tours, verdict sur ce qui a été exécuté | `test_v48_06`, `_19`, `_20` |
| lecture mécanique | le noyau lit la **dernière ligne `RESULTAT: <nombre>`** de la **dernière exécution réussie** et applique le seuil gelé ; une exécution tuée ou échouée ne compte jamais, même si elle a imprimé un résultat avant de mourir | `test_v48_04`, `_07`, `_16` |
| rôle `lecteur_test` | session neuve par fiche, sans outil (effort `medium`) : voit le préenregistrement, les exécutions scellées et leurs lignes de résultat ; répond `VERDICT: survit | éliminée | non concluant ; chiffre: … ; ligne: …` ; **seuil gelé seulement**. Toute réponse hors des trois mots, plusieurs verdicts, ou un verdict qui **contredit la lecture mécanique** (R4) vaut « non concluant », le désaccord est consigné | `test_v48_08` |
| résultats | manifeste de fin, section **« tests de mort (exploratoires) »** (`tests_de_mort_exploratoires` : statut, comptes, refus à l'étage, classement intact, coûts) ; `manifeste-tests-de-mort.json` scellé ; `noyau/tests-de-mort/materiau-tests-de-mort.md` (comptes et étiquettes, jamais le détail des sorties). **Jamais servis aux juges de la même course** (les juges ont rendu avant la première session de l'étage ; essai : aucune consigne de juge ne porte `VERDICT`, `RESULTAT:` ni la section) ; servis **en matériau à la génération suivante** | `test_v48_01` |
| refus de modèle (R-764) | les trois barrières de la v47 s'appliquent aux deux rôles : options du kit sans repli de modèle, modèle servi lu par le noyau (statut « refus », sortie mise à l'écart dans `A-L-ECART-modele-non-autorise/`, dépense à part, jamais « budget dépassé »), modèles de l'étage inclus dans les modèles permis au relais | `test_v48_10` |
| sommes | les plafonds de l'étage (fiches × (expérimentateur + lecteur)) entrent dans la somme des plafonds Claude, ou externe pour un expérimentateur d'Argon ; refus avant tout appel si le total ne suffit pas ; plafond total atteint pendant l'étage → arrêt nommé ; coûts de l'étage dans le journal de la course | `test_v48_14`, `_18` |
| juge externe | classement issu du bras : l'étage est **différé** (statut « différé » au manifeste de fin), puis joué par le lanceur **après le bras** (`--bras-rapporte-differe --tests-de-mort …`), sur le classement du bras, avec la même liste blanche (sinon refus avant tout appel) | `test_v48_21` |
| réglages | `verifier_reglages` (sonde du bac à sable, plafonds, consignes de contrôle avec tranche et champ au pire cas) et `--mesurer-consignes` (plus grosse consigne de l'expérimentateur et du lecteur, sans appel ni sonde) | `test_v48_14`, `_17` |

**Options nouvelles du lanceur** (toutes refusées avec code 2 si `--tests-de-mort` est 0 ou absent) : `--tests-de-mort N`,
`--tranche-exploratoire DOSSIER`, `--experimentateur ETIQUETTE=MODELE` **ou** `--experimentateur-externe ETIQUETTE=MODELE`
(exactement un), `--lecteur-test ETIQUETTE=MODELE` (étiquette différente de l'expérimentateur), `--budget-test-usd` (0,5),
`--budget-lecteur-test-usd` (0,1), `--executions-par-fiche` (3), `--delai-execution-s` (120), `--memoire-test-mo` (1 024),
`--executeur-tests bwrap|factice` (défaut `bwrap` ; `factice` réservé au moteur simulé, refusé avec le moteur réel).

## Essais R5 de l'étage (classe `TestV48`, définie avant `unittest.main()`)

Cas sain **et** artefacts pour chaque garde, aucun repli silencieux :

- **Bac à sable (sonde `disponible()`)** : cas sain (`print("OK")` passe) ; artefact réseau (le noyau ouvre un écouteur sur la
  boucle locale, le script s'y connecte : un exécuteur qui laisse passer est **refusé**) ; artefact système de fichiers (une
  écriture hors du dossier de travail qui réussit fait **refuser** l'exécuteur). Deux faux exécuteurs sans isolation (aucune ;
  réseau seul) sont refusés avant tout appel ; `bwrap` absent est refusé, et l'étage direct sur une course déjà faite aussi.
- **Échecs visibles** : script réseau (code non nul, erreur dans la sortie d'erreur scellée, verdict « non concluant » même s'il
  imprimait un résultat plus loin) ; écriture hors du dossier (système de fichiers en lecture seule, rien créé ailleurs) ;
  écriture dans le dossier de travail (réussit, fichier produit scellé) ; délai dépassé (tué, processus mort, « non concluant »).
- **Quotas** : quatrième demande et seconde du tour refusées et comptées ; script non lancé pour un refus.
- **Étage** : fiche sans champ, seuil flou, prédiction floue, données hors tranche (absentes, remontée de dossier, `donnees/`,
  chemin absolu, mélange) refusées à l'étage sans session ; classement modifié pendant l'étage → arrêt ; étage jamais rejoué ;
  session de l'expérimentateur ou du lecteur en erreur → arrêt nommé, manifestes écrits ; classement illisible → étage refusé,
  rien payé, course close normalement ; plafond de la fiche ; lecteur muet, contredisant ou d'accord.
- **Un essai réel conditionnel** (`test_v48_22`) : joué **seulement** si `bwrap` est installé (sinon ignoré, dit comme tel) ; il
  exige que la sonde passe sur le vrai bac à sable et refuse un exécuteur non isolé. **Non rejoué ici.**

## Reprise d'un travail interrompu deux fois par des limites d'usage

La v48 a été commencée deux fois sans être finie. À la reprise : l'arbre de la v47 a été vérifié (169 empreintes OK, 444 essais
OK) ; le brouillon (`pole/tests_de_mort.py`, 1 153 lignes, et un patch sur `demonstrations/ideation_v1.py`,
`essais/test_v7_ideation.py`, `pole/adaptateurs.py`, `pole/ideation.py`, `pole/protocole_outils.py`) a été appliqué sans
rejet, **puis relu et vérifié, non pris pour acquis** : (1) suite complète (466 essais) ; (2) **sondage de mutation** de
dix gardes (quota d'exécutions, une exécution par tour, classement figé, accord entre lecteur et lecture mécanique, sonde
réseau, données hors tranche, seuil non chiffré, ordre « préenregistrement scellé avant la session », arrêt au délai, réponse du
lecteur hors des trois mots) : chaque mutation a fait échouer au moins un essai de `TestV48` (aucune garde n'est un essai
décoratif) ; (3) comparaison octet pour octet avec la v47 (ci-dessus) ; (4) une course complète du lanceur à cinq fiches
(`--nombre 4` par proposeur, `--tests-de-mort 5`, exécuteur factice) : cinq fiches testées, classement intact, matériau écrit.
**Nom du rôle** : la décision parle du rôle « expérimentateur » ; le rôle du cycle de recherche portant déjà ce nom (avec des
outils du kit), celui de l'étage s'appelle **`experimentateur_test`** (et `lecteur_test`), pour ne jamais en hériter les outils.

## Ce qui n'est pas vérifié en réel

- **`bwrap` dans le conteneur de session-depot** : présence, droits (espaces de noms non privilégiés), version. Absent de la
  machine de cette version : aucune exécution réelle du bac à sable, seulement sa commande (drapeaux, montages, ordre
  `--bind` puis `--remount-ro`) et le comportement des exécuteurs factices.
- **Effet réel de `--remount-ro /`, de `--unshare-all --unshare-net`, de `RLIMIT_AS` et de `RLIMIT_FSIZE`**, et du groupe de
  processus tué au délai, sous `bwrap` : à constater par l'essai réel conditionnel et la sonde.
- **Jeu de montages suffisant pour le `python3` du système** (`--ro-bind /usr`, liens `/lib`, `/lib64`, `/bin` selon la
  distribution, bibliothèques de l'interpréteur) : SUPPOSÉ ; si le script ne démarre pas, la sonde échoue et l'étage est refusé
  (jamais de repli).
- **Cas réel d'une session de l'expérimentateur ou du lecteur** (qualité des scripts, respect du format `VERDICT:`), temps et
  coût réels : tout l'essai est joué par des faux. Les plafonds par défaut (0,5 et 0,1 dollar par fiche) sont des **suppositions**.
- Le statut des résultats est **exploratoire** : aucun chiffre de l'étage n'est opposable ; il n'entre dans aucun préenregistrement
  de production.

## Devis (SUPPOSÉ ; aucune dépense ici)

Aux plafonds par défaut, **cinq fiches** : 5 × (0,5 + 0,1) = **3,0 dollars au plus** (c'est le plafond, donc le pire cas ; le
coût attendu est inférieur ; le chiffre **≈ 3 dollars est SUPPOSÉ**, non mesuré), en plus du devis de la course qui l'emploie. Les totaux doivent couvrir l'étage :
`--budget-total-usd` + 3,0 (ou `--budget-externe-usd` + 2,5 si l'expérimentateur est Argon, le lecteur restant Claude à 0,5).
Épreuve proposée, sous GO séparé : (1) chez session-depot, `bwrap` présent, essai réel conditionnel ; (2) course simulée avec
`--executeur-tests bwrap` (0 dollar) ; (3) une course réelle courte avec `--tests-de-mort 5`.

## Essais

**466 essais** (444 en v47 ; + 22 `TestV48` dans `essais/test_v7_ideation.py`, avant `unittest.main()`, dont un conditionnel à
`bwrap`, ignoré ici), 0 échec, deux exécutions complètes sur l'arbre final, aucun processus survivant, `essais/_tmp` et
`__pycache__` retirés. Fichier nouveau : `pole/tests_de_mort.py`, ce LISEZMOI, les EMPREINTES v48. Fichiers changés :
`pole/protocole_outils.py` (demandes et quotas de l'expérimentateur), `pole/adaptateurs.py` (rôles de l'étage, hors `ROLES`),
`pole/ideation.py` (gabarit, validation, réglages, étage joué après le classement et après le bras),
`demonstrations/ideation_v1.py` (simulateur de l'étage, options, validations), `essais/test_v7_ideation.py`.

```
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v48.txt
```
