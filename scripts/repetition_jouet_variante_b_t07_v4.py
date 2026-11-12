#!/usr/bin/env python3
"""Répétition jouet, sur une racine locale, du script remis à l'instance de la variante B, **v4**
(`scripts/etape_a_t07_variante_b_v4.sh`) — v4, fichier neuf (R12) : `repetition_jouet_variante_b_t07_v3.py` reste intact, et ses
aides de module (course 7b jouet, run jouet de P3, dépôts distants locaux, API locale) sont importées telles quelles.

Contre-lecture courte des corrections (R-2311) : verdicts touchés par le script v4, plus des passages complets.
1. `normal` (dépôt 1, processeur de cette machine, hors EPYC : `ENV_CPU` non vide) : code 0 ; contrôle avant l'ouverture
   **passé à l'étape 8**, au journal **avant** l'empreinte de la configuration, CODE-T07 et le repli ; deux bras établis ;
   `CUBLAS_WORKSPACE_CONFIG` lu **dans le processus** de l'étape A (`reextraction-p3-t07.json`, `cublas_workspace_avant`).
2. `epyc` (dépôt 1, branche neuve, `CPU_ESSAI` = un nom EPYC : `ENV_CPU` **vide** sous `set -u`) : code 0, même contrôle, journal
   « aucun (EPYC, processeur de P3) », environnement de l'étape A réduit à `CUBLAS_WORKSPACE_CONFIG`, lu dans le processus.
3. `artefact_controle` (dépôt 3 : fichier léger de P3 **sans le témoin de la tromperie**, rescellé, cité par la configuration) :
   **code 2 à l'étape 8**, motif écrit (« témoin … absent »), **rien d'ouvert** : ni CODE-T07, ni branche, ni repli, ni
   ouverture journalisée, ni passe à blanc, ni étape A ; aucune branche poussée au dépôt distant.
4. `artefact_branche_deja_poussee` (dépôt 1, branche du passage 1) : contrôle avant l'ouverture passé, puis code 2 à l'étape 10,
   sans repli (ordre des gestes).
5. `decoupage` (dépôt 1, seuil d'essai bas) : `pousser` avec des fichiers au-dessus du seuil (tableau `ex` non vide, CLC-P3-05) ;
   mêmes contrôles qu'en v3 (recomposition, sceaux, aucun fichier au-dessus du seuil).
6. `cpu_essai_hors_essai` : `CPU_ESSAI` posée hors essai local → refus, code 2. Joué sur la **tête du script seulement** (jusqu'à
   la ligne `MESURE=`, arguments et contrôle des variables d'essai compris) : hors essai, le script entier appellerait l'API de
   Vast à son premier arrêt ; si le refus manquait, la tête finirait en code 0, sans rien écrire.
Borne de taille S-13 : inchangée (même calcul que la v3 ; contrôlée au passage 1).

    PYTHONPATH=src python scripts/repetition_jouet_variante_b_t07_v4.py --dossier <neuf> --sortie <résumé.json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ICI / "src"))
sys.path.insert(0, str(ICI / "scripts"))

import repetition_jouet_t07_v1 as r1  # noqa: E402
import repetition_jouet_t07_v2 as r2  # noqa: E402
import repetition_jouet_variante_b_t07_v3 as r3  # noqa: E402
from controle_ia.t07 import code_t07_v1 as ct  # noqa: E402

SCRIPT = ICI / "scripts" / "etape_a_t07_variante_b_v4.sh"
BR, BR7B, BR_EPYC, BR_DECOUPAGE = r3.BR, r3.BR7B, "donnees/t07-etape-a-epyc-v1", r3.BR_DECOUPAGE
TEMOIN_TROMPERIE = "tromperie-difference_moyennes-c2"
CPU_EPYC = "AMD EPYC 7763 64-Core Processor"
LIGNE_CONTROLE = "contrôle avant l'ouverture (réextraction de P3) : passé ; "


def retirer_temoin(maison: Path, rel_leger: str, nom: str) -> tuple[str, str]:
    """Fichier léger de P3 **sans** la sonde `nom` (témoin), réécrit sous un nom neuf et rescellé (artefact du contrôle)."""
    from controle_ia.premier_test_ia.figees import ecrire_sondes, lire_sondes
    sondes, meta, _ = lire_sondes(maison / rel_leger)
    assert any(s.nom == nom for s in sondes), nom
    rel = rel_leger.replace(".npz", "-sans-temoin.npz")
    return rel, ecrire_sondes(maison / rel, [s for s in sondes if s.nom != nom], meta)


def chercher(x, cle):
    """Valeurs de `cle` à toute profondeur d'un objet JSON."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k == cle:
                yield v
            yield from chercher(v, cle)
    elif isinstance(x, list):
        for v in x:
            yield from chercher(v, cle)


def rang(lignes: list[str], debut: str) -> int:
    return next((i for i, l in enumerate(lignes) if l.startswith(debut)), -1)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dossier", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--entropie-t06", type=int, default=1)
    ap.add_argument("--commit-t06", default=r1.COMMIT_T06)
    a = ap.parse_args(argv)
    script = SCRIPT.resolve()
    base = Path(a.dossier).resolve()
    if base.exists():
        print(f"REFUS : {base} existe déjà (R12)", file=sys.stderr)
        return 2
    base.mkdir(parents=True)
    journal = base / "journal-repetition.txt"
    resume = {"debut": datetime.now(timezone.utc).isoformat(), "commit_t07": r3.git(ICI, "rev-parse", "HEAD"),
              "script": {"chemin": str(script), "sha256": ct._sha(script.read_bytes())},
              "repetition": {"chemin": str(Path(__file__).resolve()), "sha256": ct._sha(Path(__file__).resolve().read_bytes())}}
    # 0. arbre de T0.6 matérialisé par git show ; 1. course 7b jouet ; 1 bis. run jouet de P3 (aides de la v3, telles quelles)
    arbre = base / "arbre-t06"
    commit6 = r3.git(ICI, "rev-parse", f"{a.commit_t06}^{{commit}}")
    emp = r3.montrer(commit6, r3.ARBRE_T06, arbre)
    resume["arbre_t06"] = {"commit": commit6, "fichiers": len(emp),
                           "empreinte_liste": hashlib.sha256(json.dumps(emp, sort_keys=True).encode()).hexdigest()}
    t06 = base / "t06"
    r1.depot_neuf(t06)
    config6 = r1.preparer_t06(t06, arbre)
    r6 = r1.lancer([a.python, "-c", r2.ENVELOPPE, str(a.entropie_t06), "--config", config6.name, "--run-id", r1.RUN_T06], t06,
                   arbre / "src", journal)
    resume["t06"] = {k: r6[k] for k in ("code", "duree_s")}
    if r6["code"] != 0:
        Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1), encoding="utf-8")
        return 1
    run6 = r1.RUN_T06
    p3 = r3.run_p3_jouet(base)
    resume["p3_jouet"] = {"run": r3.RUN_P3, "principales": p3["principales"]}
    # 2. dépôts distants locaux : 1 sain ; 3 artefact (témoin de la tromperie retiré du fichier léger, rescellé, cité)
    o1 = r3.construire_origine(base, "avec-concepts", t06, run6, True, p3)
    vraie = r3.fausser_temoin
    r3.fausser_temoin = retirer_temoin                         # le temps de construire le dépôt 3 seulement (déclaré)
    try:
        o3 = r3.construire_origine(base, "sans-temoin", t06, run6, True, p3, temoin_fausse=TEMOIN_TROMPERIE)
    finally:
        r3.fausser_temoin = vraie
    resume["depots"] = {n: {k: (str(v) if isinstance(v, Path) else v) for k, v in o.items()} for n, o in (("sain", o1), ("sans_temoin", o3))}

    def jouer(racine: Path, o: dict, perimetre: str = r3.PERIMETRE_COMPLET, attendu: str = r3.ATTENDU, extra: dict | None = None,
              branche: str = BR, echeance_s: int = 6 * 3600) -> dict:
        env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(base), "LANG": "C.UTF-8", "GH_TOKEN": "essai-local",
               "ESSAI_LOCAL": "1", "RACINE_INSTANCE": str(racine), "DEPOT_URL": f"file://{o['origine']}", "ESSAIS_LISTE": r3.ESSAIS,
               "VENV_EXISTANT": str(Path(a.python).parents[1]), "GIT_CONFIG_NOSYSTEM": "1",
               **({"TMPDIR": os.environ["TMPDIR"]} if os.environ.get("TMPDIR") else {}), **(extra or {})}
        debut = time.perf_counter()
        p = subprocess.run(["bash", str(script), o["S7"], o["C7"], run6, o["config"], branche, BR7B, attendu,
                            str(int(time.time()) + echeance_s), perimetre], env=env, capture_output=True, text=True, timeout=1800)
        with open(journal, "a", encoding="utf-8") as h:
            h.write(f"$ bash {script.name} … (racine {racine.name}, PERIMETRE {perimetre}, branche {branche})\ncode {p.returncode} en "
                    f"{round(time.perf_counter() - debut, 1)} s\n--- sortie\n{p.stdout[-8000:]}\n--- erreur\n{p.stderr[-4000:]}\n\n")
        fin = racine / "t07-etape-a-b-v1" / "fin-demandee"
        lignes = [l.split(" T07 ", 1)[1] for l in p.stdout.splitlines() if " T07 " in l]
        return {"code": p.returncode, "duree_s": round(time.perf_counter() - debut, 1),
                "fin": fin.read_text().strip() if fin.is_file() else None, "lignes": lignes, "sortie": p.stdout[-2000:],
                "repli_joue": any(l.startswith("repli, essai") for l in lignes), "derniere": lignes[-1] if lignes else None}

    def lire_pousse(org: Path, branche: str, chemin: str) -> bytes:
        presents = set(r3.git(org, "ls-tree", "-r", "--name-only", branche).splitlines())
        if chemin in presents:
            return subprocess.run(["git", "-C", str(org), "show", f"{branche}:{chemin}"], check=True, capture_output=True).stdout
        m = json.loads(r3.git(org, "show", f"{branche}:{chemin}.morceaux.json"))
        d = os.path.dirname(chemin)
        return b"".join(subprocess.run(["git", "-C", str(org), "show", f"{branche}:{d}/{x['fichier']}"], check=True,
                                       capture_output=True).stdout for x in m["morceaux"])

    def controler(racine: Path, o: dict, p: dict, branche: str = BR) -> dict:
        org, c = o["origine"], {}
        lignes = p["lignes"]
        commits = r3.git(org, "log", "--format=%s", f"{o['H']}..{branche}").splitlines()
        c["commits_pousses"] = commits[::-1]
        reg_pousse = r3.git(org, "show", f"{branche}:registres/scellements-v1.md")
        c["lignes_scores_sondes"] = [l.split("|")[1].strip() for l in reg_pousse.splitlines() if l.startswith(("| SCORES-T07 |", "| SONDES-T07 |"))]
        c["src_tests_inchanges"] = subprocess.run(["git", "-C", str(org), "diff", "--quiet", o["C7"], branche, "--", "src", "tests"]).returncode == 0
        run7 = sorted(x for x in r3.git(org, "ls-tree", "--name-only", f"{branche}:runs").splitlines() if "-t07-lecture-" in x)[-1]
        c["run_t07"] = run7
        rxd = json.loads(lire_pousse(org, branche, f"diag/{run7}/reextraction-p3-t07.json"))
        c["reextraction"] = {n: {"etat": v["etat"], "palier": v.get("palier"), "motif": (v.get("motif") or "")[:200]}
                             for n, v in rxd["resultat"]["par_sonde"].items()}
        c["cublas_dans_le_processus"] = sorted(set(str(v) for v in chercher(rxd, "cublas_workspace_avant")))
        pousses = set(r3.git(org, "ls-tree", "-r", "--name-only", branche).splitlines())
        c["planchers_figees_pousses"] = any(x.startswith(f"donnees/{run7}/planchers-figees-t07.npz") for x in pousses)
        nota = json.loads(lire_pousse(org, branche, f"diag/{run7}/notation-t07.json"))["resultat"]
        c["planchers_figees_notation"] = nota.get("planchers_figees", {}).get("etats")
        taille = json.loads(r3.git(org, "show", f"{branche}:traces/t07-etape-a-b-v1/taille-estimee.json"))
        c["taille_planchers_figees_octets"] = taille.get("planchers_figees_t07", {}).get("octets")
        c["taille_sondes_figees"] = taille["entrees"].get("sondes_figees")
        traces = r3.git(org, "show", f"{branche}:traces/t07-etape-a-b-v1/journal-t07.txt")
        c["journal_controle_pousse"] = LIGNE_CONTROLE in traces
        c["controle_pousse"] = json.loads(r3.git(org, "show", f"{branche}:traces/t07-etape-a-b-v1/controle-avant-ouverture.txt"))["figees"]
        pb = [x for x in pousses if x.startswith("passes-blanches-t07/") and x.endswith(".json")]
        c["passe_blanc_reextraction_p3"] = (json.loads(r3.git(org, "show", f"{branche}:{pb[0]}")).get("reextraction_p3") or {}).get("figees") if pb else None
        c["ordre"] = {"controle": rang(lignes, LIGNE_CONTROLE), "empreinte": rang(lignes, "configuration "),
                      "repli": rang(lignes, "repli, essai 1"), "passe_blanc": rang(lignes, "passe à blanc : code"),
                      "etape_a": rang(lignes, "étape A : code")}
        c["processeur"] = next((l for l in lignes if l.startswith("processeur : ")), None)
        c["environnement_etape_a"] = next((l for l in lignes if l.startswith("étape A : environnement ")), None)
        depot_i = racine / "t07-etape-a-b-v1" / "depot"
        c["lecture_sondes_dans_l_arbre"] = (depot_i / "diag" / run6 / "lecture-sondes-t06.json").exists()
        return c

    tromp, enj = p3["principales"]["tromperie"], p3["principales"]["enjeux"]
    passages = {}
    pn = jouer(base / "instance-normal", o1)
    passages["normal"] = {**pn, "controles": controler(base / "instance-normal", o1, pn) if pn["code"] == 0 else None}
    pe = jouer(base / "instance-epyc", o1, extra={"CPU_ESSAI": CPU_EPYC}, branche=BR_EPYC)
    passages["epyc"] = {**pe, "controles": controler(base / "instance-epyc", o1, pe, BR_EPYC) if pe["code"] == 0 else None}
    pa = jouer(base / "instance-artefact-controle", o3)
    depot_a = base / "instance-artefact-controle" / "t07-etape-a-b-v1" / "depot"
    passages["artefact_controle"] = {
        **pa, "branche_au_depot_distant": subprocess.run(["git", "-C", str(o3["origine"]), "rev-parse", "--verify", "-q", f"refs/heads/{BR}"],
                                                         capture_output=True).returncode == 0,
        "ouvertures_journalisees": (depot_a / "registres" / "scellements-v1.md.ouvertures.md").exists(),
        "runs_t07": sorted(x.name for x in (depot_a / "runs").glob("*-t07-lecture-*")) if (depot_a / "runs").is_dir() else [],
        "traces_presentes": sorted(x.name for x in (base / "instance-artefact-controle" / "t07-etape-a-b-v1" / "traces").iterdir()),
        "erreur_controle": (base / "instance-artefact-controle" / "t07-etape-a-b-v1" / "traces" / "controle-avant-ouverture.err").read_text(encoding="utf-8")[:600]
        if (base / "instance-artefact-controle" / "t07-etape-a-b-v1" / "traces" / "controle-avant-ouverture.err").is_file() else None}
    passages["artefact_branche_deja_poussee"] = jouer(base / "instance-artefact-branche", o1)
    pd = jouer(base / "instance-decoupage", o1, extra=r3.DECOUPAGE, branche=BR_DECOUPAGE)
    dec = {"controles": controler(base / "instance-decoupage", o1, pd, BR_DECOUPAGE) if pd["code"] == 0 else None}
    if pd["code"] == 0:
        org = o1["origine"]
        ajoutes = r3.git(org, "diff", "--name-only", "--diff-filter=A", o1["H"], BR_DECOUPAGE).splitlines()
        tailles = {l.split("\t", 1)[1]: int(l.split()[3]) for l in r3.git(org, "ls-tree", "-r", "-l", BR_DECOUPAGE).splitlines()}
        seuil = int(r3.DECOUPAGE["SEUIL_ESSAI"])
        fichiers = []
        for mf in sorted(x for x in ajoutes if x.endswith(".morceaux.json")):
            m = json.loads(r3.git(org, "show", f"{BR_DECOUPAGE}:{mf}"))
            orig = mf[: -len(".morceaux.json")]
            brut = lire_pousse(org, BR_DECOUPAGE, orig)
            compagnon = r3.git(org, "show", f"{BR_DECOUPAGE}:{orig}.sha256").split()[0]
            fichiers.append({"fichier": orig, "octets": m["octets"], "morceaux": len(m["morceaux"]),
                             "recomposition_egale": hashlib.sha256(brut).hexdigest() == m["sha256"] == compagnon,
                             "original_absent_de_la_branche": orig not in tailles,
                             "sceaux_des_morceaux": all(r3.git(org, "show", f"{BR_DECOUPAGE}:{os.path.dirname(orig)}/{x['fichier']}.sha256").split()[0]
                                                        == x["sha256"] for x in m["morceaux"])})
        dec.update({"fichiers_decoupes": fichiers, "ajoutes_au_dessus_du_seuil": sorted(x for x in ajoutes if tailles.get(x, 0) > seuil),
                    "commits_de_morceaux": sum(1 for x in dec["controles"]["commits_pousses"] if ": morceaux " in x)})
    passages["decoupage"] = {**pd, **dec}
    tete = "".join(script.read_text(encoding="utf-8").splitlines(keepends=True)[: rang(script.read_text(encoding="utf-8").splitlines(), "MESURE=") + 1])
    env_h = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(base), "LANG": "C.UTF-8", "CPU_ESSAI": CPU_EPYC}
    q = subprocess.run(["bash", "-c", tete, "bash", *(["x"] * 9)], env=env_h, capture_output=True, text=True, timeout=60)
    q_sain = subprocess.run(["bash", "-c", tete, "bash", *(["x"] * 9)], env={k: v for k, v in env_h.items() if k != "CPU_ESSAI"},
                            capture_output=True, text=True, timeout=60)
    passages["cpu_essai_hors_essai"] = {"code": q.returncode, "sortie": q.stdout[-500:], "erreur": q.stderr[-500:],
                                        "tete_lignes": tete.count("\n"), "cas_sain_code": q_sain.returncode, "cas_sain_sortie": q_sain.stdout[-300:]}
    resume["passages"] = passages
    resume["fin"] = datetime.now(timezone.utc).isoformat()

    n, e, ar, ab, d, h = (passages[k] for k in ("normal", "epyc", "artefact_controle", "artefact_branche_deja_poussee", "decoupage",
                                                "cpu_essai_hors_essai"))
    nc, ec = n["controles"] or {}, e["controles"] or {}

    def deux_bras(c):
        return (bool(c) and len(c["reextraction"]) == 2 and all(v["etat"] == "établi" for v in c["reextraction"].values())
                and c["planchers_figees_pousses"] and c["planchers_figees_notation"] == {tromp: "établi", enj: "établi"})

    def controle_avant_tout(c):
        o = c.get("ordre") or {}
        return (bool(c) and c["journal_controle_pousse"] and set(c["controle_pousse"]) == {tromp, enj}
                and 0 <= o["controle"] < o["empreinte"] < o["repli"] < o["passe_blanc"] < o["etape_a"])
    verdicts = {
        "normal_code_0_deux_bras_etablis": n["code"] == 0 and n["fin"] == "fin 0" and deux_bras(nc),
        "normal_controle_a_l_etape_8_avant_empreinte_code_t07_repli": controle_avant_tout(nc),
        "normal_hors_epyc_env_cpu_non_vide": bool(nc) and "ATEN_CPU_CAPABILITY=avx2 MKL_CBWR=AVX2" in (nc["processeur"] or "")
                                             and nc["environnement_etape_a"] == "étape A : environnement CUBLAS_WORKSPACE_CONFIG=:4096:8 ATEN_CPU_CAPABILITY=avx2 MKL_CBWR=AVX2",
        "normal_cublas_dans_le_processus": bool(nc) and nc["cublas_dans_le_processus"] == [":4096:8"],
        "normal_taille_et_passe_blanc_inchanges": bool(nc) and (nc["taille_planchers_figees_octets"] or 0) > 0 and nc["taille_sondes_figees"] == 2
                                                  and set(nc["passe_blanc_reextraction_p3"] or {}) == {tromp, enj}
                                                  and len(nc["lignes_scores_sondes"]) == 2 and nc["src_tests_inchanges"]
                                                  and not nc["lecture_sondes_dans_l_arbre"],
        "epyc_code_0_env_cpu_vide_sous_set_u": e["code"] == 0 and e["fin"] == "fin 0" and deux_bras(ec) and controle_avant_tout(ec)
                                               and f"essai local : nom du processeur tenu pour « {CPU_EPYC} » (CPU_ESSAI)" in e["lignes"]
                                               and ec["processeur"] == f"processeur : {CPU_EPYC} ; environnement de l'étape A en plus : aucun (EPYC, processeur de P3)"
                                               and ec["environnement_etape_a"] == "étape A : environnement CUBLAS_WORKSPACE_CONFIG=:4096:8"
                                               and ec["cublas_dans_le_processus"] == [":4096:8"] and "unbound variable" not in e["sortie"],
        "artefact_controle_code_2_rien_d_ouvert": ar["code"] == 2 and ar["fin"] == "fin 2"
                                                  and (ar["derniere"] or "").startswith("ARRET : contrôle avant l'ouverture (réextraction de P3) : code 2 : REFUS : contrôle avant l'ouverture : ")
                                                  and f"témoin {TEMOIN_TROMPERIE}" in (ar["derniere"] or "") and "rien n'est ouvert" in (ar["derniere"] or "")
                                                  and not ar["repli_joue"] and not ar["branche_au_depot_distant"] and not ar["ouvertures_journalisees"]
                                                  and ar["runs_t07"] == [] and "code-t07.txt" not in ar["traces_presentes"]
                                                  and not any(l.startswith(("configuration ", "passe à blanc", "étape A", LIGNE_CONTROLE)) for l in ar["lignes"]),
        "artefact_branche_code_2_apres_controle_sans_repli": ab["code"] == 2 and not ab["repli_joue"]
                                                             and 0 <= rang(ab["lignes"], LIGNE_CONTROLE) < len(ab["lignes"]) - 1
                                                             and "présente sur le dépôt distant" in (ab["derniere"] or ""),
        "decoupage_conforme_ex_non_vide": (d["code"] == 0 and d["fin"] == "fin 0" and len(d.get("fichiers_decoupes", [])) >= 2
                                           and all(f["recomposition_egale"] and f["original_absent_de_la_branche"] and f["sceaux_des_morceaux"]
                                                   and f["morceaux"] >= 2 for f in d["fichiers_decoupes"])
                                           and d["ajoutes_au_dessus_du_seuil"] == [] and d["commits_de_morceaux"] >= 2
                                           and controle_avant_tout(d["controles"] or {})),
        "cpu_essai_refuse_hors_essai": h["code"] == 2 and "T07 REFUS : CPU_ESSAI n'est permise qu'en essai local" in h["sortie"]
                                       and h["cas_sain_code"] == 0 and h["cas_sain_sortie"] == "",
    }
    resume["verdicts"] = verdicts
    ok = all(verdicts.values())
    resume["conforme"] = ok
    Path(a.sortie).write_text(json.dumps(resume, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    print(json.dumps({"verdicts": verdicts, "conforme": ok}, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
