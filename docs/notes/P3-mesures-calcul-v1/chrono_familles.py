import sys, time
import numpy as np, torch
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.sondes.familles import entrainer, Reglages
from controle_ia.sondes.evaluation import scores_actions
fils = int(sys.argv[1]); n_seq = int(sys.argv[2]); L = int(sys.argv[3]); epoques = int(sys.argv[4])
torch.set_num_threads(fils)
rng = np.random.default_rng(0); d = 4096
seqs = [rng.standard_normal((L, d)).astype(np.float32) for _ in range(n_seq)]
y = np.array([i % 2 for i in range(n_seq)])
for f, ag in [("difference_moyennes","max"), ("lineaire","max"), ("perceptron","max"), ("attention","attention"), ("mahalanobis","max")]:
    t = time.time(); s = entrainer(f, "x", 0, seqs, y, ag, 1, Reglages(epoques=epoques)); dt = time.time() - t
    t = time.time(); sc = scores_actions(s, seqs[:20]); ds = (time.time() - t) / 20
    print(f"{f:20s} entrainement {dt:8.1f} s ({epoques} epoques, {n_seq*L} jetons) ; notation {ds*1000:8.1f} ms par action de {L} jetons", flush=True)
