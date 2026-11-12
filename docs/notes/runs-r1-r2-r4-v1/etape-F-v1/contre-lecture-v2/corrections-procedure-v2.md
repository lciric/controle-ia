# Contre-lecture 2 — corrections de procédure et de code (liste à part) — v2

Aucune correction de code n'est exigée (listes fermées et empreintes du brouillon 2 inchangées). Corrections des
commandes de la mère (rapport v2, section 5) et notes :

- **P1 (à corriger)** — commandes décisives conditionnées au code de fin. Telles qu'écrites, les trois commandes
  s'enchaînent sans test : collées en bloc, un arrêt de la principale laisserait lancer la lecture par épisode et la
  secondaire. Lancer le bloc comme un script (`bash -u`), chaque commande suivie de :
  ```
  c=$? ; echo "code de fin : $c"
  if [ "$c" -ne 0 ]; then grep -m1 '^ARRÊT' journaux/$R1.log ; echo "arrêt, nœud de Lazar" ; exit "$c" ; fi
  ```
  (avec `$R2`, `$R3` aux deux suivantes), avant le scellement du journal et le commit. Un code non nul sans ligne
  `ARRÊT` (exception non prévue) : rien d'autre n'est lu du journal ; signaler à Lazar.
- **P2 (note)** — préalable au lancement, après la récupération : les manifestes du rejeu et de la réparation entrent
  sous `runs/` et sont lus par K2. Compter seulement, sans rien afficher d'autre, leurs occurrences des trois chemins des
  textes, des trois empreintes et du chemin de l'addendum (`grep -c -F`) ; un compte non nul arrêterait les trois
  lectures en code 2 avant tout manifeste (arrêt sans dommage, mais nœud) : le savoir avant de lancer.
- **P3 (note)** — l'épreuve du code de fin 2 en sous-processus (point 7 de la contre-lecture) peut devenir un essai
  (addendum jouet scellé dans un dépôt temporaire) ; ce n'est pas exigé : cela changerait les empreintes des essais,
  donc les listes fermées et le brouillon.
- **P4 (note)** — nommer K3 dans la demande de GO à Lazar avec les deux écarts (arrêt neuf, sens prudent).
