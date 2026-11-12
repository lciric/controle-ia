# Ordre à la fille — relance de la course Colognese et Ward Q2 sans Opus (GO-2026-11-03-16 ou -15) — v1

Écrit par session-depot le 3 novembre 2026 vers 15:23 UTC (heure relevée par `date -u` à 15:22:03). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mot direct de Lazar : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de
plafond ». Premier run arrêté en C13 sur un refus d'Opus, Fable OK (`donnees/course-colognese-ward-q2-v1-run` `53baefe6`, R-1164).
**Part à la fin de la course Jang-Feng** (et de son repli éventuel), mêmes ports 8804 à 8807, relais arrêtés par PID, sans attendre
mon mot si les § 1 et 2 sont conformes.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (lignes GO-2026-11-03-15 à 198 USD et -16 à 237 USD, inscrites à `c266f6a2`).
- Branche `outils/course-colognese-ward-q2-v1`, commit **`eb90ad4e`**, extraite sans toucher à l'index :
  `git archive eb90ad4e donnees/course-colognese-ward-q2-v1 docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1 | tar -x -C /home/user/controle-ia-travail`.
- Fiche scellée `docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v2.md`
  **`aff403e1da01b81a7b594d1bdc7c92013fc11d28f80cb548b09f51f945f065a9`** ; rapport scellé
  `…/contre-lecture-fiche-lancement-course-colognese-ward-q2-v1-brouillon2.md` **`6f586bd05b8af953dd8c0c66f0ff5b1aef383094dff1c5b25ecffe1620c35220`**.
- `table_pieces_gelees_colognese_v2.py --verifier <fiche>` → « conforme : 61 pièces ». Lanceur **v2** (`lancer-course-colognese-v2.sh`
  `43ea777e…`, `lancer_course_colognese_v2.py`).

## 2. Variante, ligne et vérification sans appel (code 0 exigé)
| Argon au départ | Variante | Ligne (`GO_ID` et 2ᵉ argument) |
|---|---|---|
| libre | `configuration-course-colognese-ward-q2-v1-sans-opus-argon.json` (`9aa94613…`) | **GO-2026-11-03-16** |
| pris | `configuration-course-colognese-ward-q2-v1-sans-opus.json` (`696b9e97…`) | **GO-2026-11-03-15** (jamais GO-11 ni GO-14) |

Dans `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/` : `env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=<ligne> /usr/bin/python3 -I -B lancer_course_colognese_v2.py verifier --configuration <variante> --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu <ligne> --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement (garde R12 au premier plan ; commande du § 7 de la fiche)
```
cd /home/user/controle-ia-travail/donnees/course-colognese-ward-q2-v1/orchestrateur/colognese
mkdir -p /home/user/runs-course-colognese-ward-q2-v1
RUN=/home/user/runs-course-colognese-ward-q2-v1/run-$(date -u +%Y%m%d-%H%M)-sans-opus
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v2.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/contre-lecture-fiche-lancement-course-colognese-ward-q2-v1-brouillon2.md
GO_ID=<ligne> PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-colognese-v2.sh lancer \
  <ligne> <variante> "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
PID réel lu au processus ; garde de session suivie jusqu'à la fin ; arrêt par PID seulement.

## 4. Arrêts sans relance
Refus de Fable (proposeur ou rôle) ; échec du contrôle d'Opus avant la course ; tout autre arrêt : **aucune relance**, sortie scellée,
message à session-depot.

## 5. Après
Sortie scellée ; ne rien lire ; branche neuve `donnees/course-colognese-ward-q2-v2-run` partie de `main` ; contrôle des clés ; rapport
scellé (variante, ligne, fiches par espèce — Kimi —, aiguilleur, mariages, coûts, refus éventuels) ; message dès la fin. Ensuite plus
aucune course : Argon reste libre pour A1-v3, **sur mon « lance »**.
