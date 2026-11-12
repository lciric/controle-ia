"""[Copie v10 de test_t06_v9_nouveaux.py] Lanceur v10 : essais neufs de la contre-lecture Opus de la v8 (R-1693), de R-1694 à R-1697. Cas sain et artefact (R5) : chaque défaut est rejoué sur le lanceur v8
(défaut reproduit) puis sur le v9 (corrigé)."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import pytest

import test_t06_v12_amorce as t7
from test_t06_v12_amorce import CLES, JOURNAL_BON, RACINE, VASTAI_V8, _env_surveillance, _lancement  # noqa: F401
from test_t06_v12_scripts import controles, env5, executer, monde5, v5  # noqa: F401
from test_t06_v12_amorce import bac, depot_session, src_epreuve  # noqa: F401

LANCEUR8 = RACINE / "scripts" / "lancer_t06_v8.sh"
LANCEUR9 = RACINE / "scripts" / "lancer_t06_v12.sh"
VASTAI_V9 = VASTAI_V8.replace("        vide) echo '{}' ;;", """        vide) echo '{}' ;;
        erreurjson) echo '{"success": false, "error": "invalid_args", "msg": "boum"}' ;;
        id404) echo 'Internal Server Error 500 : instance 40404 indisponible' ; exit 1 ;;
        vraiintrouvable) echo '{"success": false, "status": 404, "msg": "Not Found"}' ;;""")
assert VASTAI_V9 != VASTAI_V8


def _surv(tmp_path, lanceur, journal, env_sup=None, dossier="s", duree=60, vastai=VASTAI_V9, creation_il_y_a=600):
    d = tmp_path / dossier
    _lancement(d, int(time.time()) - creation_il_y_a)
    env = _env_surveillance(tmp_path, journal)
    (tmp_path / "bin" / "vastai").write_text(vastai, encoding="utf-8")
    env.update(FAUX_VASTAI_JOURNAL=str(tmp_path / "appels.txt"), FAUX_COMPTEUR_=str(tmp_path / "n"), ABSENCE_ATTENTE_S="0")
    env.pop("FAUX_INSTANCES", None)
    env.update(env_sup or {})
    env = {k: v for k, v in env.items() if v is not None}
    try:
        r = subprocess.run(["bash", str(lanceur), "surveillance", "123456", str(d)], env=env, capture_output=True, text=True, timeout=duree)
        return r.returncode, r.stdout + r.stderr, d
    except subprocess.TimeoutExpired as e:
        return None, (e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")), d


# --- instance_seule : objet d'erreur, « 404 » dans un identifiant -------------------------------------------------------------------------------------
@pytest.mark.parametrize("seule", ["erreurjson", "id404"])
def test_liste_vide_et_reponse_non_concluante_donne_arret_inventaire_jamais_arret_mort(tmp_path, seule):
    code, sortie, d = _surv(tmp_path / "v9", LANCEUR9, JOURNAL_BON, {"FAUX_LISTE": "vide", "FAUX_SEULE": seule}) if (tmp_path / "v9").mkdir() is None else None
    assert code == 3 and "ARRET inventaire" in sortie and "ARRET mort" not in sortie, sortie[-800:]


@pytest.mark.parametrize("seule", ["erreurjson", "id404"])
def test_v8_reproduit_le_faux_arret_mort(tmp_path, seule):                         # artefact : le lanceur v8 lit ces réponses comme « introuvable »
    (tmp_path / "v8").mkdir()
    code, sortie, d = _surv(tmp_path / "v8", LANCEUR8, JOURNAL_BON, {"FAUX_LISTE": "vide", "FAUX_SEULE": seule})
    assert code == 3 and "ARRET mort" in sortie


def test_vrai_introuvable_donne_arret_mort_a_deux_releves(tmp_path):
    for nom in ("a", "b"):
        (tmp_path / nom).mkdir()
    for seule in ("introuvable", "vraiintrouvable"):
        code, sortie, d = _surv(tmp_path / ("a" if seule == "introuvable" else "b"), LANCEUR9, JOURNAL_BON, {"FAUX_LISTE": "vide", "FAUX_SEULE": seule})
        assert code == 3 and "ARRET mort" in sortie, (seule, sortie[-600:])


# --- échec de masquer ---------------------------------------------------------------------------------------------------------------------------------
def _python_sans_masquage(tmp_path):
    """Faux `python3` : sort en erreur quand on l'appelle comme `masquer` (code `python3 -c` qui lit les quatre clés), sinon passe au vrai interpréteur."""
    b = tmp_path / "bin"
    b.mkdir(exist_ok=True)
    (b / "python3").write_text(f"""#!/usr/bin/env bash
if [ "$1" = "-c" ] && [[ "$2" == *'os.environ.get(k)'* ]]; then cat > /dev/null; exit 1; fi
exec {sys.executable} "$@"
""", encoding="utf-8")
    (b / "python3").chmod(0o755)


def test_echec_de_masquer_alerte_et_aucune_copie_videe(tmp_path):
    (tmp_path / "v9").mkdir()
    (tmp_path / "v8").mkdir()
    for nom, lanceur in (("v8", LANCEUR8), ("v9", LANCEUR9)):
        _python_sans_masquage(tmp_path / nom)
        code, sortie, d = _surv(tmp_path / nom, lanceur, JOURNAL_BON, {"FAUX_LISTE": "presente", "FAUX_SEULE": "repond", "PATH": f"{tmp_path / nom / 'bin'}:{os.environ['PATH']}"}, duree=8)
        vides = [f.name for f in d.glob("*") if f.is_file() and f.stat().st_size == 0 and f.name in ("inventaire-tour.json", "instance-seule.json", "journal-dernier.txt")]
        if nom == "v8":
            assert vides and "masquage" not in sortie, (vides, sortie[-400:])          # défaut reproduit : copie vidée, aucune alerte
        else:
            assert not vides, vides
            assert "ALERTE masquage en échec" in sortie and "ARRET mort" not in sortie, sortie[-600:]


# --- inventaires de la création masqués ----------------------------------------------------------------------------------------------------------------
def test_inventaires_de_creation_sans_cle(monde5, tmp_path):
    m = monde5
    inst = tmp_path / "inst.json"
    inst.write_text(json.dumps([{"id": 5, "label": "autre", "extra_env": [[k, v] for k, v in CLES.items()]}]), encoding="utf-8")
    d = controles(m)
    r = v5(m, "creation", "auto", "course", "0", d, FAUX_INSTANCES=str(inst), **CLES)
    assert r.returncode == 0, r.stdout + r.stderr
    texte = (d / "instances.json").read_text(encoding="utf-8")
    assert "***" in texte and not any(v in texte for v in CLES.values())
    assert not any(v in "\n".join(f.read_text(encoding="utf-8", errors="replace") for f in d.rglob("*") if f.is_file()) for v in CLES.values())


def test_v8_ecrivait_l_inventaire_de_creation_brut(monde5, tmp_path):                  # artefact : la v8 laisse les clés dans instances.json
    m = monde5
    shutil.copy(LANCEUR8, m["src"] / "scripts" / LANCEUR8.name)
    shutil.copy(RACINE / "scripts" / "amorce_instance_t06_v6.sh", m["src"] / "scripts" / "amorce_instance_t06_v6.sh")
    inst = tmp_path / "inst.json"
    inst.write_text(json.dumps([{"id": 5, "label": "autre", "extra_env": [[k, v] for k, v in CLES.items()]}]), encoding="utf-8")
    d = controles(m)                                                                   # contrôles du v9 (même format de lancement.txt)
    r = subprocess.run(["bash", str(LANCEUR8), "creation", "auto", "course", "0", str(d)], env=env5(m, FAUX_INSTANCES=str(inst), **CLES), capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    assert CLES["HF_TOKEN"] in (d / "instances.json").read_text(encoding="utf-8")


# --- set -u : jeton GitHub absent --------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("lanceur, attendu", [(LANCEUR8, 1), (LANCEUR9, 2)])
def test_surveillance_sans_jeton_github_code_2_et_non_127(tmp_path, lanceur, attendu):
    (tmp_path / "s").mkdir()
    code, sortie, d = _surv(tmp_path / "s", lanceur, JOURNAL_BON, {"CONTROLE_IA_GITHUB_TOKEN": None}, duree=30)
    assert code == attendu, (code, sortie[-400:])
    if attendu == 2:
        assert "jeton GitHub absent ou trop court" in sortie


# --- plafond d'épreuve lu dans la configuration, borné par le reste du GO ----------------------------------------------------------------------------
def _publier(m):
    src = m["src"]
    subprocess.run(["bash", "-c", "git add -A && git -c user.email=a@b -c user.name=x commit -q --allow-empty -m cfg"], cwd=src, check=True, capture_output=True)
    t7._git(src, "push", "-q", "origin", "HEAD:refs/heads/prep/essai-t06")
    t7._git(src, "fetch", "-q", "origin", "refs/heads/prep/essai-t06:refs/remotes/origin/prep/essai-t06")


def _controles_plafond(m, plafond, anterieures, nom):
    cfg = m["src"] / "prereg" / "config-epreuve-e2.json"
    c = json.loads(cfg.read_text(encoding="utf-8"))
    c["plafond_usd"] = plafond
    cfg.write_text(json.dumps(c), encoding="utf-8")
    _publier(m)
    sup = {} if anterieures is None else {"T06_DEPENSE_EPREUVES_ANTERIEURES_USD": anterieures}
    e = env5(m, **sup)
    if anterieures is None:
        e.pop("T06_DEPENSE_EPREUVES_ANTERIEURES_USD", None)
    return subprocess.run(["bash", str(LANCEUR9), "controles-epreuve", str(m["tmp"] / nom), t7._git(m["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e2.json"],
                          env=e, capture_output=True, text=True, timeout=120)


@pytest.mark.parametrize("plafond, anterieures, ok", [(4.3, "0.6", True), (1.5, "0", True), (3.5, "0", True), (4.9, "0", True),
                                                      (4.31, "0.6", False), (5, "0", False), (4.3, "0.7", False), (0, "0", False), (-1, "0", False), (4.3, None, False), (4.3, "abc", False)])
def test_plafond_d_epreuve_borne_par_le_reste_du_go(monde5, plafond, anterieures, ok):
    r = _controles_plafond(monde5, plafond, anterieures, "p")
    assert (r.returncode == 0) is ok, r.stdout + r.stderr
    if ok:
        assert f"plafond de l'épreuve {plafond} USD" in r.stdout and "≤ 4.9" in r.stdout
    else:
        assert not (monde5["tmp"] / "p" / "lancement.txt").exists() or "CONTRÔLES D'ÉPREUVE CONFORMES" not in r.stdout


def test_v8_refusait_un_plafond_autre_que_1_5_ou_3_5(monde5):                           # artefact : la liste fermée de la v8
    cfg = monde5["src"] / "prereg" / "config-epreuve-e2.json"
    c = json.loads(cfg.read_text(encoding="utf-8"))
    c["plafond_usd"] = 4.3
    cfg.write_text(json.dumps(c), encoding="utf-8")
    _publier(monde5)
    shutil.copy(LANCEUR8, monde5["src"] / "scripts" / LANCEUR8.name)
    r = subprocess.run(["bash", str(LANCEUR8), "controles-epreuve", str(monde5["tmp"] / "q"), t7._git(monde5["src"], "rev-parse", "HEAD"), "prereg/config-epreuve-e2.json"],
                       env=env5(monde5), capture_output=True, text=True, timeout=120)
    assert r.returncode == 2 and "1.5 (E2) ou 3.5 (E3) seulement" in r.stdout


def test_creation_relit_le_plafond_contre_le_reste_du_go(monde5):
    """La dépense antérieure des autres épreuves est écrite dans lancement.txt par les contrôles : `creation` refuse si elle a été changée pour passer sous la borne."""
    d = controles(monde5)
    lanc = d / "lancement.txt"
    lanc.write_text(lanc.read_text(encoding="utf-8").replace("epreuves_anterieures 0", "epreuves_anterieures 4.9"), encoding="utf-8")
    r = v5(monde5, "creation", "auto", "course", "0", d)
    assert r.returncode == 2 and "hors du reste du GO" in r.stdout


# --- clause de mémoire de carte envoyée à Vast --------------------------------------------------------------------------------------------------------
def test_la_recherche_envoyee_a_vast_porte_la_clause_gpu_ram_en_go(monde5):
    d = controles(monde5)
    r = v5(monde5, "creation", "auto", "course", "0", d)
    assert r.returncode == 0, r.stdout + r.stderr
    appels = (monde5["tmp"] / "appels.txt").read_text(encoding="utf-8")
    assert "gpu_ram>=19 " in appels and "gpu_ram>=19000" not in appels


def test_creation_inventaire_masquage_en_echec_refuse_la_creation(monde5, tmp_path):
    """Le masquage de l'inventaire échoue : code 2, « masquage en échec », aucun fichier d'inventaire brut ni vide, aucune ligne de création."""
    m = monde5
    _python_sans_masquage(m["tmp"])
    d = controles(m)
    r = v5(m, "creation", "auto", "course", "0", d, PATH=f"{m['tmp'] / 'bin'}:{os.environ['PATH']}", **CLES)
    assert r.returncode == 2 and "masquage en échec" in r.stdout, r.stdout + r.stderr
    assert not (d / "instances.json").exists() and not (d / "instances.json.tmp").exists()
    assert "create instance" not in r.stdout


# --- R5 cas 4 de la contre-lecture de la v9 ------------------------------------------------------------------------------------------------------------
def test_r5_cas4_refus_de_plafond_code_2_et_motif_exact(monde5):
    """Le refus d'un plafond d'épreuve garde le code 2 (les ordres d'E3 scellés l'attendent) et dit son motif exact."""
    r = _controles_plafond(monde5, 4.31, "0.6", "p-refus")
    assert r.returncode == 2, r.stdout + r.stderr
    assert "plafond_usd 4.31 refusé : plafond d'épreuve 4.31 + dépense antérieure 0.6 = 4.91 > 4.9 (reste du GO de 5 USD, marge 0.1)" in r.stdout, r.stdout
    r2 = _controles_plafond(monde5, 4.3, None, "p-sans-donnee")
    assert r2.returncode == 2 and "T06_DEPENSE_EPREUVES_ANTERIEURES_USD" in r2.stdout, r2.stdout
    r3 = _controles_plafond(monde5, 4.3, "0.6", "p-ok")
    assert r3.returncode == 0 and "plafond d'épreuve 4.3 + dépense antérieure 0.6 = 4.9 ≤ 4.9" in r3.stdout, r3.stdout


def test_r5_cas4_apres_creation_masquage_en_echec_creation_incertaine_sans_fichier_brut(monde5):
    m = monde5
    d = controles(m)
    refus = m["tmp"] / "sortie-create.json"
    # cas sain : refus explicite, inventaire (vide) lu et masqué → rang suivant proposé (code 5)
    refus.write_text('{"success": false, "error": "no_such_ask", "msg": "offre retirée"}', encoding="utf-8")
    r = subprocess.run(["bash", str(LANCEUR9), "apres-creation", str(refus), "1", str(d)], env=env5(m), capture_output=True, text=True, timeout=120)
    assert r.returncode == 5 and "OFFRE REFUSÉE À LA CRÉATION" in r.stdout, r.stdout + r.stderr
    assert (d / "instances-apres.json").is_file()
    (d / "instances-apres.json").unlink()
    # artefact : le masquage échoue → « CRÉATION INCERTAINE » (code 4), aucun fichier d'inventaire, ni brut, ni vide, ni temporaire
    _python_sans_masquage(m["tmp"])
    refus.write_text('{"success": false, "error": "no_such_ask", "msg": "offre retirée"}', encoding="utf-8")
    r = subprocess.run(["bash", str(LANCEUR9), "apres-creation", str(refus), "1", str(d)], env=env5(m, PATH=f"{m['tmp'] / 'bin'}:{os.environ['PATH']}", **CLES),
                       capture_output=True, text=True, timeout=120)
    assert r.returncode == 4 and "CRÉATION INCERTAINE" in r.stdout, r.stdout + r.stderr
    assert not (d / "instances-apres.json").exists() and not (d / "instances-apres.json.tmp").exists()
