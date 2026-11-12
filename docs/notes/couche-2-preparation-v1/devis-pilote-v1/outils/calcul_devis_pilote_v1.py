"""Calcul du devis du pilote de la couche 2 (seize tâches de la réserve, tous les moniteurs, P-3 (a), N-060 v3) — v1.

Processeur seul, aucun réseau. Chaque constante porte son statut :
  RAPPORTÉ (fichier source cité dans le devis, avec empreinte), INFÉRÉ (calculé ici), SUPPOSÉ (jamais mesuré).
Sortie : texte lisible sur la sortie standard et JSON à côté (calcul_devis_pilote_v1-sortie.json).
"""
import json
import statistics
from pathlib import Path

ICI = Path(__file__).resolve().parent

# ---------------------------------------------------------------- plan d'épisodes (plan A de la synthèse, tour 3)
# RAPPORTÉ : synthese-collisionneur-pilote-v1.md (a67e6930…), § 2.1, colonne A.
LOTS = {
    "D_honnetes_seuils_dose": 16 * 10,          # consommé, hors développement
    "C_honnetes_calibrage_dev": 16 * 30,        # D-S15 ; moitiés par graine scellée dans chaque tâche (15 / 15)
    "J_jumeaux": 16 * 10,                        # hors de tout calibrage ; partagés entre modes
    "R_dose_controles": 16 * 3 * 3,             # 3 doses écrites x 3 exécutions ; exclus du développement (P-3 (a))
    "R_dose_cout": 16 * 2 * 3,                  # 2 doses x 3 exécutions, vérification de dose (P-8)
    "S_sabotes_dose_retenue": 16 * 10,          # mode « contrôles », premier demi-développement
    "TM_temoin_mention": 16 * 2 * 3,            # témoin et mention du mode « contrôles », K = 3
}
N_PLAN_A = sum(LOTS.values())
assert N_PLAN_A == 1296, N_PLAN_A
FLAGRANTE_SEPAREE_HAUT = 16  # SUPPOSÉ : lot de dose flagrante à part (forme de C), seulement si les 3 doses n'en ont pas
CAMPAGNE_1 = ["D_honnetes_seuils_dose", "C_honnetes_calibrage_dev", "J_jumeaux", "R_dose_controles", "R_dose_cout"]
CAMPAGNE_2 = ["S_sabotes_dose_retenue", "TM_temoin_mention"]

SCEN = ["bas", "central", "haut"]

# ---------------------------------------------------------------- rythmes (secondes de carte par épisode)
GEN_BAS, GEN_HAUT = 42.1, 54.6      # RAPPORTÉ : faits-pilote-couche-2-v1.md l. 916-917 (R-143 ; depenses l. 88)
J8B, J3B = 58.2, 27.5               # RAPPORTÉ : faits l. 918-919, resume.json 994d542a… (R-205) ; À REMPLACER par le rejeu
PAS_8B_LOT8 = 0.150                 # RAPPORTÉ (INFÉRÉ là-bas) : devis-rejeu-juges-v1.md l. 118, s par pas pour un lot de 8


def trace_lite(appels, jetons, prefill_s=0.5):
    """SUPPOSÉ : appels génératifs au rythme du 8B (0,150 s par pas pour 8 lignes), plus un préremplissage par appel."""
    return appels * (jetons * PAS_8B_LOT8 / 8 + prefill_s)


RYTHMES = {
    # génération : bornes RAPPORTÉES, centre INFÉRÉ (milieu)
    "generation": {"bas": GEN_BAS, "central": (GEN_BAS + GEN_HAUT) / 2, "haut": GEN_HAUT},
    "juge_8B": {s: J8B for s in SCEN},
    "juge_3B": {s: J3B for s in SCEN},
    # b* : invite I.8 sur les juges d'ensemble (carte-inventaire-v1.json) ; SUPPOSÉ 0,5 passe 8B / 1 passe 8B / 8B + 3B
    "b_etoile": {"bas": 0.5 * J8B, "central": J8B, "haut": J8B + J3B},
    # Qwen2.5-7B « comme le juge 8B » (faits l. 809) ; SUPPOSÉ 0,5 / 1 / 1,5 passe
    "qwen": {"bas": 0.5 * J8B, "central": J8B, "haut": 1.5 * J8B},
    # TRACE-lite : au plus 18 appels (trace_lite.py, budget_max) ; SUPPOSÉ 6 x 300, 12 x 400, 18 x 600 jetons générés
    "trace_lite": {"bas": trace_lite(6, 300), "central": trace_lite(12, 400), "haut": trace_lite(18, 600)},
    # base (i), moniteur par action H.12 : 10 lectures forcées (carte-inventaire) ; SUPPOSÉ 0,3 / 0,6 / 1,5 s chacune
    "base_i_par_action": {"bas": 3.0, "central": 6.0, "haut": 15.0},
    # étiquetage : par sous-agents (N-054 point 1) -> 0 s de carte (INFÉRÉ)
    "etiquetage": {s: 0.0 for s in SCEN},
}
MONITEURS = [k for k in RYTHMES if k != "generation"]

# ---------------------------------------------------------------- prix de carte (dollars de l'heure, A100 SXM4 80 Go)
OFFRES = [1.0014, 1.0143, 1.1351, 1.1883, 1.1889, 1.2963, 1.2964, 1.2973]  # RAPPORTÉ : offres-a100-releve.txt (32c5db68…)
PRIX = {"bas": min(OFFRES), "central": statistics.median(OFFRES), "haut": 1.366}  # haut RAPPORTÉ : depenses l. 204, 208
PRIX_COLLISIONNEUR_HAUT = 1.43  # SUPPOSÉ (synthèse, consigne de session), sensibilité seulement

# ---------------------------------------------------------------- frais fixes, canaris, instances
FIXE_PAR_INSTANCE = {"bas": 2.0, "central": 2.75, "haut": 3.5}  # RAPPORTÉ : devis-couche-2-banque-deux-modes-v1.md l. 37
INSTANCES = {"bas": 3, "central": 4, "haut": 6}                 # SUPPOSÉ : 2 campagnes ; haut = une instance perdue et relancée
CANARIS_TEXTES = 64                                             # RAPPORTÉ : synthese-pilote-complement-v1.md l. 119
CANARIS_PASSES = {"bas": 1, "central": 2, "haut": 3}            # SUPPOSÉ : une passe par campagne (+ une relance au haut)
CANARI_GEN = {"bas": 16, "central": 32, "haut": 48}             # SUPPOSÉ : 16 générations de déterminisme par campagne
DESCENTE_GO_PAR_INSTANCE = 22 + 15                              # RAPPORTÉ 22 Go (8B + 3B) ; INFÉRÉ 15 Go Qwen 7B (7,6 G x 2 o)
PRIX_GO_TRANSFERT = 0.01                                        # RAPPORTÉ : filtre des lanceurs, devis-rejeu l. 140

# ---------------------------------------------------------------- lectures de N-060 v3 (mode « contrôles » seulement)
EPREUVES = {  # SUPPOSÉ, construit sur P-20 (16/16, 0/48) et les épreuves R5 de N-060 v3 point 2
    "bas": {"relecture": 16, "honnete_contre_honnete": 48, "retrait": 16, "reference_permutee": 16, "troncature": 32},
    "central": {"relecture": 24, "honnete_contre_honnete": 48, "retrait": 24, "reference_permutee": 24, "troncature": 40},
    "haut": {"relecture": 32, "honnete_contre_honnete": 48, "retrait": 32, "reference_permutee": 32, "troncature": 48},
}
RELANCES = {"bas": 1.05, "central": 1.10, "haut": 1.20}  # SUPPOSÉ : sorties vides, coupées, JSON invalide


def lectures_oracle(s):
    base = LOTS["J_jumeaux"] + LOTS["R_dose_controles"] + LOTS["S_sabotes_dose_retenue"] + LOTS["TM_temoin_mention"]
    if s == "haut":
        base += FLAGRANTE_SEPAREE_HAUT
    ep = sum(EPREUVES[s].values())
    return {"episodes_lus": base, "epreuves": ep, "avant_relances": base + ep,
            "avec_relances": round((base + ep) * RELANCES[s])}


# jetons par lecture : référence mesurée (mesurer_references_v1-sortie.txt), plan de l'agent SUPPOSÉ
REF_CAR = {"bas": 2634, "central": 3001, "haut": 3855}   # INFÉRÉ : champs moyens ; JSON moyen ; JSON maximal (60 tâches)
ENONCE_CAR = {"bas": 0, "central": 4108, "haut": 6786}   # INFÉRÉ : énoncé non montré ; moyen ; maximal
CAR_PAR_JETON = {"bas": 4.0, "central": 4.0, "haut": 3.5}  # INFÉRÉ (règle usuelle) ; 3,5 au haut
CONSIGNE = {"bas": 800, "central": 1200, "haut": 2000}     # SUPPOSÉ
PLAN_AGENT = {"bas": 1500, "central": 3000, "haut": 4000}  # SUPPOSÉ ; borne T x max_nouveaux = 10 x 400 (config T0.5, INFÉRÉ)
SORTIE = {"bas": 400, "central": 1200, "haut": 3000}       # SUPPOSÉ ; le haut compte un raisonnement facturé en sortie


def jetons(s):
    entree = CONSIGNE[s] + PLAN_AGENT[s] + (REF_CAR[s] + ENONCE_CAR[s]) / CAR_PAR_JETON[s]
    return round(entree), SORTIE[s]


LECTEURS = {  # dollars par million de jetons (entrée, sortie)
    "Claude Haiku 5.5": (0.10, 0.50),    # RAPPORTÉ : documentation du fournisseur, relevée par session-depot le 29 octobre
    "Claude Sonnet 5.5": (2.0, 10.0),    # idem
    "Claude Opus 5.5": (4.0, 20.0),      # idem
    "Claude Fable 5.1": (10.0, 50.0),    # idem
    "Gemini (Argon)": (10.0, 50.0),      # SUPPOSÉ : prix inconnu, valeur haute volontaire
}
PAIRE = {"bas": ("Claude Sonnet 5.5", "Gemini (Argon)"),
         "central": ("Claude Opus 5.5", "Gemini (Argon)"),
         "haut": ("Claude Opus 5.5", "Gemini (Argon)")}


def cout_lecture(lecteur, s):
    e, o = jetons(s)
    pe, po = LECTEURS[lecteur]
    return e * pe / 1e6 + o * po / 1e6


# étiquetage : sous-agents de session (0 dollar, comme au pilote) ; au haut, relais payant Sonnet 5.5, deux séries
ETIQ_EPISODES = LOTS["R_dose_controles"] + LOTS["R_dose_cout"] + LOTS["S_sabotes_dose_retenue"] + LOTS["TM_temoin_mention"]

# stockage
MO_PAR_EPISODE = {"bas": 0.65, "central": 1.0, "haut": 1.7}  # 0,5 Mo activations INFÉRÉ (faits l. 820) + scores par jeton et textes SUPPOSÉS


def calculer():
    r = {"scenarios": {}}
    for s in SCEN:
        n = N_PLAN_A + (FLAGRANTE_SEPAREE_HAUT if s == "haut" else 0)
        sec_mon = sum(RYTHMES[m][s] for m in MONITEURS)
        sec_ep = RYTHMES["generation"][s] + sec_mon
        h_postes = {k: n * RYTHMES[k][s] / 3600 for k in RYTHMES}
        h_canaris = CANARIS_PASSES[s] * CANARIS_TEXTES * sec_mon / 3600
        h_canari_gen = CANARI_GEN[s] * RYTHMES["generation"][s] / 3600
        h_total = sum(h_postes.values()) + h_canaris + h_canari_gen
        d_carte = h_total * PRIX[s]
        d_fixe = INSTANCES[s] * FIXE_PAR_INSTANCE[s]
        d_transfert = INSTANCES[s] * DESCENTE_GO_PAR_INSTANCE * PRIX_GO_TRANSFERT + n * MO_PAR_EPISODE[s] / 1000 * PRIX_GO_TRANSFERT
        lo = lectures_oracle(s)
        l1, l2 = PAIRE[s]
        d_or = {l1: lo["avec_relances"] * cout_lecture(l1, s), l2: lo["avec_relances"] * cout_lecture(l2, s)}
        d_oracle = sum(d_or.values())
        d_etiq = 0.0 if s != "haut" else 2 * ETIQ_EPISODES * RELANCES[s] * cout_lecture("Claude Sonnet 5.5", "central")
        postes = {
            "carte_generation": h_postes["generation"] * PRIX[s],
            "carte_juges_8B_3B": (h_postes["juge_8B"] + h_postes["juge_3B"]) * PRIX[s],
            "carte_b_etoile_qwen": (h_postes["b_etoile"] + h_postes["qwen"]) * PRIX[s],
            "carte_trace_lite": h_postes["trace_lite"] * PRIX[s],
            "carte_base_i": h_postes["base_i_par_action"] * PRIX[s],
            "carte_canaris": (h_canaris + h_canari_gen) * PRIX[s],
            "frais_fixes_instances": d_fixe,
            "transfert_stockage": d_transfert,
            "lectures_N060_v3": d_oracle,
            "etiquetage": d_etiq,
        }
        total = sum(postes.values())
        r["scenarios"][s] = {
            "episodes": n,
            "secondes_par_episode": {"generation": RYTHMES["generation"][s], "moniteurs": sec_mon, "total": sec_ep},
            "secondes_par_poste": {k: round(RYTHMES[k][s], 2) for k in RYTHMES},
            "heures": {**{k: round(v, 2) for k, v in h_postes.items()}, "canaris": round(h_canaris, 2),
                       "canari_generation": round(h_canari_gen, 2), "total": round(h_total, 2)},
            "prix_carte": PRIX[s],
            "instances": INSTANCES[s],
            "oracle": {**lo, "jetons_entree_sortie": jetons(s),
                       "dollars_par_lecture": {k: round(cout_lecture(k, s), 5) for k in (l1, l2)},
                       "dollars_par_lecteur": {k: round(v, 2) for k, v in d_or.items()}},
            "stockage_Go": round(n * MO_PAR_EPISODE[s] / 1000, 2),
            "postes_dollars": {k: round(v, 2) for k, v in postes.items()},
            "parts": {k: round(v / total, 3) for k, v in postes.items()},
            "total_dollars": round(total, 2),
            "ecart_a_90": round(total - 90, 2),
            "palier_189_s_moniteurs_franchi": sec_mon > 189,
        }
    # table des lecteurs (coût par lecteur seul, lectures avec relances)
    r["table_lecteurs"] = {k: {s: round(lectures_oracle(s)["avec_relances"] * cout_lecture(k, s), 2) for s in SCEN}
                           for k in LECTEURS}
    # contrôles d'arithmétique
    c = r["controles"] = {}
    c["plan_A_episodes"] = N_PLAN_A
    c["plan_A_heures_8B_3B"] = [round(N_PLAN_A * (GEN_BAS + J8B + J3B) / 3600, 1),
                                round(N_PLAN_A * (GEN_HAUT + J8B + J3B) / 3600, 1)]  # synthèse : 46–50
    c["plan_A_dollars_synthese"] = [round(c["plan_A_heures_8B_3B"][0] * 1.08, 1),
                                    round(c["plan_A_heures_8B_3B"][1] * 1.43, 1)]     # synthèse : 50–72
    c["qwen_heures_plan_A"] = round(N_PLAN_A * J8B / 3600, 1)                          # synthèse : + 21
    c["seuil_189_lu_comme_moniteurs"] = round(14470 * (GEN_HAUT + 189) / 3600 * 1.43, 0)  # ≈ 1 400 (pièce C)
    c["mediane_offres"] = statistics.median(OFFRES)
    # sensibilités
    sens = r["sensibilites"] = {}
    cen = r["scenarios"]["central"]
    h_cen = cen["heures"]["total"]
    sens["central_au_prix_1_43"] = round(cen["total_dollars"] + h_cen * (PRIX_COLLISIONNEUR_HAUT - PRIX["central"]), 2)
    sens["central_sans_temoin_mention_P10"] = round(
        cen["total_dollars"] - LOTS["TM_temoin_mention"] * (
            cen["secondes_par_episode"]["total"] / 3600 * PRIX["central"]
            + RELANCES["central"] * sum(cout_lecture(l, "central") for l in PAIRE["central"])), 2)
    g_opus = lectures_oracle("central")["avec_relances"] * cout_lecture("Claude Opus 5.5", "central")
    sens["central_si_gemini_au_prix_d_opus"] = round(cen["total_dollars"] - cen["oracle"]["dollars_par_lecteur"]["Gemini (Argon)"] + g_opus, 2)
    sens["central_si_gemini_au_quart"] = round(cen["total_dollars"] - 0.75 * cen["oracle"]["dollars_par_lecteur"]["Gemini (Argon)"], 2)
    sens["dollars_par_seconde_de_moniteur_par_episode_central"] = round(N_PLAN_A / 3600 * PRIX["central"], 4)
    sens["formule_rejeu"] = ("Δ$ = (episodes + canaris) × (s_rejeu − s_rapporté) / 3600 × prix ; 8B : s_rapporté = 58,2 ; "
                             "3B : 27,5 ; b* et Qwen suivent si la même lecture leur est appliquée")
    # paliers
    p = r["paliers"] = {}
    sec_cen = cen["secondes_par_episode"]["total"]
    p["palier_16_episodes_heures_central"] = round(16 * sec_cen / 3600 + 0.0, 2)
    p["palier_16_dollars_haut"] = round(16 * r["scenarios"]["haut"]["secondes_par_episode"]["total"] / 3600 * PRIX["haut"]
                                        + FIXE_PAR_INSTANCE["haut"], 2)
    n1 = sum(LOTS[k] for k in CAMPAGNE_1)
    n2 = sum(LOTS[k] for k in CAMPAGNE_2)
    p["campagne_1_episodes"] = n1
    p["campagne_2_episodes"] = n2
    for s in SCEN:
        sec = r["scenarios"][s]["secondes_par_episode"]["total"]
        p[f"campagne_1_carte_dollars_{s}"] = round(n1 * sec / 3600 * PRIX[s], 2)
        p[f"campagne_2_carte_dollars_{s}"] = round(n2 * sec / 3600 * PRIX[s], 2)
    # plafond dur par instance (campagne 1 sur 3 instances, central × 1,25, prix plafond du lanceur)
    h_inst = n1 / 3 * sec_cen / 3600 * 1.25 + 1.0
    p["plafond_heures_par_instance_campagne_1"] = round(h_inst, 1)
    p["plafond_dollars_par_instance_campagne_1"] = round(h_inst * PRIX["haut"], 2)
    # ce que coûteraient les seuls 189 s de moniteurs (plafond du palier) sur le plan A
    p["carte_plan_A_si_moniteurs_a_189_s_central"] = round(N_PLAN_A * (RYTHMES["generation"]["central"] + 189) / 3600 * PRIX["central"], 2)
    # tranche 0 : palier de 16 épisodes honnêtes (lot D), tous moniteurs, une instance ; lectures de mesure 16 x 2 lecteurs
    for s in SCEN:
        sec = r["scenarios"][s]["secondes_par_episode"]["total"]
        lect = 16 * RELANCES[s] * sum(cout_lecture(l, s) for l in PAIRE[s])
        p[f"tranche_0_dollars_{s}"] = round(16 * sec / 3600 * PRIX[s] + FIXE_PAR_INSTANCE[s] + lect, 2)
    # lectures de l'oracle par phase, au central
    paire_c = sum(cout_lecture(l, "central") for l in PAIRE["central"])
    p["oracle_central_jumeaux_et_epreuves"] = round((LOTS["J_jumeaux"] + sum(EPREUVES["central"].values())) * RELANCES["central"] * paire_c, 2)
    p["oracle_central_recherche_de_dose"] = round(LOTS["R_dose_controles"] * RELANCES["central"] * paire_c, 2)
    p["oracle_central_S_temoin_mention"] = round((LOTS["S_sabotes_dose_retenue"] + LOTS["TM_temoin_mention"]) * RELANCES["central"] * paire_c, 2)
    # bornes indépendantes du rejeu (central) : juges 8B et 3B à zéro seconde ; puis b* et Qwen aussi
    def sans(postes_sec):
        part_canaris = CANARIS_PASSES["central"] * CANARIS_TEXTES * postes_sec / 3600 * PRIX["central"]
        return N_PLAN_A * postes_sec / 3600 * PRIX["central"] + part_canaris
    sens["central_si_8B_3B_a_zero_seconde"] = round(cen["total_dollars"] - sans(J8B + J3B), 2)
    sens["central_si_8B_3B_b_etoile_qwen_a_zero"] = round(cen["total_dollars"] - sans(J8B + J3B + 2 * J8B), 2)
    # ce que 90 dollars achètent au central : génération, 8B, 3B, base (i), canaris de ces moniteurs, frais, transfert
    sec_leger = J8B + J3B + RYTHMES["base_i_par_action"]["central"]
    leger = (N_PLAN_A * (RYTHMES["generation"]["central"] + sec_leger) / 3600 * PRIX["central"]
             + CANARIS_PASSES["central"] * CANARIS_TEXTES * sec_leger / 3600 * PRIX["central"]
             + CANARI_GEN["central"] * RYTHMES["generation"]["central"] / 3600 * PRIX["central"]
             + cen["postes_dollars"]["frais_fixes_instances"] + cen["postes_dollars"]["transfert_stockage"])
    sens["central_noyau_leger_sans_b_qwen_trace_sans_oracle"] = round(leger, 2)
    sens["central_b_etoile_qwen_trace_avec_canaris"] = round(
        cen["postes_dollars"]["carte_b_etoile_qwen"] + cen["postes_dollars"]["carte_trace_lite"]
        + CANARIS_PASSES["central"] * CANARIS_TEXTES * (2 * J8B + RYTHMES["trace_lite"]["central"]) / 3600 * PRIX["central"], 2)
    return r


def main():
    r = calculer()
    (ICI / "calcul_devis_pilote_v1-sortie.json").write_text(json.dumps(r, ensure_ascii=False, indent=1))
    print(json.dumps(r, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
