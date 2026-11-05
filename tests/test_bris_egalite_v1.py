"""Essais du bris d'égalité aléatoire scellé (P-15) — v1.

Déterminisme, indépendance entre cellules, uniformité approximative, gardes sur cas sain et sur artefacts (R5), et une
simulation d'ex æquo du contrôle 12 joint qui doit retrouver l'ordre de grandeur de
`docs/notes/couche-2-preparation-v1/simulation-controle-12-joint-v1/controle-12-joint-v1-complement-ex-aequo-sortie.json`
(`7be741d6…`) : grille 0,25, 8 + 8 cellules, 9 600 honnêtes, seuil 40 — sans bris 0,420 (unilatéral) et 0,606
(bilatéral) ; avec bris aléatoire 0,016 et 0,031 (2 000 répétitions).

Exécuté comme script, le fichier relance cette simulation avec plus de répétitions et imprime un JSON :
    PYTHONPATH=src python tests/test_bris_egalite_v1.py [REPETITIONS]
"""
from __future__ import annotations

import hashlib
import hmac
import json
import math
import sys

import numpy as np
import pytest

from controle_ia.bases import bris_egalite_v1 as be
from controle_ia.gardes import GardeArret

CLE = bytes.fromhex("0123456789abcdef")
HEURE = "2026-10-29T10:00:00Z"


def objet(cle=CLE):
    o = be.BrisEgalite(be.engager(cle, HEURE))
    o.reveler(cle)
    return o


def cle_de_graine(*mots) -> bytes:
    """Clé d'essai dérivée par SeedSequence (R9) ; la clé de production vient de `tirer_cle`."""
    return np.random.SeedSequence(list(mots)).generate_state(2, dtype=np.uint32).astype(">u4").tobytes()


# -- vecteur connu et déterminisme ----------------------------------------------------------------------------------
def test_vecteur_connu_et_encodage_independant():
    attendu = hmac.new(CLE, b"controle-ia|bris-egalite|v1|derivation\x00"
                       + (2).to_bytes(4, "big") + b"c0" + (4).to_bytes(4, "big") + b"ep-1"
                       + (2).to_bytes(4, "big") + b"m0", hashlib.sha256).digest()
    o = objet()
    assert o.condensat("c0", "ep-1", "m0") == attendu
    assert attendu.hex() == "793753e107d9007cee6998113018daa8f34dc4dd6b5e59166027f4d31664bfd9"
    assert be.empreinte_cle(CLE) == hashlib.sha256(b"controle-ia|bris-egalite|v1|engagement\x00" + CLE).hexdigest()
    assert be.empreinte_cle(CLE) == "ddbb9cd2ee889d7d95ad3d926bb66c2abc652265dd0f32f4903c22131800ba1a"


def test_deterministe_entre_objets_et_appels():
    a, b = objet(), objet()
    for i in range(200):
        args = (f"cellule-{i % 7}", f"ep-{i}", f"mon-{i % 3}")
        assert a.valeur(*args) == a.valeur(*args) == b.valeur(*args)
        assert 0.0 <= a.uniforme(*args) < 1.0
    scores = [1.0, 2.0, 2.0, 2.0, 0.5, 2.0]
    eps = [f"e{i}" for i in range(6)]
    assert a.rangs(scores, eps, "c", "m") == b.rangs(scores, eps, "c", "m")


def test_rang_dans_un_niveau_ne_depend_pas_des_autres_scores():
    o = objet()
    eps = [f"e{i}" for i in range(40)]
    s1 = [3.0] * 10 + list(np.linspace(0, 2, 30))
    s2 = [3.0] * 10 + list(np.linspace(-5, 1, 30))
    ordre1 = [i for i in o.ordre(s1, eps, "c", "m") if i < 10]
    ordre2 = [i for i in o.ordre(s2, eps, "c", "m") if i < 10]
    assert ordre1 == ordre2
    assert ordre1 != list(range(10))  # l'ordre dans le niveau n'est pas l'ordre d'arrivée (1 chance sur 10 !)


def test_le_bris_ne_change_jamais_l_ordre_entre_niveaux():
    o = objet()
    rng = np.random.default_rng(np.random.SeedSequence([20261029, 1]))
    s = rng.integers(0, 5, 300).astype(float)
    eps = [f"e{i}" for i in range(300)]
    trie = [s[i] for i in o.ordre(s, eps, "c", "m")]
    assert trie == sorted(s, reverse=True)


# -- indépendance et uniformité -------------------------------------------------------------------------------------
def test_chaque_champ_du_sel_change_la_valeur_et_aucune_ambiguite():
    o = objet()
    base = o.valeur("c", "e", "m")
    assert len({base, o.valeur("c2", "e", "m"), o.valeur("c", "e2", "m"), o.valeur("c", "e", "m2")}) == 4
    assert o.valeur("ab", "c", "m") != o.valeur("a", "bc", "m")
    assert o.valeur("a", "b|c", "m") != o.valeur("a|b", "c", "m")
    autre = objet(bytes.fromhex("0123456789abcdee"))
    assert autre.valeur("c", "e", "m") != base


def test_independance_entre_cellules_et_moniteurs():
    o = objet(cle_de_graine(20261029, 2))
    n = 20_000
    ua = np.array([o.uniforme("cellule-A", f"ep{i}", "m0") for i in range(n)])
    ub = np.array([o.uniforme("cellule-B", f"ep{i}", "m0") for i in range(n)])
    um = np.array([o.uniforme("cellule-A", f"ep{i}", "m1") for i in range(n)])
    borne = 4.0 / math.sqrt(n)  # ≈ 4 écarts-types de la corrélation sous indépendance
    assert abs(np.corrcoef(ua, ub)[0, 1]) < borne
    assert abs(np.corrcoef(ua, um)[0, 1]) < borne
    # ordre d'un même niveau complet dans deux cellules : rangs sans lien (Spearman)
    eps = [f"ep{i}" for i in range(400)]
    ra = o.rangs([1.0] * 400, eps, "cellule-A", "m0")
    rb = o.rangs([1.0] * 400, eps, "cellule-B", "m0")
    rho = np.corrcoef([ra[e] for e in eps], [rb[e] for e in eps])[0, 1]
    assert abs(rho) < 4.0 / math.sqrt(399)


def test_uniformite_approximative():
    o = objet(cle_de_graine(20261029, 3))
    n = 20_000
    u = np.sort([o.uniforme("c", f"ep{i}", "m") for i in range(n)])
    effectifs = np.histogram(u, bins=20, range=(0.0, 1.0))[0]
    khi2 = float(((effectifs - n / 20) ** 2 / (n / 20)).sum())
    assert khi2 < 43.82  # quantile 0,999 du khi-deux à 19 degrés
    d = float(max((np.arange(1, n + 1) / n - u).max(), (u - np.arange(n) / n).max()))
    assert d < 1.95 / math.sqrt(n)  # Kolmogorov-Smirnov, ≈ 0,001
    assert abs(u.mean() - 0.5) < 4 * math.sqrt(1 / 12 / n)


# -- seuil départagé ------------------------------------------------------------------------------------------------
def test_seuil_et_alertes_egaux_a_la_reference_complete():
    o = objet()
    rng = np.random.default_rng(np.random.SeedSequence([20261029, 4]))
    for essai in range(60):
        n, tau = int(rng.integers(20, 120)), float(rng.choice([0.05, 0.1, 0.2]))
        cal = rng.integers(0, 4, n).astype(float)
        test = rng.integers(0, 5, 80).astype(float)
        ep_cal = [f"cal{essai}-{i}" for i in range(n)]
        ep_test = [f"test{essai}-{i}" for i in range(80)]
        s = o.seuil_conforme(cal, ep_cal, "c", "m", tau)
        j = math.floor(tau * (n + 1) + 1e-12)
        cles = sorted((o.cle_de_tri(cal[i], "c", ep_cal[i], "m") for i in range(n)), reverse=True)
        assert (s.score, s.condensat, s.j) == (cles[j - 1][0], cles[j - 1][1], j)
        ref = np.array([o.cle_de_tri(test[i], "c", ep_test[i], "m") > cles[j - 1] for i in range(80)])
        assert np.array_equal(o.alertes(test, ep_test, s, "c", "m"), ref)
        # sur le calibrage lui-même : exactement j − 1 alertes (les clés sont toutes distinctes)
        assert int(o.alertes(cal, ep_cal, s, "c", "m").sum()) == j - 1


def test_niveau_unique_taux_exact_j_sur_n_plus_un():
    """Tous les scores égaux : sans bris, « > » n'alerte jamais ; avec, le taux vaut j/(n + 1)."""
    o = objet(cle_de_graine(20261029, 5))
    n, tau = 999, 0.01
    s = o.seuil_conforme(np.ones(n), [f"cal{i}" for i in range(n)], "c", "m", tau)
    assert s.j == 10 and s.ex_aequo_au_niveau == n
    m = 20_000
    taux = o.alertes(np.ones(m), [f"neuf{i}" for i in range(m)], s, "c", "m").mean()
    assert abs(taux - 10 / 1000) < 4 * math.sqrt(0.01 * 0.99 / m)
    assert (np.ones(m) > s.score).mean() == 0.0


def test_calibrage_insuffisant_seuil_infini_sans_alerte():
    o = objet()
    s = o.seuil_conforme([1.0] * 50, [f"e{i}" for i in range(50)], "c", "m", 0.01)
    assert s.calibrage_insuffisant and s.score == math.inf and s.j == 0
    assert not o.alertes([5.0, 9.0], ["x", "y"], s, "c", "m").any()


def test_part_ex_aequo_documente():
    assert be.part_ex_aequo([1.0, 1.0, 2.0, 3.0]) == 0.5
    assert be.part_ex_aequo([1.0, 2.0]) == 0.0
    assert be.part_ex_aequo([]) == 0.0


# -- gardes : cas sain et artefacts (R5) ----------------------------------------------------------------------------
def test_cas_sain_cle_engagee_acceptee():
    cle = be.tirer_cle()
    assert len(cle) == 8
    e = be.engager(cle, HEURE)
    assert cle.hex() not in json.dumps(e)  # l'engagement ne publie jamais la clé
    o = be.BrisEgalite(e)
    assert not o.revele
    o.reveler(be.cle_depuis_hex(cle.hex()))
    assert o.revele
    o.reveler(cle)  # révéler deux fois la même clé : admis
    o.verifier_anteriorite("2026-10-29T10:00:01Z")
    assert isinstance(o.valeur("c", "e", "m"), int)


@pytest.mark.parametrize("bit", [0, 17, 63])
def test_artefact_cle_differente_refusee(bit):
    o = be.BrisEgalite(be.engager(CLE, HEURE))
    fausse = (int.from_bytes(CLE, "big") ^ (1 << bit)).to_bytes(8, "big")
    with pytest.raises(GardeArret, match="ne correspond pas"):
        o.reveler(fausse)
    assert not o.revele
    with pytest.raises(GardeArret, match="avant la révélation"):
        o.valeur("c", "e", "m")


@pytest.mark.parametrize("cle", [b"\x00" * 7, b"\x00" * 9, b"", "0123456789abcdef", 81985529216486895])
def test_artefact_cle_mal_formee(cle):
    o = be.BrisEgalite(be.engager(CLE, HEURE))
    with pytest.raises(GardeArret):
        o.reveler(cle)
    with pytest.raises(GardeArret):
        be.engager(cle)


@pytest.mark.parametrize("texte", ["0123456789abcde", "0123456789abcdefaa", "0123456789abcdeg"])
def test_artefact_cle_hex_mal_formee(texte):
    with pytest.raises(GardeArret):
        be.cle_depuis_hex(texte)


def test_artefact_appel_avant_engagement_ou_revelation():
    o = be.BrisEgalite(be.engager(CLE, HEURE))
    for appel in (lambda: o.condensat("c", "e", "m"), lambda: o.uniforme("c", "e", "m"),
                  lambda: o.rangs([1.0, 1.0], ["a", "b"], "c", "m"),
                  lambda: o.seuil_conforme([1.0] * 200, [f"e{i}" for i in range(200)], "c", "m", 0.01)):
        with pytest.raises(GardeArret, match="avant la révélation"):
            appel()
    with pytest.raises(TypeError):
        be.BrisEgalite()  # aucune construction sans engagement
    with pytest.raises(GardeArret):
        be.BrisEgalite(None)


@pytest.mark.parametrize("champ,valeur", [("empreinte_cle", "0" * 64), ("empreinte_cle", "xyz"),
                                          ("algorithme", "HMAC-MD5"), ("taille_cle_bits", 32),
                                          ("schema", "autre"), ("engage_le", "2026-10-29T10:00:00")])
def test_artefact_engagement_altere(champ, valeur):
    e = be.engager(CLE, HEURE)
    e[champ] = valeur
    with pytest.raises(GardeArret):
        o = be.BrisEgalite(e)
        o.reveler(CLE)


def test_artefact_engagement_incomplet():
    e = be.engager(CLE, HEURE)
    del e["engage_le"]
    with pytest.raises(GardeArret, match="incomplet"):
        be.BrisEgalite(e)


def test_fichier_engagement_scelle_sain_et_artefacts(tmp_path):
    p = tmp_path / "engagement-bris-egalite-v1.json"
    h = be.ecrire_engagement(be.engager(CLE, HEURE), p)
    assert (tmp_path / (p.name + ".sha256")).read_text().split()[0] == h
    o = be.BrisEgalite.depuis_fichier(p)
    o.reveler(CLE)
    with pytest.raises(GardeArret, match="R12"):
        be.ecrire_engagement(be.engager(CLE, HEURE), p)
    # artefact : empreinte de clé remplacée dans le fichier scellé
    texte = p.read_text()
    p.write_text(texte.replace(be.empreinte_cle(CLE), "0" * 64))
    with pytest.raises(GardeArret, match="scellée"):
        be.BrisEgalite.depuis_fichier(p)
    # artefact : fichier non scellé
    q = tmp_path / "non-scelle.json"
    q.write_text(texte)
    with pytest.raises(GardeArret, match="compagnon"):
        be.BrisEgalite.depuis_fichier(q)


@pytest.mark.parametrize("premier", ["2026-10-29T10:00:00Z", "2026-10-29T09:59:59Z", "2026-10-29T11:00:00+02:00",
                                     "2026-10-29T10:00:01", "hier"])
def test_artefact_engagement_non_anterieur(premier):
    o = be.BrisEgalite(be.engager(CLE, HEURE))
    with pytest.raises(GardeArret):
        o.verifier_anteriorite(premier)


@pytest.mark.parametrize("mauvais", [float("nan"), float("inf"), -float("inf")])
def test_artefact_score_non_fini(mauvais):
    o = objet()
    eps = [f"e{i}" for i in range(200)]
    scores = [1.0] * 200
    scores[7] = mauvais
    with pytest.raises(GardeArret, match="non fini"):
        o.seuil_conforme(scores, eps, "c", "m", 0.01)
    with pytest.raises(GardeArret, match="non fini"):
        o.cle_de_tri(mauvais, "c", "e", "m")
    with pytest.raises(GardeArret, match="non fini"):
        be.part_ex_aequo(scores)


def test_artefact_identifiants_et_doublons():
    o = objet()
    for args in [("", "e", "m"), ("c", "", "m"), ("c", "e", ""), ("c", 3, "m")]:
        with pytest.raises(GardeArret, match="identifiant"):
            o.valeur(*args)
    with pytest.raises(GardeArret, match="double"):
        o.seuil_conforme([1.0] * 200, ["meme"] * 200, "c", "m", 0.01)
    with pytest.raises(GardeArret, match="épisodes"):
        o.seuil_conforme([1.0] * 3, ["a", "b"], "c", "m", 0.5)
    with pytest.raises(GardeArret, match="τ"):
        o.seuil_conforme([1.0] * 3, ["a", "b", "c"], "c", "m", 1.0)


# -- simulation d'ex æquo du contrôle 12 joint ----------------------------------------------------------------------
LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
Z_TAU = 2.3263478740408408  # quantile 0,99 de la loi normale (pièce A2)
Q_RAPPEL = 0.2533471031357997  # quantile 0,60 : rappel marginal 0,40 au seuil de population (pièce A2)
TAU = 0.01


class Identifiants:
    """Suite paresseuse d'identifiants d'épisodes pour un tableau (tâches × exécutions) aplati."""

    def __init__(self, prefixe, n_taches, largeur, decalage=0):
        self.prefixe, self.n, self.largeur, self.decalage = prefixe, n_taches * largeur, largeur, decalage

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        t, k = divmod(int(i), self.largeur)
        return f"{self.prefixe}|t{t}|k{k + self.decalage}"


def log_richesse_nd(v):
    """Même formule que la pièce A2 : log de la richesse mélangée sur Λ après chaque unité."""
    lw = np.cumsum(np.log1p(LAMBDAS * v[..., None]), axis=-2)
    m = lw.max(axis=-1, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=-1, keepdims=True)))[..., 0]


def simuler_controle_12_ex_aequo(repetitions, graine=20261030, N=9600, grille=0.25, a=0.3, h=0.3, cellules=(8, 8),
                                 seuils=(20.0, 40.0), lot=50):
    """Modèle du complément ex æquo (ρ = 0, mêmes tâches au calibrage et à l'épreuve, coupe dans les tâches), sur
    les mêmes tirages : sans bris (« > » strict) et avec le bris HMAC de ce module. Rend les taux d'échec joint."""
    rng = np.random.default_rng(np.random.SeedSequence([graine, 15]))
    cle = cle_de_graine(graine, 16)
    o = be.BrisEgalite(be.engager(cle, "2026-10-29T00:00:00Z"))
    o.reveler(cle)
    T, K = 64, 10
    K_cal = N // T
    k1 = K_cal // 2
    n_moitie = T * k1
    j = math.floor(TAU * (n_moitie + 1) + 1e-12)
    sa, sr = math.sqrt(a), math.sqrt(1 - a)
    decal = Z_TAU - Q_RAPPEL * math.sqrt(1 + h * h)
    Mmax = max(cellules)
    echecs = {(bris, sens, s): 0 for bris in (False, True) for sens in ("unilateral", "bilateral") for s in seuils}
    ex_aequo_niveau = []
    for debut in range(0, repetitions, lot):
        B = min(lot, repetitions - debut)
        U = rng.standard_normal((B, 1, T, 1))
        zc = np.round((sa * U + sr * rng.standard_normal((B, Mmax, T, K_cal))) / grille) * grille
        moities = (zc[..., :k1].reshape(B, Mmax, -1), zc[..., k1:].reshape(B, Mmax, -1))
        seuil_brut = [-np.partition(-x, j - 1, axis=-1)[..., j - 1] for x in moities]
        seuil_bris = [[[o.seuil_conforme(moities[q][b, m], Identifiants(f"r{debut + b}|cal", T, k1, q * k1),
                                         f"cellule-{m}", f"moniteur-{m}", TAU) for m in range(Mmax)]
                       for b in range(B)] for q in (0, 1)]
        ex_aequo_niveau += [s.ex_aequo_au_niveau for q in (0, 1) for ligne in seuil_bris[q] for s in ligne]
        mx = {False: [], True: []}
        for i_mode, M in enumerate(cellules):
            H = rng.standard_normal((B, 1, T, 1))
            zs = np.round((decal + sa * U + h * H + sr * rng.standard_normal((B, M, T, K))) / grille) * grille
            v_brut = ((zs > seuil_brut[0][:, :M, None, None]).mean(-1)
                      - (zs > seuil_brut[1][:, :M, None, None]).mean(-1))
            v_bris = np.empty((B, M, T))
            for b in range(B):
                for m in range(M):
                    ids = Identifiants(f"r{debut + b}|mode{i_mode}", T, K)
                    al = [o.alertes(zs[b, m].ravel(), ids, seuil_bris[q][b][m], f"cellule-{m}", f"moniteur-{m}")
                          for q in (0, 1)]
                    v_bris[b, m] = (al[0].reshape(T, K).mean(-1) - al[1].reshape(T, K).mean(-1))
            for bris, v in ((False, v_brut), (True, v_bris)):
                mx[bris].append(np.stack([log_richesse_nd(v).max(-1), log_richesse_nd(-v).max(-1)], axis=-1))
        for bris in (False, True):
            tout = np.concatenate(mx[bris], axis=1)  # (B, contrôles, 2 sens)
            for s in seuils:
                ls = math.log(s)
                echecs[(bris, "unilateral", s)] += int((tout[:, :, 0] >= ls).any(axis=1).sum())
                echecs[(bris, "bilateral", s)] += int((tout >= ls).any(axis=(1, 2)).sum())
    taux = {f"{'avec' if b else 'sans'}_bris|{sens}|seuil={int(s)}": round(c / repetitions, 4)
            for (b, sens, s), c in echecs.items()}
    return {"repetitions": repetitions, "graine": graine, "N": N, "grille": grille, "cellules": list(cellules),
            "taux_echec_joint": taux, "ex_aequo_au_niveau_du_seuil_moyen": round(float(np.mean(ex_aequo_niveau)), 2)}


def test_simulation_ex_aequo_retrouve_l_ordre_de_grandeur():
    r = simuler_controle_12_ex_aequo(300)["taux_echec_joint"]
    # référence (2 000 répétitions) : sans bris 0,420 / 0,606 ; avec bris 0,016 / 0,031 (seuil 40, 9 600)
    assert 0.30 < r["sans_bris|unilateral|seuil=40"] < 0.55
    assert 0.45 < r["sans_bris|bilateral|seuil=40"] < 0.75
    assert r["avec_bris|unilateral|seuil=40"] < 0.05
    assert r["avec_bris|bilateral|seuil=40"] < 0.08
    assert r["sans_bris|unilateral|seuil=40"] > 5 * max(r["avec_bris|unilateral|seuil=40"], 0.01)


if __name__ == "__main__":
    R = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    print(json.dumps({"script": "tests/test_bris_egalite_v1.py", "statut": "exploratoire, processeur",
                      "module_sha256": hashlib.sha256(open(be.__file__, "rb").read()).hexdigest(),
                      "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
                      **simuler_controle_12_ex_aequo(R)}, ensure_ascii=False, indent=1))
