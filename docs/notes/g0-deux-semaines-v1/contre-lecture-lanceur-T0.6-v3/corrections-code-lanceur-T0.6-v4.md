# Corrections de code proposées au lanceur T0.6 (versions neuves, R12 : amorce v4) — v1

Contre-lecture du lanceur T0.6 v3 (`4f1b402d`), fille 9, 5 novembre 2026. Chaque correction : un cas sain et un artefact (R5), et une mutation au banc.

- **C-V4-1 (à corriger)** — fin de run de l'amorce sous le verrou de consignation.
  - Les commits et poussées de la fin de run (résultats et données légères, morceaux, traces) prennent le même verrou `flock` que `t06-consigner.sh` (`exec 9>>"$R/t06-consigner.lock"; flock -w 1500 9`), relâché avant `arreter_instance`.
  - `commit_verifie` distingue « rien à committer » (`git diff --cached --quiet` vrai) d'un commit en échec (`index.lock`, autre) : un échec est journalisé « ERREUR DE CHAÎNE », réessayé une fois, et sinon consigné.
  - Avant de poser `t06-fin-normale` : `git status --porcelain -- runs diag donnees` vide ; sinon, `consigner_partiel "fin de run"`.
  - Artefacts :
    - `index.lock` posé pendant la fin de run : commit réessayé, puis consigné ;
    - minuterie à l'échéance pendant la poussée finale : aucun fichier de résultat perdu, l'ordre des commits est gardé.
- **C-V4-2 (facultative)** — `familles_v2.verifier_egalite_au_paquet_gele` : en plus des 256 jetons tirés autour de μ, 256 jetons réels pris dans les premières actions notées du couple, même tolérance. Le coût est d'environ 7 s par sonde sous le paquet gelé.
