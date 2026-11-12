"""Essai différentiel de fermeture de P3-bis (`scripts/essai_fermeture_p3bis_v1.py` ; texte de P3-bis, brouillon 6, plan,
point 6 ; corrections 1 et 2 de la relecture courte du brouillon 6), joué entier sur jouet, sur processeur : issues
substituées (« vu » contre « non vu », « non tranché », « échec ») aux sorties de classe 1 identiques, taille du paquet
comprise, longueur comprimée sous le seuil écrit ; contrôle négatif (deux passages de « vu ») ; contrôles positifs détectés
(issue imprimée, code de sortie qui dépend de l'issue, paquet non bourré, variante qui dort 60 s sous « vu » — écart de durée
de plus de 30 s —, corps non comprimé) ; second paquet (sel neuf, morceaux, relecture). Environ trois minutes."""
import importlib.util
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v1", RACINE / "scripts" / "essai_fermeture_p3bis_v1.py")
ef = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ef)


def test_essai_differentiel_de_fermeture_complet(tmp_path):
    sortie = tmp_path / "essai-fermeture-p3bis.txt"
    r = ef.essai(tmp_path / "essai", sortie)
    texte = sortie.read_text(encoding="utf-8")
    assert r["conforme"], texte
    assert texte.rstrip().endswith("ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME") and "NON CONFORME" not in texte
    for autre in ("non vu", "non tranché", "échec"):
        assert f"CONFORME — issues substituées « vu » contre « {autre} » : différences de classe 1 aucune" in texte
    for v in ef.VARIANTES:
        assert f"CONFORME — contrôle positif « {v} »" in texte
    assert "'duree_s'" in next(x for x in texte.splitlines() if "« dort »" in x)            # détectée par la durée
    assert "'zlib'" in next(x for x in texte.splitlines() if "« non-comprime »" in x)        # détectée par zlib
    assert "'taille_fixe'" in next(x for x in texte.splitlines() if "« non-bourre »" in x)
    base = r["base"]
    assert {p["taille"] for p in base.values()} == {ef.ob.TAILLE_PAQUET_LECTURES}
    assert len({p["empreinte"] for p in base.values()}) == len(base)                        # sel neuf à chaque passage
    assert max(p["zlib"] for p in base.values()) - min(p["zlib"] for p in base.values()) <= ef.SEUIL_ZLIB
    assert max(p["duree_s"] for p in base.values()) - min(p["duree_s"] for p in base.values()) < ef.SEUIL_DUREE_S


def test_essai_refuse_un_dossier_ou_une_sortie_deja_la(tmp_path):
    (tmp_path / "essai").mkdir()
    with pytest.raises(SystemExit, match="R12"):
        ef.essai(tmp_path / "essai", tmp_path / "sortie.txt")
    assert ef.main(["un seul argument"]) == 2


def test_differences_voit_chaque_sortie_de_classe_1():
    """Le comparateur lui-même (R5) : deux passages égaux ne diffèrent pas ; chaque sortie changée seule est vue."""
    p = {"code": 0, "sortie": "x", "erreurs": "", "statut": [], "publics": [], "taille": ef.ob.TAILLE_PAQUET_LECTURES,
         "zlib": 1000, "duree_s": 10.0}
    assert ef.differences(p, dict(p)) == {}
    assert ef.differences(p, dict(p, zlib=1000 + ef.SEUIL_ZLIB)) == {}                       # au seuil : admis
    assert ef.differences(p, dict(p, duree_s=10.0 + ef.SEUIL_DUREE_S)) == {}
    for cle, v in (("code", 1), ("sortie", "y"), ("erreurs", "e"), ("statut", ["?? a"]), ("publics", [("a", 1)]),
                   ("zlib", 1000 + ef.SEUIL_ZLIB + 1), ("duree_s", 10.0 + ef.SEUIL_DUREE_S + 0.01)):
        assert cle in ef.differences(p, dict(p, **{cle: v}))
    assert "taille_fixe" in ef.differences(p, dict(p, taille=10240))
