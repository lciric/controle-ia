"""Banc de mutations du contre-lecteur (copies seulement ; -o pythonpath= ; import tracé). Usage : banc_cl_v1.py ARBRE COPIE SORTIE.json ID[,ID...]"""
import hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path

PY = "/home/user/controle-ia-travail/.venv/bin/python"
T2F, T2L = "tests/test_t07_plancher_v2_fonction_v1.py", "tests/test_t07_plancher_v2_lecture_v1.py"
T_NOT, T_RX, T_LEC = ("tests/test_t07_plancher_v3_notation_v1.py", "tests/test_t07_plancher_v3_reextraction_v1.py",
                      "tests/test_t07_plancher_v3_lecture_v1.py")
P2, P3, RX, L4, PB, RT = (f"src/controle_ia/t07/{n}.py" for n in ("plancher_v2", "plancher_v3", "reextraction_p3_v1", "lecture_v4",
                                                                  "passe_blanc_v2", "repli_etapes_v2"))
M = [
 ("sain", "copie saine, aucune mutation", P3, "TOLERANCE_VECTORISEE = 1e-12", "TOLERANCE_VECTORISEE = 1e-12", [T2F, T2L, T_NOT, T_RX, T_LEC]),
 # --- mutations du développeur que seul le miroir tuait : rejouées sans les essais de miroir, sans -x
 ("d27", "bascule vers les 200 de P3 à l'échec", L4,
  '                         for n, x in reextraction["par_sonde"].items() if x["etat"] != "établi"}\n        planchers_p3 = {**planchers_figees, **planchers_neufs}\n',
  '                         for n, x in reextraction["par_sonde"].items() if False}\n        planchers_p3 = {**descriptifs_p3, **planchers_figees, **planchers_neufs}\n', [T_LEC]),
 ("d28", "planchers notés par la boucle", L4, 'tableaux[f"plancher_{k}"] = pl3.scores_plancher_vectorises(plancher, seqs).T',
  'tableaux[f"plancher_{k}"] = pl.scores_plancher(plancher, seqs).T', [T_LEC]),
 ("d30", "graines des figées hors du manifeste", L4, '+ [f"plancher/{n}" for n in connus]   # v4', '+ [f"plancher/{n}" for n in neuves]   # v4', [T_LEC]),
 ("d31", "passe à blanc sous la configuration de la v2", PB, "    from .lecture_v4 import exiger_configuration\n", "    from .lecture_v2 import exiger_configuration\n", [T_LEC]),
 ("d32", "repli sous la configuration de la v2", RT, "    from .lecture_v4 import exiger_configuration\n", "    from .lecture_v2 import exiger_configuration\n", [T_LEC]),
 ("d37", "réserves du plancher des figées non recopiées à l'étape B", L4,
  "        reserves += reserves_plancher_figees(index)            # v4 : palier « carte », principale rapportée\n", "", [T_LEC]),
 # --- règle (a), plancher_v2
 ("n1", "quantile du plancher non recalculé par tirage (moyenne des quantiles)", P2,
  "    D = A[0] - np.quantile(A[1:], float(quantile_plancher), axis=0)\n",
  "    D = A[0] - np.quantile(A[1:], float(quantile_plancher), axis=0).mean()\n", [T2F, T2L]),
 ("n2", "borne basse ≥ 0 au lieu de > 0", P2, '"au_dessus_du_plancher": bool(d["bas"] > 0.0),', '"au_dessus_du_plancher": bool(d["bas"] >= 0.0),', [T2F, T2L]),
 ("n3", "garde des tirages dégénérés retirée de difference_sur_poids", P2,
  "    if degeneres > SEUIL_DEGENERES * W.shape[0]:\n", "    if False:\n", [T2F, T2L]),
 ("n4", "ex aequo non comptés pour moitié", P2, "C[k] = G @ (0.5 * (cum[strict] + cum[large]))", "C[k] = G @ cum[strict]", [T2F, T2L]),
 ("n5", "tirages du plancher désappariés de ceux de la sonde", P2,
  "    A = aires_tirees(C, W[valides], n1, n0)\n", "    A = aires_tirees(C, W[valides], n1, n0)\n    A[1:] = A[1:, ::-1]\n", [T2F, T2L]),
 ("n6", "contrôle d'égalité à aire_sous_courbe retiré", P2,
  "    if ponctuelles[0] != aire or not np.array_equal(ponctuelles[1:], aires):\n", "    if False:\n", [T2F, T2L]),
 ("n7", "contrôle des tirages contre intervalle_blocs retiré", P2,
  '    if (ic["degeneres"] != d["degeneres"] or ic["tirages"] != d["tirages"]\n', '    if False and (ic["degeneres"] != d["degeneres"] or ic["tirages"] != d["tirages"]\n', [T2F, T2L]),
 ("n7b", "garde de la borne perdue à l'addition retirée", P2,
  '    if (sortie["bas"] > q) != bool(r["au_dessus_du_plancher"]) or', '    if False and (sortie["bas"] > q) != bool(r["au_dessus_du_plancher"]) or', [T2F, T2L]),
 ("n7c", "graine des tirages décalée d'un (tirages ≠ intervalle_blocs)", P2,
  "    rng = np.random.default_rng(int(graine))\n    W = np.empty", "    rng = np.random.default_rng(int(graine) + 1)\n    W = np.empty", [T2F, T2L]),
 # --- notation par lots, plancher_v3
 ("n8", "contrôle en ligne : première et dernière action seulement", P3, "PAS_CONTROLE = 8 ", "PAS_CONTROLE = 10**9 ", [T_NOT]),
 ("n9", "échelle du contrôle gonflée (× 1e6)", P3,
  '"ecart_relatif_max": float((ecart / np.maximum(echelle, np.finfo(np.float64).tiny)).max()),',
  '"ecart_relatif_max": float((ecart / np.maximum(echelle * 1e6, np.finfo(np.float64).tiny)).max()),', [T_NOT]),
 ("n12", "poids des directions en simple précision", P3,
  "    W = np.stack([np.asarray(p.w, dtype=np.float64) for p in plancher], axis=1)\n",
  "    W = np.stack([np.asarray(p.w, dtype=np.float32).astype(np.float64) for p in plancher], axis=1)\n", [T_NOT]),
 ("n12c", "contrôle en ligne sur la seule première direction", P3, "CONTROLE_EN_LIGNE = 2\n", "CONTROLE_EN_LIGNE = 1\n", [T_NOT, T_LEC]),
 # --- réextraction
 ("n13", "réserve du palier « carte » non écrite", RX, '        v["reserve"] = RESERVE_CARTE if v["palier"] == "carte" else None\n', '        v["reserve"] = None\n', [T_RX, T_LEC]),
 ("n14", "réserve de la principale rapportée non écrite", RX, '            elif p == "échec":\n', "            elif False:\n", [T_RX, T_LEC]),
 ("n15", "exemples de validation extraits au lieu de l'entraînement", RX,
  'seqs = extraire(modele, [ex[c]["exemples"][i] for i in ex[c]["e"]], [couche], None)[couche]',
  'seqs = extraire(modele, [ex[c]["exemples"][i] for i in ex[c]["v"]], [couche], None)[couche]', [T_RX]),
 ("n17", "biais b hors de l'écart de la garde", RX,
  '"b": abs(float(s.b) - float(s0.b)) / (abs(float(s0.b)) + float(np.linalg.norm(w0)) * h_max)}', '"b": 0.0}', [T_RX]),
 ("n18", "requête q hors de l'écart de la garde", RX, '        e["q"] = _ecart(s.q, s0.q)\n', '        e["q"] = 0.0\n', [T_RX]),
 ("n21", "noms des directions redonnées non contrôlés", RX,
  "    if [x.nom for x in redonnees] != [x.nom for x in figees]:\n", "    if False:\n", [T_RX]),
 ("n22", "palier de la principale avec palier « carte » (plafond du témoin)", RX,
  '            p, pire = palier([e], tol["processeur"], tol)', '            p, pire = palier([e], tol["carte_sonde"], tol)', [T_RX]),
 ("n23", "seconde garde jouée sous la graine de T0.7 du plancher neuf (au lieu de celle de P3)", RX,
  "list(range(len(j[\"seqs\"]))), n_p3, _graine_p3(p3, cle_p3))", "list(range(len(j[\"seqs\"]))), n_p3, graine_de(f\"plancher/{s.nom}\"))", [T_RX]),
 ("n24", "sceaux des entrées de P3 non contrôlés", RX, "    fichiers = d3.controler(racine, d)\n", "    fichiers = {}\n", [T_RX]),
 ("n25", "tolérances non contrôlées à l'égalité en mode réel", RX,
  '    if mode == "reel" and {k: float(v) for k, v in t.items()} != TOLERANCES:\n', "    if False:\n", [T_RX, T_LEC]),
 ("n25b", "palier « carte » des directions à 0,9", RX, '"carte_directions": 1e-1}', '"carte_directions": 0.9}', [T_RX, T_LEC]),
 ("n25c", "palier global = le meilleur des paliers décisifs", RX,
  '        v["palier"] = max(decisifs, key=PALIERS.index)\n', '        v["palier"] = min(decisifs, key=PALIERS.index)\n', [T_RX, T_LEC]),
 ("n25d", "modèle de P3 chargé en ligne en mode réel (hors_ligne faux)", RX, 'hors_ligne=(mode == "reel"))', "hors_ligne=False)", [T_RX]),
 ("n25e", "fils de torch de P3 non posés pour la principale", RX,
  '            with fils_torch(int(p3["resultat"]["fils_entrainement_effectifs"])) as fils:\n', "            with fils_torch(1) as fils:\n", [T_RX]),
 # --- lecture_v4
 ("n26", "figées : n_p3 directions neuves au lieu de n_plancher", L4,
  'lambda cle: lv1._graine(graines, cle), int(config["n_plancher"]))', 'lambda cle: lv1._graine(graines, cle), int(config[rx.CLE_CONFIG]["n_p3"]))', [T_LEC]),
 ("n28", "réserve de la principale non recopiée à l'étape B", L4, '        for cle in ("reserve", "reserve_principale"):\n', '        for cle in ("reserve",):\n', [T_LEC]),
 ("n29", "paliers et réserves absents de l'index des scores", L4,
  "                         paliers_figees={n: paliers_de(x) for n, x in reextraction[\"par_sonde\"].items() if x[\"etat\"] == \"établi\"})\n",
  "                         paliers_figees={})\n", [T_LEC]),
 ("n31", "clé plancher_figees non contrôlée", L4, '    rx.exiger_config(config[rx.CLE_CONFIG], config["mode"])\n', "    pass\n", [T_LEC]),
 ("n32", "contrôles de la v3 et de la v2 non joués en mode réel", L4,
  '        lv3.exiger_configuration({**config, "n_plancher": lv1.N_PLANCHER_REEL})\n', "        pass\n", [T_LEC]),
 ("n34", "lecture descriptive de P3 écrite dans les scores décisifs (pas de copie)", L4,
  '    t2, idx2, absentes = dict(t), {"sondes": []}, {}\n', '    t2, idx2, absentes = t, {"sondes": []}, {}\n', [T_LEC]),
 ("n35", "lecture descriptive de P3 au niveau 0,5 + ε (au lieu de 0,95)", L4,
  "config, graines, 0.95, jeux_lus, cle=CLE_P3_DESCRIPTIF)", "config, graines, 0.51, jeux_lus, cle=CLE_P3_DESCRIPTIF)", [T_LEC]),
 ("n36", "lecture descriptive de P3 sous les graines décisives", L4,
  "config, graines, 0.95, jeux_lus, cle=CLE_P3_DESCRIPTIF)", 'config, graines, 0.95, jeux_lus, cle="intervalle")', [T_LEC]),
 ("n37", "réextraction après l'apprentissage des sondes neuves (ordre inversé)", L4, None, None, [T_LEC]),
 ("n38", "repli-recalcul admis (renvoyé à lecture_v2)", L4,
  '    if argv and argv[0] == "repli-recalcul":\n        print(', '    if argv and argv[0] == "repli-recalcul":\n        return lv2.main(argv)\n        print(', [T_LEC]),
 ("n39", "directions de P3 notées à la place du plancher neuf quand le bras est établi", L4,
  '                    if s.nom in planchers_p3:\n                        plancher = planchers_p3[s.nom]\n                        source = sources_planchers.get(',
  '                    if s.nom in planchers_p3:\n                        plancher = descriptifs_p3.get(s.nom, planchers_p3[s.nom])\n                        source = sources_planchers.get(', [T_LEC]),
]


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def muter_n37(texte):
    a = texte.index("        t0 = time.perf_counter()                 # v4 : réextraction de P3")
    b = texte.index("        if complete:\n            t0 = time.perf_counter()\n            ext = extracteur")
    bloc = texte[a:b]
    reste = texte[:a] + texte[b:]
    c = reste.index("        noms_finaux = [s.nom for s in principales]\n")
    return reste[:c] + bloc + reste[c:]


def main(arbre, copie, sortie, ids):
    arbre, copie = Path(arbre), Path(copie)
    if not (copie / "src").is_dir():
        shutil.copytree(arbre / "src", copie / "src")
        shutil.copytree(arbre / "docs/sources/invites-2606.08892-v1", copie / "docs/sources/invites-2606.08892-v1")
    res = []
    for ident, titre, fichier, ancien, nouveau, essais in M:
        if ids != ["tout"] and ident not in ids and not (ident == "sain" ):
            continue
        cible = copie / fichier
        sain = (arbre / fichier).read_text(encoding="utf-8")
        if ident == "n37":
            mute = muter_n37(sain)
        else:
            if sain.count(ancien) != 1 and ident != "sain":
                res.append({"id": ident, "titre": titre, "erreur": f"motif trouvé {sain.count(ancien)} fois"}); continue
            mute = sain.replace(ancien, nouveau)
        cible.write_text(mute, encoding="utf-8")
        trace = copie / f"trace-{ident}.json"
        env = dict(os.environ, PYTHONPATH=f"{copie}/src:{arbre}/tests:{Path(__file__).resolve().parents[1]}/greffon",
                   TRACE_IMPORT_SORTIE=str(trace), OPENBLAS_NUM_THREADS="1")
        t0 = time.time()
        r = subprocess.run([PY, "-m", "pytest", "-q", "-o", "pythonpath=", "--rootdir", str(arbre), "-c", str(arbre / "pyproject.toml"),
                            "-p", "trace_import_cl", "-p", "no:cacheprovider", "-k", "not miroir", *essais],
                           cwd=arbre, env=env, capture_output=True, text=True)
        fin = r.stdout.strip().splitlines()
        echecs = [l for l in fin if l.startswith("FAILED") or l.startswith("ERROR")]
        tr = json.loads(trace.read_text()) if trace.exists() else {}
        nom_mod = Path(fichier).stem
        vu = tr.get("modules", {}).get(nom_mod, {})
        res.append({"id": ident, "titre": titre, "fichier": fichier, "code": r.returncode, "tuee": r.returncode != 0,
                    "echecs": [e[:230] for e in echecs], "resume": fin[-1] if fin else "", "duree_s": round(time.time() - t0, 1),
                    "import_de_la_copie": bool(vu) and vu.get("chemin", "").startswith(str(copie.resolve())) if vu else None,
                    "sha_mute_importe": (vu.get("sha256") == sha(cible)) if vu else None,
                    "modules_hors_copie": [k for k, x in tr.get("modules", {}).items() if not x["chemin"].startswith(str(copie.resolve()))]})
        cible.write_text(sain, encoding="utf-8")
        Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(ident, "TUÉE" if r.returncode != 0 else "SURVIT", res[-1]["resume"], flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split(","))
