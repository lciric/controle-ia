"""Pic de mémoire du noyau d'attention « math » (composition ATen, la même sur processeur et sur carte) :
préremplissage en demi-précision bfloat16, masque de remplissage à gauche et causal, réduction en demi-précision
non permise (défaut). Mesure : pic de la mémoire résidente du processus (ru_maxrss), rapporté à la taille d'une
matrice d'attention (B, H, L, L) en simple précision."""
import resource, sys, torch
from torch.nn.attention import SDPBackend, sdpa_kernel
B, H, L, D = (int(x) for x in sys.argv[1:5])
torch.manual_seed(0)
q, k, v = (torch.randn(B, H, L, D, dtype=torch.bfloat16) for _ in range(3))
m = torch.zeros(B, 1, L, L, dtype=torch.bfloat16)
m[:, :, :, : L // 10] = torch.finfo(torch.bfloat16).min
m = m + torch.triu(torch.full((L, L), torch.finfo(torch.bfloat16).min, dtype=torch.bfloat16), 1)
torch.set_num_threads(1)
avant = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
with sdpa_kernel(SDPBackend.MATH):
    o = torch.nn.functional.scaled_dot_product_attention(q, k, v, attn_mask=m)
apres = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
unite = B * H * L * L * 4
print(f"torch {torch.__version__} ; B={B} H={H} L={L} D={D} ; réduction demi dans math permise : "
      f"{torch.backends.cuda.fp16_bf16_reduction_math_sdp_allowed()} ; sortie {o.dtype}")
print(f"unité (B,H,L,L) simple précision : {unite/1e9:.3f} Go ; hausse du pic : {(apres-avant)/1e9:.3f} Go ; "
      f"rapport : {(apres-avant)/unite:.2f}")
