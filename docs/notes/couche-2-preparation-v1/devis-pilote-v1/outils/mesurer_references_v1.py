"""Mesure des longueurs des références (cibles.controls) et des énoncés (questions)
du fichier des tâches du pilote de T0.5. Lecture seule ; aucune lecture de contenu
au-delà des longueurs et des comptes. Jetons estimés à 4 caractères par jeton (INFÉRÉ)."""
import json, sys, statistics as st, hashlib
chemin = sys.argv[1]
brut = open(chemin, 'rb').read()
print('sha256', hashlib.sha256(brut).hexdigest())
T = json.loads(brut)['taches']
n_ctrl, l_ctrl, l_q, l_ctrl_desc = [], [], [], []
for t in T:
    cs = t['cibles']['controls']
    n_ctrl.append(len(cs))
    l_ctrl.append(len(json.dumps(cs, ensure_ascii=False)))
    l_ctrl_desc.append(sum(len(c['description']) + len(c['evidence']) + len(c['id']) + len(c['section']) for c in cs))
    l_q.append(len(t['questions']))
def r(x):
    x = sorted(x)
    return dict(n=len(x), min=x[0], med=st.median(x), moy=round(st.mean(x), 1), p90=x[int(0.9 * (len(x) - 1))], max=x[-1])
out = dict(
    taches=len(T),
    controles_par_tache=r(n_ctrl),
    caracteres_reference_json=r(l_ctrl),
    caracteres_reference_champs=r(l_ctrl_desc),
    caracteres_enonce=r(l_q),
    regle_jetons='4 caracteres par jeton (INFERE)',
    jetons_reference_json_moy=round(st.mean(l_ctrl) / 4),
    jetons_reference_json_max=round(max(l_ctrl) / 4),
    jetons_enonce_moy=round(st.mean(l_q) / 4),
    jetons_enonce_max=round(max(l_q) / 4),
    repartition_controles={k: n_ctrl.count(k) for k in sorted(set(n_ctrl))},
)
print(json.dumps(out, ensure_ascii=False, indent=1))
