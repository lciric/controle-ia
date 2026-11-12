"""Banc de mutations CIBLÉ du lanceur de T0.6, v5 (R-1657 : C-V5-1 à C-V5-3 ; même méthode que les bancs v1 à v4 : chaque garde mutée dans
une copie du code doit faire échouer l'essai qui l'éprouve ; « tuée » seulement au code 1 de pytest avec « failed » ; un témoin vert est
exigé ; rien du dépôt n'est touché). Les 112 mutations de la v4 ne sont pas rejouées : `lancer_t06_v5.sh` n'en change que les blocs de
`creation`, `apres-creation` et `surveillance` visés ici.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_t06_v5.py [SORTIE.json]
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
COPIES = ("src/controle_ia", "tests", "scripts", "pyproject.toml", "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256",
          "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v2.json", "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v3.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v4.json", "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon2.json", "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon3.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v1.json", "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v1.json", ".claude/hooks/garde_calcul.py", "docs/sources/invites-2606.08892-v1")
T_CF, T_SE = "tests/test_t06_v2_configuration.py", "tests/test_t06_v2_session.py"
T_CF3, T_FA, T_LJ, T_SC = ("tests/test_t06_v3_configuration.py", "tests/test_t06_v3_familles.py", "tests/test_t06_v4_lanceur_jouet.py",
                           "tests/test_t06_v4_scripts.py")
T_CF4, T_FA3 = "tests/test_t06_v4_configuration.py", "tests/test_t06_v4_familles.py"
CF, LE, SE, LA2 = ("src/controle_ia/t06/configuration_v2.py", "src/controle_ia/t06/lecture_v2.py", "src/controle_ia/t06/session_v2.py",
                   "src/controle_ia/t06/lanceur_v2.py")
CF3, LA, FV2 = "src/controle_ia/t06/configuration_v3.py", "src/controle_ia/t06/lanceur_v3.py", "src/controle_ia/sondes/familles_v2.py"
CF4, LA4, FV3 = "src/controle_ia/t06/configuration_v4.py", "src/controle_ia/t06/lanceur_v4.py", "src/controle_ia/sondes/familles_v3.py"
S3 = "src/controle_ia/t06/session_v3.py"
AM, LN = "scripts/amorce_instance_t06_v4.sh", "scripts/lancer_t06_v4.sh"

LN5, S4 = "scripts/lancer_t06_v5.sh", "src/controle_ia/t06/session_v4.py"
T5 = "tests/test_t06_v5_scripts.py"
# (nom, fichier, ancien, nouveau, essai, -k)
MUTATIONS_V5 = [
    ("C-V5-1 : recherche par identifiant au lieu du filtre", LN5, 'search offers "$FILTRE"', 'search offers "id=$OFFRE_ARG"', T5, "cas_sain"),
    ("C-V5-1 : machines refusées non exclues", LN5, '"$CARTE" "$EXCL")', '"$CARTE" "")', T5, "cas_sain"),
    ("C-V5-1 : plus de limite de trois essais", LN5, '[ "${ESSAIS:-0}" -lt 3 ]', '[ "${ESSAIS:-0}" -lt 99 ]', T5, "artefacts_liste_vide"),
    ("C-V5-1 : rang suivant sans vérifier l'inventaire", LN5, '--raw > "$D/instances-apres.json" 2>/dev/null && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" "$ETIQ" >/dev/null', '--raw > "$D/instances-apres.json" 2>/dev/null && true', T5, "artefacts_liste_vide"),
    ("C-V5-1 : identifiant donné à la main admis", LN5, '[ "$OFFRE_ARG" = auto ] ||', 'true ||', T5, "artefacts_liste_vide"),
    ("C-V5-1 : recherche filtrée sans le disque demandé (--storage)", LN5, '-o dph_total --storage "$DISQUE" --raw > "$D/offres.json"', '-o dph_total --raw > "$D/offres.json"', T5, "cas_sain"),
    ("C-V5-2 : HF_TOKEN exigé aussi en mode jouet", LN5, '[ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ]', '[ "${#HF_L}" -ge 8 ]', T5, "surveillance_sans_hf"),
    ("C-V5-2 : HF_TOKEN jamais exigé", LN5, '[ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ]', 'true', T5, "surveillance_sans_hf"),
    ("C-V5-3 : texte au plafond de 200", LN5, 'dépense cumulée ≥ $PLC USD (plafond', 'dépense cumulée ≥ 200 USD (plafond', T5, "surveillance_sans_hf"),
    ("C-V5-1 (session) : liste dans l'ordre reçu, pas du prix croissant", S4, 'for rang, o in enumerate(sorted((o for o in offres if isinstance(o, dict)), key=cle), 1):', 'for rang, o in enumerate((o for o in offres if isinstance(o, dict)), 1):', T5, "session_v4"),
    ("C-V5-1 (session) : machine exclue admise", S4, '        if str(o.get("machine_id")) in exclues:', '        if False:', T5, "session_v4"),
    ("C-V5-1 (session) : liste vide non signalée", S4, '    if not offres:\n        raise GardeSession("recherche filtrée : liste VIDE', '    if False:\n        raise GardeSession("recherche filtrée : liste VIDE', T5, "session_v4"),
    ("C-V5-1 (session) : prix maximal absent du filtre", S4, "f\"disk_space>={b['disque_min_go']} dph_total<={c['prix_max_usd_h']}\"", "f\"disk_space>={b['disque_min_go']}\"", T5, "session_v4"),
    ("C-V5-1 (session) : bornes de l'offre non vérifiées", S4, 'r = s2.verifier_offre([o], config, carte)', 'r = {"id": int(o["id"]), "prix_carte": float(o["dph_total"]), "prix_stockage": 0.0, "telechargement": 0.0, "telechargement_forfait_usd": 0.0, "carte": "x", "machine_id": o.get("machine_id")}', T5, "session_v4"),
]
MUTATIONS = MUTATIONS_V5
TEMOINS = [("témoin lanceur v5", T5, None)]


def copier(base: Path) -> None:
    for c in COPIES:
        s, d = RACINE / c, base / c
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, symlinks=True, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)
    for x in ("runs", "diag", "donnees", "registres"):
        (base / x).mkdir(exist_ok=True)
    shutil.copy2(RACINE / "registres" / "go.md", base / "registres" / "go.md")


def pytest_sur(d: Path, essai: str, k: str | None) -> tuple[int, str]:
    cmd = [PYTHON, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", essai] + (["-k", k] if k else [])
    r = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=1800, env={**os.environ, "PYTHONPATH": "src"})
    return r.returncode, r.stdout[-400:]


def main(argv: list[str]) -> int:
    rapide = "--rapide" in argv
    filtre = next((a.split("=", 1)[1] for a in argv if a.startswith("--filtre=")), None)       # ne rejoue que les mutations dont le nom contient ce texte
    sortie = next((a for a in argv if a.endswith(".json")), None)
    res = []
    with tempfile.TemporaryDirectory(prefix="banc-t06-v5-") as t:
        base = Path(t) / "base"
        copier(base)
        for nom, essai, k in TEMOINS:
            if filtre and not any(f in m[0] for m in MUTATIONS if m[4] == essai for f in filtre.split("|")):
                continue
            if rapide and essai in (T_LJ, T_SC):
                continue
            code, fin = pytest_sur(base, essai, k)
            statut = "VERT" if code == 0 else "ROUGE"
            res.append({"temoin": nom, "statut": statut, "fin": fin.strip().splitlines()[-1] if fin.strip() else ""})
            print(f"{statut} {nom}", flush=True)
        for nom, fichier, ancien, nouveau, essai, k in MUTATIONS:
            if filtre and not any(f in nom for f in filtre.split("|")):
                continue
            if rapide and essai in (T_LJ, T_SC):
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
    print(f"FIN DU BANC DE MUTATIONS T0.6 v5 ; mutations {len([r for r in res if 'mutation' in r])} (dont {len(MUTATIONS_V5)} des corrections C-V5-1 à C-V5-3), témoins {len([r for r in res if 'temoin' in r])}, survivantes ou inapplicables ou témoins rouges : {len(survivantes)}")
    if sortie:
        Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
