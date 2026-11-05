# Ordre à la fille — tour du collisionneur v9 sur la question 2 de Kirchner (GO-2026-11-03-04) — v1

Écrit par session-depot le 3 novembre 2026 à 10:22 UTC (heure relevée par `date -u` à 10:21:16). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mot direct de Lazar : « je veux que Kirchner Q2 passe avant A1-v3 » ; « pas de plafond » (rapporté).
Premier des deux instruments Kirchner ; la course de l'organisme suivra (ordre séparé), puis la seconde course d'A1-v3.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré en avance rapide (lignes GO-2026-11-03-04, 35 USD, et -05 dans `registres/go.md`).
- Branche `donnees/collisionneur-v9-kirchner-q2-v1`, commit **`16ec2e5a`**, extraite par `git archive` dans ton clone sans toucher à
  l'index : dossier `donnees/collisionneur-v9-kirchner-q2-v1/` ; `sha256sum -c` de tous ses compagnons ; lis son
  `LISEZMOI-kirchner-q2-v9-v1.md` (291790aa…) : il porte la commande exacte et l'attente.
- `question.md` `291f91f8…`, `faits.md` `cc202ecd…`, `collisionneur_v9.py` `27e9ce40…`, lanceur `lancer-tour-kirchner-q2-v9-v1.sh` `8c0d3812…`.

## 2. Commande (port 8812 ; aucune autre utilisation d'Argon en cours : vérifie que 8805 est libre)
Depuis `donnees/collisionneur-v9-kirchner-q2-v1/` de ton clone :
```
for f in journal-kirchner-q2-v9-v1.log code-kirchner-q2-v9-v1.txt lanceur-kirchner-q2-v9-v1.pid; do [ ! -e "$f" ] || { echo "$f existe (R12)"; exit 2; }; done && \
GO_ID=GO-2026-11-03-04 PLAFOND_USD=34 PY_COLLISIONNEUR=/home/user/venv-relais-claude/bin/python \
  setsid nohup bash -c 'bash ./lancer-tour-kirchner-q2-v9-v1.sh; echo $? > code-kirchner-q2-v9-v1.txt' \
  > journal-kirchner-q2-v9-v1.log 2>&1 < /dev/null &
echo $! > lanceur-kirchner-q2-v9-v1.pid
```
Puis l'attente suivie par ton harnais (boucle `kill -0` toutes les 60 s, réarmée avant 2 h) jusqu'à la fin. Contrôle d'une espèce en
échec : aucune course ; dis-le-moi (la variante sans Argon n'est permise que si Argon est pris, sur mon mot).

## 3. Après
`collisionneur_v9.py verifier run-kirchner-q2-e3-v1` (attendu 15 cellules valides) ; scellement avant toute lecture (empreintes de
tous les fichiers produits, journal compris) ; branche neuve `donnees/collisionneur-v9-kirchner-q2-v1-run` partie de `16ec2e5a` ;
contrôle des motifs de clé à 0 ; rapport scellé (commit, empreintes, code, durée, dépense par espèce) ; aucun relais restant. Ensuite
seulement, l'ordre de la course de l'organisme Kirchner.
