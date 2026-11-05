# SPARKS-EXP7-NUL — contre-lecture du delta v3 : brouillon 3 de l'addendum n° 1 et code v3 (`4c3bf146`)

Contre-lecteur neuf (R2, sous-agent Claude, Opus 5.5). Je n'ai écrit ni le texte, ni le code, ni aucune contre-lecture
précédente. Consigne : `consigne-contre-lecture-delta-sparks-v3-v1.md`, compagnon « OK » avant lecture. Travail du
4 novembre 2026, de 22:42 à 22:58 UTC (`date -u`). Lecture seule du dépôt et de l'arbre `/home/claude/wt/sparks-exp7-nul-v3`
(`git status` vide avant et après). Aucun fetch (le commit était présent localement), aucun commit, aucun `.sha256`, aucun
réseau, aucun modèle, aucune dépense. Moins de 5 Mo employés au bloc-notes.

## Verdict

**À reprendre : le code et la commande de répétition. Le texte est scellable après les 10 couples ci-joints, qui décrivent le code v4 demandé.**
Le brouillon 3 est exactement brouillon 2 + 11 couples + G-1 à G-6, et les six changements demandés sont dans le code (197 essais rejoués, comptes égaux).
Deux défauts bloquent : (1) aucune étape de l'amorce avant le calcul n'est bornée (`git`, gardes, lot) : une étape bloquée garde la carte louée jusqu'au 18 novembre ; (2) la répétition jouet, telle qu'écrite, s'arrête à l'étape 1 et ne peut pas cloner depuis la session.

## Empreintes vérifiées (compagnons, depuis le dossier de chaque fichier)

Toutes « OK » : brouillon 3 `12e47e51…`, brouillon 2 `7e98397e…`, rapport v3 `74d34d1b…`, contre-lecture du delta v2
`578fd025…` et les cinq autres pièces de son dossier, script et sortie du brouillon 3, trois sorties de `essais-et-banc-sparks-v3/`,
13 compagnons du commit `4c3bf146` (`git diff --name-status --no-renames 50fb15cd 4c3bf146` : 26 « A », aucun autre statut).

## Points (gravité ; une ligne chacun)

### Q1. Brouillon 3 = brouillon 2 + les 11 couples dans l'ordre + G-1 à G-6, rien d'autre
1. **Conforme.** Le script (`00ef5833…`), rejoué sur une racine copiée avec l'heure 22:28, rend une sortie identique à l'octet (`3dd51187…`, copie `sortie-rejeu-appliquer-couples-b3-v1.txt`). L'empreinte intermédiaire est `e5535c9658dab08fe596764f707595c859fcd147692ae731a6961a5cb55f7548`, et le brouillon 3 rendu est identique à l'octet (`12e47e51…`, 3 marqueurs). Le script ne fait rien d'autre que ces 20 remplacements, chacun unique au moment de son application.
2. **Mineur — texte resté de la v1** (l. 235) : « `PHASE=causal`, branche `calcul/sparks-exp7-nul-causal-v1` ». Le code v3 pousse sur `calcul/sparks-exp7-nul-causal-v3`, sur ordre écrit (couple K1).
3. **Mineur — G-3 décrit un code plus borné qu'il n'est.** « chaque démarrage est borné sur la machine (`timeout` de l'amorce) » (l. 366) et « cas sain et artefact pour chaque garde » (l. 378) sont faux en v3 (Q3, Q5). Couples K2 et K9, à condition d'appliquer le code v4.

### Q2. Les six changements de la contre-lecture v2 sont-ils dans le code ?
4. **(1) Redémarrage : fait.** L'amorce sépare création et redémarrage (l. 85, 103), contrôle le commit du disque (l. 104), lit l'ordre à la tête de la branche (l. 106-108), le valide (`redemarrage.py`), relit `deja_usd` (l. 111, 114), et traite copie, causal et fin (l. 117-134). Restent les réserves de Q4.
5. **(2) Minuterie : faite** (l. 43-77), en bash et `curl`, lancée avant tout clone. `curl` et `git` sont exigés. Le tir réel reste à faire (Q6).
6. **(3) M5 secondaire : fait** (`analyse.m5_secondaire`, c_b, base et lecteur). Les intervalles de la v2 sont égaux, ce que vérifie un essai (`test_analyser_v3_ajoute_m5_sans_changer_les_tirages`).
7. **(4) A priori de B3 : fait.** `bases.orientation_b3(…, a_priori)` vaut −1 au construit inversé ; `instance.a_priori_b3` lit `rapport["construit"]`, clé bien écrite par `sparks_exp7_nul_v1/instance.py`, l. 99-102.
8. **(5) Égalité des jetons : fait.** `test_jetons_de_l_outil_egaux_au_gabarit_tokenise` couvre les cas avec et sans jeton de début, ainsi que l'artefact « jeton de début gardé ».
9. **(6) Banc : fait sur la liste du point 26.** Les gardes du point 26 (dont les trois refus de l'amorce), les scripts shell et « tuée » au seul code 1 avec « failed » (banc l. 161) sont couverts. Les gardes neuves de la v3 ne sont pas toutes mutées (Q5).

### Q3. Minuterie : les leçons de la sonde d'A1-v3 (lignes de `scripts/amorce_instance_sparks_exp7_nul_v3.sh`, sauf mention)

| Leçon | État | Ligne et raison |
|---|---|---|
| Échéance absolue posée à la création | **tenue** | l. 35-41 : posée au premier démarrage, bornée à `1795046400` (l. 39), relue du disque ensuite (l. 36) ; la réduction à la fin du GO n'est pas journalisée (faible) |
| Jamais d'arrêt qui tue la minuterie | **tenue** | aucun `stop` ni `PUT` (l. 54 ; essai `aucun_arret`) ; la sortie normale du conteneur tue la minuterie, ce qui est voulu, puisqu'aucune destruction n'est alors due |
| Principal qui attend la minuterie | **tenue, avec réserve** | l. 71-76 : l'attente est bornée (marge + 120 s). Démontré par moi sous `unshare -pf` : avec l'attente, « DELETE » est au journal ; sans l'attente (l. 76 privée de `attendre_minuterie`), 0 « DELETE ». L'attente est donc nécessaire, mais **aucune mutation du banc ne l'éprouve** et aucun essai ne tourne dans un espace de processus. Le numéro de processus est lu dans un fichier qui peut venir d'un démarrage antérieur (l. 73) ; A1-v3 prend `$!` |
| `timeout` sur l'amorce et les installations | **non tenue (majeur)** | l. 88 (`clone`), 91-92 (`sparse-checkout`, `checkout`, qui télécharge les données), 96 (garde du code, qui lit des données à la demande), 107-108 (`fetch`, `archive`), 109, 115, 121 (`redemarrage.py`, empreintes de 4 Go au plus) et 61 (`vastai destroy`) : rien n'est sous `timeout`. La minuterie ne tire qu'à l'échéance, c'est-à-dire la fin du 18. Démontré : avec un `git` bloqué, l'amorce vit jusqu'à ce que je la coupe (code 124 à 20 s), sans aucun « DELETE ». Pire cas : ≈ 0,8 USD/h de carte jusqu'au 18, soit plus de 200 USD contre un GO de 40 |
| Reprise après l'échéance | **tenue** | l. 77 : avant tout clone et tout calcul, destruction demandée et attendue (essai `apres_echeance`). Une échéance illisible sur le disque (l. 42) refuse sans lancer la minuterie (faible) |
| `curl` absent | **tenue** (refus visible) | l. 33, avant tout (essai `sans_curl`) ; aucun repli `python3`, contrairement à A1-v3 ; présence dans l'image non vérifiée (Q6) ; aucun essai « `git` absent » (l. 34, faible) |
| Délai de `vastai create` sans fuite du jeton | **non tenue (moyen)** | `lancer_sparks_exp7_nul_v3.sh`, l. 21-23 : la commande imprimée n'a pas de `timeout`, et sa sortie n'est ni redirigée ni réduite au code et à l'identifiant (R-1480). Le jeton n'est pas écrit en clair (`\$GH_TOKEN`), ce qui est juste |
| Marqueur de création incertaine | **non tenue (moyen)** | même endroit : aucun marqueur ni identifiant consigné après un code non nul ou un délai, donc une seconde création reste possible ; aucune étiquette (`--label`) pour l'inventaire |

### Q4. Redémarrages et ordres
10. **Majeur (règle) — branche des ordres sous `calcul/`.** La session y écrit (amorce l. 29, `plan.BRANCHE_ORDRES`, lanceur l. 32). Nom proposé : `ordres/sparks-exp7-nul-v4-<COMMIT[:12]>`. Il sort des branches réservées aux instances et il est lié au commit lancé, si bien que les ordres d'une répétition (autre commit) ne peuvent plus devenir le « dernier ordre » d'un vrai redémarrage. La réserve 4 du rapport (supprimer la branche avant la vraie création) tombe alors (couple K4).
11. **Moyen — ordre non lié à l'instance.** Ajouter une clé `instance`, que la machine compare à `CONTAINER_ID`, pour qu'aucun ordre ne vaille pour une autre instance au même commit (par exemple une seconde création après un échec) (couple K5).
12. **Conforme — refus d'un ordre déjà exécuté.** `exiger_nouveau` refuse tout numéro ≤ au maximum consigné. Un fichier des faits illisible lève `ValueError`, refusé ; c'est le dernier par numéro, non le plus récent, qui est lu, ce qui est sûr (un ancien numéro est refusé). L'ordre est consigné avant l'action (l. 115).
13. **Mineur — consignation non contrôlée.** Le code de retour de `redemarrage.py fait` (l. 115) est ignoré : si l'écriture échoue (disque plein), l'action part sans être consignée, et l'ordre pourra être rejoué. Ajouter `|| exit 2` (couple K6).
14. **Moyen — `deja_usd` relu, mais cru sans contrôle (R-1481).** Rien n'empêche une valeur plus basse que celle de l'ordre précédent, et la machine ne tient pas sa propre borne. Proposé : refuser une baisse ; prendre max(`deja_usd`, borne de la machine), où la borne de la machine = somme des plafonds `MINUTES` des démarrages consignés sur son disque × prix de la carte + temps écoulé depuis la création × prix du stockage. Ce calcul ne passe par aucun modèle (couple K7). La lecture par `sed` d'un flottant écrit en notation scientifique (`1e-05` → « 1 ») va dans le sens prudent.
15. **Mineur — phase causale non rejouable.** La branche des sorties est fixe (`calcul/sparks-exp7-nul-causal-v3`, script d'instance l. 18) et l'environnement ne change pas au redémarrage. Après un échec qui suit la poussée initiale (l. 45), tout nouvel ordre « causal » s'arrête à « branche déjà présente » (l. 39-40). Nommer la branche `…-causal-v4-<COMMIT[:12]>-<NNN>` (couple K1), ou écrire que l'échec est un nœud de Lazar.

### Q5. Banc v3 et essais
16. **Conforme — comptes.** J'ai rejoué 197 essais : 197 passés, code 0 (`essais-rejeu-4c3bf146-v1.txt`). La collecte par fichier donne 90 + 69 + 38. Le banc compte 114 lignes « TUÉE », soit 22 + 52 + 40 (40 = longueur de `MUTATIONS_V3`), et son `.json` 117 entrées, témoins compris. Ces comptes sont égaux au rapport. Je n'ai pas rejoué le banc.
17. **Moyen — gardes neuves sans mutation :**
   - attente du principal (l. 76), et numéro de processus de la minuterie ;
   - consignation de l'ordre (l. 115) ;
   - clés fermées, bornes de `deja_usd` et motif des cas (`redemarrage.lire_ordre`) ;
   - `lot-NNN` existant (R12) ;
   - « ordre mal lu » (l. 113) ;
   - plafonds « copie_minutes + 5 » (l. 120) et « 60 minutes » de la phase causale (l. 126) ;
   - `ECHEANCE_UTC_S` non entière (l. 38 : essai sans mutation) ;
   - succès « 2?? » de la minuterie ;
   - identifiant numérique au lanceur (l. 27) ;
   - `POUSSEE-VERIFIEE` (script d'instance, l. 125-128 : jamais joué).

   Ajouter les mutations, et jouer les essais de minuterie et d'attente sous `unshare -pf`.
18. **Mineur — aucun cas sain de la création jusqu'au calcul** : seuls les trois refus sont essayés, et la répétition doit couvrir le reste (Q6).

### Q6. Répétition jouet (rapport, section 5)
19. **Majeur — elle s'arrête à l'étape 1.** Sous `set -euo pipefail`, l'amorce de l'étape 1 sort avec le code 3, comme attendu, et `| tee` fait échouer la commande. Les étapes 2 à 4 et le nettoyage ne sont donc jamais joués : les branches `essai/…` restent sur le dépôt distant et la minuterie de l'étape 1 reste en vie 2 h (sans danger, `curl` simulé). Correction : `|| true` après chaque amorce, puis un `grep` explicite de ce qu'on attend.
20. **Majeur — dans une session de ce type, elle ne peut pas cloner.** `env -i` retire `HTTPS_PROXY`, `NO_PROXY` et `GIT_SSL_CAINFO`, et `HOME="$J"` retire la configuration globale de `git` (`http.proxyauthmethod`). Les vérifications du bloc-notes montrent que la session passe par un mandataire. Il faut passer ces variables, ainsi que `GIT_CONFIG_GLOBAL` vers la configuration de la session.
21. **Moyen — l'étape 3 n'exerce pas la phase causale.** `BRANCHE=essai/sparks-v3-jouet`, fixé dans `ENV`, sert aussi au causal. La branche existe déjà depuis l'étape 1, donc le script d'instance s'arrête à « branche déjà présente » (l. 39-40) avant le clone et l'essai de calcul, et « sans poussée vérifiée » s'affiche pour une autre raison que celle que dit le rapport. Proposé : un préfixe `BRANCHE_PREFIXE` (`calcul/` par défaut, `essai/` en répétition) et les noms du point 15.
22. **Mineur — elle écrit les ordres sur `calcul/sparks-exp7-nul-v3-ordres`** (règle, point 10). Elle modifie l'arbre du code `W` (nouvelle branche, commit), alors qu'un clone à part serait plus sûr. Elle n'a aucun `timeout`. Elle n'arrête que la dernière minuterie par son numéro, alors qu'il en naît une par étape.
23. **Sans danger quant à la dépense.** Il n'y a aucun `vastai` dans la session (`command not found`) ni dans le `PATH` de `env -i`, `curl` est simulé, `CONTAINER_ID=1` avec une clé factice, et Hugging Face n'est pas appelé en jouet. Seules des branches sont écrites sur le dépôt distant. Le chemin positif « poussée vérifiée → destruction » reste couvert par le seul essai à script factice, ce qui doit être déclaré.
24. **À éprouver sur une vraie machine avant le scellement (tir réel, R-1477) :**
   - le `DELETE` par `CONTAINER_API_KEY`, puis une lecture qui ne trouve plus l'instance (un HTTP 2xx seul ne prouve rien si Vast répond `"success": false`) ;
   - `curl` et `git` dans `pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime` (l'amorce refuse sinon, et tout le dessin tombe) ;
   - une amorce de ≈ 8 Ko passée par `--args bash -c`, relancée telle quelle par `vastai start`, avec le même environnement ;
   - à la sortie du conteneur : instance « exited » et carte non facturée ;
   - la mort de la minuterie avec le processus 1, et l'attente du principal ;
   - `vastai copy` depuis un conteneur lancé par ses arguments, peut-être sans `sshd` : le risque touche les 14 à 18 redémarrages de copie ;
   - un redémarrage quand la carte de l'hôte a été louée par un autre (liveness, stockage seul) ;
   - la durée du clone partiel du dépôt de travail.

## Changements de code requis (v4, R12 ; puis essais, banc, répétition corrigée, contre-lecture neuve du delta)
1. **`timeout` sur chaque étape de l'amorce avant le calcul** (clone et `checkout` 600 s, `fetch` et `archive` 300 s, gardes Python 120 s, `lot` 900 s), `vastai destroy` sous `timeout 120` dans la minuterie, et un essai avec un `git` bloqué (artefact).
2. `attendre_minuterie` sur `$!` du lancement en cours (et non sur le fichier), avec une mutation et des essais sous `unshare -pf` (attente et reprise après l'échéance).
3. Branche des ordres `ordres/sparks-exp7-nul-v4-<COMMIT[:12]>` (plan, amorce, lanceur, docstring de `redemarrage.py`, essais). Clé `instance` = `CONTAINER_ID` exigée. `fait … || exit 2`.
4. `deja_usd` : refus d'une baisse ; borne propre de la machine (plafonds consignés à chaque démarrage, stockage depuis la création) ; max des deux.
5. Branches des sorties `calcul/sparks-exp7-nul-v4-<COMMIT[:12]>` et `calcul/sparks-exp7-nul-causal-v4-<COMMIT[:12]>-<NNN>`, avec le préfixe `BRANCHE_PREFIXE` pour la répétition.
6. Lanceur : `timeout 300` sur `vastai create`, sortie redirigée vers un fichier non affiché (code et `new_contract` seuls), marqueur `.creation-incertaine` pour tout code non nul ou délai dépassé, `--label` lié au commit.
7. Mutations du point 17.
8. Répétition : points 19 à 22 corrigés ; puis tir réel (point 24).

## Fichiers (ce dossier, neufs, sans compagnon)
- `couples-brouillon4-v1.json` (`838882eb…`) : 10 couples K1 à K10, chacun unique dans le brouillon 3 et au moment de son application dans l'ordre, 3 marqueurs gardés ; texte d'essai `4ea5636bc604000c2a47d895ed0ce536d1e5d8d4cb8cedd03550c63c794f512b` (non versé). Ils supposent le code v4 ci-dessus : si un changement n'est pas retenu, son couple tombe avec lui (K1 et K4 : point 5 et point 3 ; K2, K3 et K9 : point 1 ; K5 à K7 : points 3 et 4 ; K10 : point 6 ; K8 seul est indépendant).
- `couples-brouillon4-contre-lecteur-v1.py` (`4f89b364…`) : script qui les écrit et les vérifie.
- `demo-minuterie-espace-processus-v1.sh` (`f277d5c0…`) et `sortie-demo-minuterie-v1.txt` (`4b8503da…`) : trois démonstrations, `curl` simulé et aucun réseau. Les amorces jouées sont la copie de l'amorce de `4c3bf146` et cette copie privée de `attendre_minuterie` à la l. 76 (par `sed`).
- `essais-rejeu-4c3bf146-v1.txt` (`9e4e4ad8…`) et `sortie-rejeu-appliquer-couples-b3-v1.txt` (`3dd51187…`).
