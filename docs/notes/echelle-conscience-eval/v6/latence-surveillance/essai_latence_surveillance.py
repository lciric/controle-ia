"""Essai de latence de la surveillance (CLV-02), lignée « session-depot », 27 octobre 2026, au commit b8b7665 des outils : même faux outil et mêmes réglages que test_surveillance_appels_lents, contre la surveillance v5 et
la v6 ; retard de la demande d'arrêt sur le plafond."""
import importlib.util, pathlib, sys
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1")
spec = importlib.util.spec_from_file_location("t", ARBRE / "echelle-v6/tests/test_offre_et_surveillance_v6.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
base = pathlib.Path(sys.argv[1])
for version in ("v5", "v6"):
    T.SURVEILLANCE = ARBRE / f"echelle-{version}/scripts/surveiller_echelle_{version}.sh"
    d = base / f"{version}"
    d.mkdir(parents=True)
    code, arrets, txt, heures, fin = T.surveiller(d, "ECHELLE 2026 : mesure\n", age_s=4499, lenteur="2", appel_s="3",
                                                  avec_heure=True)
    print(version, "code", code, "arrêts", arrets, "retard sur le plafond", round(heures[0] - fin, 2), "s")
