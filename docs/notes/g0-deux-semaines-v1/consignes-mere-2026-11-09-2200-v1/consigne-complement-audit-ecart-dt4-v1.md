# Consigne : complément de l'audit de l'écart DT-4 (avant le scellement de T0.6 r4) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-10 (`date -u`). Destinataire : l'auditeur de `audit-ecart-dt4-7a-v1.md` (`4882fe4d…`), qui reste exclu de T0.6, T0.7, P3-bis et G0.

Mêmes interdits et même limite que la consigne v1 (`consigne-audit-ecart-dt4-7a-v1.md`, `ca5024ae…`) : ni `lecture-sondes-t06.json` (nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json`) ni la branche `donnees/lecture-b-7a-quarantaine-v1` ouverts ; ni `diag/` ni `runs/` de 7a, ni `essai/t06-explo-v3` ; ni `donnees/bras-attaque*`, ni `donnees/mode-tenu-a-l-ecart*`, ni `docs/notes/bras-attaque/` ; ni l'étiqueteur ; jamais `extraire_mesures_epreuve_t06_v1.py` ; aucune valeur de clé ; aucun appel externe ; git en lecture seule ; ne pas toucher `/home/user/integ-t06` ni `/tmp/.../essai-S/`.

## Travail

1. Rejouer `verifier_ecart_dt4_v1.py` (inchangé ; s'il faut l'étendre, version neuve `…_v2.py`, R12) sur la plage `62ba4a4a..` la tête de `main` au moment du lancement (dire laquelle), lignes ajoutées.
2. Pièces nommées, texte entier : la contre-lecture 3 et ses couples ; tout `brouillons/ii-b-saboteur-budget-v1/` (brouillons 1 et 2, contre-lecture 1, simulations, journaux) ; les deux rapports de `docs/notes/g0-deux-semaines-v1/integration-t06-v13-main-v1/` ; la r4, son journal, ses couples et la variante (a) ; les consignes de la série postérieures à `62ba4a4a` ; `registres/decisions.md` R-2052 à la dernière ligne.
3. Classement (i), (ii), (iii) comme en v1 ; le rapport ne cite aucun nombre d'une occurrence (iii). Cas connus à traiter explicitement : les grandeurs de coût de 7a (réserve 1 de v1) recopiées dans les « avant » de couples de la r4 et dans la variante (a), et le 20 % d'illisibles du dossier (ii-b) brouillon 1 (retiré au brouillon 2).
4. Le différentiel r3 → r4 contient-il un élément C1 à C7 de 7a ?

## Sorties

`docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-complement-v1.md`, sortie JSON du script `…/audit-ecart-dt4-7a-v1/sortie-verifier-ecart-dt4-complement-v1.json` (et script v2 s'il y en a un), compagnons `.sha256`. Verdict en une ligne, réserves. Rien committé.
