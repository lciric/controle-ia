# Ordre de la mère à la session pilote — A1-v3, troisième course sur hôte durable — v3

Écrit le 5 novembre 2026 (vers 10:55 UTC, `date -u`) par le rédacteur-développeur du lanceur durable, pour la mère
`session_01Qi7Gr6NLmhhAcdmnACBC7G`, qui le transmet. **Destinataire : la session pilote.** Remplace l'ordre v2
(`ordre-fille-a1-v3-troisieme-course-v2.md`, `db8b0735…`, gardé tel quel, R12) : mêmes étapes, plus les valeurs du scellement de la
v4 et les corrections O-1 à O-5 de la contre-lecture courte de la v4 (`contre-lecture-courte-v4-v1/contre-lecture-courte-v4-v1.md`,
`3c69ed59…`, « scellable après 4 couples »), plus un préalable sur le commit public. GO-2026-11-04-06 (course, 400 USD),
GO-2026-11-05-03 (machine à une carte, 35 USD), GO-2026-11-05-04 (Argon rendu). **Le texte scellé v4 prime sur cet ordre.**

## Valeurs (données par la mère, vérifiées en local par le rédacteur : objets présents, empreinte du texte recalculée)
- `COMMIT_PRIVE=096d87fae8788ff08e8ab6733041eaddeb12da0a` (main du dépôt privé : lanceur durable v4 scellé, v1, sondes v1 et v10).
- `COMMIT_PUBLIC=291e9178e27fe96d7023bd6cbde476aff7fc9d11` (`lciric/ideation-organism`, branche `claude/new-session-7qxayx` ;
  **pas encore poussé** : la poussée attend le mot de Lazar ; préalable 8).
- `SHA_TEXTE=0b35494b7533c67b4aacb0cadc7820c825c82c046e641928df7641db8a381773`
  (`orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md`, égal à son compagnon).
- `COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab` (tête de `canal/conv-audit-n04` lue ; ligne GO-2026-11-04-06 égale à
  l'octet à la ligne 244 de `main`, aucun identifiant en double).
- Clé d'Argon : `CLE_ARGON="$GEMINI_API_KEY_2"` (R-1540 ; jamais affichée).
- **Jeton GitHub : `JETON_VAR=CONTROLE_IA_GITHUB_TOKEN` ou `JETON_VAR=CONTROLE_IA_GITHUB_TOKEN_2`**, la variable que Lazar indiquera ;
  sans échéance, ou échéance au 19 novembre 2026 au moins (préalable 4). On n'écrit que le nom de la variable.

## Étape 0 — dossier neuf et modules (O-1 ; avant tout préalable)
```
COMMIT_PRIVE=096d87fae8788ff08e8ab6733041eaddeb12da0a
JETON_VAR="${JETON_VAR:?choisir CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2, selon Lazar}"   # le nom seul ; préalable 4
D=/home/user/hors-clone-a1-v3-troisieme-v4; mkdir "$D" || exit 2                   # neuf (R12) ; seul mkdir de l'ordre
J="$D/journal-location-a1-v3-troisieme-v4.log"
cd /home/user/controle-ia-travail && git fetch -q origin refs/heads/main:refs/remotes/origin/main \
 && git cat-file -e "$COMMIT_PRIVE^{commit}" \
 && for f in hote_durable_a1_v3.py hote_durable_a1_v3_v4.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && { echo "$(date -u +%FT%TZ) étape 0 : COMMIT_PRIVE $COMMIT_PRIVE"; (cd "$D" && sha256sum hote_durable_a1_v3*.py sonde_hote_durable_a1_v3*.py); } >> "$J"
```
Les préalables écrivent ensuite au même journal `"$J"` (l'outil `louer` y écrit aussi, et `louer` garde sa propre garde des
marqueurs `.identifiant` et `.creation-incertaine`).

## Préalables (chacun écrit au journal `"$J"` ; un échec : arrêt et message à la mère)
1. `vastai --version` = 1.8.3 ; inventaire filtré (`python3 -I -B "$D/hote_durable_a1_v3_v4.py" inventaire`, sous l'`env -i` de la
   location sans `CLE_ARGON` ni `GO_ID`) : aucune instance du programme (les instances R8 ne se touchent pas).
2. **Branches absentes** : `git ls-remote origin 'refs/heads/donnees/attaque-goodhart-v3-a1v3-troisieme-*'` ne rend **rien**
   (`…-troisieme-v1`, `…-troisieme-refus-v1`, `…-troisieme-interrompue-v1`, `…-troisieme-signe-de-vie-v1` ; la copie
   `…-versement-interrompue-v1` est une copie de travail sur la machine, pas une branche). Une branche présente : arrêt (R12).
3. **Commande d'Argon gelée** (O-3) : lue sans exécution le 5 novembre (R-1561 : `commande_argon_v56_nuit_v2.py`, `221df610…`
   conforme, commit `60656845` du dépôt privé), relue par la contre-lecture courte de la v4 (point 14 : arguments de `servir`, clé
   dans `GEMINI_API_KEY`, clés de `/relais/etat` lues par l'hôte toutes présentes ; un 402 de l'interface → code 3 au pire cas ; le
   relais repart de zéro à chaque lancement). Écrire cette référence au journal, puis garder le **contrôle d'empreinte** :
   `git fetch -q origin refs/heads/donnees/recuperation-collisionneur-v8-v1:refs/remotes/origin/donnees/recuperation-collisionneur-v8-v1`
   puis `git show origin/donnees/recuperation-collisionneur-v8-v1:donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py | sha256sum`
   = `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` ; autre empreinte : arrêt et message.
4. **Jeton GitHub** : `curl -sI -H "Authorization: Bearer ${!JETON_VAR}" https://api.github.com/rate_limit | grep -i '^HTTP/\|^github-authentication-token-expiration'`
   (seules la ligne d'état et celle de l'échéance affichées) : réponse `200` et, soit aucune échéance, soit une échéance au
   **19 novembre 2026** au moins (et après T0 + 82 h) ; toute autre réponse : arrêt.
5. **Argon seul** (texte, section 8, point (4) ; section 13, points 7 ter et 7 quater) : aucune autre utilisation d'Argon en cours ni
   prévue pendant la course ; identifiants et heures écrits au journal. Un doute : arrêt et message.
6. **Crédit d'Argon** (O-4, aligné sur le texte, section 8, précaution du 402) : au journal, **l'un des deux** — (a) la confirmation
   de Lazar que le crédit prépayé du compte de facturation de la clé couvre au moins 400 USD, ou qu'une recharge automatique d'au
   moins ce montant est active ; ou (b) le mot de Lazar qui abandonne cette précaution, écrit **avec son prix** (un solde épuisé en
   cours de course perd, sans résultat, ce qui a été dépensé avant le premier 402 : jusqu'à ≈ 131 USD à l'attendu haut, ≈ 190 USD au
   maximum du devis, plus ≈ 5 USD de machine). Chaque mot, transmis par la mère, avec son heure et ses mots exacts. Sans (a) ni (b) :
   aucune location.
7. **Mots de Lazar sur la v4** (O-2) : au journal, avec heure et mots exacts transmis par la mère, **les deux** — (a) le périmètre de
   GO-2026-11-04-06 (« texte v3 neuf … ») couvre la v4 (ou une extension du GO l'écrit) ; (b) la publication de la v4 sur le dépôt
   public de l'organisme est accordée (R-1539 ne couvrait que la v3). Sans l'un des deux : aucune location (la dépense sortirait du
   périmètre du GO).
8. **Commit public visible** : `git ls-remote https://github.com/lciric/ideation-organism.git refs/heads/claude/new-session-7qxayx`
   rend `291e9178e27fe96d7023bd6cbde476aff7fc9d11`, **ou** `git fetch -q https://github.com/lciric/ideation-organism.git 291e9178e27fe96d7023bd6cbde476aff7fc9d11`
   réussit (le commit est atteignable sur le dépôt public, dans une copie de travail jetable). Sinon : arrêt — la machine clonerait
   le dépôt public sans y trouver le texte et refuserait après son signe de vie (coup unique).
9. **Appel de contrôle d'Argon** : le texte v4 n'en prévoit aucun pour la troisième course ; **aucun n'est fait**.

## Location (une fois ; sortie brute de `vastai` jamais affichée ; `$D`, `$J` et les modules viennent de l'étape 0)
```
COMMIT_PRIVE=096d87fae8788ff08e8ab6733041eaddeb12da0a
COMMIT_PUBLIC=291e9178e27fe96d7023bd6cbde476aff7fc9d11
SHA_TEXTE=0b35494b7533c67b4aacb0cadc7820c825c82c046e641928df7641db8a381773
COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab
JETON_VAR="${JETON_VAR:?choisir CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2, selon Lazar}"
D=/home/user/hors-clone-a1-v3-troisieme-v4
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
[ -f "$D/hote_durable_a1_v3_v4.py" ] || { echo "étape 0 non faite"; exit 2; }
cd /home/user/controle-ia-travail && git fetch -q origin refs/heads/main:refs/remotes/origin/main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && timeout 300 vastai search offers 'num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/hote_durable_a1_v3_v4.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-05-03 env -i GO_ID=GO-2026-11-05-03 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
        CLE_ARGON="$GEMINI_API_KEY_2" GH_TOKEN="${!JETON_VAR}" VAST_API_KEY="$VAST_API_KEY" timeout 1800 nice -n 10 \
        python3 -I -B "$D/hote_durable_a1_v3_v4.py" louer --go GO-2026-11-04-06 --go-machine GO-2026-11-05-03 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --commit-public "$COMMIT_PUBLIC" --sha-texte "$SHA_TEXTE" \
          --commit-registre "$COMMIT_REGISTRE" --journal-local "$D/journal-location-a1-v3-troisieme-v4.log" $V || exit 2
    done
```
(Plus de `mkdir` ici : O-1. `timeout 1800` : cinq créations de 300 s au plus tiennent.)

**Si `louer` rend 2 :**
- **« no_such_ask » final** (rien créé, aucun marqueur) : une seule reprise, dans un **dossier neuf** : l'étape 0 avec
  `D=/home/user/hors-clone-a1-v3-troisieme-v4b`, puis la location avec ce `D` (recherche comprise) ; puis message.
- **Marqueur `.creation-incertaine` présent** : **aucune** nouvelle location ; inventaire filtré, puis message (une instance peut
  exister).
- Autre refus (GO, offre, coût, clé) : rien créé ; message, sans reprise.

## Après la location
- Envoie aussitôt à la mère la « LIGNE POUR registres/etat.md » du journal (identifiant, T0, prix, échéance de la minuterie).
- `controler` à T0 + 40 min (signe de vie), puis aux heures écrites dans `"$D/journal-location-a1-v3-troisieme-v4.log.etat.json"`,
  sous le même `env -i` sans `CLE_ARGON` ni `GO_ID` (avec `GH_TOKEN="${!JETON_VAR}"` et `VAST_API_KEY`) :
  `python3 -I -B "$D/hote_durable_a1_v3_v4.py" controler --etat "$D/journal-location-a1-v3-troisieme-v4.log.etat.json" --journal-local "$D/journal-controle-a1-v3-troisieme-v4.log"` ;
  `facturation` de même, à tout moment. **Conduite par code :**
  - **0** — instance absente (détruite par elle-même ou par la minuterie) : consigner (`registres/arrets.md`, par la mère), message ;
    fin des contrôles.
  - **1** — détruite par le pilote (aucun signe de vie à T0 + 30 min : rien n'a tourné) : consigner, message ; aucune relocation sans
    mot de la mère.
  - **2** — refus (étiquette autre, instance protégée, état illisible) : **aucun geste** ; vérifier `.etat.json` et l'identifiant ;
    message immédiat ; recontrôler une fois dans 10 min, puis attendre la mère.
  - **3** — destruction demandée mais encore listée : recontrôler dans 5 min (au plus trois fois), puis message.
  - **5** — listée avant ses bornes : recontrôler à l'heure suivante de l'état ; lire l'état de Vast de la ligne (`running`,
    `stopped`, `exited`) : `stopped` ou `exited` avant l'échéance → message, puis la voie ci-dessous si elle s'applique.
  - **6** — délai dépassé ou échec de `vastai` ou de `ls-remote` : recontrôler dans 5 min, au plus trois fois de suite, puis message
    (jamais « pas de signe de vie » sur un 6).
  - **7** — encore listée après l'échéance finale : **aucun geste** ; message ; la mère décide (données possibles sur le disque).
- **Voie de récupération d'une machine arrêtée avant l'échéance** (O-5 ; non éprouvée sur Vast) — **seulement après une poussée
  finale manquée en passant** (panne passagère de GitHub, journal de l'hôte : « poussée n/N … », puis « versement non vérifié ») et
  sur mot de la mère, **avant l'échéance de la minuterie** (`echeance_finale_utc` de l'état) : `vastai start instance <ID>` ; au
  redémarrage, l'hôte ne relance rien, scelle l'état tel quel, le verse depuis une copie neuve `…-versement-interrompue-v1` sur
  `donnees/attaque-goodhart-v3-a1v3-troisieme-interrompue-v1` (C3), avec le même jeton, puis se détruit ; contrôler ensuite.
  **Pas de redémarrage** pour un **secret trouvé** (le redémarrage rejouerait le même contrôle et s'arrêterait de nouveau) ni pour un
  **jeton échu ou révoqué** (même jeton sur la machine) : la mère décide. Redémarrée **après** l'échéance, la machine est détruite
  aussitôt (échéance d'origine relue) : ne pas la redémarrer alors.
- **Aucune lecture des résultats** : la sortie est scellée sur la machine et versée avant toute lecture ; seuls les journaux du pilote
  et les codes se lisent.
- Rapport court scellé sur le canal de la session pilote à la location et à la fin ; message à la mère à chaque étape. Aucune question
  à Lazar : tout passe par la mère.
