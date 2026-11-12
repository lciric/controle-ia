"""Banc de mutations du lanceur de T0.6, v1 : chaque garde mutée (affaiblie ou retirée) dans une copie du code doit faire
échouer l'essai qui l'éprouve (« tuée » seulement au code 1 de pytest avec « failed ») ; un témoin vert (code sans
mutation) est exigé pour chaque essai visé. Aucun fichier du dépôt n'est touché : tout se joue dans une copie temporaire.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_t06_v1.py [SORTIE.json] [--rapide]

`--rapide` écarte les mutations dont l'essai est la répétition jouet de bout en bout (≈ 40 s chacune).
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
COPIES = ("src/controle_ia", "tests", "scripts", "pyproject.toml", "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256",
          "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v2.json", ".claude/hooks/garde_calcul.py", "docs/sources/invites-2606.08892-v1")
T_C, T_D, T_L, T_T, T_S, T_J, T_SC = ("tests/test_t06_cout.py", "tests/test_t06_distillation.py", "tests/test_t06_lecture.py",
                                      "tests/test_t06_test_croise.py", "tests/test_t06_session.py", "tests/test_t06_lanceur_jouet.py",
                                      "tests/test_t06_scripts.py")
C, D, I, TC, LE, SE, LA, CF = ("src/controle_ia/t06/cout.py", "src/controle_ia/t06/distillation_transcription.py",
                               "src/controle_ia/t06/identite.py", "src/controle_ia/t06/test_croise.py", "src/controle_ia/t06/lecture.py",
                               "src/controle_ia/t06/session.py", "src/controle_ia/t06/lanceur.py", "src/controle_ia/t06/configuration.py")
AM, LN = "scripts/amorce_instance_t06_v1.sh", "scripts/lancer_t06_v1.sh"

# (nom, fichier, ancien, nouveau, essai, -k)
MUTATIONS = [
    ("coût : milliers à l'espace non lus", C, 'NOMBRE = re.compile(rf"(?<![\\d.,])(?P<n>{_MILLIERS_ESPACE}|{_MILLIERS_VIRGULE}|{_SIMPLE})(?!\\d)"',
     'NOMBRE = re.compile(rf"(?<![\\d.,])(?P<n>{_MILLIERS_VIRGULE}|{_SIMPLE})(?!\\d)"', T_C, "milliers"),
    ("coût : 0 tenu pour lisible", C, "and math.isfinite(c) and c > 0", "and math.isfinite(c) and c >= 0", T_C, "illisibles"),
    ("distillation : texte privé admis dans le contexte honnête", D,
     '    if getattr(env_honnete, "instructions_cachees", None) or getattr(env_honnete, "indications_privees", None):\n        raise GardeArret("reconstruction du contexte honnête : l\'environnement porte un texte privé")\n',
     "", T_D, "texte_prive"),
    ("distillation : étiquettes sur toute la transcription", D, "            etiq[d:f] = ids[d:f]\n", "            etiq[:] = ids[:]\n", T_D, "empans"),
    ("distillation : exclusion des mentions retirée", D, 'return [k for k, t in enumerate(textes) if not mesures_action(t)["mention_texte_prive"]]',
     "return list(range(len(textes)))", T_D, "exclusion"),
    ("identité : dose 0 non comparée", I, "        if l0.shape != logits_base.shape or not torch.equal(l0, logits_base):\n            raise GardeArret",
     "        if False:\n            raise GardeArret", T_D, "controle_identite"),
    ("identité : artefact à dose 1 non exigé", I, "        if l1.shape == logits_base.shape and torch.equal(l1, logits_base):\n            raise GardeArret",
     "        if False:\n            raise GardeArret", T_D, "controle_identite"),
    ("identité : empreinte de phase non relue", I, '    if e["empreinte"] != empreinte:\n        raise GardeArret', '    if False:\n        raise GardeArret', T_D, "etat_de_phase"),
    ("test croisé : « au-dessus » au plancher égal", TC, '    au_dessus = resume["bas"] > resume["plancher"]["quantile"]', '    au_dessus = resume["bas"] >= resume["plancher"]["quantile"]', T_T, "etat_du_jeu"),
    ("test croisé : prédicteur trivial ignoré", TC, '    if any(t["separation"] is not None and t["separation"] >= sep for t in resume["triviaux"].values()):\n        return NON_INTERPRETABLE\n',
     "", T_T, "etat_du_jeu or non_interpretable"),
    ("test croisé : sonde apprise sur le pli lu", TC, '    ent = [a for a in jeu if plis[a["tache"]] != pli_lu]', '    ent = [a for a in jeu if plis[a["tache"]] == pli_lu]', T_T, "hors_du_pli or jamais_mise"),
    ("test croisé : tirages dégénérés tolérés", TC, "    if degeneres > MAX_DEGENERES * int(n_tirages):\n        raise GardeArret(f\"{degeneres} tirages dégénérés sur {n_tirages} (plus de 1 %) : lecture arrêtée\")\n",
     "", T_T, "degeneres"),
    ("test croisé : plis de tailles inégales admis", TC, "    if len(uniques) < 4 or len(uniques) % 2:", "    if len(uniques) < 4:", T_T, "partition"),
    ("test croisé : garde d'identité de la notation vectorisée retirée", TC, "            if not abs(sortie[0, 0] - ref) <= TOLERANCE_IDENTITE * (1.0 + abs(ref)):\n                raise GardeArret",
     "            if False:\n                raise GardeArret", T_T, "vectorisee"),
    ("lecture : A3 confondue avec A5", LE, '        elif not t1["contre_adaptateur_temoin"]["etablie"]:\n            ligne = "A3"\n', "", T_L, "table_A"),
    ("lecture : inversion établie ignorée", LE, '    r["T6-2"]["etablie"] = bool(r["T6-2"]["tendance"].get("etablie") and not r["T6-2"]["inversion_etablie"])',
     '    r["T6-2"]["etablie"] = bool(r["T6-2"]["tendance"].get("etablie"))', T_L, "table_A"),
    ("lecture : B1 sans le verdict de P3-bis", LE, '    if verdict_p3bis != "vu" or not bases_t08_lues:', '    if False:', T_L, "tables_B"),
    ("session : plafond non atteint à 200 USD", SE, '"arret": cumulee >= PLAFOND_USD}', '"arret": cumulee > PLAFOND_USD}', T_S, "depense"),
    ("session : run mort non vu", SE, "    if MOTIF_MORT.search(journal):\n        return \"ARRET mort", "    if False:\n        return \"ARRET mort", T_S, "surveillance"),
    ("session : GO d'un autre plafond admis", SE, '    if _plafond(g["plafond"]) != plafond:\n        raise GardeSession', '    if False:\n        raise GardeSession', T_S, "artefacts"),
    ("session : révocation ignorée", SE, '        if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"]):', '        if False:', T_S, "artefacts"),
    ("configuration : DT-5 (b) admise", CF, '    if d["DT-5"] != "a":\n        raise GardeArret', '    if False:\n        raise GardeArret', T_J, "configuration_et_citations"),
    ("lanceur : tâche de distillation dans l'évaluation admise", LA, "    if communes:\n        raise GardeArret", "    if False:\n        raise GardeArret", T_J, "controle_avant_depense"),
    ("lanceur : run réel sans préenregistrement admis", LA, '    if config["mode"] == "reel" and prereg is None:\n        raise GardeArret', '    if False:\n        raise GardeArret', T_J, "configuration_et_citations"),
    ("amorce : ligne RUN MORT retirée", AM, 'echo "AMORCE $(date -u +%FT%TZ) : RUN MORT sans résumé ni arrêt consigné (code $code) : arrêt de l\'instance par son identifiant (R10)" | tee -a "$JOURNAL"',
     'journal "run mort (code $code)"', T_SC, "run_mort"),
    ("amorce : GO non vérifié", AM, '    || refus "$GO_ID non conforme ($GOL)"', '    || true', T_SC, "refus"),
    ("amorce : second démarrage relancé", AM, '[ -d "$R/amorce-depot" ] && refus "redémarrage : dépôt déjà extrait sur le disque (second démarrage) : rien ne repart"\n', "", T_SC, "redemarrage"),
    ("lanceur de session : ARRET non transmis", LN, '            ARRET*) echo "$DEC"; echo "ARRÊT PAR L\'IDENTIFIANT (R10) : timeout -k 5 120 $VAST stop instance $ID"; exit 3 ;;\n', "", T_SC, "run_mort_depense"),
    ("lanceur de session : prix hors devis admis", LN, '        || { echo "prix $PC USD/h ou stockage $PS USD/h hors des bornes du texte ($PRIX_MAX, $STOCKAGE_MAX) : nœud, pas de création"; exit 3; }',
     "        || true", T_SC, "commande_de_creation"),
]
TEMOINS = [("témoin coût", T_C, None), ("témoin distillation", T_D, None), ("témoin lecture", T_L, None), ("témoin test croisé", T_T, None),
           ("témoin session", T_S, None), ("témoin lanceur jouet", T_J, None), ("témoin scripts", T_SC, None)]


def copier(base: Path) -> None:
    for c in COPIES:
        s, d = RACINE / c, base / c
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, symlinks=True)
        else:
            shutil.copy2(s, d)
    for x in ("runs", "diag", "donnees", "registres"):
        (base / x).mkdir(exist_ok=True)
    shutil.copy2(RACINE / "registres" / "go.md", base / "registres" / "go.md")


def pytest_sur(d: Path, essai: str, k: str | None) -> tuple[int, str]:
    cmd = [PYTHON, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", essai] + (["-k", k] if k else [])
    r = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=1800, env={**__import__("os").environ, "PYTHONPATH": "src"})
    return r.returncode, r.stdout[-400:]


def main(argv: list[str]) -> int:
    rapide = "--rapide" in argv
    sortie = next((a for a in argv if a.endswith(".json")), None)
    res = []
    with tempfile.TemporaryDirectory(prefix="banc-t06-") as t:
        base = Path(t) / "base"
        copier(base)
        vus = set()
        for nom, essai, k in TEMOINS:
            if rapide and essai in (T_J, T_SC):
                continue
            code, fin = pytest_sur(base, essai, k)
            statut = "VERT" if code == 0 else "ROUGE"
            res.append({"temoin": nom, "statut": statut, "fin": fin.strip().splitlines()[-1] if fin.strip() else ""})
            print(f"{statut} {nom}", flush=True)
            vus.add(essai)
        for nom, fichier, ancien, nouveau, essai, k in MUTATIONS:
            if rapide and essai in (T_J, T_SC):
                continue
            d = Path(t) / "m"
            shutil.copytree(base, d, symlinks=True)
            f = d / fichier
            s = f.read_text(encoding="utf-8")
            if s.count(ancien) != 1:
                res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": s.count(ancien)})
                print(f"INAPPLICABLE {nom} ({s.count(ancien)} occurrences)", flush=True)
                shutil.rmtree(d)
                continue
            f.write_text(s.replace(ancien, nouveau), encoding="utf-8")
            code, fin = pytest_sur(d, essai, k)
            tuee = code == 1 and "failed" in fin
            res.append({"mutation": nom, "fichier": fichier, "essai": essai, "k": k, "code": code, "statut": "TUÉE" if tuee else "SURVIVANTE",
                        "fin": fin.strip().splitlines()[-1] if fin.strip() else ""})
            print(f"{'TUÉE' if tuee else 'SURVIVANTE'} {nom}", flush=True)
            shutil.rmtree(d)
    survivantes = [r for r in res if r.get("statut") in ("SURVIVANTE", "INAPPLICABLE", "ROUGE")]
    print(f"FIN DU BANC DE MUTATIONS T0.6 v1 ; mutations {len([r for r in res if 'mutation' in r])}, témoins "
          f"{len([r for r in res if 'temoin' in r])}, survivantes ou inapplicables ou témoins rouges : {len(survivantes)}")
    if sortie:
        Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
