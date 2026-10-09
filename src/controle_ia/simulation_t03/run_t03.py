"""Simulation de T0.3 — lancement de bout en bout sous préenregistrement scellé (R1, R9).

    PYTHONPATH=src python -m controle_ia.simulation_t03.run_t03 \\
        --prereg prereg/T0.3-simulation-lemme-theoreme-v1.md --grille prereg/T0.3-grille-v2.json

    Réplication gelée (cellules statistiques contraires) :
        … --replication-de <run_id principal>

Chaîne : grille scellée et citée par le préenregistrement → manifeste décisif (préenregistrement
scellé exigé) → calibrage sous P₀ et gardes → garde d'équivalence → blocs → lecture gelée →
résultats scellés dans diag/<run_id>/. Toute garde qui échoue arrête le run (liste d'arrêt).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, verifier_resultat
from ..scellement import sceller, verifier
from . import blocs as B
from . import lecture as LEC

EQUIVALENCE_TOLERANCE = 1e-9


def taches(grille: dict) -> list[str]:
    """Toutes les tâches à graine du run, dans l'ordre exact de leur usage par les blocs."""
    t = []
    for cfg in grille["configs"]:
        t += [f"calib/{cfg}", f"p0/{cfg}", f"equivalence/{cfg}"]
    g = grille["P1a"]
    for N, T in g["configs"]:
        n0 = N * T
        for Bv in g["B"]:
            base = f"P1a/{N}x{T}/B{Bv}"
            t.append(f"{base}/Y")
            for schema in g["schemas"]:
                if N == 1 and schema in ("un_agent", "reparti"):
                    continue
                for m in g["m"]:
                    if m > n0 or (schema == "un_agent" and m > T):
                        continue
                    for genre in (["egaux", "dirichlet"] if schema == "aleatoire" else ["egaux"]):
                        t.append(f"{base}/{schema}/m{m}/{genre}")
    for N, T in grille["P1b"]["configs"]:
        for Bv in grille["P1b"]["B"]:
            t += [f"P1b/{N}x{T}/B{Bv}/Y", f"P1b/{N}x{T}/B{Bv}/positions"]
    for Bv in grille["P2"]["B"]:
        for m in grille["P2"]["m"]:
            t += [f"P2/B{Bv}/m{m}/Y", f"P2/B{Bv}/m{m}/positions"]
    g = grille["P3"]
    for N, T in g["configs"]:
        for Bv in g["B"]:
            base = f"P3/{N}x{T}/B{Bv}"
            t.append(f"{base}/Y")
            t += [f"{base}/m{m}/{s}" for m in g["m"] for s in g["calendriers"]]
    for Bv in grille["P34"]["B"]:
        for m in grille["P34"]["m"]:
            t.append(f"P34/B{Bv}/m{m}/Y")
    g = grille["P4"]
    for N, T in g["configs"]:
        t.append(f"P4/{N}x{T}/Y")
        t += [f"P4/{N}x{T}/{a}" for a in g["arrangements_T1"] if N == 1 or a != "apparie_autocorr"]
        t += [f"P4/{N}x{T}/{a}/rebrassage" for a in g["arrangements_T2"]]
    t += ["P43/Y", "P43/rebrassage_total", "P43/rebrassage_intra_agent"]
    t.append("P5/temps/Y")
    t += [f"P5/temps/bloc_r{r}" for r in grille["P5_temps"]["r"]]
    t += ["P5/temps/apparie_autocorr", "P5/temps/apparie_suites", "P5/agents/Y", "P5/agents/co_elevation_top"]
    t += [f"P6/{c['nom']}" for c in grille["P6"]["cellules"]]
    t.append("P7/Y")
    for s in grille["P8"]["reglages"]:
        t.append(f"P8/{s['nom']}")
        t += [f"P8/{s['nom']}/conforme/{l}" for l in range(int(grille["P8"]["conforme"]["L"]))]
    return t


def configs_des_blocs(grille: dict, blocs: list[str]) -> list[str]:
    usage = grille["configs_par_bloc"]
    voulues = {c for b in blocs for c in usage[b]}
    return [c for c in grille["configs"] if c in voulues]


COMMIT_CITE = re.compile(r"Commit du code d'analyse : `([0-9a-f]{40})`")


def charger_grille(racine: Path, grille: Path, prereg: Path) -> tuple[dict, str]:
    sha = verifier(grille)
    texte = prereg.read_text(encoding="utf-8")
    if sha not in texte:
        raise GardeArret(f"le préenregistrement {prereg} ne cite pas l'empreinte de la grille ({sha})")
    return json.loads(grille.read_text(encoding="utf-8")), sha


def exiger_code_cite(racine: Path, prereg: Path, grille: Path) -> str:
    """Garde : le code d'analyse, les tests et la grille au lancement sont ceux du commit cité par le
    préenregistrement (aucune différence entre ce commit et HEAD sur ces chemins)."""
    m = COMMIT_CITE.search(prereg.read_text(encoding="utf-8"))
    if not m:
        raise GardeArret(f"{prereg} ne cite pas le commit du code d'analyse (40 caractères hexadécimaux)")
    commit = m.group(1)
    try:
        grille_rel = str(grille.resolve().relative_to(racine.resolve()))
    except ValueError:
        raise GardeArret(f"la grille {grille} est hors du dépôt {racine}") from None
    chemins = ["src", "tests", grille_rel]
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "HEAD", "--", *chemins],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"code d'analyse, tests ou grille modifiés depuis le commit cité {commit[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit cité {commit[:12]} impossible : {r.stderr.strip()}")
    return commit


def ecrire_md(chemin: Path, texte: str) -> Path:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    chemin.write_text(texte, encoding="utf-8")
    sceller(chemin)
    return chemin


def tableau_md(lecture: dict, programme: list[dict], titre: str) -> str:
    lignes = [f"# {titre}", "", "Lecture mécanique des critères gelés (`controle_ia.simulation_t03.lecture`).", "",
              "| prédiction | verdict | cellules | conformes | contraires | à répliquer | à auditer |",
              "|---|---|---|---|---|---|---|"]
    for k, x in lecture["predictions"].items():
        lignes.append(f"| {k} | {x['verdict']} | {x['n_cellules']} | {x['n_conformes']} | {x['n_contraires']} | "
                      f"{len(x.get('a_repliquer', []))} | {len(x.get('a_auditer', []))} |")
    a = lecture["audit_symetrie"]
    lignes += ["", f"Audit de symétrie (R4), bornes {a['bornes']} : formes closes, variance des écarts réduits "
               f"{a['formes_closes']['variance_z']:.3f} sur {a['formes_closes']['n']} ; égalités, "
               f"{a['egalites']['variance_z']:.3f} sur {a['egalites']['n']} ; déclenché : {a['audit_declenche']}.", "",
               "## Énoncés du programme (table E)", "", "| énoncé | lecture | exigées | complémentaires |",
               "|---|---|---|---|"]
    for ligne in programme:
        lignes.append(f"| {ligne['enonce']} | {ligne['lecture']} | {', '.join(ligne['exiges'])} | "
                      f"{', '.join(ligne['complementaires']) or '—'} |")
    return "\n".join(lignes) + "\n"


def exiger_code_importe_sous(racine: Path) -> None:
    """Garde : le code exécuté (modules importés) est celui de `racine/src`, celui que vérifie la garde
    du commit cité ; sinon on vérifierait un arbre et on en exécuterait un autre."""
    import controle_ia

    code = Path(controle_ia.__file__).resolve()
    attendu = (racine / "src").resolve()
    if attendu not in code.parents:
        raise GardeArret(f"code importé depuis {code.parent}, hors de {attendu} : lancer depuis la racine du dépôt")


def executer(racine: str | Path, prereg: str | Path, grille_chemin: str | Path, run_id: str,
             blocs: list[str] | None = None, replication_de: str | None = None, limite_s: float = 6 * 3600,
             verifier_import: bool = True) -> dict:
    """`blocs` n'est jamais accepté de l'extérieur : run principal complet ; en réplication, les blocs sont
    déterminés par la lecture principale. `verifier_import=False` n'est permis qu'aux tests sur mini-dépôt,
    qui n'hébergent pas le code ; la ligne de commande l'active toujours."""
    racine, prereg, grille_chemin = Path(racine), Path(prereg), Path(grille_chemin)
    if blocs is not None:
        raise GardeArret("les blocs ne se choisissent pas : run principal complet, réplication déterminée par la lecture")
    if verifier_import:
        exiger_code_importe_sous(racine)
    grille, sha_grille = charger_grille(racine, grille_chemin, prereg)
    commit_cite = exiger_code_cite(racine, prereg, grille_chemin)
    principale = None
    if replication_de:
        corps = verifier_resultat(racine, racine / "diag" / replication_de / "lecture.json")
        principale = corps["resultat"]["lecture"]
        preds = {k for k, x in principale["predictions"].items() if x["a_repliquer"]}
        blocs = [b for m, bs in LEC.BLOCS_DE.items() if any(p.startswith(m + ".") for p in preds) for b in bs]
        if not blocs:
            raise GardeArret("rien à répliquer dans la lecture principale")
    blocs = blocs or list(B.BLOCS)
    inconnus = [b for b in blocs if b not in B.BLOCS]
    if inconnus:
        raise GardeArret(f"blocs inconnus : {inconnus}")
    ts = taches(grille)
    commande = "python -m controle_ia.simulation_t03.run_t03 " + " ".join(sys.argv[1:])
    config = {"grille": grille, "grille_sha256": sha_grille, "blocs": blocs, "replication_de": replication_de,
              "commit_cite": commit_cite}
    chemin_m, m = creer_manifeste(racine, run_id, config, ts + [x + "/replication" for x in ts],
                                  entropie=int(grille["entropie"]), decisif=True, prereg=prereg, commande=commande)
    ctx = B.Contexte(grille, m["graines"], suffixe="/replication" if replication_de else "",
                     facteur_R=int(grille["replication"]["facteur_R"]) if replication_de else 1)
    debut = time.monotonic()
    journal = {}

    def chrono(nom):
        journal[nom] = round(time.monotonic() - debut, 1)
        if journal[nom] > limite_s:
            raise GardeArret(f"durée {journal[nom]} s > limite {limite_s} s (liste d'arrêt)")

    cfgs = configs_des_blocs(grille, blocs)
    calib = {cfg: B.calibrer(ctx, cfg) for cfg in cfgs}
    ecrire_resultat(racine, chemin_m, "calibrage", {"configs": calib, "rho": {str(k): v for k, v in ctx.rho.items()}})
    chrono("calibrage")
    manques = [x for cfg in cfgs for x in B.garde_p0(calib[cfg], ctx.alpha, LEC.Z)]
    if manques:
        raise GardeArret("garde de calibrage sous P₀ (liste d'arrêt) : " + " ; ".join(manques))
    eq = {cfg: B.equivalence(ctx, cfg, int(grille["tailles"]["equivalence"])) for cfg in cfgs}
    ecrire_resultat(racine, chemin_m, "equivalence", eq)
    chrono("equivalence")
    ecarts = [(cfg, s, e) for cfg, x in eq.items() for s, e in x["ecart_relatif_max"].items() if not e <= EQUIVALENCE_TOLERANCE]
    if ecarts:
        raise GardeArret(f"garde d'équivalence (liste d'arrêt) : {ecarts}")
    resultats = {"calibrage": calib}
    for b in blocs:
        resultats[b] = B.BLOCS[b](ctx)
        ecrire_resultat(racine, chemin_m, f"bloc-{b}", resultats[b])
        chrono(b)
    lec = LEC.lire(resultats, ctx.alpha, grille["P8"]["lecture"])
    sortie = {"lecture": lec, "journal_s": journal}
    if principale is not None:
        finale = LEC.fusionner(principale, lec)
        sortie["lecture_finale"] = finale
        sortie["programme"] = LEC.enonces_du_programme(finale)
    else:
        sortie["programme"] = LEC.enonces_du_programme(lec)
    chemin_l = ecrire_resultat(racine, chemin_m, "lecture", sortie)
    ecrire_md(chemin_l.with_suffix(".md"), tableau_md(sortie.get("lecture_finale", lec), sortie["programme"],
                                                      f"Lecture gelée — run {run_id}"))
    return {"run_id": run_id, "manifeste": str(chemin_m), "lecture": str(chemin_l), "journal_s": journal}


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--prereg", required=True)
    a.add_argument("--grille", required=True)
    a.add_argument("--run-id", default=None)
    a.add_argument("--replication-de", default=None)
    args = a.parse_args(argv)
    suffixe = "t03-replication" if args.replication_de else "t03"
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + suffixe
    print(json.dumps(executer(args.racine, args.prereg, args.grille, run_id, None, args.replication_de),
                     indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
