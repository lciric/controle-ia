"""Puissance de P3-bis (témoin positif planté), tirée des seules sorties de P3 sous `diag/` (aucun fichier sous `donnees/`).

Entrées, vérifiées par leur sceau compagnon (R11) avant toute lecture :
- `diag/20261020-075740-p3-lecture/lecture-p3.json` : aires, intervalles par blocs de tâches et planchers des dix jeux de P3,
  effet du coût (P3-P1), accumulation par épisode (P3-P5) ;
- `diag/20261020-220858-addendum2-p3/lecture-addendum2-p3.json` : aires minimales détectables de l'addendum 2 (B3), pour
  recouper la formule ;
- `diag/20261019-230011-p3-reel/episodes-p3.json` et `diag/20261019-230011-p3-reel/resume.json` : durées du run de P3.

Formules (celles de l'addendum 2, B3, au niveau de P3-bis) :
- erreur type d'un jeu : (haut − bas) / (2 z), z = quantile normal du niveau de l'intervalle du jeu ;
- aire minimale détectable à 80 % : quantile 0,95 du plancher + (z_niveau + z_0,80) × erreur type ;
- puissance à une aire vraie A : Φ((A − q95) / erreur type − z_niveau), plancher tenu pour fixe ;
- par épisode : seuil = maximum des 60 épisodes honnêtes (fausse alarme conforme au plus 1/61) ; taux de détection k/60 ;
  « au-dessus de la fausse alarme » si la borne basse de Clopper-Pearson à 95 % (bilatéral) dépasse 1/61.
Sortie : texte sur la sortie standard (la session la verse sous `puissance-p3-bis-v1.txt`).
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from scipy.stats import beta, binom, norm

RACINE = Path(__file__).resolve().parents[2]
ENTREES = {
    "lecture": "diag/20261020-075740-p3-lecture/lecture-p3.json",
    "addendum2": "diag/20261020-220858-addendum2-p3/lecture-addendum2-p3.json",
    "episodes": "diag/20261019-230011-p3-reel/episodes-p3.json",
    "resume": "diag/20261019-230011-p3-reel/resume.json",
}
Z80 = norm.ppf(0.80)


def lire(rel: str) -> dict:
    chemin = RACINE / rel
    if "donnees" in Path(rel).parts:
        sys.exit(f"{rel} : aucun fichier sous donnees/ n'est lu")
    sceau = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()[0]
    sha = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if sha != sceau:
        sys.exit(f"{rel} : empreinte {sha[:12]} ≠ sceau {sceau[:12]} (R11)")
    print(f"entrée {rel} sha256 {sha}")
    return json.loads(chemin.read_text(encoding="utf-8"))


def z_niveau(niveau: float) -> float:
    return float(norm.ppf(1 - (1 - niveau) / 2))


def a80(q95: float, se: float, niveau: float) -> float:
    return q95 + (z_niveau(niveau) + Z80) * se


def puissance(a: float, q95: float, se: float, niveau: float) -> float:
    return float(norm.cdf((a - q95) / se - z_niveau(niveau)))


def k_min(n: int, alpha_conforme: float) -> int:
    for k in range(1, n + 1):
        if beta.ppf(0.025, k, n - k + 1) > alpha_conforme:
            return k
    return n + 1


def main() -> None:
    lec = lire(ENTREES["lecture"])["resultat"]
    add2 = lire(ENTREES["addendum2"])["resultat"]
    eps = lire(ENTREES["episodes"])["resultat"]
    res = lire(ENTREES["resume"])["resultat"]

    print("\n1. Les dix jeux de P3 (deux sondes principales × cinq jeux), tels que lus ([L] resultat.jeux)")
    lignes = []
    for p, jeux in lec["jeux"].items():
        for j, x in jeux.items():
            se = (x["haut"] - x["bas"]) / (2 * z_niveau(x["niveau"]))
            lignes.append((p, j, x["niveau"], x["aire"], x["bas"], x["haut"], se, x["plancher_quantile"],
                           x["plancher_mediane"], x["plancher_max"]))
            print(f"  {p:35s} {j:17s} niveau {x['niveau']:.3f} aire {x['aire']:.4f} [{x['bas']:.4f} ; {x['haut']:.4f}]"
                  f" erreur type {se:.4f} plancher q95 {x['plancher_quantile']:.4f} médiane {x['plancher_mediane']:.4f}"
                  f" max {x['plancher_max']:.4f}")
    se_min, se_max = min(l[6] for l in lignes), max(l[6] for l in lignes)
    q_min, q_max = min(l[7] for l in lignes), max(l[7] for l in lignes)
    print(f"  erreur type : {se_min:.4f} à {se_max:.4f} ; quantile 0,95 du plancher : {q_min:.4f} à {q_max:.4f}")

    print("\n2. Recoupement de la formule avec l'addendum 2 (B3, niveau 0,975)")
    for p, b3 in add2["descriptifs"]["B3"].items():
        refait = b3["plancher_quantile"] + b3["demi_largeur"] * (b3["z"] + b3["z80"]) / b3["z"]
        print(f"  {p:35s} A_80 écrit {b3['A_80']:.4f} ; refait {refait:.4f}")

    print("\n3. Jeu décisif de P3-bis : sonde de tromperie, saboteur planté contre témoin honnête de même longueur, 95 %")
    t = next(l for l in lignes if l[0].startswith("tromperie") and l[1] == "saboteur-temoin")
    cas = {"analogue P3 (tromperie, saboteur contre témoin)": (t[7], t[6]),
           "enveloppe prudente (plus haut plancher et plus grande erreur type de P3)": (q_max, se_max)}
    for nom, (q, se) in cas.items():
        print(f"  {nom} : q95 {q:.4f}, erreur type {se:.4f}, aire minimale détectable (80 %) {a80(q, se, 0.95):.4f}")
        print("    puissance à l'aire vraie : " + " ; ".join(
            f"{a:.2f} → {puissance(a, q, se, 0.95):.3f}" for a in (0.60, 0.62, 0.64, 0.66, 0.70, 0.75, 0.80, 0.90)))
    for q_plus in (0.65, 0.70):
        print(f"  plancher plus haut que tout P3 (q95 {q_plus:.2f}, erreur type {se_max:.4f}) : aire minimale détectable"
              f" {a80(q_plus, se_max, 0.95):.4f}")
    print("  pour mémoire, règle de P3 (deux sondes, 97,5 %) à l'enveloppe prudente : aire minimale détectable"
          f" {a80(q_max, se_max, 0.975):.4f}")

    print("\n4. Détection par épisode (statistique « maximum » de P3-P5, seuil au maximum des 60 épisodes honnêtes)")
    n, alpha = 60, 1 / 61
    km = k_min(n, alpha)
    print(f"  fausse alarme conforme au plus 1/61 = {alpha:.4f} ; borne basse de Clopper-Pearson > 1/61 dès k = {km} sur {n}"
          f" (k = {km}: {beta.ppf(0.025, km, n - km + 1):.4f} ; k = {km - 1}: {beta.ppf(0.025, km - 1, n - km + 2):.4f})")
    print("  puissance P(k ≥ k_min) au taux vrai p : " + " ; ".join(
        f"{p:.2f} → {1 - binom.cdf(km - 1, n, p):.3f}" for p in (0.05, 0.08, 0.10, 0.15, 0.20, 0.30, 0.50)))
    for p_, x in lec["P3-P5"].items():
        m = x["maximum"]
        print(f"  P3, {p_} : seuil réduit {m['seuil']:.3f}, rappel du saboteur discret {m['rappel']:.4f},"
              f" fausses alarmes observées {m['faux_positifs_observes']:.3f}")

    print("\n5. Contrôle de manipulation du coût (P3-P1 et P3-P2 de P3, 60 tâches, 95 %)")
    for cle in ("P3-P1", "P3-P2"):
        x = lec[cle]
        se = (x["haut"] - x["bas"]) / (2 * z_niveau(0.95))
        print(f"  {cle} : effet {x['effet']:.4f} [{x['bas']:.4f} ; {x['haut']:.4f}], erreur type {se:.4f},"
              f" effet minimal détectable (80 %) {(z_niveau(0.95) + Z80) * se:.4f} (log10)")

    print("\n6. Durées de P3 (A100 SXM4 80 Go), base du devis")
    d = eps["descriptifs"]
    par_ep = d["duree_s"] / res["episodes"]
    print(f"  run entier {res['duree_s']:.1f} s ; épisodes {d['duree_s']:.1f} s pour {res['episodes']} épisodes"
          f" ({par_ep:.1f} s par épisode) ; génération {d['generation_s']:.1f} s ; pic de mémoire {d['memoire_pic_gio']} Gio ;"
          f" plus long contexte rempli {d['longueur_remplie_max']} jetons ; jetons générés {d['jetons_generes']}")
    # l'indication du pas t reste dans le contexte des pas suivants : au pas t, (t + 1) indications de 41 jetons de plus
    extra = 41 * sum(t + 1 for t in range(10)) * 180
    print(f"  surcroît de contexte de P3-bis (indications de ≈ 51 jetons au lieu de 10, gardées dans l'historique, 10 pas,"
          f" 180 épisodes instruits) : ≈ {extra} jetons de contexte cumulés, soit {100 * extra / d['jetons_contexte']:.2f} %"
          f" des jetons de contexte de P3 ({d['jetons_contexte']}) ; la génération ({d['jetons_generes']} jetons) n'en"
          f" dépend qu'au second ordre")
    for prix in (1.0889, 1.30):
        for h in (4.0, 5.0, 6.0):
            print(f"  {h:.0f} h à {prix:.4f} USD de l'heure : {h * prix:.2f} USD de calcul")


if __name__ == "__main__":
    main()
