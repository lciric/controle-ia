"""Q1, Q5 : refus annoncés (GD3-03, 05, 07, 08, 02) et recherche d'autres replis silencieux. Chaque essai lance la copie
conforme du script (python3 -I -B) sur des fichiers fabriqués dans sorties/essais_entrees/ ; on note le code de retour,
la dernière ligne d'erreur et, en cas de succès, les champs de sortie utiles."""
import json, os, subprocess, sys
C = "/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v4/cl"
S = f"{C}/outils/copie_script/sim_garde_v4.py"
E = f"{C}/sorties/essais_entrees"
os.chdir(E)
BASE = ["--repetitions", "100", "--tailles", "5", "--sans-n80", "--deltas", "0.05", "--K", "3", "--taux", "0.01",
        "--biais", "0", "--m", "1"]
def ecrire(nom, contenu):
    with open(nom, "w", encoding="utf-8") as f:
        f.write(contenu)
    return nom
g5 = {"fA": [0.1, 0.0, 0.2, 0.0, 0.1], "fB": [0.0, 0.1, 0.0, 0.0, 0.1]}
r5 = {"rA": [0.5, 0.4, 0.6, 0.5, 0.5], "rB": [0.4, 0.4, 0.5, 0.4, 0.3]}
ids = ["u1", "u2", "u3", "u4", "u5"]
ecrire("g1.json", json.dumps(g5)); ecrire("g2.json", json.dumps(g5)); ecrire("r1.json", json.dumps(r5)); ecrire("r2.json", json.dumps(r5))
ecrire("g1i.json", json.dumps(g5 | {"unite": ids})); ecrire("g2i.json", json.dumps(g5 | {"unite": ids}))
ecrire("r1i.json", json.dumps(r5 | {"unite": ids})); ecrire("r2i.json", json.dumps(r5 | {"unite": ids}))
ecrire("g2i_ordre.json", json.dumps(g5 | {"unite": ids[::-1]}))
ecrire("g2i_entiers.json", json.dumps(g5 | {"unite": [1, 2, 3, 4, 5]})); ecrire("g1i_chaines.json", json.dumps(g5 | {"unite": ["1", "2", "3", "4", "5"]}))
ecrire("g_ids_mixtes.json", json.dumps(g5 | {"unite": [1, "1", 3, 4, 5]}))
ecrire("g_ids_bool.json", json.dumps(g5 | {"unite": [True, False, None, [1], {"a": 1}]}))
ecrire("g_ids_courts.json", json.dumps(g5 | {"unite": ids[:4]}))
ecrire("e_ecarts.json", json.dumps({"ecarts": [0.1, -0.1, 0.0, 0.1, 0.0]}))
ecrire("g_doublon.json", '{"fA": [0.1,0,0.2,0,0.1], "fB": [0,0.1,0,0,0.1], "fA": [0,0,0,0,0]}')
ecrire("g_doublon_imbrique.json", '{"fA": [0.1,0,0.2,0,0.1], "fB": [0,0.1,0,0,0.1], "unite": ["a","b","c","d",{"x":1,"x":2}]}')
ecrire("g_entier31.json", '{"ecarts": [' + "1" * 31 + ', 0, 0, 0, 0]}')
ecrire("g_entier30.json", '{"ecarts": [' + "1" * 30 + ', 0, 0, 0, 0]}')
ecrire("g_entier401.json", '{"ecarts": [' + "1" * 401 + ', 0, 0, 0, 0]}')
ecrire("g_souligne.json", '{"ecarts": [0.0_5, 0, 0, 0, 0]}')
ecrire("g_souligne.csv", "ecart\n0.0_5\n0\n0\n0\n0\n")
ecrire("g_souligne_fafb.csv", "fA,fB\n0.1,0.0_5\n0,0\n0,0\n0,0\n0,0\n")
ecrire("g_ok.csv", "fA,fB\n0.1,0\n0,0.1\n0.2,0\n0,0\n0.1,0.1\n")
ecrire("r_ok.csv", "rA,rB\n0.5,0.4\n0.4,0.4\n0.6,0.5\n0.5,0.4\n0.5,0.3\n")
ecrire("g_unite.csv", "unite,fA,fB\nu1,0.1,0\nu2,0,0.1\nu3,0.2,0\nu4,0,0\nu5,0.1,0.1\n")
ecrire("g_1e400.csv", "ecart\n1e400\n0\n0\n0\n0\n")
ecrire("g_espace.csv", "ecart\n 0.1\n0\n0\n0\n0\n")
ecrire("g_inf_txt.csv", "ecart\ninfinity\n0\n0\n0\n0\n")
os.makedirs("dossier.json", exist_ok=True)
F = ["--effectif-attendu", "5"]
essais = [
 # GD3-03
 ("contraste sans garde", ["--ecarts-contraste", "r1.json"] + F, "refus"),
 ("contraste sans garde, sans effectif", ["--ecarts-contraste", "r1.json"], "refus"),
 ("garde sans contraste", ["--ecarts", "g1.json", "--comparateurs", "1"] + F, "refus"),
 ("garde sans contraste, secours explicite", ["--ecarts", "g1.json", "--comparateurs", "1", "--contraste-synthetique-de-secours"] + F, "accepte"),
 ("secours explicite + contraste réel", ["--ecarts", "g1.json", "--ecarts-contraste", "r1.json", "--comparateurs", "1", "--contraste-synthetique-de-secours"] + F, "?"),
 ("secours sans aucun fichier", ["--contraste-synthetique-de-secours"], "?"),
 ("comparateurs défaut 1,2,3 avec 2 fichiers", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json"] + F, "refus"),
 ("comparateurs 1 avec 2 fichiers", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "1"] + F, "refus"),
 ("comparateurs 2 avec 2 fichiers", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "accepte"),
 ("comparateurs 02 avec 2 fichiers", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "02"] + F, "?"),
 ("comparateurs 2,2 avec 2 fichiers", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2,2"] + F, "?"),
 ("effectif sans fichier", F, "refus"),
 # GD3-08
 ("même fichier de garde deux fois", ["--ecarts", "g1.json,g1.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "refus"),
 ("même fichier de garde, chemin ./", ["--ecarts", "g1.json,./g1.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "?"),
 ("deux fichiers de garde de même contenu", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "?"),
 ("même fichier de contraste, chemin ./", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,./r1.json", "--comparateurs", "2"] + F, "?"),
 ("contraste = garde (même chemin)", ["--ecarts", "e_ecarts.json", "--ecarts-contraste", "e_ecarts.json", "--comparateurs", "1"] + F, "refus"),
 ("contraste = garde (chemin ./)", ["--ecarts", "e_ecarts.json", "--ecarts-contraste", "./e_ecarts.json", "--comparateurs", "1"] + F, "?"),
 # GD3-02
 ("identifiants identiques", ["--ecarts", "g1i.json,g2i.json", "--ecarts-contraste", "r1i.json,r2i.json", "--comparateurs", "2"] + F, "accepte"),
 ("identifiants ordre différent", ["--ecarts", "g1i.json,g2i_ordre.json", "--ecarts-contraste", "r1i.json,r2i.json", "--comparateurs", "2"] + F, "refus"),
 ("identifiants sur garde seulement", ["--ecarts", "g1i.json,g2i.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "refus"),
 ("identifiants sur un seul fichier de garde", ["--ecarts", "g1.json,g2i.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "refus"),
 ("aucun identifiant", ["--ecarts", "g1.json,g2.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "?"),
 ("identifiants 1 (entier) contre \"1\" (chaîne)", ["--ecarts", "g1i_chaines.json,g2i_entiers.json", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2", "--contraste-synthetique-de-secours"] + F, "?"),
 ("identifiants mixtes doublés 1 et \"1\"", ["--ecarts", "g_ids_mixtes.json", "--ecarts-contraste", "r1.json", "--comparateurs", "1"] + F, "refus"),
 ("identifiants booléens, null, liste, objet", ["--ecarts", "g_ids_bool.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "?"),
 ("identifiants trop courts", ["--ecarts", "g_ids_courts.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("colonne unite en CSV", ["--ecarts", "g_unite.csv", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "?"),
 # GD3-05
 ("clé JSON doublée", ["--ecarts", "g_doublon.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("clé doublée imbriquée", ["--ecarts", "g_doublon_imbrique.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("entier JSON 31 chiffres", ["--ecarts", "g_entier31.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("entier JSON 30 chiffres", ["--ecarts", "g_entier30.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("entier JSON 401 chiffres", ["--ecarts", "g_entier401.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("souligné JSON", ["--ecarts", "g_souligne.json", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("souligné CSV ecart", ["--ecarts", "g_souligne.csv", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("souligné CSV fA,fB", ["--ecarts", "g_souligne_fafb.csv", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("souligné dans --deltas", ["--deltas", "0.0_5"] + BASE[2:4] + ["--repetitions", "100", "--sans-n80", "--K", "3", "--taux", "0.01", "--biais", "0", "--m", "1"], "?"),
 ("souligné dans --effectif-attendu", ["--ecarts", "g_ok.csv", "--ecarts-contraste", "r_ok.csv", "--comparateurs", "1", "--effectif-attendu", "0_5"], "?"),
 ("CSV 1e400", ["--ecarts", "g_1e400.csv", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("CSV infinity", ["--ecarts", "g_inf_txt.csv", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "refus"),
 ("CSV espace avant nombre", ["--ecarts", "g_espace.csv", "--contraste-synthetique-de-secours", "--comparateurs", "1"] + F, "?"),
 # autres replis ou erreurs brutes
 ("--ecarts vide", ["--ecarts", ""], "?"),
 ("--ecarts vide avec contraste vide", ["--ecarts", "", "--ecarts-contraste", ""], "?"),
 ("--ecarts virgule finale", ["--ecarts", "g1.json,", "--ecarts-contraste", "r1.json,r2.json", "--comparateurs", "2"] + F, "refus"),
 ("fichier absent", ["--ecarts", "absent.json", "--ecarts-contraste", "r1.json", "--comparateurs", "1"] + F, "refus"),
 ("dossier au lieu d'un fichier", ["--ecarts", "dossier.json", "--ecarts-contraste", "r1.json", "--comparateurs", "1"] + F, "refus"),
 ("effet d'unité à τ = 0", ["--effet-unite-a", "1.0", "--taux", "0"] + ["--repetitions", "100", "--tailles", "5", "--sans-n80", "--deltas", "0.05", "--K", "3", "--biais", "0", "--m", "1"], "?"),
 ("effet d'unité 3,0001", ["--effet-unite-a", "3.0001"], "refus"),
 ("effet d'unité NaN", ["--effet-unite-a", "nan"], "refus"),
 ("effet d'unité avec fichiers réels", ["--ecarts", "g1.json", "--ecarts-contraste", "r1.json", "--comparateurs", "1", "--effet-unite-a", "1.0"] + F, "?"),
 ("indépendants avec fichiers réels", ["--ecarts", "g1.json", "--ecarts-contraste", "r1.json", "--comparateurs", "1", "--comparateurs-independants"] + F, "?"),
 # GD3-07
 ("seuils m = 8 seul", ["--m", "8"] + BASE[:-2], "?"),
 ("seuils α = 0,01, m = 8,1", ["--alpha", "0.01", "--m", "8,1"] + BASE[:-2], "?"),
 ("seuils m = 1 seul", BASE, "?"),
]
res = []
for nom, args, attendu in essais:
    if args and args[0] != "--repetitions" and "--repetitions" not in args:
        args = args + BASE
    p = subprocess.run([sys.executable, "-I", "-B", S] + args, capture_output=True, text=True, timeout=300)
    err = p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ""
    r = {"essai": nom, "attendu": attendu, "code": p.returncode, "erreur": err,
         "refus_nomme": err.startswith("refus :"), "brut": p.returncode != 0 and not err.startswith("refus :")}
    if p.returncode == 0:
        d = json.loads(p.stdout)
        r["lois"] = list(d["lois"])
        r["k"] = sorted({c.split("|k=")[1] for c in d["cellules"]})
        r["fichiers_observes"] = [{k: f[k] for k in ("chemin", "role", "comparateur", "sha256", "unites_identifiees", "forme")} | {"moyenne": f["moyenne_brute"]} for f in d.get("fichiers_observes", [])]
        r["unites"] = d.get("unites"); r["lecture_des_seuils"] = d["reglages"]["lecture_des_seuils"]; r["seuils"] = d["reglages"]["seuils"]
        r["etat_git"] = [d["commit"], d["etat_du_script"]]
        r["secours_dans_reglages"] = d["reglages"]["contraste_synthetique_de_secours"]
        r["deltas"] = d["reglages"]["deltas"]
        with open(f"{E}/sortie-{len(res):02d}.json", "w") as f:
            f.write(p.stdout)
    res.append(r)
    print(f"{nom:55s} attendu={attendu:8s} code={p.returncode} {'REFUS' if r['refus_nomme'] else ('BRUT' if r['brut'] else 'ACCEPTÉ')} {err[:150]}")
json.dump(res, open(f"{C}/sorties/verif_entrees.json", "w"), indent=1, ensure_ascii=False)
