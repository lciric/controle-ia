# Ordre à la fille — course d'idéation Jang-Feng (GO-2026-11-03-12, replis GO-13 et GO-14) — v1

Écrit par session-depot le 3 novembre 2026 vers 14:42 UTC (heure relevée par `date -u` à 14:40:50). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mot direct de Lazar : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de
plafond ». **Part à la fin de la course Colognese-Ward** (mêmes ports 8804 à 8807, relais arrêtés par PID), sans attendre mon mot si
les § 1 et 2 sont conformes.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (lignes GO-2026-11-03-12 à 198 USD, -13 à 237 USD, -14 à 198 USD).
- Branche `outils/course-jang-feng-v1`, commit **`242fef32`**, extraite sans toucher à l'index :
  `git archive 242fef32 donnees/course-jang-feng-v1 docs/notes/ideation-organisme-v1/course-jang-feng-v1 | tar -x -C /home/user/controle-ia-travail`
  (commandes A1-bis déjà en place : empreintes vérifiées).
- Fiche scellée `docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v1.md`
  **`e9141940ec6ff1ee6bb19f8b0f5d5f5236b6098eb779c7384bdf89e853da58ce`** ; rapport scellé
  `…/contre-lecture-fiche-lancement-course-jang-feng-v1-brouillon2.md` **`08b62bdc951d1d614e836bd5ae292d45bd675dcacece9fc8c424850ff45b29d8`**.
- `table_pieces_gelees_jangfeng_v2.py --verifier <fiche>` → « conforme : 60 pièces ».
- Lanceur **v2** : `lancer-course-jangfeng-v2.sh` (`13d08682…`) et `lancer_course_jangfeng_v2.py`. Lis le § 2 et le § 10 de la fiche.

## 2. Variante, ligne de GO et vérification sans appel (code 0 exigé)
| Run | Variante | Ligne (`GO_ID` et 2ᵉ argument) |
|---|---|---|
| premier, Argon libre | `configuration-course-jang-feng-v1-cinq-especes.json` | GO-2026-11-03-12 |
| premier, Argon pris | `…-avec-kimi.json` | GO-2026-11-03-12 |
| premier, contrôle de Kimi en échec | `…-sans-kimi.json` | GO-2026-11-03-12 |
| repli après refus d'Opus, Argon libre | `…-sans-opus-argon.json` | **GO-2026-11-03-13** |
| repli après refus d'Opus, Argon pris | `…-sans-opus.json` | **GO-2026-11-03-14** (et non GO-12 comme l'écrit le LISEZMOI v2 : la fiche scellée prime) |

Dans `donnees/course-jang-feng-v1/orchestrateur/jangfeng/` : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=<ligne> /usr/bin/python3 -I -B lancer_course_jangfeng_v2.py verifier --configuration <variante> --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu <ligne> --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement (garde R12 au premier plan)
```
cd /home/user/controle-ia-travail/donnees/course-jang-feng-v1/orchestrateur/jangfeng
mkdir -p /home/user/runs-course-jang-feng-v1
RUN=/home/user/runs-course-jang-feng-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-jang-feng-v1/contre-lecture-fiche-lancement-course-jang-feng-v1-brouillon2.md
GO_ID=<ligne> PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-jangfeng-v2.sh lancer \
  <ligne> <variante> "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
PID réel lu au processus ; garde de session suivie jusqu'à la fin ; arrêt par PID seulement.

## 4. Repli (déclaré d'avance, fiche § 2 et § 10)
Seulement si le **refus d'Opus** est constaté dans le journal du relais Claude 8806 et le manifeste de fin du premier run (statut de
refus pour `claude-opus-5-5`), lus sans le texte des réponses : sceller d'abord la sortie du premier run, puis relancer dans un
**dossier de run neuf** selon le tableau du § 2, sans rien rejouer à Opus. Tout autre arrêt (autre espèce, panne d'un fournisseur,
échec technique) : **pas de repli**, message à session-depot.

## 5. Après
Sortie scellée ; ne rien lire ; branche neuve `donnees/course-jang-feng-v1-run` partie de `main` (avec le premier run arrêté s'il
y a eu repli) ; contrôle des clés ; rapport scellé (variante, ligne de GO, fiches par espèce — dis si Kimi manque au compte —,
aiguilleur, mariages, coûts, refus éventuel d'Opus) ; message dès la fin. Ensuite plus aucune course : Argon reste libre pour la
seconde course d'A1-v3, **sur mon « lance »**.
