"""cl5, lot 3 : les huit autres scénarios du banc de cl4, définitions recopiées de
`docs/notes/echelle-conscience-eval/v5/contre-lecture-cl4/scripts/banc_v5.py`, mêmes graines, analyse v5 (via banc_cl5).
Usage : python -I -B banc_cl5_lot3.py SORTIE_JSONL N_BOOT PROCESSUS NOM:GRAINE0:N [...]
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import banc_cl5 as B  # noqa: E402

B.SCENARIOS.update({
    "masque_HA_fort": (1.0, 0.2, {"signature": -2.0}, {}),
    "masque_HA_fort_t015": (1.0, 0.2, {"signature": -2.0, "tau": 0.15}, {"tau": 0.15}),
    "masque_pasdefuite_t015": (0.6, 0.0, {"signature": -1.4, "tau": 0.15}, {"tau": 0.15}),
    "sig_ab_pos": (0.0, 0.0, {"signature": 2.0, "signature_b": 2.0}, {}),
    "sig_b_pos": (0.0, 0.0, {"signature_b": 2.0}, {}),
    "HA_kappa": (1.0, 0.1, {"kappa": 0.5}, {"kappa": 0.5}),
    "faible_egal_forceb_t015": (0.2, 0.2, {"tau": 0.15, "force_b": 0.75}, {"tau": 0.15, "force_b": 0.75}),
    "faible_egal_t04": (0.2, 0.2, {}, {}),
})

if __name__ == "__main__":
    sys.exit(B.principal(sys.argv[1:]))
