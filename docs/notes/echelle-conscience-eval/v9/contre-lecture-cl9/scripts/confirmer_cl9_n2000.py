"""Confirme une analyse du banc cl9 à 2 000 tirages (taille du bootstrap décisif). Usage : SCENARIO GRAINE"""
import importlib.util, json, pathlib, sys
ICI = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("b9", ICI / "banc_cl9_miroir.py")
B9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(B9)
x = B9.un((sys.argv[1], int(sys.argv[2]), 2000))
print(json.dumps(x, ensure_ascii=False))
