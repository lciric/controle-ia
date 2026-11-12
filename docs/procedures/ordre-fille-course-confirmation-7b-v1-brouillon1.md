# Ordre — course de confirmation 7b de T0.6 (organismes v0, sous préenregistrement scellé), session fille porteuse des clés — v1, brouillon 1

> **COURSE DÉCISIVE (R1), SORTIE SCELLÉE AVANT LECTURE.** La fille lance, surveille, arrête, rapatrie et détruit ; elle **ne lit aucun résultat**. L'embargo DT-4 (§ 2) est rappelé nommément parce que la course 7a l'a vu rompre par la faute d'une consigne de la mère (R-2041).

- **Statut** : brouillon 1, écrit le 2026-11-10 à partir de 06:46 UTC (heure relevée par `date -u` ; écriture commencée à 06:52 UTC) par un **rédacteur neuf**, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (Claude Opus 5.5), qui n'a écrit ni T0.6, ni T0.7, ni P3-bis, ni leurs contre-lectures, ni l'ordre de 7a, et n'est ni le lecteur exploratoire de 7a (R-2041) ni l'auditeur de l'écart DT-4 (R-2057). Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-redaction-ordre-7b-v1.md` (`0dca9d5b3564effa3a95fffe833627219073437ca40964ada7fee8b3ffc36296`, vérifiée avant lecture). Journal du rédacteur : `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon1-journal-v1.md`. **Non contre-lu.** Étapes avant la remise : marqueurs remplis par la mère (§ 14), contre-lecture (R2) par un sous-agent neuf qui ne l'a pas écrit, scellement de l'ordre, remise par Lazar à la fille.
- **Autorisation** : R-2077 (mot de Lazar du 10 novembre 2026, reçu vers 06:04 UTC ; lecture de la mère écrite au registre) : **création de 7b autorisée sous GO-2026-11-02-28**, plafond de la configuration 200 USD, **compte rendu à Lazar à 60 USD de dépense**, **mot de Lazar avant toute création sur H200** ; R-2079 (« (c) go ») : chaîne gelée v13, création au plus tard le 15 novembre, bascule éventuelle vers une chaîne v14 décidée le 13 novembre à 12:00 UTC si T0.7 n'est pas scellé ; R-2082 : T0.6 scellé (commit de scellement S `935262b17ca95894a882b02f1526ee39d1738652`, fusionné dans `main` à `1756f1cb`).
- **Exécutante** : la session fille `<<ID_SESSION_FILLE>>`, porteuse des clés, active pendant toute la course (§ 9).

## 0. Ce que cette course est, et n'est pas

- **Elle est** la course de confirmation « 7b » que préenregistre `prereg/T0.6-organismes-v0-v1.md` (révision 10, `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`) : organisme (ii) par adaptateur de rang faible à dose réglable, distillation sur les 32 tâches de réserve, neuf conditions sur les 64 tâches d'évaluation, activations, test croisé et couples descriptifs joués par la chaîne sur l'instance, **deux résultats scellés séparés** (le coût ; les sondes, fermé jusqu'au verdict scellé de P3-bis), poussés sur une branche neuve. Graines neuves : l'entropie citée par le texte (`31538212097275005629337336542801867913`), qui n'a servi à aucun run. Même chaîne que 7a (lanceur v13, amorce v11, code `1609a4bf`), configuration de 7b (`prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1ba…`, six champs d'écart avec celle de 7a, R-2056).
- **Elle n'est pas** une lecture : ni la table A (coût), ni les tables B et C (sondes), ni la règle « mots et coût » ne sont lues par la fille ni pendant la course (§ 11). Elle n'est ni une étape de T0.7, ni P3-bis, ni le bras d'attaque.

## 1. Cadre

| Élément | Valeur |
|---|---|
| Texte scellé | `prereg/T0.6-organismes-v0-v1.md`, `ef31feff…` (révision 10) ; sections lues pour cet ordre : « Plan d'analyse » (point 9 : carte, fenêtre, relance de DT-6), « Liste d'arrêt », « Devis » (confirmation 7b, ligne d'engagement), « Ce qui manque pour lancer » (plan de la confirmation, points 3, 5 et 6) |
| Commit de scellement S | `935262b17ca95894a882b02f1526ee39d1738652`, ancêtre d'`origin/main` ; c'est lui que l'instance clone (`COMMIT=$S`) ; le lanceur le trouve comme le commit qui ajoute `prereg/T0.6-organismes-v0-v1.md.sha256` (`commit_s`, lanceur l. 112) |
| Commit du code cité | `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` (ligne « Commit du code d'analyse » du texte) ; l'arbre gelé de S est le sien (`exiger_code_cite`) |
| Configuration | `prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`, empreinte canonique `ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d` ; `go_id` GO-2026-11-02-28, `plafond_usd` 200, `fraction_equivalence` 0,05, dernier jour de création 2026-11-15, fin du GO 2026-11-17T00:00:00Z (`fin_go_utc_s=1794873600`), carte de course A100 SXM4 ≤ 1,30 USD/h et ≥ 80 000 Mo, carte de relance H200 NVL ≤ 4,70 USD/h et ≥ 140 000 Mo, stockage ≤ 0,08 USD/h, téléchargement ≤ 0,05 USD/Go, disque 150 Go, étiquette `t06-v2` |
| Chaîne gelée (au commit `1609a4bf`, identique sur `main` : § 4.2) | lanceur `scripts/lancer_t06_v13.sh` `6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416` ; amorce `scripts/amorce_instance_t06_v11.sh` `43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859` ; `src/controle_ia/t06/session.py` `ad7031ab028787a3ea4bc4edfbf86206f56ccd916f447a150b639ba96f50bb17`, `session_v2.py` `6d9f75989e5e21a26b600378167a84f349d4dbc1a9c8740ede7d8471f6779266`, `session_v3.py` `365d2fde7fe9c4670fd3f2bcb404c3979b1db4e3cc862f0a4a46acf867b4bcf3`, `session_v12.py` `5b4ad5e9fa39c4a803050ed118157d005bcb30551a54a6822f38a15ca0ddd90e`, `lanceur_v6.py` `e329493b5d54fe52f6eb278b1314a78f905ca082a51ee1a0c5c3a77bd400ac80`, `configuration_v6.py` `7899622515588284d1045c72aee95d109ff755f525d3c4bcd70df14caf6fad8e` ; suite ciblée `scripts/tests-cibles-t06-v3.txt` `e76d5e6b7c32140b549de20f061a2e562df9201c5daab4060fd1ca54a05f42e2` et exclusions `scripts/tests-exclus-t06-v3.txt` `ab70a1ed4b59bdb5f488e453055029806cde30c36552684f686097fbea8ed81c` ; bras B `src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py` `317a7ea551abace1b3b78acde543688ab33bfda57cd15d8e6072f0826ce6fa17`. **Jamais une chaîne v14** (préparée sans être adoptée, R-2079) |
| Mode de la chaîne | **course** (sous-commandes `controles` puis `creation`), jamais `controles-epreuve` ; en course, le lanceur écrit `GO_ID=GO-2026-11-02-28` en dur (l. 83), exige la configuration à 200 exactement (l. 197) et ne passe à l'instance ni `MODE`, ni `CONFIG`, ni `PREREG_ABSENT`, ni `TESTS_ATTENDUS` (l. 234) : l'amorce lit la configuration et « Tests attendus » (`2022`) dans le texte de S (amorce l. 375 à 388) |
| GO | **GO-2026-11-02-28** (seule ligne lue par la chaîne en course ; plafond 200 USD ; échéance 2026-11-16) ; rattachés : GO-2026-11-07-02 (carte de repli H200, échéance 16 novembre), GO-2026-11-07-04 (bras B, échéance 16 novembre) ; **GO-2026-11-10-01** (prolongation au 23 novembre, non cumulée) **n'est pas lue par la chaîne v13** : elle ne permet aucune création après le 15 novembre (R-2077) |
| Branche de sortie | **`calcul/t06-confirmation-7b-v1`** (`T06_BRANCHE`), absente du dépôt distant avant la création (§ 4.5) ; toute seconde instance : `calcul/t06-confirmation-7b-v2`, puis `-v3` (R12) ; jamais la branche par défaut `calcul/t06-reel-v4`, jamais `main` |
| Dépôt | `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, écrit en dur dans la commande de création du lanceur v13 (l. 235) ; vérifié dans la commande imprimée (§ 4.9) ; jamais `lciric/controle-ia` |
| Outil de location | `vastai` 1.8.3 (version de 7a) ; autre version ou outil absent : arrêt, compte rendu à la mère (aucune installation par la fille sans écrit de la mère) |
| Dossier de travail | `/home/user/course-7b-v1` (neuf ; s'il existe : `-v2`, R12) ; dossier des contrôles `c7b-1` (neuf à chaque reprise des contrôles : `c7b-1-r2`, …) |

## 2. Embargo DT-4 — rappelé nommément (faute de la mère à 7a, R-2041)

À 7a, l'ordre (§ 4 B) demandait la courbe par état sans rappeler DT-4, la consigne de la mère au lecteur n'a pas relevé le conflit, et un lecteur a vu des valeurs de `lecture-sondes-t06.json` avant le verdict de P3-bis (R-2041 ; Lazar : isoler et auditer, R-2048 ; audit « aucune trace trouvée », R-2057). Pour 7b, la fille tient ceci, sans exception :

1. **Jamais** elle n'ouvre, n'affiche, ne copie, ne hache ni ne passe à un script ou à un outil un fichier `lecture-sondes-t06.json` (ni celui de 7b, ni celui de 7a, ni celui d'aucun run), ni son compagnon. Pour cela : ses clones excluent `diag/*/lecture-sondes-t06.json*` de l'extraction (§ 4.1) ; le rapatriement se fait **sans les contenus de fichiers** (`--filter=blob:none`) et n'extrait que les fichiers que cet ordre nomme (§ 4.12) ; toute liste de fichiers passe par l'exclusion `':(glob,exclude)diag/*/lecture-sondes-t06.json*'`, pour que ce nom ne sorte même pas d'une commande. La présence du résultat des sondes se déduit de celle de `resume.json` (écrit après lui, `lanceur_v6.py` l. 317 à 333).
2. **Jamais** la branche de quarantaine `donnees/lecture-b-7a-quarantaine-v1`, ni la branche de 7a `essai/t06-explo-v3`, ni aucun `diag/`, `runs/` ou `donnees/` de 7a (`20261109-070232-t06-reel`). Ses clones sont faits sur la seule branche `main` (`--single-branch`) ; elle ne fait jamais de `git fetch` sans refspec explicite.
3. **Jamais** l'extracteur `scripts/extraire_mesures_epreuve_t06_v1.py` (il ouvre le fichier des sondes en entier, R-2057) : jamais lancé, et exclu de l'extraction de ses clones.
4. **Jamais** `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, ni l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`) ; exclus de l'extraction de ses clones.
5. **Aucune lecture de résultat de 7b** : jamais affichés `lecture-cout-t06.json` (table A, lue par un lecteur neuf, § 11), `resume.json` (il porte les lignes des tables A, B et C : `lanceur_v6.py` l. 324 à 332), `distillation-t06.json`, `episodes-t06.json`, `run.err`, `run.json` ; jamais rapatriés ni ouverts les fichiers de `donnees/<run>/` (mesures, textes des actions, adaptateurs, activations : la pièce « mots et coût » doit être écrite par des auteurs qui ne les ont pas vus, texte, « Concordance avec T0.7 », point 2). Ces fichiers ne sont que **hachés** (comparés à leur compagnon) quand l'ordre le dit, sans affichage.
6. **Ce que la fille lit** (et rien d'autre) : les sorties et codes des commandes de cet ordre ; dans le dossier des contrôles, `lancement.txt`, `progres.txt`, `surveillance.txt`, `journal-instance.txt` ; sur la branche de sortie, `runs/<run>/manifeste.json` (champs nommés au § 4.12), `traces/t06-*/journal.txt` et `traces/*/empreintes.sha256`, et, en cas d'arrêt, les seuls champs `etape` et `motif` de `diag/<run>/arret.json` ; la dépense (§ 6). Les sorties du bras B ne sont pas lues (§ 7).
7. Toute ligne qui porterait un état, une aire, un score ou une ligne de table de sonde (ce que la chaîne n'écrit pas dans ses journaux : texte, plan, point 6 ; amorce, filtre C01, l. 300 et 502 à 504) est un écart : la fille n'en recopie rien, s'arrête de lire et le dit à la mère.

## 3. Préalables bloquants — vérifiés par la fille avant toute création, écrits dans son journal avec l'heure (`date -u`)

| # | Préalable | Comment la fille le vérifie (§ 4) | Sinon |
|---|---|---|---|
| P1 | **T0.6 scellé** : S `935262b1…` ancêtre d'`origin/main` ; `commit_s` rend S ; texte à S `ef31feff…` ; configuration à S `b7a5c1ba…` ; `1609a4bf` ancêtre de S | § 4.2, puis `controles` (§ 4.4) | arrêt, compte rendu |
| P2 | **T0.7 scellé** (GO-2026-11-02-28 : « sous les préenregistrements de T0.6 et T0.7 contre-lus, scellés, committés et poussés avant la course ») : exactement une ligne `SCELLEMENT-T07` dans `registres/scellements-v1.md` de `main`, égale à celle que la mère a inscrite (§ 14), et le fichier qu'elle cite a, à la tête de `main`, l'empreinte de la ligne et un compagnon conforme | § 4.3 | aucune création ; si la ligne manque encore le **13 novembre à 12:00 UTC**, cet ordre est **suspendu** (bascule de R-2079, nœud de Lazar) : rien n'est créé sous lui sans un addendum de la mère |
| P3 | **Ligne de GO lue par la chaîne : GO-2026-11-02-28**, une seule ligne à cet identifiant, non révoquée (de même GO-2026-11-07-02 et GO-2026-11-07-04) ; `controles` imprime « `GO-2026-11-02-28 conforme (plafond 200 USD, 2026-11-02 → 2026-11-16)` » | § 4.3, § 4.4 | aucune création |
| P4 | **Jour** : création au plus tard le **15 novembre 2026** (le calendrier de la configuration la refuse le 16) ; **au plus tard le 14 novembre vers 17:00 UTC pour garder une relance complète** (texte, « Devis », calendrier ; fenêtre de 3 heures comprise : la commencer au plus tard vers 14:00 UTC le 14) ; sans nœud au plus tard **2026-11-15T20:48Z** ; plus tard ce jour-là : nœud de Lazar (« Liste d'arrêt », L11) | `date -u` ; `controles` puis `creation` rejouent le calendrier | après 2026-11-15T20:48Z : aucune création sans mot de Lazar qui accepte ce retard ; le 16 : aucune création (chaîne v14 et version neuve de T0.6 : nœud) |
| P5 | **Commit de remise** : la tête de `main` clonée descend du commit de `main` qui porte cet ordre scellé, la ligne `SCELLEMENT-T07` et la ligne d'engagement (§ 14) ; l'empreinte de cet ordre égale celle du message de remise | § 4.1 | arrêt, compte rendu |
| P6 | **Ligne d'engagement** au registre des dépenses de `main` (écrite et poussée par la mère, texte au § 6) ; dépense antérieure sous GO-2026-11-02-28 et GO-2026-11-10-01 relevée par la mère (§ 14 ; attendu 0) | § 4.3 | aucune création |
| P7 | **Bras B** : conditions de GO-2026-11-07-04 (code, essais et ordre contre-lus et scellés avant la course) constatées par la mère au registre (§ 7, § 14) | § 4.3 | aucune création (le bras B ne peut pas être débrayé sans changer la commande imprimée : § 7) |
| P8 | **Chaîne** : fichiers du § 1 égaux à ceux de `1609a4bf` dans le clone de `main` ; `controles` en ligne conforme ; branche de sortie absente du dépôt distant ; gardes rejouées conformes dans le clone fait comme celui de l'amorce, et cas d'artefact refusé | § 4.2, § 4.4 à § 4.6 | arrêt, compte rendu |
| P9 | **Outil et clés** : `vastai --version` = 1.8.3 ; `HF_TOKEN` et le jeton GitHub (`CONTROLE_IA_GITHUB_TOKEN_2`, ou `CONTROLE_IA_GITHUB_TOKEN`) présents, vérifiés **par le nom seul** | § 4.0 | arrêt, compte rendu |
| P10 | **Compte** : aucune instance dont l'étiquette commence par `t06-v2` (le lanceur refuserait, code 3) | § 4.7 | arrêt, compte rendu ; la fille ne touche à aucune instance qu'elle n'a pas créée |

## 4. Étapes et commandes exactes

L'état du shell ne survit pas d'une commande à l'autre : **chaque bloc commence par la ligne d'affectations (A)**, recopiée telle quelle. Toute heure écrite au journal est relevée par `date -u`. Aucune commande n'affiche une valeur de clé : les clés passent **par leur nom** (`NOM="${NOM:-}"`, développé par le shell sans affichage).

**(A)** :

```bash
W=/home/user/course-7b-v1; M=$W/main; AM=$W/amorce; D=$W/c7b-1; J=$W/journal-fille-7b-v1.md; S=935262b17ca95894a882b02f1526ee39d1738652; C=1609a4bf2c1572f72bb8542d81d963ac6a8481c4; B=calcul/t06-confirmation-7b-v1; URL=https://github.com/lciric/controle-ia-travail.git; PY=/home/user/controle-ia-travail/.venv/bin/python; ANT0=<<DEPENSE_ANTERIEURE_USD>>; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }; champ() { sed -n "s/^$1 //p" "$D/lancement.txt" | tail -1; }
```

`PY` : l'interpréteur du dépôt de la fille où `import controle_ia.t06.lanceur` réussit (paquets de `requirements-cpu.txt`, dont torch) ; s'il est ailleurs, son chemin réel, consigné. `D`, `B` et `W` changent de nom à chaque reprise (§ 1) ; le nom en vigueur est écrit au journal.

### 4.0 Dossier, journal, enveloppe du lanceur, outil et clés

```bash
# (A)
mkdir "$W" && : > "$J" && j "début de l'ordre de 7b ; session $(hostname) ; dossier $W" || echo "ARRÊT : $W existe déjà (R12)"
cat > "$W/v13.sh" <<'FIN'
#!/usr/bin/env bash
# Enveloppe du lanceur gelé v13 : variables passées à env -i par leur NOM seulement ; aucune valeur écrite ici.
# Usage : bash v13.sh BRANCHE_DE_SORTIE SOUS-COMMANDE ARGUMENTS…
set -u
B="${1:?branche de sortie}"; shift
cd /home/user/course-7b-v1/main || exit 2
exec env -i PATH="$PATH" HOME="$HOME" LANG="${LANG:-C.UTF-8}" VAST_API_KEY="${VAST_API_KEY:-}" HF_TOKEN="${HF_TOKEN:-}" GH_TOKEN="${GH_TOKEN:-}" CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN:-}" CONTROLE_IA_GITHUB_TOKEN_2="${CONTROLE_IA_GITHUB_TOKEN_2:-}" GO_ID=GO-2026-11-02-28 T06_BRANCHE="$B" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" HTTPS_PROXY="${HTTPS_PROXY:-}" NO_PROXY="${NO_PROXY:-}" INTERVALLE="${INTERVALLE:-60}" bash scripts/lancer_t06_v13.sh "$@"
FIN
sha256sum "$W/v13.sh"
vastai --version
for k in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN CONTROLE_IA_GITHUB_TOKEN_2 VAST_API_KEY; do if [ -n "${!k:-}" ]; then echo "$k présente"; else echo "$k absente"; fi; done
```

- Si `/home/user/course-7b-v1` existe déjà, la fille prend `-v2` dans (A) et dans l'enveloppe (ligne `cd`), et le consigne.
- **Liste exacte des variables d'`env -i`** (quinze noms) : `PATH HOME LANG VAST_API_KEY HF_TOKEN GH_TOKEN CONTROLE_IA_GITHUB_TOKEN CONTROLE_IA_GITHUB_TOKEN_2 GO_ID T06_BRANCHE REQUESTS_CA_BUNDLE SSL_CERT_FILE HTTPS_PROXY NO_PROXY INTERVALLE` ; les quatre variables du mandataire de sortie viennent de l'addendum 1 de l'ordre de 7a (`8075ae07…` : sans elles, `vastai` refuse le certificat du mandataire) ; ce sont des chemins et une adresse, jamais affichés ; aucune n'est transmise à l'instance (vérifié au § 4.9). `GO_ID=GO-2026-11-02-28` sert à la garde de calcul ; en course, le lanceur ne lit pas cette variable (l. 82–83 : il écrit lui-même ce GO dans la commande de création, l. 235, et rejoue la garde sur elle, l. 236). Ne sont **jamais** posés : `PREREG_ABSENT`, `T06_EPUISEMENT_SIMULE_S` (refusé en course, l. 198), `T06_TESTS_ARGS`, `T06_PREREG`, `T06_DEPOT`, `T06_IMAGE`, `T06_REGISTRE_GO` (en course, le registre lu est celui du clone de `main`, l. 84), `BRAS_B`.
- Attendu : `vastai --version` → 1.8.3 ; `HF_TOKEN présente` ; au moins un des deux jetons GitHub présent ; `VAST_API_KEY` présente ou `vastai` configuré par son fichier (la recherche du § 4.8 le prouve). Sinon : arrêt, compte rendu.

### 4.1 Deux clones de la seule branche `main`, faits comme celui de l'amorce, sous exclusions

```bash
# (A)
printf '%s\n' '/.claude/' '/src/' '/tests/' '/scripts/' '/pyproject.toml' '/requirements-*.txt' '/prereg/' '/donnees/' '/diag/' '/runs/' '/traces/' '/registres/*.md' '/docs/*.md' '/docs/*.txt' '/docs/*.sha256' '/docs/notes/' '/docs/procedures/' '/docs/decisions/' '/docs/verdicts/' '/docs/etat-de-l-art/' '/docs/sources/invites-2606.07054-v1/' '/docs/sources/invites-2606.08892-v1/' '/docs/sources/cartes-modeles-20261006/' '/docs/sources/donnees-T0.7/' '/brouillons/ordres-t06-e2-e3-v2/' '/brouillons/ordres-t06-e2-e3-v3/' '/brouillons/ordres-t06-e2-e3-v4/' '/brouillons/ordres-t06-e2-e3-v5/' '!/docs/notes/bras-attaque/' '!/donnees/bras-attaque*' '!/donnees/mode-tenu-a-l-ecart*' '!/diag/*/lecture-sondes-t06.json*' '!/scripts/extraire_mesures_epreuve_t06_v1.py' '!/registres/index-bras-attaque*' > "$W/motifs.txt"
for X in "$M" "$AM"; do timeout -k 10 900 git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$X" && git -C "$X" sparse-checkout init --no-cone && git -C "$X" sparse-checkout set --no-cone --stdin < "$W/motifs.txt" || echo "ARRÊT : clone $X"; done
git -C "$M" checkout -q main; timeout -k 10 900 git -C "$AM" checkout -q "$S"
git -C "$M" rev-parse HEAD origin/main; git -C "$AM" rev-parse HEAD
test -f "$M/scripts/lancer_t06_v13.sh" && test -f "$AM/prereg/T0.6-organismes-v0-v1.md" && echo "extractions présentes"
git -C "$M" merge-base --is-ancestor <<COMMIT_MAIN_REMISE>> HEAD && echo "remise : ancêtre de la tête clonée"
```

- Les 28 premiers motifs sont la liste `CHEMINS_CLONAGE` de l'amorce v11 (l. 255 à 282), dans le même ordre. **Écarts déclarés à l'amorce** : `--single-branch --branch main` (l'amorce clone toutes les branches, l. 284 ; la fille n'en veut aucune sous embargo ; S et `1609a4bf` sont des ancêtres de `main`) ; six exclusions (§ 2). Aucune ne touche l'arbre gelé (`exiger_code_cite` compare des commits, non l'arbre extrait) ni ce que lit le lanceur côté session.
- Attendu : la tête de `$M` égale `origin/main` (deux fois la même ligne) ; la tête de `$AM` est S ; « extractions présentes » ; « remise : ancêtre de la tête clonée ». Puis l'ordre lui-même, lu dans `$M` : `sha256sum -c` de son compagnon conforme, empreinte égale à celle du message de remise.

### 4.2 Chaîne et commit de scellement (préalables P1 et P8)

```bash
# (A)
cd "$M"
git diff --quiet "$C" HEAD -- scripts/lancer_t06_v13.sh scripts/amorce_instance_t06_v11.sh src/controle_ia/t06/; echo "chaîne côté session = 1609a4bf : code $?"
git diff --name-only "$C" HEAD -- .claude/
sha256sum scripts/lancer_t06_v13.sh scripts/amorce_instance_t06_v11.sh src/controle_ia/t06/session.py src/controle_ia/t06/session_v2.py src/controle_ia/t06/session_v3.py src/controle_ia/t06/session_v12.py src/controle_ia/t06/lanceur_v6.py src/controle_ia/t06/configuration_v6.py scripts/tests-cibles-t06-v3.txt scripts/tests-exclus-t06-v3.txt src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py
git merge-base --is-ancestor "$C" "$S" && git merge-base --is-ancestor "$S" origin/main && echo "lignée 1609a4bf → S → origin/main"
[ "$(git log --diff-filter=A -1 --format=%H -- prereg/T0.6-organismes-v0-v1.md.sha256)" = "$S" ] && echo "commit_s = S"
git show "$S:prereg/T0.6-organismes-v0-v1.md" | sha256sum; git show "$S:prereg/T0.6-organismes-config-7b-v1.json" | sha256sum
```

Attendu : code 0 ; une seule ligne `.claude/hooks/garde_calcul.py` (sur `main`, la garde de calcul porte une troisième règle, R-1984, sans effet sur une commande de création ; c'est elle que le lanceur rejoue côté session, l. 236 ; l'instance, elle, joue l'arbre de S) ; les onze empreintes du § 1 ; « lignée … » ; « commit_s = S » ; `ef31feff…` puis `b7a5c1ba…`. Tout écart : arrêt, compte rendu (aucune substitution de fichier par la fille).

### 4.3 GO, T0.7, engagement, bras B (préalables P2, P3, P6, P7)

```bash
# (A)
cd "$M"; date -u +%FT%TZ
for g in GO-2026-11-02-28 GO-2026-11-07-02 GO-2026-11-07-04 GO-2026-11-10-01; do printf '%s : %s ligne(s)\n' "$g" "$(grep -c "^| $g |" registres/go.md)"; done
grep -E '^\| GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2} \| [0-9-]+ \| révocation \|' registres/go.md | grep -cE 'GO-2026-11-02-28|GO-2026-11-07-02|GO-2026-11-07-04|GO-2026-11-10-01'
grep -c '^| SCELLEMENT-T07 |' registres/scellements-v1.md
L7=$(grep '^| SCELLEMENT-T07 |' registres/scellements-v1.md); P7=$(printf '%s\n' "$L7" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); H7=$(printf '%s\n' "$L7" | awk -F'|' '{gsub(/ /,"",$5); print $5}')
[ "$L7" = '<<LIGNE_SCELLEMENT_T07>>' ] && echo "ligne SCELLEMENT-T07 = celle de la remise"
[ "$(git show "HEAD:$P7" | sha256sum | cut -d' ' -f1)" = "$H7" ] && [ "$(git show "HEAD:$P7.sha256" | cut -d' ' -f1)" = "$H7" ] && echo "T0.7 scellé : $P7 $H7"
git show HEAD:registres/depenses.md | grep -F 'GO-2026-11-02-28' | grep -F 'course de confirmation 7b' | grep -ci 'engagement'
grep -c '^| <<LIGNE_REGISTRE_BRAS_B>> |' registres/decisions.md
```

Attendu : une ligne pour chacun des quatre GO ; 0 révocation ; une ligne `SCELLEMENT-T07`, égale à celle de la remise, fichier et compagnon à son empreinte ; au moins une ligne d'engagement ; la ligne du registre de la mère sur le bras B présente une fois. Sinon : aucune création (et la règle du 13 novembre à 12:00 UTC pour T0.7, préalable P2).

### 4.4 Contrôles en ligne (`controles`, sans dépense)

```bash
# (A)
bash "$W/v13.sh" "$B" controles "$D" > "$W/controles-$(basename "$D").txt" 2>&1; echo "code $?"; cat "$W/controles-$(basename "$D").txt"
for k in commit prereg config branche amorce go; do printf '%s : %s\n' "$k" "$(champ "$k")"; done; sha256sum "$D/config.json"
```

- Ce que fait `controles` (lanceur l. 119 à 146) : GO-2026-11-02-28 au registre du clone de `main` ; 3 Go libres ; S par `commit_s` ; `git fetch origin main` ; S ancêtre d'`origin/main` ; huit citations du texte de S, une fois chacune ; fichiers cités et sceaux présents à S ; calendrier de la configuration contre le registre ; amorce v11 de S citée par son empreinte ; jetons présents (jamais affichés) ; écrit `lancement.txt`.
- Attendu, code 0 : première ligne « `GO-2026-11-02-28 conforme (plafond 200 USD, 2026-11-02 → 2026-11-16)` » ; dernière ligne « `CONTRÔLES CONFORMES : S=935262b17ca95894a882b02f1526ee39d1738652 ; amorce v11 43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859 ; GO GO-2026-11-02-28 ; fin_go_utc_s=1794873600 dernier_jour_creation=2026-11-15 echeance_go=2026-11-16` » ; champs : `commit` = S, `prereg` = `prereg/T0.6-organismes-v0-v1.md`, `config` = `prereg/T0.6-organismes-config-7b-v1.json`, `branche` = `calcul/t06-confirmation-7b-v1`, `amorce` = `43d85659…`, `go` = `GO-2026-11-02-28` ; `config.json` à `b7a5c1ba…`. Tout autre code ou valeur : arrêt, compte rendu ; une reprise se fait dans un dossier neuf (`c7b-1-r2`).

### 4.5 Branche de sortie absente du dépôt distant

```bash
# (A)
git -C "$M" ls-remote --exit-code origin "refs/heads/$B" > /dev/null; echo "code $?"
```

Attendu : **code 2** (absente). Code 0 : la branche existe (l'amorce refuserait, l. 404 à 409) : nom suivant (`-v2`), contrôles rejoués dans un dossier neuf. Autre code : arrêt, compte rendu.

### 4.6 Gardes rejouées dans le clone fait comme celui de l'amorce (cas sain), puis sur `main` (artefact)

```bash
# (A)
G='import json, sys
from pathlib import Path
sys.path.insert(0, "src")
from controle_ia.t06.configuration_v6 import exiger_config_t06_v6
from controle_ia.t06.lanceur import charger_taches_t06, exiger_citations_t06
from controle_ia.harnais.validation_reelle import exiger_code_importe_sous, exiger_code_cite
from controle_ia.prereg import exiger_prereg_scelle
from controle_ia.scellement import verifier
r = Path(".")
p = Path("prereg/T0.6-organismes-v0-v1.md")
c = "prereg/T0.6-organismes-config-7b-v1.json"
print("configuration", verifier(c))
config = json.loads(Path(c).read_text(encoding="utf-8"))
exiger_config_t06_v6(config, r / "registres" / "go.md")
print("exiger_config_t06_v6 passe")
t = charger_taches_t06(config, r)
print("taches", t["sha_evaluation"], t["sha_distillation"])
exiger_code_importe_sous(r)
print("exiger_code_importe_sous passe")
print("exiger_citations_t06", exiger_citations_t06(p, config, t["sha_evaluation"]))
print("exiger_prereg_scelle", exiger_prereg_scelle(p))
print("exiger_code_cite", exiger_code_cite(r, p))'
cd "$AM" && [ "$(git rev-parse HEAD)" = "$S" ] && "$PY" -I -B -c "$G"; echo "cas sain (tête S) : code $?"
cd "$M" && "$PY" -I -B -c "$G" 2>&1 | tail -n 3; echo "artefact (tête de main) : code ${PIPESTATUS[0]}"
```

- Ce sont, dans l'ordre de `lanceur_v6.executer` (l. 164 à 180) et de `manifeste.creer_manifeste` (l. 89 à 96), les gardes que l'instance jouera avant le manifeste ; c'est le pas « gardes rejouées sur S réel, dans un clone fait comme celui de l'amorce » du texte (plan de la confirmation, point 3, (5) ; R-2082, « Reste avant la création ») ; la mère les a déjà jouées sur S réel dans un clone local (R-2082) : ici, le clone vient du dépôt distant, comme celui de l'instance.
- **Attendu, cas sain** (code 0) : `configuration b7a5c1ba…` ; `exiger_config_t06_v6 passe` ; `taches 76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e 8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` ; `exiger_code_importe_sous passe` ; `exiger_citations_t06 31538212097275005629337336542801867913` ; `exiger_prereg_scelle ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` ; `exiger_code_cite 1609a4bf2c1572f72bb8542d81d963ac6a8481c4`.
- **Attendu, artefact** (R5 : la garde doit refuser un arbre gelé qui n'est pas celui du commit cité) : les mêmes lignes jusqu'à `exiger_prereg_scelle`, puis le refus « `arbre gelé (code, tests, scripts, dépendances, configuration) modifié depuis le commit cité 1609a4bf2c15` », code 1 (essai du rédacteur sur l'arbre de `main`, sans écriture : ce refus est observé). Un cas sain refusé, ou un artefact accepté : arrêt, compte rendu.

### 4.7 Inventaire avant la création (champs filtrés)

```bash
timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances",d) if isinstance(d,dict) else d; [print(i.get("id"),i.get("label"),i.get("actual_status"),i.get("dph_total"),i.get("duration")) for i in (d or [])]'
```

Commande exacte de l'ordre de 7a (§ 5, étape 6) : jamais le brut, qui imprime des variables secrètes. Aucune étiquette ne commence par `t06-v2` (sinon : arrêt, compte rendu). Les instances que la fille n'a pas créées (dont 58936096, 58936099, 58936100, intouchables par consigne de Lazar) ne sont **jamais** touchées.

### 4.8 Création sur l'A100 : fenêtre de GO-2026-11-07-02

Chaque recherche est un appel de `creation auto course`, **qui ne loue rien** (l. 178 à 240 : il choisit l'offre dans la recherche filtrée, relit l'inventaire, calcule l'heure où la dépense cumulée atteindrait 200 USD, rejoue la garde de calcul et **imprime** la commande de création) :

```bash
# (A)
n=1   # numéro de la recherche, de 1 à 12 ; jamais réutilisé (R12)
date -u +%FT%TZ; bash "$W/v13.sh" "$B" creation auto course "$ANT0" "$D" > "$D/creation-sortie-$n.txt" 2>&1; echo "code $?"; head -n 1 "$D/creation-sortie-$n.txt" | cut -c1-300
```

- **Code 0** : une A100 conforme est retenue (ligne « `OFFRE CONFORME : id=… machine=… rang=… prix_carte=… prix_stockage=… telechargement_forfait=… ; aucune instance du programme … ; cumulee=… epuisement_utc_s=…` ») : § 4.9 sans attendre (une offre change vite).
- **Code 3 avec « aucune offre conforme »** dans la première ligne : recherche vide, rien n'est créé ni compté ; la fille relance **toutes les 15 minutes, 12 recherches au plus (3 heures, 0 USD)**, chacune dans un fichier neuf, heure et code au journal. Au bout de la douzième sans A100 conforme : **§ 5 (H200, mot de Lazar)**.
- **Tout autre code 3** (instance du programme sur le compte, dépense déjà au plafond, trois essais faits, calendrier refusé) et **tout code 2** : ce n'est pas une absence d'offre : aucune bascule, arrêt, compte rendu à la mère (même règle que `scripts/fenetre_carte_t06_v1.sh`, l. 19 à 23, que cet ordre ne lance pas : il dépasserait la durée d'une commande de fond de l'outil).
- La dépense antérieure passée au lanceur est `ANT0` (relevée par la mère, § 14) pour la première instance ; **jamais 0 pour une seconde instance** (§ 5).

### 4.9 Contrôle de la commande imprimée, avant toute exécution

```bash
# (A)
n=<numéro de la recherche retenue>; F="$D/creation-sortie-$n.txt"
wc -l < "$F"; sed -n 2p "$F" | grep -c '^COMMANDE DE CRÉATION'
CMD=$(tail -n 1 "$F")
printf '%s\n' "$CMD" | grep -cE '^GO_ID=GO-2026-11-02-28 timeout -k 10 300 vastai create instance [0-9]+ --raw --image python:3\.11-bookworm --disk 150 --cancel-unavail --label t06-v2 --env "'
ENVP=$(printf '%s\n' "$CMD" | sed -n 's/.* --env "\([^"]*\)" --entrypoint bash --args -c .*/\1/p')
printf '%s\n' "$ENVP" | grep -cxE -- "-e COMMIT=$S -e PREREG=prereg/T0\.6-organismes-v0-v1\.md -e BRANCHE=$B -e DEPOT_URL=https://github\.com/lciric/controle-ia-travail\.git -e ECHEANCE_UTC_S=1794873600 -e FIN_GO_UTC_S=1794873600 -e DEPENSE_EPUISEE_UTC_S=[0-9]+ -e HF_TOKEN=\\\$HF_TOKEN -e GH_TOKEN=\\\$CONTROLE_IA_GITHUB_TOKEN(_2)?"
[ "$(printf '%s\n' "$ENVP" | sed -n 's/.*DEPENSE_EPUISEE_UTC_S=\([0-9]*\) .*/\1/p')" = "$(champ epuisement)" ] && echo "épuisement = lancement.txt"
printf '%s\n' "$CMD" | grep -cE 'REQUESTS_CA_BUNDLE|SSL_CERT_FILE|HTTPS_PROXY|NO_PROXY|VAST_API_KEY|EPREUVE_GO_ID|PREREG_ABSENT|TESTS_ATTENDUS|TESTS_ARGS|BRAS_B'
printf '%s\n' "$CMD" | sed -n 's#.* --args -c "echo \([A-Za-z0-9+/=]*\) | base64 -d > /root/amorce\.sh && bash /root/amorce\.sh" > .*#\1#p' | base64 -d | sha256sum
python3 -I -c 'import os,sys; t=open(sys.argv[1],encoding="utf-8",errors="replace").read(); print(sum(1 for k in ("VAST_API_KEY","HF_TOKEN","CONTROLE_IA_GITHUB_TOKEN","CONTROLE_IA_GITHUB_TOKEN_2","GH_TOKEN") if len(os.environ.get(k,""))>=8 and os.environ[k] in t))' "$F"
for k in offre carte prix_carte prix_stockage telechargement_forfait anterieure echeance epuisement essai_creation rang; do printf '%s : %s\n' "$k" "$(champ "$k")"; done
```

Attendu : `3` lignes ; `1` ; `1` (tête de la commande : GO, outil, image, disque 150 Go, étiquette `t06-v2`) ; `1` (les **neuf** variables passées à l'instance, et elles seules, dans l'ordre du lanceur l. 235 : commit S, texte, branche de sortie, **`DEPOT_URL` du dépôt de travail**, échéance et fin du GO au 2026-11-17T00:00:00Z, heure d'épuisement des 200 USD, deux jetons **par leur nom**) ; « épuisement = lancement.txt » ; `0` (aucune variable du mandataire, aucune clé de l'outil, aucune variable d'épreuve, aucun débrayage : la base 64 ne contient jamais le caractère `_`, ce comptage sur la commande entière est donc sûr) ; l'empreinte de l'amorce `43d85659…` ; garde des secrets `0` ; `carte course` (ou `relance` au § 5), `prix_carte` ≤ 1,30 (≤ 4,70 en relance), `prix_stockage` ≤ 0,08, `anterieure` = `ANT0`, `echeance` 1794873600, `essai_creation` ≤ 3. Un seul écart : rien n'est exécuté ; compte rendu à la mère.

### 4.10 Exécution, une fois

```bash
# (A)
n=<même numéro>; GO_ID=GO-2026-11-02-28 bash -c "$(tail -n 1 "$D/creation-sortie-$n.txt")"; echo "code $?"
```

- Forme d'exécution de 7a (R-1914 : « `GO_ID=… bash -c "<ligne 3 de la sortie du lanceur>"`, accepté par la garde de calcul ») : la commande exécutée est, octet pour octet, celle que le lanceur a imprimée **après** avoir rejoué sur son texte exact la garde de calcul du clone de `main` (l. 236) ; la recopier à la main (environ 74 000 caractères, l'amorce en base 64) risquerait de l'altérer. Les jetons y sont des références (`$HF_TOKEN`, `$CONTROLE_IA_GITHUB_TOKEN_2`) que le shell développe sans les afficher ; la sortie de `vastai` va dans `creation-brute.json`, que `apres-creation` lit puis efface (l. 241 à 259).
- **Code 0**, « `CRÉÉE : instance <ID> (création <secondes> ; sortie de vastai non affichée) ; …` » : l'identifiant `<ID>` et l'heure sont consignés ; § 4.11.
- **Code 5**, « `OFFRE REFUSÉE À LA CRÉATION (retirée ?)` » : aucune instance du programme ; la machine est exclue ; la fille rejoue **aussitôt** le § 4.8 (rang suivant, fichier de sortie neuf), puis § 4.9 et § 4.10 ; trois essais au plus par dossier (l. 212).
- **Code 4**, « `CRÉATION INCERTAINE` » : **aucune seconde création** ; inventaire filtré (§ 4.7) ; compte rendu à la mère.

### 4.11 Surveillance, heure des 60 USD

```bash
# (A)
ID=<identifiant créé>
python3 -I -B -c "import sys; sys.path.insert(0, '$M/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))" depense 60 "$(champ prix_carte)" "$(champ prix_stockage)" "$(champ creation)" "$(champ anterieure)" "$(champ telechargement_forfait)"
bash -c 'echo "$(date -u +%FT%TZ) PID $$" >> "$1/pids-surveillance.txt"; exec bash "$2/v13.sh" "$3" surveillance "$4" "$1"' _ "$D" "$W" "$B" "$ID" >> "$D/surveillance-sortie.txt" 2>&1
```

- La première commande (code de la chaîne, `session_v3 depense`, l. 83 à 110, sans réseau) écrit `… epuisement_utc_s=<H60> …` : **H60**, l'heure où la dépense cumulée de la course (antérieure, plus forfait de téléchargement, plus heures × (carte + stockage) au prix de l'offre) atteint 60 USD ; la fille l'écrit au journal en clair (`date -u -d @<H60> +%FT%TZ`). Si l'instance tourne encore à H60 : **compte rendu à Lazar** (§ 6), une fois, sans aucun arrêt.
- La seconde se lance **en tâche de fond** par l'outil de la fille (`INTERVALLE=60`, posé par l'enveloppe) ; `exec` garde le PID écrit dans `pids-surveillance.txt`, seul moyen de l'arrêter (R10). L'outil coupe une commande de fond au plus tard au bout de 2 heures : dès qu'elle s'arrête **sans** `ARRET` ni `FIN`, la fille la relance **à l'identique** (même `<ID>`, même dossier) et consigne le PID neuf. Ce que la surveillance fait (l. 260 à 351) : journal entier de l'instance masqué et recopié dans `journal-instance.txt`, lignes `AMORCE` et `PROGRES` dans `progres.txt`, présence de l'instance, garde de dépense à 200 USD ; décisions dans `surveillance.txt`.
- **Durées attendues** (lecture A de 7a, R-2040, heures de 7a, exploratoires, servant de repère seulement) : amorce ≈ 2 min ; suite ciblée ≈ 35 min (« `2022 passed …` » attendu dans le journal ; un autre compte arrête l'instance, amorce l. 492 à 494) ; données de distillation ≈ 3 h 51 ; entraînement des deux adaptateurs ≈ 28 min (un avertissement d'allocation de mémoire de la carte peut paraître au début, **sans arrêt** : 7a l'a eu ; c'est une réserve de lecture, non un arrêt) ; épisodes ≈ 3 h à dose 0 puis ≈ 45 min par état dosé (cinq) ; test croisé ≈ 2 min ; couples descriptifs ≈ 1 h 44 ; poussées ≈ 1 min ; puis le bras B (§ 7, borne 40 min). Instance ≈ 13,6 h hors création et bras B. **Aucun couperet de temps** : un run lent mais vivant n'est jamais arrêté ; 2 heures sans ligne `PROGRES` : `ALERTE` de la surveillance, compte rendu à la mère, **sans arrêt**.

### 4.12 Fin, arrêt par l'identifiant, rapatriement sans les contenus, compagnons

À la sortie de la surveillance (`FIN …` code 0, ou `ARRET …` code 3, ou `REFUS …` code 4), la fille relève la dernière ligne `AMORCE … fin, code N` de `journal-instance.txt`, puis :

```bash
# (A)
ID=<identifiant créé>; timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances",d) if isinstance(d,dict) else d; [print(i.get("id"),i.get("label"),i.get("actual_status"),i.get("dph_total"),i.get("duration")) for i in (d or [])]'
timeout -k 5 120 vastai stop instance "$ID"; echo "code $?"   # seulement si l'instance n'est pas déjà arrêtée ; jamais sur un autre identifiant
git -C "$M" fetch -q --filter=blob:none origin "refs/heads/$B:refs/remotes/origin/$B"; echo "code $?"
R=refs/remotes/origin/$B; X=':(glob,exclude)diag/*/lecture-sondes-t06.json*'; git -C "$M" rev-parse "$R"; git -C "$M" log --format='%H %cI %s' "$S..$R"
git -C "$M" diff --name-status --no-renames "$S" "$R" -- . "$X" | grep -vc '^A'
git -C "$M" diff --name-only --no-renames --diff-filter=A "$S" "$R" -- . "$X" > "$W/fichiers-ajoutes-$(basename "$D").txt"; wc -l < "$W/fichiers-ajoutes-$(basename "$D").txt"
RUN=$(sed -n 's|^runs/\([0-9]\{8\}-[0-9]\{6\}-t06-reel\)/manifeste\.json$|\1|p' "$W/fichiers-ajoutes-$(basename "$D").txt"); echo "run : $RUN"
grep -E "^(runs|diag)/$RUN/" "$W/fichiers-ajoutes-$(basename "$D").txt" | grep -v '\.sha256$' | while IFS= read -r f; do a=$(git -C "$M" show "$R:$f" | sha256sum | cut -d' ' -f1); b=$(git -C "$M" show "$R:$f.sha256" | cut -d' ' -f1); [ "$a" = "$b" ] && echo "OK $f $a" || echo "ÉCART $f"; done
for d in $(grep -oE '^traces/(t06|consignation)-[^/]+/' "$W/fichiers-ajoutes-$(basename "$D").txt" | sort -u); do git -C "$M" show "$R:${d}empreintes.sha256" | while read -r h nom; do [ "$(git -C "$M" show "$R:$d$nom" | sha256sum | cut -d' ' -f1)" = "$h" ] && echo "OK $d$nom" || echo "ÉCART $d$nom"; done; done
git -C "$M" show "$R:runs/$RUN/manifeste.json" | python3 -I -c 'import json,sys; m=json.load(sys.stdin); print(m["run_id"], m["commit"], m["decisif"], m["depot_propre"], (m["preenregistrement"] or {}).get("sha256"), m["config_sha256"], m["reserves"], m["commande"])'
```

- **Arrêt de l'instance** : à `FIN`, l'amorce a déjà demandé l'état « stopped » (disque gardé, amorce l. 151 à 164) ; la fille exécute le `stop` que la surveillance imprime **si** l'inventaire ne montre pas l'instance arrêtée ; à `ARRET mort`, `ARRET depense`, `ARRET garde`, de même ; à `ARRET inventaire`, inventaire filtré d'abord ; à `REFUS`, la minuterie de l'instance la détruit d'elle-même après 180 s (amorce l. 141 à 146) : inventaire filtré, puis compte rendu.
- **Rapatriement par refspec explicite, sans les contenus de fichiers** (`--filter=blob:none`) : seuls entrent sur le disque de la fille les fichiers que les commandes ci-dessus extraient un à un (`git show`) : manifeste, résultats de `diag/<run>/` **hors sondes**, traces de T0.6. Le résultat des sondes, les données de `donnees/<run>/` et les sorties du bras B restent sur le dépôt distant. Jamais de `verifier-arbre` sur la branche (il ouvrirait tout).
- **Attendu** (fin normale) : commits de l'instance « `T0.6 (reel), run <run> : résultats et données légères` », « `… sous-ensemble d'activations en morceaux …` », « `T0.6 : traces de l'instance (fin)` », puis, s'il a tourné, « `T0.6 : bras B de l'audit de fuite (annexe, code N)` » ; `0` changement autre qu'un ajout ; un identifiant `AAAAMMJJ-HHMMSS-t06-reel` ; `OK` pour `runs/<run>/manifeste.json`, `diag/<run>/distillation-t06.json`, `episodes-t06.json`, `lecture-cout-t06.json`, `resume.json` (hachés, **jamais affichés**) ; `OK` pour chaque fichier de chaque `traces/t06-…/` et `traces/consignation-…/` ; manifeste : `<run> 935262b17ca95894a882b02f1526ee39d1738652 True True ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169 ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d [] python -m controle_ia.t06.lanceur_v6`. Tout `ÉCART` : compte rendu à la mère, rien d'autre.
- **En cas d'arrêt consigné** (`diag/<run>/arret.json` dans la liste), la fille lit **ses seuls champs `etape` et `motif`**, jamais `partiel` :

```bash
# (A)
R=refs/remotes/origin/$B; RUN=<run>; git -C "$M" show "$R:diag/$RUN/arret.json" | python3 -I -c 'import json,sys; r=json.load(sys.stdin)["resultat"]; print("etape :", r.get("etape")); print("motif :", str(r.get("motif"))[:300])'
```

- Lignes du journal de la chaîne relevées pour le compte rendu (dans `traces/t06-…/journal.txt` et `$D/journal-instance.txt`) : `tests : …` (dernière ligne de la suite ciblée), `run : …`, `run terminé : …`, `branche … poussée …`, les lignes `PROGRES … etape=…` (durées), `ERREUR DE CHAÎNE`, `FIN ANORMALE`, `RUN MORT`, `bras B : …` (début, code et durée : ces dernières ne sont que dans `journal-instance.txt`, le bras B jouant après les traces de T0.6).

### 4.13 Destruction par l'identifiant, inventaire final

```bash
# (A)
ID=<identifiant créé>; timeout -k 5 120 vastai destroy instance "$ID" -y; echo "code $?"
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>&1); c=$?; [ "$out" = '{"instances": null}' ] && echo "absente (texte exact), code $c" || echo "texte autre (non affiché), code $c"
timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances",d) if isinstance(d,dict) else d; [print(i.get("id"),i.get("label"),i.get("actual_status"),i.get("dph_total"),i.get("duration")) for i in (d or [])]'
```

- Du **seul identifiant créé**, après le rapatriement vérifié (§ 4.12), forme de R-2039 (`-y`). **Quand** : fin normale : l'instance arrêtée garde son disque jusqu'au mot de la mère (verdict de la table A, ou décision de la mère), et **au plus tard** à la première de ces heures : 72 heures après l'arrêt (borne du poste « disque » du devis) ; **2026-11-16T23:00Z** (« Liste d'arrêt » : aucune dépense n'est couverte au-delà de la fin du 16 novembre ; le texte dit les 72 heures « une borne, non un droit au-delà du 16 novembre »). Une conservation plus longue (par exemple pour T0.7 sur la même machine, GO-2026-11-10-01) n'est possible que sur un addendum de la mère qui porte le mot de Lazar (§ 13, point ouvert). Arrêt consigné ou refus : après le rapatriement, sur le mot de la mère, et dans tous les cas avant toute seconde création (le lanceur refuse une création tant qu'une instance `t06-v2…` est sur le compte).
- Le texte rendu par `show instance` n'est jamais affiché : seul « absente (texte exact) » ou le code est écrit.

## 5. Carte H200 NVL : seulement après un mot de Lazar dans la session de la fille

La règle de la fenêtre (GO-2026-11-07-02, texte, « Plan d'analyse », point 9) et la relance de DT-6 (erreur de mémoire à la distillation sur l'A100 : « relance sur H200 sous ce texte, déclarée, aucun résultat n'ayant été lu ») restent écrites telles quelles ; R-2077 y ajoute une condition, articulée par la contre-lecture 6 (couple C6-3, en-tête du texte) : **`creation auto relance` n'est jouée qu'après un mot de Lazar**, au bout de la fenêtre comme après une erreur de mémoire, et **l'attente de ce mot est prévue**.

1. **Quand la question se pose** : (a) douze recherches A100 vides (§ 4.8) ; ou (b) arrêt consigné de la première instance dont `arret.json` dit `etape` « données de distillation » ou « distillation » et dont le `motif` est une erreur de mémoire de la carte (par exemple « out of memory », « OutOfMemoryError ») ; un arrêt d'une autre nature, ou une erreur de mémoire pendant les épisodes, n'est **pas** ce cas : compte rendu à la mère, nœud.
2. **Message de la fille à Lazar**, dans sa session (et copie à la mère), au format de décision : « **Décision** : créer 7b sur la H200 NVL (≤ 4,70 USD/h, ≥ 140 Go de mémoire de carte, même filtre) maintenant ? **Enjeu** : [fenêtre de 12 recherches sans A100 conforme, de HH:MMZ à HH:MMZ | erreur de mémoire à la distillation sur l'A100 `<ID>`, détruite, dépense de cette tentative ≈ X USD]. **Options** : (a) H200 maintenant — devis du texte : ≈ 72 USD aux durées de 7a, ≈ 136 au débit moitié, sous le plafond de 200, dépense antérieure comprise ; (b) nouvelle fenêtre A100 plus tard [heure], dans la limite du calendrier (création sans nœud au plus tard 2026-11-15T20:48Z) ; (c) rien, nœud reporté. **Nœud de dépense : aucun défaut.** » La fille ne recommande que ce que les faits appuient et le dit.
3. **Attente** : la fille ne crée rien ; elle consigne l'heure du message ; tant que l'instance A100 éventuelle n'est pas détruite, elle garde la surveillance et le § 4.13. Au-delà de 2026-11-15T20:48Z, un mot de Lazar doit dire expressément qu'il accepte la création tardive (L11) ; le 16 novembre, plus rien n'est possible sous cette chaîne.
4. **Sur le mot de Lazar** (verbatim et heure au journal) : cas (a), même dossier `D` (aucun essai n'a été compté), dépense antérieure `ANT0` ; cas (b), **instance A100 détruite d'abord** (§ 4.13), dossier neuf `$W/c7b-2`, branche neuve `calcul/t06-confirmation-7b-v2` (§ 4.5 rejoué), `controles` rejoué dans ce dossier (§ 4.4, avec `B` et `D` neufs dans (A)), et dépense antérieure **ANT1** = la plus grande de la facture relevée de la tentative A100 (si connue) et du cumul calculé par le code de la chaîne à l'heure de sa destruction :

```bash
# (A) avec D et B de la première instance
python3 -I -B -c "import sys; sys.path.insert(0, '$M/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))" depense 200 "$(champ prix_carte)" "$(champ prix_stockage)" "$(champ creation)" "$(champ anterieure)" "$(champ telechargement_forfait)" <heure de la destruction en secondes>
```

   Puis : `bash "$W/v13.sh" "$B" creation auto relance "<ANT0 ou ANT1>" "$D" > "$D/creation-sortie-$n.txt" 2>&1` (fichier neuf), § 4.9 (avec `carte relance`, `prix_carte` ≤ 4,70, la branche en vigueur dans l'expression attendue), § 4.10, § 4.11 à § 4.13. **Sans offre H200 conforme** (code 3 « aucune offre conforme ») : nœud (texte, point 9) : compte rendu à Lazar et à la mère, aucune autre recherche sans leur mot.
5. **Relance sur l'A100 après une autre erreur de chaîne** (ligne A1 du texte : avant tout épisode d'évaluation, code cité inchangé) : seulement sur un addendum de la mère qui dit la panne consignée et réparée ; même mécanique qu'au point 4 (cas (b)), carte `course`.

## 6. Dépense

- **Ligne d'engagement** au registre des dépenses, écrite et poussée par la mère **avant** la création (préalable P6), texte proposé par le texte scellé (« Devis », révision 3) : « engagement : T0.6 organisme (ii), dose–réponse et test croisé, course de confirmation 7b (GO-2026-11-02-28, plafond 200 USD) : lanceur `scripts/lancer_t06_v13.sh` (empreintes : en-tête du préenregistrement scellé), commit du code cité `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` (l'instance clone le commit de scellement S, de même arbre gelé) ; une carte A100 SXM4 80 Go ≤ 1,30 USD de l'heure (DT-6 (a)), disque ≥ 150 Go ; attendu ≈ 16 à 26 USD, pire cas ≈ 151 USD (H200) ; dépense antérieure sous ce GO relevée au registre ; crédit Vast.ai relu à la création (recharge automatique, R-283) ». La chaîne v13 ne lit pas le crédit ; cet ordre n'ajoute aucune commande de l'outil pour le lire (recharge automatique, R-283).
- **Compte rendu à Lazar à 60 USD** de dépense cumulée (R-2077), dans la session de la fille, une fois, à H60 (§ 4.11) ou dès qu'un relevé l'établit : « Dépense cumulée de 7b ≈ 60 USD atteinte à HH:MMZ (carte A100 | H200, instance `<ID>`, en marche ; dernière étape `PROGRES` : … ; tentatives antérieures : … USD) ; aucune action ; arrêt par la chaîne à 200 USD. » Copie à la mère. **Aucun arrêt** à ce seuil.
- **180 USD cumulés** : toute relance ou seconde instance est un nœud de Lazar avant dépense (texte, « Devis »).
- **200 USD cumulés** (calcul, disque, téléchargement, toutes tentatives et relances, H200 comprise) : arrêt par la chaîne : la surveillance imprime `ARRET depense` et la commande d'arrêt par l'identifiant ; la minuterie de l'instance demande d'elle-même l'état « stopped » à l'heure d'épuisement calculée à la création (`DEPENSE_EPUISEE_UTC_S`, amorce l. 101 à 110) ; résultats partiels consignés comme tels ; puis § 4.12 et § 4.13 ; aucune relance.
- **Arrêts et destruction par l'identifiant d'instance (R10), jamais par motif de ligne de commande** ; la surveillance s'arrête par son PID (`kill <PID>` du fichier `pids-surveillance.txt`), jamais par `pkill` ni `killall` (la garde de calcul les bloque). **Inventaire filtré** avant la création et après la destruction (§ 4.7, § 4.13).
- **Dépense relevée au compte rendu** : prix de la carte, du stockage et forfait de téléchargement lus dans `lancement.txt` ; heures de la création à l'arrêt et de l'arrêt à la destruction ; cumul par `session_v3 depense 200 …` à l'heure de l'arrêt, plus le stockage de l'instance arrêtée (heures × `prix_stockage`) ; facture si elle est connue (elle fait foi).

## 7. Bras B de l'audit de fuite (GO-2026-11-07-04) : joué par la chaîne, sur la même machine

- **Il est joué** : en course, l'amorce v11 lance `bras_b()` après la poussée finale de T0.6 et avant l'arrêt de l'instance (l. 553), parce que le mode est réel, qu'aucune ligne d'épreuve n'est passée (`EPREUVE_GO_ID` vide) et que `BRAS_B` n'est pas posé (défaut 1) ; sa configuration `docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json` (`4fb0da20…`), le module `bras_b_v4` (`317a7ea5…`) et le texte de l'audit `prereg/audit-fuite-r1-v4-v1.md` (`910a53dc…`) sont dans l'arbre de S (l. 418 à 442). Le lanceur v13 en course ne passe aucune variable qui le débraye (l. 234–235), et cet ordre interdit de changer la commande imprimée : **il n'est pas débrayable par la fille**.
- **Ce qu'il fait** : annexe régie par le texte de l'audit (point 7), **non par T0.6** : il ne change ni les entrées, ni les sorties, ni les règles de lecture de T0.6 ; jamais bloquant (un échec n'écrit qu'une ligne de journal) ; borne de 2 400 s (`BRAS_B_DUREE_MAX_S`) ; environ 20 minutes de carte estimées ; ses sorties (`diag/bras-b-…`, `runs/bras-b-…`, `traces/bras-b-…`) sont committées à part (« `T0.6 : bras B de l'audit de fuite (annexe, code N)` ») et poussées sur la même branche de sortie.
- **Ce que fait la fille** : rien de plus que surveiller jusqu'à `FIN` (la ligne `AMORCE … fin, code 0` vient après le bras B) ; elle relève au compte rendu les lignes `bras B : début …` et `bras B : code N en S s …` ; elle **ne rapatrie ni n'ouvre** ses sorties. Leur lecture suit le texte de l'audit et son addendum (à sceller par la mère avant toute lecture du bras B, d'après l'en-tête du texte de T0.6), hors de cet ordre.
- **Condition** : GO-2026-11-07-04 exige « code, essais et ordre contre-lus et scellés avant la course » ; la mère le constate au registre avant la remise (préalable P7). GO-2026-11-07-04 échoit le 16 novembre (non prolongé, R-2077) : le bras B joue au plus tard avant la destruction de l'instance par sa minuterie à 2026-11-17T00:00Z.

## 8. Arrêts

| Événement | Ce que fait la fille |
|---|---|
| Préalable du § 3 manquant ; empreinte du § 1 différente ; `vastai --version` ≠ 1.8.3 ; `controles` code ≠ 0 ; branche de sortie présente sans nom suivant ; garde rejouée refusée sur S, ou artefact accepté | aucune création ; compte rendu à la mère |
| Commande imprimée non conforme au § 4.9 | rien n'est exécuté ; compte rendu |
| Recherche vide (code 3 « aucune offre conforme ») | fenêtre (§ 4.8), puis § 5 |
| Autre code 3 ou code 2 à la création ; code 4 après l'exécution | aucune création de plus ; inventaire filtré ; compte rendu |
| `ARRET mort` (processus du run mort sans résumé ni arrêt consigné) | arrêt par l'identifiant si l'instance n'est pas arrêtée ; § 4.12 ; compte rendu ; aucune relance sans écrit de la mère |
| Fin anormale (`AMORCE … fin, code 1` : suite ciblée en échec, nombre de tests ≠ 2022, arrêt consigné pendant le run, installation impossible, poussée impossible) | l'amorce a arrêté l'instance ; § 4.12 (avec `etape` et `motif` d'`arret.json` s'il existe) ; § 5 si erreur de mémoire à la distillation ; sinon compte rendu, aucune relance sans addendum de la mère |
| `REFUS` (l'amorce refuse avant le run) | la minuterie détruit l'instance ; inventaire filtré ; § 4.12 si la branche existe ; compte rendu |
| `ALERTE` sans `PROGRES` depuis 2 heures, ou garde de dépense illisible (une ou deux fois) | compte rendu à la mère ; aucun arrêt |
| `ARRET garde` (garde de dépense illisible trois fois) ; `ARRET inventaire` | arrêt par l'identifiant (après inventaire filtré pour le second) ; compte rendu |
| `ARRET depense` (200 USD) | § 6 |
| Ligne de journal qui porterait un état de sonde | § 2, point 7 |
| Échéance 2026-11-17T00:00Z atteinte en marche | la minuterie consigne, pousse les résultats partiels, détruit l'instance (amorce l. 101 à 126) ; inventaire filtré ; § 4.12 ; compte rendu |

**Aucun couperet de temps** (GO-2026-11-02-28) : la seule borne de calendrier est l'échéance du GO ; un run lent mais vivant n'est jamais arrêté.

## 9. Qui exécute, sous quel mot ; levée bornée de l'interdit `vastai` ; secrets

- **La fille nommée en en-tête exécute cet ordre**, sur la remise de Lazar ; le mot qui autorise la création est R-2077 ; tout mot neuf de Lazar (H200, création tardive, conservation du disque) est écrit **dans la session de la fille** et recopié verbatim, avec l'heure, au journal.
- **Levée écrite de l'interdit `vastai` pour la fille, bornée à** : les appels que fait `scripts/lancer_t06_v13.sh` lui-même (recherche filtrée, inventaire masqué, journal, présence de l'instance) ; la commande de création imprimée, exécutée **une fois** par création autorisée (§ 4.10, § 5) ; `timeout -k 5 120 vastai stop instance <ID>` du seul identifiant créé ; `timeout -k 5 120 vastai destroy instance <ID> -y` du seul identifiant créé (§ 4.13), puis un seul `show instance <ID> --raw` dont seul le code ou le texte exact `{"instances": null}` est écrit ; l'inventaire en champs filtrés par la commande exacte du § 4.7 ; `vastai --version`. **Rien d'autre** : jamais `start`, `reboot`, `copy`, `ssh`, `execute`, ni aucune commande sur une instance qu'elle n'a pas créée.
- **Secrets** : clés par leur nom seulement ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même sortie jetée ; jamais d'affichage de `instances.json`, `offres.json` brut d'inventaire, `creation-brute.json` ; **garde des secrets à 0** (commande du § 4.9, sur le fichier visé) avant tout envoi de texte à la mère ou à Lazar ; aucune autre clé touchée ; aucun appel de modèle ; aucune dépense hors de cet ordre.
- **Git** : la fille n'écrit rien sur le dépôt distant (la branche de sortie est poussée par l'instance) ; `git fetch` toujours avec un refspec explicite ; aucun clone sans `--single-branch`.
- **Si la fille doit s'arrêter avant la fin** : elle envoie à la mère et à Lazar le texte de `lancement.txt` (garde des secrets à 0), l'identifiant, les 50 dernières lignes de `progres.txt` et de `surveillance.txt`, le chemin du journal et le PID de sa surveillance ; elle n'arrête sa surveillance (par son PID) qu'une fois une autre session confirmée en surveillance ; entre-temps, la minuterie de l'instance borne la dépense (épuisement des 200 USD, échéance du 17 novembre à 00:00Z). Rien de neuf (relance, seconde instance) n'est engagé ensuite sans mot de Lazar dans la session qui dépense.

## 10. Compte rendu de la fille (nombres seuls, sans aucune valeur de sonde ni de coût, ≤ 400 mots)

`vastai --version` ; préalables P1 à P10 (oui ou non, avec les valeurs du § 4 : empreintes, ligne `SCELLEMENT-T07`, heure) ; heures et codes de `controles`, de la vérification de branche, des gardes (cas sain, artefact) ; chaque recherche de la fenêtre (heure, code) ; mot de Lazar éventuel (verbatim, heure) ; carte, offre (`prix_carte`, `prix_stockage`, forfait de téléchargement), identifiant créé, heure de création, H60 ; PID de chaque surveillance et heure de chaque relance ; dernière ligne de la suite ciblée ; durées par étape (lignes `PROGRES`) ; arrêt oui ou non, avec `etape` et `motif` s'il y a lieu ; heure de `FIN` et code de `fin` ; heure et code du `stop` ; tête de la branche de sortie, nombre de fichiers ajoutés (liste filtrée), compagnons `OK` et `ÉCART` ; identifiant du run et champs du manifeste du § 4.12 ; bras B (code, durée) ; dépense relevée (§ 6) ; heure et code de la destruction, texte de `show instance` (« absente » ou code), inventaire final ; écarts à l'ordre. **La fille ne lit ni la table A, ni les sondes, ni le résumé** ; elle ne cite ni `ligne_A`, ni `ligne_B`, ni `ligne_C`. Son journal (`journal-fille-7b-v1.md`, garde des secrets à 0) est envoyé à la mère, qui le verse et le scelle.

## 11. Ce qui suit la course (hors de cet ordre)

1. La mère verse et scelle le journal et le compte rendu de la fille ; inscrit la ligne `RUN-CONFIRMATION-T06` (manifeste de 7b, à sa sortie scellée) au registre `registres/scellements-v1.md` (texte, « Concordance avec T0.7 », point 4) ; inscrit la dépense au registre des dépenses.
2. **Table A** (coût : T6-1, T6-2, T6-10, T6-8, part « coût » de l'audit R4), lue dans l'ordre du point 7 du plan d'analyse, avant tout verdict de la table A, par un lecteur neuf qui relève aussi les effectifs et les réserves (dont l'avertissement d'allocation de mémoire de la carte dans `run.err`, s'il paraît) ; **verdict de la table A** par un sous-agent neuf (R13), scellé, soumis à Lazar.
3. **Règle « mots et coût »** : pièce neuve, calculée après la course sur processeur, après le scellement de T0.8, par des auteurs qui n'ont vu aucune donnée de 7b ; ligne `CODE-MOTS-ET-COUT-T06` avant son exécution, `ISSUE-MOTS-ET-COUT-T06` après (texte, « Concordance avec T0.7 », points 2 à 5).
4. **Sondes** (T6-5, T6-3, T6-4, T6-7, T6-6, T6-9, part « sondes » de l'audit R4 ; tables B et C) : **seulement après le verdict scellé de P3-bis** (DT-4) **et après la lecture scellée des bases boîte noire de T0.8 sur ces épisodes** ; ouverture de `lecture-sondes-t06.json` seulement après un contrôle d'ouverture v2 passé (lignes `VERDICT-P3BIS` et `ISSUE-MOTS-ET-COUT-T06` au registre, strictement antérieures) ; verdict des tables B et C par un sous-agent neuf (R13), scellé, soumis à Lazar.
5. T0.7 (étape A et suivantes) : son propre ordre et sa propre ligne de GO ; P3-bis : sa chaîne et son GO.

## 12. Ce que cet ordre ne fait pas

Aucune lecture de résultat (ni coût, ni sondes, ni résumé, ni bras B) ; aucune étape de T0.7 ; aucun contact externe ; aucun appel de modèle ; aucune modification du code, du texte scellé, de la configuration ou de la commande imprimée ; aucune chaîne v14 ; aucune fusion de la branche de sortie dans `main` ; aucune écriture de la fille sur le dépôt distant ; aucun geste sur une instance que la fille n'a pas créée.

## 13. Devis (rappel du texte scellé, « Devis de la confirmation 7b », révision 3 ; aucun chiffre neuf)

- **Attendu** (A100, heures de 7a : instance 13,59 h) : 14,8 à 17,7 USD de calcul ; disque de l'instance arrêtée ≤ 5,8 USD (72 h × 0,08) ; téléchargement ≤ 2 USD : **≈ 16 à 26 USD** ; bras B ≈ 20 minutes de carte en plus.
- **Pire cas** (cumulatif, sous 200 USD) : P1, hôte deux fois plus lent ≈ 46 USD ; P2, P1 plus une relance complète ≈ 86 USD ; P3, erreur de mémoire à la distillation puis course entière sur H200 ≈ 151 USD. **H200 d'emblée** (fenêtre vide) : ≈ 72 USD aux durées de 7a, ≈ 136 au débit moitié. Compte rendu à Lazar à 60 USD ; nœud de Lazar avant toute relance au-delà de 180 ; arrêt à 200.
- **Calendrier** : dernière création sans nœud 2026-11-15T20:48Z ; pour garder une relance complète, première création au plus tard le 14 novembre vers 17:00Z.

**Points ouverts portés à la mère** (détail au journal du rédacteur) : (1) conservation du disque au-delà du 16 novembre pour T0.7 « sur la même machine » (GO-2026-11-10-01) contre la « Liste d'arrêt » du texte : nœud de Lazar, défaut de cet ordre : destruction au plus tard 2026-11-16T23:00Z ; (2) forme d'exécution de la commande (R-1914) à confirmer par la contre-lecture ; (3) l'amorce v11 clone toutes les branches du dépôt distant (l. 284) : sur l'instance, les commits et les arbres (noms de fichiers, sans contenu) des branches sous embargo présentes sur le dépôt distant entrent dans son `.git` ; personne ne les lit ; accès mécanique à consigner comme R-2064 ; (4) conditions de GO-2026-11-07-04 et état de l'addendum du bras B ; (5) aucune ligne de GO propre à l'étape A de T0.7 n'a été trouvée par le rédacteur dans `registres/go.md`.

## 14. Marqueurs (à remplir par la mère avant la contre-lecture ; une occurrence chacun)

| Marqueur (nom, sans chevrons) | Où | Ce que la mère y écrit |
|---|---|---|
| `ID_SESSION_FILLE` | en-tête | identifiant de la session fille porteuse des clés |
| `DEPENSE_ANTERIEURE_USD` | ligne (A) | dépense déjà inscrite au registre des dépenses sous GO-2026-11-02-28 et GO-2026-11-10-01 au commit de remise, en USD (attendu `0`) |
| `COMMIT_MAIN_REMISE` | § 4.1 | commit de `main` (40 caractères) qui porte cet ordre scellé, la ligne `SCELLEMENT-T07` et la ligne d'engagement |
| `LIGNE_SCELLEMENT_T07` | § 4.3 | la ligne exacte `| SCELLEMENT-T07 | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |` de `registres/scellements-v1.md` (format de `scripts/controle_lecture_t06_v1.py`, commit `061ac380`) |
| `LIGNE_REGISTRE_BRAS_B` | § 4.3 | identifiant de la ligne de `registres/decisions.md` (forme `R-NNNN`) où la mère constate les conditions de GO-2026-11-07-04 (§ 7) |

## 15. Sources

Texte scellé `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`) et configuration `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1ba…`) ; `registres/decisions.md` (au commit `85346292`) R-1914, R-1977, R-2039 à R-2041, R-2048, R-2057, R-2062, R-2064, R-2077, R-2079 à R-2082 ; `registres/go.md` GO-2026-11-02-28, GO-2026-11-07-02, GO-2026-11-07-04, GO-2026-11-10-01 ; ordre de 7a `docs/procedures/ordre-fille-cles-2-course-dose-reponse-exploratoire-v1.md` (`4c6c70d4…`) et ses addenda 1 (`8075ae07…`) et 2 (`c53c9263…`) ; lecture A de 7a (`3c84c419…`, comptes, heures, mémoire seulement) ; contre-lectures 6 et 7 du texte ; rapport d'essai à blanc de la voie B (`docs/notes/g0-deux-semaines-v1/integration-t06-v13-main-v1/rapport-essai-blanc-S-voie-b-v1.md`) ; au commit `1609a4bf`, par `git show` : `scripts/lancer_t06_v13.sh`, `scripts/amorce_instance_t06_v11.sh`, `scripts/fenetre_carte_t06_v1.sh`, `src/controle_ia/t06/session.py`, `session_v2.py`, `session_v3.py`, `session_v12.py`, `lanceur.py`, `lanceur_v6.py`, `src/controle_ia/harnais/validation_reelle.py`, `src/controle_ia/manifeste.py`, `src/controle_ia/prereg.py`, `.claude/hooks/garde_calcul.py` ; au commit `061ac380`, `scripts/controle_lecture_t06_v1.py` (format du registre). Lignes et empreintes : journal du rédacteur.
