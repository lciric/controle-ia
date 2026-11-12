# Ordre à la fille — course d'idéation Scheurer (GO-2026-11-03-10) — v1

Écrit par session-depot le 3 novembre 2026 vers 14:20 UTC. Destinataire : la fille `session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mot direct de
Lazar : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de plafond ». **Part à la fin de la course Ibrahim**
(mêmes ports 8804 à 8807, relais arrêtés par PID), sans attendre mon mot si les § 1 et 2 sont conformes.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (GO-2026-11-03-10, 237 USD).
- Branche `outils/course-scheurer-v1`, commit **`7997da49`**, extraite sans toucher à l'index :
  `git archive 7997da49 donnees/course-scheurer-v1 docs/notes/ideation-organisme-v1/course-scheurer-v1 docs/notes/ideation-organisme-v1/commandes-a1-bis-v1 | tar -x -C /home/user/controle-ia-travail`.
- Fiche scellée `docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v1.md`
  **`31c8ffd2fbc76924849fe2955a4a2ad1ca35fa1cdb52b1dd6be9535ff6eeb41c`** ; rapport scellé `…/contre-lecture-fiche-lancement-course-scheurer-v1.md`
  **`217bb9773d9aa3b2b3a8c104eea210a586b4471461c250b98726d908740d210e`**.
- `table_pieces_gelees_scheurer_v1.py --verifier <fiche>` → « conforme : 50 pièces ».

## 2. Variante et vérification sans appel (code 0 exigé)
- **Argon libre au départ** (aucun tour ni course ne l'utilise ; port 8805 libre) → `configuration-course-scheurer-v1-sans-opus-argon.json` ;
  sinon `…-sans-opus.json` ; repli `…-sans-opus-sans-kimi.json` si le contrôle de Kimi échoue. **Jamais** `…-juges-opus` ni `…-avec-opus`
  sans mot de Lazar. Opus ne reçoit pas la question (refus au collisionneur, R-486) ; seul son contrôle « OK » du lanceur reste.
- `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-10 /usr/bin/python3 -I -B lancer_course_scheurer_v1.py verifier --configuration <variante> --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-10 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement (garde R12 au premier plan)
```
cd /home/user/controle-ia-travail/donnees/course-scheurer-v1/orchestrateur/scheurer
mkdir -p /home/user/runs-course-scheurer-v1
RUN=/home/user/runs-course-scheurer-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-scheurer-v1/contre-lecture-fiche-lancement-course-scheurer-v1.md
GO_ID=GO-2026-11-03-10 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-scheurer-v1.sh lancer \
  GO-2026-11-03-10 <variante> "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
PID réel lu au processus ; garde de session suivie jusqu'à la fin ; arrêt par PID seulement.

## 4. Après
Sortie scellée ; ne rien lire ; branche neuve `donnees/course-scheurer-v1-run` partie de `main` ; contrôle des clés ; rapport scellé
(variante jouée, fiches, aiguilleur par classe et espèce, refus, mariages, coûts par espèce) ; message dès la fin (je copie au canal).
