# Ordre à la fille — course Scheurer sans Claude (GO-2026-11-03-17) — v1

Écrit par session-depot le 3 novembre 2026 vers 18:32 UTC (heure relevée par `date -u` à 18:31:14). Destinataire : la fille
`session_01XJ6Mgq5AWikCJZKnsMkbRZ`. Mots directs de Lazar : « oui : Scheurer à trois espèces, Ibrahim à cinq », « ibrahim en premier ».
Décision de session-depot sur le fond lu : R-1170. **Part à la fin de la seconde course Ibrahim** (mêmes ports, relais arrêtés par PID ;
un seul usage d'Argon à la fois), sans attendre mon mot si les § 1 et 2 sont conformes.

## 1. Sources (empreintes vérifiées ; tout écart : rien ne part)
- `main` tiré (ligne GO-2026-11-03-17, 130 USD).
- Branche `outils/course-scheurer-v1`, commit **`780cb712`**, extraite sans toucher à l'index :
  `git archive 780cb712 donnees/course-scheurer-v1 docs/notes/ideation-organisme-v1/course-scheurer-v1 | tar -x -C /home/user/controle-ia-travail`.
- Fiche scellée `docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v2.md`
  **`3523370b0d6639c352d5f614d61e1507f9c560632da1d7438c4974eb71ab6746`** ; rapport `…/contre-lecture-fiche-lancement-course-scheurer-v2-brouillon1.md`
  **`926ed6ff3232d693e97e1690ee3dc32ceb2963e6ec77746ec54ecaec007e4f62`** ; levée du retrait `…/levee-retrait-variante-sans-claude-v1.md` `4f004270…`.
- Configuration `configuration-course-scheurer-v1-sans-claude.json` `ff8e5dd2…` ; lanceur `lancer-course-scheurer-v2.sh` `9391a28d…`.
- `table_pieces_gelees_scheurer_v2.py --verifier <fiche>` → « conforme : 61 pièces ».

## 2. Vérification sans appel (code 0 exigé)
`env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=/tmp GO_ID=GO-2026-11-03-17 /usr/bin/python3 -I -B lancer_course_scheurer_v2.py verifier --configuration configuration-course-scheurer-v1-sans-claude.json --registre-go /home/user/controle-ia-travail/registres/go.md --go-attendu GO-2026-11-03-17 --preenregistrement <fiche> --contre-lecture <rapport>`.

## 3. Lancement (garde R12 au premier plan ; dossier de run NEUF)
```
cd /home/user/controle-ia-travail/donnees/course-scheurer-v1/orchestrateur/scheurer
RUN=/home/user/runs-course-scheurer-v1/run-$(date -u +%Y%m%d-%H%M)-sans-claude
GO_ID=GO-2026-11-03-17 nohup setsid bash lancer-course-scheurer-v2.sh lancer GO-2026-11-03-17 \
  configuration-course-scheurer-v1-sans-claude.json "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
(F et C : fiche et rapport du § 1 ; pas de `PY_RELAIS_CLAUDE`.) Aucun relais Claude ne démarre. Contrôle d'Argon en échec : dis-le-moi
aussitôt (crédits). Refus ou arrêt : aucune relance. PID réel ; garde de session ; arrêt par PID.

## 4. Après
Sortie scellée ; ne rien lire ; branche neuve `donnees/course-scheurer-v2-run` partie de `main` ; contrôle des clés ; rapport scellé
(fiches par espèce, aiguilleur, mariages, coûts dont **dépense d'Argon au registre cumulé**, refus, et comptes des notes d'Astra juge
sur les fiches d'Astra à part des autres — comptes seulement) ; message dès la fin.
