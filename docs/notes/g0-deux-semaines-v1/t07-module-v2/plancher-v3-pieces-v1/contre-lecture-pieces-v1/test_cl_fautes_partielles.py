"""Essai du contre-lecteur : fautes réelles d'étendue partielle à travers `reextraire` (run jouet de P3 des essais du développeur)."""
import json, os
import numpy as np
from test_t07_plancher_v3_reextraction_v1 import p3, _config, _lancer, en, rx   # noqa: F401 (appui : run jouet de P3)

SORTIE = os.environ["CL_SORTIE"]


def _partiel(part, genre):
    def extraire(modele, exemples, couches, echeance=None):
        n = len(exemples)
        k = max(1, int(round(part * n)))
        touches = set(range(0, n, max(1, n // k))[:k]) if k < n else set(range(n))
        ex = []
        for i, x in enumerate(exemples):
            if i in touches and genre == "empan" and x["debut"] >= 1:
                x = {**x, "debut": x["debut"] - 1, "fin": x["fin"] - 1}
            ex.append(x)
        s = en.extraire(modele, ex, couches, echeance)
        if genre == "echange":                      # les jetons de l'exemple touché remplacés par ceux d'un autre (mêmes effectifs)
            for c in s:
                for i in sorted(touches):
                    s[c][i] = s[c][(i + 1) % n].copy()
        return s
    return extraire, None


def test_fautes_partielles(p3):
    res = {"import": rx.__file__}
    for genre in ("empan", "echange"):
        for part in (0.0, 0.002, 0.01, 0.03, 0.1, 0.3, 1.0):
            if part == 0.0:
                r, _ = _lancer(p3, config=_config(p3, "rapportee"))
            else:
                r, _ = _lancer(p3, config=_config(p3, "rapportee"), extraire=_partiel(part, genre)[0])
            res[f"{genre}/{part}"] = {n: {"etat": v["etat"], "palier": v.get("palier"), "temoin": (v.get("garde_identite") or {}).get("palier"),
                                          "ecart_temoin": (v.get("garde_identite") or {}).get("ecart_max"),
                                          "directions": (v.get("garde_directions_p3") or {}).get("palier"),
                                          "ecart_directions": (v.get("garde_directions_p3") or {}).get("ecart_max"),
                                          "reserve": v.get("reserve"), "exemples": r["rapport"].get("jetons", {})}
                                      for n, v in r["par_sonde"].items()}
    open(SORTIE, "w").write(json.dumps(res, ensure_ascii=False, indent=1, default=str))
