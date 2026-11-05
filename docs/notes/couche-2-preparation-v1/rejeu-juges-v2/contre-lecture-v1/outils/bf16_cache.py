"""Écart cache contre passes complètes en bfloat16 (processeur), selon le contraste des logits du modèle jouet."""
import math, sys, torch
sys.argv = [sys.argv[0], sys.argv[1]]
src = open(sys.argv[0].replace("bf16_cache.py", "cache_contre_passes_completes.py")).read().split("pire = 0.0")[0]
exec(src)
for echelle in (1.0, 5.0, 40.0):
    def m_(g, dtype):
        m = modele(g, torch.float32)
        with torch.no_grad():
            m.lm_head.weight.mul_(echelle / 40.0)
        return m.to(dtype)
    for dtype in (torch.float32, torch.bfloat16):
        m = m_(1, dtype)
        r = v2.lire_par_probabilite_v2(m, tok, contexte, CAS["forme à échelle, saine"], CRITERES, True, 0.0, term)
        ref = reference(m, contexte, CAS["forme à échelle, saine"])
        e = max(abs(math.log(r["criteres"][n]["masse"]) - math.log(sum(p.values()))) for n, p in ref.items())
        ep = max(abs(r["criteres"][n]["probabilites"][str(v)] - x / sum(p.values())) for n, p in ref.items() for v, x in p.items())
        print(f"contraste ×{echelle:>4} {str(dtype):15} écart max de log-masse {e:.3g} ; écart max de probabilité renormalisée {ep:.3g}")
