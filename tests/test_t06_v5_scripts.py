"""Lanceur v5 (C-V5-1 à C-V5-3, R-1657) : un faux `vastai` qui reproduit le comportement réel de vastai 1.8.3 — la recherche par identifiant
rend une liste VIDE, l'identifiant d'une même offre change d'une recherche à l'autre, l'offre du premier rang est retirée à la création —
cas sain et artefacts (R5). Les fixtures et les aides de la v4 sont réutilisées."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret  # noqa: F401
from controle_ia.t06 import session_v4 as s4
from controle_ia.t06.session import GardeSession
from test_t06_v4_scripts import (CONFIG_E2, DF_FACTICE, ENV_DE_BASE, GO_E, OFFRE_E2, RACINE, _commit_source, _config_epreuve, _git,  # noqa: F401
                                 bac, depot_session, src_epreuve)

LANCEUR5 = RACINE / "scripts" / "lancer_t06_v5.sh"
SESSION4 = RACINE / "src" / "controle_ia" / "t06" / "session_v4.py"
VAST_REEL = """#!/usr/bin/env bash
# faux vastai 1.8.3 : recherche par identifiant VIDE ; identifiants qui changent à chaque recherche filtrée ; offre du premier rang retirée
echo "$*" >> "$FAUX_VASTAI_JOURNAL"
case "$1 $2" in
"search offers")
    case "$3" in id=*) echo '[]'; exit 0;; esac
    n=$(cat "$FAUX_COMPTEUR" 2>/dev/null || echo 0); n=$((n + 1)); echo "$n" > "$FAUX_COMPTEUR"
    python3 - "$n" "$FAUX_OFFRES" <<'PY'
import json, sys
n, base = int(sys.argv[1]), json.load(open(sys.argv[2]))
for k, o in enumerate(base):
    o["id"] = 48448000 + 10 * n + k                      # l'identifiant change d'une recherche à l'autre
print(json.dumps(base))
PY
    exit 0 ;;
"create instance")
    echo "$3" >> "$FAUX_CREES"
    nb=$(wc -l < "$FAUX_CREES")
    if [ "${FAUX_RETIRE:-1}" -ge "$nb" ]; then echo '{"success": false, "error": "no_such_ask", "msg": "offre retirée"}'; exit 1; fi
    echo '{"success": true, "new_contract": 777777}'; exit 0 ;;
"show instances") cat "${FAUX_INSTANCES:-/dev/null}" 2>/dev/null || true; [ -n "${FAUX_INSTANCES:-}" ] || echo '[]'; exit 0 ;;
"logs "*) cat "$FAUX_JOURNAL"; exit 0 ;;
esac
if [ "$1" = logs ]; then cat "$FAUX_JOURNAL"; exit 0; fi
echo "appel inattendu : $*" >&2; exit 3
"""
M1, M2, M3 = {"machine_id": 101}, {"machine_id": 102}, {"machine_id": 103}
OFFRES = [{**OFFRE_E2, "dph_total": 0.30, "gpu_name": "RTX 3060", **M3},                     # moins chère mais mauvaise carte : jamais choisie
          {**OFFRE_E2, "dph_total": 0.33, **M2}, {**OFFRE_E2, "dph_total": 0.31, **M1}, {**OFFRE_E2, "dph_total": 0.36, "machine_id": 104}]


@pytest.fixture
def monde5(src_epreuve, tmp_path):
    src = src_epreuve
    shutil.copy(LANCEUR5, src / "scripts" / LANCEUR5.name)
    shutil.copy(SESSION4, src / "src" / "controle_ia" / "t06" / SESSION4.name)
    b = tmp_path / "bin"
    b.mkdir(exist_ok=True)
    for nom, texte in (("vastai", VAST_REEL), ("df", DF_FACTICE)):
        (b / nom).write_text(texte, encoding="utf-8")
        (b / nom).chmod(0o755)
    (tmp_path / "offres.json").write_text(json.dumps(OFFRES), encoding="utf-8")
    (tmp_path / "journal.txt").write_text("AMORCE 2026-11-07T10:00:00Z : commit abc\n", encoding="utf-8")
    return {"src": src, "tmp": tmp_path}


def env5(m, **sup):
    e = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    t = m["tmp"]
    e.update(PATH=f"{t / 'bin'}:{e.get('PATH', '')}", T06_DEPOT=str(m["src"]), CONTROLE_IA_GITHUB_TOKEN="jeton-gh-factice", HOME=str(m["src"].parent),
             FAUX_OFFRES=str(t / "offres.json"), FAUX_VASTAI_JOURNAL=str(t / "appels.txt"), FAUX_COMPTEUR=str(t / "compteur.txt"),
             FAUX_CREES=str(t / "crees.txt"), FAUX_JOURNAL=str(t / "journal.txt"), T06_REGISTRE_GO=str(m["src"] / "registres" / "go.md"),
             T06_BRANCHE_CODE="prep/essai-t06", T06_BRANCHE="essai/t06-e2-test", INTERVALLE="1")
    e.update(sup)
    return {k: v for k, v in e.items() if v is not None}


def v5(m, *args, **sup):
    return subprocess.run(["bash", str(LANCEUR5), *map(str, args)], env=env5(m, **sup), capture_output=True, text=True, timeout=180)


def controles(m, nom="e2"):
    d = m["tmp"] / nom
    r = v5(m, "controles-epreuve", d, _git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e2.json")
    assert r.returncode == 0, r.stdout + r.stderr
    return d


def executer(m, ligne: str, **sup):
    return subprocess.run(["bash", "-c", ligne], env=env5(m, **sup), capture_output=True, text=True, timeout=180)


def test_cas_sain_liste_filtree_id_vide_ids_changeants_offre_retiree_puis_rang_suivant(monde5):
    m = monde5
    d = controles(m)
    r = v5(m, "creation", "auto", "course", "0", d)
    assert r.returncode == 0, r.stdout + r.stderr
    cmd1 = r.stdout.splitlines()[-1]
    appels = (m["tmp"] / "appels.txt").read_text(encoding="utf-8")
    assert "id=" not in appels and "--storage 150" in appels and "-o dph_total" in appels and "gpu_name=RTX_4090" in appels and "rentable=true" in appels     # aucune relecture par identifiant
    assert "RTX 3060" not in cmd1 and f"create instance {48448000 + 10 * 1 + 2} " in cmd1                  # premier rang CONFORME (le rang 1 de la liste est la mauvaise carte) = machine 101 (id de CETTE recherche)
    assert "rang=2 machine=101" in r.stdout and "machine_proposee 101" in (d / "lancement.txt").read_text(encoding="utf-8")
    # la création du premier rang échoue (offre retirée) : aucune instance du programme → rang suivant demandé
    x = executer(m, cmd1)
    assert x.returncode == 5 and "OFFRE REFUSÉE À LA CRÉATION" in x.stdout and "machine 101 exclue" in x.stdout and "creation auto course 0" in x.stdout, x.stdout + x.stderr
    # deuxième essai : nouvelle recherche (les identifiants ont changé), machine 101 exclue → machine 102
    r2 = v5(m, "creation", "auto", "course", "0", d)
    assert r2.returncode == 0 and "machine=102" in r2.stdout and "rang=3" in r2.stdout, r2.stdout + r2.stderr
    cmd2 = r2.stdout.splitlines()[-1]
    assert f"create instance {48448000 + 10 * 2 + 1} " in cmd2 and cmd2 != cmd1                       # autre identifiant (liste relue), autre machine
    x2 = executer(m, cmd2)
    assert x2.returncode == 0 and "CRÉÉE : instance 777777" in x2.stdout, x2.stdout + x2.stderr
    lanc = (d / "lancement.txt").read_text(encoding="utf-8")
    assert "machine_refusee 101" in lanc and lanc.count("essai_creation") == 2 and "prix_carte 0.3300" in lanc          # prix lu DANS LA LISTE


def test_artefacts_liste_vide_identifiant_a_la_main_trois_essais_instance_presente(monde5):
    m = monde5
    d = controles(m)
    r = v5(m, "creation", "48448050", "course", "0", d)
    assert r.returncode == 2 and "auto" in r.stdout                                          # identifiant donné à la main : refusé
    (m["tmp"] / "offres.json").write_text("[]", encoding="utf-8")
    r = v5(m, "creation", "auto", "course", "0", d)
    assert r.returncode == 3 and "liste VIDE" in r.stdout and "essai_creation" not in (d / "lancement.txt").read_text(encoding="utf-8")
    (m["tmp"] / "offres.json").write_text(json.dumps([{**OFFRE_E2, "dph_total": 0.9, "machine_id": 1}]), encoding="utf-8")        # trop chère : aucune conforme
    r = v5(m, "creation", "auto", "course", "0", d)
    assert r.returncode == 3 and "aucune offre conforme" in r.stdout and "prix" in r.stdout
    # trois essais refusés → la quatrième création est refusée
    (m["tmp"] / "offres.json").write_text(json.dumps([{**OFFRE_E2, "dph_total": 0.30 + k / 100, "machine_id": 200 + k} for k in range(5)]), encoding="utf-8")
    for k in range(3):
        r = v5(m, "creation", "auto", "course", "0", d)
        assert r.returncode == 0, (k, r.stdout)
        x = executer(m, r.stdout.splitlines()[-1], FAUX_RETIRE="9")
        assert x.returncode == 5, (k, x.stdout)
    r = v5(m, "creation", "auto", "course", "0", d)
    assert r.returncode == 3 and "trois essais de création déjà faits" in r.stdout
    # refus explicite MAIS une instance du programme existe : création incertaine (code 4), pas de rang suivant
    d2 = controles(m, "e2bis")
    r = v5(m, "creation", "auto", "course", "0", d2)
    inst = m["tmp"] / "instances.json"
    inst.write_text(json.dumps([{"id": 5, "label": "t06-e2", "actual_status": "running", "cur_state": "running"}]), encoding="utf-8")
    x = executer(m, r.stdout.splitlines()[-1], FAUX_RETIRE="9", FAUX_INSTANCES=str(inst))
    assert x.returncode == 4 and "CRÉATION INCERTAINE" in x.stdout and "machine_refusee" not in (d2 / "lancement.txt").read_text(encoding="utf-8")


def test_surveillance_sans_hf_token_en_jouet_et_plafond_nomme(monde5):
    m = monde5
    d = controles(m)
    import time
    with open(d / "lancement.txt", "a", encoding="utf-8") as f:
        f.write(f"prix_carte 0.33\nprix_stockage 0.02\ntelechargement_forfait 0.03\nanterieure 0\ninstance 777777\ncreation {int(time.time()) - 60}\nplafond_creation 1.5\n")
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(["bash", str(LANCEUR5), "surveillance", "777777", str(d)], env=env5(m, HF_TOKEN=None), capture_output=True, text=True, timeout=4)
    s = (d / "surveillance.txt").read_text(encoding="utf-8")
    assert "dépense cumulée ≥ 1.5 USD" in s and "≥ 200 USD" not in s and "surveillance v5" in s                        # C-V5-2 (jouet sans HF_TOKEN), C-V5-3
    # artefacts : sans jeton GitHub, refus ; en mode réel sans HF_TOKEN, refus
    r = subprocess.run(["bash", str(LANCEUR5), "surveillance", "777777", str(d)], env=env5(m, HF_TOKEN=None, CONTROLE_IA_GITHUB_TOKEN="court"), capture_output=True, text=True, timeout=30)
    assert r.returncode == 2 and "jeton GitHub" in r.stdout
    texte = (d / "lancement.txt").read_text(encoding="utf-8").replace("mode jouet", "mode reel")
    (d / "lancement.txt").write_text(texte, encoding="utf-8")
    r = subprocess.run(["bash", str(LANCEUR5), "surveillance", "777777", str(d)], env=env5(m, HF_TOKEN=None), capture_output=True, text=True, timeout=30)
    assert r.returncode == 2 and "HF_TOKEN" in r.stdout and "mode réel" in r.stdout


def test_session_v4_filtre_et_choix():
    cfg = _config_epreuve(CONFIG_E2)
    assert s4.filtre_recherche(cfg, "course") == "num_gpus=1 rentable=true gpu_name=RTX_4090 cpu_ram>=32 cpu_cores_effective>=8 disk_space>=150 dph_total<=0.6"
    assert s4.choisir_offre([{**OFFRE_E2, "dph_total": 0.5, "machine_id": 1}, {**OFFRE_E2, "dph_total": 0.4, "machine_id": 2}], cfg, "course")["machine_id"] == 2   # le moins cher
    r = s4.choisir_offre([{**OFFRE_E2, "dph_total": 0.4, "machine_id": 2}, {**OFFRE_E2, "dph_total": 0.5, "machine_id": 1}], cfg, "course", ["2"])
    assert r["machine_id"] == 1 and r["rang"] == 2
    for liste, motif in (([], "VIDE"), ("x", "illisible"), ([{**OFFRE_E2, "gpu_name": "autre"}], "aucune offre conforme"), ([{**OFFRE_E2, "machine_id": 9}], "déjà refusée")):
        with pytest.raises(GardeSession, match=motif):
            s4.choisir_offre(liste, cfg, "course", ["9"] if motif == "déjà refusée" else ())
    with pytest.raises(GardeSession, match="carte"):
        s4.filtre_recherche(cfg, "autre")
