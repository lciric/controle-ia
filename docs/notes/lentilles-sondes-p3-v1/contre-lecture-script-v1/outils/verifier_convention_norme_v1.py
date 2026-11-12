"""Contre-lecture v1 : convention de la lentille (h @ J.T contre J @ h), structure des couches, rôle du gain g.
Vecteurs témoins aléatoires (SeedSequence 20261029), jamais une direction de sonde. N'affiche aucun jeton.
Usage : python -I -B verifier_convention_norme_v1.py <lentille.pt> <fragment.safetensors> <script v1>"""
import sys, importlib.util, numpy as np, torch
pt, st, script = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("cmp_v1", script); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ck = torch.load(pt, map_location="cpu", weights_only=True, mmap=True)
J = {c: ck["J"][c].float().numpy().astype(np.float64) for c in (7, 15, 23, 30)}
rng = np.random.default_rng(np.random.SeedSequence(20261029))
h = rng.standard_normal(4096)
for c in (7, 15, 23):
    a = h @ J[c].T                       # forme documentée par le fichier : residual @ J.T
    b = m.vers_sortie(h[:, None], J[c], np.ones(4096), "direction", {})[:, 0] * m.rms(J[c] @ h[:, None])[0, 0]  # script, g = 1, échelle rendue
    t = J[c].T @ h                       # forme fautive (transposée)
    asym = np.linalg.norm(J[c] - J[c].T) / np.linalg.norm(J[c])
    print(f"c{c}: script vs h@J.T : écart rel {np.linalg.norm(a-b)/np.linalg.norm(a):.2e} ; "
          f"cos(h@J.T, J.T@h) = {a@t/np.linalg.norm(a)/np.linalg.norm(t):.4f} ; asymétrie ‖J−Jᵀ‖/‖J‖ = {asym:.3f} ; "
          f"‖J−I‖/‖I‖ = {np.linalg.norm(J[c]-np.eye(4096))/64:.3f}")
print(f"c30 : ‖J−I‖/‖I‖ = {np.linalg.norm(J[30]-np.eye(4096))/64:.3f} (≈ 0 serait une cible = sortie du bloc 30)")
WU = m._lire_safetensors(m.Path(st), "lm_head.weight")
g = m._lire_safetensors(m.Path(st), "model.norm.weight").astype(np.float64)
print(f"g : min {g.min():.4f} max {g.max():.4f} moyenne {g.mean():.4f} écart type {g.std():.4f} (uniforme ? {np.allclose(g, g[0])})")
def tete(lg, k=20): return set(np.argsort(-lg, kind="stable")[:k].tolist())
for c in (15,):
    for i in range(3):
        v = rng.standard_normal(4096)
        y1 = m.vers_sortie(v[:, None], J[c], g, "direction", {})[:, 0]
        y3 = m.vers_sortie(3.7 * v[:, None], J[c], g, "direction", {})[:, 0]
        ym = m.vers_sortie(-v[:, None], J[c], g, "direction", {})[:, 0]
        y_sans_g = m.vers_sortie(v[:, None], J[c], np.ones(4096), "direction", {})[:, 0]
        l1, l3, lm, l0 = (WU @ y.astype(np.float32) for y in (y1, y3, ym, y_sans_g))
        print(f"témoin {i}: échelle ×3,7 même tête {tete(l1)==tete(l3)} (écart max {np.abs(l1-l3).max():.1e}) ; "
              f"−v = −logits {np.allclose(lm, -l1, atol=1e-4)} ; tête avec g ∩ sans g = {len(tete(l1)&tete(l0))}/20")
