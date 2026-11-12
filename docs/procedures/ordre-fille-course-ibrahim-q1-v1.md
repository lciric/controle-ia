# Ordre à la fille — course d'idéation Ibrahim Q1 (GO-2026-11-03-09) — v1

Écrit par session-depot le 3 novembre 2026 vers 12:13 UTC (heure relevée par `date -u` à 12:10:21). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mot direct de Lazar : « go trois tours et course Ibrahim ; pas de plafond ». Dépôt Pivotal ce soir
23:00 UTC. **Elle utilise les ports 8804 à 8807 de la course Kirchner : elle part à la fin de la course Kirchner, relais arrêtés par PID**,
sans attendre mon mot si les § 1 et 2 sont conformes.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (GO-2026-11-03-09, 198 USD).
- Branche `outils/course-ibrahim-q1-v1`, commit **`965eb21b`**, extraite sans toucher à l'index :
  `git archive 965eb21b donnees/course-ibrahim-q1-v1 docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1 | tar -x -C /home/user/controle-ia-travail`
  (les commandes A1-bis déjà en place servent ; vérifie leurs empreintes).
- Fiche scellée `docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/fiche-lancement-course-ibrahim-q1-v1.md`
  **`32ecac7aa0fc93b248c9c565a21486e02e3b4d305aad0cbb841323e3dc7674f2`** ; rapport scellé `…/contre-lecture-fiche-lancement-course-ibrahim-q1-v1.md`
  **`8a6838ac8d0774df88fdd19b8cc9c9a5712d8c7646388e13a0ba3afed3f789a0`** ; configuration de lancement **quatre espèces sans Argon**
  `donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim/configuration-course-ibrahim-q1-v2-avec-kimi.json` `5b4fe587…` (cinq espèces
  `…-v2-cinq-especes.json` `41feac66…` seulement si Argon est libre et aucun tour ne l'attend) ; lanceur `lancer-course-ibrahim-v2.sh` `3cba586c…`.
- `table_pieces_gelees_ibrahim_v2.py --verifier <fiche>` → « conforme : 55 pièces ».

## 2. Vérification sans appel (code 0 exigé)
Dans `…/ibrahim/` : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-09 /usr/bin/python3 -I -B lancer_course_ibrahim_v1.py verifier --configuration configuration-course-ibrahim-q1-v2-avec-kimi.json --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-09 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement, à la fin de la course Kirchner (ports 8804 à 8807 libres)
Garde R12 au premier plan, puis :
```
cd /home/user/controle-ia-travail/donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim
mkdir -p /home/user/runs-course-ibrahim-q1-v1
RUN=/home/user/runs-course-ibrahim-q1-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/fiche-lancement-course-ibrahim-q1-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1/contre-lecture-fiche-lancement-course-ibrahim-q1-v1.md
GO_ID=GO-2026-11-03-09 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-ibrahim-v2.sh lancer \
  GO-2026-11-03-09 configuration-course-ibrahim-q1-v2-avec-kimi.json "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
PID réel lu au processus ; garde de session suivie par ton harnais jusqu'à la fin. Repli : `…-v2-sans-kimi.json` si le contrôle de Kimi
échoue. Arrêt par PID seulement.

## 4. Après
Sortie scellée par le lanceur ; ne rien lire ; branche neuve `donnees/course-ibrahim-q1-v1-run` partie de `main` ; contrôle des clés (seul
le faux positif connu de `caviardage.py`) ; rapport scellé (fiches, aiguilleur par classe et par espèce, mariages, coûts par espèce) ;
message dès la fin (je copie au canal).
