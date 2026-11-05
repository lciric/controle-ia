"""Gardes de P3 que la contre-lecture R2 du texte et du code dit jamais déclenchées (constat TC-11,
`prereg/contre-lectures/P3-premier-test-v1-relecture-texte-code-v1.md`) : un test par garde, cas sain et artefact (R5).
Modèle jouet et tokeniseur par caractères ; fichiers dans des dossiers jetables. S'y ajoutent deux points que le même
constat dit non testés : les mêmes graines d'action d'une condition à l'autre pour une tâche, et le plan de la garde
d'identité (une action contrôlée par lot, Mahalanobis sur les premiers lots seulement)."""
import json
import shutil
import subprocess
import time

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import SENTINELLE, FormatBrut, FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.harnais.sondes import SondeLineaire
from controle_ia.manifeste import ecrire_resultat, graines
from controle_ia.premier_test_ia import donnees as dn
from controle_ia.premier_test_ia import empans as em
from controle_ia.premier_test_ia import entrainement as en
from controle_ia.premier_test_ia import figees as fg
from controle_ia.premier_test_ia import lecture as lp
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.notation import Notation
from controle_ia.scellement import empreinte, sceller

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FINS = {TOK.convert_tokens_to_ids("<|im_end|>"), TOK.eos_token_id}
FMT = FormatChat(TOK, fins=FINS)
D = 6


class FormatAltere(FormatChat):
    """Format jouet dont le rendu complet est faussé d'une façon choisie (artefacts des gardes des empans)."""

    def __init__(self, faute: str):
        super().__init__(TOK, fins=FINS)
        self.faute = faute

    def rendre(self, messages, invite):
        m = [dict(x) for x in messages]
        dernier = m[-1]
        if self.faute == "sentinelle-absente" and dernier["role"] == "user" and dernier["content"] == SENTINELLE:
            dernier["content"] = "x"
        elif self.faute == "sentinelle-repetee" and dernier["role"] == "user" and dernier["content"] == SENTINELLE:
            dernier["content"] = SENTINELLE + " " + SENTINELLE
        r = super().rendre(m, invite)
        if self.faute == "rendu-reponse" and dernier["role"] == "assistant" and dernier["content"] != SENTINELLE:
            r = r + [r[-1]]                 # le rendu de la réponse imposée n'est plus celui des pièces
        if self.faute == "rendu-utilisateur" and dernier["role"] == "user" and dernier["content"] not in (SENTINELLE, "x"):
            r = r + [r[-1]]                 # le rendu du texte utilisateur n'est plus celui des pièces
        return r


# --- empans : réponse imposée, message utilisateur, format de dialogue exigé

def test_reponse_forcee_cas_sain_et_artefacts():
    r = em.jetons_reponse_forcee(FMT, "", "Pretend.", "The sky is blue.")
    assert r["fin"] - r["debut"] == len("The sky is blue.") - 5
    with pytest.raises(GardeArret, match="réponse imposée vide"):
        em.jetons_reponse_forcee(FMT, "", "Pretend.", "   ")
    with pytest.raises(GardeArret, match="identifiants ≠ rendu complet du gabarit"):
        em.jetons_reponse_forcee(FormatAltere("rendu-reponse"), "", "Pretend.", "The sky is blue.")


def test_message_utilisateur_cas_sain_et_artefacts():
    u = em.jetons_message_utilisateur(FMT, "", "hello world", 4)
    assert u["fin"] - u["debut"] == 4
    with pytest.raises(GardeArret, match="texte utilisateur vide"):
        em.jetons_message_utilisateur(FMT, "", "  \n ", 4)
    with pytest.raises(GardeArret, match="max_jetons < 1"):
        em.jetons_message_utilisateur(FMT, "", "hello world", 0)
    for faute in ("sentinelle-absente", "sentinelle-repetee"):
        with pytest.raises(GardeArret, match="sentinelle introuvable ou répétée"):
            em.jetons_message_utilisateur(FormatAltere(faute), "", "hello world", 4)
    with pytest.raises(GardeArret, match="message utilisateur : identifiants ≠ rendu complet du gabarit"):
        em.jetons_message_utilisateur(FormatAltere("rendu-utilisateur"), "", "hello world", 4)


def test_format_de_dialogue_exige():
    em._exiger_chat(FMT)                                        # cas sain : FormatChat
    for f in (em.jetons_reponse_forcee, em.jetons_message_utilisateur):
        with pytest.raises(GardeArret, match="format de dialogue"):
            f(FormatBrut(TOK), "", "Pretend.", "The sky is blue.")


# --- extraction et entraînement : empan hors des positions, activation non finie, échéances

def _modele():
    return modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)


def test_extraire_cas_sain_et_artefacts(monkeypatch):
    modele = _modele()
    ex = en.preparer_enjeux(FMT, [{"texte": "aaaa bbbb cccc", "y": 1, "groupe": "g0"}], 8)
    sain = en.extraire(modele, ex, [0, 2])
    assert sain[0][0].shape == (8, 32) and np.all(np.isfinite(sain[2][0]))
    hors = [dict(ex[0], fin=len(ex[0]["ids"]) + 3)]
    with pytest.raises(GardeArret, match="hors des"):
        en.extraire(modele, hors, [0, 2])
    with pytest.raises(GardeArret, match="limite de durée dépassée pendant l'extraction"):
        en.extraire(modele, ex, [0, 2], echeance=time.perf_counter() - 1.0)
    vraie = en.passe_unique

    def avec_nan(m, ids, couches):
        acts = vraie(m, ids, couches)
        acts[couches[0]] = np.full_like(acts[couches[0]], np.nan)
        return acts

    monkeypatch.setattr(en, "passe_unique", avec_nan)
    with pytest.raises(GardeArret, match="activation non finie"):
        en.extraire(modele, ex, [0, 2])


def test_echeance_cas_sain_et_artefact():
    en._echeance(None, "essai")
    en._echeance(time.perf_counter() + 3600.0, "essai")
    with pytest.raises(GardeArret, match="limite de durée dépassée pendant essai"):
        en._echeance(time.perf_counter() - 1.0, "essai")


def test_budget_de_l_entrainement_cas_sain_et_artefact():
    rng = np.random.default_rng(4)
    seqs = {0: [rng.standard_normal((4, D)) + (k % 2) for k in range(20)]}
    y = [k % 2 for k in range(20)]
    graines_s = {f"tromperie-{f}-c0": 1 for f in en.FAMILLES_P3}
    r = en.entrainer_concept("tromperie", seqs, y, list(range(16)), list(range(16, 20)), [0], graines_s,
                             echeance=time.perf_counter() + 3600.0)
    assert len(r["sondes"]) == len(en.FAMILLES_P3)
    with pytest.raises(GardeArret, match="limite de durée dépassée pendant l'entraînement de tromperie-difference_moyennes-c0"):
        en.entrainer_concept("tromperie", seqs, y, list(range(16)), list(range(16, 20)), [0], graines_s,
                             echeance=time.perf_counter() - 1.0)


# --- lanceur : couches et sondes principales de la notation, citations, format de l'agent, configuration

def _config(tmp_path):
    from test_premier_test_ia_run import _config as config_jouet

    return config_jouet(tmp_path)


def _sondes(couches=(0, 2), largeur=32):
    rng = np.random.default_rng(1)
    return [SondeLineaire(f"s{c}", c, rng.standard_normal(largeur), 0.0, "max") for c in couches]


class _Passe(Exception):
    """Levée juste après les gardes d'entrée de `jouer_p3` : elles ont laissé passer (cas sain)."""


def test_jouer_p3_gardes_d_entree(tmp_path, monkeypatch):
    c = _config(tmp_path)
    sondes_hors = _sondes((0, 3))
    with pytest.raises(GardeArret, match="activations lues aux couches"):
        rp.jouer_p3(None, FMT, [], {}, c, {}, Notation(sondes_hors), ["s0"])
    with pytest.raises(GardeArret, match="absentes de la notation"):
        rp.jouer_p3(None, FMT, [], {}, c, {}, Notation(_sondes()), ["absente"])

    def passe(*a, **k):
        raise _Passe()

    monkeypatch.setattr(rp, "charger_invite", passe)
    with pytest.raises(_Passe):
        rp.jouer_p3(None, FMT, [], {}, c, {}, Notation(_sondes()), ["s0", "s2"])


def _prereg_p3(tmp_path, texte):
    p = tmp_path / "p3.md"
    p.write_text(texte, encoding="utf-8")
    return p


def test_citations_p3_cas_sain_et_artefacts(tmp_path):
    c = _config(tmp_path)
    cfg, taches = f"- Configuration de P3 (empreinte canonique) : `{rp.empreinte_config(c)}`", f"- Tâches de P3 : `{'c' * 64}`"
    ent = "- Entropie : `4242`"
    assert rp.exiger_citations_p3(_prereg_p3(tmp_path, "\n".join([cfg, taches, ent])), c, "c" * 64) == 4242
    for absente in (cfg, taches, ent):
        texte = "\n".join(x for x in (cfg, taches, ent) if x != absente)
        with pytest.raises(GardeArret, match="ne cite pas la configuration, les tâches ou l'entropie de P3"):
            rp.exiger_citations_p3(_prereg_p3(tmp_path, texte), c, "c" * 64)


def test_format_de_l_agent_en_mode_reel():
    sain = rp.controler_format_agent(FMT, {"nom": "agent-jouet"}, "jouet")
    assert sain["verifie"] is True and sain["texte_attendu_ouverture"] is None
    reel = rp.controler_format_agent(FMT, {"texte_attendu_ouverture": "You are an expert ML researcher"}, "reel")
    assert reel["verifie"] is True
    with pytest.raises(GardeArret, match="texte attendu dans l'ouverture absent de la configuration"):
        rp.controler_format_agent(FMT, {"nom": "agent-jouet"}, "reel")
    with pytest.raises(GardeArret, match="ouverture sans"):
        rp.controler_format_agent(FMT, {"texte_attendu_ouverture": "Today Date: 26 Jul 2024"}, "reel")


def test_configuration_de_p3_mode_et_durees(tmp_path):
    c = _config(tmp_path)
    rp.exiger_config_p3(c)
    with pytest.raises(GardeArret, match="mode 'autre' inconnu"):
        rp.exiger_config_p3(dict(c, mode="autre"))
    for cle in ("duree_max_s", "budget_entrainement_s"):
        for v in (0, -5, rp.DUREE_MAX_S + 1, True, "900"):
            with pytest.raises(GardeArret, match=f"{cle} .* un nombre dans"):
                rp.exiger_config_p3(dict(c, **{cle: v}))
        rp.exiger_config_p3(dict(c, **{cle: rp.DUREE_MAX_S}))


# --- sondes figées : écriture (noms en double, classe non sérialisable) et relecture (empreinte, classe)

class _Inconnue:
    nom, couche, agregation = "inconnue", 0, "max"


def test_ecrire_sondes_cas_sain_et_artefacts(tmp_path):
    sha = fg.ecrire_sondes(tmp_path / "sain.npz", _sondes(), {"essai": 1})
    assert sha == empreinte(tmp_path / "sain.npz")
    with pytest.raises(GardeArret, match="noms en double"):
        fg.ecrire_sondes(tmp_path / "double.npz", _sondes() + _sondes()[:1], {})
    with pytest.raises(GardeArret, match="classe _Inconnue non sérialisable"):
        fg.ecrire_sondes(tmp_path / "inconnue.npz", [_Inconnue()], {})
    assert not (tmp_path / "double.npz").exists() and not (tmp_path / "inconnue.npz").exists()


def _index_change(chemin, change):
    """Réécrit l'index du fichier des sondes par `change`, garde les tableaux, et rescelle (le sceau ne voit rien)."""
    with np.load(chemin, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    index = json.loads(bytes(t["index"]).decode("utf-8"))
    change(index)
    t["index"] = np.frombuffer(json.dumps(index, ensure_ascii=False, sort_keys=True).encode("utf-8"), dtype=np.uint8)
    with open(chemin, "wb") as f:
        np.savez(f, **t)
    (chemin.parent / (chemin.name + ".sha256")).write_text(f"{empreinte(chemin)}  {chemin.name}\n", encoding="utf-8")


def test_lire_sondes_cas_sain_et_artefacts(tmp_path):
    sondes = _sondes()
    for nom in ("sain.npz", "empreinte.npz", "classe.npz"):
        fg.ecrire_sondes(tmp_path / nom, sondes, {})
    relues, _, _ = fg.lire_sondes(tmp_path / "sain.npz")
    assert [s.empreinte() for s in relues] == [s.empreinte() for s in sondes]
    _index_change(tmp_path / "empreinte.npz", lambda i: i["sondes"][0].__setitem__("empreinte", "0" * 64))
    with pytest.raises(GardeArret, match="empreinte reconstruite ≠ empreinte écrite"):
        fg.lire_sondes(tmp_path / "empreinte.npz")
    _index_change(tmp_path / "classe.npz", lambda i: i["sondes"][1].__setitem__("classe", "Autre"))
    with pytest.raises(GardeArret, match="classe 'Autre' inconnue"):
        fg.lire_sondes(tmp_path / "classe.npz")


# --- notation : attention sans requête, score non fini

def test_notation_attention_sans_requete_et_score_non_fini():
    rng = np.random.default_rng(2)
    sain = Notation([SondeLineaire("a", 0, rng.standard_normal(D), 0.0, "attention", rng.standard_normal(D))])
    assert np.isfinite(sain.noter({0: rng.standard_normal((3, D))})["a"])
    with pytest.raises(GardeArret, match="sonde linéaire à attention sans requête q"):
        Notation([SondeLineaire("a", 0, rng.standard_normal(D), 0.0, "attention", None)])
    geante = Notation([SondeLineaire("g", 0, np.full(D, 1e200), 0.0, "max")])
    assert np.isfinite(geante.noter({0: np.ones((2, D))})["g"])
    with pytest.raises(GardeArret, match="notation : score non fini"):
        geante.noter({0: np.full((2, D), 1e200)})


# --- données génériques : colonnes, affirmation vide, compte, empreinte ; découpage

def _csv(tmp_path, nom, texte):
    f = tmp_path / nom
    f.write_text(texte, encoding="utf-8")
    sceller(f)
    return f


def test_charger_faits_cas_sain_et_artefacts(tmp_path):
    sain = _csv(tmp_path, "sain.csv", "statement,label\nThe sky is blue.,1\nThe sky is green.,0\nWater is wet.,1\n")
    assert dn.charger_faits(sain, None, 2) == ["The sky is blue.", "Water is wet."]
    with pytest.raises(GardeArret, match="colonnes « statement » et « label » attendues"):
        dn.charger_faits(_csv(tmp_path, "colonnes.csv", "text,label\nThe sky is blue.,1\n"), None, None)
    with pytest.raises(GardeArret, match="affirmation vide"):
        dn.charger_faits(_csv(tmp_path, "vide.csv", 'statement,label\n"  ",1\nWater is wet.,1\n'), None, None)
    with pytest.raises(GardeArret, match="2 affirmations vraies, 3 attendues"):
        dn.charger_faits(sain, None, 3)
    with pytest.raises(GardeArret, match="R11"):
        dn.charger_faits(sain, "0" * 64, 2)


def test_decouper_cas_sain_et_artefacts():
    groupes = [f"g{k // 2}" for k in range(20)]
    idx_e, idx_v = dn.decouper(groupes, np.random.default_rng(0), 0.8)
    assert not {groupes[i] for i in idx_e} & {groupes[i] for i in idx_v} and len(idx_e) + len(idx_v) == 20
    for part in (0.0, 1.0, -0.1, 1.5):
        with pytest.raises(GardeArret, match="part d'entraînement dans ]0, 1\\[ attendue"):
            dn.decouper(groupes, np.random.default_rng(0), part)
    with pytest.raises(GardeArret, match="au moins deux groupes"):
        dn.decouper(["g0"] * 4, np.random.default_rng(0), 0.8)


# --- lecture : effet du coût, autre garde repropagée ; source du run (arrêt présent, empreinte du résumé)

def test_effet_ou_non_calculable_repropage_les_autres_gardes():
    rng = np.random.default_rng(3)
    a = {f"t{k}": [10.0 * (k + 1), 20.0] for k in range(5)}
    b = {f"t{k}": [5.0 * (k + 1), 10.0] for k in range(5)}
    assert lp.effet_ou_non_calculable(a, b, rng)["calculable"] is True
    nc = lp.effet_ou_non_calculable({"t0": [10.0], "t1": [None]}, {"t0": [5.0], "t1": [5.0]}, rng)
    assert nc["calculable"] is False and "tâches lisibles dans les deux conditions" in nc["motif"]
    with pytest.raises(GardeArret, match="ne portent pas sur les mêmes tâches"):
        lp.effet_ou_non_calculable(a, {"autre": [1.0]}, rng)


@pytest.fixture(scope="module")
def run_jouet(tmp_path_factory):
    """Un run jouet de P3, complet, dans un dépôt jetable (entropie fixée, comme les tests du lanceur)."""
    from test_premier_test_ia_run import _taches

    racine = tmp_path_factory.mktemp("run-jouet")
    depot = racine / "depot"
    depot.mkdir()
    for args in (["init", "-q", "-b", "main"], ["config", "user.email", "t@example.invalid"], ["config", "user.name", "t"],
                 ["config", "commit.gpgsign", "false"]):
        subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True)
    (depot / "README").write_text("x\n")
    f = _taches(depot)
    subprocess.run(["git", "-C", str(depot), "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(depot), "commit", "-q", "-m", "init"], check=True, capture_output=True)
    config = _config(racine)
    vraie = rp.creer_manifeste
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(rp, "creer_manifeste", lambda *a, entropie=None, **k: vraie(*a, entropie=entropie or 20261019, **k))
        rp.executer(config, depot, "20261019-090000-p3-jouet", None, str(f), autoriser_depot_sale=True)
    return {"depot": depot, "config": config, "run": "20261019-090000-p3-jouet"}


def _copie_du_run(run_jouet, tmp_path):
    d = tmp_path / "copie"
    shutil.copytree(run_jouet["depot"], d, ignore=shutil.ignore_patterns(".git"))
    return d


def test_charger_source_arret_present(run_jouet, tmp_path):
    d = _copie_du_run(run_jouet, tmp_path)
    run = run_jouet["run"]
    assert lp.charger_source(d, run)["resume"]["episodes"] == 8                      # cas sain
    ecrire_resultat(d, d / "runs" / run / "manifeste.json", "arret", {"etape": "essai", "motif": "essai"})
    with pytest.raises(GardeArret, match="arret.json présent à côté du résumé"):
        lp.charger_source(d, run)


def test_charger_source_empreinte_du_resume_autre(run_jouet, tmp_path):
    d = _copie_du_run(run_jouet, tmp_path)
    run = run_jouet["run"]
    f = d / "diag" / run / "resume.json"
    corps = json.loads(f.read_text(encoding="utf-8"))
    corps["resultat"]["scores_sha256"] = "0" * 64                  # résumé rattaché au même manifeste, rescellé
    f.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    (d / "diag" / run / "resume.json.sha256").write_text(f"{empreinte(f)}  resume.json\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte ≠ celle des résultats du run"):
        lp.charger_source(d, run)


def test_plan_de_la_garde_d_identite(run_jouet):
    """Une entrée par lot ; l'action contrôlée est la première action notable du premier épisode du lot (à défaut, du
    lot) ; Mahalanobis contrôlé sur les `lots_mahalanobis_identite` premiers lots seulement."""
    d, run, c = run_jouet["depot"], run_jouet["run"], run_jouet["config"]
    epi = json.loads((d / "diag" / run / "episodes-p3.json").read_text(encoding="utf-8"))["resultat"]
    with np.load(d / "donnees" / run / "scores-p3.npz", allow_pickle=False) as z:
        notees = np.all(np.isfinite(z["scores"]), axis=1)
        lignes = list(zip(z["episode"].tolist(), z["pas"].tolist(), notees.tolist()))
    plan = [e["episode"] for e in epi["fiches"]]
    lots = [plan[k:k + c["lot"]] for k in range(0, len(plan), c["lot"])]
    assert len(epi["identite"]) == len(lots) == 2
    for k, (entree, lot) in enumerate(zip(epi["identite"], lots)):
        assert entree["lot"] == k
        notables = [(e, p) for e, p, n in lignes if n and e in lot]
        if not notables:
            assert entree.get("sans_action_notable") is True
            continue
        premier = [(e, p) for e, p in notables if e == lot[0]]
        attendue = min(premier, key=lambda x: x[1]) if premier else notables[0]
        assert (entree["episode"], entree["pas"]) == attendue
        assert entree["mahalanobis"] is (k < c["lots_mahalanobis_identite"])
        assert entree["ecart_relatif_max"] <= c["tolerance_identite"]
    avec, sans = epi["identite"][0], epi["identite"][1]
    if "sondes_controlees" in avec and "sondes_controlees" in sans:
        assert avec["sondes_controlees"] > sans["sondes_controlees"]           # Mahalanobis exclu après le premier lot


def test_memes_graines_d_action_d_une_condition_a_l_autre(tmp_path, monkeypatch):
    """Pour une même tâche, chaque condition reçoit les mêmes graines d'action et le même échantillon de la garde
    d'équivalence (un générateur neuf par épisode, depuis la clé de la tâche)."""
    from test_premier_test_ia_run import TACHES

    c = _config(tmp_path)
    vu = {}

    def capture(modele, fmt, envs, ids, n, T, graines_a, couches, max_nouveaux, temperature, echantillon, *a, **k):
        vu["ids"], vu["graines"], vu["echantillon"] = list(ids), graines_a, echantillon
        raise _Passe()

    monkeypatch.setattr(rp, "jouer_episodes", capture)
    plan = rp.plan_p3(TACHES)
    g = graines(rp.cles_des_graines(TACHES, c), 77)
    graines_taches = {t["identifiant"]: g[f"tache/{t['identifiant']}"] for t in TACHES}
    consignes = {k: {"consigne": "PRIVATE NOTE: essai.", "indication": "Reminder: essai."} for k in ("saboteur", "temoin", "mention")}
    with pytest.raises(_Passe):
        rp.jouer_p3(None, FMT, plan, graines_taches, dict(c, lot=8), consignes, Notation(_sondes()), ["s0", "s2"])
    assert len(vu["ids"]) == 8
    par_tache = {}
    for b, e in enumerate(vu["ids"]):
        tache = e.split("/")[1]
        par_tache.setdefault(tache, []).append((json.dumps(sorted(vu["graines"][b].items())),
                                                sorted(s for bb, _, s in vu["echantillon"] if bb == b)))
    assert len(par_tache) == 2 and all(len(v) == 4 and len(set(x[0] for x in v)) == 1 and len({tuple(x[1]) for x in v}) == 1
                                       for v in par_tache.values())
    a, b = par_tache.values()
    assert a[0][0] != b[0][0]                                      # deux tâches : deux graines distinctes
