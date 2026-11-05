"""Chaîne de données de l'environnement (a) (T0.5) : API d'arXiv, règle, tirage, sources, conversion.

Hors réseau : l'ouverture des adresses est simulée. Chaque garde est testée sur un cas sain et sur un artefact (R5).
"""
from __future__ import annotations

import gzip
import io
import tarfile
import urllib.error

import pytest

from controle_ia.environnements import corpus_arxiv as ca
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines


def _entree_xml(pid="2506.00001", v=2, publie="2025-07-01", primaire="cs.LG", commentaire="Accepted at NeurIPS 2025",
                titre="A study of things", resume="We study things."):
    com = f"<arxiv:comment>{commentaire}</arxiv:comment>" if commentaire is not None else ""
    return (f"<entry><id>http://arxiv.org/abs/{pid}v{v}</id><published>{publie}T00:00:00Z</published>"
            f"<updated>{publie}T00:00:00Z</updated><title>{titre}</title><summary>{resume}</summary>{com}"
            f'<arxiv:primary_category term="{primaire}"/><category term="{primaire}"/></entry>')


def _page(total, entrees):
    return ('<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom" '
            'xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:arxiv="http://arxiv.org/schemas/atom">'
            f"<opensearch:totalResults>{total}</opensearch:totalResults>{''.join(entrees)}</feed>").encode()


def _ouvreur(pages):
    """Sert les pages dans l'ordre ; garde la trace des adresses demandées."""
    vues = []

    def ouvrir(url):
        vues.append(url)
        return pages[len(vues) - 1]

    ouvrir.vues = vues
    return ouvrir


# --- API ---------------------------------------------------------------------------------------------------

def test_lire_entrees_cas_sain():
    total, es = ca.lire_entrees(_page(1, [_entree_xml(commentaire="NeurIPS 2025 Spotlight")]))
    assert total == 1 and es[0]["id"] == "2506.00001" and es[0]["version"] == 2
    assert es[0]["categorie_principale"] == "cs.LG" and es[0]["commentaire"] == "NeurIPS 2025 Spotlight"


def test_lire_entrees_erreur_de_l_api_arrete():
    erreur = ("<entry><id>http://arxiv.org/api/errors#incorrect_id</id><title>Error</title>"
              "<summary>incorrect id format</summary></entry>")
    with pytest.raises(GardeArret, match="erreur"):
        ca.lire_entrees(_page(1, [erreur]))


def test_interroger_pagine_et_controle_le_total():
    p1 = _page(3, [_entree_xml("2506.00001"), _entree_xml("2506.00002")])
    p2 = _page(3, [_entree_xml("2506.00003")])
    ouvrir = _ouvreur([p1, p2])
    pages, es, journal = ca.interroger("q", 2, ouvrir=ouvrir, dormir=lambda s: None)
    assert [e["id"] for e in es] == ["2506.00001", "2506.00002", "2506.00003"] and len(pages) == 2
    assert "start=2" in ouvrir.vues[1] and journal == []


def test_interroger_total_change_arrete():
    p1 = _page(3, [_entree_xml("2506.00001"), _entree_xml("2506.00002")])
    p2 = _page(4, [_entree_xml("2506.00003")])
    with pytest.raises(GardeArret, match="total"):
        ca.interroger("q", 2, ouvrir=_ouvreur([p1, p2]), dormir=lambda s: None)


def test_interroger_doublons_arrete():
    p1 = _page(2, [_entree_xml("2506.00001")])
    p2 = _page(2, [_entree_xml("2506.00001")])
    with pytest.raises(GardeArret, match="distinctes"):
        ca.interroger("q", 1, ouvrir=_ouvreur([p1, p2]), dormir=lambda s: None)


def test_interroger_page_vide_relue_puis_consignee():
    p1 = _page(2, [_entree_xml("2506.00001")])
    vide = _page(2, [])
    p2 = _page(2, [_entree_xml("2506.00002")])
    pages, es, journal = ca.interroger("q", 1, ouvrir=_ouvreur([p1, vide, p2]), dormir=lambda s: None)
    assert len(es) == 2 and journal == [{"url": journal[0]["url"], "page_vide": 1}]


def test_interroger_pages_vides_repetees_arrete():
    p1 = _page(2, [_entree_xml("2506.00001")])
    vide = _page(2, [])
    with pytest.raises(GardeArret, match="page vide"):
        ca.interroger("q", 1, ouvrir=_ouvreur([p1, vide, vide, vide, vide]), dormir=lambda s: None, essais=4)


def test_reprises_sur_panne_puis_arret_sans_exclusion():
    def panne(url):
        raise urllib.error.URLError("hors ligne")

    journal = []
    with pytest.raises(GardeArret, match="tentatives"):
        ca._avec_reprises(panne, "https://x", 3, 0.0, lambda s: None, journal)
    assert len(journal) == 3


def test_reprises_laissent_passer_404():
    def absent(url):
        raise urllib.error.HTTPError(url, 404, "absent", {}, None)

    with pytest.raises(urllib.error.HTTPError):
        ca._avec_reprises(absent, "https://x", 3, 0.0, lambda s: None, [])


# --- règle -------------------------------------------------------------------------------------------------

def _e(**k):
    base = {"id": "2506.00001", "version": 1, "publie": "2025-07-01", "categorie_principale": "cs.LG",
            "commentaire": "Accepted to NeurIPS 2025", "titre": "Efficient training", "resume": "We train faster."}
    return {**base, **k}


def test_regle_cas_sain():
    assert ca.motif_exclusion(_e()) is None
    assert ca.motif_exclusion(_e(commentaire="ICLR 2026 (oral)")) is None


@pytest.mark.parametrize("champ, valeur, motif", [
    ("categorie_principale", "math.OC", "catégorie"),
    ("publie", "2025-05-31", "fenêtre"),
    ("publie", "2026-07-01", "fenêtre"),
    ("commentaire", "Accepted at ICML 2025", "sans NeurIPS"),
    ("commentaire", "NeurIPS 2025 Workshop on X", "atelier"),
    ("commentaire", "Under review at ICLR 2026", "atelier"),
    ("commentaire", "Submitted to ICLR 2026", "atelier"),
    ("titre", "Detecting deceptive agents", "sujet"),
    ("titre", "Red-teaming language models", "sujet"),
    ("resume", "We monitor training.", "sujet"),
    ("resume", "Models that lie.", "sujet"),
])
def test_regle_artefacts(champ, valeur, motif):
    assert motif in ca.motif_exclusion(_e(**{champ: valeur}))


def test_regle_mot_entier_pour_lie():
    assert ca.motif_exclusion(_e(resume="Earlier work applies.")) is None


def test_tirage_deterministe_et_permutation_des_tries():
    g = graines(["tirage-corpus"], 12345)["tirage-corpus"]
    ids = [f"2506.{k:05d}" for k in range(30)]
    o1, o2 = ca.ordre_de_tirage(ids, g), ca.ordre_de_tirage(list(reversed(ids)), g)
    assert o1 == o2 and sorted(o1) == ids and o1 != ids  # l'ordre d'entrée ne compte pas ; c'est une vraie permutation
    autre = graines(["tirage-corpus"], 12346)["tirage-corpus"]
    assert ca.ordre_de_tirage(ids, autre) != o1


def test_tirage_doublons_arrete():
    g = graines(["tirage-corpus"], 1)["tirage-corpus"]
    with pytest.raises(GardeArret):
        ca.ordre_de_tirage(["a", "a"], g)


def test_entropie_de_regle_exige_le_scellement(tmp_path):
    from controle_ia.scellement import sceller

    regle = tmp_path / "regle.md"
    regle.write_text("règle\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        ca.entropie_de_regle(regle)
    h = sceller(regle)
    assert ca.entropie_de_regle(regle) == (int(h[:32], 16), h)


# --- sources -----------------------------------------------------------------------------------------------

def _tar(fichiers: dict[str, bytes], liens: dict[str, str] | None = None) -> bytes:
    b = io.BytesIO()
    with tarfile.open(fileobj=b, mode="w") as tf:
        for nom, contenu in fichiers.items():
            ti = tarfile.TarInfo(nom)
            ti.size = len(contenu)
            tf.addfile(ti, io.BytesIO(contenu))
        for nom, cible in (liens or {}).items():
            ti = tarfile.TarInfo(nom)
            ti.type = tarfile.SYMTYPE
            ti.linkname = cible
            tf.addfile(ti)
    return b.getvalue()


def test_nature_source():
    assert ca.nature_source(b"%PDF-1.5 ...")[0] == "pdf"
    t = _tar({"a.tex": b"x"})
    assert ca.nature_source(gzip.compress(t))[0] == "tar"
    assert ca.nature_source(t)[0] == "tar"
    assert ca.nature_source(gzip.compress(b"\\documentclass{article}"))[0] == "tex-seul"
    assert ca.nature_source(b"bonjour")[0] == "inconnu"


def test_bombe_de_decompression_refusee():
    with pytest.raises(ca.SourceRefusee, match="décompressée"):
        ca._decompresser_borne(gzip.compress(b"0" * 5000), limite=1000)


def test_extraction_cas_sain_garde_les_seuls_textes(tmp_path):
    t = _tar({"main.tex": b"\\documentclass{x}", "sec/intro.tex": b"intro", "fig.png": b"\x89PNG"},
             liens={"lien.tex": "/etc/passwd"})
    info = ca.extraire_textes(t, tmp_path / "p")
    assert info["fichiers_texte"] == ["main.tex", "sec/intro.tex"] and info["fichiers_ignores"] == 1
    assert not (tmp_path / "p" / "fig.png").exists() and not (tmp_path / "p" / "lien.tex").exists()


@pytest.mark.parametrize("nom", ["../evade.tex", "/abs/evade.tex", "a/../../evade.tex"])
def test_extraction_chemin_dangereux_refuse(tmp_path, nom):
    with pytest.raises(ca.SourceRefusee, match="chemin"):
        ca.extraire_textes(_tar({nom: b"x"}), tmp_path / "p")
    assert not (tmp_path / "evade.tex").exists()


def test_extraction_exige_un_dossier_neuf(tmp_path):
    (tmp_path / "p").mkdir()
    with pytest.raises(FileExistsError):
        ca.extraire_textes(_tar({"a.tex": b"x"}), tmp_path / "p")


def test_extraction_sans_texte_refusee(tmp_path):
    with pytest.raises(ca.SourceRefusee, match="aucun fichier texte"):
        ca.extraire_textes(_tar({"fig.png": b"x"}), tmp_path / "p")


def test_retirer_commentaires():
    assert ca.retirer_commentaires("50\\% fait % commentaire\nsuite") == "50\\% fait \nsuite"


def _ecrire(d, fichiers):
    for nom, contenu in fichiers.items():
        p = d / nom
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenu, encoding="utf-8")


def test_fichier_principal(tmp_path):
    doc = "\\documentclass{article}\n\\begin{document}\nx\n\\end{document}\n"
    _ecrire(tmp_path, {"a.tex": doc, "macros.tex": "\\newcommand{\\x}{y}", "vieux.tex": "% \\documentclass{a}\n"})
    assert ca.fichier_principal(tmp_path, ["a.tex", "macros.tex", "vieux.tex"])[0] == "a.tex"
    _ecrire(tmp_path, {"main.tex": doc})
    assert ca.fichier_principal(tmp_path, ["a.tex", "main.tex"])[0] == "main.tex"
    with pytest.raises(ca.SourceRefusee, match="aucun fichier principal"):
        ca.fichier_principal(tmp_path, ["macros.tex", "vieux.tex"])


def test_aplatir_inclusions(tmp_path):
    _ecrire(tmp_path, {
        "main.tex": "\\documentclass{a}\\begin{document}\n\\input{sec/intro}\n% \\input{sec/cache}\n"
                    "\\include{sec/fin.tex}\n\\input{absent}\n\\input{../../etc/passwd}\n\\end{document}",
        "sec/intro.tex": "INTRO \\input macros", "macros.tex": "MACROS", "sec/cache.tex": "CACHE", "sec/fin.tex": "FIN"})
    texte, info = ca.aplatir(tmp_path, "main.tex")
    assert "INTRO" in texte and "MACROS" in texte and "FIN" in texte and "CACHE" not in texte
    assert info["inclus"] == ["sec/intro.tex", "macros.tex", "sec/fin.tex"]
    assert sorted(info["manquants"]) == ["../../etc/passwd", "absent"]


def test_aplatir_import_relatif(tmp_path):
    _ecrire(tmp_path, {"main.tex": "\\import{chap/}{un}", "chap/un.tex": "UN \\input{deux}", "chap/deux.tex": "DEUX"})
    texte, info = ca.aplatir(tmp_path, "main.tex")
    assert "UN" in texte and "DEUX" in texte and info["manquants"] == []


def test_aplatir_inclusion_circulaire_refusee(tmp_path):
    _ecrire(tmp_path, {"main.tex": "\\input{main}"})
    with pytest.raises(ca.SourceRefusee, match="imbriquées"):
        ca.aplatir(tmp_path, "main.tex")


def _papier(paragraphes=60):
    corps = "\n\n".join(f"Paragraph {k}: " + "learning dynamics are studied here. " * 12 for k in range(paragraphes))
    return ("\\documentclass{article}\n\\title{Essai}\n\\begin{document}\n\\maketitle\n"
            "\\begin{abstract}Un résumé.\\end{abstract}\n\\section{Intro}\n\\input{sec}\n"
            "\\begin{figure}\\includegraphics{f.png}\\caption{Légende}\\end{figure}\n\\end{document}\n"), corps


def test_traiter_papier_garde(tmp_path):
    principal, corps = _papier()
    source = gzip.compress(_tar({"main.tex": principal.encode(), "sec.tex": corps.encode(), "f.png": b"\x89PNG"}))
    filtre = tmp_path / "f.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")
    fiche = ca.traiter_papier({"id": "2506.00001", "version": 3, "titre": "Essai"}, tmp_path / "d", filtre,
                              ouvrir=lambda url: source, dormir=lambda s: None)
    assert fiche["statut"] == "gardé", fiche.get("motif")
    md = (tmp_path / "d" / "textes" / "2506.00001v3.md").read_text(encoding="utf-8")
    assert "Un résumé." in md and "title: Essai" in md and "Paragraph 59" in md
    assert "f.png" not in md and "Légende" not in md
    assert fiche["source_sha256"] == ca.sha256(source) and fiche["texte_sha256"] == ca.sha256(md.encode("utf-8"))


def test_traiter_papier_trop_court_exclu(tmp_path):
    principal, corps = _papier(paragraphes=2)
    source = gzip.compress(_tar({"main.tex": principal.encode(), "sec.tex": corps.encode()}))
    filtre = tmp_path / "f.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")
    fiche = ca.traiter_papier({"id": "2506.00002", "version": 1, "titre": "Court"}, tmp_path / "d", filtre,
                              ouvrir=lambda url: source, dormir=lambda s: None)
    assert fiche["statut"] == "exclu" and "hors de" in fiche["motif"]


def test_traiter_papier_pdf_et_404_exclus(tmp_path):
    filtre = tmp_path / "f.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")
    pdf = ca.traiter_papier({"id": "2506.00003", "version": 1, "titre": "P"}, tmp_path / "d", filtre,
                            ouvrir=lambda url: b"%PDF-1.7", dormir=lambda s: None)
    assert pdf["statut"] == "exclu" and pdf["motif"] == "source PDF seulement"

    def absent(url):
        raise urllib.error.HTTPError(url, 404, "absent", {}, None)

    f404 = ca.traiter_papier({"id": "2506.00004", "version": 1, "titre": "Q"}, tmp_path / "d", filtre,
                             ouvrir=absent, dormir=lambda s: None)
    assert f404["statut"] == "exclu" and "HTTP 404" in f404["motif"]


def test_traiter_papier_panne_reseau_arrete(tmp_path):
    def panne(url):
        raise urllib.error.HTTPError(url, 503, "indisponible", {}, None)

    filtre = tmp_path / "f.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")
    with pytest.raises(GardeArret, match="tentatives"):
        ca.traiter_papier({"id": "2506.00005", "version": 1, "titre": "R"}, tmp_path / "d", filtre,
                          ouvrir=panne, dormir=lambda s: None)


def test_constituer_s_arrete_au_besoin_et_numerote(tmp_path):
    principal, corps = _papier()
    bon = gzip.compress(_tar({"main.tex": principal.encode(), "sec.tex": corps.encode()}))
    sources = {"2506.00001": b"%PDF", "2506.00002": bon, "2506.00003": bon, "2506.00004": bon}
    entrees = {k: {"id": k, "version": 1, "titre": k} for k in sources}
    filtre = tmp_path / "f.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")

    def ouvrir(url):
        return sources[url.rsplit("/", 1)[1][:-2]]

    fiches = ca.constituer(list(sources), entrees, 2, tmp_path / "d", filtre, ouvrir=ouvrir, dormir=lambda s: None)
    assert [f["statut"] for f in fiches] == ["exclu", "gardé", "gardé"]
    assert [f.get("rang_garde") for f in fiches] == [None, 0, 1] and [f["rang_tirage"] for f in fiches] == [0, 1, 2]
