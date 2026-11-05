# Ordre à la fille — seconde course Ibrahim Q1, cinq espèces avec Argon (GO-2026-11-03-18) — v1

Écrit par session-depot le 3 novembre 2026 vers 18:27 UTC. Destinataire : la fille `session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mots directs de
Lazar : « oui : Scheurer à trois espèces, Ibrahim à cinq » puis « ibrahim en premier ». **Part tout de suite** si les § 1 et 2 sont
conformes ; la course Scheurer sans Claude suivra par un ordre à part.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (ligne GO-2026-11-03-18, 198 USD).
- Kit `outils/course-ibrahim-q1-v1` `965eb21b` déjà extrait chez toi (course du midi) : revérifie ses empreintes, ou réextrais par
  `git archive 965eb21b donnees/course-ibrahim-q1-v1 docs/notes/ideation-organisme-v1/course-ibrahim-q1-v1 | tar -x -C /home/user/controle-ia-travail`.
- Fiche scellée `…/course-ibrahim-q1-v1/fiche-lancement-course-ibrahim-q1-v1.md` `32ecac7aa0fc93b248c9c565a21486e02e3b4d305aad0cbb841323e3dc7674f2` ;
  rapport `…/contre-lecture-fiche-lancement-course-ibrahim-q1-v1.md` `8a6838ac8d0774df88fdd19b8cc9c9a5712d8c7646388e13a0ba3afed3f789a0`.
- Configuration **cinq espèces** `configuration-course-ibrahim-q1-v2-cinq-especes.json` `41feac66…` ; lanceur `lancer-course-ibrahim-v2.sh`.
- Argon libre (port 8805, aucun autre usage).

## 2. Vérification sans appel (code 0 exigé)
`env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-18 /usr/bin/python3 -I -B lancer_course_ibrahim_v1.py verifier --configuration configuration-course-ibrahim-q1-v2-cinq-especes.json --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-18 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement (garde R12 au premier plan ; dossier de run NEUF)
```
cd /home/user/controle-ia-travail/donnees/course-ibrahim-q1-v1/orchestrateur/ibrahim
RUN=/home/user/runs-course-ibrahim-q1-v1/run-$(date -u +%Y%m%d-%H%M)-cinq-especes
GO_ID=GO-2026-11-03-18 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup setsid bash lancer-course-ibrahim-v2.sh lancer \
  GO-2026-11-03-18 configuration-course-ibrahim-q1-v2-cinq-especes.json "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
(F et C : la fiche et le rapport du § 1.) Repli `…-v2-avec-kimi.json` seulement si le contrôle d'Argon échoue — et alors dis-le-moi
aussitôt : Lazar rechargera les crédits. Refus d'une espèce : elle sort, rien ne se rejoue. PID réel ; garde de session ; arrêt par PID.

## 4. Après
Sortie scellée ; ne rien lire ; branche neuve `donnees/course-ibrahim-q1-seconde-v1-run` partie de `main` ; contrôle des clés ; rapport
scellé (variante, fiches par espèce, aiguilleur, mariages, coûts, refus) ; message dès la fin. Puis la course Scheurer (ordre à part).
