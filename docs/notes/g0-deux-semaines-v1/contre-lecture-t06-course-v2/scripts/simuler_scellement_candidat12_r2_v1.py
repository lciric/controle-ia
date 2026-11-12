"""Simule le remplissage des quatre marqueurs restants du candidat 12 r2 par des valeurs factices de la bonne forme, puis applique
le contrôle de conformité des préenregistrements du dépôt (`controle_ia.prereg.problemes`, appelé par `sceller_prereg` et
`exiger_prereg_scelle`) et les lectures de la chaîne (motifs du lanceur v12 `controles`, `lire_unique` de l'amorce v10).
Écrit seulement la copie remplie dans DOSSIER_JETABLE.

Usage : python -I simuler_scellement_candidat12_r2_v1.py ARBRE CANDIDAT_R2 DOSSIER_JETABLE [--couples COUPLES.json]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ARBRE, CAND, JET = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(ARBRE / "src"))
from controle_ia import prereg  # noqa: E402

t = CAND.read_text(encoding="utf-8")
if "--couples" in sys.argv:
    for c in json.loads(Path(sys.argv[sys.argv.index("--couples") + 1]).read_text(encoding="utf-8")):
        n = t.count(c["ancien"])
        if n != 1:
            raise SystemExit(f"couple {c['id']} : « ancien » trouvé {n} fois")
        t = t.replace(c["ancien"], c["nouveau"])
avant = {m: t.count(m) for m in sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t)))}
FACTICES = {"<<COMMIT_CODE_T06>>": "0" * 40, "<<EMPREINTES_CODE_T06>>": "a" * 64, "<<EMPREINTE_AMORCE_T06>>": "69b669e176e5cb09a48a012c2ce961a36ca09e1c0a022fa179c842e5220308b3",
            "<<VALEURS_CITEES_T06>>": "b" * 64}
# le marqueur des valeurs citées porte deux valeurs (empreinte canonique et chemin) : remplissage par occurrence, comme le ferait la mère
t2 = t.replace("Configuration de T0.6 (empreinte canonique) : `<<VALEURS_CITEES_T06>>`", "Configuration de T0.6 (empreinte canonique) : `" + "b" * 64 + "`")
t2 = t2.replace("Chemin de la configuration de T0.6 : `<<VALEURS_CITEES_T06>>`", "Chemin de la configuration de T0.6 : `prereg/config-t06-reel-v1.json`")
for m, v in FACTICES.items():
    t2 = t2.replace(m, v)
JET.mkdir(parents=True, exist_ok=True)
copie = JET / "candidat12-r2-rempli-factice.md"
copie.write_text(t2, encoding="utf-8")
motifs = ["Entropie : `[0-9]+`", "Configuration de T0.6 \\(empreinte canonique\\) : `[0-9a-f]{64}`", "Tâches d'évaluation de T0.6 : `[0-9a-f]{64}`",
          "Tests attendus : `[0-9]+`", "Chemin de la configuration de T0.6 : `[^`]+`", "Chemin des tâches d'évaluation de T0.6 : `[^`]+`",
          "Chemin des tâches de distillation de T0.6 : `[^`]+`", "Chemin des consignes de P3 : `[^`]+`"]
lignes = t2.splitlines()
plie = " ".join(t2.replace("\n", " ").split())
print(json.dumps({
    "marqueurs_avant_remplissage": avant,
    "marqueurs_apres_remplissage": sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t2))),
    "prereg.problemes": prereg.problemes(copie),
    "motifs_du_lanceur_v12_(chacun_1_attendu)": {m.split(" :")[0]: sum(1 for l in lignes if re.search(m, l)) for m in motifs},
    "amorce_citee_forme_du_lanceur": "`scripts/amorce_instance_t06_v10.sh` (`69b669e176e5cb09a48a012c2ce961a36ca09e1c0a022fa179c842e5220308b3`" in plie,
}, ensure_ascii=False, indent=1))
