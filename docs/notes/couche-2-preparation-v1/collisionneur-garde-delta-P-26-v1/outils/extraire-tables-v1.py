"""Tables des recoupements (synthèse P-26) à partir des sorties JSON de sorties/ — lecture seule, aucun calcul aléatoire."""
import glob
import json
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(ICI, "sorties")


def charger(nom):
    p = os.path.join(S, nom + ".json")
    if not os.path.exists(p) or os.path.getsize(p) == 0:
        return None
    return json.load(open(p))


def f2(x):
    return "—" if x is None else f"{x:.2f}".replace(".", ",")


def parse(et):
    d = {}
    for morceau in et.split("|")[1:]:
        k, v = morceau.split("=")
        d[k] = v
    d["loi"] = et.split("|")[0]
    return d


out = []
r1 = charger("R1-recoupement-pieces")
if r1:
    out.append("## R1 — recoupement des chiffres des pièces (graine 52691029, 4 000 répétitions)\n")
    out.append("| loi | δ | n | biais | k | seuil 160 : garde seule / k gardes / k contrastes / fiche | seuil 20 : k gardes / fiche | frontière 160 |")
    out.append("|---|---|---|---|---|---|---|---|")
    for et, c in r1["cellules"].items():
        d = parse(et)
        a, b = c["160.0"], c["20.0"]
        out.append(f"| {d['loi']} | {d['delta']} | {d['n']} | {d['biais']} | {d['k']} | "
                   f"{f2(a['garde_seule']['part'])} / {f2(a['k_gardes']['part'])} / {f2(a['k_contrastes']['part'])} / {f2(a['fiche_entiere']['part'])} | "
                   f"{f2(b['k_gardes']['part'])} / {f2(b['fiche_entiere']['part'])} | {a['frontiere_part']:.4f} |")
    out.append("")

for K in (10, 5, 3, 2, 1):
    p = charger(f"P-K{K}")
    if not p:
        continue
    out.append(f"## P-K{K} — k = 8, τ = 0,01, K_h = K_s = {K} (graine 52691029, 4 000 répétitions)\n")
    out.append("| δ | n_h = n_s | biais | k gardes : seuil 160 / 40 / 20 | fiche : seuil 160 / 40 / 20 | garde seule 160 | frontière 160 / 20 | tricheur 160 |")
    out.append("|---|---|---|---|---|---|---|---|")
    for et, c in p["cellules"].items():
        d = parse(et)
        s160, s40, s20 = c["160.0"], c["40.0"], c["20.0"]
        out.append(f"| {d['delta']} | {d['n']} | {d['biais']} | {f2(s160['k_gardes']['part'])} / {f2(s40['k_gardes']['part'])} / {f2(s20['k_gardes']['part'])} | "
                   f"{f2(s160['fiche_entiere']['part'])} / {f2(s40['fiche_entiere']['part'])} / {f2(s20['fiche_entiere']['part'])} | "
                   f"{f2(s160['garde_seule']['part'])} | {s160['frontiere_part']:.4f} / {s20['frontiere_part']:.4f} | {s160['tricheur_part']:.4f} |")
    out.append("")

out.append("## n80 du minimum des k gardes (dichotomie du script, 2 000 répétitions, pas ≤ 1/32)\n")
out.append("| sortie | loi | δ | seuil | biais | k | n80 | pas |")
out.append("|---|---|---|---|---|---|---|---|")
for chemin in sorted(glob.glob(os.path.join(S, "N80-*.json"))):
    nom = os.path.basename(chemin)[:-5]
    d = charger(nom)
    if not d:
        continue
    graine = d["reglages"]["graine"]
    for loi, info in d["lois"].items():
        for cle, r in info.get("n_pour_puissance_0_8_k_gardes", {}).items():
            kv = dict(x.split("=") for x in cle.split("|"))
            out.append(f"| {nom} (graine {graine}) | {loi} | {kv['delta']} | {kv['seuil']} | {kv['biais']} | {kv['k']} | "
                       f"{r.get('n_approx') if r.get('n_approx') is not None else '> ' + str(r.get('au_dela_de'))} | {r.get('pas_de_la_dichotomie', '')} |")
out.append("")

for nom in ("BETA-validation-rho017", "BETA-A", "BETA-ABj"):
    d = charger(nom)
    if not d:
        continue
    out.append(f"## {nom} (graine {d['reglages']['graine']})\n")
    out.append("| cellule | seuils : k gardes | seuils : fiche | garde seule (1er seuil) |")
    out.append("|---|---|---|---|")
    for et, c in d["cellules"].items():
        seuils = [k for k in c if re.match(r"^\d", k)]
        out.append(f"| {et} | " + " / ".join(f"{s}: {f2(c[s]['k_gardes']['part'])}" for s in seuils) + " | "
                   + " / ".join(f"{s}: {f2(c[s]['fiche_entiere']['part'])}" for s in seuils) + f" | {f2(c[seuils[0]]['garde_seule']['part'])} |")
    for cle, r in d.get("n80", {}).items():
        out.append(f"| n80 {cle} | {r.get('n_approx') if r.get('n_approx') is not None else '> ' + str(r.get('au_dela_de'))} | | |")
    out.append("")

for chemin in sorted(glob.glob(os.path.join(S, "PILOTES-*.json"))):
    nom = os.path.basename(chemin)[:-5]
    d = charger(nom)
    if not d:
        continue
    out.append(f"## {nom} (graine {d['reglages']['graine']}, {d['reglages']['pilotes']} pilotes par case, biais {d['reglages']['biais']}, δ {d['reglages']['delta']}, seuil {d['reglages']['seuil']}, k {d['reglages']['k']})\n")
    out.append("| case | n80 : min / q10 / médiane / q90 / max | part < 288 | écart-type moyen de g | part de g nul |")
    out.append("|---|---|---|---|---|")
    for case, r in d["resultats"].items():
        q = r["quantiles_0_10_50_90_100"]
        out.append(f"| {case} | {' / '.join(str(int(x)) if x != float('inf') else '∞' for x in q)} | {f2(r['part_n80_sous_288'])} | {r['ecart_type_moyen_de_g']:.4f} | {f2(r['part_moyenne_g_nul'])} |")
    out.append("")

pl = charger("planchers-v1")
if pl:
    out.append("## Tailles minimales à écarts nuls (exactes, fonction du script ; δ − biais)\n")
    out.append("| δ | biais | seuil 20 | 40 | 160 | 320 |")
    out.append("|---|---|---|---|---|---|")
    lignes = {}
    for cle, v in pl.items():
        kv = dict(x.split("=") for x in cle.split("|"))
        lignes.setdefault((kv["delta"], kv["biais"]), {})[kv["seuil"]] = v
    for (dd, b), r in lignes.items():
        out.append(f"| {dd} | {b} | {r['20']} | {r['40']} | {r['160']} | {r['320']} |")
    out.append("")

print("\n".join(out))
