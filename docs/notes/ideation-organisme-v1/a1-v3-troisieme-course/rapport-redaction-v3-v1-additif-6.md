# Additif 6 au rapport de rédaction v3 — sonde v6 : mandataire du conteneur de la fille

Même rédacteur-développeur, 4 novembre 2026, de 22:52 à 23:08 UTC (`date -u`).

**Fait constaté par la fille** (22:48 et 22:51 UTC, deux passages, rien créé), relayé par le directeur :
- le trafic sortant de son conteneur passe par un mandataire qui réémet les certificats ;
- `ClientPilote._lancer` de la v5 ne transmettait à `vastai` que `PATH`, `HOME`, `LANG` et `VAST_API_KEY` ;
- l'appel échouait (« SSLCertVerificationError : self-signed certificate in certificate chain », code 1), et le marqueur de création
  incertaine était posé à tort.

Version 6 à noms neufs (R12) : les v1 à v5 sont inchangées. Elle porte **seulement** les points (a) à (d) de la demande. Mêmes
interdits : aucun commit, aucun `.sha256`, aucune location, aucune clé lue, aucune dépense.

**Verdict.** Les variables du mandataire, quand elles sont présentes, sont transmises à `vastai`. Une erreur de certificat ne pose
plus de marqueur, et toute autre erreur le pose toujours. **95 essais de la sonde v6 passent.** Résultat de l'ensemble : section 3.
**Un défaut voisin reste hors de la demande**, donc non corrigé (section 7).

## 1. Fichiers neufs (sha256 : section 4)

Copies renommées de la v5 (étiquette `sonde-a1-v3-v6`, branches `donnees/sonde-hote-durable-a1-v3-v6…`, dossier `/root/sonde-a1-v3-v6`,
fichiers `sonde-v6-*`), puis modifiées :
- `src/controle_ia/sonde_hote_durable_a1_v3_v6.py` ;
- `scripts/amorce_sonde_hote_durable_a1_v3_v6.sh` : seuls les noms changent ;
- `tests/test_sonde_hote_durable_a1_v3_v6.py` : 95 essais, soit les 86 de la v5 et 9 neufs.

## 2. Ce qui change, et rien d'autre (diff exact : section 5)

**(a) Variables du mandataire.**
- `_lancer` transmet aussi `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE`, mais seulement s'ils sont
  présents et non vides dans l'environnement reçu (`VARIABLES_MANDATAIRE`).
- Aucune autre variable n'est transmise.
- Leurs valeurs sont masquées dans tout journal du pilote, comme les secrets : elles sont ajoutées à `SECRETS_PILOTE`.

**(b) Erreur de certificat.**
- La sortie d'erreur de `vastai` est captée, mais seulement pour y chercher « CERTIFICATE_VERIFY_FAILED » ou « SSLCertVerificationError »
  (`MOTS_CERTIFICAT`). Elle est oubliée aussitôt et n'est jamais écrite.
- Si le code de sortie est non nul et qu'un de ces mots est présent, l'appel lève
  `RefusCertificat("vastai … : appel non parvenu à Vast (certificat) ; code N")`. C'est une sous-classe de `RefusAvantAppel` :
  **aucun marqueur** de création incertaine n'est posé.
- Toute autre erreur garde le marqueur (m-1).

**(c) Commande** : les trois variables sont ajoutées à chaque `env -i` (section 6).

**(d) Essais.**
- Cas sain : les cinq variables, présentes, arrivent à `vastai`. La valeur de `HTTPS_PROXY` est vue par l'outil, qui ne voit rien
  d'autre que les variables permises.
- Artefacts :
  - une variable absente ou vide n'est pas inventée ;
  - `AUTRE_VARIABLE` et `GH_TOKEN` ne passent pas dans l'environnement de l'outil ;
  - le mot de passe du mandataire n'apparaît pas au journal de location.
- Erreur de certificat (trois formes) : refus « certificat », aucun marqueur, rien de la sortie d'erreur au journal, et une location
  reste possible ensuite.
- Autre erreur (trois formes, dont « certificat » écrit en français seulement) : marqueur posé.

## 3. Essais (`timeout 900 nice -n 10`, aucun réseau)

- `tests/test_sonde_hote_durable_a1_v3_v6.py` : **95 passés**.
- Ensemble (v6 à v1, lanceur durable, garde de calcul) : **476 passés**, aucun sauté, en 821 s
  (95 + 86 + 72 + 66 + 52 + 19 + 49 + 37). Sortie : `…/sorties/essais-sonde-v6.txt`
  (`dcf201eac01f553d4f807c062deade7779dbe9b65b39c021646d10583a9feec2`).

## 4. Empreintes à la remise

Relevées à 23:07 UTC.

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3_v6.py` (777 lignes) | `205d03da9205de4cabc0a1aaca014e5bb73f239e7a42b52e31e22db55fa40ab6` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v6.sh` | `4909b6e990bd3ae9811bacae446fc46c382337f56607cc226bd187d2739ffe96` |
| `tests/test_sonde_hote_durable_a1_v3_v6.py` (95 essais) | `63c09474cfd4aa1fde5a66411fd9f3f920fccf712ad94db0b80db5db1089038f` |
| bloc-notes `sorties/essais-sonde-v6.txt` | `dcf201eac01f553d4f807c062deade7779dbe9b65b39c021646d10583a9feec2` |
| bloc-notes `sorties/diff-sonde-v5-vers-v6-brut.txt` | `057b2cb97f33b8236df6d00d6676a87bf2d0d00f7991cd9b8a563087c2ea8083` |
| bloc-notes `sorties/diff-sonde-v5-vers-v6-hors-renommage.txt` | `aafdf5728bbcf9414a9e1041a9649597eccabc3a1933c6564dcc93c4d3a088b9` |

Ce fichier ne porte pas sa propre empreinte : elle est donnée avec la remise. Les instantanés versés pendant le travail sont
intermédiaires ; seules ces empreintes valent pour le rendu.

## 5. Diff exact par rapport à la v5

Les deux diffs sont dans le bloc-notes `/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/v3b1/sorties/` :
- `diff-sonde-v5-vers-v6-brut.txt` : renommages compris ;
- `diff-sonde-v5-vers-v6-hors-renommage.txt` : la v5 renommée par le même `sed`, comparée à la v6.

Le second ne contient que les points (a), (b) et (d).

**Module :**
- paragraphe de tête ;
- `VARIABLES_MANDATAIRE`, `MOTS_CERTIFICAT` et `SECRETS_PILOTE` étendu ;
- classe `RefusCertificat` ;
- dans `_lancer` :
  - l'environnement étendu aux variables du mandataire présentes ;
  - `stderr=subprocess.PIPE` au lieu de `DEVNULL` ;
  - la recherche des deux mots, puis l'oubli de la sortie d'erreur ;
  - le refus « certificat ».

**Amorce :** aucune ligne, hors renommage.

**Essais :** le titre et les 9 essais neufs.

## 6. Commande exacte de la sonde v6, pour la fille

Préalables :
- crédit de Vast rechargé (R-1483) ;
- `vastai --version` rend `1.8.3` ;
- sonde v6 committée sur `main` du dépôt privé ;
- rien d'autre ne tourne sous GO-2026-11-04-09.

L'exposition du jeton est acceptée pour la seule sonde (R-1484). Mode tir recommandé ; borne : 0,37 USD au plus.

Les trois variables ajoutées à chaque `env -i` sont `HTTPS_PROXY`, `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE`. `vastai` passe par
`requests`, qui lit `REQUESTS_CA_BUNDLE`, et non `SSL_CERT_FILE`. À défaut, `REQUESTS_CA_BUNDLE` prend donc la valeur de
`SSL_CERT_FILE`. Une variable vide n'est pas transmise. Si le conteneur de la fille pose aussi `NO_PROXY` ou `HTTP_PROXY`, les
ajouter de même : le code les transmet.

```
COMMIT_PRIVE=<hash complet de 40 caractères donné par le directeur>
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-sonde-a1-v3-v6; mkdir "$D" || exit 2                      # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v6.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=0 rentable=true reliability>=0.98 cpu_cores_effective>=4 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/sonde_hote_durable_a1_v3_v6.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-04-09 env -i GO_ID=GO-2026-11-04-09 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
        GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/sonde_hote_durable_a1_v3_v6.py" louer --go GO-2026-11-04-09 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-s 1200 --tir-minuterie \
          --journal-local "$D/journal-location-sonde-v6.log" $V || exit 2
    done
```

Après la création, les étapes et les critères de réussite sont ceux de l'additif 5 (section 6), lus en `sonde-a1-v3-v6`. Le contrôle :

```
D=/home/user/hors-clone-sonde-a1-v3-v6
env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
  GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" \
  timeout 900 nice -n 10 python3 -I -B "$D/sonde_hote_durable_a1_v3_v6.py" controler \
    --etat "$D/journal-location-sonde-v6.log.etat.json" --journal-local "$D/journal-controle-sonde-v6.log"
```

## 7. Défaut voisin, hors de la demande, non corrigé : à trancher

Dans `controler`, la recherche du signe de vie (`branche_existe`) lance `git ls-remote` avec un environnement réduit à `PATH`, `HOME`,
`GH_TOKEN` et `GIT_TERMINAL_PROMPT`. Les variables du mandataire n'y sont pas, et il n'y a pas de magasin de certificats.

Dans le conteneur de la fille, cet appel échouera probablement comme `vastai`. `branche_existe` rend alors **faux**, sans délai ni
exception. `controler` en conclut « aucun signe de vie » et, à partir de T0 + 30 min, **détruit une machine saine** par son
identifiant.

Ce n'est pas une fuite : la sonde est factice. Mais le tir de la minuterie serait devancé, et l'objet de la sonde manqué.

Deux corrections sont possibles, dans une version 7 :
- transmettre les mêmes variables à `git ls-remote` ;
- traiter un échec de `ls-remote` comme le code 6 (« recontrôler »), et non comme une absence de signe de vie.

En attendant, la fille peut lancer `controler` seulement après T0 + 70 min, sans risque : la machine est détruite par la minuterie à
T0 + 40.
