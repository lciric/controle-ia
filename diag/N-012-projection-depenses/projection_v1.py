"""Projection des dépenses de la phase 0 (nœud N-012) — v1.

Entrées : relevé filtré des instances et des offres Vast.ai
(`traces/vastai-releve-20261006-1330/`), heures d'arrêt (`registres/arrets.md`),
dépense de marche cumulée (`registres/depenses.md`), heures de carte restantes
(`livrables/premier-rendu-v1/devis-v1.md`, section 1). Sortie : JSON sur la
sortie standard. Les hypothèses sont nommées et consignées dans la sortie.
"""
import datetime as dt
import json
import sys
from pathlib import Path

RACINE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
RELEVE = RACINE / "traces/vastai-releve-20261006-1330"

instances = json.loads((RELEVE / "instances.json").read_text(encoding="utf-8"))
offres = [json.loads(l) for l in (RELEVE / "offres.jsonl").read_text(encoding="utf-8").splitlines()]

# Heures d'arrêt (registres/arrets.md) et prix de marche des contrats (registres/depenses.md).
ARRETS = {54183350: "2026-10-04T18:12", 54285455: "2026-10-05T08:31", 54298522: "2026-10-05T10:31",
          54311651: "2026-10-05T12:14", 54332340: "2026-10-05T14:55", 54476244: "2026-10-06T12:11"}
PRIX_MARCHE = {54298522: 1.093, 54332340: 4.441, 54476244: 4.669}
PORTEUSES = [54298522, 54332340, 54476244]  # instances qui portent des activations de T0.4

H = {
    "depense_marche_cumulee_usd": 5.1,          # registres/depenses.md, ligne du 2026-10-06 12:11 UTC
    "heures_carte_restantes": round(47 * 1.3, 1),  # devis v1 : T0.5 à T0.9 + commun = 47 h, marge 30 %
    "delai_decision_h": 24.0,                   # destruction éventuelle un jour après le relevé
    "copie_h_par_instance": 0.25,               # redémarrage et copie, par instance porteuse
    "disque_travail_go": 150,                   # volume du devis v1
    "jours_disque_travail": 24,                 # du 2026-10-08 au 2026-11-01
    "telechargements_usd": 3.0,                 # ≈ 5 créations d'instance × 0,6 USD
}

releve = dt.datetime.strptime(instances["releve_utc"], "%Y-%m-%dT%H:%M:%SZ")
fin = dt.datetime(2026, 11, 1, 0, 0)
h_restantes = (fin - releve).total_seconds() / 3600

taux = {i["id"]: i["storage_total_cost"] for i in instances["instances"]}
cumul_disques = sum(taux[k] * (releve - dt.datetime.fromisoformat(v)).total_seconds() / 3600 for k, v in ARRETS.items())
taux_six = sum(taux.values())
taux_porteuses = sum(taux[k] for k in PORTEUSES)


def moins_chere(prefixe, ram_min=0):
    for o in offres:
        for x in o["offres"]:
            if x["gpu_name"].startswith(prefixe) and x["gpu_ram"] >= ram_min:
                return x  # les offres sont triées par prix croissant
    return None


cartes = {"A100 80 Go": moins_chere("A100", 79000), "H100": moins_chere("H100"), "H200": moins_chere("H200")}
deja = H["depense_marche_cumulee_usd"] + cumul_disques
copie = H["copie_h_par_instance"] * sum(PRIX_MARCHE.values())


def scenario(carte, disques_usd):
    o = cartes[carte]
    carte_usd = H["heures_carte_restantes"] * o["dph_total"]
    disque_travail = H["disque_travail_go"] * o["storage_cost"] / 30 * H["jours_disque_travail"]
    total = deja + disques_usd + carte_usd + disque_travail + H["telechargements_usd"]
    return {"carte": carte, "prix_usd_h": round(o["dph_total"], 3), "calcul_usd": round(carte_usd, 1),
            "disques_arretes_usd": round(disques_usd, 1), "disque_travail_usd": round(disque_travail, 1),
            "total_phase0_usd": round(total, 1)}


def date_plafond(seuil, taux_h):
    return (releve + dt.timedelta(hours=(seuil - deja) / taux_h)).strftime("%Y-%m-%d %H:%M")


sortie = {
    "releve_utc": instances["releve_utc"],
    "hypotheses": H,
    "taux_disques_usd_h": {str(k): round(v, 5) for k, v in taux.items()},
    "taux_six_usd_h": round(taux_six, 4), "par_jour_six_usd": round(24 * taux_six, 2),
    "taux_porteuses_usd_h": round(taux_porteuses, 4),
    "cumul_disques_usd": round(cumul_disques, 2), "deja_depense_usd": round(deja, 1),
    "heures_jusqu_au_1er_novembre": round(h_restantes, 1),
    "disques_six_jusqu_au_1er_novembre_usd": round(taux_six * h_restantes, 1),
    "alerte_120_disques_seuls": date_plafond(120, taux_six), "plafond_150_disques_seuls": date_plafond(150, taux_six),
    "cartes_moins_cheres": {k: {"id_offre": v["id"], "usd_h": v["dph_total"], "stockage_usd_go_mois": v["storage_cost"],
                                "pilote": v["driver_version"], "cuda": v["cuda_max_good"]} for k, v in cartes.items()},
    "scenarios": {
        "a_rapatrier_puis_detruire_A100": scenario("A100 80 Go", taux_six * H["delai_decision_h"] + copie),
        "b_tout_garder_A100": scenario("A100 80 Go", taux_six * h_restantes),
        "c_garder_les_trois_porteuses_A100": scenario("A100 80 Go", taux_six * H["delai_decision_h"]
                                                      + taux_porteuses * (h_restantes - H["delai_decision_h"])),
        "b_tout_garder_H200": scenario("H200", taux_six * h_restantes),
        "a_rapatrier_puis_detruire_H200": scenario("H200", taux_six * H["delai_decision_h"] + copie),
    },
}


def date_plafond_avec_calcul(seuil, taux_disques_h, carte="A100 80 Go"):
    """Disques gardés, plus le calcul restant réparti du 2026-10-08 au 2026-10-28 et le disque de travail."""
    o = cartes[carte]
    debut, fin_calcul = dt.datetime(2026, 10, 8), dt.datetime(2026, 10, 28)
    par_h_calcul = H["heures_carte_restantes"] * o["dph_total"] / ((fin_calcul - debut).total_seconds() / 3600)
    par_h_travail = H["disque_travail_go"] * o["storage_cost"] / 30 / 24
    t, cumul, pas = releve, deja, dt.timedelta(minutes=10)
    while cumul < seuil and t < fin:
        h = pas.total_seconds() / 3600
        cumul += taux_disques_h * h + ((par_h_calcul + par_h_travail) * h if debut <= t < fin_calcul else 0.0)
        t += pas
    return t.strftime("%Y-%m-%d %H:%M") if cumul >= seuil else "non atteint avant le 2026-11-01"


sortie["plafond_150_disques_gardes_et_calcul_A100"] = date_plafond_avec_calcul(150, taux_six)
sortie["alerte_120_disques_gardes_et_calcul_A100"] = date_plafond_avec_calcul(120, taux_six)
print(json.dumps(sortie, indent=1, ensure_ascii=False))
