# Ordre à la fille — course d'idéation Kirchner Q2 (GO-2026-11-03-05) — v1

Écrit par session-depot le 3 novembre 2026 à 10:40 UTC (heure relevée par `date -u` à 10:39:14). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mots directs de Lazar à session-depot : « je eux que Kirchner Q2 passe avant A1-v3 » et « go
Kirchner sans plafond ». **Elle ne part qu'après la fin du tour du collisionneur Kirchner (GO-2026-11-03-04) et l'arrêt de son relais
par PID** : jamais deux usages d'Argon à la fois. Même discipline que la course Heimersheim (`ordre-fille-course-heimersheim-v1.md`).

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré en avance rapide (GO-2026-11-03-05, 245 USD, au registre).
- Branche `outils/course-kirchner-q2-v1`, commit **`53e1f738`**, extraite sans toucher à l'index :
  `git archive 53e1f738 donnees/course-kirchner-q2-v1 docs/notes/ideation-organisme-v1/course-kirchner-q2-v1 docs/notes/ideation-organisme-v1/commandes-a1-bis-v1 | tar -x -C /home/user/controle-ia-travail`
  (les commandes A1-bis sont identiques à celles déjà extraites pour Heimersheim).
- Fiche scellée `docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/fiche-lancement-course-kirchner-q2-v1.md`
  **`9234a09a5fa87062fcd79864070428933d6852f4975ef7b443c322ab80161630`** ; rapport scellé `…/contre-lecture-fiche-lancement-course-kirchner-q2-v1.md`
  **`b70b0ec7748b48cca3d5da7db973df97323c811aaa81317ea5f481dd66cac580`** ; configuration de lancement
  `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v2-cinq-especes.json` **`4211e9ba…`** ; lanceur
  `lancer-course-kirchner-v2.sh` `2840b238…`.
- `table_pieces_gelees_kirchner_v2.py --verifier <fiche>` → « conforme : 49 pièces ».

## 2. Vérification sans appel (code 0 exigé)
Dans `…/kirchner/` : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-05 /usr/bin/python3 -I -B lancer_course_kirchner_v1.py verifier --configuration configuration-course-kirchner-q2-v2-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-05 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement, après la fin du tour Kirchner (sur ton constat, sans attendre mon mot si les § 1 et 2 sont conformes et le relais du tour arrêté)
Lance la garde R12 d'abord au premier plan, puis :
```
cd /home/user/controle-ia-travail/donnees/course-kirchner-q2-v1/orchestrateur/kirchner
mkdir -p /home/user/runs-course-kirchner-q2-v1
RUN=/home/user/runs-course-kirchner-q2-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/fiche-lancement-course-kirchner-q2-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/contre-lecture-fiche-lancement-course-kirchner-q2-v1.md
GO_ID=GO-2026-11-03-05 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-kirchner-v2.sh lancer \
  GO-2026-11-03-05 configuration-course-kirchner-q2-v2-cinq-especes.json "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
PID réel du lanceur lu au processus ; garde de session suivie par ton harnais (relevés toutes les 2 min) jusqu'à la fin. Replis :
`…-v2-avec-kimi.json` (contrôle d'Argon en échec), puis `…-v2-sans-kimi.json` (contrôle de Kimi en échec). Arrêt par PID seulement.

## 4. Après
Sortie scellée par le lanceur ; ne rien lire ; branche neuve `donnees/course-kirchner-q2-v1-run` partie de `main` ; contrôle des clés
(seul le faux positif connu de `caviardage.py` admis) ; rapport scellé avec les nombres par classe de l'aiguilleur et par espèce (CLK-02),
fiches, mariages, coûts par espèce ; aucun relais restant. Puis la seconde course d'A1-v3, **sur mon « lance »**.
