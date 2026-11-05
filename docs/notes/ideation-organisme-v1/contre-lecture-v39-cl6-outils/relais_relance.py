"""CL6 : relance contre le même relais (réserve 4, plafond 40) après une tentative qui a payé ses contrôles Claude.
Le vrai `Compteur` du relais, la garde de cohérence du lanceur (même expression), le vrai cœur `executer_ideation` ;
chaque session Claude dépense son plafond (pire cas du devis) ; un appel que le relais refuse rend une erreur (402).
Usage : python -I -B relais_relance.py COPIE_V39 DOSSIER_SIMULEE"""
import json
import os
import shutil
import sys

COPIE, SIM = sys.argv[1:3]
sys.path.insert(0, COPIE)
from pole import ideation as idn  # noqa: E402
from pole.adaptateurs import Resultat  # noqa: E402
from pole.relais_reel import Compteur  # noqa: E402
from essais.test_v7_ideation import FauxAdaptateur, fiche_brute  # noqa: E402

PREP = os.path.join(SIM, "prep")
BUDGETS = {("proposeur_ideation", "claude-opus-5-5"): 5.0, ("proposeur_ideation", "claude-fable-5-1"): 9.3,
           ("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
TOTAL = 40.0


class AdaptateurDerriereRelais(FauxAdaptateur):
    def __init__(self, compteur, *a, **k):
        super().__init__(*a, **k)
        self.compteur = compteur

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        if not self.compteur.reserver():
            self.compteur.refus += 1
            return Resultat("", [], 0.0, "erreur", "402 : plafond de dépense du relais atteint")
        r = super().lancer(role, consigne, dossier, budget_usd, max_tours, modele=modele)
        cout = 0.2 if consigne == idn.APPEL_DE_CONTROLE_CONSIGNE else float(budget_usd)  # pire cas : le plafond
        self.compteur.regler(cout)
        return Resultat(r.texte_final, [], cout, r.statut, r.erreur)


def garde_du_lanceur(etat):
    """Même expression que demonstrations/ideation_v1.py:384 (v39)."""
    plus_petit_juge = min(BUDGETS[("juge_ideation", m)] for m in ("claude-fable-5-1", "claude-opus-5-5"))
    return not (float(etat["plafond_usd"]) - float(etat["reserve_par_appel_usd"]) < TOTAL - plus_petit_juge - 1e-9)


for prior in (0.0, 0.4):
    compteur = Compteur(40.0, 4.0)
    if prior:  # tentative 1 : deux contrôles Claude payés, puis refus (contrôle d'Argon, SORTIE existante, --max-tours…)
        for _ in range(2):
            compteur.reserver(); compteur.regler(0.2)
    etat = compteur.etat()
    ok = garde_du_lanceur(etat)
    fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
    ad = AdaptateurDerriereRelais(compteur, fiches)
    ctrl = idn.appel_de_controle(ad, ["claude-fable-5-1", "claude-opus-5-5"], os.path.join(SIM, "R1-controle"), 0.2,
                                 compteur.etat, exiger_cout=True)
    cout_ctrl = sum(c["cout_declare_usd"] for c in ctrl.values())
    sortie = os.path.join(SIM, f"R1-relance-{prior}")
    for d in (sortie, os.path.join(SIM, "R1-controle")):
        shutil.rmtree(d, ignore_errors=True)
    try:
        res = idn.executer_ideation(ad, sortie, liste_blanche=os.path.join(PREP, "liste-blanche.json"),
                                    question=os.path.join(PREP, "question.md"), pieces=[os.path.join(PREP, "piece-a.md")],
                                    materiau=[os.path.join(PREP, "materiau.md")], seconde_passe=True,
                                    proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                                    juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
                                    temoins=os.path.join(PREP, "temoins.json"), graine=7, budget_total_usd=TOTAL,
                                    budgets=BUDGETS, cout_deja_engage_usd=cout_ctrl, lire_etat_relais=compteur.etat,
                                    taille_max_pieces=750_000)
        issue = "course complète (juges rendus : %d)" % res["lecture"]["juges_rendus"]
    except idn.CourseInterrompue as e:
        issue = "arrêt : " + str(e)[:160]
    fin = json.load(open(os.path.join(sortie, "manifeste-fin.json")))["reglages"]["journal"]
    print(f"dépense antérieure au relais {prior:.1f} : garde du lanceur {'passe' if ok else 'refuse'} "
          f"(état lu : plafond {etat['plafond_usd']}, réserve {etat['reserve_par_appel_usd']}, dépense {etat['depense_usd']}) ; "
          f"journal du cœur {fin['cout_total_usd']:.2f} ; relais {compteur.depense:.2f} dépensés, {compteur.refus} refus ; {issue}")
