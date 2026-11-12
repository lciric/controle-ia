# Ordre à la fille — course d'idéation Heimersheim (GO-2026-11-03-02) — v1

Écrit par session-depot le 3 novembre 2026 à 08:27 UTC (heure relevée par `date -u` à 08:26:32). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mots de Lazar à session-depot : « go heimersheim sans plafond » et « go lance heimersheim dès
que le devis est prêt ». Course non décisive ; sortie lue par Lazar comme matière à réflexion.

## 1. Sources (vérifie chaque empreinte ; tout écart : rien ne part, tu me l'écris)
- `main` tiré en avance rapide (la ligne GO-2026-11-03-02, 244 USD, doit être dans `registres/go.md` de ton clone).
- Branche `outils/course-heimersheim-v1`, commit **`6d2b3c4c`**, récupérée par refspec explicite, puis extraite **sans toucher à
  l'index ni à `main`** : `git archive 6d2b3c4c donnees/course-heimersheim-v1 docs/notes/ideation-organisme-v1/course-heimersheim-v1 docs/notes/ideation-organisme-v1/commandes-a1-bis-v1 | tar -x -C /home/user/controle-ia-travail`.
- Fiche de lancement scellée : `docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1.md`,
  **`f4915d9c750b1050261435f191294e275c5b3ed9956bd20efc41eea90a8b5ed2`** ; rapport de contre-lecture scellé :
  `…/contre-lecture-fiche-lancement-course-heimersheim-v1.md`, **`18e7c5011a175305fd7975437679c0730b9f024f641a3fedad03d006ad73db17`**.
- Configuration de lancement : `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v2-cinq-especes.json`,
  **`5eb0f1af48f176c0599a7a79acb554df43d90e1acac4f84a699af129da589788`** ; lanceur `lancer-course-heimersheim-v3.sh`
  `337e91949a1a8bbbcc6443748a24c591312ec9d8f9fb92d2862c7aa2376a0fdd`.
- Contrôle de la table : `/usr/bin/python3 -I -B table_pieces_gelees_heimersheim_v3.py --verifier <fiche>` → « conforme : 43 pièces ».

## 2. Vérification sans appel ni écriture (code 0 exigé ; sortie gardée au journal)
Dans `…/heimersheim/` : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-02 /usr/bin/python3 -I -B lancer_course_heimersheim_v2.py verifier --configuration configuration-course-heimersheim-v2-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-02 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement — **seulement après mon « lance »** (mon appel seul à Argon doit être fini : jamais deux usages d'Argon en même temps)
```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
mkdir -p /home/user/runs-course-heimersheim-v1
RUN=/home/user/runs-course-heimersheim-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-heimersheim-v1/contre-lecture-fiche-lancement-course-heimersheim-v1.md
GO_ID=GO-2026-11-03-02 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-heimersheim-v3.sh lancer \
  GO-2026-11-03-02 configuration-course-heimersheim-v2-cinq-especes.json "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
echo "PID du lanceur : $!"
```
- **Session active jusqu'à la fin** (≈ 5 h attendues, délai 12 h) : une commande en arrière-plan **suivie par ton harnais** qui attend la
  fin du PID du lanceur (`while kill -0 PID; do sleep 60; done`), réarmée avant son délai de 2 h ; jamais la seule relève horaire.
- Replis, dans l'ordre et seulement sur échec du contrôle concerné (aucune course partie) : `configuration-course-heimersheim-v2-avec-kimi.json`
  (contrôle d'Argon en échec), puis `…-v2-sans-kimi.json` (contrôle de Kimi en échec) ; dis-moi lequel.
- Arrêt (R10) : `kill <PID du lanceur>` seulement ; jamais par motif.

## 4. Après
La sortie est scellée par le lanceur avant toute lecture ; ne lis rien du contenu. Verse le dossier du run sur une branche de données
neuve `donnees/course-heimersheim-v1-run`, partie de `main` (contrôle des clés : seul le faux positif connu de `caviardage.py` admis,
s'il apparaît) ; rapport scellé : commit, empreintes, code de sortie, durée, nombre de fiches, refus de l'aiguilleur, quarantaines,
mariages par bras, coûts par espèce (registre et relevés des relais), heures `date -u`. Aucun relais ne reste (PID vérifiés).
