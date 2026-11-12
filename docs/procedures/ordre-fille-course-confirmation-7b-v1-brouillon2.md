# Ordre — course de confirmation 7b de T0.6 (organismes v0, sous préenregistrement scellé), session fille porteuse des clés — v1, brouillon 2

> **COURSE DÉCISIVE (R1), SORTIE SCELLÉE AVANT LECTURE.** La fille lance, surveille, arrête, rapatrie et détruit ; elle **ne lit aucun résultat**. L'embargo DT-4 (§ 2) est rappelé nommément : à 7a, une consigne de la mère l'a fait rompre (R-2041).

- **Statut** : brouillon 2, écrit le 2026-11-10 à partir de 07:12 UTC (`date -u`) par le rédacteur du brouillon 1 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5 ; auteur d'aucune pièce de T0.6, T0.7, P3-bis ni de l'ordre de 7a). Remplace le brouillon 1 (`bd337c7d…`, gardé, R12) selon les décisions de la mère (R-2087 et son message du 10 novembre). Journal : `…-brouillon2-journal-v1.md`. **Non contre-lu** ; avant la remise : marqueurs (§ 14), contre-lecture (R2) par un sous-agent neuf, scellement, remise par Lazar.
- **Autorisation** : R-2077 (mot de Lazar du 10 novembre ; lecture de la mère au registre) : création sous **GO-2026-11-02-28**, plafond 200 USD, **compte rendu à Lazar à 60 USD**, **mot de Lazar avant toute création sur H200** ; R-2079 : chaîne v13, création au plus tard le 15 ; R-2082 : T0.6 scellé.
- **Exécutante** : la session fille `<<ID_SESSION_FILLE>>`, porteuse des clés, active pendant toute la course.

## 0. Objet

La course préenregistrée par `prereg/T0.6-organismes-v0-v1.md` (révision 10, `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`), chaîne de 7a (v13, code `1609a4bf`), configuration de 7b, graines neuves : **deux résultats scellés séparés** (coût ; sondes, fermé jusqu'au verdict scellé de P3-bis), poussés sur une branche neuve. Ni lecture (§ 11), ni étape de T0.7 (instance seulement gardée pour elle, § 4.13), ni P3-bis, ni bras d'attaque.

## 1. Cadre

| Élément | Valeur |
|---|---|
| S | `935262b17ca95894a882b02f1526ee39d1738652`, ancêtre d'`origin/main`, cloné par l'instance, trouvé par `commit_s` (lanceur l. 112) |
| Code cité | `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` (arbre gelé de S) |
| Configuration | `prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`, canonique `ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d` : GO-2026-11-02-28, plafond 200, dernier jour de création 2026-11-15, fin du GO `1794873600` (2026-11-17T00:00:00Z), A100 SXM4 ≤ 1,30 USD/h, relance H200 NVL ≤ 4,70 USD/h, stockage ≤ 0,08 USD/h, disque 150 Go, étiquette `t06-v2` |
| Chaîne gelée (`1609a4bf` ; identique sur `main`, § 4.2) | `scripts/lancer_t06_v13.sh` `6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416` ; `scripts/amorce_instance_t06_v11.sh` `43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859` ; `src/controle_ia/t06/session.py` `ad7031ab028787a3ea4bc4edfbf86206f56ccd916f447a150b639ba96f50bb17`, `session_v2.py` `6d9f75989e5e21a26b600378167a84f349d4dbc1a9c8740ede7d8471f6779266`, `session_v3.py` `365d2fde7fe9c4670fd3f2bcb404c3979b1db4e3cc862f0a4a46acf867b4bcf3`, `session_v12.py` `5b4ad5e9fa39c4a803050ed118157d005bcb30551a54a6822f38a15ca0ddd90e`, `lanceur_v6.py` `e329493b5d54fe52f6eb278b1314a78f905ca082a51ee1a0c5c3a77bd400ac80`, `configuration_v6.py` `7899622515588284d1045c72aee95d109ff755f525d3c4bcd70df14caf6fad8e` ; `scripts/tests-cibles-t06-v3.txt` `e76d5e6b7c32140b549de20f061a2e562df9201c5daab4060fd1ca54a05f42e2`, `scripts/tests-exclus-t06-v3.txt` `ab70a1ed4b59bdb5f488e453055029806cde30c36552684f686097fbea8ed81c` ; `src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py` `317a7ea551abace1b3b78acde543688ab33bfda57cd15d8e6072f0826ce6fa17`. **Jamais de chaîne v14** (R-2079) |
| Mode | **course** (`controles`, `creation`), jamais `controles-epreuve` : GO en dur (l. 83), plafond 200 exigé (l. 197) ; l'instance lit configuration et « Tests attendus » (`2022`) dans le texte de S (amorce l. 375 à 388) |
| GO | **GO-2026-11-02-28** (seul lu ; échéance 16 novembre) ; GO-2026-11-07-02 (carte de repli), GO-2026-11-07-04 (bras B) ; GO-2026-11-10-01 (prolongation au 23) **non lue par la chaîne** : aucune création après le 15 |
| Branche de sortie | **`calcul/t06-confirmation-7b-v1`**, absente du dépôt distant (§ 4.5) ; seconde instance `-v2`, puis `-v3` ; jamais `calcul/t06-reel-v4` ni `main` |
| Dépôt | `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, en dur dans la commande de création (l. 235), vérifié au § 4.9 ; jamais `lciric/controle-ia` |
| Outil, dossiers | `vastai` 1.8.3 (autre version ou absent : arrêt, aucune installation sans écrit de la mère) ; travail `/home/user/course-7b-v1` (neuf, sinon `-v2`) ; contrôles `c7b-1` (neuf à chaque reprise : `c7b-1-r2`, …) |

## 2. Embargo DT-4 et chemins interdits

1. **Jamais** la fille n'ouvre, n'affiche, ne copie, ne hache ni ne passe à un outil un `lecture-sondes-t06.json` (de 7b, de 7a, d'aucun run) ni son compagnon : exclu de ses clones (§ 4.1), jamais rapatrié (§ 4.12), exclu de toute liste par `':(glob,exclude)diag/*/lecture-sondes-t06.json*'` ; sa présence se déduit de `resume.json`, écrit après lui (`lanceur_v6.py` l. 317 à 333).
2. **Jamais** `donnees/lecture-b-7a-quarantaine-v1`, `essai/t06-explo-v3`, ni `diag/`, `runs/`, `donnees/` de 7a ; clones de la seule branche `main` ; `git fetch` par refspec explicite.
3. **Jamais** `scripts/extraire_mesures_epreuve_t06_v1.py` (R-2057), `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, l'étiqueteur (`prep/etiqueteur-v2-lecture-interrompue-reprise-v1`) : exclus de ses clones ; aucune recherche récursive sur un arbre qui contient un chemin interdit sans l'exclure (interdits communs v2, règle 9) ; jamais `verifier-arbre`.
4. **Aucune lecture de résultat de 7b** : jamais affichés `lecture-cout-t06.json`, `resume.json` (il porte `ligne_A`, `ligne_B`, `ligne_C`), `distillation-t06.json`, `episodes-t06.json`, `run.err`, `run.json` (hachés seulement) ; jamais rapatrié `donnees/<run>/` (la pièce « mots et coût » s'écrit sans vue des données de 7b).
5. **La fille ne lit que** ses sorties et codes ; `lancement.txt`, `progres.txt`, `surveillance.txt`, `journal-instance.txt` ; les champs nommés du manifeste, `traces/t06-*/journal.txt`, `traces/*/empreintes.sha256`, `etape` et `motif` d'`arret.json` ; la dépense. Une ligne portant un état, une aire, un score ou une ligne de table (filtre C01, amorce l. 300, 502 à 504) : rien n'en est recopié, la lecture cesse, la mère est avertie.
6. **Accès mécanique connu** (code gelé ; consigné par la mère, R-2087, même classe que R-2064) : sur l'instance, l'amorce clone toutes les branches du dépôt distant (l. 284), dont celles sous embargo, et son extraction copie `docs/notes/bras-attaque/` ; leurs objets entrent sur l'instance **sans lecture ni affichage** ; seule S est extraite et jouée ; la fille n'y touche pas.

## 3. Préalables bloquants (vérifiés par la fille, écrits au journal avec l'heure)

| # | Préalable | Où | Sinon |
|---|---|---|---|
| P1 | **T0.6 scellé** : S ancêtre d'`origin/main`, `commit_s` = S, texte et configuration à leurs empreintes dans S, `1609a4bf` ancêtre de S | § 4.2, 4.4 | arrêt |
| P2 | **T0.7 scellé** (GO-2026-11-02-28 l'exige) : une seule ligne `SCELLEMENT-T07` dans `registres/scellements-v1.md` de `main`, égale à celle de la remise, fichier et compagnon à son empreinte | § 4.3 | aucune création ; ligne absente le **13 novembre à 12:00 UTC** : ordre **suspendu** (R-2079, nœud), rien sans addendum de la mère |
| P3 | **GO-2026-11-02-28** seul lu, une ligne, non révoqué (de même GO-2026-11-07-02, -07-04) ; `controles` le dit conforme | § 4.3, 4.4 | aucune création |
| P4 | **Jour** : création au plus tard le **15** ; **le 14 vers 17:00 UTC** pour garder une relance (fenêtre commencée vers 14:00) ; sans nœud au plus tard **2026-11-15T20:48Z** | `date -u` | après : mot de Lazar ; le 16 : rien |
| P5 | **Remise** : tête clonée descendante du commit de remise ; empreinte de l'ordre égale au message de remise | § 4.1 | arrêt |
| P6 | **Engagement** au registre des dépenses (écrit par la mère, § 6) ; dépense antérieure relevée (§ 14) | § 4.3 | aucune création |
| P7 | **Bras B** (GO-2026-11-07-04) : code contre-lu (rempli) ; **addendum v3 scellé** (**non rempli à la rédaction**, § 7) | § 4.3 | **aucune création avant un mot de Lazar sur ce point**, dans la session de la fille |
| P8 | **Chaîne** égale à `1609a4bf` ; `controles` conforme ; branche absente ; gardes conformes sur S, artefact refusé | § 4.2, 4.4 à 4.6 | arrêt |
| P9 | `vastai` 1.8.3 ; `HF_TOKEN` et un jeton GitHub présents (par le nom) ; `PY` importe `controle_ia.t06.lanceur` | § 4.0, 4.6 | arrêt |
| P10 | Aucune instance d'étiquette `t06-v2…` | § 4.7 | arrêt ; rien n'est touché |

## 4. Étapes et commandes exactes

L'état du shell ne survit pas d'une commande à l'autre : **chaque bloc commence par la ligne (A)**. Les clés passent **par leur nom**, jamais par leur valeur.

**(A)** :

```bash
W=/home/user/course-7b-v1; M=$W/main; AM=$W/amorce; D=$W/c7b-1; J=$W/journal-fille-7b-v1.md; S=935262b17ca95894a882b02f1526ee39d1738652; C=1609a4bf2c1572f72bb8542d81d963ac6a8481c4; B=calcul/t06-confirmation-7b-v1; URL=https://github.com/lciric/controle-ia-travail.git; PY=/home/user/controle-ia-travail/.venv/bin/python; ANT0=<<DEPENSE_ANTERIEURE_USD>>; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }; champ() { sed -n "s/^$1 //p" "$D/lancement.txt" | tail -1; }
```

`PY` : interpréteur du dépôt de la fille (chemin réel consigné s'il diffère). `W`, `D`, `B` changent à chaque reprise ; le nom en vigueur est écrit au journal.

### 4.0 Dossier, journal, enveloppe du lanceur, inventaire, outil, clés

```bash
# (A)
mkdir "$W" && : > "$J" && j "début de l'ordre de 7b ; dossier $W" || echo "ARRÊT : $W existe déjà (R12)"
cat > "$W/v13.sh" <<'FIN'
#!/usr/bin/env bash
# Enveloppe du lanceur gelé v13 : variables passées à env -i par leur NOM seulement ; aucune valeur écrite ici.
# Usage : bash v13.sh BRANCHE_DE_SORTIE SOUS-COMMANDE ARGUMENTS…
set -u
B="${1:?branche de sortie}"; shift
cd /home/user/course-7b-v1/main || exit 2
exec env -i PATH="$PATH" HOME="$HOME" LANG="${LANG:-C.UTF-8}" VAST_API_KEY="${VAST_API_KEY:-}" HF_TOKEN="${HF_TOKEN:-}" GH_TOKEN="${GH_TOKEN:-}" CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN:-}" CONTROLE_IA_GITHUB_TOKEN_2="${CONTROLE_IA_GITHUB_TOKEN_2:-}" GO_ID=GO-2026-11-02-28 T06_BRANCHE="$B" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" HTTPS_PROXY="${HTTPS_PROXY:-}" NO_PROXY="${NO_PROXY:-}" INTERVALLE="${INTERVALLE:-60}" bash scripts/lancer_t06_v13.sh "$@"
FIN
cat > "$W/inventaire.sh" <<'FIN'
#!/usr/bin/env bash
# Inventaire en champs filtrés (commande de l'ordre de 7a) : jamais le brut, qui imprime des variables secrètes.
timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances",d) if isinstance(d,dict) else d; [print(i.get("id"),i.get("label"),i.get("actual_status"),i.get("dph_total"),i.get("duration")) for i in (d or [])]'
FIN
sha256sum "$W/v13.sh" "$W/inventaire.sh"
vastai --version
for k in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN CONTROLE_IA_GITHUB_TOKEN_2 VAST_API_KEY; do if [ -n "${!k:-}" ]; then echo "$k présente"; else echo "$k absente"; fi; done
```

- Dossier existant : `-v2` dans (A) et dans la ligne `cd` de l'enveloppe. L'enveloppe passe **quinze noms** à `env -i`, aucune valeur ; les quatre du mandataire viennent de l'addendum 1 de l'ordre de 7a (`8075ae07…`), jamais transmis à l'instance ; en course, le lanceur ignore `GO_ID` (l. 82–83), écrit le GO dans la commande (l. 235) et y rejoue la garde de calcul (l. 236). **Jamais posés** : `PREREG_ABSENT`, `T06_EPUISEMENT_SIMULE_S` (refusé, l. 198), `T06_TESTS_ARGS`, `T06_PREREG`, `T06_DEPOT`, `T06_IMAGE`, `T06_REGISTRE_GO` (registre du clone de `main`, l. 84), `BRAS_B`.
- Attendu : 1.8.3 ; `HF_TOKEN` et un jeton GitHub présents ; `VAST_API_KEY` présente ou `vastai` configuré par son fichier.

### 4.1 Deux clones de la seule branche `main`, comme celui de l'amorce, sous exclusions

```bash
# (A)
printf '%s\n' '/.claude/' '/src/' '/tests/' '/scripts/' '/pyproject.toml' '/requirements-*.txt' '/prereg/' '/donnees/' '/diag/' '/runs/' '/traces/' '/registres/*.md' '/docs/*.md' '/docs/*.txt' '/docs/*.sha256' '/docs/notes/' '/docs/procedures/' '/docs/decisions/' '/docs/verdicts/' '/docs/etat-de-l-art/' '/docs/sources/invites-2606.07054-v1/' '/docs/sources/invites-2606.08892-v1/' '/docs/sources/cartes-modeles-20261006/' '/docs/sources/donnees-T0.7/' '/brouillons/ordres-t06-e2-e3-v2/' '/brouillons/ordres-t06-e2-e3-v3/' '/brouillons/ordres-t06-e2-e3-v4/' '/brouillons/ordres-t06-e2-e3-v5/' '!/docs/notes/bras-attaque/' '!/donnees/bras-attaque*' '!/donnees/mode-tenu-a-l-ecart*' '!/diag/*/lecture-sondes-t06.json*' '!/scripts/extraire_mesures_epreuve_t06_v1.py' '!/registres/index-bras-attaque*' > "$W/motifs.txt"
for X in "$M" "$AM"; do timeout -k 10 900 git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$X" && git -C "$X" sparse-checkout init --no-cone && git -C "$X" sparse-checkout set --no-cone --stdin < "$W/motifs.txt" || echo "ARRÊT : clone $X"; done
git -C "$M" checkout -q main; timeout -k 10 900 git -C "$AM" checkout -q "$S"
git -C "$M" rev-parse HEAD origin/main; git -C "$AM" rev-parse HEAD
test -f "$M/scripts/lancer_t06_v13.sh" && test -f "$AM/prereg/T0.6-organismes-v0-v1.md" && echo "extractions présentes"
git -C "$M" merge-base --is-ancestor <<COMMIT_MAIN_REMISE>> HEAD && echo "remise : ancêtre de la tête clonée"
```

Les 28 premiers motifs sont ceux de l'amorce (l. 255 à 282) ; **écarts déclarés** : une seule branche, six exclusions (sans effet sur l'arbre gelé ni sur le lanceur). Attendu : `$M` à `origin/main`, `$AM` à S, les deux messages ; puis `sha256sum -c` du compagnon de cet ordre dans `$M`, égal au message de remise.

### 4.2 Chaîne et commit de scellement (P1, P8)

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

Attendu : code 0 ; la seule ligne `.claude/hooks/garde_calcul.py` (règle neuve R-1984, sans effet sur une création) ; les onze empreintes du § 1 ; lignée ; `commit_s = S` ; `ef31feff…`, `b7a5c1ba…`. Écart : arrêt.

### 4.3 GO, T0.7, engagement, bras B (P2, P3, P6, P7)

```bash
# (A)
cd "$M"; date -u +%FT%TZ
for g in GO-2026-11-02-28 GO-2026-11-07-02 GO-2026-11-07-04 GO-2026-11-10-01; do printf '%s : %s ligne(s)\n' "$g" "$(grep -c "^| $g |" registres/go.md)"; done
grep -E '^\| GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2} \| [0-9-]+ \| révocation \|' registres/go.md | grep -cE 'GO-2026-11-02-28|GO-2026-11-07-02|GO-2026-11-07-04|GO-2026-11-10-01'
grep -c '^| SCELLEMENT-T07 |' registres/scellements-v1.md
L7=$(grep '^| SCELLEMENT-T07 |' registres/scellements-v1.md); printf '%s\n' "$L7" > "$W/ligne-scellement-t07.txt"; P7=$(printf '%s\n' "$L7" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); H7=$(printf '%s\n' "$L7" | awk -F'|' '{gsub(/ /,"",$5); print $5}')
[ "$L7" = '<<LIGNE_SCELLEMENT_T07>>' ] && echo "ligne SCELLEMENT-T07 = celle de la remise"
[ "$(git show "HEAD:$P7" | sha256sum | cut -d' ' -f1)" = "$H7" ] && [ "$(git show "HEAD:$P7.sha256" | cut -d' ' -f1)" = "$H7" ] && echo "T0.7 scellé : $P7 $H7"
git show HEAD:registres/depenses.md | grep -F 'GO-2026-11-02-28' | grep -F 'course de confirmation 7b' | grep -ci 'engagement'
grep -c '^| <<LIGNE_REGISTRE_BRAS_B>> |' registres/decisions.md
```

Attendu : une ligne par GO ; 0 révocation ; une ligne `SCELLEMENT-T07`, égale à la remise, fichier et compagnon conformes ; au moins une ligne d'engagement ; la ligne du bras B une fois. Si elle manque (la mère écrit `AUCUNE` quand l'addendum n'est pas scellé) : **aucune création avant un mot de Lazar sur le bras B** (§ 7).

### 4.4 Contrôles en ligne (`controles`, sans dépense)

```bash
# (A)
bash "$W/v13.sh" "$B" controles "$D" > "$W/controles-$(basename "$D").txt" 2>&1; echo "code $?"; cat "$W/controles-$(basename "$D").txt"
for k in commit prereg config branche amorce go; do printf '%s : %s\n' "$k" "$(champ "$k")"; done; sha256sum "$D/config.json"
```

`controles` (l. 119 à 146) ; **attendu**, code 0 : « `GO-2026-11-02-28 conforme (plafond 200 USD, 2026-11-02 → 2026-11-16)` », puis « `CONTRÔLES CONFORMES : S=935262b17ca95894a882b02f1526ee39d1738652 ; amorce v11 43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859 ; GO GO-2026-11-02-28 ; fin_go_utc_s=1794873600 dernier_jour_creation=2026-11-15 echeance_go=2026-11-16` » ; champs S, texte, configuration, branche `calcul/t06-confirmation-7b-v1`, amorce `43d85659…`, GO ; `config.json` à `b7a5c1ba…`. Sinon : arrêt ; reprise dans un dossier neuf.

### 4.5 Branche de sortie absente du dépôt distant

```bash
# (A)
git -C "$M" ls-remote --exit-code origin "refs/heads/$B" > /dev/null; echo "code $?"
```

Attendu **code 2**. Code 0 (l'amorce refuserait, l. 404 à 409) : nom suivant, contrôles rejoués dans un dossier neuf. Autre : arrêt.

### 4.6 Gardes rejouées : clone de l'amorce (cas sain), `main` (artefact)

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

Gardes de `lanceur_v6.executer` (l. 164 à 180) et `manifeste.creer_manifeste` (l. 89 à 96), sur un clone venu du dépôt distant comme celui de l'instance (texte, plan, point 3 (5) ; R-2082). **Cas sain**, code 0 : `configuration b7a5c1ba…` ; `exiger_config_t06_v6 passe` ; `taches 76cdeace… 8d20a698…` ; `exiger_code_importe_sous passe` ; `exiger_citations_t06 31538212097275005629337336542801867913` ; `exiger_prereg_scelle ef31feff…` ; `exiger_code_cite 1609a4bf2c1572f72bb8542d81d963ac6a8481c4`. **Artefact** (R5), code 1 : mêmes lignes, puis « `arbre gelé (code, tests, scripts, dépendances, configuration) modifié depuis le commit cité 1609a4bf2c15` » (refus observé par le rédacteur). Sain refusé ou artefact accepté : arrêt.

### 4.7 Inventaire avant la création

```bash
# (A)
bash "$W/inventaire.sh"
```

Aucune étiquette `t06-v2…` (sinon arrêt). Les instances non créées par la fille (dont 58936096, 58936099, 58936100, intouchables) ne sont jamais touchées.

### 4.8 Création sur l'A100 : fenêtre de GO-2026-11-07-02

`creation auto course` **ne loue rien** : il choisit l'offre, relit l'inventaire, rejoue la garde de calcul et **imprime** la commande (l. 178 à 240).

```bash
# (A)
n=1   # numéro de la recherche, de 1 à 12 ; jamais réutilisé (R12)
date -u +%FT%TZ; bash "$W/v13.sh" "$B" creation auto course "$ANT0" "$D" > "$D/creation-sortie-$n.txt" 2>&1; echo "code $?"; head -n 1 "$D/creation-sortie-$n.txt" | cut -c1-300
```

- **Code 0** (« `OFFRE CONFORME : …` ») : § 4.9 sans attendre.
- **Code 3 avec « aucune offre conforme »** : recherche vide, rien créé ni compté ; nouvelle recherche **toutes les 15 minutes, 12 au plus (3 h, 0 USD)**, fichier neuf, heure et code au journal ; douze vides : § 5.
- **Autre code 3** (instance du programme, dépense au plafond, trois essais, calendrier) **ou code 2** : aucune bascule ; arrêt, compte rendu (règle de `scripts/fenetre_carte_t06_v1.sh` l. 19 à 23 ; script non lancé : il dépasserait la durée d'une commande de fond).
- Dépense antérieure : `ANT0` à la première instance, **jamais 0 ensuite** (§ 5).

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

Attendu : `3` ; `1` ; `1` ; `1` (les **neuf** variables de la l. 235 et elles seules, dont `DEPOT_URL` du dépôt de travail et deux jetons **par leur nom**) ; « épuisement = lancement.txt » ; `0` (la base 64 n'a jamais de `_`) ; `43d85659…` ; garde des secrets `0` ; `carte course` (`relance` au § 5), `prix_carte` ≤ 1,30 (≤ 4,70), `prix_stockage` ≤ 0,08, `anterieure` = dépense passée, `echeance` 1794873600, `essai_creation` ≤ 3. Un écart : rien n'est exécuté.

### 4.10 Exécution, une fois

```bash
# (A)
n=<même numéro>; GO_ID=GO-2026-11-02-28 bash -c "$(tail -n 1 "$D/creation-sortie-$n.txt")"; echo "code $?"
```

- Forme de 7a (R-1914), **à juger par la contre-lecture** (§ 13) : la commande imprimée, à l'octet ; jetons par référence ; sortie de `vastai` lue puis effacée par `apres-creation` (l. 241 à 259).
- **Code 0** « `CRÉÉE : instance <ID> …` » : identifiant et heure au journal. **Code 5** (offre refusée) : § 4.8 aussitôt (fichier neuf), § 4.9, § 4.10 ; trois essais au plus par dossier. **Code 4** (création incertaine) : aucune seconde création ; inventaire ; compte rendu.

### 4.11 Surveillance, heure des 60 USD

```bash
# (A)
ID=<identifiant créé>
python3 -I -B -c "import sys; sys.path.insert(0, '$M/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))" depense 60 "$(champ prix_carte)" "$(champ prix_stockage)" "$(champ creation)" "$(champ anterieure)" "$(champ telechargement_forfait)"
bash -c 'echo "$(date -u +%FT%TZ) PID $$" >> "$1/pids-surveillance.txt"; exec bash "$2/v13.sh" "$3" surveillance "$4" "$1"' _ "$D" "$W" "$B" "$ID" >> "$D/surveillance-sortie.txt" 2>&1
```

- La première (`session_v3 depense`, l. 83 à 110) rend `epuisement_utc_s=<H60>`, heure des 60 USD cumulés, écrite au journal ; instance en marche à H60 : **compte rendu à Lazar** (§ 6), sans arrêt.
- La seconde, **en tâche de fond** ; `exec` garde le PID écrit (arrêt par ce PID seulement) ; arrêtée **sans** `ARRET` ni `FIN` (limite de 2 h de l'outil) : relancée à l'identique (l. 260 à 351).
- **Repères** (7a, lecture A, R-2040) : suite ≈ 35 min (« `2022 passed …` », sinon arrêt, l. 492 à 494) ; distillation ≈ 4 h 20 (avertissement de mémoire possible, **sans arrêt**) ; épisodes ≈ 6 h 50 ; test croisé et couples ≈ 1 h 46 ; puis bras B ; ≈ 13,6 h. **Aucun couperet de temps** ; 2 h sans `PROGRES` : `ALERTE`, compte rendu, sans arrêt.

### 4.12 Fin, arrêt par l'identifiant, rapatriement sans les contenus, compagnons

À la sortie de la surveillance (`FIN` 0, `ARRET` 3, `REFUS` 4), la fille relève la dernière ligne `AMORCE … fin, code N`, puis :

```bash
# (A)
ID=<identifiant créé>; bash "$W/inventaire.sh"
timeout -k 5 120 vastai stop instance "$ID"; echo "code $?"   # seulement si l'instance n'est pas déjà arrêtée ; jamais un autre identifiant
git -C "$M" fetch -q --filter=blob:none origin "refs/heads/$B:refs/remotes/origin/$B"; echo "code $?"
R=refs/remotes/origin/$B; X=':(glob,exclude)diag/*/lecture-sondes-t06.json*'; git -C "$M" rev-parse "$R"; git -C "$M" log --format='%H %cI %s' "$S..$R"
git -C "$M" diff --name-status --no-renames "$S" "$R" -- . "$X" | grep -vc '^A'
L=$W/fichiers-ajoutes-$(basename "$D").txt; git -C "$M" diff --name-only --no-renames --diff-filter=A "$S" "$R" -- . "$X" > "$L"; wc -l < "$L"
RUN=$(sed -n 's|^runs/\([0-9]\{8\}-[0-9]\{6\}-t06-reel\)/manifeste\.json$|\1|p' "$L"); echo "run : $RUN"
grep -E "^(runs|diag)/$RUN/" "$L" | grep -v '\.sha256$' | while IFS= read -r f; do a=$(git -C "$M" show "$R:$f" | sha256sum | cut -d' ' -f1); b=$(git -C "$M" show "$R:$f.sha256" | cut -d' ' -f1); [ "$a" = "$b" ] && echo "OK $f $a" || echo "ÉCART $f"; done
for d in $(grep -oE '^traces/(t06|consignation)-[^/]+/' "$L" | sort -u); do git -C "$M" show "$R:${d}empreintes.sha256" | while read -r h nom; do [ "$(git -C "$M" show "$R:$d$nom" | sha256sum | cut -d' ' -f1)" = "$h" ] && echo "OK $d$nom" || echo "ÉCART $d$nom"; done; done
git -C "$M" show "$R:runs/$RUN/manifeste.json" | python3 -I -c 'import json,sys; m=json.load(sys.stdin); print(m["run_id"], m["commit"], m["decisif"], m["depot_propre"], (m["preenregistrement"] or {}).get("sha256"), m["config_sha256"], m["reserves"], m["commande"])'
```

- **Arrêt** : à `FIN`, l'amorce a déjà demandé « stopped » (l. 151 à 164) ; le `stop` imprimé n'est exécuté que si l'inventaire ne montre pas l'instance arrêtée ; `REFUS` : la minuterie détruit après 180 s (l. 141 à 146).
- **Rapatriement sans les contenus** : seuls entrent sur le disque les fichiers extraits ci-dessus ; sondes, `donnees/<run>/` et bras B restent sur le dépôt distant.
- **Attendu** (fin normale) : commits « `T0.6 (reel), run <run> : résultats et données légères` », « `… sous-ensemble d'activations en morceaux …` », « `T0.6 : traces de l'instance (fin)` », puis « `T0.6 : bras B de l'audit de fuite (annexe, code N)` » s'il a tourné ; `0` changement autre qu'un ajout ; un run `AAAAMMJJ-HHMMSS-t06-reel` ; `OK` pour le manifeste, `distillation-t06.json`, `episodes-t06.json`, `lecture-cout-t06.json`, `resume.json` (hachés, **jamais affichés**) et chaque fichier des traces ; manifeste : `<run> 935262b17ca95894a882b02f1526ee39d1738652 True True ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169 ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d [] python -m controle_ia.t06.lanceur_v6`. `ÉCART` : compte rendu, rien d'autre.
- **Arrêt consigné** : `etape` et `motif` seuls, jamais `partiel` :

```bash
# (A)
R=refs/remotes/origin/$B; RUN=<run>; git -C "$M" show "$R:diag/$RUN/arret.json" | python3 -I -c 'import json,sys; r=json.load(sys.stdin)["resultat"]; print("etape :", r.get("etape")); print("motif :", str(r.get("motif"))[:300])'
```

- Lignes relevées (`traces/t06-…/journal.txt`, `journal-instance.txt`) : `tests : …`, `run : …`, `run terminé : …`, `branche … poussée …`, `PROGRES … etape=…`, `ERREUR DE CHAÎNE`, `FIN ANORMALE`, `RUN MORT`, `bras B : …` (celles-ci dans `journal-instance.txt` seulement).

### 4.13 Fin de course : instance gardée pour l'étape A de T0.7, ou détruite

Décision de la mère (R-2087 et son message du 10 novembre) : T0.7 (brouillon 19, « Calcul et dépense », « Lancement nominal ») joue son étape A **sur l'instance de 7b, après la course et la poussée de ses résultats, avant sa destruction**. Après une **fin normale** (`fin, code 0`, `resume.json` présent, compagnons `OK`), la fille vérifie **une fois** et l'écrit au journal :

```bash
# (A)
git -C "$M" fetch -q origin refs/heads/main:refs/remotes/origin/main; git -C "$M" rev-parse origin/main; date -u +%FT%TZ
REG=$(git -C "$M" show origin/main:registres/scellements-v1.md); printf '%s\n' "$REG" | grep -c '^| SCELLEMENT-T07 |'; printf '%s\n' "$REG" | grep -c '^| GO-ETAPE-A-T07 |'
[ "$(printf '%s\n' "$REG" | grep '^| SCELLEMENT-T07 |')" = "$(cat "$W/ligne-scellement-t07.txt")" ] && echo "SCELLEMENT-T07 inchangée"
LA=$(printf '%s\n' "$REG" | grep '^| GO-ETAPE-A-T07 |'); PA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$5); print $5}')
EX=$(git -C "$M" show "origin/main:$PA"); [ "$(git -C "$M" show "origin/main:$PA" | sha256sum | cut -d' ' -f1)" = "$HA" ] && [ "$(git -C "$M" show "origin/main:$PA.sha256" | cut -d' ' -f1)" = "$HA" ] && [ "$(printf '%s\n' "$EX" | grep -c '^| GO-')" = 1 ] && git -C "$M" show origin/main:registres/go.md | grep -qxF -- "$(printf '%s\n' "$EX" | grep '^| GO-')" && echo "GO-ETAPE-A-T07 conforme : $PA $HA"
```

- **Si** `1`, `1` et les deux messages (l'extrait est une ligne de `registres/go.md` : forme de T0.7, brouillon 19, table des clés) : **l'instance reste arrêtée** pour l'étape A ; la fille ne la redémarre pas et n'y joue rien ; l'étape A suit son ordre d'exécution, `docs/procedures/ordre-execution-etape-a-t07-v1.md` (empreinte `<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>`), et sa ligne de GO ; la fille détruit l'instance (§ 4.14) sur le mot de la mère (étape A finie, sorties poussées).
- **Sinon** (ligne absente ou non conforme ; fin anormale, arrêt, refus ; relance à créer) : **destruction** dès le rapatriement vérifié.
- **Dans tous les cas, au plus tard le 2026-11-16 à 23:00Z** : fin de la couverture de la dépense et avant la minuterie de l'amorce (17 novembre 00:00 UTC), qu'un redémarrage relancerait (amorce l. 111 à 127, 199, 213). La vérification n'est pas refaite : une ligne plus tardive ne garde pas l'instance.

### 4.14 Destruction par l'identifiant, inventaire final

```bash
# (A)
ID=<identifiant créé>; timeout -k 5 120 vastai destroy instance "$ID" -y; echo "code $?"
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>&1); c=$?; [ "$out" = '{"instances": null}' ] && echo "absente (texte exact), code $c" || echo "texte autre (non affiché), code $c"
bash "$W/inventaire.sh"
```

Du **seul identifiant créé**, après le rapatriement vérifié, forme de R-2039, au moment du § 4.13 ; toujours avant une seconde création (refusée tant qu'une instance `t06-v2…` existe). Le texte de `show instance` n'est jamais affiché.

## 5. Carte H200 NVL : seulement après un mot de Lazar dans la session de la fille

La fenêtre (GO-2026-11-07-02) et la relance de DT-6 restent telles quelles ; R-2077, articulé par la contre-lecture 6 (C6-3) : **`creation auto relance` n'est jouée qu'après un mot de Lazar**, au bout de la fenêtre comme après une erreur de mémoire ; l'attente est prévue.

1. **Cas** : (a) douze recherches A100 vides ; (b) arrêt consigné d'`etape` « données de distillation » ou « distillation » et de `motif` mémoire de la carte (« out of memory », « OutOfMemoryError »). Autre erreur, ou mémoire pendant les épisodes : compte rendu, nœud.
2. **Message à Lazar** (copie à la mère), format de décision, **sans défaut** (nœud de dépense) : décision (H200 NVL maintenant ?), enjeu (fenêtre vide ou erreur de mémoire, heures, dépense déjà faite), options ((a) H200 : ≈ 72 USD aux durées de 7a, ≈ 136 au débit moitié ; (b) nouvelle fenêtre A100, au plus tard 2026-11-15T20:48Z ; (c) rien).
3. **Attente** : rien n'est créé ; heure du message au journal ; après 2026-11-15T20:48Z, le mot doit accepter la création tardive (L11) ; le 16, rien.
4. **Sur le mot** (verbatim et heure au journal) : cas (a), même dossier, `ANT0` ; cas (b), A100 détruite d'abord (§ 4.14), dossier `$W/c7b-2`, branche `calcul/t06-confirmation-7b-v2` (§ 4.5), `controles` rejoué (§ 4.4, `D` et `B` neufs dans (A)), dépense antérieure **ANT1** = la plus grande de la facture de la tentative (si connue) et du cumul de la chaîne à sa destruction :

```bash
# (A) avec D et B de la première instance
python3 -I -B -c "import sys; sys.path.insert(0, '$M/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))" depense 200 "$(champ prix_carte)" "$(champ prix_stockage)" "$(champ creation)" "$(champ anterieure)" "$(champ telechargement_forfait)" <heure de la destruction en secondes>
```

   Puis `bash "$W/v13.sh" "$B" creation auto relance "<ANT0 ou ANT1>" "$D" > "$D/creation-sortie-$n.txt" 2>&1` (fichier neuf), § 4.9 (`carte relance`, `prix_carte` ≤ 4,70, branche en vigueur), § 4.10 à § 4.14. Sans offre H200 conforme : nœud (texte, point 9), aucune autre recherche sans mot.
5. **Relance A100 après une autre erreur de chaîne** (ligne A1 : avant tout épisode d'évaluation, code inchangé) : seulement sur addendum de la mère ; mécanique du point 4 (b), carte `course`.

## 6. Dépense

- **Engagement**, écrit et poussé par la mère avant la création (P6), texte du texte scellé (« Devis ») : « engagement : T0.6 organisme (ii), dose–réponse et test croisé, course de confirmation 7b (GO-2026-11-02-28, plafond 200 USD) : lanceur `scripts/lancer_t06_v13.sh` (empreintes : en-tête du préenregistrement scellé), commit du code cité `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` (l'instance clone le commit de scellement S, de même arbre gelé) ; une carte A100 SXM4 80 Go ≤ 1,30 USD de l'heure (DT-6 (a)), disque ≥ 150 Go ; attendu ≈ 16 à 26 USD, pire cas ≈ 151 USD (H200) ; dépense antérieure sous ce GO relevée au registre ; crédit Vast.ai relu à la création (recharge automatique, R-283) ». La chaîne ne lit pas le crédit ; l'ordre n'ajoute aucune commande pour le lire.
- **60 USD** : compte rendu à Lazar dans la session de la fille, une fois (heure, carte, instance, étape), copie à la mère ; **aucun arrêt**. **180 USD** : toute relance est un nœud de Lazar avant dépense. **200 USD** (tout compris, toutes tentatives, H200 comprise) : arrêt par la chaîne (`ARRET depense` ; minuterie de l'instance, amorce l. 101 à 110) ; § 4.12, § 4.14 ; aucune relance.
- **R10** : instances par leur identifiant, surveillance par son PID (`kill <PID>`), jamais par motif (`pkill`, `killall`) ; inventaire filtré avant la création et après la destruction.
- **Relevé** : cumul `session_v3 depense 200 …` à l'heure de l'arrêt, plus le stockage jusqu'à la destruction ; la facture, si connue, fait foi.

## 7. Bras B de l'audit de fuite (GO-2026-11-07-04) : joué par la chaîne, sur la même machine

- **Joué** par l'amorce après la poussée finale de T0.6, avant l'arrêt (l. 418 à 442, 553) : mode réel, aucune ligne d'épreuve, `BRAS_B` non posé ; ses pièces (`4fb0da20…`, `317a7ea5…`, `prereg/audit-fuite-r1-v4-v1.md` `910a53dc…`) sont dans S. **Non débrayable par la fille** (la commande de course ne le débraye pas, l. 234–235, et ne se change pas). Régi par le texte de l'audit (point 7), non par T0.6 ; jamais bloquant ; borne 2 400 s ; ≈ 20 min ; sorties à part sur la même branche, ni rapatriées ni ouvertes ; la fille relève `bras B : début …` et `bras B : code N en S s …`.
- **Conditions de GO-2026-11-07-04** (« code, essais et ordre contre-lus et scellés avant la course »), vérifiées en lecture seule (journal, § 2) :
  - **code et essais contre-lus : rempli** : R-1781 ; rapport `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md` (`09c202e62d4cd4d9af2c0100183ac9cffb90387025d784a81eeeb1df57d13a02`), § 2 « Bras B v4 conforme à GO-2026-11-08-01 » (0,3 borne incluse, lecture stricte, 44 essais, banc 21 sur 21) ; code dans l'arbre gelé cité par T0.6 ;
  - **addendum v3 scellé : non rempli** : sur `main`, seul le brouillon `docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md` (`2ec90141…`, « scellable après couples », R-1781) ; la copie après couples (`1a372523…`, « prête », R-1784) n'est que sur `fe240b24`, hors de `main` ; aucune ligne du registre n'en consigne le scellement ;
  - **cet ordre** : contre-lu et scellé avant la remise.
- **Règle** : sans la ligne de la mère qui consigne le scellement de l'addendum v3 (§ 14), **la fille ne crée rien avant un mot de Lazar sur ce point**, écrit dans sa session.

## 8. Arrêts

- Préalable manquant, empreinte différente, `controles` ≠ 0, garde mal jugée, commande non conforme : rien n'est créé ni exécuté ; compte rendu.
- Recherche vide : § 4.8, puis § 5. Autre code 3, code 2, ou code 4 après l'exécution : rien de plus ; inventaire ; compte rendu.
- `ARRET mort`, fin anormale (`fin, code 1` : suite en échec, tests ≠ 2022, arrêt consigné, installation, poussée), `ARRET garde`, `ARRET inventaire` (inventaire d'abord) : arrêt par l'identifiant si besoin ; § 4.12 ; § 5 si mémoire à la distillation ; sinon aucune relance sans écrit de la mère ; § 4.14.
- `REFUS` : la minuterie détruit ; inventaire ; § 4.12 si la branche existe. `ARRET depense` : § 6. `ALERTE` : compte rendu, aucun arrêt. Échéance du 17 à 00:00Z en marche : la minuterie consigne, pousse, détruit (l. 101 à 126) ; inventaire ; § 4.12.
- **Aucun couperet de temps** (GO-2026-11-02-28) : un run lent mais vivant n'est jamais arrêté.

## 9. Qui exécute ; levée bornée de l'interdit `vastai` ; secrets

- **La fille nommée en en-tête** exécute cet ordre sur la remise de Lazar ; tout mot neuf de Lazar (bras B, H200, création tardive) est écrit **dans sa session** et recopié verbatim, avec l'heure, au journal.
- **Levée de l'interdit `vastai`, bornée à** : les appels du lanceur ; la commande imprimée, **une fois** par création autorisée ; `stop` et `destroy … -y` du **seul identifiant créé**, puis un seul `show instance <ID> --raw` (code ou texte exact seulement) ; `inventaire.sh` ; `vastai --version`. **Rien d'autre** : jamais `start`, `reboot`, `copy`, `ssh`, `execute` (le redémarrage pour l'étape A relève de son ordre), ni geste sur une instance non créée par la fille.
- **Secrets** : clés par leur nom ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; jamais affichés `instances.json`, `offres.json`, `creation-brute.json` ; **garde des secrets à 0** (commande du § 4.9) avant tout envoi de texte ; aucune autre clé, aucun appel de modèle, aucune autre dépense.
- **Git** : rien écrit sur le dépôt distant par la fille ; refspec explicite ; clones `--single-branch`.
- **Arrêt de la fille avant la fin** : `lancement.txt` (garde des secrets à 0), identifiant, 50 dernières lignes de `progres.txt` et `surveillance.txt`, PID, envoyés à la mère et à Lazar ; surveillance arrêtée par son PID quand une autre session surveille ; la minuterie borne la dépense ; rien de neuf sans mot de Lazar dans la session qui dépense.

## 10. Compte rendu de la fille (nombres seuls, sans valeur de sonde ni de coût, ≤ 400 mots)

`vastai --version` ; P1 à P10 (valeurs, ligne `SCELLEMENT-T07`) ; heures et codes de `controles`, de la branche, des gardes ; chaque recherche ; mots de Lazar (verbatim, heure) ; carte, prix, identifiant, création, H60 ; PID de la surveillance ; dernière ligne de la suite ; durées par étape ; arrêt (`etape`, `motif`) ; `fin` et `stop` ; tête de la branche, fichiers ajoutés, compagnons ; run et manifeste ; bras B (code, durée) ; issue du § 4.13 ; dépense relevée ; destruction, inventaire final ; écarts. **Ni table A, ni sondes, ni résumé** (ni `ligne_A`, `ligne_B`, `ligne_C`). Journal (garde des secrets à 0) envoyé à la mère, qui le verse et le scelle.

## 11. Ce qui suit, et ce que cet ordre ne fait pas

- **Suite (hors de cet ordre)** : la mère verse journal et compte rendu, inscrit `RUN-CONFIRMATION-T06` et la dépense ; **table A** lue dans l'ordre du point 7 du plan par un lecteur neuf (réserve de mémoire de `run.err` comprise), verdict par un sous-agent neuf (R13), scellé, soumis à Lazar ; **règle « mots et coût »** après le scellement de T0.8, par des auteurs sans vue des données de 7b ; **sondes** (tables B et C) seulement après le verdict scellé de P3-bis et la lecture scellée des bases boîte noire de T0.8, par le contrôle d'ouverture v2 ; étape A de T0.7 par son ordre et son GO.
- **Ne fait pas** : aucune lecture de résultat ; aucune étape de T0.7 ; aucun contact externe ni appel de modèle ; aucune modification du code, du texte, de la configuration ou de la commande ; aucune chaîne v14 ; aucune fusion ni écriture de la fille sur le dépôt distant ; aucun geste sur une instance qu'elle n'a pas créée.

## 12. Devis et calendrier (texte scellé)

Attendu (A100, 13,59 h) ≈ **16 à 26 USD** ; bras B ≈ 20 min de carte ; pire cas P1 ≈ 46, P2 ≈ 86, P3 (mémoire puis H200) ≈ 151 ; H200 d'emblée ≈ 72 (durées de 7a), ≈ 136 (débit moitié). Seuils 60, 180, 200 USD. Première création au plus tard le 14 vers 17:00Z ; sans nœud au plus tard 2026-11-15T20:48Z ; destruction au plus tard 2026-11-16T23:00Z. L'étape A de T0.7 a son propre plafond (10 USD, brouillon 19).

## 13. À juger par la contre-lecture

1. **Forme d'exécution** (§ 4.10), gardée de 7a (R-1914) : la garde de la session ne voit pas `vastai create` dans `bash -c "$(tail -n 1 …)"` ; restent la garde rejouée par le lanceur sur le texte exact (l. 236) et le § 4.9 ; recopier environ 73 000 caractères risquerait d'altérer la commande.
2. **Bras B** (§ 7) : GO-2026-11-07-09 et -08-01 exigent l'addendum « avant toute lecture », non avant la course ; la règle de l'ordre est plus stricte, sur décision de la mère.
3. **Étape A** (§ 4.13) : vérification unique, sur les deux lignes nommées par la mère ; T0.7 exige aussi `RUN-CONFIRMATION-T06` et `SCELLEMENT-CONCEPTS-T07` pour l'ouvrir, sans effet sur la garde de l'instance.

## 14. Marqueurs (à remplir par la mère avant la contre-lecture ; une occurrence chacun)

| Marqueur (sans chevrons) | Où | Valeur |
|---|---|---|
| `ID_SESSION_FILLE` | en-tête | identifiant de la session fille |
| `DEPENSE_ANTERIEURE_USD` | ligne (A) | dépense inscrite sous GO-2026-11-02-28 et GO-2026-11-10-01 à la remise, en USD (attendu `0`) |
| `COMMIT_MAIN_REMISE` | § 4.1 | commit de `main` portant cet ordre scellé, `SCELLEMENT-T07` et l'engagement |
| `LIGNE_SCELLEMENT_T07` | § 4.3 | la ligne exacte de `registres/scellements-v1.md` (format de `scripts/controle_lecture_t06_v1.py`, commit `061ac380`) |
| `LIGNE_REGISTRE_BRAS_B` | § 4.3 | `R-NNNN` où la mère consigne le scellement de l'addendum v3 ; `AUCUNE` sinon |
| `EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07` | § 4.13 | sha256 de l'ordre d'exécution de l'étape A, scellé avant la course |

Sources, lignes et empreintes : journal.
