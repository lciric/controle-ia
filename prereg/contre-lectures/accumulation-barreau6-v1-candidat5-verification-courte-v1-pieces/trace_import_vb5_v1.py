import sys, hashlib, os
racine = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.join(racine, "src"))
avant = set(sys.modules)
import controle_ia.accumulation_b6.lecture_v1, controle_ia.accumulation_b6.garde_v1, controle_ia.accumulation_b6.etats_v1, controle_ia.accumulation_b6.phrases_v1, controle_ia.accumulation_b6.code_accb6_v1  # noqa
for nom in sorted(set(sys.modules) - avant):
    m = sys.modules[nom]; f = getattr(m, "__file__", None)
    if f and os.path.isabs(f) and f.startswith(racine + os.sep + "src"):
        print(hashlib.sha256(open(f, "rb").read()).hexdigest(), os.path.relpath(f, racine), nom)
