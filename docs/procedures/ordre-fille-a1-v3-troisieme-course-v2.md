# Ordre de la mère à la session pilote — A1-v3, troisième course sur hôte durable — v2

Écrit le 5 novembre 2026 (heures au rapport `rapport-redaction-v4-v1.md`) par le rédacteur-développeur du lanceur durable, pour la mère
`session_01Qi7Gr6NLmhhAcdmnACBC7G`, qui le transmet. **Destinataire : la session pilote** (la session qui louera ; plus une fille
nommée). Remplace l'ordre v1 (`ordre-fille-a1-v3-troisieme-course-v1.md`, `97f712a7…`, gardé tel quel, R12), d'après la contre-lecture
complète du lanceur v3 (`contre-lecture-complete-v1/contre-lecture-complete-lanceur-v3-v1.md`, `ed4dc27e…`, points 20, 27, 31, 34 à 37)
et celle du texte (`…-texte-v3-v1.md`, `06d6283d…`, couples 12 et 15). GO-2026-11-04-06 (course, 400 USD), GO-2026-11-05-03 (machine
à une carte, 35 USD), GO-2026-11-05-04 (Argon rendu). **Le texte scellé v4 prime sur cet ordre** ; cet ordre ne part qu'après son
scellement et un mot de la mère qui donne les valeurs ci-dessous.

## Valeurs (données par la mère au départ ; aucune n'est devinée)
- `COMMIT_PRIVE=<hash complet du commit de main du dépôt privé qui porte le lanceur durable v4, la v1, la sonde v1 et la sonde v10>`.
- `COMMIT_PUBLIC=<hash complet du commit public de lciric/ideation-organism qui porte le texte scellé v4 ; descend de 9776ed0>`.
- `SHA_TEXTE=<empreinte de orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md, égale à son compagnon>`.
- `COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab` (tête de `canal/conv-audit-n04` lue ; ligne GO-2026-11-04-06 égale à
  l'octet à la ligne 244 de `main`, aucun identifiant en double), sauf autre valeur donnée par la mère.
- Clé d'Argon : `CLE_ARGON="$GEMINI_API_KEY_2"` (R-1540 ; jamais affichée).
- **Jeton GitHub : `JETON_VAR=CONTROLE_IA_GITHUB_TOKEN` ou `JETON_VAR=CONTROLE_IA_GITHUB_TOKEN_2`**, la variable que Lazar indiquera ;
  ce jeton doit être sans échéance, ou échoir au 19 novembre 2026 au moins (préalable 4). On n'écrit que le nom de la variable.

## Préalables (chacun écrit au journal de la location, `"$D/journal-location-a1-v3-troisieme-v4.log"` ; un échec : arrêt et message)
1. `vastai --version` = 1.8.3 ; inventaire filtré (`python3 -I -B "$D/hote_durable_a1_v3_v4.py" inventaire` sous le même `env -i`) :
   aucune instance du programme (les instances R8 ne se touchent pas).
2. **Branches absentes** (motif corrigé, les quatre branches de la course) :
   `git ls-remote origin 'refs/heads/donnees/attaque-goodhart-v3-a1v3-troisieme-*'` ne rend **rien** (`…-troisieme-v1`,
   `…-troisieme-refus-v1`, `…-troisieme-interrompue-v1`, `…-troisieme-signe-de-vie-v1`). `…-versement-interrompue-v1` est une copie
   de travail sur la machine, pas une branche. Une branche présente : arrêt (R12 ; coup unique, contre-lecture du lanceur, point 26).
3. **Commande d'Argon gelée, lue sans être lancée** (non vérifiée par le rédacteur : absente de son conteneur et de toute référence
   locale, aucun réseau) : `git fetch -q origin refs/heads/donnees/recuperation-collisionneur-v8-v1:refs/remotes/origin/donnees/recuperation-collisionneur-v8-v1`,
   puis `git show origin/donnees/recuperation-collisionneur-v8-v1:donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py | sha256sum`
   = `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851`, puis lecture du texte (sans l'exécuter) : (a) la réponse de
   `/relais/etat` porte les clés `plafond_usd`, `max_appels`, `appels`, `cle_presente`, `depense_usd` ; (b) `servir` accepte
   `--port`, `--plafond-usd`, `--max-appels`, `--journal` ; (c) la clé est lue dans `GEMINI_API_KEY`. Écrire au journal ce qui est
   vu, ligne et réponse. Un écart à (a), (b) ou (c) : arrêt et message (sinon la machine louée refuserait après son signe de vie,
   ce qui consomme la branche du signe de vie). Noter aussi, pour l'audit, ce que fait la commande d'un HTTP 402 de l'interface
   (code 3 ou code 4) : une lecture, non une condition.
4. **Jeton GitHub** : `curl -sI -H "Authorization: Bearer ${!JETON_VAR}" https://api.github.com/rate_limit | grep -i '^HTTP/\|^github-authentication-token-expiration'`
   (seules la ligne d'état et celle de l'échéance affichées) : sans en-tête et réponse `200` (jeton sans échéance), ou échéance au **19 novembre 2026** au moins (et
   après T0 + 82 h) ; sinon arrêt et message. Un en-tête absent sur une réponse autre que 200 n'est **pas** « conforme » : arrêt.
5. **Argon seul** (texte, section 8, point (4) ; section 13, points 7 ter et 7 quater) : aucune autre utilisation d'Argon en cours ni
   prévue pendant la course ; écrire au journal les identifiants des sessions et instances vues et les heures. Un doute : arrêt et
   message à la mère.
6. **Crédit d'Argon** (texte, section 8, précaution du 402) : la confirmation de Lazar, transmise par la mère (crédit prépayé d'au
   moins 400 USD sur le compte de facturation de la clé, ou recharge automatique), est **écrite au journal** avec son heure et ses
   mots ; sans elle : aucune location, message à la mère.
7. **Appel de contrôle d'Argon** : le texte v4 n'en prévoit aucun pour la troisième course (la seconde en avait fait un, hors course,
   section 0.5 bis) ; **aucun n'est fait**. S'il est voulu (contre-lecture du texte, point 30), il passe d'abord par un couple au
   texte et par le lanceur ; il ne s'improvise pas ici.

## Location (une fois ; sortie brute de `vastai` jamais affichée)
```
COMMIT_PRIVE=<valeur de la mère>
COMMIT_PUBLIC=<valeur de la mère>
SHA_TEXTE=<valeur de la mère>
COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab
JETON_VAR=<CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2, selon Lazar>
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-a1-v3-troisieme-v4; mkdir "$D" || exit 2                   # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin refs/heads/main:refs/remotes/origin/main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py hote_durable_a1_v3_v4.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
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
(`timeout 1800` : cinq créations de 300 s au plus tiennent ; contre-lecture du lanceur, point 28.)

**Si `louer` rend 2 :**
- **« no_such_ask » final** (cinq offres disparues, rien créé, aucun marqueur) : une seule reprise, dans un **dossier neuf**
  (`D=/home/user/hors-clone-a1-v3-troisieme-v4b`, puis toute la commande ci-dessus avec ce `D`, recherche comprise) ; puis message.
- **Marqueur `.creation-incertaine` présent** : **aucune** nouvelle location ; inventaire filtré, puis message à la mère (une instance
  peut exister).
- Autre refus (GO, offre, coût, clé) : rien créé ; message, sans reprise.

## Après la location
- Envoie aussitôt à la mère la « LIGNE POUR registres/etat.md » du journal (identifiant, T0, prix, échéance de la minuterie).
- `controler` à T0 + 40 min (signe de vie), puis aux heures écrites dans `"$D/journal-location-a1-v3-troisieme-v4.log.etat.json"`,
  sous le même `env -i` sans `CLE_ARGON` ni `GO_ID` (avec `GH_TOKEN="${!JETON_VAR}"` et `VAST_API_KEY`) :
  `python3 -I -B "$D/hote_durable_a1_v3_v4.py" controler --etat "$D/journal-location-a1-v3-troisieme-v4.log.etat.json" --journal-local "$D/journal-controle-a1-v3-troisieme-v4.log"` ;
  `facturation` de même, à tout moment. **Conduite par code :**
  - **0** — instance absente de l'inventaire (détruite par elle-même ou par la minuterie) : consigner (`registres/arrets.md` par la
    mère), message ; fin des contrôles.
  - **1** — détruite par le pilote (aucun signe de vie à T0 + 30 min : rien n'a tourné) : consigner, message ; aucune relocation sans
    mot de la mère (R12 : la branche du signe de vie n'existe pas, mais un texte et un GO décident).
  - **2** — refus (étiquette autre, instance protégée, état illisible) : **aucun geste** ; vérifier `.etat.json` et l'identifiant ;
    message immédiat ; recontrôler une fois dans 10 min avec le même état, puis attendre la mère.
  - **3** — destruction demandée mais encore listée : recontrôler dans 5 min (au plus trois fois), puis message.
  - **5** — listée avant ses bornes : recontrôler à l'heure suivante de l'état ; lire l'état de Vast écrit dans la ligne
    (`running`, `stopped`, `exited`) : `stopped` ou `exited` **avant l'échéance** → voie de récupération ci-dessous.
  - **6** — délai dépassé ou échec de `vastai` ou de `ls-remote` (la v4 rend 6 sur tout échec de `vastai`) : recontrôler dans 5 min,
    au plus trois fois de suite, puis message (ne jamais conclure « pas de signe de vie » sur un 6).
  - **7** — encore listée après l'échéance finale : **aucun geste** ; message ; la mère décide (données possibles sur le disque).
- **Voie de récupération d'une machine arrêtée avant l'échéance** (poussée finale manquée, secret trouvé : l'hôte s'arrête sans se
  détruire ; non éprouvée sur Vast) : sur mot de la mère seulement (dépense : stockage, puis quelques minutes de machine), et **avant
  l'échéance de la minuterie** (`echeance_finale_utc` de l'état) : `vastai start instance <ID>` ; au redémarrage, l'hôte ne relance
  rien, scelle l'état tel quel, le verse depuis une copie neuve `…-versement-interrompue-v1` sur `donnees/attaque-goodhart-v3-a1v3-troisieme-interrompue-v1`
  (C3), avec le même jeton, puis se détruit ; contrôler ensuite. Redémarrée **après** l'échéance, la machine est détruite aussitôt
  (l'échéance d'origine est relue) : ne pas la redémarrer alors ; la mère décide (copie par `vastai`, non éprouvée).
- **Aucune lecture des résultats** : la sortie est scellée sur la machine et versée avant toute lecture ; seuls les journaux du pilote
  et les codes se lisent.
- Rapport court scellé sur le canal de la session pilote à la location et à la fin ; message à la mère à chaque étape. Aucune question
  à Lazar : tout passe par la mère.
