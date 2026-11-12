# Ordre d'exécution — étape A de T0.7 sur l'instance gardée de la course 7b — v1, brouillon 1

> **POINT BLOQUANT PB-1 (§ 0 bis) : aucune voie connue ne permet aujourd'hui de faire tourner une commande sur l'instance de 7b après son redémarrage.** L'instance est créée en mode « args » (pas de serveur SSH) ; au redémarrage, son amorce gelée pousse puis dort ; `execute` et `copy` sont refusés à la clé de la session. L'ordre est écrit en entier ; il ne s'exécute pas avant que la mère ait fixé la voie (marqueur `VOIE_EXECUTION_INSTANCE`).

- **Statut** : brouillon 1, écrit le 2026-11-10 à partir de 07:30 UTC (`date -u`) par le développeur du module de T0.7 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), sur la consigne de la mère du 10 novembre (« passe à blanc de l'extracteur, puis brouillon 1 de l'ordre d'exécution de l'étape A »). **Non contre-lu.** Auteur du code qu'il fait jouer : déclaré (R2 : la contre-lecture doit être faite par un sous-agent neuf).
- **Autorisation** : **GO-2026-11-10-04** (R-2089 ; `registres/go.md` l. 294 de `main` `1821ed26`) : « T0.7, étape A sur l'instance de la course de confirmation 7b […] passe à blanc de l'extracteur, garde d'ouverture et d'identité, extraction des jeux génériques, sondes neuves et validation, notation, témoins et base « coût seul », scellement et poussée » ; **20 USD tout compris** (carte, stockage de l'instance gardée arrêtée, téléchargement) ; **A100 ou H200, la H200 seulement après un mot de Lazar** ; aucun épisode joué ; arrêt et destruction par identifiant (R10) ; échéance 2026-11-23.
- **Texte qui régit l'étape** : le préenregistrement scellé de T0.7 (`prereg/T0.7-sondes-v0-v1.md`, ligne `SCELLEMENT-T07`), sections « Calcul et dépense », « Écrits exigés par P3-bis » (b) « Lancement nominal », (c) engagement, (d) garde adaptée, « Module », « Ordre d'exécution » (brouillon 19, l. 2468-2475).
- **Exécutante** : la session `<<ID_SESSION_EXECUTANTE>>`, porteuse des clés (Vast.ai, GitHub), active pendant toute l'étape ; elle écrit son journal `journal-etape-a-t07-v1.md` (une ligne datée par geste, `date -u`).

## 0. Objet

Jouer, sur l'instance de 7b **gardée arrêtée** après la course (ordre de 7b, brouillon 2, `488c2e51…`, § 4.13 : instance gardée si `SCELLEMENT-T07` et `GO-ETAPE-A-T07` sont au registre à la fin normale), dans cet ordre : (0) `CODE-T07` inscrite par la mère au registre (P12, avant le redémarrage) ; (1) mise en place du code de T0.7 au commit cité, dans un dossier à part, et contrôle de `CODE-T07` contre l'arbre ; (2) suite figée des essais de T0.7 ; (3) **passe à blanc de l'extracteur** (aucune donnée décisive) ; (4) **étape A** (`lecture_v2 etape-a`) ; (5) scellement et poussée des sorties sur une **branche neuve** ; puis arrêt et **destruction de l'instance par son identifiant, au plus tard le 2026-11-16 à 23:00Z**. Ni épisode, ni étape B, ni lecture d'un résultat (de 7b ou de l'étape A), ni geste sur P3-bis.

## 0 bis. Point bloquant PB-1 : voie d'exécution sur l'instance

**Constat** (lectures seules, citées) :

1. La commande de création de 7b est `vastai create instance … --entrypoint bash --args -c "echo <amorce> | base64 -d > /root/amorce.sh && bash /root/amorce.sh"` (`scripts/lancer_t06_v13.sh` l. 235, commit `1609a4bf`) : mode « args », **sans serveur SSH** (constat déjà consigné : R-060).
2. Au redémarrage, l'amorce gelée (`scripts/amorce_instance_t06_v11.sh`, `43d85659…`, l. 203-214) pousse les commits en attente, détruit si l'échéance ou la dépense est passée, sinon **dort** (`sleep infinity`) ; elle ne lance rien d'autre, et aucune ligne de l'amorce ne nomme T0.7 (seul le bras B est une étape annexe, l. 417-442, jouée avant l'arrêt).
3. `vastai execute` (commandes `ls`, `rm`, `du` seulement) et `vastai copy` ont été refusés à la clé de la session (« This action requires login », R-060) ; `copy` passe par rsync sur SSH et exige une clé SSH au compte (R-1590 : changement de compte, nœud) ; la session ne peut ouvrir aucune connexion SSH sortante (R-821).
4. La chaîne v14 préparée (`prep/t06-chaine-v14-v1`, amorce v12) ne porte pas non plus d'étape de T0.7.

**Conséquence** : le montage « étape annexe sur l'instance de 7b, comme le bras B » du brouillon 19 n'a pas de mécanisme ; le bras B, lui, est joué par l'amorce elle-même.

**Options** (décision de la mère, puis de Lazar si dépense ou compte) :

| Option | Avantage | Inconvénient |
|---|---|---|
| (a) **Recréer le conteneur** de l'instance de 7b avec une amorce de T0.7 (`vastai update instance <ID> …`, si la version 1.8.3 le permet) qui joue le bloc du § 4.6 | instance, modèle et 31,5 Go d'activations gardés ; dans le plafond de GO-2026-11-10-04 | **non vérifié** : persistance du disque, du cache du modèle et du dépôt de 7b ; la minuterie de l'amorce de 7b ne tourne plus (l'amorce de T0.7 doit porter la sienne) ; amorce de T0.7 à écrire, essayer en local, contre-lire ; épreuve à blanc sur une instance jetable (dépense : ligne de GO propre) |
| (b) **Variante B** du texte (`GO-LECTURE-T07`, délégation GO-2026-10-20-07, ≤ 10 USD par lancement) : instance neuve, modèle descendu, activations recalculées (`lecture_v2 repli-recalcul`, adaptateurs et sous-ensemble poussés par la chaîne de 7b, amorce l. 318-321) ; l'instance de 7b est détruite à la fin de sa course | aucune recréation inconnue ; code du repli déjà répété en jouet (252 activations égales au bit près) | amorce et lanceur de T0.7 à écrire (création, minuterie, poussée) ; garde d'équivalence au lieu de la garde d'identité ; ≈ 4 à 5 USD, pire cas ≈ 10 USD (texte) |
| (c) Rien avant le 16 : l'instance de 7b est détruite par la fille, l'étape A attend une variante B | aucune dépense nouvelle | l'étape A glisse ; la mère porte le nœud |

**Recommandation du rédacteur** : (b), confiance moyenne : c'est la seule voie que le texte scellé décrit déjà en entier et dont le code est répété ; (a) n'est sûre qu'après une épreuve que le calendrier (destruction le 16) rend serrée. **Voie retenue** : `<<VOIE_EXECUTION_INSTANCE>>` (option, mot de Lazar s'il en faut un, R-…). Le reste de l'ordre suppose une voie qui fait jouer **le bloc du § 4.6 tel quel** sur la machine qui porte les données de 7b ; sous (b), les points propres à la variante B sont au § 5.

## 1. Cadre

| Élément | Valeur |
|---|---|
| Code de T0.7 | commit du code contre-lu et répété (`C7`), et commit de scellement de T0.7 (`S7`) : **S7 descend de C7 sans changer l'arbre gelé** (`git diff --quiet C7 S7 -- src tests`), comme la voie B de T0.6 (S `935262b1…` descendant de `1609a4bf`, R-2064) ; S7 ancêtre d'`origin/main` |
| Configuration | fichier JSON scellé dans S7 (chemin dans la ligne (A)) ; empreinte canonique `<<EMPREINTE_CONFIG_T07>>`, vérifiée par `lecture_v2 empreinte-config` ; même fichier pour la passe à blanc et l'étape A |
| Course lue | 7b : run `RUN6`, branche `calcul/t06-confirmation-7b-v1` (ou `-v2`, `-v3`), S de T0.6 `935262b17ca95894a882b02f1526ee39d1738652` |
| Instance | celle de 7b, gardée arrêtée (§ 4.13 de l'ordre de 7b) ; carte relevée par la fille ; **H200 : rien sans un mot de Lazar** |
| Dossier sur l'instance | `/root/t07-etape-a-v1/` (neuf ; `-v2` à une relance) ; **le clone de T0.6 (`/root/amorce-depot`) n'est jamais modifié** : seuls trois fichiers et un dossier de la course y sont lus, par liens (§ 4.6, étape 4) |
| Interpréteur | celui de la course (`/root/amorce-depot/.venv/bin/python`, Python 3.11, `requirements-gpu.txt`) ; garde : exigences de paquets égales entre S de T0.6 et S7, sinon arrêt |
| Branche de sortie | **`donnees/t07-etape-a-v1`** (nom du brouillon 19, l. 2474), **absente du dépôt distant** avant la première poussée ; sinon `-v2` ; jamais `main`, jamais une branche `calcul/…` |
| Dépôt | `https://github.com/lciric/controle-ia-travail.git` seulement ; jamais `lciric/controle-ia` |
| Plafond | 20 USD tout compris (GO-2026-11-10-04) ; stockage compté depuis l'arrêt de l'instance à la fin de 7b (texte, « Calcul et dépense ») |
| Échéances | redémarrage au plus tard **2026-11-16T18:00Z** ; destruction au plus tard **2026-11-16T23:00Z** (avant la minuterie de l'amorce de 7b, 17 novembre 00:00 UTC, que le redémarrage relance : amorce l. 111-127, 199, 213) ; au-delà : variante B |

## 2. Embargos et chemins interdits

1. **Jamais** l'exécutante n'ouvre, n'affiche, ne copie, ne hache ni ne passe à un outil un `lecture-sondes-t06.json` (de 7b, de 7a, d'aucun run) ni son compagnon. Sur l'instance : le dossier `diag/<RUN6>/` du clone de T0.6 n'est **jamais listé ni lié en entier** ; seuls `episodes-t06.json` et son compagnon y sont liés, par leur nom ; l'extraction partielle du clone de T0.7 exclut `diag/*/lecture-sondes-t06.json*`.
2. **Jamais** `donnees/lecture-b-7a-quarantaine-v1`, la branche `essai/t06-explo-v3`, ni `diag/`, `runs/`, `donnees/` de 7a ; clones de la **seule branche `main`** (`--single-branch`), `git fetch` par refspec explicite.
3. **Jamais** `scripts/extraire_mesures_epreuve_t06_v1.py`, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, l'étiqueteur ; **règle 9** : aucune recherche récursive (`grep -r`, `rg`, `find -exec`, motif développé) sur un arbre qui contient un chemin interdit sans l'exclure ; `git grep` avec exclusions ; jamais `verifier-arbre`.
4. **Aucune lecture de résultat de 7b** : `lecture-cout-t06.json`, `resume.json`, `distillation-t06.json`, `episodes-t06.json`, `run.err` jamais affichés (le module de T0.7 lit les épisodes ; l'exécutante, jamais).
5. **Aucune lecture des sorties de l'étape A** : `scores-actions-t07.npz`, `sondes-t07.json`, `ouverture-t07.json`, `notation-t07.json`, `arret.json` (sauf `etape` et `motif`), `sondes-neuves-t07.npz`, `temoins-lexicaux-t07.json`, manifeste du run de T0.7 : hachés, jamais affichés (fermés jusqu'à l'étape B). La sortie de la passe à blanc, sans donnée décisive, peut être lue ; l'exécutante n'en recopie que les champs du § 8.
6. **Aucune sortie de P3-bis lue ni citée** (texte, (b) 1) : seul le module lit, par sa garde, les registres de P3-bis (présence, date, sceau).
7. **Accès mécanique connu** (ordre de 7b, § 2.6) : le `.git` du clone de T0.6 sur l'instance porte les objets de toutes les branches ; personne n'y touche.

## 3. Préalables bloquants (vérifiés par l'exécutante, écrits au journal avec l'heure)

| # | Préalable | Où | Sinon |
|---|---|---|---|
| P0 | **PB-1 levé** : voie fixée au § 0 bis, et son épreuve faite s'il en faut une | § 0 bis | rien |
| P1 | **`RUN-CONFIRMATION-T06`** : une ligne au registre de `main`, chemin `runs/<RUN6>/manifeste.json` de 7b | § 4.1 | attente (le texte : relance quand la ligne existe) |
| P2 | **`SCELLEMENT-CONCEPTS-T07`** : une ligne, chemin `donnees/t07-concepts-v1/phrases-concepts-v1.jsonl` ; lignes permises des jeux, au plus une chacune, chemins `donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl` (`-JD`), `donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl` (`-JA`), `donnees/t07-jeux-synthetiques-v3/domaine-cout-v3.jsonl` (`-JC`, s'il est scellé) (inventaire des jeux `c9910a54…`, § 4.3 ; cités par chemin, empreinte lue au registre) ; chaque fichier présent sur `main` avec son compagnon, et le journal du script de son dossier (`journal-verification*.txt`, compagnon) | § 4.1 | attente (concepts) ; jeu sans ligne : repli du texte |
| P3 | **`GO-ETAPE-A-T07`** : une ligne ; son extrait scellé est une ligne de `registres/go.md` et nomme GO-2026-11-10-04 ; non révoquée, non échue | § 4.1 | rien |
| P4 | **`SCELLEMENT-T07`** : une ligne, égale à celle de la remise de 7b | § 4.1 | arrêt, nœud |
| P5 | `SCORES-T07`, `SONDES-T07` absentes (étape déjà jouée sinon) ; `VERDICT-P3BIS` et le journal de P3-bis : relevés, jugés par la garde du module (G2), jamais lus par l'exécutante au-delà de la présence et de la date | § 4.1 | arrêt, nœud |
| P6 | **Engagement** de dépense de GO-2026-11-10-04 au registre des dépenses (écrit par la mère avant la première minute de carte) | § 4.1 | rien |
| P7 | **Compte rendu de la fille de 7b** : fin normale, branche poussée, rapatriement vérifié, instance **arrêtée et gardée** (issue du § 4.13), identifiant, run, carte, prix de la carte et du stockage, heure de l'arrêt ; carte **A100** (H200 : mot de Lazar dans la session de l'exécutante, verbatim au journal) | rapport de la fille | rien |
| P8 | **Code** : S7 descend de C7, arbre gelé égal, S7 ancêtre de `main` ; essais attendus au commit (ligne (A), `ATT`) | § 4.1 | arrêt |
| P9 | **Heure** : maintenant ≤ 2026-11-16T18:00Z | `date -u` | variante B |
| P10 | **Dépense projetée** (§ 6) : relevé + 5 h de carte ≤ 20 USD | § 6 | nœud (devis neuf) |
| P11 | `vastai` 1.8.3 ; inventaire : l'instance de 7b seule, à l'état « stopped » ; aucune autre instance d'étiquette `t07…` | § 4.2 | arrêt |
| P12 | **`CODE-T07`** (DS-3 bis accordée, option (a), R-2104 ; configuration `code_t07_exige` vrai) : une ligne au registre de `main`, **inscrite par la mère avant le redémarrage** (donc strictement avant la première ouverture des activations), citant un fichier scellé écrit par `python -m controle_ia.t07.code_t07_v1 ecrire <clone> C7 registres/code-t07/CODE-T07-v1.json` : commit C7 (celui qui a été contre-lu et répété en jouet) et empreintes des fichiers de `src/controle_ia/t07/` ; une correction du code après le scellement de T0.7 n'est possible qu'avant cette ouverture, contre-lue, répétée en jouet, puis inscrite par cette ligne (unique) | § 4.1 | rien |

## 4. Étapes et commandes

L'état du shell ne survit pas d'une commande à l'autre : **chaque bloc de la session commence par la ligne (A)**. Les clés passent par leur nom, jamais par leur valeur.

**(A)** :

```bash
W=/home/user/etape-a-t07-v1; M=$W/main; J=$W/journal-etape-a-t07-v1.md; ID=<<ID_INSTANCE_7B>>; RUN6=<<RUN_T06_7B>>; C7=<<COMMIT_CODE_T07>>; S7=<<COMMIT_SCELLEMENT_T07>>; CFG=<<CHEMIN_CONFIG_T07>>; ATT='<<LIGNE_ESSAIS_T07>>'; BR=donnees/t07-etape-a-v1; GO=GO-2026-11-10-04; PC=<<PRIX_CARTE_USD_H>>; PS=<<PRIX_STOCKAGE_USD_H>>; TA=<<INSTANT_ARRET_7B_UTC>>; URL=https://github.com/lciric/controle-ia-travail.git; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }
```

`TA`, `TR` (heure du redémarrage, § 4.3) : secondes UTC. `W`, `BR` changent à une reprise ; le nom en vigueur est écrit au journal.

### 4.1 Préalables depuis `main` (session ; lecture seule)

```bash
# (A)
mkdir -p "$W" && j "début ; voie : relue au § 0 bis" && git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$M" && git -C "$M" sparse-checkout set --no-cone '/registres/*.md' '/registres/go-extraits/' && git -C "$M" checkout -q main && git -C "$M" rev-parse HEAD
REG="$M/registres/scellements-v1.md"; for k in RUN-CONFIRMATION-T06 SCELLEMENT-CONCEPTS-T07 GO-ETAPE-A-T07 SCELLEMENT-T07 CODE-T07 SCORES-T07 SONDES-T07 VERDICT-P3BIS; do printf '%s %s\n' "$k" "$(grep -c "^| $k |" "$REG")"; done
grep "^| RUN-CONFIRMATION-T06 |" "$REG" | awk -F'|' '{gsub(/ /,"",$4); print $4}'
LA=$(grep '^| GO-ETAPE-A-T07 |' "$REG"); PA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$5); print $5}')
[ "$(sha256sum < "$M/$PA" | cut -d' ' -f1)" = "$HA" ] && [ "$(cut -d' ' -f1 "$M/$PA.sha256")" = "$HA" ] && [ "$(grep -c '^| GO-' "$M/$PA")" = 1 ] && grep -qxF -- "$(grep '^| GO-' "$M/$PA")" "$M/registres/go.md" && grep -q "^| $GO |" "$M/$PA" && echo "GO-ETAPE-A-T07 conforme ($GO)"
[ "$(grep '^| SCELLEMENT-T07 |' "$REG")" = "$(cat "$W/ligne-scellement-t07.txt")" ] && echo "SCELLEMENT-T07 inchangée"
grep -c "$GO" "$M/registres/depenses.md"
git -C "$M" merge-base --is-ancestor "$C7" "$S7" && git -C "$M" diff --quiet "$C7" "$S7" -- src tests && git -C "$M" merge-base --is-ancestor "$S7" HEAD && echo "code conforme"
```

Attendus : `1` pour les cinq premières clés (`CODE-T07` comprise, P12), `0` pour `SCORES-T07` et `SONDES-T07`, `VERDICT-P3BIS` relevé (0 ou 1) ; le chemin égal à `runs/<RUN6>/manifeste.json` ; les trois messages ; au moins une ligne d'engagement. `ligne-scellement-t07.txt` : la ligne `<<LIGNE_SCELLEMENT_T07>>`, écrite à l'octet par l'exécutante au début. La révocation et l'échéance de la ligne de GO se lisent dans `registres/go.md`, sur la seule ligne de l'identifiant.

### 4.2 Outil et inventaire (session)

```bash
# (A)
vastai --version; date -u +%FT%TZ
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>/dev/null); printf '%s' "$out" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; d=d[0] if isinstance(d, list) else d; print("etat :", d.get("actual_status"), "/", d.get("intended_status"), "; carte :", d.get("gpu_name"), "; étiquette :", d.get("label"))'
```

Seuls ces quatre champs sont imprimés ; le texte brut n'est jamais affiché. Attendu : `exited` / `stopped`, la carte de 7b, l'étiquette de 7b.

### 4.3 Redémarrage de l'instance gardée, par son identifiant

Ordre de 7b, § 4.13 : la fille ne redémarre pas l'instance ; **le redémarrage relève de cet ordre**. Une fois, après P0 à P11 :

```bash
# (A)
GO_ID=$GO timeout -k 5 120 vastai start instance "$ID"; echo "code $?"; TR=$(date +%s); j "redémarrage demandé, TR=$TR"
```

Puis l'état est relevé toutes les 2 minutes par le bloc du § 4.2 jusqu'à `running`. **Attendu** : l'amorce de 7b repart (« DEMARRAGE n »), pousse ce qui attend (rien), puis « sommeil (second démarrage après une fin normale, rien ne repart) » (amorce l. 207-214) ; la minuterie de 7b repart avec l'échéance de la course (≤ 17 novembre 00:00 UTC). Si l'instance n'est pas `running` deux heures après la demande, ou si l'amorce annonce une destruction : arrêt par l'identifiant si besoin (§ 4.8), compte rendu, variante B.

### 4.4 Remise du bloc à l'instance

Par la voie du § 0 bis : le bloc du § 4.6 est écrit sur l'instance sous `/root/t07-etape-a-v1/etape-a-t07-instance-v1.sh` et joué **une fois** :

```bash
bash /root/t07-etape-a-v1/etape-a-t07-instance-v1.sh "$S7" "$C7" "$RUN6" "$CFG" "$BR" "$ATT"
```

Son empreinte sha256 (calculée par l'exécutante sur le texte remis) est écrite au journal avant le jeu. Les lignes `T07 …` qu'il imprime se lisent par la voie (sous (a), `vastai logs "$ID"` filtré sur `^20.* T07 `) ; aucune autre ligne n'est recopiée.

### 4.5 Ce que fait le bloc (résumé)

1. Gardes de la machine : interpréteur de la course, données de 7b sur le disque, fin normale marquée, carte visible, jeton GitHub présent (par le nom).
2. Clone de T0.7 (`main` seule, partiel, extraction partielle), extraction de **S7** ; gardes du code (tête = S7, C7 ancêtre, arbre gelé égal, S7 ancêtre de `main`) et de l'environnement (exigences de paquets égales à S de T0.6).
3. **Registres à jour depuis `main`** à l'ouverture (CT-17 de la contre-lecture du code) : `registres/*.md` et `registres/go-extraits/`, plus chaque fichier cité par `registres/scellements-v1.md` et `registres/prealables-p3bis-v1.md`, recopiés de `origin/main` avec leurs compagnons ; nommément les fichiers des quatre lignes `SCELLEMENT-JEUX-T07-JD`, `-JA`, `-JC` (s'il est scellé) et `SCELLEMENT-CONCEPTS-T07` (P2), présence contrôlée, et le **journal du script** du dossier de chaque jeu (remesure des jetons, E-8) ; chemin interdit cité → arrêt ; `src/` et `tests/` restent ceux de S7 (contrôlé) ; l'arbre n'est plus propre : le manifeste l'écrit (`autoriser_depot_sale`, CT-15). La configuration (brouillon v4 au moins : `enonces_reserve`, `code_t07_exige` vrai) cite l'énoncé des tâches de réserve (fichier scellé de T0.5) : il entre par l'extraction partielle (chemins cités par la configuration).
4. Données de 7b : **liens** vers le clone de T0.6 : `runs/<RUN6>/manifeste.json`, `diag/<RUN6>/episodes-t06.json` (et compagnons), `donnees/<RUN6>/` ; jamais `diag/<RUN6>/` en entier.
5. **Essais figés** : `tests/test_t07_*.py` (liste et empreintes écrites dans les traces), dernière ligne égale à `ATT` (durée retirée), sinon arrêt.
6. **Empreinte canonique de la configuration** égale à la valeur du § 1, sinon arrêt.
6 bis. **`CODE-T07`** (ordre fixé par la mère : 1. `CODE-T07` inscrite, 2. passe à blanc, 3. étape A) : `python -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md` rejoue, sans rien écrire, le contrôle que la garde de l'étape A refera (ligne présente, sceau, commit cité ancêtre de la tête S7, fichiers du module importé égaux à la liste) ; code ≠ 0 → arrêt, ni passe à blanc ni étape A.
7. **Passe à blanc** (`lecture_v2 passe-blanc`) : échantillon des jeux extrait, frontière, gabarit, **remesure des jetons contre le journal du script** (E-8 : écart = arrêt), durée, mémoire ; sortie scellée sous `passes-blanches-t07/`, committée et **poussée sur la branche neuve** quelle que soit son issue ; code ≠ 0 → arrêt, l'étape A ne part pas.
8. **Étape A** (`lecture_v2 etape-a . <RUN6> <CFG>`, lancée depuis la racine) : avant l'extraction, remesure des jetons (arrêt sur écart) et **rejeu du contrôle 9** contre les textes d'action de 7b (paires en défaut exclues et consignées dans `sondes-t07.json`, consigne v3 des jeux, § 7 et § 10 étape 4 ; E-8, D-2 (a)) ; code 0 → sorties committées et poussées ; code 3 avec motif R11 (garde d'identité) → **une** relance, même carte, même commit, même configuration, run neuf ; tout autre code 3 → nœud, sorties et `arret.json` poussés, aucune relance ; code 2 → refus de la garde, journal poussé, compte rendu.
9. Traces (journal du bloc, sorties standard et d'erreur, essais, `pip freeze`, `nvidia-smi`) poussées ; aucun fichier de plus de 90 Mo (sinon arrêt avant le commit, nœud).

### 4.6 Le bloc (texte remis à l'instance)

```bash
#!/usr/bin/env bash
# etape-a-t07-instance-v1.sh S7 C7 RUN6 CONFIG BRANCHE ATTENDU — étape A de T0.7 sur la machine de 7b ; écrit sous /root/t07-etape-a-v1 seulement
set -uo pipefail
S7="$1"; C7="$2"; RUN6="$3"; CONFIG="$4"; BR="$5"; ATTENDU="$6"
S6=935262b17ca95894a882b02f1526ee39d1738652; URL=https://github.com/lciric/controle-ia-travail.git
R=/root; T6="$R/amorce-depot"; T="$R/t07-etape-a-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-t07.txt"
mkdir -p "$X" || exit 4
j() { printf '%s T07 %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
arret() { j "ARRET : $1"; exit "${2:-4}"; }
# 1. machine
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent"
PY="$T6/.venv/bin/python"; [ -x "$PY" ] || arret "interpréteur de la course absent"
[ -e "$R/t06-fin-normale" ] || arret "fin normale de 7b non marquée"
for f in "runs/$RUN6/manifeste.json" "diag/$RUN6/episodes-t06.json"; do [ -f "$T6/$f" ] && [ -f "$T6/$f.sha256" ] || arret "$f absent du disque de 7b"; done
[ -d "$T6/donnees/$RUN6/activations" ] || arret "activations de 7b absentes du disque"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible"
j "machine conforme ; carte $(head -n 1 "$X/nvidia-smi.txt")"
# 2. dépôt de T0.7 au commit S7
[ ! -e "$D" ] || arret "$D existe déjà (R12)"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$D" || arret "clonage"
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (T0.7)"; git -C "$D" config user.email "instance-calcul@invalid"
MOTIFS='/*
!/*/
/.claude/
/src/
/tests/
/scripts/
!/scripts/extraire_mesures_epreuve_t06_v1.py
/brouillons/T0.7-*
/docs/*
!/docs/*/
/docs/decisions/
/docs/notes/g0-deux-semaines-v1/
/docs/sources/invites-2606.08892-v1/
/prereg/*
!/prereg/contre-lectures/
/registres/*.md
/registres/go-extraits/
!/diag/*/lecture-sondes-t06.json*'
CITES=$(git -C "$D" show "$S7:$CONFIG" | python3 -I -c 'import json, sys
def f(x):
    if isinstance(x, dict):
        if isinstance(x.get("chemin"), str):
            yield x["chemin"]
        for v in x.values():
            yield from f(v)
    elif isinstance(x, list):
        for v in x:
            yield from f(v)
for p in sorted(set(f(json.load(sys.stdin)))):
    print("/" + p); print("/" + p + ".sha256")') || arret "configuration illisible dans S7"
git -C "$D" sparse-checkout init --no-cone && printf '%s\n%s\n' "$MOTIFS" "$CITES" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle"
git -C "$D" checkout -q "$S7" || arret "commit S7 introuvable"
[ "$(git -C "$D" rev-parse HEAD)" = "$S7" ] || arret "tête ≠ S7"
git -C "$D" merge-base --is-ancestor "$C7" "$S7" || arret "C7 n'est pas ancêtre de S7"
git -C "$D" diff --quiet "$C7" "$S7" -- src tests || arret "arbre gelé changé entre C7 et S7"
git -C "$D" fetch -q origin refs/heads/main:refs/remotes/origin/main || arret "fetch de main"
H=$(git -C "$D" rev-parse origin/main); git -C "$D" merge-base --is-ancestor "$S7" "$H" || arret "S7 n'est pas ancêtre de main"
git -C "$D" diff --quiet "$S6" "$S7" -- requirements-cpu.txt requirements-gpu.txt || arret "exigences de paquets changées depuis la course"
j "code conforme : S7 $S7, C7 $C7, main $H"
# 3. registres de main et fichiers cités (CT-17)
for f in $(git -C "$D" ls-tree -r --name-only "$H" -- registres/ | grep -E '^registres/([^/]+\.md(\.sha256)?|go-extraits/[^/]+)$'); do
    mkdir -p "$D/$(dirname "$f")" && git -C "$D" show "$H:$f" > "$D/$f" || arret "registre $f"; done
for p in $(awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); if ($4 ~ /^[A-Za-z0-9._\/-]+$/ && $4 !~ /\.\./) print $4 }' "$D/registres/scellements-v1.md" "$D/registres/prealables-p3bis-v1.md" 2>/dev/null | sort -u); do
    case "$p" in *lecture-sondes-t06*|donnees/bras-attaque*|donnees/mode-tenu-a-l-ecart*|docs/notes/bras-attaque/*|donnees/lecture-b-7a-quarantaine-v1*|scripts/extraire_mesures_epreuve_t06_v1.py) arret "chemin interdit cité par un registre : $p";;
        donnees/"$RUN6"/*) continue;; esac
    for q in "$p" "$p.sha256"; do git -C "$D" cat-file -e "$H:$q" 2>/dev/null || continue
        mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "$H:$q" > "$D/$q" || arret "fichier cité $q"; done
done
for k in SCELLEMENT-JEUX-T07-JD SCELLEMENT-JEUX-T07-JA SCELLEMENT-JEUX-T07-JC SCELLEMENT-CONCEPTS-T07; do      # les quatre lignes (inventaire § 4.3)
    p=$(grep "^| $k |" "$D/registres/scellements-v1.md" | awk -F'|' '{ gsub(/ /, "", $4); print $4 }'); [ -n "$p" ] || { j "$k : ligne absente"; continue; }
    [ -f "$D/$p" ] && [ -f "$D/$p.sha256" ] || arret "$k : $p ou son compagnon absent de main"
    [ "$k" = SCELLEMENT-CONCEPTS-T07 ] && continue
    for f in $(git -C "$D" ls-tree --name-only "$H" -- "$(dirname "$p")/" | grep -E '/journal-verification[^/]*\.txt(\.sha256)?$'); do      # E-8 : journal du script
        git -C "$D" show "$H:$f" > "$D/$f" || arret "journal du script $f"; done
    j "$k : $p présent, compagnon présent ; journaux du script : $(ls "$D/$(dirname "$p")" | grep -c '^journal-verification.*\.txt$')"
done
[ -z "$(git -C "$D" status --porcelain -- src tests)" ] || arret "src ou tests changés par la mise à jour des registres"
j "registres de main $H recopiés ; registre $(sha256sum < "$D/registres/scellements-v1.md" | cut -c1-16)"
# 4. données de 7b, par liens (le clone de T0.6 n'est jamais modifié ; diag/<RUN6>/ jamais lié en entier)
mkdir -p "$D/runs/$RUN6" "$D/diag/$RUN6" "$D/donnees"
for f in "runs/$RUN6/manifeste.json" "runs/$RUN6/manifeste.json.sha256" "diag/$RUN6/episodes-t06.json" "diag/$RUN6/episodes-t06.json.sha256"; do
    if [ -e "$D/$f" ]; then cmp -s "$D/$f" "$T6/$f" || arret "$f du dépôt ≠ disque de 7b"; else ln -s "$T6/$f" "$D/$f" || arret "lien $f"; fi; done
[ ! -e "$D/donnees/$RUN6" ] || arret "donnees/$RUN6 déjà présent dans le dépôt de T0.7"
ln -s "$T6/donnees/$RUN6" "$D/donnees/$RUN6" || arret "lien donnees/$RUN6"
# 5. essais figés de T0.7 (aucun couperet de temps)
cd "$D" || arret "dépôt"
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
sha256sum tests/test_t07_*.py > "$X/essais-liste.txt"
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no tests/test_t07_*.py --basetemp="$T/essais-tmp" -o tmp_path_retention_policy=failed > "$X/essais.txt" 2> "$X/essais.err"; c=$?
DL=$(tail -n 1 "$X/essais.txt" | sed -E 's/ in [0-9.]+s.*$//'); j "essais : code $c, $DL"
[ "$c" = 0 ] && [ "$DL" = "$ATTENDU" ] || arret "essais de T0.7 : code $c, « $DL » attendu « $ATTENDU »"
E=$(PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 empreinte-config "$CONFIG") || arret "empreinte de la configuration"
j "configuration $CONFIG, empreinte canonique $E"
PYTHONPATH=src "$PY" -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md > "$X/code-t07.txt" 2>&1 || arret "CODE-T07 non conforme (code-t07.txt) : ni passe à blanc ni étape A"
j "$(head -n 1 "$X/code-t07.txt")"
# 6. branche neuve et poussées
git ls-remote --exit-code origin "refs/heads/$BR" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR présente sur le dépôt distant (R12) ou dépôt injoignable"
git checkout -q -b "$BR" || arret "branche locale"
gros() { find "$@" -type f -size +90M 2>/dev/null | head -n 1; }
pousser() {  # $1 = message ; $2… = chemins (ajout explicite des seuls chemins présents, jamais -A)
    local m="$1" x a=(); shift; for x in "$@"; do [ -e "$x" ] && a+=("$x"); done
    [ -z "$(gros "${a[@]}")" ] || arret "fichier de plus de 90 Mo : $(gros "${a[@]}") (nœud)"
    git add --sparse -f -- "${a[@]}" && git commit -q -m "$m" || arret "commit « $m »"
    local n; for n in 1 2 3; do git push -q origin "HEAD:refs/heads/$BR" && { j "poussé : $(git rev-parse HEAD) « $m »"; return 0; }; sleep $((20 * n)); done
    arret "poussée « $m » impossible"; }
# 7. passe à blanc (aucune donnée décisive)
PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 passe-blanc . "$RUN6" "$CONFIG" > "$X/passe-blanc.txt" 2> "$X/passe-blanc.err"; c=$?
j "passe à blanc : code $c ; $(head -n 1 "$X/passe-blanc.txt")"
XT=traces/t07-etape-a-v1; traces() { mkdir -p "$D/$XT" && cp -f "$X"/* "$D/$XT/"; }      # traces copiées dans le dépôt pour le commit
[ -d passes-blanches-t07 ] && traces && pousser "T0.7 : passe à blanc de l'extracteur (aucune donnée décisive), code $c" passes-blanches-t07 "$XT"
[ "$c" = 0 ] || arret "passe à blanc : code $c : l'étape A ne part pas (motif : passe-blanc.err, sortie scellée)"
# 8. étape A (une relance seulement après un arrêt R11 de la garde d'identité)
for essai in 1 2; do
    PYTHONPATH=src "$PY" -m controle_ia.t07.lecture_v2 etape-a . "$RUN6" "$CONFIG" > "$X/etape-a-$essai.txt" 2> "$X/etape-a-$essai.err"; c=$?
    RUN7=$(ls -1 runs 2>/dev/null | grep -- '-t07-lecture-' | sort | tail -n 1); j "étape A, essai $essai : code $c, run $RUN7"
    traces; CH=(registres/scellements-v1.md registres/scellements-v1.md.ouvertures.md "$XT")
    [ -n "$RUN7" ] && CH+=("runs/$RUN7" "diag/$RUN7") && [ -d "donnees/$RUN7" ] && CH+=("donnees/$RUN7")
    pousser "T0.7, étape A (essai $essai) : sorties scellées, code $c${RUN7:+, run $RUN7}" "${CH[@]}"
    [ "$c" = 0 ] && { j "FIN : étape A menée au bout, run $RUN7, tête $(git rev-parse HEAD)"; exit 0; }
    if [ "$c" = 3 ] && [ "$essai" = 1 ] && grep -q 'R11' "$X/etape-a-1.err"; then j "arrêt R11 (garde d'identité) : une relance, même carte, même commit"; continue; fi
    arret "étape A : code $c (essai $essai) : nœud, aucune relance (motif : etape-a-$essai.err)" 3
done
arret "étape A : second arrêt R11 : nœud de Lazar" 3
```

Lignes imprimées (`… T07 …`) : seules lues par l'exécutante. Les sorties de l'étape A ne sont ni imprimées ni affichées (§ 2.5) ; `etape-a-*.txt` porte le chemin des scores et les noms des sondes lues, rien d'autre.

### 4.7 Surveillance et vérification de la poussée (session)

- Toutes les 15 minutes : état (§ 4.2), lignes `T07` neuves par la voie, cumul de la dépense (§ 6) écrits au journal ; aucun couperet de temps.
- À la ligne `FIN` (ou `ARRET`) : la tête de la branche se vérifie **sans rien rapatrier des sorties** :

```bash
# (A)
git -C "$M" ls-remote origin "refs/heads/$BR"; git -C "$M" fetch -q origin "refs/heads/$BR:refs/remotes/origin/$BR" && git -C "$M" log --oneline "$S7..origin/$BR" && git -C "$M" diff --stat "$S7" "origin/$BR" -- src tests | tail -n 1
R7=refs/remotes/origin/$BR; for f in $(git -C "$M" diff --name-only --diff-filter=A "$S7" "$R7" -- runs diag donnees passes-blanches-t07 | grep -v '\.sha256$' | grep -v 'lecture-sondes-t06'); do a=$(git -C "$M" show "$R7:$f" | sha256sum | cut -d' ' -f1); b=$(git -C "$M" show "$R7:$f.sha256" 2>/dev/null | cut -d' ' -f1); [ "$a" = "$b" ] && echo "OK $f" || echo "ÉCART $f"; done
```

Attendu : les commits du § 4.5 (passe à blanc, étape A, traces), **aucun changement sous `src` ni `tests`** (ligne vide), `OK` pour chaque fichier **ajouté par l'instance** (seuls ceux-là sont hachés : jamais un fichier de `diag/` ou `runs/` venu de `main`, où peuvent se trouver ceux de 7a ; liens de la course jamais committés). Les fichiers sont hachés, jamais affichés.

### 4.8 Arrêt et destruction par l'identifiant (R10), inventaire final

Après la poussée vérifiée (ou sur un arrêt, une fois les traces poussées, ou à l'échéance) :

```bash
# (A)
timeout -k 5 120 vastai destroy instance "$ID" -y; echo "code $?"; j "destruction demandée"
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>&1); c=$?; [ "$out" = '{"instances": null}' ] && echo "absente (texte exact), code $c" || echo "texte autre (non affiché), code $c"
```

**Au plus tard le 2026-11-16 à 23:00Z, quoi qu'il arrive** ; si l'étape A n'est pas menée au bout à cette heure, les traces poussées font foi et l'étape passe en **variante B** (nœud de la mère). Un arrêt de dépense (§ 6) se fait par `timeout -k 5 120 vastai stop instance "$ID"` (identifiant seul), puis destruction à la décision de la mère avant la même échéance. Jamais `pkill`, `killall`, ni un geste sur une autre instance.

## 5. Variante B (si la voie (b) du § 0 bis est retenue, ou si l'instance de 7b n'est plus disponible)

Mêmes préalables, sauf P7 (instance gardée) remplacé par : branche de 7b poussée avec `donnees/<RUN6>/adaptateur-*.pt`, `textes-actions-t06.jsonl`, `mesures-t06.npz` et le sous-ensemble d'activations (amorce l. 318-321), compagnons `OK` ; ligne **`GO-LECTURE-T07`** (extrait scellé) au lieu de `GO-ETAPE-A-T07` ; engagement sous cette ligne. Le bloc du § 4.6 change en trois points : (1) les données de 7b viennent d'un clone de la branche de 7b **sans** `diag/*/lecture-sondes-t06.json*` (motif d'exclusion de l'extraction partielle), non du disque ; (2) le modèle est descendu (≈ 16 Go) ; (3) l'étape A est lancée par `lecture_v2 repli-recalcul . <RUN6> <CFG>` (garde d'équivalence au lieu de la garde d'identité ; R11 : une relance). La machine (création, minuterie, destruction) relève d'un lanceur et d'une amorce de T0.7 **non écrits** : à écrire, essayer en local et contre-lire avant toute création.

## 6. Dépense (contre 20 USD, GO-2026-11-10-04)

- **Relevé** (session, à chaque surveillance et avant le redémarrage) : stockage depuis l'arrêt de 7b, plus carte depuis le redémarrage, plus 0,10 USD de téléchargement forfaitaire :

```bash
# (A) ; TR=0 avant le redémarrage
python3 -I -c 'import sys, time; pc, ps, ta, tr = map(float, sys.argv[1:5]); n = time.time(); c = ps * (n - ta) / 3600 + (pc * (n - tr) / 3600 if tr > 0 else 0.0) + 0.10; print(f"cumul {c:.2f} USD ; projeté + 5 h de carte {c + 5 * pc:.2f} USD")' "$PC" "$PS" "$TA" "${TR:-0}"
```

- **Avant le redémarrage** : projeté ≤ 20 USD, sinon nœud (devis neuf) ; A100 à 1,30 USD de l'heure : ≈ 6,5 USD de carte au pire, plus le stockage (≤ 0,08 USD de l'heure).
- **10 USD** cumulés : compte rendu à Lazar dans la session de l'exécutante (copie à la mère), **aucun arrêt** (plafond du brouillon 19 ; proposé, § 10).
- **20 USD** : dès que cumul + un quart d'heure de carte ≥ 20 USD, arrêt par l'identifiant (§ 4.8), nœud, aucune relance sans un mot de Lazar sur un devis neuf.
- La facture, si connue, fait foi. La dépense de l'étape A est inscrite sous GO-2026-11-10-04, non sous GO-2026-11-02-28 (que la minuterie de 7b compte aussi : double compte à déclarer au registre des dépenses).

## 7. Arrêts

- Préalable manquant, empreinte différente, code non conforme, essais différents de l'attendu, passe à blanc non tenue (code 3 : frontière, mémoire ou extraction de l'échantillon) : **l'étape A ne part pas** ; traces poussées ; arrêt de l'instance par l'identifiant ; compte rendu ; nœud de la mère.
- Étape A : code 3 R11 → une relance (bloc) ; second R11 → nœud de Lazar ; autre code 3 → nœud, aucune relance ; code 2 → compte rendu (une clé exigée absente se règle avant le redémarrage, P1 à P3).
- Dépense (§ 6) ; échéance (§ 4.8) ; instance non `running` deux heures après la demande ; amorce de 7b qui annonce une destruction : arrêt, compte rendu.
- Refus d'un contrôle ou d'un classifieur : arrêt et rapport tel quel ; aucun contournement.

## 8. Compte rendu de l'exécutante (nombres seuls, ≤ 400 mots)

`vastai --version` ; P0 à P11 (valeurs) ; heure du redémarrage et de `running` ; empreinte du bloc remis ; lignes `T07` : machine, code, registres, essais (dernière ligne), empreinte canonique ; **passe à blanc** : code, issue, frontière par jeu (enregistrements, exactes, ajustées, fautes), gabarit, mémoire (besoin de l'hôte et disponible, pic de la carte et total, en Gio), durée du chargement et durée estimée de l'extraction, chemin et empreinte de sa sortie ; étape A : code, run, essais ; tête de la branche, commits, `OK` / `ÉCART` ; dépense relevée ; destruction, inventaire final ; écarts. **Ni score, ni aire, ni contenu des sorties de l'étape A.** Journal (garde des secrets à 0) envoyé à la mère, qui le verse et le scelle.

## 9. Ce qui suit, et ce que cet ordre ne fait pas

- **Suite (mère)** : la mère recopie **à l'octet**, dans le registre et le journal des ouvertures de `main`, les lignes `SCORES-T07`, `SONDES-T07` et `OUVERTURE-T07` écrites sur l'instance (branche de sortie), **après** avoir vérifié que le journal de P3-bis de `main` ne porte aucune ligne datée avant la fin de l'étape A qui manquait à la copie recopiée au point 3 du bloc (sinon nœud : la garde de fin d'étape A a lu une copie ; G2, G4) ; dépense inscrite ; étape B sur processeur, plus tard, par son propre ordre.
- **Ne fait pas** : aucun épisode, aucune étape B, aucune lecture de sortie, aucune modification du code, du texte scellé, de la configuration ou de la chaîne de T0.6 ; aucune fusion ; aucune écriture sur `main` par l'exécutante ni par l'instance ; aucun contact externe ni appel de modèle.

## 10. À juger par la contre-lecture

1. **PB-1** et le choix de la voie (§ 0 bis) ; sous (a), la forme exacte de la recréation et sa preuve à blanc.
2. **Registres recopiés de `main` sur S7** (CT-17) au lieu d'un commit de lancement propre : l'arbre est déclaré non propre au manifeste ; l'alternative est un commit `L7` (S7 plus les seuls registres et fichiers cités), poussé par la mère, qui rend l'arbre propre.
3. **Garde de fin d'étape A** : elle lit la copie du journal de P3-bis faite à l'ouverture ; la mère refait la vérification sur `main` avant de recopier les lignes (§ 9).
4. **Liens** vers le disque de 7b (trois fichiers, un dossier) au lieu d'une copie : aucune écriture dans le clone de T0.6 ; `git add` explicite, les liens ne sont jamais committés.
5. **Journal du script des jeux cherché dans le dossier du jeu** (`journal-verification*.txt`, un seul qui porte le jeu) : convention de dépôt, à nommer par le brouillon 21 ou par une ligne de registre ; absent en mode réel : arrêt (passe à blanc et étape A).
6. **Essais sur l'instance** : Python 3.11 et `requirements-gpu.txt` contre Python 3.13 dans la session ; la dernière ligne attendue (`ATT`) est celle d'un jeu des essais au commit C7 dans l'environnement de l'instance, ou de la session si la contre-lecture l'accepte (écart possible : essais sautés).
7. **Seuil de 10 USD** (compte rendu) et marge d'un quart d'heure (arrêt) : proposés.
8. `git add --sparse` (git ≥ 2.35) : version de git de l'image de 7b à relever (non vérifiée).
9. Le bloc n'est **pas répété** en jouet : à répéter sur une machine locale (racine factice `/root` remplacée) avant la remise.

## 11. Marqueurs (à remplir par la mère ; une occurrence chacun)

| Marqueur (sans chevrons) | Où | Valeur |
|---|---|---|
| `ID_SESSION_EXECUTANTE` | en-tête | identifiant de la session qui exécute |
| `VOIE_EXECUTION_INSTANCE` | § 0 bis | option retenue (a), (b) ou (c), mot de Lazar s'il en faut un, ligne de registre |
| `EMPREINTE_CONFIG_T07` | § 1 | empreinte canonique de la configuration de T0.7 scellée |
| `ID_INSTANCE_7B` | ligne (A) | identifiant de l'instance de 7b (compte rendu de la fille) |
| `RUN_T06_7B` | ligne (A) | run de 7b (`AAAAMMJJ-HHMMSS-t06-reel`) |
| `COMMIT_CODE_T07` | ligne (A) | commit du code de T0.7 contre-lu et répété (C7) |
| `COMMIT_SCELLEMENT_T07` | ligne (A) | commit de scellement de T0.7 (S7), descendant de C7, arbre gelé égal |
| `CHEMIN_CONFIG_T07` | ligne (A) | chemin de la configuration scellée dans S7 |
| `LIGNE_ESSAIS_T07` | ligne (A) | dernière ligne attendue des essais `tests/test_t07_*.py` au commit C7, durée retirée (au commit de ce brouillon, dans la session : rapport « -complement-v3 ») |
| `PRIX_CARTE_USD_H` | ligne (A) | prix horaire de la carte de 7b (`prix_carte` de `lancement.txt`) |
| `PRIX_STOCKAGE_USD_H` | ligne (A) | prix horaire du stockage (`prix_stockage`) |
| `INSTANT_ARRET_7B_UTC` | ligne (A) | heure de l'arrêt de l'instance à la fin de 7b, en secondes UTC |
| `LIGNE_SCELLEMENT_T07` | § 4.1 | la ligne `SCELLEMENT-T07` exacte de la remise de 7b |

Sources : `scripts/lancer_t06_v13.sh` et `scripts/amorce_instance_t06_v11.sh` au commit `1609a4bf` ; ordre de 7b brouillon 2 (`488c2e51…`) ; `registres/go.md` et `registres/decisions.md` de `main` `1821ed26` (R-060, R-821, R-1590, R-2087, R-2089) ; brouillon 19 de T0.7 (`07039ed2…`) ; inventaire des jeux (`c9910a54…`, § 4.3) ; module `src/controle_ia/t07/` au commit `a3539339` (passe à blanc `passe_blanc_v1.py`, contrôles des jeux `controle_jeux_v1.py`, `CODE-T07` `code_t07_v1.py`), essais : 310 passés, 1 sauté, 3 xfail.
