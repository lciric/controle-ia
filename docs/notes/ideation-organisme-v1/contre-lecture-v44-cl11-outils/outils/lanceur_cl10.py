"""CL10 : lanceur_pire.py (CL7 à CL9) plus deux pannes pilotées par fichier, sans changer la ligne de commande :
--panne-coeur F : tant que F existe, le cœur (`executer_ideation`) lève avant son manifeste de départ (contrôles déjà joués) ;
--claude-casse F : tant que F existe, toute session Claude simulée (contrôle compris) rend le statut « erreur » (relais
                   relancé à la même adresse, mal réglé).
Usage : python3 -B lanceur_cl10.py ARBRE [--cout-controle-claude X] [--panne-coeur F] [--claude-casse F] -- ARGS…"""
import importlib.util
import json
import os
import sys

arbre = sys.argv[1]
reste = sys.argv[2:]
cout_controle = panne = casse = None
while reste and reste[0] != "--":
    if reste[0] == "--cout-controle-claude":
        cout_controle = float(reste[1])
    elif reste[0] == "--panne-coeur":
        panne = reste[1]
    elif reste[0] == "--claude-casse":
        casse = reste[1]
    else:
        raise SystemExit("option inconnue " + reste[0])
    reste = reste[2:]
reste = reste[1:]
sys.path.insert(0, arbre)
spec = importlib.util.spec_from_file_location("ideation_v1_lanceur", os.path.join(arbre, "demonstrations", "ideation_v1.py"))
lanceur = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lanceur)
from pole.adaptateurs import Resultat  # noqa: E402

original = lanceur.AdaptateurIdeationSimule.lancer


def lancer_pire(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
    controle = consigne.startswith(lanceur.idn.APPEL_DE_CONTROLE_CONSIGNE)
    if casse and os.path.exists(casse):
        sys.stderr.write("CLAUDE " + json.dumps({"role": role, "modele": modele, "controle": controle, "plafond": budget_usd,
                                                 "cout": 0.0, "taille": len(consigne), "casse": True}) + "\n")
        return Resultat("", [], 0.0, "erreur", "relais mal réglé (simulé CL10)")
    r = original(self, role, consigne, dossier, budget_usd, max_tours, modele)
    cout = (budget_usd if cout_controle is None else cout_controle) if controle else budget_usd
    sys.stderr.write("CLAUDE " + json.dumps({"role": role, "modele": modele, "controle": controle, "plafond": budget_usd,
                                             "cout": cout, "taille": len(consigne)}) + "\n")
    return Resultat(r.texte_final, r.fichiers, cout, r.statut, r.erreur)


lanceur.AdaptateurIdeationSimule.lancer = lancer_pire
if panne:
    coeur = lanceur.idn.executer_ideation

    def coeur_en_panne(*a, **k):
        if os.path.exists(panne):
            raise RuntimeError("panne simulée du cœur avant son manifeste de départ (CL10)")
        return coeur(*a, **k)
    lanceur.idn.executer_ideation = coeur_en_panne
raise SystemExit(lanceur.principal(reste))
