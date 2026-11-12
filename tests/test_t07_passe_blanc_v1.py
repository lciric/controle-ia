"""Essais R5 de la passe à blanc de l'extracteur de T0.7 (`src/controle_ia/t07/passe_blanc_v1.py`, sous-commande `passe-blanc` de
`lecture_v2`) : chaque garde (frontière « avant le champ », gabarit, mémoire de l'hôte, mémoire de la carte, extraction de
l'échantillon, refus avant calcul) a un cas sain et au moins un artefact, sur le modèle jouet du harnais (tokeniseur par caractères,
aucun téléchargement) et les jeux factices de `test_t07_sondes_neuves_v1.py` ; la passe n'écrit rien hors de son dossier."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste
from controle_ia.scellement import verifier
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import passe_blanc_v1 as pb
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07 import sondes_neuves_v1 as sn
from test_t07_lecture_v1 import RUN_T06, _sans_ligne, construire_run
from test_t07_sondes_neuves_v1 import construire_complet, enregistrements, poser_jeux

COUCHES_JOUET = [1, 2]
RUN_MODELE = "20261108-130000-t06-jouet"
INSTANT_PB = 1_800_000_000
GIO = 2**30


def extracteur_jouet(classe=sn.Extracteur):
    from controle_ia.environnements.lancer_pilote_a import charger_modele_et_format
    modele, fmt = charger_modele_et_format({}, "jouet", 11)
    return classe(modele, fmt, COUCHES_JOUET)


def memoire(disponible=64 * GIO, carte=None):
    return lambda: {"hote": {"disponible": disponible, "totale": 128 * GIO, "residente": GIO, "pic_resident": GIO}, "carte": carte}


@pytest.fixture
def jb(depot):
    j = construire_complet(depot)
    j.config["couches"] = list(COUCHES_JOUET)
    return j


def _pb(j, **kw):
    kw.setdefault("instant", INSTANT_PB)
    kw.setdefault("extracteur", extracteur_jouet())
    kw.setdefault("mesure", memoire())
    config = kw.pop("config", j.config)
    return pb.passe_a_blanc(j.racine, j.registre, config, RUN_T06, **kw)


def _arbre(racine: Path) -> dict:
    return {str(p.relative_to(racine)): p.stat().st_mtime_ns for p in racine.rglob("*")
            if p.is_file() and ".git" not in p.parts and pb.DOSSIER not in p.parts}


# ------------------------------------------------------------------------------------------------------------------ cas sain
def test_passe_tenue_sur_le_modele_jouet_et_rien_d_ecrit_hors_de_son_dossier(jb):
    """Cas sain : frontière exacte sur tous les enregistrements de J-C et J-A, gabarit conforme partout, échantillon fixe extrait,
    mémoire jugée (carte : sans objet en jouet) ; sortie scellée sous `passes-blanches-t07/`, nom distinct de toute sortie de
    l'étape A ; aucun fichier créé ni modifié ailleurs (registre, journal des ouvertures, runs, diag, donnees)."""
    avant = _arbre(jb.racine)
    r = _pb(jb)
    assert r["issue"] == "tenue" and r["motifs"] == []
    s = r["sortie"]
    assert s["frontiere"]["tient"] and s["gabarit"]["tient"] and s["memoire"]["tient"]
    for n in ("JC", "JA"):
        f = s["frontiere"]["par_jeu"][n]
        assert f["enregistrements"] == 20 and f["exactes"] == 20 and f["ajustees"] == 0 and f["fautes"] == 0
    assert "JD" not in s["frontiere"]["par_jeu"]
    assert [x["indice"] for x in s["echantillon"]["pris"]["JD"]][:4] == [0, 1, 2, 3]
    assert len(s["echantillon"]["pris"]["phrases"]) == 2 * 2 * pb.PAIRES_PAR_CONCEPT      # la plus longue y est déjà
    assert s["durees"]["passes_etape_a"] == 20 + 2 * 20 + 20 + 12 and s["durees"]["extraction_etape_a_estimee_s"] > 0
    assert s["memoire"]["jugement"]["carte_jugee"].startswith("sans objet")
    assert s["memoire"]["jugement"]["activations_etape_a_octets"] == 4 * 2 * 32 * s["durees"]["jetons_etape_a"]
    chemin = jb.racine / r["chemin"]
    assert verifier(chemin) == r["sha256"]
    assert r["chemin"].startswith(pb.DOSSIER + "/") and chemin.name == pb.FICHIER
    assert not set(Path(r["chemin"]).parts) & {"runs", "diag", "donnees"}
    assert pb.FICHIER not in {lv1.FICHIER_SONDES, lv1.FICHIER_SCORES} and "passe-blanc" in chemin.parent.name
    assert _arbre(jb.racine) == avant
    assert not jb.journal.exists() or not any("OUVERTURE-T07" in l or "REFUS-T07" in l for l in jb.lignes_journal())
    assert not rg.cle_presente(jb.registre, rg.SCORES_T07) and not rg.cle_presente(jb.registre, rg.SONDES_T07)


def test_echantillon_fixe_et_ecrit():
    """Les deux premières paires dans l'ordre du fichier, plus l'enregistrement le plus long (le premier en cas d'égalité)."""
    recs = enregistrements("dissimulation")
    assert pb.echantillon_jeu(recs, [5] * len(recs)) == [0, 1, 2, 3]
    longueurs = [5] * len(recs)
    longueurs[13] = longueurs[17] = 9
    assert pb.echantillon_jeu(recs, longueurs) == [0, 1, 2, 3, 13]


# ---------------------------------------------------------------------------------------------------------------- frontière
def test_frontiere_artefact_reel_blancs_de_tete(depot):
    """Artefact réel : une réponse de J-C commençant par un blanc (acceptée par `lire_jeu`, le champ étant à `position_cost`) fait
    entrer la frontière de l'étape A dans le champ `COST:` (préfixe non commun, frontière ajustée sur la réponse brute) : arrêt
    motivé, F2, sortie scellée, frontière « ne tient pas »."""
    jc = enregistrements("domaine-cout")
    jc[5] = {**jc[5], "reponse": " " + jc[5]["reponse"], "position_cost": jc[5]["position_cost"] + 1}
    jb = construire_run(depot)                               # comme `construire_complet`, avec ce J-C (R12 : un seul scellement)
    jb.config.update(garde_adaptee=True, portee_regle_4="restreinte", jetons_entrainement=None, couches=list(COUCHES_JOUET),
                     sondes_par_concept={**jb.config["sondes_par_concept"], "dissimulation": None, "domaine": None})
    poser_jeux(jb, {rg.SCELLEMENT_JEUX_JD: enregistrements("dissimulation"), rg.SCELLEMENT_JEUX_JC: jc,
                    rg.SCELLEMENT_JEUX_JA: enregistrements("intention-autres-modes")})
    r = _pb(jb)
    s = r["sortie"]
    assert r["issue"] == "arrêt" and not s["frontiere"]["tient"] and s["gabarit"]["tient"]
    assert s["frontiere"]["par_jeu"]["JC"]["fautes"] == 1 and s["frontiere"]["par_jeu"]["JC"]["ajustees"] == 1
    assert s["frontiere"]["fautes"][0]["indice"] == 5 and s["frontiere"]["fautes"][0]["faute"].startswith("F2")
    assert any("jeu JC" in m for m in r["motifs"]) and verifier(jb.racine / r["chemin"]) == r["sha256"]


@pytest.mark.parametrize("decalage,regle", [(-1, "F3"), (1, "F2"), (None, "F1")])
def test_frontiere_artefacts_decales(jb, decalage, regle):
    """Artefacts : une frontière non maximale (k − 1), entrée dans le champ (k + 1) ou vide (0) est refusée par F3, F2, F1."""
    class Decale(sn.Extracteur):
        def frontiere(self, reponse, position_cost):
            k = super().frontiere(reponse, position_cost)
            return 0 if decalage is None else k + decalage
    r = _pb(jb, extracteur=extracteur_jouet(Decale))
    assert r["issue"] == "arrêt" and not r["sortie"]["frontiere"]["tient"]
    assert {f["faute"][:2] for f in r["sortie"]["frontiere"]["fautes"]} == {regle}


def test_gabarit_artefact(jb, monkeypatch):
    """Artefact : la garde du gabarit de l'étape A (identifiants = rendu complet) refuse deux enregistrements par jeu : arrêt
    motivé, faute « gabarit » comptée à part de la frontière."""
    vrai = pb.jetons_reponse_forcee

    def faux(fmt, consigne, utilisateur, reponse, retrait):
        if "plan r01 1 " in reponse:
            raise GardeArret("réponse imposée : identifiants ≠ rendu complet du gabarit")
        return vrai(fmt, consigne, utilisateur, reponse, retrait)
    monkeypatch.setattr(pb, "jetons_reponse_forcee", faux)
    r = _pb(jb)
    s = r["sortie"]
    assert r["issue"] == "arrêt" and not s["gabarit"]["tient"] and s["frontiere"]["tient"]
    assert all(v["fautes"] == 2 for v in s["gabarit"]["par_jeu"].values())


def test_extraction_artefact(jb):
    """Artefact : une passe de l'échantillon en arrêt (empan vide, activations non finies…) : arrêt motivé, motif écrit."""
    class Panne(sn.Extracteur):
        def reponse(self, contexte, observation, reponse, empan, position_cost=None):
            if empan == "action_entiere":
                raise GardeArret("empan de 3 jetons hors des activations ou non fini (couche 1)")
            return super().reponse(contexte, observation, reponse, empan, position_cost)
    r = _pb(jb, extracteur=extracteur_jouet(Panne))
    assert r["issue"] == "arrêt" and any("extraction de l'échantillon, jeu JC" in m for m in r["motifs"])
    assert r["sortie"]["frontiere"]["tient"]


# ------------------------------------------------------------------------------------------------------------------ mémoire
def test_memoire_hote_cas_sain_et_artefact(jb):
    """Cas sain : besoin (activations de l'étape A × facteur de copies) sous la part maximale du disponible ; artefact : 1 Mio
    disponible → arrêt motivé « mémoire de l'hôte »."""
    assert _pb(jb, mesure=memoire(disponible=64 * GIO))["issue"] == "tenue"
    r = _pb(jb, mesure=memoire(disponible=2**20), instant=INSTANT_PB + 1)
    assert r["issue"] == "arrêt" and not r["sortie"]["memoire"]["tient"]
    assert any(m.startswith("mémoire de l'hôte") for m in r["motifs"]) and r["sortie"]["frontiere"]["tient"]


def test_memoire_carte_cas_sain_et_artefact(jb):
    """Cas sain : pic réservé à la moitié de la carte ; artefact : pic réservé à 95 % → arrêt motivé « mémoire de la carte »."""
    sain = {"pic_alloue": 30 * GIO, "pic_reserve": 40 * GIO, "totale": 80 * GIO, "nom": "jouet"}
    r = _pb(jb, mesure=memoire(carte=sain))
    assert r["issue"] == "tenue" and "carte_jugee" not in r["sortie"]["memoire"]["jugement"]
    plein = {**sain, "pic_reserve": 76 * GIO}
    r = _pb(jb, mesure=memoire(carte=plein), instant=INSTANT_PB + 1)
    assert r["issue"] == "arrêt" and any(m.startswith("mémoire de la carte") for m in r["motifs"])


def test_memoire_illisible_ou_sans_carte_en_reel():
    """Aucun repli silencieux : mémoire de l'hôte illisible → motif ; mode réel sans carte → motif ; carte illisible → motif ;
    jouet sans carte → jugée « sans objet » (cas sain)."""
    h = {"disponible": 64 * GIO}
    assert pb._juger_memoire({"hote": {"disponible": None}, "carte": None}, 10, "jouet")[1].startswith("mémoire de l'hôte illisible")
    assert pb._juger_memoire({"hote": h, "carte": None}, 10, "reel")[1].startswith("mode réel sans carte")
    assert pb._juger_memoire({"hote": h, "carte": {"illisible": "RuntimeError: x"}}, 10, "reel")[1].startswith("mémoire de la carte illisible")
    j, motif = pb._juger_memoire({"hote": h, "carte": None}, 10, "jouet")
    assert motif is None and j["besoin_hote_octets"] == 20


def test_sonde_memoire_reelle_lisible():
    """La sonde de mémoire lit l'hôte (Linux) ; sans carte, `carte` vaut None."""
    m = pb.sonde_memoire()
    assert m["hote"]["disponible"] > 0 and m["hote"]["residente"] > 0


# ----------------------------------------------------------------------------------------------------------- refus, R12, CLI
def test_refus_avant_calcul_sans_rien_ecrire(jb):
    """Refus (code 2), rien d'écrit : aucun jeu ni phrase au registre ; sceau faux d'un jeu ; dossier de sortie déjà présent (R12) ;
    configuration non conforme. Cas sain : la même passe, entrées remises, est tenue."""
    for cle in (rg.SCELLEMENT_JEUX_JD, rg.SCELLEMENT_JEUX_JC, rg.SCELLEMENT_JEUX_JA, rg.SCELLEMENT_CONCEPTS_T07):
        _sans_ligne(jb, cle)
    with pytest.raises(pb.RefusPasse, match="rien à éprouver"):
        _pb(jb)
    poser_jeux(jb)
    jeu = jb.racine / "prereg/jeux-v3/scellement-jeux-t07-jd.jsonl"
    texte = jeu.read_text(encoding="utf-8")
    jeu.write_text(texte + "\n", encoding="utf-8")
    with pytest.raises(pb.RefusPasse, match="sceau"):
        _pb(jb)
    jeu.write_text(texte, encoding="utf-8")
    assert not (jb.racine / pb.DOSSIER).exists()
    assert _pb(jb)["issue"] == "tenue"
    with pytest.raises(pb.RefusPasse, match="R12"):
        _pb(jb)
    with pytest.raises(pb.RefusPasse, match="configuration"):
        _pb(jb, config={**jb.config, "entropie": None}, instant=INSTANT_PB + 5)


def test_sous_commande_de_lecture_v2(jb, capsys):
    """`lecture_v2 passe-blanc` charge le modèle de la course par `extracteur_de_la_course` (manifeste de T0.6 : agent, mode,
    graine « modele-jouet ») : code 0 et sortie scellée ; artefacts : run de T0.6 sans manifeste lisible → code 2, rien d'écrit ;
    mesure de la mémoire réelle de l'hôte."""
    creer_manifeste(jb.racine, RUN_MODELE, {"mode": "jouet", "agent": {}}, ["modele-jouet"], entropie=7, autoriser_depot_sale=True)
    (jb.racine / "donnees" / RUN_MODELE).mkdir(parents=True)                # DF-04 : la passe lit les jetons notés de la course
    for nom in ("mesures-t06.npz", "mesures-t06.npz.sha256"):
        shutil.copy(jb.racine / "donnees" / RUN_T06 / nom, jb.racine / "donnees" / RUN_MODELE / nom)
    cfg = jb.racine / "config-t07-passe.json"
    cfg.write_text(json.dumps(jb.config, ensure_ascii=False), encoding="utf-8")
    code = lv.main(["passe-blanc", str(jb.racine), "20261108-140000-t06-jouet", str(cfg), "--registre", str(jb.registre)])
    assert code == pb.CODE_REFUS and not (jb.racine / pb.DOSSIER).exists()
    assert "REFUS (passe à blanc, rien d'écrit)" in capsys.readouterr().err
    code = lv.main(["passe-blanc", str(jb.racine), RUN_MODELE, str(cfg), "--registre", str(jb.registre)])
    out = capsys.readouterr().out
    assert code == pb.CODE_OK and "passe à blanc : tenue" in out
    chemin = jb.racine / out.split("sortie ", 1)[1].split()[0]
    assert verifier(chemin) == out.split("sortie ", 1)[1].split()[1]
    s = json.loads(chemin.read_text(encoding="utf-8"))
    assert s["run_t06"] == RUN_MODELE and s["memoire"]["jugement"]["hote"]["disponible"] > 0 and s["nature"] == pb.NATURE


# ------------------------------------------------------------------------------------- DF-04 (contre-lecture différentielle)
def test_DF04_memoire_de_la_notation(jb, monkeypatch):
    """DF-04 : la passe juge aussi la mémoire de la notation (une couche, toutes les actions notées, float32, jetons notés lus dans
    `mesures-t06.npz`). Cas sain : besoin écrit, tenue ; artefacts : notation de 40 Gio pour 64 Gio disponibles (jeux tenus) →
    arrêt « mémoire de la notation » ; mesures absentes → arrêt « non estimable » (aucun repli silencieux)."""
    r = _pb(jb)
    j = r["sortie"]["memoire"]["jugement"]
    n = j["notation"]
    assert r["issue"] == "tenue" and n["octets"] == 4 * 32 * n["jetons_notes"] and j["besoin_notation_octets"] == 2 * n["octets"]
    monkeypatch.setattr(pb, "octets_notation", lambda *a: {"actions_notees": 1, "jetons_notes": 1, "octets": 40 * GIO})
    r = _pb(jb, instant=INSTANT_PB + 1)
    assert r["issue"] == "arrêt" and any(m.startswith("mémoire de la notation") for m in r["motifs"]) and r["sortie"]["frontiere"]["tient"]
    monkeypatch.undo()
    (jb.racine / "donnees" / RUN_T06 / "mesures-t06.npz").rename(jb.racine / "donnees" / RUN_T06 / "mesures-t06.npz.ailleurs")
    r = _pb(jb, instant=INSTANT_PB + 2)
    assert r["issue"] == "arrêt" and any("non estimable" in m for m in r["motifs"]) and not r["sortie"]["memoire"]["tient"]
