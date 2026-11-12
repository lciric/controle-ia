# Ordre à la fille — course d'idéation Colognese et Ward Q2 (GO-2026-11-03-11) — v1

Écrit par session-depot le 3 novembre 2026 vers 14:21 UTC (heure relevée par `date -u` à 14:20:19). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mot direct de Lazar : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de
plafond ». **Part à la fin de la course Scheurer** (mêmes ports 8804 à 8807, relais arrêtés par PID), sans attendre mon mot si les § 1 et 2
sont conformes.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (GO-2026-11-03-11, 198 USD).
- Branche `outils/course-colognese-ward-q2-v1`, commit **`f56beeee`**, extraite sans toucher à l'index :
  `git archive f56beeee donnees/course-colognese-ward-q2-v1 docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1 | tar -x -C /home/user/controle-ia-travail`
  (commandes A1-bis déjà en place : empreintes vérifiées).
- Fiche scellée `docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v1.md`
  **`cd4f53a5cb9fb82189f36dbbce015b59805c44b989917406189bd685db5983e2`** ; rapport scellé `…/contre-lecture-fiche-lancement-course-colognese-ward-q2-v1.md`
  **`6c8df845d77361d9bec60a9a9ea30f9f6acaf2b57f71d38ec9ceda410c68bfcf`**.
- `table_pieces_gelees_colognese_v1.py --verifier <fiche>` → « conforme : 49 pièces ».

## 2. Variante et vérification sans appel (code 0 exigé)
- **Argon libre au départ** → `configuration-course-colognese-ward-q2-v1-cinq-especes.json` (`63e48ad9…`) ; sinon `…-avec-kimi.json` ;
  repli `…-sans-kimi.json` si le contrôle de Kimi échoue.
- Dans `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/` : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-11 /usr/bin/python3 -I -B lancer_course_colognese_v1.py verifier --configuration <variante> --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-11 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement (garde R12 au premier plan)
```
cd /home/user/controle-ia-travail/donnees/course-colognese-ward-q2-v1/orchestrateur/colognese
mkdir -p /home/user/runs-course-colognese-ward-q2-v1
RUN=/home/user/runs-course-colognese-ward-q2-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/contre-lecture-fiche-lancement-course-colognese-ward-q2-v1.md
GO_ID=GO-2026-11-03-11 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-colognese-v1.sh lancer \
  GO-2026-11-03-11 <variante> "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
PID réel lu au processus ; garde de session suivie jusqu'à la fin ; arrêt par PID seulement.

## 4. Après
Sortie scellée ; ne rien lire ; branche neuve `donnees/course-colognese-ward-q2-v1-run` partie de `main` ; contrôle des clés ; rapport
scellé (variante, fiches par espèce — dis pourquoi Kimi manque au compte s'il manque encore —, aiguilleur, mariages, coûts) ; message dès
la fin.
