"""Course v3 et course v4 côte à côte (lecteur R13, lecture seule) : nombres clés et bras qui ne dépendent pas de R1.

Usage : python -I comparaison_v3_v4_v1.py <arbre de lecture>
"""
import hashlib
import json
import sys
from pathlib import Path

A = Path(sys.argv[1])
R = {
    "principale": ("analyse-principale-r1-r2-v1", "20261103-072723-analyse-principale-r1-r2-v1", "20261106-121351-analyse-principale-r1-r2-v1"),
    "par_episode": ("analyse-par-episode-v1", "20261103-072805-analyse-par-episode-v1", "20261106-121448-analyse-par-episode-v1"),
    "secondaire": ("analyse-blanche-noire-v3", "20261103-072840-analyse-blanche-noire-v3", "20261106-121459-analyse-blanche-noire-v3"),
}


def lire(nom, run):
    p = A / "diag" / run / f"{R[nom][0]}.json"
    return hashlib.sha256(p.read_bytes()).hexdigest(), json.loads(p.read_text())["resultat"]


for nom, (_, r3, r4) in R.items():
    h3, d3 = lire(nom, r3)
    h4, d4 = lire(nom, r4)
    print(f"\n=== {nom} : v3 {r3} ({h3}) / v4 {r4} ({h4})")
    print("  classes v3 :", d3["issue"].get("classes"), " v4 :", d4["issue"].get("classes"))
    print("  réserves v3 :", d3["issue"].get("reserves"), " v4 :", d4["issue"].get("reserves"))
    print("  audit v3 :", d3["issue"].get("audit_R4"), " v4 :", d4["issue"].get("audit_R4"))
    if nom == "principale":
        for c in ("couverture",):
            print(f"  {c} v3 {d3['calcul'][c]} v4 {d4['calcul'][c]}")
        print("  fidélité (toutes) v3 :", d3["calcul"]["rejeu"]["fidelite_toutes"])
        print("  fidélité (toutes) v4 :", d4["calcul"]["rejeu"]["fidelite_toutes"])
        for b in d4["calcul"]["principale"]["bras"]:
            x3 = d3["calcul"]["principale"]["bras"][b]
            x4 = d4["calcul"]["principale"]["bras"][b]
            print(f"  bras {b:12s} rappel 1 % v3 {x3['par_alpha']['1/100']['rappel']:.4f} v4 {x4['par_alpha']['1/100']['rappel']:.4f} ; aire v3 {x3['auc']:.4f} v4 {x4['auc']:.4f}")
    if nom == "par_episode":
        for b in d4["calcul"]["principale_bras"]["bras"]:
            x3 = d3["calcul"]["principale_bras"]["bras"][b]["par_alpha"]["1/100"]
            x4 = d4["calcul"]["principale_bras"]["bras"][b]["par_alpha"]["1/100"]
            print(f"  bras {b:4s} rappel v3 {x3['rappel']:.4f} v4 {x4['rappel']:.4f} ; FA v3 {x3['fausses_alarmes_compte']} v4 {x4['fausses_alarmes_compte']} ; mention v3 {x3['part_mention']:.4f} v4 {x4['part_mention']:.4f}")
        print("  pas de détection v3 :", d3["calcul"]["principale_bras"]["bras"]["W"].get("pas_de_detection"),
              " v4 :", d4["calcul"]["principale_bras"]["bras"]["W"].get("pas_de_detection"))
        for k in ("W-G", "W-J3s", "W-T", "W-J8s"):
            a3 = d3["calcul"]["principale_bras"]["comparaisons"][k]["par_alpha"]["1/100"]
            a4 = d4["calcul"]["principale_bras"]["comparaisons"][k]["par_alpha"]["1/100"]
            print(f"  {k} v3 {a3['estimation']:+.4f} [{a3['bas']:+.4f} ; {a3['haut']:+.4f}] v4 {a4['estimation']:+.4f} [{a4['bas']:+.4f} ; {a4['haut']:+.4f}]")
    if nom == "secondaire":
        for b in d4["P3"]["bras"]:
            m3, m4 = d3["P3"]["bras"][b], d4["P3"]["bras"][b]
            if not m3["lu"]:
                print(f"  bras {b:14s} v3 non lu ({m3['motifs']}) ; v4 lu={m4['lu']}")
                continue
            s3, s4 = m3["mesures"]["somme_terminale"], m4["mesures"]["somme_terminale"]
            print(f"  bras {b:14s} aire v3 {s3['aire']['estimation']:.6f} v4 {s4['aire']['estimation']:.6f} ; puissance v3 {s3['puissance']['estimation']:.6f} v4 {s4['puissance']['estimation']:.6f} ; identiques : {s3 == s4}")
        for k in d4["P3"]["comparaisons"]:
            c3, c4 = d3["P3"]["comparaisons"][k], d4["P3"]["comparaisons"][k]
            print(f"  {k:18s} v3 p_aj {c3.get('holm', {}).get('p_ajustee') if isinstance(c3.get('holm'), dict) else c3.get('holm')} ; v4 p_aj {c4['holm']['p_ajustee']:.4f} (p {c4['holm']['p']:.5f}) ; aire v4 {c4['aire']['estimation']:+.4f} [{c4['aire']['bas']:+.4f} ; {c4['aire']['haut']:+.4f}] ; puissance v4 {c4['puissance']['estimation']:+.4f}")
        # Holm recalculé à la main sur les p bilatérales v4
        ps = sorted((c["holm"]["p"], k) for k, c in d4["P3"]["comparaisons"].items())
        m = len(ps)
        courant = 0.0
        for j, (p, k) in enumerate(ps):
            courant = max(courant, min(1.0, (m - j) * p))
            c = d4["P3"]["comparaisons"][k]
            print(f"  Holm à la main {k:18s} p {p:.5f} → ajustée {courant:.5f} (écrite {c['holm']['p_ajustee']:.5f}) ; rejet {courant < 0.05} (écrit {c['holm']['rejetee']})")
