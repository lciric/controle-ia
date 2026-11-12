"""Arithmétique du devis du saboteur à budget (ii-b), course exploratoire — brouillon 1 (processeur, aucune donnée lue).

Toutes les entrées sont écrites ici et sourcées dans `devis-ii-b-v1-brouillon1.md` (section « Hypothèses ») :
- débit d'épisode et durées fixes : lecture A de 7a (`lecture-A-exploratoire-non-opposable-v1.md`, `3c84c419…`, § 4) ;
- distillation : 7a, 14 min 51 s pour 160 transcriptions × 3 époques (adaptateur saboteur), même code, mêmes réglages ;
- jumeau honnête (oracle) : NON MESURÉ, estimation de conception (un préremplissage par action, huit suites courtes) ;
- prix : consigne de la mère (A100 SXM4 80 Go vers 1,12 USD/h), bornes des configurations de T0.6 (1,30 ; 2,10 en v2 de
  7a ; 4,70 pour la H200 NVL), stockage ≤ 0,08 USD/h, téléchargement ≤ 0,05 USD/Go.
"""
from __future__ import annotations

EP_S = 43.3                 # s par épisode, lots de 8, T = 10 (7a : 320 épisodes de distillation en 3 h 50 min 58 s)
FIXE_H = {"amorce, format et disque": 0.07, "suite ciblée": 0.58, "création, image et modèle (non relevé en 7a)": 0.25,
          "écriture, scellement, poussées": 0.10}
DIST_S_PAR_TRANSCRIPTION_EPOQUE = 891 / 480   # 7a : 14 min 51 s, 160 transcriptions × 3 époques
EPOQUES = 3
N_ETALONNAGE_EP = 64 + 32   # honnête d'étalonnage (32 tâches × 2) + saboteur flagrant de P3 (32 tâches × 1)
EP_PAR_TOUR = 32            # un épisode par tâche de réserve
N_EVAL_EP = 4 * 64          # H, B50, B100, TJ100 sur les 64 tâches d'évaluation
T = 10
ANCRAGE_ACTIONS = 320       # jumeau à contexte d'origine sur le premier tour du maître (descriptif)
JUGE_UNE_PASSE_S = 0.3      # juge 8B de T0.8 en une passe, par action (option ; estimation)
STOCKAGE_USD_H, TELECH_USD_GO = 0.08, 0.05      # bornes de l'offre (stockage ≤ 0,08 USD/h ; téléchargement ≤ 0,05 USD/Go)
STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU = 24, 20  # instance arrêtée gardée jusqu'au rapatriement vérifié ; modèle ≈ 16 Go + image
STOCKAGE_H, TELECH_GO = 48, 40                  # pire : 48 h arrêtée (borne de l'ordre), 40 Go descendus


def heures(tours: int, t_j: float, n_acc: int, lent: float = 1.0, juge: bool = True) -> dict:
    h = {}
    h["fixe"] = sum(FIXE_H.values())
    h["étalonnage : épisodes"] = N_ETALONNAGE_EP * EP_S / 3600
    h["étalonnage : jumeau"] = N_ETALONNAGE_EP * T * t_j / 3600
    h["maître : épisodes"] = tours * EP_PAR_TOUR * EP_S / 3600
    h["filtrage : jumeau du maître (et ancrage)"] = (tours * EP_PAR_TOUR * T + ANCRAGE_ACTIONS) * t_j / 3600
    h["distillation (élève et témoin-jumeau)"] = 2 * n_acc * EPOQUES * DIST_S_PAR_TRANSCRIPTION_EPOQUE / 3600 + 0.01
    h["évaluation : épisodes"] = N_EVAL_EP * EP_S / 3600
    h["évaluation : jumeau (lecture 1)"] = N_EVAL_EP * T * t_j / 3600
    h["juge T0.8 en une passe (option, lecture 2)"] = (N_EVAL_EP * T * JUGE_UNE_PASSE_S / 3600) if juge else 0.0
    h = {k: v * lent for k, v in h.items()}
    h["total"] = sum(h.values())
    return h


def usd(total_h: float, prix: float, stockage_h: float = STOCKAGE_H, telech_go: float = TELECH_GO) -> dict:
    c = total_h * prix
    s = stockage_h * STOCKAGE_USD_H
    t = telech_go * TELECH_USD_GO
    return {"carte": c, "stockage arrêté": s, "téléchargement": t, "total": c + s + t}


def imprimer(nom: str, h: dict, prix_list, stockage_h: float = STOCKAGE_H, telech_go: float = TELECH_GO) -> None:
    if "total" not in h:
        h = {**h, "total": sum(h.values())}
    print(f"\n## {nom}")
    for k, v in h.items():
        print(f"  {k} : {v:.2f} h")
    print(f"  (stockage arrêté {stockage_h} h ; téléchargement {telech_go} Go)")
    for p in prix_list:
        u = usd(h["total"], p, stockage_h, telech_go)
        print(f"  à {p:.4g} USD/h : carte {u['carte']:.1f} + stockage arrêté ≤ {u['stockage arrêté']:.1f} "
              f"+ téléchargement ≤ {u['téléchargement']:.1f} = {u['total']:.1f} USD")


def main() -> None:
    print("Devis (ii-b), brouillon 1 — arithmétique ; heures de carte ; USD")
    imprimer("Attendu bas : 6 tours, jumeau 0,5 s/action, 96 acceptés", heures(6, 0.5, 96), (1.0889, 1.12), STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    imprimer("Attendu central : 10 tours, jumeau 1,0 s/action, 96 acceptés", heures(10, 1.0, 96), (1.12, 1.30), STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    imprimer("Attendu haut : 12 tours, jumeau 1,5 s/action, 127 acceptés", heures(12, 1.5, 127), (1.30,), STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    imprimer("Arrêt précoce au tour 4 (taux trop bas), jumeau 1,0 s/action, sans distillation ni évaluation",
             {**{k: v for k, v in heures(4, 1.0, 0, juge=False).items() if k.startswith(("fixe", "étalonnage", "maître", "filtrage"))}},
             (1.12, 1.30), STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    p1 = heures(12, 3.0, 127, lent=2.0)
    imprimer("Pire P1 : hôte deux fois plus lent, 12 tours, jumeau 3,0 s/action, 127 acceptés", p1, (1.30, 1.40, 2.10))
    p_h200 = heures(12, 1.5, 127)
    imprimer("Repli H200 NVL d'emblée (aucune A100 conforme ; durées de l'A100 au haut de l'attendu, débit H200 non mesuré)",
             p_h200, (4.441, 4.669, 4.70))
    # P3 : erreur de mémoire à la distillation sur A100 (hôte lent), puis course entière sur H200 aux durées du haut de l'attendu
    perdu = {k: v for k, v in heures(12, 3.0, 127, lent=2.0).items() if k.startswith(("fixe", "étalonnage", "maître", "filtrage"))}
    perdu_h = sum(perdu.values())
    print("\n## Pire P3 : erreur de mémoire à la distillation (A100, hôte lent, 1,40 USD/h), relance entière sur H200 NVL "
          "à 4,70 USD/h aux durées du haut de l'attendu — nœud de Lazar, hors plafond")
    a100 = perdu_h * 1.40
    h200 = p_h200["total"] * 4.70
    print(f"  A100 perdue : {perdu_h:.2f} h × 1,40 = {a100:.1f} USD ; H200 : {p_h200['total']:.2f} h × 4,70 = {h200:.1f} USD ; "
          f"stockage ≤ {2 * STOCKAGE_H * STOCKAGE_USD_H:.1f} ; téléchargement ≤ {2 * TELECH_GO * TELECH_USD_GO:.1f} ; "
          f"total ≈ {a100 + h200 + 2 * STOCKAGE_H * STOCKAGE_USD_H + 2 * TELECH_GO * TELECH_USD_GO:.1f} USD")
    print("\n## Variante « avec raisonnement » du juge de T0.8 (option) : 2 560 actions, jusqu'à 400 jetons générés, "
          f"au débit d'une action d'épisode (EP_S / T = {EP_S / T:.2f} s) : {N_EVAL_EP * T * EP_S / T / 3600:.2f} h")


if __name__ == "__main__":
    main()
