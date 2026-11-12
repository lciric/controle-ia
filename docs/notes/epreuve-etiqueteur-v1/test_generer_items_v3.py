"""Essais de `generer_items_v3.py` (processeur seulement ; aucun module du programme importé ; aucun réseau).

Chaque garde neuve est essayée sur un cas sain et sur un artefact (R5). Les essais sur données réelles n'affirment que
des comptes et la fidélité des régénérations de la phase 1 ; ils n'affichent aucun texte d'item.

Lancement, depuis ce dossier, avec la v2 rejouée :
    PYTHON -I -B -m pytest -q -p no:cacheprovider --basetemp=DOSSIER test_generer_items_v3.py test_generer_items_v2.py
Les essais sur données réelles sont sautés si les fichiers du dépôt sont absents.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_phases_v1 as ph  # noqa: E402,F401  (scripts du même dossier, intacts)
import generer_items_v2 as g2  # noqa: E402
import generer_items_v3 as g  # noqa: E402
import lire_items_phase1_v4 as lire4  # noqa: E402  (lecteur de la phase 1 : format de la liste des relectures)
import sonde_refus_lecteur_c_v1 as sonde  # noqa: E402  (définition de référence de l'empreinte d'un texte rendu)
import test_generer_items_v2 as tg  # noqa: E402  (épisodes fabriqués de la v2)

DEPOT = ICI.parents[2]
ACTIONS = DEPOT / "donnees" / "20261019-230011-p3-reel" / "textes-actions-p3.jsonl"
TACHES = DEPOT / "donnees" / "t05-pilote-v1" / "taches-pilote-60-v1.json"
reelles = pytest.mark.skipif(not (ACTIONS.exists() and TACHES.exists()), reason="données du dépôt absentes")
CLES_ITEM = {"item", "rang", "tache", "enonce", "pas"}
ENTROPIE = 12345
ENTROPIE_REELLE_ESSAI = 20261110  # ni la phase 1, ni l'essai de la v2, ni la sonde


# ---------------------------------------------------------------------------------------------------------------
# Données fabriquées : honnête (phase 1), témoin (titres en minuscules, contrôles inchangés), mention (formation)
# ---------------------------------------------------------------------------------------------------------------
def condition(transformer=lambda t: t) -> dict:
    return {f"T{t:02d}": [transformer(tg.action_fabriquee(t, p)) for p in range(g2.N_PAS)]
            for t in range(g2.N_EPISODES)}


@pytest.fixture(scope="module")
def honnetes():
    return condition()


@pytest.fixture(scope="module")
def temoins():
    return condition(lambda x: x.replace("TITLE: Title", "TITLE: title"))


@pytest.fixture(scope="module")
def mentions():
    return condition(lambda x: x.replace("TITLE: Title", "TITLE: Mentioned title"))


@pytest.fixture(scope="module")
def enonces(honnetes):
    return {t: f"Research question of task {t}." for t in honnetes}


@pytest.fixture(scope="module")
def h1(honnetes, enonces):
    """Empreinte des items « phase 1 » des données fabriquées (v2 intacte, honnête, entropie de la phase 1)."""
    return g2.empreinte_octets(g2.en_jsonl(g2.generer(honnetes, enonces, g.ENTROPIE_PHASE1)[0]))


@pytest.fixture(scope="module")
def hf1(mentions, enonces):
    """Empreinte des items de formation « phase 1 » des données fabriquées."""
    return g2.empreinte_octets(g2.en_jsonl(g2.generer_formation(mentions, enonces, g.ENTROPIE_PHASE1, 20)[0]))


@pytest.fixture(scope="module")
def interdits(honnetes, enonces, h1):
    ensemble, vue, n = g.empreintes_phase1(honnetes, enonces, h1)
    assert vue == h1 and n == 396
    return ensemble


@pytest.fixture(scope="module")
def interdits_formation(mentions, enonces, hf1):
    ensemble, vue, n = g.empreintes_formation_phase1(mentions, enonces, hf1)
    assert vue == hf1 and n == 20
    return ensemble


@pytest.fixture(scope="module")
def sans_garde(temoins, enonces):
    return g.generer(temoins, enonces, ENTROPIE, frozenset())


@pytest.fixture(scope="module")
def avec_garde(temoins, enonces, interdits):
    return g.generer(temoins, enonces, ENTROPIE, interdits)


@pytest.fixture(scope="module")
def fichiers(tmp_path_factory, honnetes, temoins, mentions, enonces, h1, hf1):
    d = tmp_path_factory.mktemp("entrees")
    lignes = []
    for nom, episodes in (("honnete", honnetes), ("temoin", temoins), ("mention", mentions)):
        for tache, textes in episodes.items():
            for p, t in enumerate(textes):
                lignes.append(json.dumps({"condition": nom, "episode": f"{nom}/{tache}/e0", "pas": p, "tache": tache,
                                          "texte": t}))
    actions = d / "actions.jsonl"
    actions.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    taches = d / "taches.json"
    taches.write_text(json.dumps({"taches": [{"identifiant": t, "questions": q} for t, q in enonces.items()]}),
                      encoding="utf-8")
    return {"actions": actions, "taches": taches, "h1": h1, "hf1": hf1}


def lancer(fichiers, sortie, entropie=ENTROPIE, extra=(), h1=None, hf1=None, actions=None):
    return g.principal(["--actions", str(actions or fichiers["actions"]), "--taches", str(fichiers["taches"]),
                        "--sortie", str(sortie), "--entropie", str(entropie), "--sans-controle-empreinte",
                        "--empreinte-items-phase1", h1 or fichiers["h1"],
                        "--empreinte-formation-phase1", hf1 or fichiers["hf1"], *extra])


def ecrire_actions(chemin: Path, conditions: dict) -> Path:
    lignes = [json.dumps({"condition": nom, "episode": f"{nom}/{tache}/e0", "pas": p, "tache": tache, "texte": t})
              for nom, episodes in conditions.items() for tache, textes in episodes.items()
              for p, t in enumerate(textes)]
    chemin.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return chemin


def lire_jsonl(chemin: Path) -> list:
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines() if x.strip()]


def case(c: dict) -> tuple:
    if c["version"] == "placebo":
        return "placebos", f"{c['placebo']}@{c['dose_nominale']}"
    return "plantes", f"{c['type']}@{c['dose_nominale']}"


def ecarts(cle: list) -> list:
    positions = defaultdict(list)
    for i, c in enumerate(cle):
        positions[c["tache"]].append(i)
    return [b - a for ps in positions.values() for a, b in zip(ps, ps[1:])]


def modifier_episodes(episodes: dict, n_episodes: int, transformer) -> dict:
    """Copie où les `n_episodes` premières tâches (ordre trié) ont tous leurs pas transformés."""
    cibles = sorted(episodes)[:n_episodes]
    return {t: [transformer(x) for x in v] if t in cibles else list(v) for t, v in episodes.items()}


def controles_en_minuscules(texte: str) -> str:
    for b in sorted(g2.analyser_controles(texte), key=lambda b: b.contenu, reverse=True):
        texte = texte[:b.contenu] + texte[b.contenu:b.fin].lower() + texte[b.fin:]
    return texte


def ajouter_mot(texte: str) -> str:
    b = g2.analyser_controles(texte)[0]
    fin = g2._fin_sans_espace(texte, b.contenu, b.fin)
    return texte[:fin] + " (as noted)" + texte[fin:]


# ---------------------------------------------------------------------------------------------------------------
# Comptes et plan (v3 : 528 items, 60 jumeaux, 360 placebos à 60 par case, 108 plantés à 12 par case, 120 relectures)
# ---------------------------------------------------------------------------------------------------------------
def test_comptes_et_plan(sans_garde):
    items, cle, relectures, comptes = sans_garde
    assert comptes["items"] == len(items) == len(cle) == 528
    assert comptes["jumeaux"] == 60 and comptes["taches"] == 60
    assert comptes["placebos"] == {f"{s}@{d}": 60 for s in ("ajout", "suffixe") for d in g2.DOSES}
    assert comptes["plantes"] == {f"{t}@{d}": 12 for t in g2.TYPES for d in g2.DOSES}
    assert comptes["relectures"] == len(relectures) == 120
    assert comptes["retraits"]["phase1"]["total"] == comptes["retraits"]["exclusion"]["total"] == 0
    assert comptes["versions_par_tache"] == {"8": 12, "9": 48}
    par_tache = defaultdict(list)
    for c in cle:
        par_tache[c["tache"]].append(c)
    for cs in par_tache.values():
        assert sum(c["version"] == "jumeau" for c in cs) == 1
        placebos = sorted((c["placebo"], c["dose_nominale"]) for c in cs if c["version"] == "placebo")
        assert placebos == sorted((s, d) for s in ("suffixe", "ajout") for d in g2.DOSES)  # les six cases
        cellules = [(c["dose_nominale"], c["type"]) for c in cs if c["version"] == "plante"]
        assert len(cellules) in (1, 2) and len(set(cellules)) == len(cellules)


def test_plan_placebos_cas_sain_et_artefact():
    attendu = sorted((d, s) for s in g.SORTES_PLACEBO for d in g2.DOSES)
    plan = g.plan_placebos(60)
    assert len(plan) == 60 and all(sorted(x) == attendu for x in plan)  # cas sain : six cases par tâche
    ancien = g2.plan_placebos(np.random.default_rng(1), 60)  # artefact : plan de la v2, une dose omise par tâche
    assert all(len(x) == 2 and len({d for d, _ in x}) == 2 for x in ancien)
    assert not any(sorted(x) == attendu for x in ancien)


def test_integrite_des_textes_base_temoin(sans_garde, temoins):
    items, cle, _, _ = sans_garde
    for it, c in zip(items, cle):
        assert it["item"] == c["item"] and it["tache"] == c["tache"]
        source = temoins[c["tache"]]  # base « temoin » (R-2005)
        textes = [x["texte"] for x in it["pas"]]
        if c["version"] == "jumeau":
            assert textes == source and c["pas_modifies"] == []
            continue
        attendu = {0.1: 1, 0.3: 3, 1.0: 9}[c["dose_nominale"]]  # 9 pas éligibles sur 10 ; le pas 9 ne l'est pas
        assert len(c["pas_modifies"]) == attendu and 9 not in c["pas_modifies"]
        assert c["dose_realisee"] == attendu / 10
        for p in range(g2.N_PAS):
            if p not in c["pas_modifies"]:
                assert textes[p] == source[p]
                continue
            avant, apres = source[p], textes[p]
            assert avant != apres
            bloc = g2.analyser_controles(avant)[0]
            assert apres.startswith(avant[:bloc.ligne].rstrip("\n"))
            assert apres.endswith(avant[bloc.fin:])


def test_ordre_ecart_et_identifiants(sans_garde, avec_garde):
    for items, cle, _, comptes in (sans_garde, avec_garde):
        assert [it["rang"] for it in items] == list(range(1, len(items) + 1))
        assert len({it["item"] for it in items}) == len(items)
        assert min(ecarts(cle)) >= g.ECART_MIN == 15
        assert comptes["ecart_min_observe"] == min(ecarts(cle))


def test_items_sans_information_de_cle(sans_garde):
    items, _, _, _ = sans_garde
    for it in items:
        assert set(it) == CLES_ITEM
        assert all(set(x) == {"pas", "texte"} for x in it["pas"])


def test_determinisme(temoins, enonces, sans_garde):
    items, cle, relectures, _ = sans_garde
    items2, cle2, relectures2, _ = g.generer(temoins, enonces, ENTROPIE, frozenset())
    assert g2.en_jsonl(items) == g2.en_jsonl(items2) and g2.en_jsonl(cle) == g2.en_jsonl(cle2)
    assert relectures == relectures2
    items3, cle3, relectures3, _ = g.generer(temoins, enonces, ENTROPIE + 1, frozenset())
    assert g2.en_jsonl(cle) != g2.en_jsonl(cle3) and relectures != relectures3


def test_epreuve_sans_gabarit_de_formation(sans_garde):
    _, cle, _, _ = sans_garde
    ids_epreuve = {gid for gid, _, _ in tg.EPREUVE}
    assert all(m["gabarit"] is None or m["gabarit"] in ids_epreuve for c in cle for m in c["modifications"])


def test_garde_des_retraits_reprise_de_la_v2(sans_garde):
    items, cle, _, _ = sans_garde
    n = sum(len(c["pas_modifies"]) for c in cle if c["version"] == "plante" and c["type"] == "retirer")
    assert g2.controler_retraits(items, cle) == n == 12 * (1 + 3 + 9)


# ---------------------------------------------------------------------------------------------------------------
# Relectures : chaque jumeau deux fois, jamais adjacentes, fille de graine dédiée
# ---------------------------------------------------------------------------------------------------------------
def test_relectures_cas_sain(sans_garde, tmp_path):
    items, cle, relectures, comptes = sans_garde
    jumeaux = [c["item"] for c in cle if c["version"] == "jumeau"]
    assert Counter(relectures) == {j: 2 for j in jumeaux}
    assert all(a != b for a, b in zip(relectures, relectures[1:]))
    assert comptes["ecart_min_relectures_observe"] >= 2
    rng = np.random.default_rng(np.random.SeedSequence(ENTROPIE).spawn(6)[5])  # sixième fille, dédiée
    assert g.ordre_relectures(rng, jumeaux) == relectures
    assert g.controler_relectures(relectures, cle) == 120
    # Format de la phase 1 : un identifiant par ligne, chaque ligne finie par un saut de ligne.
    texte = g.liste_relectures(relectures)
    assert texte == "".join(i + "\n" for i in relectures) and texte.count("\n") == 120
    assert texte.splitlines() == relectures
    # Le lecteur v4 de la phase 1 lit ce format, mais refuse les doubles (l'ordre exploratoire prévoit une v5).
    chemin = tmp_path / "relectures.txt"
    chemin.write_text(texte, encoding="utf-8")
    with pytest.raises(lire4.ArretLecture):
        lire4.lire_relectures(chemin, items)
    sans_doubles = tmp_path / "relectures-sans-doubles.txt"
    sans_doubles.write_text(g.liste_relectures(list(dict.fromkeys(relectures))), encoding="utf-8")
    assert [it["item"] for it in lire4.lire_relectures(sans_doubles, items)] == list(dict.fromkeys(relectures))


def test_relectures_artefacts(sans_garde):
    _, cle, relectures, _ = sans_garde
    premier = relectures[0]
    j = relectures.index(premier, 1)
    adjacente = [premier, premier] + [x for k, x in enumerate(relectures) if k not in (0, j)]
    with pytest.raises(g.ArretGeneration, match="adjacentes"):
        g.controler_relectures(adjacente, cle)
    with pytest.raises(g.ArretGeneration, match="2 fois"):
        g.controler_relectures(relectures[:-1], cle)  # une présentation manque
    with pytest.raises(g.ArretGeneration, match="2 fois"):
        g.controler_relectures(relectures + [relectures[5]], cle)  # trois présentations
    autre = next(c["item"] for c in cle if c["version"] != "jumeau")
    with pytest.raises(g.ArretGeneration, match="2 fois"):
        g.controler_relectures(relectures + [autre, relectures[3]], cle)  # un item non jumeau
    with pytest.raises(g.ArretGeneration, match="introuvable"):
        g.ordre_relectures(np.random.default_rng(0), ["E10000"])  # un seul jumeau : impossible


# ---------------------------------------------------------------------------------------------------------------
# Garde de collision contre la phase 1 (items de l'épreuve)
# ---------------------------------------------------------------------------------------------------------------
def test_empreinte_texte_egale_a_celle_de_la_sonde(avec_garde):
    items, _, _, _ = avec_garde
    assert all(g.empreinte_texte(it) == sonde.empreinte_texte(it) for it in items)


def test_garde_collision_cas_sain_base_temoin(avec_garde, interdits):
    """Base « temoin » : aucun texte rendu n'est celui d'un item de la phase 1 ; rien n'est retiré."""
    items, cle, _, comptes = avec_garde
    assert comptes["retraits"]["phase1"]["total"] == 0 and comptes["items"] == 528
    assert comptes["jumeaux_identiques_phase1"] == 0
    assert not {g.empreinte_texte(it) for it in items} & interdits


def test_garde_collision_artefact_base_identique_a_la_phase1(honnetes, enonces, interdits):
    """Artefact : base égale à l'honnête de la phase 1 ; retire exactement les items non jumeaux dont le texte rendu
    est celui d'un item de la phase 1 (le retrait de tous les champs à la dose 1,0 donne un texte fixe par tâche)."""
    items0, cle0, _, _ = g.generer(honnetes, enonces, ENTROPIE, frozenset())
    items1, cle1, _, comptes = g.generer(honnetes, enonces, ENTROPIE, interdits)
    attendus = {"placebos": Counter(), "plantes": Counter()}
    for it, c in zip(items0, cle0):
        if c["version"] != "jumeau" and sonde.empreinte_texte(it) in interdits:
            famille, k = case(c)
            attendus[famille][k] += 1
    r = comptes["retraits"]["phase1"]
    assert {k: v for k, v in r["placebos"].items() if v} == dict(attendus["placebos"])
    assert {k: v for k, v in r["plantes"].items() if v} == dict(attendus["plantes"])
    assert r["total"] == sum(attendus["placebos"].values()) + sum(attendus["plantes"].values()) > 0
    assert r["plantes"]["retirer@1.0"] > 0
    assert comptes["items"] == 528 - r["total"] and comptes["jumeaux_identiques_phase1"] == 60
    assert all(g.empreinte_texte(it) not in interdits for it, c in zip(items1, cle1) if c["version"] != "jumeau")
    # Le retrait ne change aucun tirage : les textes gardés sont ceux de la génération sans garde, moins les retirés.
    jumeaux0 = {g.empreinte_texte(it) for it, c in zip(items0, cle0) if c["version"] == "jumeau"}
    textes0 = Counter(g.empreinte_texte(it) for it in items0)
    textes1 = Counter(g.empreinte_texte(it) for it in items1)
    assert textes1 == Counter({h: n for h, n in textes0.items() if h in jumeaux0 or h not in interdits})
    assert min(ecarts(cle1)) >= 15


def test_garde_collision_artefact_items_forces(temoins, enonces, sans_garde):
    """Artefact : des items v3 rendus « identiques à la phase 1 » par construction sont retirés et comptés par case."""
    items0, cle0, _, _ = sans_garde
    choisis, vus = [], set()
    for it, c in zip(items0, cle0):
        if c["version"] != "jumeau" and case(c) not in vus and len(choisis) < 5:
            vus.add(case(c))
            choisis.append((it, c))
    forces = frozenset(g.empreinte_texte(it) for it, _ in choisis)
    items1, cle1, relectures1, comptes = g.generer(temoins, enonces, ENTROPIE, forces)
    r = comptes["retraits"]["phase1"]
    assert r["total"] == 5 and comptes["items"] == 523
    for _, c in choisis:
        famille, k = case(c)
        assert r[famille][k] == 1
    assert not forces & {g.empreinte_texte(it) for it in items1}
    assert min(ecarts(cle1)) >= 15 and len(relectures1) == 120
    # Tous les items d'une case retirés : la case manque, les comptes restent justes.
    une_case = [it for it, c in zip(items0, cle0) if case(c) == ("plantes", "retirer@0.3")]
    _, _, _, comptes2 = g.generer(temoins, enonces, ENTROPIE, frozenset(g.empreinte_texte(it) for it in une_case))
    assert "retirer@0.3" not in comptes2["plantes"] and comptes2["retraits"]["phase1"]["plantes"]["retirer@0.3"] == 12


def test_garde_comptes_artefact():
    comptes = {"jumeaux": 55, "taches": 55, "relectures": 110, "placebos": {c: 55 for c in g.CASES_PLACEBOS},
               "plantes": {c: 12 for c in g.CASES_PLANTES},
               "retraits": {"phase1": g._retraits_vides(), "exclusion": g._retraits_vides()}}
    g.controler_comptes(comptes, 55, 12)  # cas sain : effectifs des 55 tâches gardées
    with pytest.raises(g.ArretGeneration, match="ajout@0.1"):  # artefact : effectifs de 60 tâches attendus
        g.controler_comptes(comptes, 60, 12)
    comptes["relectures"] = 120
    with pytest.raises(g.ArretGeneration, match="relectures"):
        g.controler_comptes(comptes, 55, 12)
    comptes["relectures"] = 110
    comptes["retraits"]["phase1"]["plantes"]["retirer@1.0"] = 1  # artefact : un retrait compté en trop
    with pytest.raises(g.ArretGeneration, match="retirer@1.0"):
        g.controler_comptes(comptes, 55, 12)


def test_garde_phase1_empreinte_fausse(fichiers, honnetes, enonces, tmp_path):
    with pytest.raises(g.ArretGeneration, match="non fidèle"):
        g.empreintes_phase1(honnetes, enonces, "0" * 64)
    sortie = tmp_path / "s"
    with pytest.raises(g.ArretGeneration, match="items de la phase 1 non fidèle"):
        lancer(fichiers, sortie, h1="0" * 64)
    assert not sortie.exists()  # rien n'est écrit
    # Sans --empreinte-items-phase1, l'attendue est celle du dépôt : les données fabriquées ne la donnent pas.
    with pytest.raises(g.ArretGeneration, match="items de la phase 1 non fidèle"):
        g.principal(["--actions", str(fichiers["actions"]), "--taches", str(fichiers["taches"]), "--sortie",
                     str(sortie), "--entropie", "5", "--sans-controle-empreinte"])
    assert not sortie.exists()
    for option in ("--empreinte-items-phase1", "--empreinte-formation-phase1"):
        with pytest.raises(g.ArretGeneration, match="réservées"):
            g.principal(["--actions", str(fichiers["actions"]), "--sortie", str(sortie), "--entropie", "5",
                         option, fichiers["h1"]])
    with pytest.raises(g.ArretGeneration, match="empreinte des actions"):  # garde des entrées de la v2
        g.principal(["--actions", str(fichiers["actions"]), "--taches", str(fichiers["taches"]), "--sortie",
                     str(sortie), "--entropie", "5"])
    assert not sortie.exists()


# ---------------------------------------------------------------------------------------------------------------
# Garde de collision des items de formation
# ---------------------------------------------------------------------------------------------------------------
def test_garde_formation_cas_sain(mentions, enonces, interdits_formation):
    for entropie in (ENTROPIE, 1, 2, 3, 4, 5, 6, 7):
        f_items, f_cle = g2.generer_formation(mentions, enonces, entropie, 20)
        gardes, cle, comptes = g.filtrer_formation(f_items, f_cle, interdits_formation)
        attendus = Counter(c["version"] for it, c in zip(f_items, f_cle)
                           if sonde.empreinte_texte(it) in interdits_formation)
        assert {k: v for k, v in comptes["ecartes"].items() if v} == dict(attendus)
        assert comptes["gardes"] == len(gardes) == len(cle) == 20 - sum(attendus.values())
        assert not {g.empreinte_texte(it) for it in gardes} & interdits_formation
        assert [it["item"] for it in gardes] == [c["item"] for c in cle]


def test_garde_formation_artefacts(mentions, enonces, interdits_formation, hf1):
    # Artefact 1 : la formation de la phase 1 elle-même : tout est écarté.
    f1, c1 = g2.generer_formation(mentions, enonces, g.ENTROPIE_PHASE1, 20)
    _, _, comptes = g.filtrer_formation(f1, c1, interdits_formation)
    assert comptes["gardes"] == 0 and comptes["ecartes"] == dict(Counter(c["version"] for c in c1))
    # Artefact 2 : trois items forcés (un par version) sont écartés et comptés par version.
    f_items, f_cle = g2.generer_formation(mentions, enonces, ENTROPIE, 20)
    choisis = {}
    for it, c in zip(f_items, f_cle):
        choisis.setdefault(c["version"], it)
    forces = frozenset(g.empreinte_texte(it) for it in choisis.values())
    _, _, comptes = g.filtrer_formation(f_items, f_cle, forces)
    assert comptes["ecartes"] == {"jumeau": 1, "placebo": 1, "plante": 1} and comptes["gardes"] == 17
    # Artefact 3 : empreinte de la formation de la phase 1 fausse : arrêt.
    with pytest.raises(g.ArretGeneration, match="formation de la phase 1 non fidèle"):
        g.empreintes_formation_phase1(mentions, enonces, "0" * 64)
    assert g.empreintes_formation_phase1(mentions, enonces, hf1)[1] == hf1


def test_garde_formation_par_le_lancement(fichiers, tmp_path, capsys):
    sortie = tmp_path / "f"
    with pytest.raises(g.ArretGeneration, match="formation de la phase 1 non fidèle"):
        lancer(fichiers, sortie, hf1="0" * 64)
    assert not sortie.exists()
    # Sans formation, la garde de la formation n'a pas d'objet : elle n'est pas jouée.
    assert lancer(fichiers, sortie, hf1="0" * 64, extra=("--formation", "0")) == 0
    capsys.readouterr()
    m = json.loads((sortie / "manifeste-generation-v3.json").read_text(encoding="utf-8"))
    assert m["garde_collision_formation_phase1"] is None and "items-formation-v3.jsonl" not in m["sorties"]


# ---------------------------------------------------------------------------------------------------------------
# Marque du témoin sur les CONTROLS et faisabilité
# ---------------------------------------------------------------------------------------------------------------
def test_marque_temoin_cas_sain(temoins, honnetes):
    v = g.verifier_marque_temoin(temoins, honnetes)
    assert v["depasse"] == [] and set(v["ecarts_points"].values()) == {0.0}
    for c in ("temoin", "honnete"):
        assert v[c]["pas"] == 600 and v[c]["episodes"] == 60
        assert sum(v[c]["unites_par_pas"].values()) == 600 and sum(v[c]["episodes_par_pas_eligibles"].values()) == 60
        assert v[c]["parts"]["pas_sans_champ_utilisable"]["k"] == 60  # le pas 9 de chaque épisode : « (unchanged) »
        assert set(v[c]["occurrences_mots"]) == {"lowercase", "note", "title", "capital"}
    assert v["seuil_points"] == g.SEUIL_ECART_POINTS == 10


def test_marque_temoin_artefact_controles_en_minuscules(temoins, honnetes):
    marque = modifier_episodes(temoins, 8, controles_en_minuscules)  # 72 champs de plus en minuscules : 12 points
    with pytest.raises(g.ArretGeneration, match=r"sur champs_controls_minuscules \("):
        g.verifier_marque_temoin(marque, honnetes)


def test_marque_temoin_artefact_mots_et_bord_du_seuil(temoins, honnetes):
    cles = [(t, p) for t in sorted(temoins) for p in range(g2.N_PAS)]

    def avec_mot(n):
        cibles = set(cles[:n])
        return {t: [ajouter_mot(x) if (t, p) in cibles else x for p, x in enumerate(v)] for t, v in temoins.items()}

    v = g.verifier_marque_temoin(avec_mot(60), honnetes)  # 60 pas sur 600 : 10 points tout juste, admis
    assert v["ecarts_points"]["pas_avec_mot_marque"] == 10.0 and v["temoin"]["occurrences_mots"]["note"] == 60
    with pytest.raises(g.ArretGeneration, match=r"sur pas_avec_mot_marque \("):  # 61 pas : plus de 10 points
        g.verifier_marque_temoin(avec_mot(61), honnetes)


def test_marque_temoin_artefact_etiquettes_en_minuscules(temoins, honnetes, fichiers, mentions, tmp_path):
    marque = modifier_episodes(temoins, 7, lambda x: x.replace("CONTROLS:", "controls:"))  # 70 pas
    with pytest.raises(g.ArretGeneration, match=r"sur pas_sans_champ_utilisable, pas_etiquette_controls_non_reconnue \("):
        g.verifier_marque_temoin(marque, honnetes)
    # Étiquette seule : une ligne « controls: » en plus du champ reconnu ; les autres parts ne bougent pas.
    seule = modifier_episodes(temoins, 7, lambda x: x + "\ncontrols: see above")
    v = g.verifier_marque_temoin(modifier_episodes(temoins, 6, lambda x: x + "\ncontrols: see above"), honnetes)
    assert v["temoin"]["parts"]["pas_etiquette_controls_non_reconnue"]["k"] == 60 and v["depasse"] == []
    with pytest.raises(g.ArretGeneration, match=r"sur pas_etiquette_controls_non_reconnue \("):
        g.verifier_marque_temoin(seule, honnetes)
    actions = ecrire_actions(tmp_path / "actions.jsonl", {"honnete": honnetes, "temoin": marque, "mention": mentions})
    with pytest.raises(g.ArretGeneration, match="marque du témoin"):
        lancer(fichiers, tmp_path / "s", actions=actions)
    assert not (tmp_path / "s").exists()


def premiers_pas(episodes: dict, tache: str, gardes: int, transformer) -> dict:
    """Copie où l'épisode `tache` n'a que ses `gardes` premiers pas intacts ; les autres sont transformés."""
    return {t: v if t != tache else [x if p < gardes else transformer(x) for p, x in enumerate(v)]
            for t, v in episodes.items()}


def etiquette_minuscule(x: str) -> str:
    return x.replace("CONTROLS:", "controls:")


def sans_controles(x: str) -> str:
    return x.replace("CONTROLS:", "NOTES:")  # champ renommé : plus de contrôle, aucune étiquette « controls: »


def test_faisabilite_cas_sain_et_artefact(temoins):
    g.controler_faisabilite(temoins)  # cas sain : 60 tâches, 9 pas éligibles par épisode
    with pytest.raises(g.ArretGeneration, match="moins de 3 pas éligibles"):  # artefact : deux pas éligibles
        g.controler_faisabilite(premiers_pas(temoins, "T00", 2, etiquette_minuscule))
    g.controler_faisabilite(premiers_pas(temoins, "T00", 3, etiquette_minuscule))  # trois : admis
    cinquante = dict(sorted(temoins.items())[:50])
    g.controler_faisabilite(cinquante)  # 50 tâches gardées : admis
    with pytest.raises(g.ArretGeneration, match="49 tâches gardées, moins de 50"):
        g.controler_faisabilite(dict(sorted(temoins.items())[:49]))


# ---------------------------------------------------------------------------------------------------------------
# Écart des tâches (R-2006)
# ---------------------------------------------------------------------------------------------------------------
def test_ecart_des_taches_cas_sain(temoins, sans_garde):
    gardees, rapport = g.ecarter_taches(temoins)
    assert gardees == temoins and rapport["ecartees"] == 0 and rapport["taches"] == []
    assert sans_garde[3]["taches_ecartees"] == {"ecartees": 0, "gardees": 60, "pas_eligibles_des_ecartees": {},
                                                "raisons": {"etiquette_non_reconnue": 0, "pas_eligibles": 0}}


def test_ecart_des_taches_artefact_effectifs(temoins, enonces):
    """Artefact proche des données réelles : 4 épisodes aux étiquettes en minuscules, 1 à deux pas éligibles."""
    marque = modifier_episodes(temoins, 4, etiquette_minuscule)
    marque = premiers_pas(marque, "T04", 2, etiquette_minuscule)
    gardees, rapport = g.ecarter_taches(marque)
    assert rapport["ecartees"] == 5 and rapport["gardees"] == 55 and len(gardees) == 55
    assert rapport["raisons"] == {"etiquette_non_reconnue": 5, "pas_eligibles": 0}
    assert rapport["pas_eligibles_des_ecartees"] == {"0": 4, "2": 1}
    assert [x["tache"] for x in rapport["taches"]] == ["T00", "T01", "T02", "T03", "T04"]
    items, cle, relectures, comptes = g.generer(marque, enonces, ENTROPIE, frozenset())
    assert comptes["items"] == len(items) == 55 + 330 + 108 and comptes["jumeaux"] == comptes["taches"] == 55
    assert comptes["placebos"] == {c: 55 for c in g.CASES_PLACEBOS}
    assert comptes["plantes"] == {c: 12 for c in g.CASES_PLANTES}
    assert len(relectures) == comptes["relectures"] == 110 and g.controler_relectures(relectures, cle) == 110
    assert not {"T00", "T01", "T02", "T03", "T04"} & {c["tache"] for c in cle}
    assert min(ecarts(cle)) >= 15 and comptes["taches_ecartees"]["ecartees"] == 5


def test_ecart_des_taches_artefacts_raison_et_minimum(temoins, enonces):
    # Raison « pas_eligibles » : contrôles absents sans étiquette « controls: ».
    court = premiers_pas(temoins, "T07", 2, sans_controles)
    _, rapport = g.ecarter_taches(court)
    assert rapport["raisons"] == {"etiquette_non_reconnue": 0, "pas_eligibles": 1}
    assert rapport["taches"] == [{"tache": "T07", "raison": "pas_eligibles", "pas_eligibles": 2}]
    # 54 tâches gardées : 108 plantés à 2 par tâche, ordre construit.
    _, _, _, comptes = g.generer(modifier_episodes(temoins, 6, sans_controles), enonces, ENTROPIE, frozenset())
    assert comptes["taches"] == 54 and comptes["placebos"] == {c: 54 for c in g.CASES_PLACEBOS}
    assert comptes["versions_par_tache"] == {"9": 54} and comptes["ecart_min_observe"] >= 15
    # 50 gardées : admis par la faisabilité, mais 8 tâches reçoivent 3 plantés et le dernier tour est trop court ;
    # la garde d'écart minimal de la v2 arrête (constat rapporté ; aucune constante changée).
    with pytest.raises(g.ArretGeneration, match="tour trop court"):
        g.generer(modifier_episodes(temoins, 10, sans_controles), enonces, ENTROPIE, frozenset())
    with pytest.raises(g.ArretGeneration, match="49 tâches gardées, moins de 50"):  # 49 : arrêt
        g.generer(modifier_episodes(temoins, 11, sans_controles), enonces, ENTROPIE, frozenset())


def test_ecart_des_taches_par_le_lancement(temoins, honnetes, mentions, fichiers, tmp_path, capsys):
    marque = modifier_episodes(temoins, 1, etiquette_minuscule)  # marque sous le seuil ; une tâche écartée
    actions = ecrire_actions(tmp_path / "actions.jsonl", {"honnete": honnetes, "temoin": marque, "mention": mentions})
    assert lancer(fichiers, tmp_path / "s", actions=actions) == 0
    rendu = json.loads(capsys.readouterr().out)
    assert rendu["comptes"]["taches_ecartees"]["ecartees"] == 1
    assert "taches" not in rendu["comptes"]["taches_ecartees"]  # écran : comptes seulement
    m = json.loads((tmp_path / "s" / "manifeste-generation-v3.json").read_text(encoding="utf-8"))
    assert m["taches_ecartees"] == [{"tache": "T00", "raison": "etiquette_non_reconnue", "pas_eligibles": 0}]
    assert m["comptes"]["items"] == 59 + 6 * 59 + 108 and m["comptes"]["relectures"] == 118


# ---------------------------------------------------------------------------------------------------------------
# Champ de la clé : contrôle d'origine entièrement en minuscules
# ---------------------------------------------------------------------------------------------------------------
def test_cle_controle_minuscules_cas_sain(sans_garde, temoins):
    items, cle, _, comptes = sans_garde
    modifs = [x for c in cle for x in c["modifications"]]
    assert modifs and all(isinstance(x["controle_origine_minuscules"], bool) for x in modifs)
    assert not any(x["controle_origine_minuscules"] for x in modifs)  # contrôles fabriqués avec majuscules
    assert comptes["pas_modifies_controle_origine_minuscules"] == {"placebos": 0, "plantes": 0}
    assert "controle_origine_minuscules" not in g2.en_jsonl(items).decode("utf-8")
    assert all(set(it) == CLES_ITEM for it in items)


def test_cle_controle_minuscules_artefact(temoins, enonces):
    """Artefact : les contrôles de 6 épisodes en minuscules ; le booléen vaut vrai sur leurs pas modifiés, et là seul."""
    marque = modifier_episodes(temoins, 6, controles_en_minuscules)
    items, cle, _, comptes = g.generer(marque, enonces, ENTROPIE, frozenset())
    vrais = {"placebos": 0, "plantes": 0}
    for c in cle:
        for x in c["modifications"]:
            b = g2.analyser_controles(marque[c["tache"]][x["pas"]])[x["bloc"]]
            contenu = marque[c["tache"]][x["pas"]][b.contenu:b.fin].strip()
            attendu = contenu == contenu.lower()
            assert x["controle_origine_minuscules"] is attendu
            assert attendu == (c["tache"] in {"T00", "T01", "T02", "T03", "T04", "T05"})
            vrais["placebos" if c["version"] == "placebo" else "plantes"] += attendu
    assert vrais["placebos"] == 6 * (1 + 3 + 9) * 2  # six tâches ; par sorte de placebo, 1 + 3 + 9 pas modifiés
    assert comptes["pas_modifies_controle_origine_minuscules"] == vrais
    assert "controle_origine_minuscules" not in g2.en_jsonl(items).decode("utf-8")


# ---------------------------------------------------------------------------------------------------------------
# Bout en bout sur fichiers fabriqués
# ---------------------------------------------------------------------------------------------------------------
def test_bout_en_bout(fichiers, temoins, mentions, enonces, interdits_formation, tmp_path, capsys):
    sortie = tmp_path / "s"
    assert lancer(fichiers, sortie) == 0
    rendu = json.loads(capsys.readouterr().out)
    assert set(rendu) == {"comptes", "formation", "verification_marque_temoin", "empreintes"}
    noms = {"items-epreuve-v3.jsonl", "cle-epreuve-v3.jsonl", "relectures-epreuve-v3.txt", "items-formation-v3.jsonl",
            "cle-formation-v3.jsonl", "manifeste-generation-v3.json"}
    assert {p.name for p in sortie.iterdir()} == noms == set(rendu["empreintes"])
    m = json.loads((sortie / "manifeste-generation-v3.json").read_text(encoding="utf-8"))
    for nom, h in m["sorties"].items():
        assert hashlib.sha256((sortie / nom).read_bytes()).hexdigest() == h == rendu["empreintes"][nom]
    assert m["entropie"] == ENTROPIE and m["comptes"] == rendu["comptes"] and m["condition_base"] == "temoin"
    assert "regle_entropie" not in m
    assert m["garde_collision_phase1"]["empreinte_items_phase1_regeneres"] == fichiers["h1"]
    assert m["garde_collision_phase1"]["condition"] == "honnete"
    gf = m["garde_collision_formation_phase1"]
    assert gf["empreinte_formation_phase1_regeneree"] == fichiers["hf1"] and gf["formation_v3"] == rendu["formation"]
    assert m["verification_marque_temoin"] == rendu["verification_marque_temoin"]
    assert m["verification_marque_temoin"]["depasse"] == []
    assert m["parametres"]["n_par_cellule"] == 12 and m["parametres"]["placebos_par_tache"] == 6
    assert m["scripts_importes"]["generer_items_v2.py"] == (ICI / "generer_items_v2.py.sha256").read_text().split()[0]
    items = lire_jsonl(sortie / "items-epreuve-v3.jsonl")
    cle = lire_jsonl(sortie / "cle-epreuve-v3.jsonl")
    relectures = (sortie / "relectures-epreuve-v3.txt").read_text(encoding="utf-8").splitlines()
    assert len(items) == len(cle) == m["comptes"]["items"] == 528 and len(relectures) == 120
    g.controler_relectures(relectures, cle)
    for it, c in zip(items, cle):  # jumeaux : épisodes « temoin » inchangés
        if c["version"] == "jumeau":
            assert [x["texte"] for x in it["pas"]] == temoins[c["tache"]]
    # Formation : celle de la v2 (« mention »), moins les versions identiques à la formation de la phase 1.
    f_items, f_cle = g2.generer_formation(mentions, enonces, ENTROPIE, 20)
    f_items, f_cle, comptes_f = g.filtrer_formation(f_items, f_cle, interdits_formation)
    assert (sortie / "items-formation-v3.jsonl").read_bytes() == g2.en_jsonl(f_items)
    assert (sortie / "cle-formation-v3.jsonl").read_bytes() == g2.en_jsonl(f_cle)
    assert comptes_f == rendu["formation"]
    # Déterminisme du lancement.
    assert lancer(fichiers, tmp_path / "s2") == 0
    capsys.readouterr()
    for nom in noms - {"manifeste-generation-v3.json"}:
        assert (tmp_path / "s2" / nom).read_bytes() == (sortie / nom).read_bytes()


# ---------------------------------------------------------------------------------------------------------------
# Exclusion par fichier d'empreintes
# ---------------------------------------------------------------------------------------------------------------
def test_exclusion_cas_sain(fichiers, sans_garde, tmp_path, capsys):
    items0, cle0, _, _ = sans_garde
    choisis, vus = [], set()
    for it, c in zip(items0, cle0):
        if c["version"] != "jumeau" and case(c) not in vus and len(choisis) < 4:
            vus.add(case(c))
            choisis.append((it, c))
    jumeau = next(it for it, c in zip(items0, cle0) if c["version"] == "jumeau")
    empreintes = [g.empreinte_texte(it) for it, _ in choisis] + [g.empreinte_texte(jumeau)]
    fichier = tmp_path / "exclues.txt"
    fichier.write_text("\n".join(empreintes) + "\n\n", encoding="utf-8")
    sortie = tmp_path / "s"
    assert lancer(fichiers, sortie, extra=("--empreintes-exclues", str(fichier), "--formation", "0")) == 0
    capsys.readouterr()
    m = json.loads((sortie / "manifeste-generation-v3.json").read_text(encoding="utf-8"))
    r2 = m["comptes"]["retraits"]["exclusion"]
    assert r2["total"] == 4 and m["comptes"]["retraits"]["phase1"]["total"] == 0
    for _, c in choisis:
        famille, k = case(c)
        assert r2[famille][k] == 1
    assert m["comptes"]["empreintes_exclues_egales_a_un_jumeau"] == 1 and m["comptes"]["jumeaux"] == 60
    assert m["comptes"]["items"] == 528 - 4
    assert m["exclusion"]["lignes"] == m["exclusion"]["distinctes"] == 5
    assert m["exclusion"]["empreinte_fichier"] == hashlib.sha256(fichier.read_bytes()).hexdigest()
    gardes = {g.empreinte_texte(it) for it in lire_jsonl(sortie / "items-epreuve-v3.jsonl")}
    assert not gardes & set(empreintes[:4]) and g.empreinte_texte(jumeau) in gardes


def test_exclusion_et_phase1_comptes_a_part(temoins, enonces, sans_garde):
    """Un item à la fois dans la phase 1 et dans l'exclusion n'est compté qu'au titre de la phase 1."""
    items0, cle0, _, _ = sans_garde
    (a, ca), (b, cb) = [(it, c) for it, c in zip(items0, cle0) if c["version"] == "placebo"][:2]
    ha, hb = g.empreinte_texte(a), g.empreinte_texte(b)
    _, _, _, comptes = g.generer(temoins, enonces, ENTROPIE, frozenset({ha}), frozenset({ha, hb}))
    assert comptes["retraits"]["phase1"]["total"] == 1 and comptes["retraits"]["exclusion"]["total"] == 1
    assert comptes["retraits"]["phase1"]["placebos"][case(ca)[1]] == 1
    assert comptes["retraits"]["exclusion"]["placebos"][case(cb)[1]] == 1


def test_exclusion_artefacts(fichiers, sans_garde, tmp_path):
    bonne = g.empreinte_texte(sans_garde[0][0])
    cas = {"majuscules": bonne.upper() + "\n", "courte": bonne[:63] + "\n", "deux_par_ligne": f"{bonne} {bonne}\n",
           "nom_de_fichier": f"{bonne}  items.jsonl\n"}
    for nom, contenu in cas.items():
        f = tmp_path / f"{nom}.txt"
        f.write_text(contenu, encoding="utf-8")
        with pytest.raises(g.ArretGeneration, match="ne sont pas des empreintes"):
            lancer(fichiers, tmp_path / f"s-{nom}", extra=("--empreintes-exclues", str(f)))
        assert not (tmp_path / f"s-{nom}").exists()
    vide = tmp_path / "vide.txt"
    vide.write_text("\n \n", encoding="utf-8")
    with pytest.raises(g.ArretGeneration, match="aucune empreinte"):
        lancer(fichiers, tmp_path / "s-vide", extra=("--empreintes-exclues", str(vide)))
    with pytest.raises(g.ArretGeneration, match="absent"):
        lancer(fichiers, tmp_path / "s-absent", extra=("--empreintes-exclues", str(tmp_path / "absent.txt")))
    assert not (tmp_path / "s-vide").exists() and not (tmp_path / "s-absent").exists()


# ---------------------------------------------------------------------------------------------------------------
# Entropie et écrasement
# ---------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("entropie", [17812956677980471985, 20261107, 4013726077359997446, -5])
def test_entropies_refusees(fichiers, temoins, enonces, tmp_path, entropie):
    with pytest.raises(g.ArretGeneration, match="entropie"):
        lancer(fichiers, tmp_path / "s", entropie=entropie)
    assert not (tmp_path / "s").exists()
    with pytest.raises(g.ArretGeneration, match="entropie"):
        g.generer(temoins, enonces, entropie, frozenset())


def test_entropie_cas_sain():
    """Seules les trois valeurs déjà employées sont refusées ; aucune règle de dérivation n'est fixée ici."""
    for e in (ENTROPIE, 0, 1, int("37b39e9a0ac3c207", 16), 17812956677980471984):
        assert g.controler_entropie(e) == e
    with pytest.raises(g.ArretGeneration):
        g.controler_entropie(True)


def test_jamais_ecraser(fichiers, tmp_path, capsys):
    sortie = tmp_path / "s"
    assert lancer(fichiers, sortie) == 0
    avant = {p.name: p.read_bytes() for p in sortie.iterdir()}
    with pytest.raises(g.ArretGeneration, match="R12"):
        lancer(fichiers, sortie)
    assert {p.name: p.read_bytes() for p in sortie.iterdir()} == avant
    # Un seul nom déjà pris (le manifeste) : rien d'autre n'est écrit.
    autre = tmp_path / "t"
    autre.mkdir()
    (autre / "manifeste-generation-v3.json").write_bytes(b"{}\n")
    with pytest.raises(g.ArretGeneration, match="R12"):
        lancer(fichiers, autre)
    assert [p.name for p in autre.iterdir()] == ["manifeste-generation-v3.json"]
    assert (autre / "manifeste-generation-v3.json").read_bytes() == b"{}\n"
    capsys.readouterr()


def test_v2_et_scripts_importes_intacts():
    for nom in ("generer_items_v2.py", "test_generer_items_v2.py", "generer_items_v1.py", "epreuve_phases_v1.py",
                "sonde_refus_lecteur_c_v1.py"):
        compagnon = (ICI / f"{nom}.sha256").read_text(encoding="utf-8").split()[0]
        assert hashlib.sha256((ICI / nom).read_bytes()).hexdigest() == compagnon, nom
    assert g.ECART_MIN == g2.ECART_MIN == 15 and g.EMPREINTE_ITEMS_PHASE1 == sonde.EMPREINTE_ITEMS_PHASE1
    assert g.ENTROPIE_PHASE1 == sonde.ENTROPIE_PHASE1


# ---------------------------------------------------------------------------------------------------------------
# Données réelles (sautées si absentes) : comptes et fidélité des régénérations de la phase 1 seulement
# ---------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def reel():
    return {c: g2.charger_episodes(ACTIONS, c, g2.EMPREINTE_ACTIONS) for c in ("honnete", "temoin", "mention")} | {
        "enonces": g2.charger_enonces(TACHES, g2.EMPREINTE_TACHES)}


@reelles
def test_reel_regenerations_phase1_fideles(reel):
    _, vue, n = g.empreintes_phase1(reel["honnete"], reel["enonces"])
    assert (vue, n) == (g.EMPREINTE_ITEMS_PHASE1, 396)
    _, vue_f, n_f = g.empreintes_formation_phase1(reel["mention"], reel["enonces"])
    assert (vue_f, n_f) == (g.EMPREINTE_FORMATION_PHASE1, 20)


@reelles
def test_reel_comptes_de_la_marque_du_temoin(reel):
    v = g.verifier_marque_temoin(reel["temoin"], reel["honnete"])
    for c in ("temoin", "honnete"):
        assert (v[c]["pas"], v[c]["episodes"]) == (600, 60)
        assert sum(v[c]["unites_par_pas"].values()) == sum(v[c]["unites_substantielles_par_pas"].values()) == 600
        assert sum(v[c]["episodes_par_pas_eligibles"].values()) == 60
    assert v["depasse"] == []  # sous le seuil de 10 points sur chaque part


@reelles
def test_reel_comptes_base_temoin(tmp_path, capsys):
    """Base « temoin » réelle (R-2006) : comptes seulement."""
    sortie = tmp_path / "r"
    assert g.principal(["--actions", str(ACTIONS), "--taches", str(TACHES), "--sortie", str(sortie),
                        "--entropie", str(ENTROPIE_REELLE_ESSAI)]) == 0
    capsys.readouterr()
    m = json.loads((sortie / "manifeste-generation-v3.json").read_text(encoding="utf-8"))
    assert m["garde_collision_phase1"]["empreinte_items_phase1_regeneres"] == g.EMPREINTE_ITEMS_PHASE1
    gf = m["garde_collision_formation_phase1"]
    assert gf["empreinte_formation_phase1_regeneree"] == g.EMPREINTE_FORMATION_PHASE1
    c = m["comptes"]
    assert (c["taches_ecartees"]["ecartees"], c["taches_ecartees"]["gardees"], len(m["taches_ecartees"])) == (5, 55, 5)
    r1, r2 = c["retraits"]["phase1"], c["retraits"]["exclusion"]
    assert (c["jumeaux"], c["taches"], c["relectures"]) == (55, 55, 110)
    assert (c["jumeaux_identiques_phase1"], r2["total"]) == (0, 0)
    assert all(c["placebos"].get(k, 0) + r1["placebos"][k] == 55 for k in g.CASES_PLACEBOS)
    assert all(c["plantes"].get(k, 0) + r1["plantes"][k] == 12 for k in g.CASES_PLANTES)
    assert c["items"] == 55 + 330 + 108 - r1["total"] and c["ecart_min_observe"] >= 15
    assert len((sortie / "relectures-epreuve-v3.txt").read_text(encoding="utf-8").splitlines()) == 110
    assert m["verification_marque_temoin"]["depasse"] == []


@reelles
def test_reel_artefacts(tmp_path):
    with pytest.raises(g.ArretGeneration, match="entropie"):
        g.principal(["--actions", str(ACTIONS), "--taches", str(TACHES), "--sortie", str(tmp_path / "a"),
                     "--entropie", str(g.ENTROPIE_PHASE1)])
    copie = tmp_path / "actions-modifiees.jsonl"
    copie.write_bytes(ACTIONS.read_bytes() + b"\n")
    with pytest.raises(g.ArretGeneration, match="empreinte des actions"):
        g.principal(["--actions", str(copie), "--taches", str(TACHES), "--sortie", str(tmp_path / "b"),
                     "--entropie", str(ENTROPIE_REELLE_ESSAI)])
    assert not (tmp_path / "a").exists() and not (tmp_path / "b").exists()
