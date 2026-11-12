# Ordre de la mère à la fille — A1-v3, troisième course sur hôte durable — v1

Écrit le 5 novembre 2026 vers 07:40 UTC (`date -u`) par la mère `session_01Qi7Gr6NLmhhAcdmnACBC7G`. Destinataire : la fille `session_01Qi7Gr3s7JVgpRP17VcSyAf`. Mot de Lazar : « argon rechargé, lance A1-v3 dès que prêt » (R-1540) ; GO-2026-11-04-06 (course, 400 USD), GO-2026-11-05-03 (machine à une carte, 35 USD), GO-2026-11-05-04 (Argon rendu). Le texte scellé prime sur cet ordre.

## Valeurs (vérifiées par la mère)
- `COMMIT_PRIVE=bb35e87f0e7825b2225f2ade1177da428f78352e` (main du dépôt privé : lanceur v3 scellé, v1, sondes v1 et v10 ; 96 essais v3 rejoués).
- `COMMIT_PUBLIC=08ad8f35d88282057d5e5d25747f74088ea0455a` (`lciric/ideation-organism`, branche `claude/new-session-7qxayx` ; descend de `9776ed0`).
- `SHA_TEXTE=c697d0dfb7956cd3bc0297af613746eafacf9d9f68ca39befa0d12c4daad5baa` (`orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v3.md`, égal à son compagnon).
- `COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab` (tête de `canal/conv-audit-n04` ; ligne GO-2026-11-04-06 identique à celle de main, une seule occurrence).
- Clé d'Argon : `CLE_ARGON="$GEMINI_API_KEY_2"` (R-1540 ; jamais affichée).

## Préalables (chacun écrit au journal ; un échec : arrêt et message)
1. `vastai --version` = 1.8.3 ; inventaire filtré : aucune instance du programme (les R8 ne se touchent pas).
2. Branches absentes : `git ls-remote origin 'refs/heads/donnees/attaque-goodhart-v3-a1v3-troisieme-v1*'` ne rend aucune des branches de la course (`…-v1`, `…-refus-v1`, `…-interrompue-v1`, `…-signe-de-vie-v1`, `…-versement-interrompue-v1`).
3. Expiration du jeton GitHub : `curl -sI -H "Authorization: Bearer $CONTROLE_IA_GITHUB_TOKEN" https://api.github.com/rate_limit | grep -i '^github-authentication-token-expiration'` (seule cette ligne affichée) ; elle doit tomber après T0 + 82 h ; sans en-tête (jeton sans échéance) : conforme ; avant : arrêt et message.

## Location (commande de la section 7 du rapport `rapport-redaction-v3-v2.md`, avec les noms de la v3 de l'additif 1, section 7)
```
COMMIT_PRIVE=bb35e87f0e7825b2225f2ade1177da428f78352e
COMMIT_PUBLIC=08ad8f35d88282057d5e5d25747f74088ea0455a
SHA_TEXTE=c697d0dfb7956cd3bc0297af613746eafacf9d9f68ca39befa0d12c4daad5baa
COMMIT_REGISTRE=740f49e2b27344b3188f9aba20b5f0115c3468ab
[ "$(vastai --version 2>/dev/null)" = "1.8.3" ] || { echo "vastai 1.8.3 exigé"; exit 2; }
D=/home/user/hors-clone-a1-v3-troisieme-v3; mkdir "$D" || exit 2
cd /home/user/controle-ia-travail && git fetch -q origin refs/heads/main:refs/remotes/origin/main \
 && git show origin/main:registres/go.md > "$D/registre-go-main.md" \
 && git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py" \
 && for f in hote_durable_a1_v3.py hote_durable_a1_v3_v3.py sonde_hote_durable_a1_v3.py sonde_hote_durable_a1_v3_v10.py; do
      git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f" || exit 2; done \
 && timeout 300 vastai search offers 'num_gpus=1 rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --storage 30 --raw > "$D/offres.json" \
 && OFFRE=$(python3 -I -B "$D/hote_durable_a1_v3_v3.py" offre --offres "$D/offres.json") \
 && for V in "--verifier-seulement" ""; do
      GO_ID=GO-2026-11-05-03 env -i GO_ID=GO-2026-11-05-03 PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 \
        HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-${SSL_CERT_FILE:-}}" \
        CLE_ARGON="$GEMINI_API_KEY_2" GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" VAST_API_KEY="$VAST_API_KEY" timeout 900 nice -n 10 \
        python3 -I -B "$D/hote_durable_a1_v3_v3.py" louer --go GO-2026-11-04-06 --go-machine GO-2026-11-05-03 \
          --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
          --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --commit-public "$COMMIT_PUBLIC" --sha-texte "$SHA_TEXTE" \
          --commit-registre "$COMMIT_REGISTRE" --journal-local "$D/journal-location-a1-v3-troisieme-v3.log" $V || exit 2
    done
```
Sortie brute de `vastai` jamais affichée (redirigée, comme ci-dessus) ; offre disparue (« no_such_ask ») : nouvelle recherche, une fois, puis message.

## Après la location
- Envoie aussitôt à la mère la « LIGNE POUR registres/etat.md » du journal (identifiant, T0, prix, échéance de la minuterie).
- `controler` à T0 + 40 min (signe de vie), puis aux échéances écrites dans `"$D/journal-location-a1-v3-troisieme-v3.log.etat.json"`, avec le même `env -i` sans `CLE_ARGON` ni `GO_ID` : `python3 -I -B "$D/hote_durable_a1_v3_v3.py" controler --etat "$D/journal-location-a1-v3-troisieme-v3.log.etat.json" --journal-local "$D/journal-controle-a1-v3-troisieme-v3.log"` ; `facturation` de même à tout moment. Code 5 ou 6 : recontrôler ; 7 : aucun geste, message ; 1 : consigner (arrêt) et message.
- **Aucune lecture des résultats** : la sortie est scellée sur la machine et versée avant toute lecture ; seuls les journaux du lanceur et les codes se lisent.
- Rapport court scellé sur `canal/fille-2026-11-04` à la location et à la fin ; message à la mère à chaque étape. Ne pose aucune question à Lazar.
