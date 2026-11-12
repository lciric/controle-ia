import json, sys
from pathlib import Path
from controle_ia.t07 import reextraction_p3_v1 as rx, lecture_v4 as lv4
print("import", rx.__file__)
racine = Path("/home/user/controle-ia-travail")
cfg = json.loads((racine / "docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v7.json").read_text())
lv4.exiger_configuration(cfg)
p3 = rx.lire_p3(racine, cfg["donnees_p3"])
c, g, r = p3["config"], p3["graines"], p3["resultat"]
print("mode", c.get("mode"), "fils", c.get("fils"), "couches", c.get("couches"), "n_plancher P3", c.get("n_plancher"))
for k in ("n_faits_max", "retrait_fin_tromperie", "n_par_classe_enjeux", "max_jetons_enjeux", "part_entrainement", "agent"):
    print(" config", k, "présent" if k in c else "ABSENT", (c.get(k) if k != "agent" else list(c.get(k, {}))))
for k in ("tirage-enjeux", "decoupage-tromperie", "decoupage-enjeux", "plancher/tromperie", "plancher/enjeux", "modele-jouet",
          "sonde/enjeux-lineaire-c15", "sonde/tromperie-difference_moyennes-c15"):
    print(" graine", k, "présente" if k in g else "ABSENTE")
d = r["donnees"]
print(" donnees", {k: (len(v) if isinstance(v, list) else v) for k, v in d.items()})
print(" effectifs", r["effectifs"], "principales", r["principales"], "fils_entrainement_effectifs", r["fils_entrainement_effectifs"])
from controle_ia.premier_test_ia.figees import lire_sondes
f = cfg["planchers_p3"]
sondes, meta, sha = lire_sondes(racine / f["chemin"], f["sha256"])
par = {s.nom: s for s in sondes}
print(" fichier léger :", len(sondes), "sondes ; méta", list(meta))
for n in ("tromperie-difference_moyennes-c15", "enjeux-difference_moyennes-c15", "enjeux-lineaire-c15"):
    s = par.get(n); print(" ", n, None if s is None else (type(s).__name__, s.couche, s.agregation, getattr(s, "famille", None), s.w.dtype, s.w.shape))
for cpt in ("tromperie", "enjeux"):
    noms = meta["planchers"][cpt]; d0 = par[noms[0]]
    print(" plancher", cpt, len(noms), noms[0], d0.agregation, d0.couche, d0.w.dtype)
# témoins et directions de P3 par les fonctions du module
principales = {cpt: par[cfg["sondes_par_concept"][cpt]] for cpt in ("tromperie", "enjeux")}
for cpt, s in principales.items():
    t = rx._temoin(racine, cfg, cpt, s); ds = rx._directions_p3(racine, cfg, s, cfg["plancher_figees"]["n_p3"])
    print(" témoin de", s.nom, "→", t.nom, "; directions de P3 :", len(ds), "; graine", rx._graine_p3(p3, f"plancher/{cpt}") is not None,
          "; graine sonde", rx._graine_p3(p3, f"sonde/{s.nom}") is not None)
