"""Lanceur v40 avec le moteur simulé « au pire cas » côté Claude (contre-lecture CL7).

Usage : python3 -B lanceur_pire.py ARBRE_V40 [--cout-controle-claude X] -- ARGS DU LANCEUR…
Chaque session Claude simulée rend un coût égal à son plafond (pire cas) ; le contrôle Claude rend X (défaut : son
plafond). Aucun réseau ; chaque appel Claude simulé est consigné sur la sortie d'erreur (préfixe « CLAUDE »)."""
import importlib.util
import json
import os
import sys

arbre = sys.argv[1]
reste = sys.argv[2:]
cout_controle = None
if reste and reste[0] == "--cout-controle-claude":
    cout_controle = float(reste[1])
    reste = reste[2:]
assert reste[0] == "--"
reste = reste[1:]
sys.path.insert(0, arbre)
spec = importlib.util.spec_from_file_location("ideation_v1_lanceur", os.path.join(arbre, "demonstrations", "ideation_v1.py"))
lanceur = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lanceur)
from pole.adaptateurs import Resultat  # noqa: E402

original = lanceur.AdaptateurIdeationSimule.lancer


def lancer_pire(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
    r = original(self, role, consigne, dossier, budget_usd, max_tours, modele)
    controle = consigne.startswith(lanceur.idn.APPEL_DE_CONTROLE_CONSIGNE)
    cout = (budget_usd if cout_controle is None else cout_controle) if controle else budget_usd
    sys.stderr.write("CLAUDE " + json.dumps({"role": role, "modele": modele, "controle": controle, "plafond": budget_usd,
                                             "cout": cout, "taille": len(consigne)}) + "\n")
    return Resultat(r.texte_final, r.fichiers, cout, r.statut, r.erreur)


lanceur.AdaptateurIdeationSimule.lancer = lancer_pire
raise SystemExit(lanceur.principal(reste))
