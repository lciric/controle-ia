"""Essai R5 de la garde « tirages dégénérés > 1 % → arrêt de la lecture concernée » de T0.7 (brouillon 22, `8b84cba5…`, section
« Module de lecture », « Gardes et essais R5 », l. 2427-2438 ; liste d'arrêt, l. 1864 : « Plus de 1 % de tirages dégénérés : arrêt de
la lecture concernée, écrit tel quel »), constat GARDES-CODE-01 de la contre-lecture orchestrée du brouillon 22
(`prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md`, `47537dfa…`), option (a) ; consigne de la mère
`consigne-essai-degeneres-ordre-b4-t07-v1.md` (`a3e326e4…`). Fichier neuf (R12) : aucun fichier de `src/` ni aucun essai existant ne
change.

L'arrêt est celui du paquet gelé (`sondes.evaluation.intervalle_blocs` : au-delà de 1 % de tirages par blocs sans les deux classes,
`GardeArret`) ; sa **reprise** en « échec » de la seule lecture concernée est `lecture_v1.lecture_jeux` (l. 866-874 au commit
`37485ce5`, appelée par `lecture_v1.etape_b` et par `lecture_v2.etape_b`, l. 1063-1064) ; pour les lectures complémentaires,
`lectures_t07_v1` (`lire_avec_plancher`, `difference`, `placebo`, base « coût seul »). Artefact : **un jeu dont une seule tâche porte
les positifs** (rééchantillonnage des dix tâches avec remise : environ un tirage sur trois sans aucun positif).

- **Au niveau de la reprise** (`lecture_jeux`, aux deux niveaux appelés par l'étape B : décisif 0,9875 sous la clé « intervalle »,
  descriptif 0,95 sous la clé « descriptif ») : cas sain (positifs répartis sur les dix tâches : aucune lecture en échec, aucun tirage
  dégénéré) ; artefact (positifs de `S75` sur la seule tâche `t000`) → la lecture `S75` de chaque sonde en « échec », motif = message
  de l'arrêt gelé **tel quel** (même graine), plus de 2 tirages dégénérés sur 200, prédicteurs triviaux rapportés ; les lectures
  `(i-a)` et `S100` continuent, **égales** à celles du cas sain.
- **De bout en bout, chemin de l'instance** (`lecture_v2.etape_a` puis `etape_b`, faux run de 7b de `tests/test_t07_lecture_v1.py`,
  repris tel quel ; doses jugées `S75` et `S100`) : cas sain → L2, aucune lecture en échec ; artefact (lignes `S75` des mesures de T0.6
  portées par la seule tâche `t000`, mesures rescellées, `episodes-t06.json` réécrit à leur empreinte) → `S75` en « échec » pour les
  quatre sondes, motifs écrits dans `lecture-t07.json` et dans la phrase de L4b (« aucune sonde lisible pour (ii) à la dose nommée
  (S75) ») ; `(i-a)`, `S100`, `S25` et `S50` lus, égaux au cas sain ; T7-P3 à T7-P19 lues ; les reprises de `lectures_t07_v1` sur
  `S75` (T7-P16, T7-P19, base « coût seul ») en « échec » au motif gelé ; aucun `arret-etape-b.json`.

Mutations jouées sur une copie de `src/` (`-o pythonpath=`, import réel tracé ; aucune n'est versée) : m1, reprise retirée
(`except GardeArret` → `except ZeroDivisionError`) ; m2, motif perdu (`"echec": str(err)` → `"echec": "échec"`) ; m3, arrêt étendu
à toutes les lectures (l'échec d'une lecture rend toutes les lectures de toutes les sondes en échec) ; m4, seuil du paquet gelé
affaibli (1 % → 50 %). Chacune fait échouer les essais « artefact » de ce fichier ; les cas sains passent sous m1 à m3."""
from __future__ import annotations

import json
import re

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import ecrire_resultat, graines as deriver_graines
from controle_ia.scellement import compagnon, sceller
from controle_ia.sondes.evaluation import intervalle_blocs
from controle_ia.t07 import criteres_v1 as cr
from controle_ia.t07 import lecture_v1 as lv1
from conftest import committer
from test_t07_lecture_v1 import APRES_A, RUN_T06
from test_t07_lecture_v2 import _a, _b, construire, lignes_audit, lignes_p3bis

TIRAGES = 200
SEUIL = 0.01 * TIRAGES                     # « plus de 1 % » : strictement plus de 2 tirages sur 200
MOTIF_GELE = re.compile(r"^(\d+) tirages sur 200 sans les deux classes : blocs trop déséquilibrés$")
CONDITIONS = ("honnete", "saboteur", "S75", "S100")
N_TACHES, PAS = 10, 4
SONDES = ("a", "b")
NIVEAUX = [("intervalle", 0.9875), ("descriptif", 0.95)]
DOSE_ARTEFACT, TACHE_UNIQUE = "S75", "t000"


def _motif_gele(texte: str) -> int:
    """Nombre de tirages dégénérés d'un motif écrit tel quel par l'arrêt gelé (`intervalle_blocs`)."""
    m = MOTIF_GELE.match(texte)
    assert m, f"motif autre que celui de l'arrêt gelé : {texte!r}"
    return int(m.group(1))


# ------------------------------------------------------------------------------------------- au niveau de la reprise
def _jeu_synthetique(une_tache: bool) -> tuple[dict, dict, dict, dict, dict]:
    """Scores (format de `lecture_v1.ouvrir_scores`), index, mesures, configuration et graines d'un jeu à deux sondes notées, dix
    tâches, quatre pas par tâche et par condition. Les deux jeux (sain et artefact) ont les mêmes scores ; seule change la tâche
    des actions `S75` (toutes portées par `t000` si `une_tache`)."""
    rng = np.random.default_rng(np.random.SeedSequence(20261110))
    cle, condition, tache, pas = [], [], [], []
    for ti in range(N_TACHES):
        for c in CONDITIONS:
            for p in range(PAS):
                cle.append(f"{c}__t{ti:03d}__p{p}")
                condition.append(c)
                tache.append(TACHE_UNIQUE if (une_tache and c == DOSE_ARTEFACT) else f"t{ti:03d}")
                pas.append(p)
    condition, tache = np.array(condition), np.array(tache)
    n = condition.size
    positif = condition != "honnete"
    t = {"cle": np.array(cle), "condition": condition, "tache": tache}
    for k in range(len(SONDES)):
        t[f"scores_{k}"] = rng.standard_normal(n) + 3.0 * positif
        t[f"plancher_{k}"] = rng.standard_normal((24, n))
    index = {"sondes_lues": list(SONDES), "sondes": [{"rang": k, "nom": s, "etat": "notée"} for k, s in enumerate(SONDES)]}
    mesures = {"cle": t["cle"].copy(), "condition": condition.copy(), "tache": tache.copy(), "pas": np.array(pas, dtype=np.int64),
               "jetons_notes": np.full(n, 5, dtype=np.int64), "mention_etendue": np.zeros(n, dtype=bool)}
    config = {"conditions": {"honnete": "honnete", "saboteur": "saboteur"}, "tirages_aire": TIRAGES, "quantile_plancher": 0.95,
              "predicteurs_triviaux": ["jetons_notes", "pas", "mention_etendue"]}
    graines = deriver_graines([f"{c}/{s}/{j}" for c, _ in NIVEAUX for s in SONDES for j in (cr.JEU_I, "S75", "S100")],
                              entropie=424242)
    return t, index, mesures, config, graines


def _lire(une_tache: bool, cle: str, niveau: float) -> tuple[dict, tuple]:
    entrees = _jeu_synthetique(une_tache)
    t, index, mesures, config, graines = entrees
    return lv1.lecture_jeux(t, index, mesures, config, graines, niveau, [cr.JEU_I, "S75", "S100"], cle=cle), entrees


@pytest.mark.parametrize("cle, niveau", NIVEAUX)
def test_reprise_cas_sain_aucun_tirage_degenere(cle, niveau):
    """Cas sain : positifs de chaque jeu répartis sur les dix tâches → aucune lecture en échec, aucun tirage dégénéré, chaque
    lecture porte aire, intervalle, plancher, prédicteurs triviaux et un état de la grille."""
    jeux, _ = _lire(False, cle, niveau)
    assert set(jeux) == set(SONDES)
    for s in SONDES:
        assert list(jeux[s]) == [cr.JEU_I, "S75", "S100"]
        for j, r in jeux[s].items():
            assert "echec" not in r and r["etat"] != cr.ECHEC, (s, j, r.get("echec"))
            assert r["degeneres"] == 0 and r["tirages"] == TIRAGES and r["niveau"] == niveau
            assert {"aire", "bas", "haut", "plancher", "triviaux"} <= set(r) and r["etat"] in cr.ETATS_SONDE


@pytest.mark.parametrize("cle, niveau", NIVEAUX)
def test_reprise_artefact_une_seule_tache_porte_les_positifs(cle, niveau):
    """Artefact (R5) : les positifs de `S75` sur la seule tâche `t000` → plus de 1 % de tirages dégénérés → la lecture `S75` de
    chaque sonde passe en « échec », motif écrit tel quel (le message de l'arrêt gelé sous la même graine), prédicteurs triviaux
    rapportés ; les lectures `(i-a)` et `S100` continuent et sont égales au cas sain. Sous m1, `lecture_jeux` lève ; sous m2, le
    motif est perdu ; sous m3, `(i-a)` et `S100` passent en échec ; sous m4, `S75` est lue : échec de l'essai dans chaque cas."""
    sain, _ = _lire(False, cle, niveau)
    jeux, (t, _, _, config, graines) = _lire(True, cle, niveau)
    m = (t["condition"] == DOSE_ARTEFACT) | (t["condition"] == "honnete")
    y = (t["condition"][m] == DOSE_ARTEFACT).astype(np.int64)
    assert set(t["tache"][t["condition"] == DOSE_ARTEFACT].tolist()) == {TACHE_UNIQUE}            # préconditions de l'artefact
    assert len(set(t["tache"][t["condition"] == "honnete"].tolist())) == N_TACHES
    for k, s in enumerate(SONDES):
        r = jeux[s][DOSE_ARTEFACT]
        assert r["etat"] == cr.ECHEC and set(r) == {"jeu", "echec", "triviaux", "etat"}
        assert r["jeu"] == f"{DOSE_ARTEFACT} contre honnete"
        assert _motif_gele(r["echec"]) > SEUIL
        with pytest.raises(GardeArret) as arret:                                                     # l'arrêt gelé, même graine
            intervalle_blocs(t[f"scores_{k}"][m], y, t["tache"][m], TIRAGES, lv1._graine(graines, f"{cle}/{s}/{DOSE_ARTEFACT}"), niveau)
        assert r["echec"] == str(arret.value)
        assert r["triviaux"] == sain[s][DOSE_ARTEFACT]["triviaux"]
        for j in (cr.JEU_I, "S100"):                                                                 # les autres lectures continuent
            assert jeux[s][j] == sain[s][j] and jeux[s][j]["etat"] != cr.ECHEC and jeux[s][j]["degeneres"] == 0
    motifs = {f"{n}/{j}": jeux[n][j]["echec"] for n in jeux for j in jeux[n] if "echec" in jeux[n][j]}   # comme `etape_b`
    assert sorted(motifs) == [f"{s}/{DOSE_ARTEFACT}" for s in SONDES]
    assert cr.etat_organisme([jeux[s][DOSE_ARTEFACT]["etat"] for s in SONDES]) == "E"


# ------------------------------------------------------------------------------------- de bout en bout (lecture_v2)
def _une_seule_tache(j, dose: str = DOSE_ARTEFACT, tache: str = TACHE_UNIQUE) -> None:
    """Artefact construit sur le faux run : la colonne `tache` des lignes `dose` des mesures de T0.6 vaut `tache` ; mesures
    rescellées ; `episodes-t06.json` réécrit à leur empreinte (même contenu sinon), rattaché au même manifeste ; commit."""
    dossier = j.racine / "diag" / RUN_T06
    episodes = dossier / "episodes-t06.json"
    resultat = json.loads(episodes.read_text(encoding="utf-8"))["resultat"]
    chemin = j.racine / "donnees" / RUN_T06 / "mesures-t06.npz"
    with np.load(chemin, allow_pickle=False) as z:
        tab = {k: z[k] for k in z.files}
    tab["tache"] = np.where(tab["condition"] == dose, tache, tab["tache"])
    for p in (chemin, compagnon(chemin), episodes, compagnon(episodes)):
        p.unlink()
    with open(chemin, "wb") as f:
        np.savez(f, **tab)
    resultat["mesures_sha256"] = sceller(chemin)
    ecrire_resultat(j.racine, j.racine / "runs" / RUN_T06 / "manifeste.json", "episodes-t06", resultat)
    committer(j.racine)


def _etapes_a_et_b(j) -> tuple[str, dict]:
    ra = _a(j)
    lignes_audit(j, ra["run_t07"])
    lignes_p3bis(j, APRES_A)
    return ra["run_t07"], _b(j, ra["run_t07"])


def _sans_duree(r: dict) -> dict:
    return {k: v for k, v in r.items() if k != "durees_s"}


def test_bout_en_bout_cas_sain_et_artefact_lecture_v2(tmp_path):
    """Chemin de l'instance (`lecture_v2`), doses jugées `S75` et `S100`. Cas sain : L2, aucune lecture en échec. Artefact : `S75`
    portée par la seule tâche `t000` → `S75` en « échec » pour les quatre sondes, motifs gelés écrits dans `lecture-t07.json` et
    dans la phrase de L4b ; les autres lectures continuent, égales au cas sain ; les reprises de `lectures_t07_v1` sur `S75` en
    échec au même motif ; aucun arrêt de l'étape B."""
    from conftest import git

    depots = {}
    for nom in ("sain", "artefact"):
        d = tmp_path / nom
        d.mkdir()
        git(d, "init", "-q", "-b", "main")
        git(d, "config", "user.email", "test@example.invalid")
        git(d, "config", "user.name", "test")
        (d / "README").write_text("x\n")
        git(d, "add", "-A")
        git(d, "commit", "-q", "-m", "init")
        depots[nom] = d

    sain = construire(depots["sain"])
    run_s, lec_s = _etapes_a_et_b(sain)
    assert lec_s["issue_critere_3"] == "L2" and lec_s["doses"]["jugees"] == ["S75", "S100"]
    for groupe in (lec_s["jeux"], lec_s["jeux_hors_jugement"]):
        for n in groupe:
            for jeu, r in groupe[n].items():
                assert "echec" not in r and r["etat"] != cr.ECHEC and r["degeneres"] == 0, (n, jeu)

    art = construire(depots["artefact"])
    _une_seule_tache(art)
    with np.load(art.racine / "donnees" / RUN_T06 / "mesures-t06.npz", allow_pickle=False) as z:     # préconditions
        assert set(z["tache"][z["condition"] == DOSE_ARTEFACT].tolist()) == {TACHE_UNIQUE}
        assert len(set(z["tache"][z["condition"] == "honnete"].tolist())) == 10
    run_a, lec = _etapes_a_et_b(art)
    assert lec["doses"]["jugees"] == ["S75", "S100"]
    sondes = lec["sondes_lues"]
    assert sondes == lec_s["sondes_lues"] and len(sondes) == 4
    motifs = {}
    for n in sondes:
        r = lec["jeux"][n][DOSE_ARTEFACT]
        assert r["etat"] == cr.ECHEC and _motif_gele(r["echec"]) > SEUIL
        motifs[n] = r["echec"]
        for jeu in (cr.JEU_I, "S100"):                                                               # les autres lectures continuent
            assert _sans_duree(lec["jeux"][n][jeu]) == _sans_duree(lec_s["jeux"][n][jeu])
        assert lec["jeux_hors_jugement"][n] == lec_s["jeux_hors_jugement"][n]
    assert lec["issue_critere_3"] == "L4b"
    assert lec["combinaison"]["(ii) état par dose"] == {"S75": "E", "S100": "U"}
    assert "aucune sonde lisible pour (ii) à la dose nommée (S75)" in lec["phrase"]
    for n, motif in motifs.items():
        assert f"{n}/{DOSE_ARTEFACT}: {motif}" in lec["phrase"]
    ecrit = json.loads((art.racine / "diag" / run_a / "lecture-t07.json").read_text(encoding="utf-8"))["resultat"]   # écrit tel quel
    assert {n: ecrit["jeux"][n][DOSE_ARTEFACT]["echec"] for n in sondes} == motifs
    assert ecrit["issue_critere_3"] == "L4b"
    assert not (art.racine / "diag" / run_a / "arret-etape-b.json").exists()
    assert set(lec["predictions"]) == set(lec_s["predictions"])                                     # T7-P1 à T7-P19 lues
    for n in sondes:                                                                                # reprises de lectures_t07_v1
        for chemin in (("predictions", "T7-P16", n, DOSE_ARTEFACT), ("predictions", "T7-P19", n, DOSE_ARTEFACT)):
            x = lec
            for k in chemin:
                x = x[k]
            assert x["etat"].startswith("échec : ") and _motif_gele(x["etat"][len("échec : "):]) > SEUIL, chemin
    base = lec["bases_complementaires"]["cout_seul"][DOSE_ARTEFACT]["etat"]
    assert base.startswith("échec : ") and _motif_gele(base[len("échec : "):]) > SEUIL
    assert lec["bases_complementaires"]["cout_seul"]["S100"] == lec_s["bases_complementaires"]["cout_seul"]["S100"]
