# Étape E de la réception v4 de R1 — rapport de l'exécutant neuf (v1)

- **Écrit par** un exécutant neuf (sous-agent, Claude Opus 5.5) pour conv-audit, consigne
  `docs/notes/runs-r1-r2-r4-v1/consigne-etape-E-reception-r1-v4-v1.md` (sha256
  `694f6f8e6e69678f0f9e9727b149d9323998ddc9ba0168892ae68baba984f323`, compagnon vérifié « OK » à 02:44 UTC). Je n'ai écrit
  ni la fiche, ni le vérificateur, ni l'addendum, ni fait les étapes B à D.
- **Fiche qui fait foi** : `fiche-reception-r1-v4-v2.md`, sha256
  `605931f3dba3a6f9aa413cbac924794b6ba6577627d571d61f8d86a34d2f638f` (compagnon vérifié « OK »), lue en entier.
- **Vérificateur employé** : `verifier_reception_r1_v4_v1.py` du dépôt de travail, sha256
  `3ea2352d57c7283420591fcbb8f6975aa4533fc2ee49257b1bb8703a2f4e93a4` (compagnon vérifié « OK »).
- Heures : `date -u`. Toute commande lancée sous `timeout 900 nice -n 10`. Aucun `git fetch` (les refs nommées étaient
  déjà au dépôt), aucun commit, aucun `.sha256`, aucune poussée, aucun modèle chargé, aucune dépense.

## Verdict de l'étape E

**Conforme.** Vérificateur : code 0, « RÉCEPTION CONFORME » ; tête de `refs/remotes/origin/calcul/r1-r2-reel-v1` égale à
l'identifiant annoncé `1d6bdc8dd30afe1e77bcfa38164b327ec5d37c52` ; `git merge-base --is-ancestor` vrai (code 0).

## 1. Références et ascendance (02:44:59 UTC)

```
git rev-parse refs/remotes/origin/calcul/r1-r2-reel-v1            → 1d6bdc8dd30afe1e77bcfa38164b327ec5d37c52
git rev-parse refs/remotes/origin/calcul/r1-v4-reparation-reel-v1 → 2b71248a0944399b4b0937fb1e49064192fb0767
git rev-parse refs/remotes/origin/prep/r1-relance-v4              → 5bd62a004279776c2718b3201c11001e16fa6527
git merge-base --is-ancestor 1d6bdc8d… refs/remotes/origin/calcul/r1-r2-reel-v1 → code 0 (vrai)
```

Commit C : un seul parent `d432f41f1395f551e0ccccad70ec36b8ec5036d9` ; son message nomme la branche source
`calcul/r1-v4-reparation-reel-v1` à `2b71248a…0767`, le témoin `5bd62a00`, les runs
`20261104-234729-r1-v4-reparation-reel` et `20261105-021737-r1-v4-rejeu-reel`, la fiche `605931f3…`, « 198 chemins,
aucun sous traces/ ». Tous égaux aux faits annoncés par la session de pilotage.

## 2. Arbres (02:45:12 UTC)

Bloc-notes `B = /tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/etape-E-r1-v4`.

```
git worktree add --detach $B/ARBRE 1d6bdc8dd30afe1e77bcfa38164b327ec5d37c52   (HEAD vérifiée = C, arbre propre)
git worktree add --detach $B/REC   5bd62a004279776c2718b3201c11001e16fa6527   (HEAD vérifiée = 5bd62a00)
```

`traces/` n'a été ni ouvert ni listé.

## 3. Recalcul de la section 7

**Pièces recopiées de C dans `<REC>`** (02:45:53 UTC), par `git show 1d6bdc8d…:<chemin> > $B/REC/<chemin>`, chacune
vérifiée par identifiant de blob (`git rev-parse C:<chemin>` = `git hash-object` de la copie) :

| chemin | blob |
|---|---|
| `runs/20261104-234729-r1-v4-reparation-reel/manifeste.json` | `93efe35f…` |
| `….sha256` | `c396d519…` |
| `diag/20261104-234729-r1-v4-reparation-reel/resolution-graine-lot-v3-reparation.json` | `2a416755…` |
| `….sha256` | `44734137…` |
| `prereg/R1-table-tokenisation-v4.json` | `6749f35b…` |
| `prereg/R1-table-tokenisation-v4.json.sha256` | `d4556ab6…` |

**Pièces de P3** : la configuration `prereg/R1-reparation-v4-config-v2.json` (sha256 `4d0655d1…85e5`, égal à la fiche)
cite `chemin_textes`, `chemin_scores`, `chemin_fiches`, `chemin_manifeste_p3`, `chemin_taches`, `chemin_consignes` ; les
six sont suivies au commit `5bd62a00` et déjà présentes dans `<REC>` à leurs chemins (tailles égales à celles du dépôt de
travail) ; rien n'a été copié en plus ; leurs empreintes sont revérifiées par le code.

**Tokeniseur** (02:46:22 UTC) : seuls `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json` de
`meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, par `hf_hub_download`
(`huggingface_hub` 1.33.0), sous
`env -i HF_TOKEN="$HF_TOKEN" HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt REQUESTS_CA_BUNDLE=/root/.ccr/ca-bundle.crt HF_HUB_DISABLE_TELEMETRY=1 .venv/bin/python -I …`
(clé passée par son nom, jamais affichée ; seule variable ajoutée hors liste : `HF_HUB_DISABLE_TELEMETRY=1`). Aucun poids.

| fichier | sha256 |
|---|---|
| `tokenizer.json` | **`79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`** (égal à l'attendu) |
| `tokenizer_config.json` | `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424` |
| `special_tokens_map.json` | `6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec` |

**Environnement du recalcul** : Python 3.13.18 (`.venv` du dépôt), `transformers` **5.18.0**, `tokenizers` **0.23.2**,
numpy 2.4.6.

**Commande** (02:46:30 → 02:48:03 UTC), exacte de la section 7, `<TOK>` = `$B/TOK`, `<HORS>` = `$B/HORS` :

```
cd $B/REC && PYTHONPATH=src timeout 900 nice -n 10 python -m controle_ia.runs_nuit.chaine_table_v4_v1 \
    --config prereg/R1-reparation-v4-config-v2.json \
    --reparation diag/20261104-234729-r1-v4-reparation-reel/resolution-graine-lot-v3-reparation.json \
    --table prereg/R1-table-tokenisation-v4.json --reception --tokeniseur $B/TOK \
    > $B/HORS/recalcul-reception-r1-v4.json 2> $B/HORS/recalcul-reception-r1-v4.err ; echo "code $?"
```

**Code de sortie du recalcul : 0.** Sortie (616 octets) et erreur standard (419 octets) ni affichées ni lues ; seul le
vérificateur a lu la sortie.

## 4. Vérificateur de la section 8

**Commande** (02:48:12 → 02:48:14 UTC), lancée depuis `/home/user/controle-ia-travail`, avec `python3 -I` (Python 3.13.18,
bibliothèque standard) :

```
timeout 900 nice -n 10 python3 -I docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/verifier_reception_r1_v4_v1.py verifier \
    --fiche docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/fiche-reception-r1-v4-v2.md \
    --fiche-sha256 605931f3dba3a6f9aa413cbac924794b6ba6577627d571d61f8d86a34d2f638f \
    --depot /home/user/controle-ia-travail --racine $B/ARBRE \
    --commit-versement 1d6bdc8dd30afe1e77bcfa38164b327ec5d37c52 \
    --source refs/remotes/origin/calcul/r1-v4-reparation-reel-v1 \
    --run-reparation 20261104-234729-r1-v4-reparation-reel --run-rejeu 20261105-021737-r1-v4-rejeu-reel \
    --scores-p3 /home/user/controle-ia-travail/donnees/20261019-230011-p3-reel/scores-p3.npz \
    --sortie-recalcul $B/HORS/recalcul-reception-r1-v4.json --racine-recalcul $B/REC
```

**Code de sortie : 0.** Sortie complète (sortie standard et erreur standard réunies, 265 octets) :

```
RÉCEPTION CONFORME ; gardes passées : fiche, runs, textes, versement, octets, presence, compagnon, temoin, reparation, table, chaine-locale, rejeu, commit-rejeu, rattachement, verdict, table-comparee, provenance, comptes, coherence-table, fichiers, npz, recalcul
```

Les 22 gardes, dans l'ordre de la section 8 de la fiche. Ni valeur de P-R5 ni compte de couverture dans cette sortie.

## 5. Non lu, nettoyage

- Aucun fichier de `runs/`, `diag/`, `donnees/`, aucun `.npz`, ni la sortie du recalcul n'a été ouvert, affiché ou
  résumé par moi ; seuls le recalcul et le vérificateur les ont lus. Rien sous `traces/`. Seuls des noms, tailles et
  identifiants de blob ont été relevés.
- 02:48:30 UTC : `git worktree remove --force` de `$B/ARBRE` et `$B/REC` (codes 0), `git worktree prune`, dossier du
  tokeniseur `$B/TOK` supprimé (empreinte gardée ci-dessus). Restent au bloc-notes : `$B/HORS/` (sortie du recalcul, non
  lue), `$B/scripts/tirer_tokeniseur.py`, la sortie du vérificateur. Disque libre revenu à 11 Go.
- Réserve d'écriture : ce rapport n'est ni scellé ni commité par moi (consigne : aucun `.sha256`, aucun commit).
