"""CL11 : la vraie commande d'Argon (commande_argon_v1.py), par l'adaptateur réel de la v44, contre le faux serveur local."""
import json, os, sys, tempfile
ARBRE, ENV, CONFIG = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, ARBRE)
from pole.adaptateurs import AdaptateurCommandeExterne
ad = AdaptateurCommandeExterne([ENV], environnement={"PATH": "/usr/bin:/bin"}, delai_s=1800)
CAS = [  # (nom, config du serveur, taille de consigne, plafond)
 ("controle-1077663-plafond-3.1-sortie-max", {}, 1_077_663, 3.1),
 ("passe1-685992-plafond-2.5-sortie-max", {}, 685_992, 2.5),
 ("passe2-1173975-plafond-3.1-sortie-max", {}, 1_173_975, 3.1),
 ("juge-1166746-plafond-3.5-sortie-max", {}, 1_166_746, 3.5),
 ("passe2-compte-exact-plus-haut-(3,2-car-par-jeton)", {"jetons_par_car_compte": 1/3.2, "jetons_par_car_facture": 1/3.2}, 1_173_975, 3.1),
 ("passe2-facture-au-dessus-du-compte-(3,2-vs-4)", {"jetons_par_car_compte": 0.25, "jetons_par_car_facture": 1/3.2}, 1_173_975, 3.1),
 ("passe2-pensees-en-plus-de-la-sortie-(8000)", {"pensees": 8000}, 1_173_975, 3.1),
 ("passe2-tronquee-MAX_TOKENS", {"fin": "MAX_TOKENS"}, 1_173_975, 3.1),
 ("controle-entree-seule-trop-grosse-(1500000-a-3.1)", {}, 1_500_000, 3.1),
]
res = []
for nom, cfg, taille, plafond in CAS:
    json.dump(cfg, open(CONFIG, "w"))
    with tempfile.TemporaryDirectory() as d:
        r = ad.lancer("proposeur_ideation", "x" * taille, d, plafond, 1)
    res.append({"cas": nom, "plafond": plafond, "statut": r.statut, "cout_declare": round(r.cout_declare_usd, 6),
                "au_dessus_du_plafond": r.cout_declare_usd > plafond + 1e-12, "cout_inconnu": r.cout_inconnu,
                "erreur": (r.erreur or "")[:160]})
    print(json.dumps(res[-1], ensure_ascii=False))
