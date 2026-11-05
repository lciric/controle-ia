# Revalidation de T0.5 — outils de scellement et de lancement (v1)

Outils de la session du 2026-10-10 qui ont servi au scellement de `prereg/T0.5-revalidation-equivalence-pilote-v1.md`
(commit 4014e57) et qui serviront au lancement. Plan : `plan-lancement-revalidation-v4.md`. Ils ont été relus par quatre
vérifications de sous-agents neufs (rapports sous `prereg/contre-lectures/T0.5-revalidation-verification-remplissage-*`).

- `lancer_revalidation_v3.sh OFFRE DOSSIER` : création de l'instance en un seul appel ; il rejoue lui-même
  `controles_avant_depense_v3.sh` sur le commit de scellement, vérifie le prix (≤ 1,30 USD l'heure) et le crédit
  (≥ 6 h × prix + 0,9 USD), l'amorce, la garde de calcul. Code 3 : crédit ou prix (nœud).
- `controles_avant_depense_v3.sh S DOSSIER` : contrôles sur un clone neuf ; sortie au commit 4014e57 :
  `controles-avant-depense-4014e57.txt` (23 contrôles conformes).
- `remplir_revalidation_v4.py`, `sceller_revalidation_v2.sh`, `registres_scellement_v2.py`, `etat_scellement.py` : le
  scellement (déjà fait ; ne pas rejouer : R12). `exporter_verification.py` : export des rapports des sous-agents.
  `repetition_jouet_v2.sh` : répétition jouet de l'amorce sur un dépôt jetable.

Chemins propres à la session : les scripts nomment le bloc-notes de la session du 2026-10-10
(`/tmp/claude-0/-home-user/5a6b9d1d-…/scratchpad`). Une autre session adapte la variable `B` (lanceur) et `PY`
(contrôles), et recrée deux environnements : `venv-vastai` (`pip install vastai==1.8.3`) et `venv-gpu-neuf`
(`python3.11 -m venv` puis `pip install -r requirements-gpu.txt`). Jamais de `vastai show instance --raw` sans filtre.
