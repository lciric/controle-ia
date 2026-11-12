# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 3

> **VARIANTE B** (décision de la mère, R-2112, sur le point bloquant PB-1 du brouillon 1) : l'étape A ne se joue pas sur
> l'instance de 7b. Une instance **A100 neuve**, créée par la fille après la course de 7b et la poussée de ses résultats,
> clone le code de T0.7, récupère la sortie de 7b par refspec explicite, **recalcule les activations** (repli, garde
> d'équivalence), puis joue la passe à blanc et l'étape A, pousse ses sorties sur une branche neuve et s'arrête ; la fille la
> détruit par son identifiant. **Ligne de GO : GO-2026-11-10-06** (mot de Lazar, R-2115 ; 20 USD).

- **Statut** : brouillon 3, écrit le 2026-11-10 à partir de 09:40 UTC (`date -u`) par le développeur du module de T0.7 (sous-agent
  de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), auteur du code et du script qu'il fait jouer (R2 : la
  contre-lecture revient à un sous-agent neuf). Remplace le brouillon 2 (`a0d75ce1…`, gardé tel quel, R12) après la contre-lecture
  différentielle du code (`dd794e2e…`) : **DF-01** (le repli joue la garde d'ouverture avant tout recalcul, recalcule sous un nom
  daté, scelle son rapport à côté des activations, reprend sur un recalcul couvert, se relance sous un nom neuf), **DF-02**
  (`CODE-T07` contrôlée aussi par la passe à blanc et l'étape B, sur tout `src/controle_ia/`, arbre de travail propre exigé),
  **DF-04** (la passe à blanc juge la mémoire de la notation) ; script de l'instance à son empreinte neuve, répété de nouveau
  (§ 11). Le brouillon 1 (`bd7d03b8…`) reste tel quel. **Non contre-lu.**
- **Texte qui régit l'étape** : le préenregistrement scellé de T0.7 (`prereg/T0.7-sondes-v0-v1.md`, ligne `SCELLEMENT-T07`),
  « Calcul et dépense » (variante B : « instance A100 SXM4 80 Go ≤ 1,30 USD de l'heure […] descente du modèle […] recalcul des
  activations (point 8, repli) ») ; « Écrits exigés par P3-bis » (b) 2 « Variante B » (même code, même configuration, même règle
  de `sondes_lues`) ; ligne de registre **`GO-LECTURE-T07`** (« extrait scellé de la ligne du GO cité pour la variante B ») ;
  DS-3 bis (a), R-2104 : ligne **`CODE-T07`**.
- **Autorisation** : **GO-2026-11-10-06** (calcul, Lazar ; R-2115 ; `registres/go.md` de `main`) : **20 USD, non cumulés avec
  GO-2026-11-10-04** ; instance A100, **la H200 seulement après un mot de Lazar** ; échéance le **2026-11-23** ; périmètre :
  recalcul des activations depuis la sortie poussée de 7b, puis passe à blanc et étape A. GO-2026-11-10-04 (étape A sur l'instance
  de 7b) ne couvre pas cette instance ; la délégation GO-2026-10-20-07 (≤ 10 USD par lancement) ne couvre pas le pire cas du devis
  (§ 6).
- **Exécutante** : la fille porteuse des clés (Vast.ai, GitHub, Hugging Face), session `<<ID_SESSION_FILLE>>` ; journal
  `journal-etape-a-t07-b-v1.md`, une ligne datée par geste (`date -u`).

## 0. Objet

Après la fin normale de 7b et la poussée vérifiée de ses résultats : créer une instance A100 neuve qui joue, sans autre geste de la
fille que la surveillance, le script `scripts/etape_a_t07_variante_b_v1.sh` (§ 5) : clone partiel du code de T0.7 au commit de
scellement S7 ; registres et fichiers cités recopiés de `main` ; sortie de 7b récupérée par refspec explicite (fichiers nommés) ;
essais figés ; puis, **dans cet ordre** : **`CODE-T07`** (inscrite par la mère avant la création, contrôlée sur l'instance),
**repli** (recalcul des activations, garde d'équivalence), **passe à blanc**, **étape A** ; poussée sur une branche neuve ; arrêt.
La fille vérifie la poussée et **détruit l'instance par son identifiant** (R10). Ni épisode, ni étape B, ni lecture d'un résultat.

## 1. Cadre

| Élément | Valeur |
|---|---|
| Code de T0.7 | C7 (commit du code contre-lu et répété en jouet) et S7 (commit de scellement de T0.7, descendant de C7, `git diff --quiet C7 S7 -- src tests`, ancêtre de `main`), comme la voie B de T0.6 ; contrôlés sur l'instance |
| Script de l'instance | `scripts/etape_a_t07_variante_b_v1.sh`, sha256 `99e4c92611c2f161249499816c29fbba52553165a33fb3b3e86c47a7fdbc6a0f` (commit `8ae9fc44`) ; **répété en jouet sur une racine locale** (§ 11) |
| Configuration | fichier JSON scellé dans S7 (brouillon : `configuration-t07-v4.json`, `code_t07_exige` vrai, `enonces_reserve`) ; empreinte canonique `<<EMPREINTE_CONFIG_T07>>`, revérifiée sur l'instance |
| Course lue | 7b : run `RUN6`, branche `BR7B` (`calcul/t06-confirmation-7b-v1`, ou `-v2`, `-v3`), lue par refspec explicite |
| Machine | une **A100 SXM4 80 Go**, ≤ 1,30 USD de l'heure ; filtre de la chaîne de T0.6 (`session_v7.filtre_recherche`, `1609a4bf` : `reliability>=0.98`, `inet_down>=500`, `cuda_max_good>=13.0`) ; ≥ 16 cœurs, ≥ 128 Go de mémoire vive ; **disque 100 Go** (modèle ≈ 16 Go, paquets ≈ 10 Go, activations recalculées ≈ 31,5 Go) ; image `python:3.11-bookworm` ; étiquette `t07-b-v1` ; mode « args » (aucun serveur SSH : tout passe par le script) ; **H200 seulement après un mot de Lazar** (GO-2026-11-10-06), hors de cet ordre : devis et ordre à refaire |
| Dossier de la fille | `/home/user/etape-a-t07-b-v1/` (neuf ; `-v2` à une reprise) |
| Branche de sortie | **`donnees/t07-etape-a-v1`**, absente du dépôt distant avant la première poussée (contrôlé par le script) ; sinon `-v2` ; jamais `main`, jamais une branche `calcul/…` |
| Dépôt | `https://github.com/lciric/controle-ia-travail.git`, en dur dans le script hors essai ; jamais `lciric/controle-ia` |
| Échéances | création après la poussée vérifiée de 7b et les lignes du § 3, au plus tard le **2026-11-22 à 12:00Z** (la minuterie tombe alors avant la fin de GO-2026-11-10-06, le 23) ; **minuterie de l'instance** : destruction par son identifiant à `création + 12 h` (§ 6) ; la fille détruit dès la poussée vérifiée |

## 2. Embargos et chemins interdits

1. **Jamais** la fille ni l'instance n'ouvrent, n'affichent, ne copient, ne hachent ni ne passent à un outil un
   `lecture-sondes-t06.json` (de 7b, de 7a, d'aucun run) ni son compagnon. Sur l'instance, la branche de 7b est lue par refspec
   explicite dans un **clone partiel** (`--filter=blob:none`) : seuls les fichiers **nommés** sont extraits (`runs/<run>/manifeste.json`,
   `diag/<run>/episodes-t06.json`, `diag/<run>/distillation-t06.json`, `diag/<run>/arret.json` s'il existe, et, dans `donnees/<run>/`,
   adaptateurs, mesures, textes, manifeste et morceaux du sous-ensemble) ; `diag/<run>/` n'est jamais listé ; le contenu de
   `lecture-sondes-t06.json` **n'est jamais descendu** (objet manquant du clone partiel, vérifié par la répétition, § 11) ; le
   script s'arrête s'il le trouve dans l'arbre.
2. **Jamais** `donnees/lecture-b-7a-quarantaine-v1`, la branche `essai/t06-explo-v3`, ni `diag/`, `runs/`, `donnees/` de 7a ;
   clones de la **seule branche `main`** (`--single-branch`), `git fetch` par refspec explicite.
3. **Jamais** `scripts/extraire_mesures_epreuve_t06_v1.py`, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
   `docs/notes/bras-attaque/`, l'étiqueteur ; tout chemin interdit cité par un registre arrête le script ; **règle 9** : aucune
   recherche récursive sur un arbre qui contient un chemin interdit sans l'exclure (`git grep` avec exclusions) ; jamais
   `verifier-arbre`.
4. **Aucune lecture de résultat de 7b** : `lecture-cout-t06.json`, `resume.json`, `distillation-t06.json`, `episodes-t06.json`,
   `run.err` jamais affichés (le module de T0.7 lit ce qu'il lui faut ; la fille, rien).
5. **Aucune lecture des sorties de l'étape A** (`scores-actions-t07.npz`, `sondes-t07.json`, `ouverture-t07.json`,
   `notation-t07.json`, `sondes-neuves-t07.npz`, `temoins-lexicaux-t07.json`, manifeste du run de T0.7) : hachées, jamais
   affichées. Le rapport du repli et la sortie de la passe à blanc, sans donnée décisive, peuvent être lus ; la fille n'en recopie
   que les champs du § 8.
6. **Aucune sortie de P3-bis lue ni citée** : seul le module lit, par sa garde, les registres de P3-bis (présence, date, sceau).
7. **Secrets** : clés par leur nom (`HF_TOKEN`, jeton GitHub) ; jamais `env`, `printenv`, `set` sans argument, `export -p`,
   `/proc/*/environ` ; jamais affichés `creation-brute.json`, `offres.json`, `instances.json` ; garde des secrets à 0 avant tout
   envoi de texte.

## 3. Préalables bloquants (vérifiés par la fille, écrits au journal avec l'heure)

| # | Préalable | Où | Sinon |
|---|---|---|---|
| P1 | **Course 7b** : fin normale, branche `BR7B` poussée, rapatriement vérifié (compte rendu de la fille de 7b) ; l'instance de 7b n'est pas gardée pour T0.7 (détruite selon son ordre) | compte rendu | rien |
| P2 | **`RUN-CONFIRMATION-T06`** au registre de `main`, chemin `runs/<RUN6>/manifeste.json` ; **le même fichier** sur `BR7B` (empreinte égale) | § 4.1 | attente |
| P3 | **`SCELLEMENT-CONCEPTS-T07`** (`donnees/t07-concepts-v1/phrases-concepts-v1.jsonl`) ; lignes des jeux permises, au plus une chacune (`donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`, `…/intention-autres-modes-v2.jsonl`, `donnees/t07-jeux-synthetiques-v3/domaine-cout-v3.jsonl` s'il est scellé), fichiers, compagnons et journaux du script sur `main` | § 4.1 | attente (concepts) ; jeu sans ligne : repli du texte |
| P4 | **`GO-LECTURE-T07`** : une ligne ; son extrait scellé est une ligne de `registres/go.md` et nomme `GO` (ligne (A)) ; non révoquée, non échue ; aucune ligne `GO-ETAPE-A-T07` (étape annexe abandonnée sur 7b) ou, si elle existe, la garde lira l'une ou l'autre (écrit au journal) | § 4.1 | rien |
| P5 | **`SCELLEMENT-T07`** : une ligne, égale à `<<LIGNE_SCELLEMENT_T07>>` | § 4.1 | arrêt, nœud |
| P6 | **`CODE-T07`** : une ligne, inscrite par la mère avant la création (`python -m controle_ia.t07.code_t07_v1 ecrire <clone> C7 registres/code-t07/CODE-T07-v1.json`, scellé), citant C7 | § 4.1 | rien |
| P7 | `SCORES-T07`, `SONDES-T07` absentes ; `VERDICT-P3BIS` et le journal de P3-bis relevés (présence, date), jugés par la garde | § 4.1 | arrêt, nœud |
| P8 | **Engagement** de dépense sous `GO` au registre des dépenses (mère) ; dépense antérieure sous cette ligne : `ANT0` | § 4.1 | rien |
| P9 | **Code** : S7 descend de C7, arbre gelé égal, S7 ancêtre de `main` ; script de l'instance à son empreinte (§ 1) | § 4.1 | arrêt |
| P10 | `vastai` 1.8.3 ; `HF_TOKEN` et le jeton GitHub présents (par le nom) ; inventaire : aucune instance d'étiquette `t07…` | § 4.2 | arrêt |
| P11 | **Heure** : création au plus tard le 2026-11-22 à 12:00Z | `date -u` | nœud |

## 4. Étapes et commandes (session de la fille)

L'état du shell ne survit pas d'une commande à l'autre : **chaque bloc commence par la ligne (A)**. Les clés passent par leur nom.

**(A)** :

```bash
W=/home/user/etape-a-t07-b-v1; M=$W/main; J=$W/journal-etape-a-t07-b-v1.md; GO=GO-2026-11-10-06; PLAF=20; ANT0=<<DEPENSE_ANTERIEURE_USD>>; RUN6=<<RUN_T06_7B>>; BR7B=<<BRANCHE_7B>>; C7=<<COMMIT_CODE_T07>>; S7=<<COMMIT_SCELLEMENT_T07>>; CFG=<<CHEMIN_CONFIG_T07>>; ATT='<<LIGNE_ESSAIS_T07>>'; BR=donnees/t07-etape-a-v1; SCRIPT=scripts/etape_a_t07_variante_b_v1.sh; SHA_SCRIPT=99e4c92611c2f161249499816c29fbba52553165a33fb3b3e86c47a7fdbc6a0f; URL=https://github.com/lciric/controle-ia-travail.git; j() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }
```

### 4.1 Préalables depuis `main` (lecture seule)

```bash
# (A)
mkdir -p "$W" && git clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$M" && git -C "$M" sparse-checkout set --no-cone '/registres/*.md' '/registres/go-extraits/' '/registres/code-t07/' '/scripts/etape_a_t07_variante_b_v1.sh' && git -C "$M" checkout -q main && git -C "$M" rev-parse HEAD; j "main $(git -C "$M" rev-parse HEAD)"
REG="$M/registres/scellements-v1.md"; for k in RUN-CONFIRMATION-T06 SCELLEMENT-CONCEPTS-T07 GO-LECTURE-T07 GO-ETAPE-A-T07 SCELLEMENT-T07 CODE-T07 SCORES-T07 SONDES-T07 VERDICT-P3BIS; do printf '%s %s\n' "$k" "$(grep -c "^| $k |" "$REG")"; done
LR=$(grep '^| RUN-CONFIRMATION-T06 |' "$REG"); PR=$(printf '%s\n' "$LR" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HR=$(printf '%s\n' "$LR" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$PR" = "runs/$RUN6/manifeste.json" ] && git -C "$M" fetch -q origin "refs/heads/$BR7B:refs/remotes/origin/$BR7B" && [ "$(git -C "$M" show "refs/remotes/origin/$BR7B:$PR" | sha256sum | cut -d' ' -f1)" = "$HR" ] && echo "RUN-CONFIRMATION-T06 conforme à $BR7B"
LA=$(grep '^| GO-LECTURE-T07 |' "$REG"); PA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$4); print $4}'); HA=$(printf '%s\n' "$LA" | awk -F'|' '{gsub(/ /,"",$5); print $5}'); [ "$(sha256sum < "$M/$PA" | cut -d' ' -f1)" = "$HA" ] && [ "$(cut -d' ' -f1 "$M/$PA.sha256")" = "$HA" ] && [ "$(grep -c '^| GO-' "$M/$PA")" = 1 ] && grep -qxF -- "$(grep '^| GO-' "$M/$PA")" "$M/registres/go.md" && grep -q "^| $GO |" "$M/$PA" && echo "GO-LECTURE-T07 conforme ($GO)"
[ "$(grep '^| SCELLEMENT-T07 |' "$REG")" = "$(cat "$W/ligne-scellement-t07.txt")" ] && echo "SCELLEMENT-T07 inchangée"
grep -c "$GO" "$M/registres/depenses.md"
git -C "$M" merge-base --is-ancestor "$C7" "$S7" && git -C "$M" diff --quiet "$C7" "$S7" -- src tests && git -C "$M" merge-base --is-ancestor "$S7" HEAD && [ "$(sha256sum < "$M/$SCRIPT" | cut -d' ' -f1)" = "$SHA_SCRIPT" ] && echo "code et script conformes"
```

Attendus : `1` pour `RUN-CONFIRMATION-T06`, `SCELLEMENT-CONCEPTS-T07`, `GO-LECTURE-T07`, `SCELLEMENT-T07`, `CODE-T07` ; `0` pour
`SCORES-T07`, `SONDES-T07` ; `GO-ETAPE-A-T07` et `VERDICT-P3BIS` relevés ; les quatre messages ; au moins une ligne
d'engagement. `ligne-scellement-t07.txt` : la ligne `SCELLEMENT-T07` (P5), écrite à l'octet par la fille au début. La branche de
7b est lue **par refspec**, dans un clone partiel, et seul le manifeste y est lu (empreinte, jamais affiché).

### 4.2 Outil et inventaire

```bash
# (A)
vastai --version; date -u +%FT%TZ
timeout -k 5 120 vastai show instances --raw 2>/dev/null | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; print([(i.get("id"), i.get("label"), i.get("actual_status")) for i in (d or []) if str(i.get("label") or "").startswith(("t06", "t07"))])'
```

Seuls l'identifiant, l'étiquette et l'état des instances `t06…` et `t07…` sont imprimés. Attendu : aucune `t07…`.

### 4.3 Recherche de l'offre

```bash
# (A)
timeout -k 5 120 vastai search offers 'num_gpus=1 rentable=true gpu_name=A100_SXM4 reliability>=0.98 inet_down>=500 cuda_max_good>=13.0 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=100 dph_total<=1.3' -o dph_total --storage 100 --raw > "$W/offres.json" 2>"$W/offres.err"; echo "code $?"
python3 -I -c 'import json,sys; o=json.load(open(sys.argv[1])); o=o.get("offers", o) if isinstance(o, dict) else o; o=[x for x in o if x.get("gpu_name")=="A100 SXM4" and x.get("num_gpus")==1 and float(x.get("dph_total",9))<=1.3 and float(x.get("gpu_ram",0))>=79000]; x=o[0] if o else None; print("aucune offre" if x is None else "id=%s carte=%s prix_h=%.4f stockage_h=%s machine=%s cuda=%s offres=%d" % (x["id"], x["gpu_name"], float(x["dph_total"]), x.get("storage_total_cost"), x.get("machine_id"), x.get("cuda_max_good"), len(o)))' "$W/offres.json"
```

Au plus **trois** recherches, espacées d'au moins 30 minutes ; vides : compte rendu, nœud (aucune autre carte sans mot). Le prix
horaire relevé (`prix_h`, carte et disque compris) entre au relevé de dépense (§ 6) ; `offres.json` n'est jamais affiché.

### 4.4 Création, une fois

```bash
# (A) ; OFFRE = l'id de la ligne imprimée au § 4.3
B64=$(base64 -w0 < "$M/$SCRIPT"); [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$SHA_SCRIPT" ] || echo "ÉCART : encodage du script"
TC=$(date +%s); ECH=$((TC + 43200)); j "création demandée, TC=$TC, échéance de la minuterie $ECH"
GO_ID=$GO timeout -k 10 300 vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 100 --cancel-unavail --label t07-b-v1 --env "-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" --entrypoint bash --args -c "echo $B64 | base64 -d > /root/etape-a-t07-b.sh && bash /root/etape-a-t07-b.sh $S7 $C7 $RUN6 $CFG $BR $BR7B '$ATT' $ECH" > "$W/creation-brute.json" 2>&1; echo "code $?"
python3 -I -c 'import json,sys; d=json.load(open(sys.argv[1])); print("succès :", d.get("success"), "; identifiant :", d.get("new_contract"))' "$W/creation-brute.json"
```

`GO_ID=$GO` en tête : la garde de calcul de la session exige un GO valide de `registres/go.md` dans la commande. L'identifiant
imprimé devient `ID` (écrit au journal) ; `creation-brute.json` n'est jamais affiché. Création incertaine (code ≠ 0 sans
identifiant) : inventaire (§ 4.2) avant tout autre geste ; **aucune seconde création** sans écrit de la mère.

### 4.5 Surveillance (toutes les 15 minutes ; aucun couperet de temps)

```bash
# (A) ; ID et TC du journal
timeout -k 5 120 vastai logs "$ID" --tail 400 2>/dev/null | grep -E '^[0-9TZ:-]+ T07 ' | tail -n 20
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>/dev/null); printf '%s' "$out" | python3 -I -c 'import json,sys; d=json.load(sys.stdin); d=d.get("instances", d) if isinstance(d, dict) else d; d=d[0] if isinstance(d, list) else d; print("état :", d.get("actual_status"), "/", d.get("intended_status"))'
python3 -I -c 'import sys,time; p,tc,ant=map(float,sys.argv[1:4]); h=(time.time()-tc)/3600; c=ant+p*h+1.2; print(f"cumul ≈ {c:.2f} USD (carte et disque {p*h:.2f}, téléchargement borné 1,20, antérieur {ant:.2f}) ; projeté + 15 min {c+p/4:.2f}")' "$PRIX_H" "$TC" "$ANT0"
```

Seules les lignes `… T07 …` du script sont lues (jamais d'état de sonde, d'aire ni de score : le script n'en imprime aucun).
Attendu, dans l'ordre : minuterie lancée ; carte ; code conforme ; registres recopiés ; les quatre lignes ; sortie de 7b
extraite ; essais (dernière ligne égale à `ATT`) ; configuration ; `CODE-T07 conforme` ; repli, essai 1, code 0 (« recalcul
fait ») ; trois « poussé » ; `FIN`. Une ligne `ARRET` : § 7.

### 4.6 Vérification de la poussée (sans rien rapatrier des sorties)

```bash
# (A)
git -C "$M" ls-remote origin "refs/heads/$BR"; git -C "$M" fetch -q origin "refs/heads/$BR:refs/remotes/origin/$BR" && git -C "$M" log --format=%s "$S7..origin/$BR" | head -n 5 && git -C "$M" diff --stat "$S7" "origin/$BR" -- src tests | tail -n 1
R7=refs/remotes/origin/$BR; for f in $(git -C "$M" diff --name-only --diff-filter=A "$S7" "$R7" -- replis-t07 passes-blanches-t07 runs diag donnees | grep -v '\.sha256$' | grep -v 'lecture-sondes-t06'); do a=$(git -C "$M" show "$R7:$f" | sha256sum | cut -d' ' -f1); b=$(git -C "$M" show "$R7:$f.sha256" 2>/dev/null | cut -d' ' -f1); [ "$a" = "$b" ] && echo "OK $f" || echo "ÉCART $f"; done
git -C "$M" show "$R7:registres/scellements-v1.md" | grep -E '^\| (SCORES|SONDES)-T07 \|' | cut -d'|' -f2,3
```

Attendu : trois commits (garde et repli, passe à blanc, étape A), **aucun changement sous `src` ni `tests`**, `OK` pour chaque
fichier **ajouté par l'instance** (seuls ceux-là sont hachés ; jamais un fichier venu de `main` ou de 7b ; le rapport du repli est
`donnees/<run>/activations/rapport-repli-t07.json`, les activations elles-mêmes ne sont jamais poussées), et les deux lignes
`SCORES-T07`, `SONDES-T07` (clé et date seulement).

### 4.7 Arrêt et destruction par l'identifiant (R10), inventaire final

```bash
# (A)
timeout -k 5 120 vastai destroy instance "$ID" -y; echo "code $?"; j "destruction demandée ($ID)"
out=$(timeout -k 5 120 vastai show instance "$ID" --raw 2>&1); c=$?; [ "$out" = '{"instances": null}' ] && echo "absente (texte exact), code $c" || echo "texte autre (non affiché), code $c"
```

Dès la poussée vérifiée (§ 4.6), ou sur un `ARRET` une fois ses traces poussées, ou à l'atteinte du plafond (§ 6). Le script
demande de lui-même l'état « stopped » à sa fin (`FIN` ou `ARRET`) ; la minuterie détruit l'instance à `ECH` si la fille ne
l'a pas fait. Du **seul identifiant créé** ; jamais `pkill`, `killall`, ni un geste sur une autre instance ; inventaire du § 4.2
après.

## 5. Ce que joue l'instance (`scripts/etape_a_t07_variante_b_v1.sh`, `99e4c926…`)

0. **Minuterie** : destruction de l'instance par son identifiant (`CONTAINER_ID`, API de Vast) à `ECH` (échéance bornée à 24 h).
1. **Machine** : outils, jetons par leur nom, carte visible (`nvidia-smi`).
2. **Code** : clone partiel de la seule branche `main`, extraction partielle (chemins utiles et chemins cités par la
   configuration ; `diag/*/lecture-sondes-t06.json*` exclu), commit S7 ; gardes : tête = S7, C7 ancêtre, arbre gelé égal, S7
   ancêtre de `main`.
3. **Registres de `main`** recopiés (`registres/*.md`, `registres/go-extraits/`) et **fichiers qu'ils citent** avec leurs
   compagnons (un fichier suivi à S7 hors de l'extraction partielle y est d'abord ajouté : sinon git le retire au changement de
   branche, défaut trouvé par la répétition, § 11), dont les fichiers des quatre lignes `SCELLEMENT-JEUX-T07-JD`, `-JA`, `-JC` et `SCELLEMENT-CONCEPTS-T07` (présence
   contrôlée) et le **journal du script** du dossier de chaque jeu (remesure des jetons, E-8) ; chemin interdit cité → arrêt ;
   `src/` et `tests/` inchangés (contrôlé).
4. **Sortie de 7b**, par refspec explicite, fichiers nommés seulement (§ 2.1) ; `arret.json` de 7b recopié s'il existe (la garde
   le lit : la lecture ne part pas) ; fichiers cités par la configuration de 7b (tâches, consignes) recopiés de `main`.
5. **Environnement** : `python3 -m venv`, `pip install -r requirements-gpu.txt` de S7 ; torch voit la carte ; **modèle descendu**
   au cache local (`precharger_modele`, révision figée du manifeste de 7b, `HF_TOKEN`) ; tout le reste lit hors ligne.
6. **Essais figés** `tests/test_t07_*.py` (liste et empreintes dans les traces), dernière ligne égale à `ATT` ; empreinte
   canonique de la configuration.
7. **`CODE-T07`** : `python -m controle_ia.t07.code_t07_v1 verifier . registres/scellements-v1.md` (commit cité ancêtre de la tête,
   fichiers du module importé égaux à la liste, **tout `src/controle_ia/` égal au commit cité et arbre de travail propre**, DF-02 ;
   `PYTHONDONTWRITEBYTECODE=1` : aucun `__pycache__`) ; non conforme → arrêt, rien d'autre ; le même contrôle est rejoué par la
   garde du repli, la passe à blanc et l'étape A.
8. **Branche neuve** (absente du distant, sinon arrêt R12) ; poussées par chemins explicites, aucun fichier de plus de 90 Mo.
9. **Repli** (`lecture_v2 repli-seul`, DF-01) : **garde d'ouverture de l'étape A d'abord** (journalisée : lignes et sceaux, GO,
   refus de la course 7a, `CODE-T07`, garde adaptée ; refus → code 2, rien n'est calculé, l'instance s'arrête : relance sur une
   instance neuve quand la ligne existe) ; puis recalcul **sous un nom daté** (`donnees/<run>/activations-repli-<date>/`) :
   identité à dose 0, rejeu en forçage, garde d'équivalence ; réussite → renommé `activations/`, rapport scellé à côté
   (`rapport-repli-t07.json`, empreinte des activations) ; code 3 (R11) → **une** relance sur la même carte, sous un nom daté neuf
   (le premier recalcul reste) ; second échec → nœud ; poussée « garde, repli » (rapport, journal des ouvertures, traces).
10. **Passe à blanc** : `lecture_v2 passe-blanc` (`CODE-T07` contrôlée d'abord, DF-02 ; mémoire de la notation jugée, DF-04) ;
    sortie scellée poussée quelle que soit son issue ; code ≠ 0 → arrêt, l'étape A ne part pas.
11. **Étape A** : `lecture_v2 etape-a-apres-repli` (rapport du repli relu et **couvrant** : sceau, run, manifeste, garde, empreinte
    des activations ; garde d'ouverture rejouée, `CODE-T07` comprise ; garde d'identité remplacée par la garde d'équivalence) ; sorties, registre (`SCORES-T07`, `SONDES-T07`) et journal des ouvertures
    poussés ; code ≠ 0 → nœud, aucune relance sous ce texte.
12. **Fin** : `lecture-sondes-t06.json` absent de l'arbre (contrôlé) ; « stopped » demandé ; la fille détruit.

## 6. Devis de la variante B (A100, recalcul des activations puis étape A) et dépense

| Phase | Attendu (h) | Pire cas (h) | Source |
|---|---|---|---|
| Création, démarrage, image | 0,10 | 0,30 | E2 (R-1689 : démarrage en file 17 min) |
| Clone partiel, registres, sortie de 7b | 0,10 | 0,45 | E2 (R-1687 : clonage partiel 10 s) ; borne du clonage de l'amorce de T0.6 (900 s) |
| Paquets (`requirements-gpu.txt`) | 0,15 | 0,50 | amorce de T0.6 (installation bornée à 3 600 s) ; non mesuré à part : **supposé** |
| Modèle (≈ 16 Go) | 0,10 | 1,00 | `inet_down` ≥ 500 Mb/s : ≈ 0,07 h ; pire : débit dix fois plus bas (E2 : ≈ 10 Mb/s reçus pour 861 annoncés) |
| Essais de T0.7 (14 fichiers) | 0,30 | 0,60 | mesuré : 1 002,7 s ici, 4 cœurs partagés |
| Repli : recalcul et garde d'équivalence | 0,10 | 0,40 | brouillon 19 : 576 épisodes × 0,45 s ≈ 0,07 h (P3 : 108,4 s pour 240, **supposé** même longueur) ; écriture de 31,5 Go ; une relance R11 au pire |
| Passe à blanc | 0,10 | 0,20 | estimation de la passe (échantillon) |
| Étape A | 2,00 à 3,50 | 4,00 à 7,00 | brouillon 19, « Calcul et dépense » (attendu) ; pire : hôte deux fois plus lent |
| Poussées | 0,10 | 0,30 | scores et sondes ≤ 2 Go |
| **Total** | **3,2 à 4,7** | **7,8 à 10,8** | |

- **Coût** (≤ 1,30 USD de l'heure, carte et disque de 100 Go compris dans `dph_total`) : attendu **≈ 4,2 à 6,1 USD** ; pire cas
  ≈ 10,1 à 14,0 USD ; plus le téléchargement, borné à 24 Go × 0,05 USD = **1,20 USD** (modèle ≈ 16, paquets ≈ 5, sortie de 7b et
  dépôt ≈ 3), et le disque après l'arrêt jusqu'à la destruction (≤ 0,08 USD de l'heure, ≤ 1 h). **Attendu ≈ 5,4 à 7,4 USD ; pire
  cas ≈ 11,4 à 15,3 USD.** Le brouillon 19 (variante B : ≈ 4 à 5 USD, pire ≈ 9 à 10) ne comptait ni les essais, ni la passe à
  blanc, ni l'étape A entière à son devis propre : écart déclaré.
- **Plafond** : **20 USD** (GO-2026-11-10-06, non cumulé avec GO-2026-11-10-04 ; `PLAF`, ligne (A)) ; la minuterie de l'instance
  (création + 12 h) borne la carte à ≈ 15,6 USD, soit ≤ 17,7 USD avec le téléchargement et le disque : sous le plafond, même au
  pire cas du devis (≈ 15,3 USD).
- **Relevé** : bloc du § 4.5 (`PRIX_H` = `prix_h` du § 4.3) ; **compte rendu** à Lazar à 10 USD (aucun arrêt) ; **arrêt** dès que
  le cumul plus un quart d'heure de carte atteint `PLAF` : destruction par l'identifiant (§ 4.7), nœud, aucune relance sans un mot
  de Lazar sur un devis neuf. La facture, si connue, fait foi. Dépense inscrite sous `GO`.

## 7. Arrêts

- Préalable manquant, empreinte différente, recherche vide, création incertaine : rien n'est créé (ou plus rien) ; compte rendu.
- Ligne `ARRET` du script (code 2 avant la branche : machine, code, registres, sortie de 7b, environnement, essais, `CODE-T07`, branche
  présente ; code 3 : refus de la garde au repli, repli après relance, passe à blanc, étape A) ; **refus de la garde au repli**
  (ligne manquante) : rien n'est calculé, l'instance s'arrête, la fille la détruit ; une création neuve n'a lieu que sur un écrit
  de la mère (même GO, devis inchangé), quand la ligne existe ; le script pousse ses traces si la branche existe et demande
  « stopped » ; la fille relève la ligne, vérifie ce qui est poussé (§ 4.6), **détruit** (§ 4.7), compte rendu, nœud de la mère.
- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement.

## 8. Compte rendu de la fille (nombres seuls, ≤ 400 mots)

`vastai --version` ; P1 à P11 (valeurs) ; recherche (offre, prix, cuda) ; identifiant, `TC`, `ECH` ; lignes `T07` (machine, code,
registres, quatre lignes, sortie de 7b, essais, configuration, `CODE-T07`, repli : actions et écart maximal de la garde,
passe à blanc : issue, frontière, mémoire, durée estimée, étape A : code et run) ; tête de la branche, commits, `OK` / `ÉCART` ;
dépense relevée ; destruction, inventaire final ; écarts. **Ni score, ni aire, ni contenu des sorties de l'étape A.** Journal
(garde des secrets à 0) envoyé à la mère.

## 9. Ce qui suit, et ce que cet ordre ne fait pas

- **Suite (mère)** : recopier **à l'octet**, dans le registre et le journal des ouvertures de `main`, les lignes `SCORES-T07`,
  `SONDES-T07` et `OUVERTURE-T07` écrites sur l'instance, après avoir vérifié que le journal de P3-bis de `main` ne porte aucune
  ligne datée avant la fin de l'étape A qui manquait à la copie de l'instance (sinon nœud ; G2, G4) ; inscrire la dépense ; étape
  B sur processeur, par son propre ordre.
- **Ne fait pas** : aucun épisode ; aucune étape B ; aucune lecture de sortie ; aucune modification du code, du texte, de la
  configuration ou de la chaîne de T0.6 ; aucune fusion ; aucune écriture sur `main` ; aucun contact externe ni appel de modèle ;
  aucune H200.

## 10. À juger par la contre-lecture

1. La ligne `GO-LECTURE-T07` pour cette instance (texte : « variante B »), dont l'extrait cite GO-2026-11-10-06 ; la minuterie
   (création + 12 h) contre le plafond de 20 USD.
2. Registres recopiés de `main` sur S7 (arbre non propre déclaré au manifeste, CT-15, CT-17) ; la garde de fin d'étape A lit la
   copie du journal de P3-bis faite à l'ouverture (§ 9).
3. Journal du script des jeux cherché dans le dossier du jeu (convention).
4. Essais : sur l'instance, la suite entière ; à la répétition locale, une liste réduite (§ 11) ; `ATT` à mesurer au commit C7 dans
   l'environnement de l'instance ou à accepter de la session.
5. Seuil de compte rendu (10 USD) et marge d'un quart d'heure : proposés. Paquets installés sans couperet de dépense propre
   (borne de 3 600 s).
6. L'instance demande « stopped » à sa fin ; la destruction reste à la fille (R10), la minuterie la garantit à `ECH`.

## 11. Répétition locale du script de l'instance (mode jouet)

Script `scripts/repetition_jouet_variante_b_t07_v1.py` : course 7b jouet (chaîne de T0.6 de `1609a4bf`, entropie fixée à 1), dépôt
distant local (`main` : C7, S7, H avec `CODE-T07` et `GO-LECTURE-T07` ; branche de 7b avec ce que l'amorce v11 pousse, dont un
`lecture-sondes-t06.json` factice), puis **le script de l'instance joué tel quel par `bash`, sous `env -i`**, en essai local
(`ESSAI_LOCAL=1` : racine, dépôt et interpréteur locaux, liste d'essais réduite à `tests/test_t07_journal_p3bis_d3_v1.py`, ni
minuterie, ni appel à Vast, ni modèle descendu).

| passage | script | code | résultat | pièces (`docs/notes/g0-deux-semaines-v1/t07-module-v2/`) |
|---|---|---|---|---|
| 1 (brouillon 2) | `f75fec22…` | 3 | **défaut trouvé** : fichiers suivis à S7 hors de l'extraction partielle (tâches citées par la configuration de 7b), recopiés puis retirés par git au changement de branche ; repli en arrêt R11 ; traces poussées | `repetition-jouet-variante-b-v1/` (passage 1) |
| 2 (brouillon 2) | `eea99808…` | 0 | correction (ajout à l'extraction partielle avant la recopie) ; repli, passe à blanc, étape A ; trois commits | `repetition-jouet-variante-b-v1/` |
| **3 (ce brouillon)** | **`99e4c926…`** (`8ae9fc44`) | **0** | de 09:35:50 à 09:37:29 UTC : essais `20 passed` ; `CODE-T07 conforme` (18 fichiers ; tout `src/controle_ia/` égal au commit cité, arbre propre) ; **repli : garde d'ouverture d'abord, « recalcul fait »**, garde d'équivalence passée (21 actions, écart maximal 0), rapport `donnees/<run>/activations/rapport-repli-t07.json` scellé ; passe à blanc tenue (`CODE-T07` et mémoire de la notation comprises) ; étape A code 0 ; **trois commits poussés** ; `SCORES-T07` et `SONDES-T07` au registre poussé ; `src` et `tests` inchangés ; **`lecture-sondes-t06.json` ni dans l'arbre, ni descendu** (objet manquant du clone partiel). **Artefact** : branche déjà poussée → code 2, repli non joué | `repetition-jouet-variante-b-v2/` |

Non répétés (réel seulement) : minuterie et appels à Vast, installation des paquets, descente du modèle, carte.

## 12. Marqueurs (à remplir par la mère ; une occurrence chacun)

Remplis à ce brouillon : `GO_VARIANTE_B_T07` = **GO-2026-11-10-06** (R-2115, message de la mère) ; le plafond, **20 USD**, est
celui de cette ligne (`PLAF`).

| Marqueur (sans chevrons) | Où | Valeur |
|---|---|---|
| `ID_SESSION_FILLE` | en-tête | identifiant de la session fille |
| `EMPREINTE_CONFIG_T07` | § 1 | empreinte canonique de la configuration de T0.7 scellée |
| `LIGNE_SCELLEMENT_T07` | § 3 | la ligne `SCELLEMENT-T07` exacte |
| `DEPENSE_ANTERIEURE_USD` | ligne (A) | dépense déjà inscrite sous cette ligne (attendu `0`) |
| `RUN_T06_7B` | ligne (A) | run de 7b |
| `BRANCHE_7B` | ligne (A) | branche poussée par 7b (`calcul/t06-confirmation-7b-v1`, ou suivante) |
| `COMMIT_CODE_T07` | ligne (A) | C7 |
| `COMMIT_SCELLEMENT_T07` | ligne (A) | S7 |
| `CHEMIN_CONFIG_T07` | ligne (A) | chemin de la configuration scellée dans S7 |
| `LIGNE_ESSAIS_T07` | ligne (A) | dernière ligne attendue des essais de T0.7 au commit C7, durée retirée |

Sources : `scripts/lancer_t06_v13.sh`, `src/controle_ia/t06/session_v7.py` et `scripts/amorce_instance_t06_v11.sh` au commit
`1609a4bf` ; ordre de 7b, brouillon 2 (`488c2e51…`) ; ordre de l'étape A, brouillon 1 (`bd7d03b8…`) ; brouillon 19 de T0.7
(`07039ed2…`) ; inventaire des jeux (`c9910a54…`, § 4.3) ; `registres/go.md` et `registres/decisions.md` de `main`
(R-060, R-821, R-1590, R-1677, R-1687, R-1689, R-2089, R-2104, R-2112, R-2115) ; contre-lecture différentielle du code (`dd794e2e…`) ; module `src/controle_ia/t07/` au commit `8ae9fc44` (repli, garde d'abord : `repli_etapes_v1.py`).
