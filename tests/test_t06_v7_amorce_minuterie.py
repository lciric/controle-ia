"""Amorce v7 de T0.6 (R-1689, défaut trouvé par E2) : au démarrage d'une instance dont l'heure de dépense épuisée est déjà passée, la minuterie relancée ne doit pas
prendre la branche C08 (`PUT stopped`) puisque l'amorce demande la destruction ; l'arrêt gagnait, l'instance restait « exited », non détruite.
Essais : (1) le scénario d'E2 rejoué en vrai (amorce hors essai local, `curl` factice qui journalise les méthodes) : sur l'amorce v6 le `PUT stopped` part (défaut
reproduit) ; sur la v7 seul le `DELETE` part ; (2) la minuterie seule : un ordre de destruction qui arrive PENDANT la consignation de C08 supprime le `PUT stopped`
(deuxième geste) ; cas sain : sans ordre de destruction, C08 envoie toujours `PUT stopped` puis la minuterie détruit à l'échéance."""
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

import pytest

import test_t06_v6_amorce as t6a
from test_t06_v6_amorce import CURL_FACTICE, ENV_DE_BASE, _distant, _lancer_amorce, bac  # noqa: F401

RACINE = Path(__file__).resolve().parents[1]
AMORCE6 = RACINE / "scripts" / "amorce_instance_t06_v6.sh"
AMORCE7 = RACINE / "scripts" / "amorce_instance_t06_v7.sh"


@pytest.fixture(params=["v6", "v7"])
def amorce(request, monkeypatch):
    monkeypatch.setattr(t6a, "AMORCE", AMORCE6 if request.param == "v6" else AMORCE7)
    return request.param


def _curl(tmp_path) -> dict:
    (tmp_path / "bin").mkdir(exist_ok=True)
    (tmp_path / "bin" / "curl").write_text(CURL_FACTICE, encoding="utf-8")
    (tmp_path / "bin" / "curl").chmod(0o755)
    return {"PATH": f"{tmp_path / 'bin'}:{os.environ['PATH']}", "CONTAINER_ID": "424242", "CONTAINER_API_KEY": "cle-factice",
            "MINUTERIE_PAS_S": "1", "MINUTERIE_REESSAI_S": "1", "FAUX_CURL_JOURNAL": str(tmp_path / "curl.txt")}


def test_demarrage_apres_la_depense_epuisee_la_destruction_gagne_sur_l_arret(bac, amorce, tmp_path):
    """Scénario d'E2 : premier run complet (essai local), puis redémarrage HORS essai local alors que l'heure de dépense épuisée est passée et que le marqueur manque.
    v6 : la minuterie envoie `PUT stopped` (défaut) ; v7 : seul le `DELETE` part."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    assert not (racine / "t06-depense-epuisee").exists() and (racine / "t06-fin-normale").exists()
    (racine / "t06-depense-epuisee-utc.txt").write_text(str(int(time.time()) - 30), encoding="utf-8")            # DEP passée
    (racine / "amorce-depot" / "diag" / "apres").mkdir()
    (racine / "amorce-depot" / "diag" / "apres" / "note.json").write_text("{}", encoding="utf-8")                  # un commit en attente à pousser
    code2, _, sortie2, _ = _lancer_amorce(bac, distant, env_sup={"AMORCE_ESSAI_LOCAL": "0", **_curl(tmp_path)})
    methodes = (tmp_path / "curl.txt").read_text(encoding="utf-8").split()
    j = (racine / "t06-minuterie.log").read_text(encoding="utf-8")
    if amorce == "v6":
        assert "PUT" in methodes, (methodes, j)                       # le défaut d'E2 est reproduit par cet essai
        return
    assert code2 == 0, (sortie2[-1500:], j)
    assert methodes == ["DELETE"], (methodes, j)
    assert "instance 424242 détruite" in j and "PUT stopped (" not in j and "DÉPENSE ÉPUISÉE (C08" not in j
    assert "dépense déjà épuisée au démarrage" in (racine / "t06-depense-epuisee").read_text(encoding="utf-8")
    assert "second démarrage après la dépense épuisée" in sortie2 and "poussée des commits en attente d'abord" in sortie2


def test_minuterie_ordre_de_destruction_pendant_la_consignation_supprime_le_put_stopped(bac, amorce, tmp_path):
    """Minuterie seule : à l'heure de dépense épuisée elle consigne ; si l'amorce pose `t06-detruire` pendant la consignation, le `PUT stopped` n'est pas envoyé
    (v6 : il part). Cas sain : sans ordre de destruction, `PUT stopped` puis `DELETE` à l'échéance."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(HOME=str(tmp_path), **_curl(tmp_path))
    for cas in ("ordre", "sain"):
        (tmp_path / "curl.txt").unlink(missing_ok=True)
        for f in ("t06-detruire", "t06-depense-epuisee", "t06-minuterie.log"):
            (racine / f).unlink(missing_ok=True)
        corps = f'#!/usr/bin/env bash\necho "consignation factice"\n' + (f'echo "ordre de l amorce" > "{racine}/t06-detruire"\n' if cas == "ordre" else "")
        (racine / "t06-consigner.sh").write_text(corps, encoding="utf-8")
        now = int(time.time())
        r = subprocess.run(["bash", str(racine / "t06-minuterie.sh"), str(now + 5), str(now - 5), str(racine), "https://api.invalid/v0"],
                           env=env, capture_output=True, text=True, timeout=120)
        j = (racine / "t06-minuterie.log").read_text(encoding="utf-8")
        methodes = (tmp_path / "curl.txt").read_text(encoding="utf-8").split()
        assert r.returncode == 0 and "instance 424242 détruite" in j, (cas, j)
        if cas == "sain":
            assert methodes == ["PUT", "DELETE"] and "PUT stopped (dépense épuisée) : HTTP 200" in j      # C08 inchangée
        elif amorce == "v6":
            assert "PUT" in methodes                                                                          # défaut reproduit
        else:
            assert methodes == ["DELETE"] and "PUT stopped non envoyé : ordre de destruction de l'amorce reçu pendant la consignation (R-1689)" in j


# ---------------------------------------------------------------------------------------------------------------------------------
# R-1692, E2-6 : une échéance qui tombe avant que le run ait produit quoi que ce soit ne laissait RIEN sur la branche (le journal n'était poussé qu'en fin de run)
# ---------------------------------------------------------------------------------------------------------------------------------
BRANCHE_JOUET = "calcul/t06-jouet-v4"
NB_COMMITS_RUN_COMPLET = 4                                                   # « init » + trois commits (résultats et données légères, morceaux, traces) : la poussée initiale ne crée aucun commit (E2-3)


def _sujets(distant):
    return t6a._git(distant, "log", "--format=%s", BRANCHE_JOUET).splitlines()


def test_echeance_sans_resultat_depose_le_journal_sur_la_branche(bac, amorce):
    """Cas sain (v7) : la consignation lancée par la minuterie (`t06-consigner.sh "échéance"`) sans aucun résultat neuf pousse un commit de journal
    (`traces/consignation-…/journal-consignation.txt` : motif, heure, dernière ligne, 400 dernières lignes) ; artefact (v6) : aucun commit, rien sur la branche."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    avant = _sujets(distant)
    journal = next(racine.rglob("journal.txt"))
    with open(journal, "a", encoding="utf-8") as f:
        f.write("2099-01-01T00:00:00Z ÉCHÉANCE 4102444800 atteinte (C14) : consignation (ligne de l'essai)\n2099-01-01T00:00:01Z installation des dépendances (dernière étape de l'essai)\n")
    r = subprocess.run(["bash", str(racine / "t06-consigner.sh"), "échéance"], capture_output=True, text=True, timeout=120)
    assert r.returncode == 0, r.stdout + r.stderr
    apres = _sujets(distant)
    fichiers = [f.split("\t")[-1] for f in t6a._fichiers_distants(distant)]
    traces = [f for f in fichiers if "traces/consignation-" in f and f.endswith("journal-consignation.txt")]
    if amorce == "v6":
        assert apres == avant and not traces, (apres, traces)             # défaut reproduit : le journal ne part pas
        return
    assert len(apres) == len(avant) + 1 and apres[0] == "T0.6 : journal de l'instance (échéance)", apres
    assert len(traces) == 1
    texte = t6a._git(distant, "show", f"{BRANCHE_JOUET}:{traces[0]}")
    assert "motif : échéance" in texte and "ÉCHÉANCE 4102444800 atteinte (C14)" in texte and "dernière étape de l'essai" in texte
    assert "dernière ligne du journal avant la consignation : 2099-01-01T00:00:01Z installation des dépendances" in texte
    assert any(f.endswith("empreintes.sha256") and "traces/consignation-" in f for f in fichiers)


def test_fin_de_run_normale_ne_cree_aucun_commit_de_journal_en_plus(bac, amorce):
    """Aucun commit artificiel : le chemin de fin de run (sans la ligne de commande de consignation) n'écrit jamais `traces/consignation-…` ; le nombre de commits
    de la branche d'un run complet est identique en v6 et en v7."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    assert not [f for f in t6a._fichiers_distants(distant) if "traces/consignation-" in f]
    sujets = _sujets(distant)
    assert not any("journal de l'instance" in s for s in sujets)
    assert len(sujets) == NB_COMMITS_RUN_COMPLET, sujets                    # identique en v6 et en v7


def test_echeance_pendant_la_poussee_finale_v7_ajoute_un_seul_commit_de_journal_apres_les_autres(bac, amorce):
    """Version v7 du cas C-V4-1 (la minuterie lance la consignation pendant la poussée finale) : rien n'est perdu ni croisé ; v6 : quatre commits ; v7 : les quatre mêmes,
    dans le même ordre, puis le seul commit de journal de la consignation d'échéance (R-1692)."""
    hook = """#!/usr/bin/env bash
if [ ! -e "$RACINE_AMORCE/hook-lance" ]; then : > "$RACINE_AMORCE/hook-lance"
  setsid bash "$RACINE_AMORCE/t06-consigner.sh" "échéance" < /dev/null > "$RACINE_AMORCE/concurrent.log" 2>&1 &
  sleep 3
fi
exit 0
"""
    distant = _distant(bac)
    code, journal, sortie, racine = _lancer_amorce(bac, distant, "mn", {"FAUX_PRECOMMIT": hook})
    assert code == 0, sortie[-2500:]
    for _ in range(120):
        if "branche calcul/t06-jouet-v4 poussée (échéance)" in (racine / "concurrent.log").read_text():
            break
        time.sleep(0.5)
    c = (racine / "concurrent.log").read_text()
    assert "branche calcul/t06-jouet-v4 poussée (échéance)" in c and "ERREUR DE CHAÎNE" not in c and "ERREUR DE CHAÎNE" not in journal
    m = t6a._git(distant, "log", "--reverse", "--format=%s", BRANCHE_JOUET).splitlines()
    assert m[0] == "init" and "résultats et données légères" in m[1] and "morceaux" in m[2] and m[3].startswith("T0.6 : traces")
    assert len(m) == (4 if amorce == "v6" else 5), m
    if amorce == "v7":
        assert m[4] == "T0.6 : journal de l'instance (échéance)"


def test_minuterie_a_l_echeance_depose_la_ligne_d_echeance_et_le_journal_sur_la_branche(bac, amorce, tmp_path):
    """Chemin réel de E2-6 : la MINUTERIE (curl factice) atteint l'échéance ; la ligne « ÉCHÉANCE … atteinte (C14) » (écrite par elle) et le journal de l'instance
    arrivent sur la branche avant le DELETE. v6 : rien (défaut) ; v7 : commit « journal de l'instance (échéance) » avec les deux fichiers."""
    distant = _distant(bac)
    code, _, sortie, racine = _lancer_amorce(bac, distant)
    assert code == 0, sortie[-1500:]
    avant = _sujets(distant)
    journal = next(racine.rglob("journal.txt"))
    with open(journal, "a", encoding="utf-8") as f:
        f.write("2099-01-01T00:00:01Z installation des dépendances (dernière étape de l'essai)\n")
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(_curl(tmp_path), HOME=str(tmp_path))
    now = int(time.time())
    r = subprocess.run(["bash", str(racine / "t06-minuterie.sh"), str(now + 2), "0", str(racine), "https://api.invalid/v0"], env=env, capture_output=True, text=True, timeout=120)
    log = (racine / "t06-minuterie.log").read_text(encoding="utf-8")
    assert r.returncode == 0 and "ÉCHÉANCE" in log and "instance 424242 détruite" in log, log
    apres = _sujets(distant)
    fichiers = [f.split("\t")[-1] for f in t6a._fichiers_distants(distant)]
    if amorce == "v6":
        assert apres == avant and not [f for f in fichiers if "traces/consignation-" in f]
        return
    assert apres[0] == "T0.6 : journal de l'instance (échéance)" and len(apres) == len(avant) + 1, apres
    fin = [f for f in fichiers if f.endswith("t06-minuterie-fin.txt")]
    assert len(fin) == 1
    assert "ÉCHÉANCE" in t6a._git(distant, "show", f"{BRANCHE_JOUET}:{fin[0]}")
    jr = [f for f in fichiers if f.endswith("journal-consignation.txt")]
    assert "dernière étape de l'essai" in t6a._git(distant, "show", f"{BRANCHE_JOUET}:{jr[0]}")
    assert "cle-factice" not in t6a._git(distant, "show", f"{BRANCHE_JOUET}:{fin[0]}")
