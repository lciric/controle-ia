"""Fermeture et ouverture de P3-bis (`premier_test_ia.ouverture_p3bis_v1` ; texte de P3-bis, brouillon 6, plan, points 1, 6
et 8, « Liste d'arrêt », « Ce que le code et la chaîne doivent changer », points 2 (c) et 5 ; corrections 1 et 2 de la
relecture courte du brouillon 6) : cas sains et artefacts (R5).
- Paquet des lectures : taille fixe de 16 783 360 octets, en-têtes fixes, corps comprimé puis bourré (incompressible), sel
  neuf à chaque mise en paquet, seule l'empreinte imprimée, aucun fichier en clair restant ; artefacts : contenu trop gros,
  sel absent, sel dérivé de l'entropie, paquet déjà présent, rien à fermer, relecture fausse, corps tronqué, flux altéré.
- Second paquet : morceaux, index, relecture à l'octet, épisodes exclus de git ; artefacts : sel absent, morceau trop gros,
  fichier resté en clair (poussé de force), morceau altéré, fichier du run absent, paquet déjà présent ; dépliage (chemin
  présent ou suivi : refus, rien d'écrit).
- Garde d'ouverture : chaque refus de la liste d'arrêt, chaque mode admis (chemin normal sans le fichier de T0.7, D8 ;
  branche 1 réduite ; branche 2 pleine ; « maintenir » puis « ouvrir »), réserve « écrit après la lecture fermée », journal,
  ligne de commande (code 2) ; fichier d'issue exposé (deux clés seules ; accord avec l'issue mécanique)."""
import json
import lzma
import subprocess
import zlib
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia import ouverture_p3bis_v1 as ob
from controle_ia.scellement import sceller
from controle_ia.t07 import registre_v1 as rg

RUN = "20261120-120000-p3bis-jouet"
RL, RLC = "20261120-130000-p3bis-lecture", "20261120-130100-p3bis-lc"
ESPACE = ob.ESPACE_DEFAUT
INSTANT = ob.instant_utc("2026-11-25T12:00:00Z")
DATE_PAQUET = "2026-11-12T12:00:00Z"
AVANT = "2026-11-10T10:00:00Z"


def _git(d, *args):
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout


def _depot(d: Path) -> Path:
    d.mkdir(parents=True, exist_ok=True)
    _git(d, "init", "-q", "-b", "calcul")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    (d / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "init")
    return d


def _ecrire_scelle(d: Path, chemin: str, contenu: bytes) -> str:
    p = d / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(contenu)
    return sceller(p)


def _run_fabrique(d: Path) -> dict:
    """Fichiers du run (contenus factices) : `donnees/<run>/` et les épisodes, avec leurs compagnons."""
    contenus = {f"donnees/{RUN}/{n}": f"{n} {k}".encode() * (300 + 50 * k) for k, n in enumerate(ob.DONNEES_EXIGEES)}
    contenus[f"diag/{RUN}/{ob.EPISODES}"] = json.dumps({"fiches": list(range(400))}).encode()
    for c, b in contenus.items():
        _ecrire_scelle(d, c, b)
    return contenus


def _sorties_fabriquees(d: Path, issue="vu", ligne=4) -> list[str]:
    _ecrire_scelle(d, f"runs/{RL}/manifeste.json", b'{"commande": "lecture de P3"}')
    _ecrire_scelle(d, f"diag/{RL}/lecture-p3.json", json.dumps({"resultat": {"issue": "x" * 300}}).encode())
    _ecrire_scelle(d, f"runs/{RLC}/manifeste.json", b'{"commande": "lecture complementaire"}')
    _ecrire_scelle(d, f"diag/{RLC}/lecture-p3bis.json",
                   json.dumps({"resultat": {"issue_mecanique": {"issue": issue, "ligne": ligne}}}).encode())
    (d / ESPACE).mkdir(exist_ok=True)
    (d / ESPACE / "lecture-p3.sortie").write_text('{"issue_mecanique": "..."}\n', encoding="utf-8")
    (d / ESPACE / "lecture-p3.erreurs").write_text("", encoding="utf-8")
    return ob.sorties_des_lectures(d, [RL, RLC], ESPACE)


@pytest.fixture
def clone(tmp_path):
    """Clone fermé : run fermé en second paquet (fichiers en clair retirés, comme dans un clone neuf), puis déplié."""
    d = _depot(tmp_path / "clone")
    contenus = _run_fabrique(d)
    ob.fermer_run(d, RUN, taille_morceau=4096)
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "run")
    for c in list(contenus) + [x + ".sha256" for x in contenus]:
        (d / c).unlink()
    assert not any((d / "donnees" / RUN).iterdir())
    return {"d": d, "contenus": contenus}


# ================================================================================================= paquet des lectures
def test_fermer_taille_fixe_en_tetes_fixes_corps_comprime_puis_bourre(clone, capsys):
    d = clone["d"]
    deplies = ob.deplier_run(d, RUN, ESPACE)
    chemins = _sorties_fabriquees(d)
    originaux = {c: (d / c).read_bytes() for c in chemins if not c.endswith(ob.DEPLIE)}
    sha = ob.fermer(d, RUN, [RL, RLC], ESPACE, entropie=4242)
    assert capsys.readouterr().out == sha + "\n"                                   # seule l'empreinte est imprimée
    cible = d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES
    octets = cible.read_bytes()
    assert len(octets) == ob.TAILLE_PAQUET_LECTURES == 16_783_360 == 1_639 * 10_240
    assert (d / (str(cible.relative_to(d)) + ".sha256")).is_file()
    restes = [c for c in chemins + deplies if (d / c).exists()]
    assert restes == [] and not (d / "donnees" / RUN).exists() and not (d / ESPACE).exists()   # rien en clair
    assert _git(d, "status", "--porcelain", "--untracked-files=all").split() == [
        "??", f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}", "??", f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}.sha256"]
    sel, archive = ob.relire_paquet_lectures(octets, 4242)
    fichiers = dict(ob.membres_de(archive))
    assert {c: fichiers[c] for c in originaux} == originaux
    membres = ob.membres_de(octets)
    flux, bourre = ob.decomprimer(membres[1][1], bourre_permise=True)
    assert flux == archive and len(bourre) == ob.TAILLE_CORPS_LECTURES - len(ob.comprimer(archive))
    assert len(zlib.compress(membres[1][1])) >= len(membres[1][1])               # corps incompressible de bout en bout
    # un autre contenu : mêmes en-têtes, mêmes places, même fin ; autre sel, autre empreinte
    autre = ob.paquet_lectures(ob.tar_de([("x", b"y" * 5000)], ob.tarfile.PAX_FORMAT), ob.tirer_sel())
    assert len(autre) == len(octets) and autre[:512] == octets[:512] and autre[1024:1536] == octets[1024:1536]
    assert autre[-1024:] == octets[-1024:] == bytes(1024) and autre[512:544] != octets[512:544]


def test_sel_neuf_a_chaque_mise_en_paquet(tmp_path):
    empreintes = set()
    for k in (1, 2):
        d = _depot(tmp_path / f"d{k}")
        _sorties_fabriquees(d)
        empreintes.add(ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None))
    assert len(empreintes) == 2                                                     # même contenu, deux empreintes


@pytest.mark.parametrize("artefact, motif", [
    ("trop gros", "trop grosses pour la taille fixe"), ("sel absent", "sel absent"), ("sel dérivé", "dérivé de l'entropie"),
    ("relecture fausse", "la relecture ne redonne"), ("corps tronqué", "corps de 16780799 octets")])
def test_fermer_artefacts_aucun_paquet_et_fichiers_gardes(tmp_path, monkeypatch, artefact, motif):
    d = _depot(tmp_path / "d")
    chemins = _sorties_fabriquees(d)
    if artefact == "trop gros":
        monkeypatch.setattr(ob, "TAILLE_CORPS_LECTURES", 100)
    elif artefact == "sel absent":
        monkeypatch.setattr(ob, "tirer_sel", lambda: b"")
    elif artefact == "sel dérivé":
        monkeypatch.setattr(ob, "tirer_sel", lambda: (4242).to_bytes(32, "big"))
    elif artefact == "relecture fausse":
        vraie = ob.relire_paquet_lectures
        monkeypatch.setattr(ob, "relire_paquet_lectures", lambda o, e=None: (vraie(o, e)[0], b"autre"))
    else:
        monkeypatch.setattr(ob, "tirer_bourre", lambda n: ob.secrets.token_bytes(n - 1))
    with pytest.raises(GardeArret, match=motif):
        ob.fermer(d, RUN, [RL, RLC], ESPACE, entropie=4242, imprimer=lambda x: None)
    assert not (d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES).exists()            # aucun paquet non scellé ne reste
    assert all((d / c).exists() for c in chemins)                                   # la mise en paquet se refera


def test_fermer_gardes_simples(tmp_path):
    d = _depot(tmp_path / "d")
    with pytest.raises(GardeArret, match="aucune sortie de lecture"):
        ob.fermer(d, RUN, [RL, RLC], ESPACE)
    _sorties_fabriquees(d)
    ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None)
    _sorties_fabriquees(d)
    with pytest.raises(GardeArret, match="R12"):
        ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None)


def test_relecture_du_paquet_des_lectures_refuse_les_alterations(tmp_path):
    archive = ob.tar_de([("diag/x/lecture-p3bis.json", b"{}" * 2000)], ob.tarfile.PAX_FORMAT)
    sel = ob.tirer_sel()
    octets = ob.paquet_lectures(archive, sel)
    assert ob.relire_paquet_lectures(octets) == (sel, archive)
    with pytest.raises(GardeArret, match="16783359 octets"):
        ob.relire_paquet_lectures(octets[:-1])
    altere = bytearray(octets)
    altere[1536 + len(ob.comprimer(archive)) // 2] ^= 0xFF                          # un octet au milieu du flux xz
    with pytest.raises(GardeArret, match="flux xz illisible"):
        ob.relire_paquet_lectures(bytes(altere))
    autres_noms = ob.tar_de([("sel.bin", sel), (ob.NOM_CORPS, ob.corps_lectures(archive))])
    with pytest.raises(GardeArret, match="membres"):
        ob.relire_paquet_lectures(autres_noms)
    with pytest.raises(GardeArret, match="sel nul"):
        ob.relire_paquet_lectures(ob.paquet_lectures(archive, bytes(32)))
    assert lzma.decompress(ob.comprimer(b"abc")) == b"abc"


def test_motifs_du_registre_recopies_de_t07():
    assert (ob.SHA.pattern, ob.DATE.pattern, ob.CLE.pattern, ob.FORMAT_DATE) == (rg.SHA.pattern, rg.DATE.pattern,
                                                                                 rg.CLE.pattern, rg.FORMAT_DATE)


# ================================================================================================= second paquet
def test_second_paquet_morceaux_index_relecture_et_episodes_exclus(tmp_path):
    d = _depot(tmp_path / "d")
    contenus = _run_fabrique(d)
    index = ob.fermer_run(d, RUN, taille_morceau=4096)
    assert len(index["morceaux"]) >= 2 and max(m["taille"] for m in index["morceaux"]) <= 4096
    assert index["taille"] == sum(m["taille"] for m in index["morceaux"])
    relu = ob.relire_run(d, RUN)
    attendus = ob.fichiers_du_run(d, RUN)
    assert relu == {c: (d / c).read_bytes() for c in attendus} and set(contenus) <= set(relu)
    assert f"donnees/{RUN}/{ob.SONDES_COMPLETES}" in relu and f"donnees/{RUN}/{ob.SONDES_COMPLETES}.sha256" in relu   # entier
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "run")
    ob.exiger_aucun_clair(d, RUN)                                                   # épisodes exclus, données ignorées
    suivis = _git(d, "ls-files").split()
    assert f"diag/{RUN}/{ob.INDEX_RUN}" in suivis and f"diag/{RUN}/{ob.EPISODES}" not in suivis
    _git(d, "add", "-f", f"diag/{RUN}/{ob.EPISODES}")                              # artefact : épisodes poussés de force
    with pytest.raises(GardeArret, match="suivis en clair"):
        ob.exiger_aucun_clair(d, RUN)
    _git(d, "rm", "-q", "--cached", f"diag/{RUN}/{ob.EPISODES}")
    ob.exiger_aucun_clair(d, RUN)
    _git(d, "add", "-f", f"donnees/{RUN}/scores-p3.npz")                           # artefact : données poussées de force
    with pytest.raises(GardeArret, match="suivis en clair"):
        ob.exiger_aucun_clair(d, RUN)


@pytest.mark.parametrize("artefact, motif", [("sel absent", "sel absent"), ("morceau trop gros", "hors de"),
                                             ("fichier absent", "absents ou sans compagnon"), ("relecture fausse", "relecture")])
def test_second_paquet_artefacts_rien_ne_reste(tmp_path, monkeypatch, artefact, motif):
    d = _depot(tmp_path / "d")
    _run_fabrique(d)
    taille = 4096
    if artefact == "sel absent":
        monkeypatch.setattr(ob, "tirer_sel", lambda: b"")
    elif artefact == "morceau trop gros":
        taille = ob.TAILLE_MORCEAU_MAX + 1
    elif artefact == "fichier absent":
        (d / "donnees" / RUN / "scores-p3.npz").unlink()
    else:
        vraie = ob.relire_run
        monkeypatch.setattr(ob, "relire_run", lambda r, run: {**vraie(r, run), "donnees/x": b"en trop"})
    with pytest.raises(GardeArret, match=motif):
        ob.fermer_run(d, RUN, taille_morceau=taille)
    assert not list((d / "diag" / RUN).glob(ob.PAQUET_RUN + "*")) and not (d / "diag" / RUN / ob.INDEX_RUN).exists()


def test_second_paquet_relecture_refuse_morceau_altere_ou_trop_gros(tmp_path, monkeypatch):
    d = _depot(tmp_path / "d")
    _run_fabrique(d)
    index = ob.fermer_run(d, RUN, taille_morceau=4096)
    with pytest.raises(GardeArret, match="R12"):
        ob.fermer_run(d, RUN, taille_morceau=4096)
    monkeypatch.setattr(ob, "TAILLE_MORCEAU_MAX", 1000)
    with pytest.raises(GardeArret, match="au plus 1000"):
        ob.relire_run(d, RUN)
    monkeypatch.undo()
    m = d / "diag" / RUN / index["morceaux"][0]["nom"]
    b = bytearray(m.read_bytes())
    b[-1] ^= 0xFF                                                                   # un octet du morceau changé
    m.write_bytes(bytes(b))
    with pytest.raises(GardeArret):
        ob.relire_run(d, RUN)
    vide = _depot(tmp_path / "vide")
    assert ob.fermer_run(vide, RUN, partiel=True) is None                          # arrêt du run sans aucun fichier


def test_deplier_cas_sain_puis_chemin_present_ou_suivi(clone):
    d, contenus = clone["d"], clone["contenus"]
    deplies = ob.deplier_run(d, RUN, ESPACE)
    assert deplies == list(ob.fichiers_lus(RUN)) and len(deplies) == 8              # seuls les fichiers lus sont dépliés
    assert all((d / c).read_bytes() == b for c, b in contenus.items() if c in deplies)
    assert not (d / "donnees" / RUN / ob.SONDES_COMPLETES).exists()
    assert _git(d, "status", "--porcelain", "--untracked-files=all") == ""           # exclus ou ignorés : arbre propre
    assert json.loads((d / ESPACE / ob.DEPLIE).read_text(encoding="utf-8"))["fichiers"] == deplies
    with pytest.raises(GardeArret, match="déjà suivis ou présents"):                 # artefact : chemins présents
        ob.deplier_run(d, RUN, ESPACE)
    for c in deplies:
        (d / c).unlink()
    (d / f"diag/{RUN}/{ob.EPISODES}").write_text("en clair", encoding="utf-8")
    _git(d, "add", "-f", f"diag/{RUN}/{ob.EPISODES}")
    (d / f"diag/{RUN}/{ob.EPISODES}").unlink()
    with pytest.raises(GardeArret, match="déjà suivis ou présents"):                 # artefact : chemin suivi par git
        ob.deplier_run(d, RUN, ESPACE)
    assert not (d / "donnees" / RUN / "scores-p3.npz").exists()                      # rien d'écrit


def test_lectures_fermees_depliage_refuse_n_imprime_qu_un_code(tmp_path):
    d = _depot(tmp_path / "d")
    sortie = []
    assert ob.lectures_fermees(d, RUN, RL, RLC, imprimer=sortie.append) == 1
    assert sortie == ["code dépliage du second paquet : 1"]


# ================================================================================================= garde d'ouverture
def _ligne(cle, date, chemin, sha):
    return f"| {cle} | {date} | {chemin} | {sha} |"


def _decision(d, n, decision, date):
    chemin = ob.FICHIER_DECISION.format(n=n)
    return chemin, _ecrire_scelle(d, chemin, f"# Rendez-vous de P3-bis\n\nDécision : {decision}\nDate : {date}\n".encode())


def _monter(d, *, ecrits=True, normal=True, t07_present=False, rdv=(), garde=False, scellement_t07=False, extra=(),
            date_ecrits=AVANT, date_garde="2026-11-19T10:00:00Z"):
    """Registres de la garde : écrits de T0.7 (fichiers scellés), lignes de T0.7 au registre des scellements (compagnon
    seul, ou fichier présent), décisions du rendez-vous (dates, décisions), ligne de la garde adaptée."""
    (d / "registres").mkdir(exist_ok=True)
    lignes = ["# Registre des préalables de P3-bis", ""]
    if ecrits:
        for k in ob.CLES_ECRITS:
            chemin = f"prereg/T0.7-ecrit-{k.lower()}.md"
            lignes.append(_ligne(k, date_ecrits, chemin, _ecrire_scelle(d, chemin, k.encode())))
    t07 = d / "prereg" / "T0.7-sondes-v0-v1.md"
    sha_t07 = _ecrire_scelle(d, "prereg/T0.7-sondes-v0-v1.md", b"texte scelle de T0.7 avec la garde adaptee")
    if garde:
        lignes.append(_ligne(ob.CLE_GARDE_ADAPTEE, date_garde, "prereg/T0.7-sondes-v0-v1.md", sha_t07))
    for n, (decision, date) in enumerate(rdv, start=1):
        chemin, sha = _decision(d, n, decision, date)
        lignes.append(_ligne(f"RENDEZ-VOUS-P3BIS-{n}", date, chemin, sha))
    lignes += list(extra)
    (d / ob.REGISTRE_PREALABLES).write_text("\n".join(lignes) + "\n", encoding="utf-8")
    sc = ["# Registre des scellements (T0.6, T0.7, P3-bis)", "", _ligne("SCELLEMENT-P3BIS", AVANT, "prereg/p3bis.md", "a" * 64)]
    if normal:
        for cle, nom in ((ob.SCORES_T07, "scores-actions-t07.npz"), (ob.SONDES_T07, "sondes-t07.json")):
            chemin = f"diag/t07-run/{nom}"
            sha = _ecrire_scelle(d, chemin, nom.encode())
            if not t07_present:
                (d / chemin).unlink()                                      # D8 : compagnon seul, fichier fermé de T0.7 absent
            sc.append(_ligne(cle, "2026-11-22T10:00:00Z", chemin, sha))
    if scellement_t07:
        sc.append(_ligne(ob.SCELLEMENT_T07, "2026-11-18T10:00:00Z", "prereg/T0.7-sondes-v0-v1.md", sha_t07))
    (d / ob.REGISTRE_SCELLEMENTS).write_text("\n".join(sc) + "\n", encoding="utf-8")
    return t07


@pytest.fixture
def ouvrable(clone):
    """Clone fermé dont les deux paquets sont faits (lectures fabriquées, issue « vu »)."""
    d = clone["d"]
    ob.deplier_run(d, RUN, ESPACE)
    originaux = {c: (d / c).read_bytes() for c in _sorties_fabriquees(d) if not c.endswith(ob.DEPLIE)}
    ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None)
    return {"d": d, "originaux": originaux, "contenus": clone["contenus"]}


def _ouvrir(d, mode="plein", sortie="sortie", **k):
    lignes = []
    r = ob.ouvrir(d, mode, RUN, d.parent / sortie, date_paquet=DATE_PAQUET, instant=INSTANT, imprimer=lignes.append, **k)
    return r, lignes


def test_chemin_normal_ouverture_pleine_sans_le_fichier_de_t07(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    r, lignes = _ouvrir(d)
    assert r["mode"] == "plein" and r["chemin"] == "chemin normal" and r["reserves"] == []
    s = d.parent / "sortie"
    assert {c: (s / c).read_bytes() for c in ouvrable["originaux"]} == ouvrable["originaux"]
    assert all((s / c).read_bytes() == b for c, b in ouvrable["contenus"].items())    # second paquet ouvert aussi
    journal = (d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8")
    assert journal.count("| OUVERTURE-P3BIS | 2026-11-25T12:00:00Z | plein (chemin normal) |") == 1
    assert r["paquet_lectures_sha256"] in journal and lignes[0].startswith("ouverture pleine (chemin normal)")
    with pytest.raises(GardeArret, match="R12"):                                     # dossier de sortie déjà là
        _ouvrir(d)


def test_chemin_normal_fichier_de_t07_present_verifie(ouvrable):
    d = ouvrable["d"]
    _monter(d, t07_present=True)
    assert _ouvrir(d)[0]["mode"] == "plein"
    (d / "diag/t07-run/sondes-t07.json").write_bytes(b"altere")                      # artefact : fichier présent altéré
    with pytest.raises(ob.RefusOuverture, match="ni lignes SCORES-T07 .*présent, d'empreinte"):
        _ouvrir(d, sortie="sortie-2")


def test_branche_1_reduite_et_branche_2_pleine(ouvrable):
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:30:00Z")], garde=True, scellement_t07=True)
    r, lignes = _ouvrir(d, "reduit")
    assert r["mode"] == "reduit" and r["chemin"].startswith("branche 1") and lignes[0].startswith("ouverture réduite")
    assert "remis au seul lecteur du verdict" in lignes[0] and len(lignes) == 1
    with pytest.raises(ob.RefusOuverture, match="branche 1 : ouverture réduite seulement"):
        _ouvrir(d, "plein", sortie="s2")
    # branche 2 : garde adaptée absente : ouverture pleine anticipée, nœud déclaré ; réduite refusée
    _monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:30:00Z")], garde=False, scellement_t07=True)
    with pytest.raises(ob.RefusOuverture, match="ouverture réduite demandée sans ligne GARDE-ADAPTEE-T07-P3BIS"):
        _ouvrir(d, "reduit", sortie="s3")
    r, _ = _ouvrir(d, "plein", sortie="s4")
    assert r["chemin"].startswith("branche 2") and "nœud de Lazar" in r["chemin"]
    # branche 2 aussi : garde adaptée inscrite après la décision, ou citant un autre texte que celui de SCELLEMENT-T07
    _monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:30:00Z")], garde=True, scellement_t07=True,
            date_garde="2026-11-21T10:00:00Z")
    with pytest.raises(ob.RefusOuverture, match="inscrite après la décision"):
        _ouvrir(d, "reduit", sortie="s5")
    _monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:30:00Z")], garde=True, scellement_t07=False)
    with pytest.raises(ob.RefusOuverture, match="T0.7 non scellé"):
        _ouvrir(d, "reduit", sortie="s6")


def test_maintenir_puis_ouvrir_et_chemin_normal_reduit_refuse(ouvrable):
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z"), ("ouvrir", "2026-11-23T09:00:00Z")])
    r, _ = _ouvrir(d)
    assert r["chemin"].startswith("branche 2") and [x["decision"] for x in r["decisions"]] == ["maintenir", "ouvrir"]
    _monter(d, rdv=[("maintenir", "2026-11-20T12:10:00Z")])
    r, _ = _ouvrir(d, sortie="s2")
    assert r["chemin"] == "chemin normal (rendez-vous sans objet)"
    with pytest.raises(ob.RefusOuverture, match="chemin normal : ouverture pleine seulement"):
        _ouvrir(d, "reduit", sortie="s3")


def test_ecrit_apres_la_mise_en_paquet_accepte_avec_reserve(ouvrable):
    d = ouvrable["d"]
    _monter(d, date_ecrits="2026-11-15T10:00:00Z")
    r, lignes = _ouvrir(d)
    assert len(r["reserves"]) == 3 and all("écrit après la lecture fermée" in x for x in r["reserves"])
    assert sum(x.startswith("réserve : ") for x in lignes) == 3
    assert "écrit après la lecture fermée" in (d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8")


def _remplacer(d, chemin, avant, apres):
    p = d / chemin
    texte = p.read_text(encoding="utf-8")
    assert avant in texte
    p.write_text(texte.replace(avant, apres, 1), encoding="utf-8")


REFUS = {
    "registre absent": (lambda d: (d / ob.REGISTRE_PREALABLES).unlink(), "registre des préalables .* absent"),
    "ligne absente": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, "| ECRIT-ENGAGEMENT-ETAPE-A-P3BIS |", "x"),
                      "0 ligne\\(s\\) ECRIT-ENGAGEMENT-ETAPE-A-P3BIS"),
    "ligne en double": (lambda d: (d / ob.REGISTRE_PREALABLES).write_text(
        (d / ob.REGISTRE_PREALABLES).read_text(encoding="utf-8") + [x for x in (d / ob.REGISTRE_PREALABLES).read_text(
            encoding="utf-8").splitlines() if x.startswith("| ECRIT-PERIMETRE")][0] + "\n", encoding="utf-8"),
                        "2 ligne\\(s\\) ECRIT-PERIMETRE-JEUX-P3BIS"),
    "date mal formée": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, AVANT, "2026-11-10"), "mal formée : date"),
    "colonnes": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, f"| {AVANT} |", "|"), "mal formée \\(3 colonnes"),
    "sceau faux": (lambda d: (d / "prereg/T0.7-ecrit-ecrit-perimetre-jeux-p3bis.md").write_bytes(b"autre"),
                   "compagnon .sha256 .* ≠ empreinte du fichier"),
    "compagnon absent": (lambda d: (d / "prereg/T0.7-ecrit-ecrit-lancement-relance-p3bis.md.sha256").unlink(),
                         "compagnon .sha256 absent"),
    "date postérieure": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, AVANT, "2026-11-25T12:00:00Z"),
                         "pas strictement antérieure à l'ouverture"),
    "clé inconnue": (lambda d: (d / ob.REGISTRE_PREALABLES).write_text((d / ob.REGISTRE_PREALABLES).read_text(
        encoding="utf-8") + _ligne("AUTRE-CLE-P3BIS", AVANT, "x.md", "b" * 64) + "\n", encoding="utf-8"),
                     "clé inconnue AUTRE-CLE-P3BIS"),
    "première cellule": (lambda d: (d / ob.REGISTRE_PREALABLES).write_text((d / ob.REGISTRE_PREALABLES).read_text(
        encoding="utf-8") + _ligne("écrit libre", AVANT, "x.md", "b" * 64) + "\n", encoding="utf-8"),
                         "n'a pas la forme d'une clé"),
    "ni T0.7 ni ouvrir": (lambda d: _monter(d, normal=False), "ni lignes SCORES-T07 et SONDES-T07 bien formées"),
    "maintenir": (lambda d: _monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z")]), "décision « maintenir »"),
    "ligne après ouvrir": (lambda d: _monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:10:00Z"),
                                                                    ("maintenir", "2026-11-21T12:10:00Z")]),
                           "après une décision « ouvrir »"),
    "non croissants": (lambda d: _monter(d, normal=False, rdv=[("maintenir", "2026-11-21T12:10:00Z"),
                                                                ("ouvrir", "2026-11-21T12:10:00Z")]),
                       "non strictement croissantes"),
    "non consécutifs": (lambda d: (_monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z"),
                                                                  ("ouvrir", "2026-11-21T12:10:00Z")]),
                                   _remplacer(d, ob.REGISTRE_PREALABLES, "RENDEZ-VOUS-P3BIS-2", "RENDEZ-VOUS-P3BIS-3")),
                        "numéros de rendez-vous"),
    "numéro 01": (lambda d: (_monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:10:00Z")]),
                             _remplacer(d, ob.REGISTRE_PREALABLES, "RENDEZ-VOUS-P3BIS-1", "RENDEZ-VOUS-P3BIS-01")),
                  "numéros de rendez-vous"),
    "décision avant le rendez-vous": (lambda d: _monter(d, normal=False, rdv=[("ouvrir", "2026-11-19T12:10:00Z")]),
                                      "avant le rendez-vous \\(2026-11-20T12:00:00Z\\)"),
    "décision, autre fichier": (lambda d: (_monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:10:00Z")]),
                                           _remplacer(d, ob.REGISTRE_PREALABLES, "rendez-vous-P3-bis-v1.md",
                                                      "rendez-vous-P3-bis-v2.md")),
                                "rendez-vous-P3-bis-v1.md' attendu"),
    "garde adaptée en double": (lambda d: (_monter(d, normal=False, garde=True),
                                           _remplacer(d, ob.REGISTRE_PREALABLES, "# Registre", "| GARDE-ADAPTEE-T07-P3BIS | "
                                                      f"{AVANT} | prereg/T0.7-sondes-v0-v1.md | {'c' * 64} |\n# Registre")),
                                "2 lignes GARDE-ADAPTEE-T07-P3BIS"),
    "empreinte de la ligne autre": (lambda d: _remplacer(
        d, ob.REGISTRE_PREALABLES, (d / "prereg/T0.7-ecrit-ecrit-perimetre-jeux-p3bis.md.sha256").read_text(
            encoding="utf-8").split()[0], "f" * 64), "≠ celle du registre"),
    "SCORES-T07 compagnon autre": (lambda d: (d / "diag/t07-run/scores-actions-t07.npz.sha256").write_text(
        "d" * 64 + "  scores-actions-t07.npz\n", encoding="utf-8"), "compagnon de diag/t07-run/scores-actions-t07.npz ≠"),
    "SCORES-T07 en double": (lambda d: (d / ob.REGISTRE_SCELLEMENTS).write_text((d / ob.REGISTRE_SCELLEMENTS).read_text(
        encoding="utf-8") + [x for x in (d / ob.REGISTRE_SCELLEMENTS).read_text(encoding="utf-8").splitlines()
                             if x.startswith("| SCORES-T07")][0] + "\n", encoding="utf-8"), "2 lignes SCORES-T07"),
}


@pytest.mark.parametrize("cas", sorted(REFUS))
def test_refus_de_la_garde_rien_ouvert_et_journalise(ouvrable, cas):
    d = ouvrable["d"]
    _monter(d)
    modifier, motif = REFUS[cas]
    modifier(d)
    with pytest.raises(ob.RefusOuverture, match=motif):
        _ouvrir(d)
    assert not (d.parent / "sortie").exists()                                        # rien d'ouvert
    journal = (d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8")
    assert journal.count("| REFUS-P3BIS | 2026-11-25T12:00:00Z | plein |") == 1 and "OUVERTURE-P3BIS" not in journal


def test_ligne_de_commande_code_2_sur_refus_et_0_sur_ouverture(ouvrable, capsys):
    d = ouvrable["d"]
    _monter(d, normal=False)
    args = ["ouvrir", "--racine", str(d), "--mode", "plein", "--run", RUN, "--sortie", str(d.parent / "cli"),
            "--date-paquet", DATE_PAQUET, "--instant", str(INSTANT)]
    assert ob._main(args) == 2
    assert capsys.readouterr().err.startswith("REFUS : ni lignes SCORES-T07")
    _monter(d)
    assert ob._main(args) == 0 and (d.parent / "cli" / "diag" / RLC / "lecture-p3bis.json").is_file()
    with pytest.raises(ob.RefusOuverture, match="date de la mise en paquet illisible"):   # ni --date-paquet ni commit
        ob.ouvrir(d, "plein", RUN, d.parent / "cli-2", instant=INSTANT, imprimer=lambda x: None)


# ================================================================================================= fichier d'issue
def _issue(d, **doc):
    base = {"issue": "vu", "ligne": 4, "verdict": ob.VERDICT, "verdict_sha256": "e" * 64}
    base.update(doc)
    p = d / "docs" / "verdicts" / "verdict-P3-bis-v1-issue.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    for f in (p, Path(str(p) + ".sha256")):
        f.unlink(missing_ok=True)
    p.write_text(json.dumps({k: v for k, v in base.items() if v is not None}), encoding="utf-8")
    sceller(p)
    return p


def test_exposer_issue_deux_valeurs_seules_et_accord(tmp_path, capsys):
    lc = tmp_path / "lecture-p3bis.json"
    lc.write_text(json.dumps({"resultat": {"issue_mecanique": {"issue": "vu", "ligne": 4}}}), encoding="utf-8")
    p = _issue(tmp_path)
    assert ob.exposer_issue(p, lc) == {"issue": "vu", "ligne": 4}
    assert ob._main(["exposer-issue", str(p)]) == 0
    assert json.loads(capsys.readouterr().out) == {"issue": "vu", "ligne": 4}
    for doc, motif in (({"ligne": 5}, "hors de la table"), ({"issue": "peut-être"}, "hors de la table"),
                       ({"ligne": True}, "hors de la table"), ({"verdict": "autre.md"}, "hors de forme"),
                       ({"verdict_sha256": "E" * 64}, "hors de forme"), ({"verdict": None}, "clés")):
        with pytest.raises(GardeArret, match=motif):
            ob.exposer_issue(_issue(tmp_path, **doc))
    p = _issue(tmp_path, issue="non vu", ligne=5)
    with pytest.raises(GardeArret, match="désaccord .* nœud de Lazar"):
        ob.exposer_issue(p, lc)
    q = tmp_path / "en-trop.json"
    q.write_text(json.dumps({"issue": "vu", "ligne": 4, "verdict": ob.VERDICT, "verdict_sha256": "e" * 64, "x": 1}),
                 encoding="utf-8")
    sceller(q)
    with pytest.raises(GardeArret, match="clés"):
        ob.exposer_issue(q)
    (Path(str(p) + ".sha256")).unlink()
    with pytest.raises(GardeArret, match="compagnon"):
        ob.exposer_issue(p)
