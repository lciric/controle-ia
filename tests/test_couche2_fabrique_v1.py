"""Journal de fabrique, ordre scellé, palier de rythme (couche 2, v1) : chaque garde sur un cas sain et un artefact (R5)."""
import json
from datetime import datetime, timedelta, timezone

import numpy as np
import pytest

from controle_ia.couche2 import fabrique_v1 as fb
from controle_ia.gardes import GardeArret
from controle_ia.scellement import compagnon

TACHES = [f"t{i:02d}" for i in range(4)]
POSTES = ("generation", "juge_8b", "trace_lite")
SORTIE = "a" * 64


class Horloge:
    def __init__(self):
        self.t = datetime(2026, 10, 29, 10, 0, tzinfo=timezone.utc)

    def __call__(self):
        self.t += timedelta(seconds=1)
        return self.t.isoformat(timespec="microseconds")


def blocs():
    return [fb.bloc("palier", "D", TACHES, range(1)), fb.bloc("reste", "D", TACHES, range(1, 3))]


def palier(regle="chaque_episode", seuil=189.0, lecture="generation_comprise", n=4):
    return fb.PalierRythme(seuil_s=seuil, lecture=lecture, regle=regle, n_episodes=n, postes=POSTES)


def secondes(total_moniteurs=100.0, generation=50.0):
    return {"generation": generation, "juge_8b": total_moniteurs / 2, "trace_lite": total_moniteurs / 2}


def ouvrir(tmp_path, pal=None, entropie=12345):
    chemin_ordre = tmp_path / "ordre.json"
    fb.ecrire_ordre(chemin_ordre, fb.tirer_ordre(blocs(), entropie))
    j = fb.JournalFabrique.creer(tmp_path / "journal.jsonl", chemin_ordre, pal or palier(), instance="i-1",
                                 run_id="20261029-100000-t0", horloge=Horloge())
    return j


def jouer(j, n, sec=None):
    for _ in range(n):
        r = j.prochain_rang
        el, rng = j.debut(r)
        j.fin(r, secondes=sec or secondes(), version="v1", cache="froid", empreinte_sortie=SORTIE)


def reecrire(chemin, lignes):
    chemin.write_text("".join(json.dumps(l, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
                              for l in lignes), encoding="utf-8")


def rechainer(dicos):
    """Recalcule numéros, chaîne et empreintes : un faussaire soigneux (pour isoler les gardes sémantiques)."""
    prec, sortie = fb.ZERO, []
    for i, d in enumerate(dicos):
        texte, emp = fb._ligne(i, d["type"], d["horodatage"], prec, d["contenu"])
        sortie.append(json.loads(texte))
        prec = emp
    return sortie, prec


# ---------------------------------------------------------------- ordre

def test_ordre_deterministe_par_blocs_et_graines_distinctes():
    a, b = fb.tirer_ordre(blocs(), 7), fb.tirer_ordre(blocs(), 7)
    assert a == b and fb.empreinte_ordre(a) == fb.empreinte_ordre(b)
    assert [e["bloc"] for e in a["elements"]] == ["palier"] * 4 + ["reste"] * 8
    assert sorted(e["tache"] for e in a["elements"][:4]) == TACHES  # un épisode par tâche au palier
    assert [e["rang"] for e in a["elements"]] == list(range(12))
    etats = {tuple(e["graine"]["etat_controle"]) for e in a["elements"]}
    assert len(etats) == 12
    c = fb.tirer_ordre(blocs(), 8)
    assert [e["tache"] for e in c["elements"]] != [e["tache"] for e in a["elements"]] or \
        c["elements"][0]["graine"] != a["elements"][0]["graine"]


def test_graine_depend_du_lot():
    assert fb.graine_episode(1, "C", "t", 0) != fb.graine_episode(1, "D", "t", 0)


def test_ordre_entropie_neuve_consignee():
    o = fb.tirer_ordre(blocs(), None)
    assert fb.exiger_ordre_retire(o) == fb.empreinte_ordre(o)


def test_artefact_ordre_doublon_et_bloc_vide():
    with pytest.raises(GardeArret, match="double"):
        fb.tirer_ordre([fb.bloc("a", "D", ["t"], [0]), fb.bloc("b", "D", ["t"], [0])], 1)
    with pytest.raises(GardeArret, match="vide"):
        fb.tirer_ordre([fb.bloc("a", "D", [], [0])], 1)


def test_ordre_sain_puis_artefact_retouche(tmp_path):
    chemin = tmp_path / "ordre.json"
    sha = fb.ecrire_ordre(chemin, fb.tirer_ordre(blocs(), 3))
    ordre, sha2 = fb.charger_ordre(chemin)
    assert sha == sha2
    # retouché à la main, puis rescellé : le sceau passe, le retirage refuse
    o = json.loads(chemin.read_text())
    o["elements"][0], o["elements"][1] = o["elements"][1], o["elements"][0]
    chemin2 = tmp_path / "ordre2.json"
    chemin2.write_text(json.dumps(o) + "\n")
    from controle_ia.scellement import sceller
    sceller(chemin2)
    with pytest.raises(GardeArret, match="retouché"):
        fb.charger_ordre(chemin2)


def test_artefact_ordre_ecrase_et_sceau_casse(tmp_path):
    chemin = tmp_path / "ordre.json"
    fb.ecrire_ordre(chemin, fb.tirer_ordre(blocs(), 3))
    with pytest.raises(GardeArret, match="R12"):
        fb.ecrire_ordre(chemin, fb.tirer_ordre(blocs(), 4))
    chemin.write_text(chemin.read_text().replace('"t00"', '"t09"', 1))
    with pytest.raises(GardeArret, match="empreinte"):
        fb.charger_ordre(chemin)


# ---------------------------------------------------------------- palier (objet)

def test_palier_p23_p28_valeurs_sourcees_et_regle_obligatoire():
    p = fb.palier_p23_p28(regle="moyenne_du_palier", postes=POSTES)
    assert (p.seuil_s, p.n_episodes, p.lecture) == (189.0, 16, "generation_comprise")
    with pytest.raises(TypeError):
        fb.palier_p23_p28(postes=POSTES)  # règle sans défaut
    with pytest.raises(TypeError):
        fb.PalierRythme(seuil_s=189.0, lecture="generation_comprise", regle="chaque_episode", postes=POSTES)


@pytest.mark.parametrize("champ,valeur,motif", [
    ("seuil_s", float("nan"), "seuil"), ("seuil_s", -1.0, "seuil"), ("lecture", "tout", "lecture"),
    ("regle", "mediane", "règle"), ("n_episodes", 0, "taille"), ("postes", ("juge_8b", "x"), "generation"),
    ("postes", ("generation",), "moniteur"), ("postes", ("generation", "x", "x"), "double")])
def test_artefact_palier_mal_forme(champ, valeur, motif):
    args = dict(seuil_s=189.0, lecture="generation_comprise", regle="chaque_episode", n_episodes=4, postes=POSTES)
    args[champ] = valeur
    with pytest.raises(GardeArret, match=motif):
        fb.PalierRythme(**args)


def test_palier_lectures():
    s = secondes(total_moniteurs=150.0, generation=50.0)
    assert palier(lecture="generation_comprise").rythme(s) == 200.0
    assert palier(lecture="moniteurs_seuls").rythme(s) == 150.0


@pytest.mark.parametrize("sec,motif", [
    ({"generation": 1.0, "juge_8b": 1.0}, "manquants"),
    ({"generation": 1.0, "juge_8b": 1.0, "trace_lite": 1.0, "qwen": 1.0}, "inattendus"),
    ({"generation": float("nan"), "juge_8b": 1.0, "trace_lite": 1.0}, "invalide"),
    ({"generation": -0.1, "juge_8b": 1.0, "trace_lite": 1.0}, "invalide"),
    ({"generation": None, "juge_8b": 1.0, "trace_lite": 1.0}, "invalide")])
def test_artefact_secondes(sec, motif):
    with pytest.raises(GardeArret, match=motif):
        palier().rythme(sec)


# ---------------------------------------------------------------- journal : cas sain

def test_journal_sain_bout_en_bout(tmp_path):
    j = ouvrir(tmp_path)
    el, rng = j.debut(0)
    assert isinstance(rng, np.random.Generator)
    from controle_ia.manifeste import generateur
    assert np.array_equal(rng.standard_normal(3), generateur(el["graine"]).standard_normal(3))
    j.fin(0, secondes=secondes(), version="v1", cache="froid", empreinte_sortie=SORTIE)
    jouer(j, 11)
    sha = j.clore("ordre épuisé")
    lec = fb.lire_journal(j.chemin, ancre_attendue=j.ancre())
    assert lec["clos"] and lec["prochain_rang"] == 12 and len(lec["episodes"]) == 12
    assert lec["palier_lu"]["sonne"] is False and lec["arret"] is None
    assert compagnon(j.chemin).read_text().startswith(sha)
    types = [l["type"] for l in lec["lignes"]]
    assert types[0] == "ouverture" and types[-1] == "cloture" and types.count("palier_lu") == 1
    assert lec["ouverture"]["ordre_sha256"] == fb.empreinte_ordre(lec["ouverture"]["ordre"])
    for l in lec["lignes"]:
        assert l["horodatage"].endswith("+00:00")


def test_artefact_journal_existe_deja(tmp_path):
    j = ouvrir(tmp_path)
    with pytest.raises(GardeArret, match="R12"):
        fb.JournalFabrique.creer(j.chemin, tmp_path / "ordre.json", palier(), instance="i", run_id="r")


def test_artefact_palier_plus_long_que_l_ordre(tmp_path):
    chemin_ordre = tmp_path / "o.json"
    fb.ecrire_ordre(chemin_ordre, fb.tirer_ordre(blocs(), 1))
    with pytest.raises(GardeArret, match="jamais être lu"):
        fb.JournalFabrique.creer(tmp_path / "j.jsonl", chemin_ordre, palier(n=13), instance="i", run_id="r")


# ---------------------------------------------------------------- refus hors ordre

def test_artefact_generation_hors_ordre(tmp_path):
    j = ouvrir(tmp_path)
    with pytest.raises(fb.HorsOrdre, match="attendu"):
        j.debut(1)
    j.debut(0)
    with pytest.raises(fb.HorsOrdre, match="en cours"):
        j.debut(1)
    with pytest.raises(fb.HorsOrdre, match="sans début"):
        j.fin(1, secondes=secondes(), version="v", cache="c", empreinte_sortie=SORTIE)
    j.fin(0, secondes=secondes(), version="v", cache="c", empreinte_sortie=SORTIE)
    with pytest.raises(fb.HorsOrdre):
        j.debut(0)  # déjà joué
    jouer(j, 11)
    with pytest.raises(fb.HorsOrdre, match="épuisé"):
        j.debut(12)


@pytest.mark.parametrize("champ,valeur,motif", [("version", "", "version"), ("cache", " ", "cache"),
                                                 ("empreinte_sortie", "xyz", "sha256")])
def test_artefact_champs_d_episode(tmp_path, champ, valeur, motif):
    j = ouvrir(tmp_path)
    j.debut(0)
    args = dict(secondes=secondes(), version="v", cache="c", empreinte_sortie=SORTIE)
    args[champ] = valeur
    with pytest.raises(GardeArret, match=motif):
        j.fin(0, **args)


def test_artefact_horloge_en_recul_ou_hors_utc(tmp_path):
    j = ouvrir(tmp_path)
    j._horloge = lambda: "2020-01-01T00:00:00+00:00"
    with pytest.raises(GardeArret, match="recul"):
        j.debut(0)
    j._horloge = lambda: "2026-10-29T12:00:00+02:00"
    with pytest.raises(GardeArret, match="UTC"):
        j.debut(0)


# ---------------------------------------------------------------- palier dans le journal

def test_palier_chaque_episode_sain_juste_au_seuil(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 4, secondes(total_moniteurs=139.0, generation=50.0))  # 189 s pile : pas « au-delà »
    assert j.palier_lu and j.arrete is None
    jouer(j, 1, secondes(total_moniteurs=500.0))  # hors palier : mesuré, ne sonne pas
    lec = fb.lire_journal(j.chemin)
    assert lec["palier_lu"]["sonne"] is False and lec["episodes"][-1]["rythme_palier"] == 550.0


def test_artefact_palier_chaque_episode_sonne_et_arret_ecrit(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 1)
    j.debut(1)
    with pytest.raises(fb.ArretPalier, match="nœud de devis"):
        j.fin(1, secondes=secondes(total_moniteurs=140.0), version="v", cache="c", empreinte_sortie=SORTIE)
    with pytest.raises(fb.ArretPalier):
        j.debut(2)
    lec = fb.lire_journal(j.chemin)
    assert lec["arret"]["rang"] == 1 and lec["palier_lu"]["rangs_au_dela"] == [1]
    j.clore("arrêt du palier")
    assert fb.lire_journal(j.chemin)["clos"]


def test_palier_moyenne_sain_et_artefact(tmp_path):
    # sain : un épisode lent, moyenne sous le seuil
    j = ouvrir(tmp_path, palier(regle="moyenne_du_palier"))
    jouer(j, 1, secondes(total_moniteurs=300.0))
    jouer(j, 3, secondes(total_moniteurs=50.0))
    assert j.palier_lu and j.arrete is None
    # artefact : moyenne au-delà, lue seulement au 4e épisode
    d = tmp_path / "b"
    d.mkdir()
    k = ouvrir(d, palier(regle="moyenne_du_palier"))
    jouer(k, 3, secondes(total_moniteurs=200.0))
    assert not k.palier_lu
    k.debut(3)
    with pytest.raises(fb.ArretPalier):
        k.fin(3, secondes=secondes(total_moniteurs=200.0), version="v", cache="c", empreinte_sortie=SORTIE)
    assert fb.lire_journal(k.chemin)["arret"]["verdict"]["valeur"] == 250.0


def test_palier_moniteurs_seuls_ignore_la_generation(tmp_path):
    j = ouvrir(tmp_path, palier(lecture="moniteurs_seuls"))
    jouer(j, 4, secondes(total_moniteurs=180.0, generation=1000.0))
    assert j.arrete is None


# ---------------------------------------------------------------- reprise

def test_reprise_saine_et_artefacts(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 2)
    j.debut(2)
    ancre = j.ancre()
    with pytest.raises(GardeArret, match="motif"):
        fb.JournalFabrique.reprendre(j.chemin, ancre_attendue=ancre)
    with pytest.raises(fb.JournalCorrompu, match="ancre"):
        fb.JournalFabrique.reprendre(j.chemin, ancre_attendue="0" * 64, motif_interruption="x")
    k = fb.JournalFabrique.reprendre(j.chemin, ancre_attendue=ancre, motif_interruption="instance perdue",
                                     horloge=j._horloge)
    assert k.prochain_rang == 2 and k.rythmes == j.rythmes
    jouer(k, 10)
    k.clore("fin")
    lec = fb.lire_journal(k.chemin)
    assert [l["type"] for l in lec["lignes"]].count("interruption") == 1 and lec["prochain_rang"] == 12
    with pytest.raises(GardeArret, match="clos"):
        fb.JournalFabrique.reprendre(k.chemin, ancre_attendue=k.ancre())


def test_artefact_reprise_apres_arret(tmp_path):
    j = ouvrir(tmp_path)
    j.debut(0)
    with pytest.raises(fb.ArretPalier):
        j.fin(0, secondes=secondes(total_moniteurs=1000.0), version="v", cache="c", empreinte_sortie=SORTIE)
    with pytest.raises(fb.ArretPalier, match="nœud de devis"):
        fb.JournalFabrique.reprendre(j.chemin, ancre_attendue=j.ancre())


def test_artefact_ecriture_par_un_tiers(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 1)
    with open(j.chemin, "a") as f:
        f.write("{}\n")
    with pytest.raises(fb.JournalCorrompu, match="tiers"):
        j.debut(1)


# ---------------------------------------------------------------- vérification d'intégrité

def journal_clos_sain(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 6)
    lignes = [json.loads(l) for l in j.chemin.read_text().splitlines()]
    return j, lignes


def test_artefact_ligne_reecrite(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    lignes[6]["contenu"]["secondes"]["juge_8b"] = 1.0  # ligne 6 : épisode du rang 2
    reecrire(j.chemin, lignes)
    with pytest.raises(fb.JournalCorrompu, match="réécrite"):
        fb.lire_journal(j.chemin)


def test_artefact_ligne_non_canonique(tmp_path):
    j, _ = journal_clos_sain(tmp_path)
    t = j.chemin.read_text().splitlines()
    t[3] = t[3].replace(",", ", ", 1)
    j.chemin.write_text("\n".join(t) + "\n")
    with pytest.raises(fb.JournalCorrompu, match="canonique"):
        fb.lire_journal(j.chemin)


def test_artefact_chaine_cassee(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    del lignes[4]
    for i, l in enumerate(lignes):  # numéros recousus, empreintes propres recalculées, précédents laissés
        l["n"] = i
        l.pop("empreinte")
        l["empreinte"] = fb._sha(fb._canonique(l))
    reecrire(j.chemin, lignes)
    with pytest.raises(fb.JournalCorrompu, match="chaîne cassée"):
        fb.lire_journal(j.chemin)


def test_artefact_ligne_retiree(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    del lignes[4]
    reecrire(j.chemin, lignes)
    with pytest.raises(fb.JournalCorrompu, match="numéro"):
        fb.lire_journal(j.chemin)


def test_artefact_trou_d_ordre_meme_rechaine(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    # retire le début et la fin du rang 2 (lignes 5 et 6), rechaîne tout : seule la garde d'ordre peut le voir
    dicos = [l for l in lignes if not (l["type"] in ("debut", "episode") and l["contenu"]["rang"] == 2)]
    reecrit, _ = rechainer(dicos)
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="trou ou désordre"):
        fb.lire_journal(j.chemin)


def test_artefact_episode_permute_rechaine(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    dicos = [dict(l) for l in lignes]
    for d in dicos:
        if d["type"] in ("debut", "episode") and d["contenu"]["rang"] == 1:
            d["contenu"] = dict(d["contenu"], tache="autre")
    reecrit, _ = rechainer(dicos)
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="différent de l'ordre"):
        fb.lire_journal(j.chemin)


def test_artefact_verdict_du_palier_falsifie_rechaine(tmp_path):
    j = ouvrir(tmp_path)
    j.debut(0)
    with pytest.raises(fb.ArretPalier):
        j.fin(0, secondes=secondes(total_moniteurs=1000.0), version="v", cache="c", empreinte_sortie=SORTIE)
    lignes = [json.loads(l) for l in j.chemin.read_text().splitlines()]
    dicos = [l for l in lignes if l["type"] != "arret_palier"]
    for d in dicos:
        if d["type"] == "palier_lu":
            d["contenu"] = dict(d["contenu"], sonne=False)
    reecrit, _ = rechainer(dicos)
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="palier incohérent"):
        fb.lire_journal(j.chemin)


def test_artefact_arret_retire_rechaine(tmp_path):
    j = ouvrir(tmp_path)
    j.debut(0)
    with pytest.raises(fb.ArretPalier):
        j.fin(0, secondes=secondes(total_moniteurs=1000.0), version="v", cache="c", empreinte_sortie=SORTIE)
    lignes = [json.loads(l) for l in j.chemin.read_text().splitlines()]
    reecrit, _ = rechainer([l for l in lignes if l["type"] != "arret_palier"])
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="arrêt n'est pas écrit"):
        fb.lire_journal(j.chemin)


def test_artefact_verdict_omis_rechaine(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    reecrit, _ = rechainer([l for l in lignes if l["type"] != "palier_lu"])
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="aucun verdict"):
        fb.lire_journal(j.chemin)


def test_artefact_derniere_ligne_tronquee_ou_reecrite(tmp_path):
    j, _ = journal_clos_sain(tmp_path)
    ancre = j.ancre()
    brut = j.chemin.read_bytes()
    j.chemin.write_bytes(brut[:-10])
    with pytest.raises(fb.JournalCorrompu, match="tronquée"):
        fb.lire_journal(j.chemin)
    j.chemin.write_bytes(brut[:-10] + b"\n")
    with pytest.raises(fb.JournalCorrompu, match="illisible"):
        fb.lire_journal(j.chemin)
    # dernière ligne réécrite avec empreinte recalculée : seule l'ancre la voit
    lignes = [json.loads(l) for l in brut.decode().splitlines()]
    lignes[-1]["contenu"]["cache"] = "chaud"
    reecrit, _ = rechainer(lignes)
    reecrire(j.chemin, reecrit)
    assert fb.lire_journal(j.chemin)  # sans ancre : indétectable, d'où l'ancre
    with pytest.raises(fb.JournalCorrompu, match="ancre"):
        fb.lire_journal(j.chemin, ancre_attendue=ancre)


def test_artefact_ajout_apres_cloture(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 4)
    j.clore("fin")
    with pytest.raises(GardeArret, match="clos"):
        j.debut(4)
    lignes = [json.loads(l) for l in j.chemin.read_text().splitlines()]
    dicos = lignes + [{"type": "debut", "horodatage": "2026-10-29T11:00:00.000000+00:00",
                       "contenu": lignes[-3]["contenu"]}]
    reecrit, _ = rechainer(dicos)
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="après la clôture"):
        fb.lire_journal(j.chemin)


def test_artefact_sceau_de_cloture(tmp_path):
    j = ouvrir(tmp_path)
    jouer(j, 4)
    j.clore("fin")
    compagnon(j.chemin).unlink()
    with pytest.raises(fb.JournalCorrompu, match="sceau"):
        fb.lire_journal(j.chemin)
    d = tmp_path / "b"
    d.mkdir()
    k = ouvrir(d)
    jouer(k, 1)
    compagnon(k.chemin).write_text("0" * 64 + "  journal.jsonl\n")
    with pytest.raises(fb.JournalCorrompu, match="sans clôture"):
        fb.lire_journal(k.chemin)


def test_artefact_ordre_engage_retouche_rechaine(tmp_path):
    j, lignes = journal_clos_sain(tmp_path)
    o = lignes[0]["contenu"]["ordre"]
    o["elements"][0]["graine"]["etat_controle"][0] += 1
    reecrit, _ = rechainer(lignes)
    reecrire(j.chemin, reecrit)
    with pytest.raises(fb.JournalCorrompu, match="ouverture invalide"):
        fb.lire_journal(j.chemin)


def test_artefact_journal_absent_ou_vide(tmp_path):
    with pytest.raises(fb.JournalCorrompu, match="absent"):
        fb.lire_journal(tmp_path / "rien.jsonl")
    (tmp_path / "vide.jsonl").write_text("")
    with pytest.raises(fb.JournalCorrompu, match="vide"):
        fb.lire_journal(tmp_path / "vide.jsonl")
