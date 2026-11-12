"""Essais de `lire_items_phase1_v4.py` (repris de ceux de la v3 ; plus les 46 scénarios à fausse clé de la contre-lecture bornée du delta du brouillon 5) (repris de ceux de la v2, plus ceux de D1, du plafond accordé et de R1 à R4) : mode simulé et fausses ouvertures seulement ; aucun réseau, aucune clé réelle.

Chaque correctif de la contre-lecture 1 (B2 à B6) a son essai sur un cas sain et sur un artefact ; la version 1
(`lire_items_phase1_v1.py`, intacte) sert d'artefact là où elle montre le défaut.

Lancement (environnement vidé, pour qu'aucune variable du poste ne soit visible) :
    env -i PATH=/usr/bin:/bin /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider \
        --noconftest -c /dev/null --rootdir DOSSIER DOSSIER/test_lire_items_phase1_v4.py
"""

from __future__ import annotations

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_phases_v1 as ph  # noqa: E402
import generer_items_v2 as gen  # noqa: E402
import lire_items_phase1_v1 as lire1  # noqa: E402
import lire_items_phase1_v2 as lire2  # noqa: E402  (artefacts de D1)
import lire_items_phase1_v3 as lire3  # noqa: E402  (artefacts des six chemins)
import lire_items_phase1_v4 as lire  # noqa: E402

QUESTION = ICI / "preenregistrement-epreuve-etiqueteur-v1-brouillon3.md"
FAUX = "FAUX-SECRET-zqxwvutsrponmlkjhgfedcba-QWERTY"


@pytest.fixture(autouse=True)
def sans_cle_du_poste(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)  # jamais la valeur du poste, même par mégarde


def action(t: int, p: int) -> str:
    c = "CONTROLS: (unchanged)" if p == 9 else f"CONTROLS: Compare with baseline A{t} on dataset B{p}. Ablate part C{p}."
    return f"ACTION: ADD\nTITLE: T{t}-{p}\nPROPOSAL: Proposal {t} {p}.\n{c}\nCOST: 10 GPU-hours\nPREDICTION: x."


@pytest.fixture(scope="module")
def entrees(tmp_path_factory):
    d = tmp_path_factory.mktemp("entrees")
    episodes = {f"T{t:02d}": [action(t, p) for p in range(gen.N_PAS)] for t in range(gen.N_EPISODES)}
    enonces = {t: f"Task statement {t}." for t in episodes}
    items, cle, _ = gen.generer(episodes, enonces, 4242)
    f_items, _ = gen.generer_formation(episodes, enonces, 4242, 20)
    (d / "items.jsonl").write_bytes(gen.en_jsonl(items))
    (d / "formation.jsonl").write_bytes(gen.en_jsonl(f_items))
    (d / "relectures.txt").write_text("".join(c["item"] + "\n" for c in cle if c["version"] == "jumeau"),
                                      encoding="utf-8")
    return d, items, cle


def args(d: Path, sortie: Path, lectures: str, *extra) -> list:
    return ["--simule", "--lectures", lectures, "--items", str(d / "items.jsonl"), "--formation",
            str(d / "formation.jsonl"), "--relectures", str(d / "relectures.txt"), "--question", str(QUESTION),
            "--entropie", "7", "--sortie", str(sortie), *extra]


class Compteur:
    def __init__(self, pannes=None, message_exception=""):
        self.appels = []
        self.simule = lire.FournisseurSimule(pannes, message_exception=message_exception)

    def __call__(self, lecteur, lecture, item, tentative, consigne):
        self.appels.append((lecteur, lecture, item))
        return self.simule(lecteur, lecture, item, tentative, consigne)


def lancer(d, sortie, lectures, *extra, compteur=None):
    return lire.principal(args(d, sortie, lectures, *extra), appeler_simule=compteur or Compteur(), dormir=lambda s: None)


def manifeste(dossier: Path) -> dict:
    return json.loads((dossier / "manifeste-lecture-phase1-v4.json").read_text(encoding="utf-8"))


def lignes(chemin: Path) -> list:
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines() if x.strip()]


class _Corps(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


# ---------------------------------------------------------------------------------------------------------------
def test_format_des_reponses():
    bonne = "\n".join([f"STEP {n}: NO" for n in range(9)] + ['STEP 9: YES | WEAKENED | "on a single seed"'])
    assert lire.analyser_reponse("```\n" + bonne + "\n```")[9]["categorie"] == "WEAKENED"
    with pytest.raises(lire.FormatInvalide):
        lire.analyser_reponse(bonne + "\nVoici.")


def test_B2_reglages_geles_cas_sain_et_artefact(monkeypatch):
    g = lire.corps_gemini("c")["generationConfig"]
    assert g == {"temperature": 0, "maxOutputTokens": 8000, "thinkingConfig": {"thinkingBudget": 8192}}
    k = lire.corps_kimi("c")
    assert "temperature" not in k and k["max_tokens"] == 32000 and k["reasoning_effort"] == "high"
    vues = []

    def ouvrir(r):
        vues.append(json.loads(r.data))
        return _Corps(json.dumps({"model": "kimi-k3.1-pro", "usage": {"prompt_tokens": 1, "completion_tokens": 1},
                                  "choices": [{"finish_reason": "stop", "message": {"content": "x"}}]}).encode())

    lire.appeler_kimi("c", "http://127.0.0.1:8789", lire.Secrets(), ouvrir=ouvrir)  # cas sain : v2
    lire1.appeler_kimi("kimi-k3.1-pro", "c", 8000, "http://127.0.0.1:8789", ouvrir=ouvrir)  # artefact : v1
    assert "temperature" not in vues[0] and vues[0]["max_tokens"] == 32000
    assert vues[1]["temperature"] == 0 and vues[1]["max_tokens"] == 8000
    assert lire.LECTEURS["B"]["temperature_servie"] == 1.0 and lire.LECTEURS["A"]["temperature_servie"] == 0


def test_B2_temperatures_ecrites(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "f", "format") == 0
    m = manifeste(tmp_path / "f")
    assert m["lecteurs"]["B"]["temperature_envoyee"] is None and m["lecteurs"]["B"]["temperature_servie"] == 1.0
    j = lignes(tmp_path / "f" / "journal-phase1-B-v4.jsonl")
    assert j and all(x["temperature_servie"] == 1.0 and x["temperature_envoyee"] is None for x in j)


def test_B3_garde_reserve_la_pensee_cas_sain_et_artefact(entrees, tmp_path):
    consigne = "x" * 3000
    pire_a = lire.cout_pire_cas("A", consigne)
    assert pire_a == pytest.approx(1000 / 1e6 * 10 + (8000 + 8192) / 1e6 * 50)
    assert lire1.cout_pire_cas((10.0, 50.0), consigne, 8000) < pire_a  # la v1 ne réservait pas la pensée
    d, items, _ = entrees
    # Cas sain : sorties dans la réserve, lecture complète sous le plafond.
    assert lancer(d, tmp_path / "s", "format") == 0 and manifeste(tmp_path / "s")["depense_estimee_dollars"] <= 300
    # Artefact : la pensée dépasse son budget, ou la sortie dépasse la réserve : le lecteur s'arrête aussitôt.
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    for sorte, dossier in (("pensee", "p"), ("sortie", "o")):
        c = Compteur({("A", "format", it, 1): sorte for it in f})
        assert lancer(d, tmp_path / dossier, "format", compteur=c) == 4
        m = manifeste(tmp_path / dossier)
        assert "A" in m["lecteurs_arretes"] and m["controle_format"]["feu_vert"] is False
        assert sum(1 for x in c.appels if x[0] == "A") <= 2  # au plus les appels déjà partis (deux fils)


def test_B4_essai_de_format_seul_puis_feu_vert(entrees, tmp_path):
    d, _, _ = entrees
    c = Compteur()
    assert lancer(d, tmp_path / "f", "format", compteur=c) == 0
    assert {x[1] for x in c.appels} == {"format"}  # l'essai de format est lancé seul
    m = manifeste(tmp_path / "f")
    assert m["controle_format"]["feu_vert"] is True and m["controle_format"]["motifs"] == []
    sans = Compteur()
    with pytest.raises(lire.ArretLecture):  # artefact : lecture principale sans feu vert
        lancer(d, tmp_path / "p0", "principale+relecture", compteur=sans)
    assert sans.appels == [] and not (tmp_path / "p0").exists()
    avec = Compteur()  # cas sain : avec le manifeste au feu vert
    assert lancer(d, tmp_path / "p", "principale+relecture", "--feu-vert-format",
                  str(tmp_path / "f" / "manifeste-lecture-phase1-v4.json"), "--depense-engagee",
                  str(m["depense_estimee_dollars"]), compteur=avec) == 0
    assert {x[1] for x in avec.appels} == {"principale", "relecture"} and len(avec.appels) == 2 * (396 + 60)


def test_B4_feu_rouge_si_tronquee_ou_plafond(entrees, tmp_path):
    d, _, _ = entrees
    it = lignes(d / "formation.jsonl")[0]["item"]
    c = Compteur({("B", "format", it, 1): "tronquee", ("B", "format", it, 2): "tronquee"})
    assert lancer(d, tmp_path / "t", "format", compteur=c) == 6
    m = manifeste(tmp_path / "t")
    assert m["controle_format"]["feu_vert"] is False and any("tronquées" in x for x in m["controle_format"]["motifs"])
    with pytest.raises(lire.ArretLecture):
        lancer(d, tmp_path / "p", "principale+relecture", "--feu-vert-format",
               str(tmp_path / "t" / "manifeste-lecture-phase1-v4.json"))
    assert lancer(d, tmp_path / "b", "format", "--plafond-dollars", "2") in (3, 6)  # plafond trop bas : feu rouge
    assert manifeste(tmp_path / "b")["controle_format"]["feu_vert"] is False


def test_B5_rendu_controle_avant_tout_appel(entrees, tmp_path):
    d, items, _ = entrees
    faux = [dict(x) for x in items]
    faux[5]["type"] = "retirer"  # artefact : un champ de la clé glissé dans un item de la lecture principale
    e = tmp_path / "e"
    e.mkdir()
    (e / "items.jsonl").write_bytes(gen.en_jsonl(faux))
    for n in ("formation.jsonl", "relectures.txt"):
        (e / n).write_bytes((d / n).read_bytes())
    fautif = Compteur()
    assert lancer(e, tmp_path / "f", "format", compteur=fautif) == 2  # même l'essai de format rend les trois lectures
    assert fautif.appels == [] and manifeste(tmp_path / "f")["arret"].startswith("rendu")
    sain = Compteur()
    assert lancer(d, tmp_path / "ok", "format", compteur=sain) == 0 and sain.appels  # cas sain


def test_B5_rendu_fautif_aucun_appel_et_journal_garde(entrees, tmp_path):
    d, _, _ = entrees
    f = lignes(d / "formation.jsonl")
    f[3]["version"] = "jumeau"  # artefact dans les items de formation : refus au rendu, avant tout appel
    e = tmp_path / "e"
    e.mkdir()
    (e / "formation.jsonl").write_bytes(gen.en_jsonl(f))
    for n in ("items.jsonl", "relectures.txt"):
        (e / n).write_bytes((d / n).read_bytes())
    c = Compteur()
    assert lancer(e, tmp_path / "s", "format", compteur=c) == 2
    assert c.appels == []
    m = manifeste(tmp_path / "s")
    assert m["arret"].startswith("rendu") and (tmp_path / "s" / "journal-phase1-A-v4.jsonl").exists()


def test_B5_cle_refusee_arrete_tous_les_appels(entrees, tmp_path, monkeypatch):
    d, _, _ = entrees
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("A", "format", f[0], 1): "cle_refusee"})
    assert lancer(d, tmp_path / "k", "format", "--fils-par-lecteur", "1", compteur=c) == 5
    m = manifeste(tmp_path / "k")
    assert m["arret"].startswith("général")
    # après le refus, plus aucun appel ne part (au plus ceux déjà en vol : deux fils)
    rang_refus = c.appels.index(("A", "format", f[0]))
    assert len(c.appels) - rang_refus <= 2
    j = lignes(tmp_path / "k" / "journal-phase1-A-v4.jsonl")
    assert any(x["sorte"] == "cle_refusee_ou_absente" for x in j)  # journal gardé
    rb = lignes(tmp_path / "k" / "reponses-phase1-B-v4.jsonl")
    assert any(x["statut"] == "non_appele" for x in rb)  # l'autre lecteur s'arrête aussi
    # mode réel : variable absente, arrêt avant tout appel et avant toute sortie
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-07-05 | 2026-11-07 | décision |\n", encoding="utf-8")
    base = args(d, tmp_path / "r", "format")[1:]
    with pytest.raises(lire.ArretLecture):
        lire.principal(["--reel", *base, "--go", "GO-2026-11-07-05", "--registre-go", str(registre), "--commit", "x"])
    assert not (tmp_path / "r").exists()


def test_B6_masquage_avant_troncature_cas_sain_et_artefact(monkeypatch):
    monkeypatch.setenv("CLE_FACTICE", FAUX)

    def ouvrir_corps(corps):
        def ouvrir(requete):
            raise urllib.error.HTTPError(requete.full_url, 400, "x", {}, io.BytesIO(corps.encode()))
        return ouvrir

    corps = "x" * 280 + FAUX
    v1 = lire1.appeler_gemini("gemini-4-argon", "c", 8000, "CLE_FACTICE", None, ouvrir=ouvrir_corps(corps))
    assert FAUX[:20] in v1.echec  # artefact : la v1 écrivait le préfixe
    s = lire.Secrets()
    v2 = lire.appeler_gemini("c", "CLE_FACTICE", s, ouvrir=ouvrir_corps(corps))
    assert not any(FAUX[i:i + 6] in v2.echec for i in range(len(FAUX) - 5))
    v2b = lire.appeler_gemini("c", "CLE_FACTICE", s, ouvrir=ouvrir_corps("refus : " + FAUX[:12] + " (tronquée)"))
    assert FAUX[:12] not in v2b.echec and "[clé]" in v2b.echec
    sain = lire.appeler_gemini("c", "CLE_FACTICE", s, ouvrir=ouvrir_corps("quota dépassé"))
    assert sain.echec == "HTTP 400 : quota dépassé"  # cas sain : rien à masquer, rien de changé


def test_B6_aucun_fragment_de_cle_dans_les_sorties(entrees, tmp_path, monkeypatch, capsys):
    d, _, _ = entrees
    monkeypatch.setenv("GEMINI_API_KEY", FAUX)
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("A", "format", f[1], 1): "exception"}, message_exception=f"jeton {FAUX[3:30]} refusé")
    lancer(d, tmp_path / "s", "format", compteur=c)
    sortie = capsys.readouterr().out
    fenetres = {FAUX[i:i + 8] for i in range(len(FAUX) - 7)}
    for fichier in (tmp_path / "s").iterdir():
        texte = fichier.read_text(encoding="utf-8")
        assert not any(w in texte for w in fenetres), fichier.name
    assert not any(w in sortie for w in fenetres)
    j = lignes(tmp_path / "s" / "journal-phase1-A-v4.jsonl")
    assert any("[clé]" in (x.get("message") or "") for x in j)  # l'exception est écrite, masquée


def test_reprises_ecrites_et_determinisme(entrees, tmp_path):
    d, _, _ = entrees
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("A", "format", f[0], 1): "transport", ("B", "format", f[1], 1): "format",
                  ("B", "format", f[1], 2): "format"})
    assert lancer(d, tmp_path / "r", "format", compteur=c) == 6  # un item illisible : feu rouge
    rb = {x["item"]: x for x in lignes(tmp_path / "r" / "reponses-phase1-B-v4.jsonl")}
    ra = {x["item"]: x for x in lignes(tmp_path / "r" / "reponses-phase1-A-v4.jsonl")}
    assert ra[f[0]]["statut"] == "ok" and ra[f[0]]["tentatives"] == 2
    assert rb[f[1]]["statut"] == "illisible" and rb[f[1]]["tentatives"] == 2
    assert (tmp_path / "r" / "reponses-phase1-B-v4.encours.jsonl").exists()
    assert lancer(d, tmp_path / "a", "format") == 0 and lancer(d, tmp_path / "b", "format") == 0
    for k in ("A", "B"):
        assert (tmp_path / "a" / f"reponses-phase1-{k}-v4.jsonl").read_bytes() == \
               (tmp_path / "b" / f"reponses-phase1-{k}-v4.jsonl").read_bytes()


def test_depense_engagee_et_modele_servi(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "e", "format", "--plafond-dollars", "300", "--depense-engagee", "299.5") == 3
    assert manifeste(tmp_path / "e")["depense_estimee_dollars"] <= 300
    with pytest.raises(lire.ArretLecture):
        lancer(d, tmp_path / "x", "format", "--plafond-dollars", "300", "--depense-engagee", "300")
    f = [x["item"] for x in lignes(d / "formation.jsonl")]
    c = Compteur({("B", "format", it, 1): "modele" for it in f})
    assert lancer(d, tmp_path / "m", "format", compteur=c) == 4
    assert "B" in manifeste(tmp_path / "m")["lecteurs_arretes"]


# ---------------------------------------------------------------------------------------------------------------
# Contre-lecture du delta : D1, plafond accordé, R1 à R4
# ---------------------------------------------------------------------------------------------------------------
import subprocess  # noqa: E402

CLE_FORME = "AIzaSyFAUXfauxFAUXfauxFAUXfauxFAUXfaux"  # fausse clé à la forme d'une clé Google
FRAGMENTS = {CLE_FORME[i:i + 6] for i in range(len(CLE_FORME) - 5)}


def sans_fragment(texte: str) -> bool:
    return not any(f in texte for f in FRAGMENTS)


def test_D1_nom_de_variable_cas_sain_et_artefact(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "ok", "format", "--variable-cle-gemini", "GEMINI_API_KEY_2") == 0  # cas sain
    with pytest.raises(lire.ArretLecture) as e:  # artefact : la valeur passée comme nom
        lancer(d, tmp_path / "ko", "format", "--variable-cle-gemini", CLE_FORME)
    assert sans_fragment(str(e.value)) and not (tmp_path / "ko").exists()
    # la v2 écrivait cette valeur au manifeste en mode simulé
    lire2.principal(args(d, tmp_path / "v2", "format", "--variable-cle-gemini", CLE_FORME),
                    appeler_simule=lire2.FournisseurSimule(), dormir=lambda s: None)
    assert not sans_fragment((tmp_path / "v2" / "manifeste-lecture-phase1-v2.json").read_text(encoding="utf-8"))


def _main(version: str, argv: list) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", "-B", str(ICI / f"lire_items_phase1_{version}.py"), *argv],
                          capture_output=True, text=True, env={"PATH": "/usr/bin:/bin"}, timeout=120)


def test_D1_sortie_d_erreur_masquee_en_mode_reel(entrees, tmp_path):
    d, _, _ = entrees
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-07-05 | 2026-11-07 | décision |\n", encoding="utf-8")
    base = args(d, tmp_path / "r", "format")[1:] + ["--go", "GO-2026-11-07-05", "--registre-go", str(registre),
                                                     "--commit", "abcdef1", "--variable-cle-gemini", CLE_FORME]
    v3 = _main("v4", ["--reel", *base])
    assert v3.returncode == 2 and sans_fragment(v3.stderr + v3.stdout) and not (tmp_path / "r").exists()
    v2 = _main("v2", ["--reel", *base])  # artefact : la v2 recopiait la clé sur la sortie d'erreur
    assert not sans_fragment(v2.stderr + v2.stdout)
    # erreurs d'arguments : jamais recopiées, ni entre apostrophes ni comme arguments non reconnus
    for extra in (["--plafond-dollars", CLE_FORME], [CLE_FORME]):
        r = _main("v4", ["--simule", *args(d, tmp_path / "a", "format")[1:], *extra])
        assert r.returncode == 2 and sans_fragment(r.stderr + r.stdout) and "arguments refusés" in r.stderr


def test_D1_formes_des_autres_arguments(entrees, tmp_path):
    d, _, _ = entrees
    for extra in (["--commit", CLE_FORME], ["--relais-empreinte", CLE_FORME], ["--go", CLE_FORME],
                  ["--relais-kimi", "http://" + CLE_FORME + ".exemple"]):
        with pytest.raises(lire.ArretLecture) as e:
            lancer(d, tmp_path / "x", "format", *extra)
        assert sans_fragment(str(e.value))


def test_plafond_accorde_300_cas_sain_et_artefact(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "s", "format") == 0 and manifeste(tmp_path / "s")["plafond_dollars"] == 300
    with pytest.raises(lire.ArretLecture):
        lancer(d, tmp_path / "x", "format", "--plafond-dollars", "400")


def test_R1_second_lancement_controle_contre_l_essai_de_format(entrees, tmp_path):
    d, _, _ = entrees
    assert lancer(d, tmp_path / "f", "format") == 0
    fv = str(tmp_path / "f" / "manifeste-lecture-phase1-v4.json")
    depense = manifeste(tmp_path / "f")["depense_estimee_dollars"]
    with pytest.raises(lire.ArretLecture):  # artefact : autre plafond
        lancer(d, tmp_path / "p1", "principale+relecture", "--feu-vert-format", fv, "--plafond-dollars", "250",
               "--depense-engagee", str(depense))
    with pytest.raises(lire.ArretLecture):  # artefact : dépense de l'essai de format oubliée
        lancer(d, tmp_path / "p2", "principale+relecture", "--feu-vert-format", fv)
    assert lancer(d, tmp_path / "p3", "principale+relecture", "--feu-vert-format", fv, "--depense-engagee",
                  str(depense)) == 0  # cas sain


def test_R3_exception_hors_d_une_lecture(entrees, tmp_path):
    d, _, _ = entrees

    def fautif(lecteur, lecture, item, tentative, consigne):
        r = lire.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)
        r.jetons_entree = "x"  # jetons illisibles : l'erreur naît hors du bloc qui saisit les appels
        return r

    assert lire.principal(args(d, tmp_path / "e", "format"), appeler_simule=fautif, dormir=lambda s: None) == 7
    m = manifeste(tmp_path / "e")
    assert m["arret"].startswith("exception imprévue") and m["code_de_sortie"] == 7
    assert lancer(d, tmp_path / "s", "format") == 0  # cas sain


def test_R4_cle_invalide_en_400_et_402_du_relais(monkeypatch, entrees, tmp_path):
    monkeypatch.setenv("CLE_FACTICE", CLE_FORME)

    def ouvrir_erreur(code, corps):
        def ouvrir(requete):
            raise urllib.error.HTTPError(requete.full_url, code, "x", {}, io.BytesIO(corps.encode()))
        return ouvrir

    invalide = lire.appeler_gemini("c", "CLE_FACTICE", lire.Secrets(),
                                   ouvrir=ouvrir_erreur(400, '{"error": {"status": "INVALID_ARGUMENT", "details": '
                                                             '[{"reason": "API_KEY_INVALID"}]}}'))
    assert invalide.cle_refusee  # artefact de la v2 : 400 sans arrêt général
    assert not lire2.appeler_gemini("c", "CLE_FACTICE", lire2.Secrets(), ouvrir=ouvrir_erreur(
        400, '{"reason": "API_KEY_INVALID"}')).cle_refusee
    autre = lire.appeler_gemini("c", "CLE_FACTICE", lire.Secrets(), ouvrir=ouvrir_erreur(400, "requête mal formée"))
    assert not autre.cle_refusee  # cas sain : un autre 400 reste une erreur ordinaire
    k = lire.appeler_kimi("c", "http://127.0.0.1:8789", lire.Secrets(), ouvrir=ouvrir_erreur(402, "plafond"))
    assert k.detail.get("arret_lecteur")
    d, _, _ = entrees

    def relais_plein(lecteur, lecture, item, tentative, consigne):
        if lecteur == "B":
            return lire.Reponse(echec="HTTP 402 : plafond", detail={"arret_lecteur": "relais : plafond atteint (402)"})
        return lire.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)

    assert lire.principal(args(d, tmp_path / "k", "format"), appeler_simule=relais_plein, dormir=lambda s: None) == 4
    assert "B" in manifeste(tmp_path / "k")["lecteurs_arretes"]


def test_relais_max_appels_en_mode_reel(entrees, tmp_path, monkeypatch):
    d, _, _ = entrees
    monkeypatch.setenv("GEMINI_API_KEY", CLE_FORME)
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-07-05 | 2026-11-07 | décision |\n", encoding="utf-8")
    base = args(d, tmp_path / "r", "format")[1:] + ["--go", "GO-2026-11-07-05", "--registre-go", str(registre),
                                                     "--commit", "abcdef1"]
    for extra in ([], ["--relais-max-appels", "64"]):  # artefact : défaut du relais (64) ou rien
        with pytest.raises(lire.ArretLecture) as e:
            lire.principal(["--reel", *base, *extra])
        assert "au moins 100" in str(e.value) and not (tmp_path / "r").exists()


# ---------------------------------------------------------------------------------------------------------------
# Les 46 scénarios à fausse clé de la contre-lecture bornée du delta du brouillon 5, reconstitués d'après son rapport
# (section 1 et `resultats_pilote_d1_v3.txt`) : sorties standard et d'erreur et tout fichier écrit sont cherchés pour
# chacun des fragments de 6 caractères de la clé. Les six chemins qui fuyaient en v3 sont rejoués aussi contre la v3.
# ---------------------------------------------------------------------------------------------------------------
import urllib.request  # noqa: E402

CLE = "AI" + "zaSyFAUXcleZQXWVUTSRPOnmlkjhgfedcbaQW"  # 39 caractères, forme d'une clé Google, sans suite de chiffres
FRAG6 = {CLE[i:i + 6] for i in range(len(CLE) - 5)}


def propre(*textes) -> bool:
    return not any(f in x for x in textes for f in FRAG6)


def fichiers(dossier: Path) -> list:
    return [f.read_text(encoding="utf-8") for f in dossier.rglob("*") if f.is_file()] if dossier.exists() else []


def _registre(tmp_path):
    r = tmp_path / "go.md"
    r.write_text("| GO-2026-11-07-05 | 2026-11-07 | décision |\n", encoding="utf-8")
    return r


def _argv_reel(d, sortie, registre, *extra):
    return ["--reel", *args(d, sortie, "format")[1:], "--go", "GO-2026-11-07-05", "--registre-go", str(registre),
            "--commit", "abcdef1", "--relais-max-appels", "100", *extra]


def _sous_processus(version, argv, cle_dans_env=True):
    env = {"PATH": "/usr/bin:/bin"} | ({"GEMINI_API_KEY": CLE} if cle_dans_env else {})
    return subprocess.run([sys.executable, "-I", "-B", str(ICI / f"lire_items_phase1_{version}.py"), *argv],
                          capture_output=True, text=True, env=env, timeout=120)


SIX = {  # les six chemins exacts du rapport : (mode, arguments ajoutés, clé posée dans l'environnement)
    "ambigu_re_reel": ("reel", [f"--re={CLE}"], True),
    "ambigu_relais_reel": ("reel", [f"--relais={CLE}"], True),
    "ambigu_re_simule": ("simule", [f"--re={CLE}"], False),
    "ambigu_relais_simule": ("simule", [f"--relais={CLE}"], False),
    "chemin_items_simule_sans_cle": ("simule", ["--items", CLE], False),
    "chemin_registre_go_reel": ("reel", ["--registre-go", CLE], True),
}


@pytest.mark.parametrize("nom", sorted(SIX))
def test_six_chemins_fermes_en_v4_et_ouverts_en_v3(nom, entrees, tmp_path):
    d, _, _ = entrees
    mode, extra, env = SIX[nom]
    registre = _registre(tmp_path)
    for version, sortie in (("v4", tmp_path / "s4"), ("v3", tmp_path / "s3")):
        if mode == "reel":
            argv = _argv_reel(d, sortie, registre, *extra)
        else:
            argv = ["--simule", *args(d, sortie, "format")[1:], *extra]
        if "--items" in extra:  # la clé remplace le chemin des items
            i = argv.index("--items")
            argv = argv[:i] + argv[i + 2:] + []
        if "--registre-go" in extra:
            i = argv.index("--registre-go")
            argv = argv[:i] + argv[i + 2:]
        argv = argv + extra if ("--items" in extra or "--registre-go" in extra) else argv
        r = _sous_processus(version, argv, env)
        textes = [r.stdout, r.stderr, *fichiers(sortie)]
        if version == "v4":
            assert r.returncode == 2 and propre(*textes), (nom, r.stderr)
            assert not sortie.exists()
        else:
            assert not propre(*textes), nom  # artefact : la v3 écrivait la clé entière sur la sortie d'erreur


ARGUMENTS = {  # erreurs d'arguments et formes (21 scénarios du rapport, dans les deux modes), noms de variable (5)
    "plafond": ["--plafond-dollars", CLE], "positionnel": [CLE], "entropie": ["--entropie", CLE],
    "lectures_choix": ["--lectures", CLE], "max_appels": ["--relais-max-appels", CLE],
    "forme_commit": ["--commit", CLE], "forme_go": ["--go", CLE], "forme_empreinte": ["--relais-empreinte", CLE],
    "forme_kimi": ["--relais-kimi", f"http://{CLE}:1"], "reel_egal": [f"--reel={CLE}"], "simule_egal": [f"--simule={CLE}"],
    "separateur": ["--", CLE], "variable_valeur": ["--variable-cle-gemini", CLE],
    "variable_egal": [f"--variable-cle-gemini={CLE}"], "variable_abregee": [f"--variable={CLE}"],
    "variable_minuscules": ["--variable-cle-gemini", "gemini_api_key"], "fils_4": ["--fils-par-lecteur", "4"],
    "chemin_formation": ["--formation", CLE], "chemin_question": ["--question", CLE],
    "chemin_relectures": ["--relectures", CLE], "sortie_existante": [],
}


@pytest.mark.parametrize("mode", ["reel", "simule"])
@pytest.mark.parametrize("nom", sorted(ARGUMENTS))
def test_arguments_jamais_recopies(nom, mode, entrees, tmp_path):
    d, _, _ = entrees
    sortie = tmp_path / "s"
    extra = ARGUMENTS[nom]
    if nom == "sortie_existante":
        sortie = tmp_path / CLE
        sortie.mkdir()
    base = _argv_reel(d, sortie, _registre(tmp_path)) if mode == "reel" else ["--simule", *args(d, sortie, "format")[1:]]
    for opt in ("--formation", "--question", "--relectures", "--lectures", "--entropie", "--commit", "--go",
                "--relais-max-appels"):
        if opt in extra and opt in base:  # la valeur fautive remplace la valeur saine
            i = base.index(opt)
            base = base[:i] + base[i + 2:]
    r = _sous_processus("v4", [*base, *extra], cle_dans_env=(mode == "reel"))
    assert r.returncode == 2, (nom, mode, r.stderr)
    assert propre(r.stdout, r.stderr, *(fichiers(sortie) if nom != "sortie_existante" else [])), (nom, mode, r.stderr)


# Chemins du fournisseur, en mode réel sans réseau (fausses ouvertures) : clé posée dans l'environnement.
class _Corps(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _gemini_ok(texte="", modele="gemini-4-argon", jetons=10):
    return {"modelVersion": modele, "usageMetadata": {"promptTokenCount": jetons, "candidatesTokenCount": 5},
            "candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": texte}]}}]}


REPONSE = "\n".join(f"STEP {n}: NO" for n in range(10))
FOURNISSEUR = {
    "503_cle_a_297": lambda r: (_ for _ in ()).throw(urllib.error.HTTPError(r.full_url, 503, "x", {}, io.BytesIO(("x" * 297 + CLE).encode()))),
    "400_cle_fragmentee": lambda r: (_ for _ in ()).throw(urllib.error.HTTPError(r.full_url, 400, "x", {}, io.BytesIO(
        (CLE[:6] + " " + CLE[:7] + " " + CLE[:20] + " " + CLE[:15] + "\n" + CLE[15:] + " " + "y" * 270 + CLE).encode()))),
    "401_cle": lambda r: (_ for _ in ()).throw(urllib.error.HTTPError(r.full_url, 401, "x", {}, io.BytesIO(("refus " + CLE).encode()))),
    "oserror_cle": lambda r: (_ for _ in ()).throw(OSError("connexion coupée " + CLE)),
    "exception_cle": lambda r: (_ for _ in ()).throw(RuntimeError("z" * 296 + CLE)),
    "modele_cle": lambda r: _Corps(json.dumps(_gemini_ok(REPONSE, modele=CLE)).encode()),
    "texte_cle": lambda r: _Corps(json.dumps(_gemini_ok("réponse " + CLE)).encode()),
    "jetons_cle": lambda r: _Corps(json.dumps(_gemini_ok(REPONSE, jetons=CLE)).encode()),
    "400_invalide_cle": lambda r: (_ for _ in ()).throw(urllib.error.HTTPError(r.full_url, 400, "x", {}, io.BytesIO(
        ('{"reason": "API_KEY_INVALID", "cle": "' + CLE + '"}').encode()))),
}


class _OuvreurKimi:
    def open(self, requete, timeout=None):
        return _Corps(json.dumps({"model": "kimi-k3.1-pro", "usage": {"prompt_tokens": 10, "completion_tokens": 5},
                                  "choices": [{"finish_reason": "stop", "message": {"content": REPONSE}}]}).encode())


@pytest.mark.parametrize("nom", sorted(FOURNISSEUR))
def test_chemins_du_fournisseur_en_mode_reel(nom, entrees, tmp_path, monkeypatch, capsys):
    d, _, _ = entrees
    monkeypatch.setenv("GEMINI_API_KEY", CLE)
    monkeypatch.setattr(urllib.request, "urlopen", lambda r, context=None, timeout=None: FOURNISSEUR[nom](r))
    monkeypatch.setattr(urllib.request, "build_opener", lambda *h: _OuvreurKimi())
    monkeypatch.setattr(lire.time, "sleep", lambda s: None)
    sortie = tmp_path / "s"
    code = lire.principal(_argv_reel(d, sortie, _registre(tmp_path)), dormir=lambda s: None)
    out = capsys.readouterr()
    assert code in (4, 5, 6, 7) and propre(out.out, out.err, *fichiers(sortie)), (nom, code)


def test_CD5_11_reserve_d_une_tentative_interrompue_comptee(entrees, tmp_path):
    d, _, _ = entrees

    def fautif(lecteur, lecture, item, tentative, consigne):
        r = lire.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)
        if lecteur == "A":
            r.jetons_entree = "x"  # exception après l'appel, hors du bloc qui saisit les appels
        return r

    for module, dossier in ((lire3, tmp_path / "v3"), (lire, tmp_path / "v4")):
        assert module.principal(args(d, dossier, "format"), appeler_simule=fautif, dormir=lambda s: None) == 7
    m3 = json.loads((tmp_path / "v3" / "manifeste-lecture-phase1-v3.json").read_text(encoding="utf-8"))
    m4 = manifeste(tmp_path / "v4")
    consignes = lire.rendre_tout({"format": lignes(d / "formation.jsonl")}, lire.ph.extraire_question(QUESTION))
    pire_a = sum(lire.cout_pire_cas("A", c) for c in consignes.values())
    assert m3["depense_estimee_dollars"] < pire_a  # artefact : la v3 sous-comptait (seul Kimi était compté)
    assert m4["depense_estimee_dollars"] >= pire_a and m4["tentatives_interrompues_comptees_au_pire"] == 20
    assert m4["reserve_restante_dollars"] == 0
