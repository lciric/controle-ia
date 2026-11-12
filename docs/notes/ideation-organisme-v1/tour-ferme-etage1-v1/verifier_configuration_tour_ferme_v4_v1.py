"""Vérification sans appel de la configuration v4 du tour fermé par les fonctions mêmes du lanceur v64 (`ideation-organism`
`eaa74ca`, `demonstrations/tour_ferme_v64.py`), dans l'ordre de son chemin réel : lecture de la configuration
(`configuration_v56.lire_configuration_v56`), garde 15 (`exiger_machine_jetable_reel`), adaptateurs réels sans relance des portes
(`roles_reels(..., transmettre=False)`, le chemin de `--verifier-seulement`), familles séparées. `--verifier-seulement` lui-même
exige un préenregistrement scellé qui gèle l'empreinte de cette configuration (brouillon 7, pas encore scellé) : d'où cet
équivalent. Les commandes v6 n'existant pas encore à leur chemin de la fille dans ce conteneur, une copie de la configuration où
seuls ces deux chemins pointent vers les fichiers v6 de la branche (empreintes contrôlées) sert aux adaptateurs ; la configuration
elle-même est lue telle quelle. Aucune écriture hors d'un dossier temporaire, aucun réseau, aucun appel.

    python -I -B verifier_configuration_v4_v1.py COPIE_ORCHESTRATOR CONFIGURATION DOSSIER_COMMANDES_V6
"""
import hashlib, importlib.util, json, os, shutil, sys, tempfile
ORCH, CONF, CMD = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("tour_ferme_v64_lanceur", os.path.join(ORCH, "demonstrations", "tour_ferme_v64.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
from pole import configuration_v56 as cfg
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
ATTENDUES = {"commande_kimi_v6.py": "889309305aeb37de9801c2f40c31769fd268abded1ac61ea94196fd0d51195ae",
             "commande_argon_v56_nuit_v6.py": "5eae1a0468430e243c3c4e099b3969f949f62add688531aafdd7f0f44e036e55"}
r = {"configuration": os.path.abspath(CONF), "sha256": sha(CONF), "lanceur": L.T.VERSION, "adaptateur": L.AC.VERSION}
conf = cfg.lire_configuration_v56(CONF)
r["1_lecture_configuration_v56"] = "conforme"
try:
    r["2_garde_15_machine_jetable"] = {"permis": list(L.exiger_machine_jetable_reel(os.environ, conf)), "resultat": "conforme"}
except Exception as x:
    r["2_garde_15_machine_jetable"] = {"resultat": f"refus : {x}"}
plan = {"generations": 3, "cartes_par_proposeur": 12, "cartes_reference": 12, "m_e_bh": 4, "plafond_usd": 50.0,
        "duree_max_s": 72 * 3600.0, "parts": {"kimi": 44.0, "argon": 6.0}}  # parts et plafond du plan gelé (brouillon 6)
with tempfile.TemporaryDirectory(prefix="verif-conf-v4-") as d:
    shutil.copytree(os.path.join(os.path.dirname(os.path.abspath(CONF)), "pieces"), os.path.join(d, "pieces"))
    t = open(CONF, encoding="utf-8").read()
    for f, s in ATTENDUES.items():
        p = os.path.join(CMD, f); assert sha(p) == s, f
        fille = "/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/" + f
        assert t.count(json.dumps(fille)) == 1; t = t.replace(json.dumps(fille), json.dumps(p))
    copie = os.path.join(d, "configuration-tour-ferme-v4-chemins-de-la-branche.json"); open(copie, "w", encoding="utf-8").write(t)
    conf2 = cfg.lire_configuration_v56(copie)
    base, sortie = os.path.join(d, "sessions"), os.path.join(d, "sortie"); os.makedirs(base)
    proposeurs, etage, roles, infos = L.roles_reels(conf2, plan, base, sortie, transmettre=False)
    L.T.exiger_familles_separees((roles["experimentateur"][0], roles["familles"]["experimentateur"]),
                                 (roles["verificateur"][0], roles["familles"]["verificateur"]))
    r["3_roles_reels_sans_porte"] = "conforme"
    r["4_familles_separees"] = "conforme"
    r["modeles_demandes"] = infos["modeles_demandes"]
    r["bareme_des_commandes"] = infos["bareme_des_commandes"]
    r["accuses_plafond"] = infos["accuses_plafond"]
    r["substitutions_dans_les_commandes"] = {k: str(v) for k, v in infos["substitutions_dans_les_commandes"].items()} \
        if isinstance(infos["substitutions_dans_les_commandes"], dict) else str(infos["substitutions_dans_les_commandes"])
    r["adaptateurs"] = {n: {"classe": type(etage).__name__ if False else infos["adaptateurs"][n].get("version_v64"),
                            "empreintes_des_arguments": {os.path.basename(k): v for k, v in infos["adaptateurs"][n]["empreintes"].items()},
                            "controle_modele_servi": infos["adaptateurs"][n]["controle_modele_servi"][:40]} for n in ("kimi", "argon")}
r["verification"] = "conforme" if all(str(r[k]).startswith("conforme") or (isinstance(r[k], dict) and r[k].get("resultat") == "conforme")
                                      for k in r if k[:2] in ("1_", "2_", "3_", "4_")) else "voir les refus"
print(json.dumps(r, ensure_ascii=False, indent=1))
