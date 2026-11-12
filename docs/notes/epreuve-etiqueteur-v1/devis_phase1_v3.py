# Devis v3 de la phase 1 : consignes réellement rendues (génération d'essai v2, graine 20261107), réglages gelés de
# lire_items_phase1_v2.py (Argon : sortie 8 000 + pensée 8 192 ; Kimi : 32 000 raisonnement compris).
import sys
sys.path.insert(0, sys.argv[1])
import epreuve_phases_v1 as ph
import lire_items_phase1_v2 as lire
q = ph.extraire_question(sys.argv[2])
items = ph.lire_jsonl(sys.argv[3]); cle = ph.lire_jsonl(sys.argv[4]); form = ph.lire_jsonl(sys.argv[5])
jum = {c["item"] for c in cle if c["version"] == "jumeau"}
def car(lot): return sum(len(ph.rendre_consigne(i, q)) for i in lot)
def vis(lot): return sum(len(ph.reponse_visible_longue(i)) for i in lot)
lots = {"format": form, "principale+relecture": items + [i for i in items if i["item"] in jum]}
R = 1.05
total = {"central": 0.0, "haut": 0.0, "prudent": 0.0}
for nom, lot in lots.items():
    n = len(lot) * R; ci = car(lot) * R; cv = vis(lot) * R
    for k, m in lire.LECTEURS.items():
        pi, po = m["prix"]
        pens_c = 4000 if k == "A" else 8000     # hypothèse centrale de la contre-lecture 1
        pens_h = 8192 if k == "A" else 16000    # haut : pensée au budget (Argon), moitié du plafond (Kimi)
        sc = {"central": (ci / 4, cv / 4 + pens_c * n), "haut": (ci / 4, cv / 4 + pens_h * n),
              "prudent": (ci / 3, lire.sortie_reservee(k) * n)}
        for s, (ji, jo) in sc.items():
            c = ji / 1e6 * pi + jo / 1e6 * po
            total[s] += c
            print(f"{nom:22s} {k} {s:8s} appels {n:6.0f} entrée {ji/1e6:6.3f} M sortie {jo/1e6:7.3f} M : {c:7.2f} dollars")
print({s: round(v, 1) for s, v in total.items()})
