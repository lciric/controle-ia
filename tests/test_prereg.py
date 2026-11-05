import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste
from controle_ia.prereg import SECTIONS, exiger_prereg_scelle, problemes, sceller_prereg
from controle_ia.scellement import sceller


EMPREINTES_CONTRE_LECTURE = f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`"


def ecrire(chemin, remplir=True, sauf=None, contre_lecture=EMPREINTES_CONTRE_LECTURE):
    corps = ["# Préenregistrement test\n"]
    for s in SECTIONS:
        if s == sauf:
            continue
        texte = "contenu " + s + (" ; " + contre_lecture if s == "Contre-lecture" else "")
        corps.append(f"## {s}\n\n{texte if remplir else 'À REMPLIR'}\n")
    chemin.write_text("\n".join(corps), encoding="utf-8")
    return chemin


def test_contre_lecture_par_entree(tmp_path):
    """Contre-lecture 3, M-6 : chaque entrée « Contre-lecture k » cite ses deux empreintes ; des tournures légitimes
    ne sont plus refusées."""
    a, b, c = "a" * 64, "b" * 64, "c" * 64
    saine = (f"- **Contre-lecture 1** : brouillon `{a}`, rapport `{b}` ; rien à reporter dans le code.\n"
             f"- **Contre-lecture 2** : brouillon `{c}`, rapport `{a}` ; zip à venir après le verdict.")
    assert problemes(ecrire(tmp_path / "p.md", contre_lecture=saine)) == []
    for attente in ("en cours", "TODO", "A faire", "faite ; verdict scellable ; remarques intégrées"):
        texte = f"- **Contre-lecture 1** : brouillon `{a}`, rapport `{b}`.\n- **Contre-lecture 2** : {attente}."
        assert any("contre-lecture 2 sans ses deux empreintes" in x for x in problemes(ecrire(tmp_path / "p.md",
                                                                                         contre_lecture=texte)))


def test_artefact_contre_lecture_sans_empreintes(tmp_path):
    for faible in ("À compléter après la contre-lecture", f"brouillon `{'a' * 64}` seulement", f"`{'a' * 64}` et `{'a' * 64}`"):
        p = ecrire(tmp_path / "p.md", contre_lecture=faible)
        assert any("deux empreintes" in x for x in problemes(p))
        with pytest.raises(GardeArret, match="deux empreintes"):
            sceller_prereg(p)


def test_sain_prereg_conforme(tmp_path):
    p = ecrire(tmp_path / "p.md")
    assert problemes(p) == []
    h = sceller_prereg(p)
    assert exiger_prereg_scelle(p) == h


def test_artefact_gabarit_non_rempli(tmp_path):
    p = ecrire(tmp_path / "p.md", remplir=False)
    assert len(problemes(p)) == len(SECTIONS)
    with pytest.raises(GardeArret, match="R1"):
        sceller_prereg(p)


def test_artefact_section_absente(tmp_path):
    p = ecrire(tmp_path / "p.md", sauf="Liste d'arrêt")
    with pytest.raises(GardeArret, match="Liste d'arrêt"):
        sceller_prereg(p)


def test_artefact_scelle_par_contournement_mais_non_conforme(tmp_path):
    p = ecrire(tmp_path / "p.md", sauf="Contre-lecture")
    sceller(p)  # scellé sans passer par sceller_prereg
    with pytest.raises(GardeArret, match="non conforme"):
        exiger_prereg_scelle(p)


def test_artefact_prereg_modifie_apres_scellement(tmp_path):
    p = ecrire(tmp_path / "p.md")
    sceller_prereg(p)
    p.write_text(p.read_text() + "\najout tardif\n")
    with pytest.raises(GardeArret, match="empreinte"):
        exiger_prereg_scelle(p)


def test_run_decisif_rattache_au_prereg(depot):
    p = ecrire(depot / "prereg.md")
    h = sceller_prereg(p)
    committer(depot)
    _, m = creer_manifeste(depot, "20261004-120000-decisif", {}, ["t"], decisif=True, prereg=p)
    assert m["preenregistrement"]["sha256"] == h


def test_artefact_marqueur_de_gabarit_restant(tmp_path):
    """Un marqueur de substitution (<<NOM>>) oublié dans une section remplie bloque le scellement."""
    p = ecrire(tmp_path / "p.md")
    p.write_text(p.read_text(encoding="utf-8") + "\nSuite : <<CONTRE_LECTURE_2>>\n", encoding="utf-8")
    assert problemes(p) == ["marqueurs de gabarit restants : <<CONTRE_LECTURE_2>>"]
    with pytest.raises(GardeArret, match="gabarit"):
        sceller_prereg(p)
    sain = ecrire(tmp_path / "q.md")
    sain.write_text(sain.read_text(encoding="utf-8") + "\nUn chevron isolé << ou >> ne compte pas.\n", encoding="utf-8")
    assert problemes(sain) == []


def test_artefact_prereg_hors_du_depot(depot, tmp_path_factory):
    """Un préenregistrement scellé mais placé hors du dépôt arrête la création du manifeste (GardeArret)."""
    ailleurs = ecrire(tmp_path_factory.mktemp("ailleurs") / "prereg.md")
    sceller_prereg(ailleurs)
    with pytest.raises(GardeArret, match="hors du dépôt"):
        creer_manifeste(depot, "20261004-120001-decisif", {}, ["t"], decisif=True, prereg=ailleurs)
