"""Q5, GD2-05/06/09/10 : entrées du script v3 — fichiers fabriqués, réglages ; refus nommés, erreurs brutes, acceptations.
Usage : python3 -I -B verif_entrees.py DOSSIER_ESSAIS SORTIE.json
"""
import json
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "copie_script", "sim_garde_v3.py")
BASE = ["--sans-n80", "--repetitions", "100", "--tailles", "10", "--deltas", "0.05", "--m", "8", "--K", "3", "--taux", "0.01",
        "--biais", "0", "--comparateurs", "1"]


def lancer(args):
    p = subprocess.run([sys.executable, "-I", "-B", SCRIPT] + args, capture_output=True, text=True, timeout=600)
    err = p.stderr.strip()
    if p.returncode == 0:
        try:
            d = json.loads(p.stdout)
        except ValueError:
            return {"code": 0, "issue": "sortie illisible"}
        fo = d.get("fichiers_observes")
        return {"code": 0, "issue": "accepte", "fichiers_observes": [
            {k: f.get(k) for k in ("forme", "n_observes", "moyenne_brute", "part_nuls")} for f in fo] if fo else None,
            "lois": list(d["lois"]), "k_des_cellules": sorted({c.split("|k=")[1] for c in d["cellules"]})}
    if err.startswith("refus :"):
        return {"code": p.returncode, "issue": "refus nommé", "message": err[:300]}
    return {"code": p.returncode, "issue": "erreur brute", "message": err.splitlines()[-1][:300] if err else ""}


def main():
    dos = sys.argv[1]
    os.makedirs(dos, exist_ok=True)

    def f(nom, contenu, binaire=False):
        ch = os.path.join(dos, nom)
        with open(ch, "wb") as h:
            h.write(contenu if binaire else contenu.encode("utf-8"))
        return ch

    cinq = "\n".join(["0.1", "-0.2", "0.0", "0.05", "0.3"])
    essais = []

    def garde(nom, contenu, n=5, binaire=False, extra=None, sans_effectif=False):
        ch = f(nom, contenu, binaire)
        args = BASE + ["--ecarts", ch] + ([] if sans_effectif else ["--effectif-attendu", str(n)]) + (extra or [])
        essais.append({"cas": nom, "fichier": ch, "resultat": lancer(args)})

    # --- CSV de garde
    garde("ok_ecart.csv", "ecart\n" + cinq + "\n")
    garde("ok_fAfB.csv", "fA,fB\n0.1,0\n0,0.1\n0.2,0.1\n0,0\n0.3,0.3\n")
    garde("virgule_une_colonne.csv", "ecart\n0,1\n-0,2\n0,0\n0,05\n0,3\n")
    garde("virgule_entete_deux_colonnes.csv", "ecart,note\n0,1\n-0,2\n0,0\n0,05\n0,3\n")
    garde("entete_ecart_fA_fB.csv", "ecart,fA,fB\n0.5,0.2,0.1\n0.5,0.2,0.1\n0.5,0.2,0.1\n0.5,0.2,0.1\n0.5,0.2,0.1\n")
    garde("virgule_fAfB.csv", "fA,fB\n0,1,0,2\n0,0,0,1\n0,2,0,1\n0,0,0,0\n0,3,0,3\n")
    garde("effectif_faux.csv", "ecart\n" + cinq + "\n", n=180)
    garde("sans_effectif.csv", "ecart\n" + cinq + "\n", sans_effectif=True)
    garde("ligne_vide_milieu.csv", "ecart\n0.1\n\n-0.2\n0.0\n0.05\n0.3\n")
    garde("ligne_vide_fin.csv", "ecart\n" + cinq + "\n\n")
    garde("ligne_espaces.csv", "ecart\n0.1\n   \n-0.2\n0.0\n0.05\n")
    garde("booleens.csv", "ecart\nTrue\nFalse\n0.1\n0.1\n0.1\n")
    garde("nan.csv", "ecart\nnan\n0.1\n0.1\n0.1\n0.1\n")
    garde("inf.csv", "ecart\ninf\n0.1\n0.1\n0.1\n0.1\n")
    garde("champ_vide.csv", "fA,fB\n0.1,\n0.1,0\n0.1,0\n0.1,0\n0.1,0\n")
    garde("souligne_0.0_5.csv", "ecart\n0.0_5\n0.1\n0.1\n0.1\n0.1\n")
    garde("pourcentages.csv", "ecart\n10\n-20\n0\n5\n30\n")
    garde("bom.csv", b"\xef\xbb\xbfecart\n0.1\n-0.2\n0.0\n0.05\n0.3\n", binaire=True)
    garde("entete_espaces.csv", " ecart \n" + cinq + "\n")
    garde("entete_majuscule.csv", "Ecart\n" + cinq + "\n")
    garde("point_virgule.csv", "fA;fB\n0,1;0\n0;0,1\n0,2;0,1\n0;0\n0,3;0,3\n")
    garde("tabulation.csv", "fA\tfB\n0.1\t0\n0\t0.1\n0.2\t0.1\n0\t0\n0.3\t0.3\n")
    garde("guillemets.csv", 'ecart\n"0,1"\n"-0,2"\n"0,0"\n"0,05"\n"0,3"\n')
    garde("fA_hors_borne.csv", "fA,fB\n1.5,1.0\n0,0\n0,0\n0,0\n0,0\n")
    garde("crlf.csv", "ecart\r\n" + cinq.replace("\n", "\r\n") + "\r\n")
    garde("latin1.csv", "écart\n0.1\n0.1\n".encode("latin-1"), n=2, binaire=True)
    garde("vide.csv", "")
    garde("entete_seul.csv", "ecart\n", n=0)
    garde("plus_signe.csv", "ecart\n+0.1\n-0.2\n0.0\n0.05\n0.3\n")
    garde("rArB_en_garde.csv", "rA,rB\n0.1,0\n0,0.1\n0.2,0.1\n0,0\n0.3,0.3\n")
    garde("colonne_identifiant.csv", "unite,fA,fB\nt1,0.1,0\nt2,0,0.1\nt3,0.2,0.1\nt4,0,0\nt5,0.3,0.3\n")
    # --- JSON de garde
    garde("ok_ecarts.json", json.dumps({"ecarts": [0.1, -0.2, 0.0, 0.05, 0.3]}))
    garde("ok_fAfB.json", json.dumps({"fA": [0.1, 0, 0.2, 0, 0.3], "fB": [0, 0.1, 0.1, 0, 0.3]}))
    garde("json_booleen.json", '{"ecarts": [true, 0.1, 0.1, 0.1, 0.1]}')
    garde("json_null.json", '{"ecarts": [null, 0.1, 0.1, 0.1, 0.1]}')
    garde("json_chaine.json", '{"ecarts": ["0.1", 0.1, 0.1, 0.1, 0.1]}')
    garde("json_nan.json", '{"ecarts": [NaN, 0.1, 0.1, 0.1, 0.1]}')
    garde("json_infinity.json", '{"ecarts": [Infinity, 0.1, 0.1, 0.1, 0.1]}')
    garde("json_1e400.json", '{"ecarts": [1e400, 0.1, 0.1, 0.1, 0.1]}')
    garde("json_entier_401_chiffres.json", '{"ecarts": [' + "1" * 401 + ', 0.1, 0.1, 0.1, 0.1]}')
    garde("json_imbrique.json", '{"ecarts": [[0.1], 0.1, 0.1, 0.1, 0.1]}')
    garde("json_cle_signe.json", json.dumps({"ecarts": [0.1, -0.2, 0.0, 0.05, 0.3], "signe": "B-A"}))
    garde("json_cle_unites.json", json.dumps({"fA": [0.1, 0, 0.2, 0, 0.3], "fB": [0, 0.1, 0.1, 0, 0.3],
                                              "unites": ["t1", "t2", "t3", "t4", "t5"]}))
    garde("json_cle_doublee.json", '{"ecarts": [0.9, 0.9, 0.9, 0.9, 0.9], "ecarts": [0.1, -0.2, 0.0, 0.05, 0.3]}')
    garde("json_racine_liste.json", "[0.1, 0.2, 0.3, 0.4, 0.5]")
    garde("json_longueurs.json", json.dumps({"fA": [0.1, 0, 0.2, 0, 0.3], "fB": [0, 0.1, 0.1, 0]}))
    garde("json_hors_borne.json", json.dumps({"ecarts": [1.5, 0.1, 0.1, 0.1, 0.1]}))
    garde("json_fA_negatif.json", json.dumps({"fA": [-0.1, 0, 0.2, 0, 0.3], "fB": [0, 0.1, 0.1, 0, 0.3]}))
    garde("json_profond.json", "[" * 100000 + "]" * 100000)
    garde("json_rArB_en_garde.json", json.dumps({"rA": [0.1, 0, 0.2, 0, 0.3], "rB": [0, 0.1, 0.1, 0, 0.3]}))
    garde("JSON_MAJUSCULE.JSON", json.dumps({"ecarts": [0.1, -0.2, 0.0, 0.05, 0.3]}))
    garde("json_sans_extension", json.dumps({"ecarts": [0.1, -0.2, 0.0, 0.05, 0.3]}))

    # --- contraste
    g5 = f("g5.json", json.dumps({"ecarts": [0.1, -0.2, 0.0, 0.05, 0.3]}))
    g5b = f("g5b.json", json.dumps({"ecarts": [0.0, 0.0, 0.1, 0.05, 0.0]}))

    def contr(nom, contenu, extra=None, n=5, garde_fichiers=None):
        ch = f(nom, contenu)
        gf = garde_fichiers or g5
        args = BASE + ["--ecarts", gf, "--ecarts-contraste", ch, "--effectif-attendu", str(n)] + (extra or [])
        essais.append({"cas": "contraste:" + nom, "fichier": ch, "resultat": lancer(args)})

    contr("c_ok_rArB.csv", "rA,rB\n0.5,0.4\n0.6,0.3\n0.4,0.4\n0.5,0.5\n0.7,0.4\n")
    contr("c_fAfB.csv", "fA,fB\n0.5,0.4\n0.6,0.3\n0.4,0.4\n0.5,0.5\n0.7,0.4\n")
    contr("c_rA_hors_borne.csv", "rA,rB\n1.5,1.0\n0.6,0.3\n0.4,0.4\n0.5,0.5\n0.7,0.4\n")
    contr("c_rA_hors_borne.json", json.dumps({"rA": [1.5, 0.6, 0.4, 0.5, 0.7], "rB": [1.0, 0.3, 0.4, 0.5, 0.4]}))
    contr("c_ecart.json", json.dumps({"ecarts": [0.1, 0.3, 0.0, 0.0, 0.3]}))
    contr("c_longueur_6.json", json.dumps({"ecarts": [0.1, 0.3, 0.0, 0.0, 0.3, 0.1]}))
    # nombre de fichiers de contraste différent du nombre de garde
    ch1 = f("c1.json", json.dumps({"ecarts": [0.1, 0.3, 0.0, 0.0, 0.3]}))
    essais.append({"cas": "contraste:deux_gardes_un_contraste", "resultat": lancer(
        BASE + ["--ecarts", g5 + "," + g5b, "--ecarts-contraste", ch1, "--effectif-attendu", "5"])})
    essais.append({"cas": "contraste_sans_garde (ignoré ?)", "resultat": lancer(
        BASE + ["--ecarts-contraste", ch1, "--effectif-attendu", "5"])})
    essais.append({"cas": "effectif_sans_fichier (ignoré ?)", "resultat": lancer(BASE + ["--effectif-attendu", "5"])})
    essais.append({"cas": "deux_gardes_comparateurs_1 (k forcé ?)", "resultat": lancer(
        BASE[:-1] + ["1,2,3", "--ecarts", g5 + "," + g5b, "--effectif-attendu", "5"])})
    essais.append({"cas": "garde_reelle_sans_contraste (contraste de secours)", "resultat": lancer(
        BASE + ["--ecarts", g5, "--effectif-attendu", "5"])})

    # --- réglages
    reglages = {
        "alpha_nan": ["--alpha", "nan"], "alpha_0": ["--alpha", "0"], "alpha_1": ["--alpha", "1"],
        "delta_0.6": ["--deltas", "0.6"], "delta_0": ["--deltas", "0"], "delta_nan": ["--deltas", "nan"],
        "delta_0.5_taux_0": ["--deltas", "0.5", "--taux", "0"], "delta_0.5_taux_0.01": ["--deltas", "0.5"],
        "taux_0.95_delta_0.05": ["--taux", "0.95"], "taux_0.9_delta_0.05": ["--taux", "0.9"],
        "taux_0.9_biais_0.2": ["--taux", "0.89", "--biais", "0.2", "--deltas", "0.05"],
        "biais_negatif": ["--biais", "-0.01"], "biais_nan": ["--biais", "nan"],
        "effet_0.6": ["--effet-unite-a", "0.6"], "effet_nan": ["--effet-unite-a", "nan"],
        "effet_0.05_taux_0": ["--effet-unite-a", "0.05", "--taux", "0"],
        "effet_0.5_taux_0.9": ["--effet-unite-a", "0.5", "--taux", "0.9"],
        "graine_-1": ["--graine", "-1"], "repetitions_50": ["--repetitions", "50"], "repetitions_200000": ["--repetitions", "200000"],
        "tailles_vide": ["--tailles", ""], "tailles_5_virgule": ["--tailles", "5,"], "tailles_20001": ["--tailles", "20001"],
        "tailles_garde_compte": ["--tailles", "10,20", "--tailles-garde", "5"], "tailles_garde_0": ["--tailles-garde", "0"],
        "K_0": ["--K", "0"], "m_0": ["--m", "0"], "K_sabotes_compte": ["--K", "3", "--K-sabotes", "3,10"],
        "comparateurs_0": ["--comparateurs", "0"], "comparateurs_65": ["--comparateurs", "65"],
        "ecart_contraste_0.6": ["--ecart-contraste", "0.6"], "ecart_contraste_0": ["--ecart-contraste", "0"],
        "tailles_garde_differentes_ok": ["--tailles-garde", "4"],
    }
    for nom, extra in reglages.items():
        essais.append({"cas": "reglage:" + nom, "resultat": lancer(BASE + extra)})

    bilan = {}
    for e in essais:
        bilan.setdefault(e["resultat"]["issue"], []).append(e["cas"])
    json.dump({"bilan": bilan, "essais": essais}, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
    for e in essais:
        r = e["resultat"]
        print(f'{e["cas"]:45s} {r["issue"]:12s} {r.get("message", "") or r.get("fichiers_observes") or r.get("k_des_cellules")}'[:260])


if __name__ == "__main__":
    main()
