# Orchestrateur du pôle, v7 — version 49 : corrections de la contre-lecture CL13 (confinement de l'étage, modèle servi, moissonneur)

Lignée conv-audit (sous-agent), 30 octobre 2026. v1 à v48 gardées (R12) : LISEZMOI et EMPREINTES v1 à v48 intacts (aucun
fichier scellé d'une version précédente n'est modifié).
Source : `contre-lecture-cl13-orchestrateur-v48-v1.md` (Claude Opus 5.5, sous-agent neuf, R2) : verdict « lançable après
corrections », 12 constats (CL13-01 à CL13-12), dont deux critiques (CL13-01, CL13-02). Les douze sont traités ci-dessous.

**v49 n'est pas contre-lue.** Elle corrige une contre-lecture ; elle n'a pas été relue par un sous-agent neuf.

**Aucune session réelle, aucune dépense, aucun réseau, aucune clé, aucun `bwrap` exercé.** `bwrap` est absent de cette machine :
tout ce qui dépend du vrai bac à sable est vérifié **en structure seulement** (commande, drapeaux, montages, logique de la
sonde sur des sorties données, plomberie du noyau avec un faux `bwrap` qui ne confine rien) ; les deux essais réels sont
écrits et conditionnels (`skipUnless(bwrap)`), **jamais joués ici**. Toutes les sondes d'évasion des essais visent des cibles
factices dans des dossiers provisoires, jamais le vrai `/usr`, `/etc` ou `/root`.

**Rétrocompatibilité.** Sans `--tests-de-mort`, les sorties de la course de référence restent celles de la v47 octet pour octet
(empreintes gelées `SORTIES_V47_SHA256`, `CONSIGNES_V47_SHA256`, `REGLAGES_KIT_V47_SHA256`, essai `test_v48_11`, rejoué et OK).

## Constat → correction → essai

| constat | correction | essai |
|---|---|---|
| **CL13-01** (critique) : le script garde les capacités du superutilisateur et remonte en écriture `/usr`, `/etc/alternatives`, la tranche | `commande()` : `--unshare-user` (obligatoire, pas la variante « -try »), `--uid 65534 --gid 65534`, `--cap-drop ALL`, `--new-session` ; un seul montage inscriptible (`--bind <travail> /travail`) ; la tranche n'est liée que si c'est un vrai dossier (`lstat`, jamais un lien) ; aucun `--cap-add`, `--dev-bind`, `--bind-try`, `--tmpfs`. **Sonde des privilèges** (R5) : un script joué dans le bac lit `CapEff`, `CapPrm`, l'identité, tente de remonter `/travail/tranche` et `/`, tente d'écrire dans la tranche ; `evaluer_sonde_privileges` refuse capacités non nulles, identité 0, remontage réussi, écriture réussie, script joué hors du bac, code ≠ 0, ligne manquante ou illisible ; l'écriture dans la tranche est aussi vue côté noyau (fichier témoin). Pas de `start_new_session` pour l'exécuteur réel (`bwrap --new-session` fait `setsid`, refusé à un chef de groupe) : arrêt par `killpg` (erreurs ignorées) puis `kill`, appuyé sur l'espace de processus et `--die-with-parent` | `test_v49_01`, `_02`, `_03` ; réel : `test_v48_22`, `test_v49_19` |
| **CL13-02** (critique) : le noyau écrit le script « à travers » un lien posé par le script et écrase un fichier de l'hôte | le noyau n'écrit plus jamais dans un chemin que le script peut atteindre : **dossier de travail neuf par exécution** (`execution-NN/travail`, créé par `mkdir` exclusif) ; écriture du script et copie de la tranche par `O_CREAT|O_EXCL|O_NOFOLLOW` puis `lstat` (fichier régulier, un seul nom, taille attendue) ; dossiers intermédiaires vérifiés par `lstat` ; un dossier ou un lien déjà là fait **arrêter l'étage** (manifestes écrits) | `test_v49_05`, `_06` |
| **CL13-03** (haute) : copie des produits en suivant les liens (`/proc/self/environ`, fichier secret de l'hôte) | inventaire par `scandir` + `lstat` ; seuls les fichiers **réguliers** sont ouverts, par descripteur de dossier avec `O_NOFOLLOW`, `O_NONBLOCK`, `O_NOCTTY` puis `fstat` ; liens, tubes, prises, périphériques sont **consignés avec leur genre** (« non copié : lien vers … »), jamais suivis ni ouverts ; le lecteur voit les noms et les genres | `test_v49_07`, `_08` |
| **CL13-04** (moyenne) : un tube nommé bloque le noyau sans fin, sans manifeste | même inventaire (un tube n'est jamais ouvert) ; borne du nombre d'entrées parcourues ; noms invalides (octets non UTF-8, caractères de contrôle) et noms trop longs consignés sans erreur ; essai gardé par une alarme (un blocage fait échouer, pas geler) | `test_v49_05`, `_07`, `_08` |
| **CL13-05** (moyenne) : R-764 sans contrôle du modèle servi pour Argon | la commande externe rend `modele_servi` (et `refus` facultatif) ; le noyau le compare au modèle demandé (identifiant exact ou suffixe de date) : statut « refus », texte jamais servi, dépense comptée à part ; **exigé avec le moteur réel** (`adaptateur_commande_externe`), facultatif au moteur simulé (la barrière absente est dite au manifeste) ; la commande reçoit `MODELE_DEMANDE_POLE` ; défense générique du noyau `controle_modele_resultat` pour tout adaptateur (course et étage) ; l'écart arrête la course, met la sortie à l'écart, écrit les manifestes | `test_v49_09`, `_10` ; régression corrigée `test_cl43_03` |
| **CL13-06** (mineure) : `ResultMessage.stop_reason` et `model_usage` non lus | refus si `stop_reason == "refusal"` au résultat (événement `result.stop_reason`) ou si un modèle autre que le modèle demandé a été facturé dans `model_usage` (coût ou jetons non nuls ; entrée illisible = ayant servi) ; le texte reçu avant le refus est écarté | `test_v49_11` |
| **CL13-07** (mineure) : modèles de l'étage absents de la liste exigée du relais | `modeles_du_relais` : proposeurs, juges et, avec `--tests-de-mort`, l'expérimentateur Claude et le lecteur ; `verifier_relais` exige la liste exacte | `test_v49_12` |
| **CL13-08** (mineure) : `test_v48_22` ne prouvait pas ce qu'il annonçait | `test_v48_22` joue l'étage entier avec le vrai bac (lecture de la tranche et recalcul → survit ; écriture hors du dossier → échec, rien créé ; script trop long → tuée au délai) ; `test_v49_19` rejoue les évasions de la contre-lecture contre des cibles factices ; la sonde a ses artefacts (`test_v49_02`) | `test_v48_22`, `test_v49_02`, `_19` |
| **CL13-09** (mineure) : plafond « journalier » remis à zéro au redémarrage, arXiv en clair | compteur persistant : `compteur-AAAA-MM-JJ.json` et son `.sha256` par jour UTC, écriture atomique, relu au démarrage ; sceau faux, contenu invalide ou fichier disparu = le relais **ne démarre pas** ; `--dossier-compteur` obligatoire avec l'amont réel ; arXiv en `https://export.arxiv.org/api/query` | `test_v49_13`, `_14` ; `test_url_amont` |
| **CL13-10** (mineure) : modules de code écrasés en place (5 FAILED contre les EMPREINTES v47) | dit tel quel : le code de la v47 est dans l'historique (commit `15ab6ea4`, 169/169 OK) et son lot zippé ; celui de la v48 : commit `19cadf8c` et son lot. Table de provenance ci-dessous (empreintes v48 et v49 de chaque fichier modifié), et un essai qui la vérifie | `test_v49_18` |
| **CL13-11** (mineure) : « survit » repose sur le chiffre imprimé par le script | le noyau **recalcule** le chiffre quand le script déclare `CALCUL: fichier=…; colonne=…; statistique=…` (moyenne, médiane, somme, minimum, maximum, nombre, part positive, écart type) sur un fichier du préenregistrement : concordant (à l'arrondi d'affichage près) → « chiffre recalculé par le noyau » ; **discordant dans un sens comme dans l'autre → « non concluant »** (R4) ; sans ligne `CALCUL:` ou non recalculable → étiqueté « chiffre imprimé par le script, non recalculé » au matériau (« survit (chiffre imprimé par le script, non recalculé) ») ; le lecteur voit le champ `recalcul_noyau`, jamais le script | `test_v49_15`, `_16`, `_17` |
| **CL13-12** (mineure) : ressources de l'hôte non bornées | bornes du dossier de travail : 2 000 entrées, 256 Mo au total, profondeur 12, parcourues sans suivre de lien ; **surveillance pendant l'exécution** (toutes les 0,25 s) : dépassement → processus tué, « échouée (limites de l'hôte dépassées) », jamais comptée comme chiffre ; limites du processus : mémoire, taille de fichier, `RLIMIT_CORE` 0, temps processeur (délai arrondi + 5 s), 512 descripteurs, 1 024 processus (réel seulement ; non appliquée à root) | `test_v49_04`, `_03` |

Choix d'interprétation à relire : (1) CL13-11 est traité par recalcul d'une statistique **déclarée** plus étiquetage, non par
service du script au lecteur (qui y verrait le code qu'il ne juge pas). (2) CL13-12 est traité par quota vérifié pendant
l'exécution, non par système de fichiers en mémoire borné (`--size`/`--tmpfs`, `bwrap` ≥ 0.9, non éprouvable ici). (3) CL13-05 :
changement de contrat de la commande externe avec le moteur réel — **elle doit rendre `modele_servi`** ; la commande de
session-depot (appel à Argon) est à adapter avant toute course réelle, et le nom de modèle qu'Argon rend est à fixer (le noyau
compare à l'identifiant demandé, suffixe de date admis).

## Provenance du code modifié (R12, CL13-10)

Chaque fichier de code dont le contenu diffère de la v48, avec son empreinte v48 (celle de `EMPREINTES-orchestrateur-pole-v7-v48.txt`)
et son empreinte v49. Fichier d'essais : son empreinte v49 n'est pas comparée par l'essai (il ne peut pas se contenir lui-même),
mais elle est dans `EMPREINTES-orchestrateur-pole-v7-v49.txt`.

| fichier | empreinte v48 | empreinte v49 |
|---|---|---|
| `demonstrations/ideation_v1.py` | `7bc92daaf345bfde4dd9f5b7023a88c36297444c833eee97a569582699fe2251` | `cdcdcdddaa2840674c2255769a9aa55c5f61cc6e087b0eba45a9f95daca03218` |
| `essais/faux_sdk/claude_agent_sdk.py` | `77504cbc5aa0788f0e69934d6afd47a5c8ce3180edeaf65b389a46c4289f165f` | `56bb5116f1c95def096a6776c9fc8080d1540a4cdd69f487a5d9810e88d0b0c8` |
| `essais/test_v47_relais_moisson.py` | `538f9799602b6c73b03f3b5ab0a78f625bad2b04132a0ab0e6159aa569dcf209` | `53b76c4110c51d003218905a759a5ee27d9a8ecf35a657925874dbfddcfb6cd6` |
| `essais/test_v7_ideation.py` | `a8fa36157e26c2dc9a3442c6cc6a786a0b03148a9f1e449110fe70eb22b672b9` | `eb7477b7c7f7b4e9b76abab2b65a2dbd9ab8557fdc06ad36c3df2490f6e03092` |
| `pole/adaptateurs.py` | `530bcccfd99db796cb2bb9a735cb396566155c8e2046c803caac8bc46aa6479c` | `aa0b93938c71bf3690d6d152f17f4a07c9b4b64d35f6b5454213a65d12953ad2` |
| `pole/ideation.py` | `d79e06f197172a0e64ad691082d37deed5bd214cd8b74f89a7cb346fbf037da0` | `aace98f24108e4484d11c5cf3b05f77c8ab1bcce0fb8f1662432ad5ea85f8f65` |
| `pole/relais_moisson.py` | `a413e7e62a537313af671260f75d5a00e70e1fbe5d3bed2301504cdc8fe2a6e5` | `11584bfa67d78439cc369b4e82eb1418077660c4abd61e00bc8e06e01d763cce` |
| `pole/tests_de_mort.py` | `893340ece18862f98946ffa1abc361b6ebf8e79b037d8c65613b8e5ef8c833ba` | `c57c49aa822f57fb1a1cec8e8850f7f9685bb442d7d21aa80a1658a992b16338` |

Aucun autre fichier de code ne change. `pole/protocole_outils.py`, `pole/relais.py`, `pole/relais_reel.py` sont ceux de la v48.

## Essais

**485 essais** (466 en v48 ; + 19 `TestV49` dans `essais/test_v7_ideation.py`, avant `unittest.main()`) : **483 OK, 2 ignorés**
(les deux essais réels conditionnels à `bwrap`, `test_v48_22` et `test_v49_19`), 0 échec, deux exécutions complètes sur l'arbre
final (`python3 -B -m unittest discover -s essais -t . -p 'test_*.py'`), aucun processus survivant, `essais/_tmp` et `__pycache__`
retirés. En v48 : 466 essais, 465 OK, 1 ignoré. Une régression introduite par la correction a été trouvée par la suite et
corrigée (`test_cl43_03` : le contrôle du modèle servi s'appuyait sur la classe du kit que l'essai remplace ; il passe
maintenant par une fonction de module `modele_conforme`, et la commande factice du plafond rend `modele_servi`).
Fichiers changés : voir la table. Fichiers nouveaux : ce LISEZMOI, les EMPREINTES v49.

## Ce qui n'est pas vérifié en réel

- **`bwrap` jamais exercé ici** : l'effet réel de `--unshare-user --uid 65534 --cap-drop ALL`, de `--remount-ro /`, de
  `--new-session`, de `--die-with-parent` et de l'espace de processus pour tuer les petits-enfants ; `RLIMIT_NPROC` (non appliquée
  à root) ; l'existence des chemins liés en lecture seule (`/etc/python3`, `/etc/alternatives`…) selon la distribution. Les essais
  `test_v48_22` et `test_v49_19` sont écrits pour être joués dans le conteneur de session-depot, avec `bwrap` : **à rejouer avant
  tout usage de l'étage** ; si la sonde des privilèges échoue, l'étage est refusé (aucun repli).
- **La sonde des privilèges** n'a été jouée que sur des sorties données (cas sain et artefacts) : la vraie sonde tente un remontage
  de montage, ce qu'on ne fait pas hors d'un vrai bac.
- **`--disable-userns` et un filtre d'appels système** (suggérés par la contre-lecture) : non ajoutés ; sans effet sur les constats
  traités tant que les capacités sont nulles, mais à envisager.
- **Crochet `PreModelSwitch` du kit** (quatrième barrière possible, signalé par la contre-lecture) : non implémenté, absent du type
  du kit Python ; à vérifier.
- **Forme exacte de `model_usage`** du kit 0.2.172 (clés `costUSD`, `inputTokens`, `outputTokens`, `cacheReadInputTokens`,
  `cacheCreationInputTokens`, un modèle par clé) : SUPPOSÉE d'après les types du kit ; les noms de champs `stop_reason`, `model_usage`
  du `ResultMessage` sont vérifiés contre le kit installé, pas le contenu d'un vrai message.
- **Commande réelle d'Argon** : elle ne rend pas encore `modele_servi` (contrat nouveau, voir plus haut) ; non vérifiée.
- **Relais de moisson réel** : amont arXiv en https et compteur persistant éprouvés seulement contre l'amont factice local ;
  la garde de fuite reste lexicale (une paraphrase d'une hypothèse du programme peut quitter la machine) — à faire valider par
  Lazar au GO de la première moisson réelle.
- **`/dev` et `/dev/shm`** restent inscriptibles dans le bac (éphémères, sans effet sur l'hôte, CL13-12) : non traité.
- Le statut des résultats de l'étage reste **exploratoire** ; le recalcul ne couvre que les statistiques simples déclarées.

## Fabrication des empreintes

```
(awk '{print $2}' EMPREINTES-orchestrateur-pole-v7-v48.txt; echo LISEZMOI-orchestrateur-pole-v7-v49.md; echo EMPREINTES-orchestrateur-pole-v7-v48.txt) | sort -u | xargs sha256sum > EMPREINTES-orchestrateur-pole-v7-v49.txt
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v49.txt
```
