"""cl5, lot 2 du banc : mêmes générateur et analyse que `banc_cl5.py` (importé), scénarios ajoutés :
  - écart d'échelle vrai (1,0 et 0,2) sous deux signatures d'un seul jeu, à des tailles différentes et de signes
    opposés (jeu a négatif au petit, jeu b positif au grand) : un « nul » peut-il être fabriqué ?
  - signatures négatives croisées (jeu a au petit, jeu b au grand), cadrages homogènes (tau 0,15).
Usage : python -I -B banc_cl5_lot2.py SORTIE_JSONL N_BOOT PROCESSUS NOM:GRAINE0:N [...]
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import banc_cl5 as B  # noqa: E402

B.SCENARIOS.update({
    "masque_croise_HA_t04": (1.0, 0.2, {"signature": -2.0}, {"signature_b": 2.0}),
    "masque_croise_HA_t015": (1.0, 0.2, {"signature": -2.0, "tau": 0.15}, {"signature_b": 2.0, "tau": 0.15}),
    "masque_croise_HA_doux_t015": (1.0, 0.2, {"signature": -1.4, "tau": 0.15}, {"signature_b": 1.4, "tau": 0.15}),
    "croise_neg_8a_70b_t015": (0.0, 0.0, {"signature": -2.0, "tau": 0.15}, {"signature_b": -2.0, "tau": 0.15}),
})

if __name__ == "__main__":
    sys.exit(B.principal(sys.argv[1:]))
