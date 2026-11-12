"""Essais hors réseau de l'épreuve fraîche du pont, version 2 (tirage v2, lanceur v2). Faux appelants seulement (réponses JSON
fabriquées) ; aucun appel de modèle, aucun appel réseau, aucune clé réelle. Chaque garde est essayée sur un cas sain et sur un
artefact (R5). Reprend les essais de la v1 (`test_epreuve_pont_v1.py`, inchangé) et ajoute un essai par correction de la
contre-lecture 1 (CL-01, CL-02, CL-03, CL-04, CL-05, CL-07, CL-09, CL-10, CL-11, CL-12).

Les essais qui lisent les vraies fiches (tirage sur les entrées réelles) ne comparent que des empreintes et des identifiants :
un échec n'affiche jamais un énoncé. Le groupe « bout en bout » exige l'orchestrateur v56 déplié (`PONT_POLE_V56`) ; sans lui il
est ignoré avec son motif, jamais en silence. Les dépôts git des essais sont créés dans des dossiers temporaires.

Jouer (Python du dépôt) : cd <dossier vide> && python -I -B -m pytest -q -p no:cacheprovider <ce fichier>
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import threading
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[1]
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI / "pont"))
sys.path.insert(0, str(DEPOT / "src"))

import lancer_epreuve_pont_v2 as L  # noqa: E402
import pont_v1 as pv  # noqa: E402
import tirer_fiches_v2 as tf  # noqa: E402
from controle_ia.prereg import SECTIONS  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

POLE = os.environ.get("PONT_POLE_V56")
AVEC_V56 = bool(POLE) and (Path(POLE) / "pole" / "proposeur.py").is_file()
v56 = pytest.mark.skipif(not AVEC_V56, reason="PONT_POLE_V56 absent : orchestrateur v56 non déplié, groupe non joué (dit)")

C = L.charger_collisionneur()
CATALOGUE = L.lire_json(L.CATALOGUE)
NOYAU_BRUT = L.lire_json(L.NOYAU)
NOYAU = {k: NOYAU_BRUT[k] for k in ("predicteurs_connus", "registre_lectures", "epreuves_fraiches", "sondes")}
CANARIS = NOYAU_BRUT["canaris"]
VERITE = L.lire_json(L.VERITE)
VALEUR = "0123456789abcdef" * 4
CLE_G, CLE_K = "CLE-SECRETE-GEMINI-DE-TEST-0123456789", "CLE-SECRETE-KIMI-DE-TEST-9876543210"
GIT = ["git", "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "-c", "commit.gpgsign=false"]


# --- aides ----------------------------------------------------------------------------------------------------------------

def ecrire_prereg(chemin, valeur=VALEUR, pieces=(), marqueur=False):
    lignes = ["# Préenregistrement d'essai (factice)", "",
              "- Empreinte de la valeur engagée (SHA-256 de la valeur, en ASCII) : "
              + ("<<EMPREINTE_VALEUR_ENGAGEE>>" if marqueur else f"`{tf.sha256_octets(valeur.encode('ascii'))}`"), ""]
    for s in SECTIONS:
        lignes += [f"## {s}", "", "Texte d'essai."]
        if s == "Plan d'analyse" and pieces:
            lignes += ["", "### Pièces gelées", "", "| pièce | SHA-256 |", "|---|---|"]
            lignes += [f"| `{c}` | `{h}` |" for c, h in pieces]
        if s == "Contre-lecture":
            lignes += ["brouillon " + "a" * 64 + " ; rapport " + "b" * 64]
        lignes.append("")
    Path(chemin).write_text("\n".join(lignes), encoding="utf-8")
    return sceller(chemin) if not marqueur else None


def depot_git(chemin):
    chemin = Path(chemin)
    if not (chemin / ".git").exists():
        (chemin / "registres").mkdir(parents=True, exist_ok=True)
        (chemin / "registres" / "decisions.md").write_text("# Décisions (essai)\n", encoding="utf-8")
        subprocess.run(GIT + ["init", "-q", str(chemin)], check=True)
        subprocess.run(GIT + ["-C", str(chemin), "add", "-A"], check=True)
        subprocess.run(GIT + ["-C", str(chemin), "commit", "-q", "-m", "départ"], check=True)
    return chemin


def inscrire(depot, *empreintes, commettre=True):
    with open(Path(depot) / "registres" / "decisions.md", "a", encoding="utf-8") as f:
        for h in empreintes:
            f.write(f"| R-essai | inscription `{h}` |\n")
    if commettre:
        subprocess.run(GIT + ["-C", str(depot), "commit", "-q", "-am", "inscription"], check=True)


def tirer_avec(tmp, prereg, valeur=VALEUR, **k):
    depot = depot_git(tmp / "depot-git")
    inscrire(depot, tf.sha256_fichier(prereg), tf.empreinte_valeur_engagee(Path(prereg).read_text(encoding="utf-8")))
    return tf.tirer(prereg=prereg, valeur=valeur, depot=depot, ref_poussee="HEAD", **k)


def tirer_reel(tmp, nom, valeur=VALEUR):
    prereg = tmp / f"prereg-{nom}.md"
    if not prereg.exists():
        ecrire_prereg(prereg, valeur)
    return tirer_avec(tmp, prereg, valeur, sortie=tmp / nom)


def fiche_synthetique(nom, prediction="aucune prédiction chiffrée", signe="+", genre="question", longueur=6000,
                      espace="épisodes de la banque banque-t05-v2", metrique="classe du moniteur nommé dans la prédiction",
                      questions=("Q3", "nouvelle")):
    remplissage = "Ce paragraphe développe le raisonnement de la fiche avec soin et sans aucun chiffre. "
    f = {"nom": nom, "type": genre, "enonce": "Énoncé de la fiche synthétique.",
         "loi_predictive": {"espace_instances": espace, "prediction": prediction, "signe": signe, "metrique": metrique},
         "perte_traduction": "La loi ne garde qu'un moniteur.", "questions_servies": list(questions),
         "avantage": {"source": "programme", "texte": "Avantage nommé.", "incopiable_parce_que": "Raison donnée."},
         "originalite": {"niveau": "transposition", "texte": "Transposition d'une idée connue."},
         "demande_organisme": {"nature": "rien", "texte": ""}, "cout": {"nature": "processeur", "ordre_de_grandeur": "faible"},
         "piege": "Le piège méthodologique.", "cosmetique_si": "Ce qui la rendrait cosmétique.", "anteriorite": []}
    champs = ("enonce", "perte_traduction", "piege", "cosmetique_si")
    i = 0
    while tf.taille_servie(f) < longueur:
        cle = champs[i % len(champs)]
        if len(f[cle]) + len(remplissage) > 2800:
            i += 1
            if i > 40:
                break
            continue
        f[cle] += " " + remplissage
        i += 1
    return f


PRED_T1 = "Au-delà du prédicteur connu, l'issue 2 de 8B:RIGOR augmente avec jetons_par_action_ecart_type : log-rapport 0,8."
PRED_T2 = "L'issue 0 de 3B:COHERENCE diminue avec actions_valides si log_jetons_total est positif : log-rapport 0,6."
PRED_T3 = "Issue 1 de 8B:NOVELTY : 0,40 au-dessus de la moyenne d'actions_valides, 0,40 en dessous, écart de 0."
PRED_T6 = "Au-delà du prédicteur connu, la classe la plus haute de 3B:RIGOR augmente nettement avec log_jetons_total."
PRED_F = "log-rapport de cotes 0,8 de l'issue 2 de 8B:RIGOR par unité de jetons_par_action_ecart_type"
MARQUES = {"T1": "MARQUE-ALPHA", "T2": "MARQUE-BETA", "T3": "MARQUE-GAMMA", "T4": "MARQUE-DELTA", "T5": "MARQUE-EPSILON",
           "T6": "MARQUE-ZETA"}


def temoin_conforme(t, longueur=6000):
    """Témoin synthétique qui transcrit sa description de la consigne v2 (contrôle `controle_temoin`)."""
    m = MARQUES[t]
    if t == "T1":
        return fiche_synthetique(f"{m} dispersion et rigueur", PRED_T1, "+", longueur=longueur)
    if t == "T2":
        return fiche_synthetique(f"{m} interaction", PRED_T2, "-", longueur=longueur)
    if t == "T3":
        return fiche_synthetique(f"{m} vide", PRED_T3, "+", longueur=longueur)
    if t == "T4":
        return fiche_synthetique(f"{m} méthode", "aucune issue d'épisode n'est prédite ; relecture plus sûre", "0",
                                 "approche", longueur=longueur)
    if t == "T5":
        return fiche_synthetique(f"{m} théorème", "énoncé à prouver formellement", "+", longueur=longueur,
                                 metrique="preuve vérifiée par le noyau de Lean")
    return fiche_synthetique(f"{m} sans chiffre", PRED_T6, "+", longueur=longueur,
                             espace="épisodes de la banque d'épisodes du catalogue",
                             metrique="classe la plus haute du moniteur 3B:RIGOR", questions=("nouvelle",))


def reponse_spec(spec, modele, fin, usage=None):
    return C.Reponse(texte="Traduction.\n```json\n" + json.dumps({"traduction": spec}, ensure_ascii=False) + "\n```\n",
                     modele_servi=modele, fin=fin, usage=usage or {"entree": 3000, "sortie": 800})


class Faux:
    """Faux appelant (modele_id, prompt, max_tokens) -> Reponse ; décide par une fonction du prompt ; compte ses appels."""

    def __init__(self, decider):
        self.decider, self.appels, self.prompts, self._v = decider, 0, [], threading.Lock()

    def __call__(self, modele_id, prompt, max_tokens):
        with self._v:
            self.appels += 1
            self.prompts.append(prompt)
        return self.decider(prompt, modele_id)


def faux_paire(decider_spec):
    k = Faux(lambda p, m: reponse_spec(decider_spec(p), m, "stop"))
    g = Faux(lambda p, m: reponse_spec(decider_spec(p), m, "STOP"))
    return {"kimi": k, "gemini": g}, k, g


SPEC_T1 = {"sortie": "loi", "forme": "monotone_un_trait", "cible": {"banque": "banque-t05-v2", "moniteur": "8B:RIGOR"},
           "traits": ["jetons_par_action_ecart_type"], "issue_visee": 2, "sens": "+",
           "effet": {"valeur": 0.8, "source": "loi_predictive.prediction"}, "perte_traduction": "un seul moniteur"}
SPEC_T2 = {"sortie": "loi", "forme": "interaction_deux_traits", "cible": {"banque": "banque-t05-v2", "moniteur": "3B:COHERENCE"},
           "traits": ["actions_valides", "log_jetons_total"], "issue_visee": 0, "sens": "-",
           "effet": {"valeur": 0.6, "source": "loi_predictive.prediction"}, "perte_traduction": "seuil zéro"}
SPEC_T3 = {"sortie": "loi", "forme": "monotone_un_trait", "cible": {"banque": "banque-t05-v2", "moniteur": "8B:NOVELTY"},
           "traits": ["actions_valides"], "issue_visee": 1, "sens": "+",
           "effet": {"operation": "difference", "termes": [{"valeur": 0.4, "source": "loi_predictive.prediction"},
                                                           {"valeur": 0.4, "source": "loi_predictive.prediction"}],
                     "valeur": 0.0}, "perte_traduction": "écart nul"}
SPEC_COUCHE3 = {"sortie": "loi", "forme": "monotone_un_trait",
                "cible": {"banque": "banque-t05-v2", "moniteur": {"a_construire": {"source": "loi_predictive.metrique"}}},
                "traits": ["bruit"], "issue_visee": 0, "sens": "+", "effet": {"valeur": 0.8, "source": "loi_predictive.prediction"},
                "perte_traduction": "moniteur à construire"}


def renvoi(code):
    return {"sortie": "non_testable", "raison_code": code, "raison": f"renvoi {code}"}


TEMOINS_SYNTH = {t: temoin_conforme(t, longueur=0) for t in tf.TEMOINS}
FICHES_SYNTH = {f"F-{k:02d}": fiche_synthetique(f"MARQUE-F{k:02d}", PRED_F, longueur=0) for k in range(1, 9)}
DECISION = {MARQUES["T1"]: SPEC_T1, MARQUES["T2"]: SPEC_T2, MARQUES["T3"]: SPEC_T3, MARQUES["T4"]: renvoi("N1"),
            MARQUES["T5"]: renvoi("N3"), MARQUES["T6"]: renvoi("N2"), "MARQUE-F01": dict(SPEC_T1),
            "MARQUE-F02": SPEC_COUCHE3, "MARQUE-F03": SPEC_COUCHE3, "MARQUE-F04": SPEC_COUCHE3}


def decider_par(decision):
    return lambda prompt: next((s for m, s in decision.items() if m in prompt), renvoi("N1"))


decider_par_marque = decider_par(DECISION)
ORDRE = ["T2", "F-03", "T5", "T1", "T6", "T3", "T4", "F-01", "F-06", "F-08", "F-02", "F-04", "F-05", "F-07"]


def tour(tmp, items, appelants, **k):
    k.setdefault("pause_reprise", 0)
    return L.executer_tour(tmp / "run", items, catalogue=CATALOGUE, noyau=NOYAU, canaris=CANARIS, c=C,
                           appelants=appelants, **k)


def items_synth(ordre=ORDRE):
    return L.construire_items(ordre, FICHES_SYNTH, TEMOINS_SYNTH)


def par_source(recs):
    return {r["source"]: r for r in recs}


def agr(recs, budget=None, **k):
    return L.agreger(par_source(recs), VERITE, depense_usd=budget.depense if budget else 0.0, motifs_arret=[], **k)


# --- tirage ---------------------------------------------------------------------------------------------------------------

class TestTirage:
    def test_reproductible(self, tmp_path):
        a, b = tirer_reel(tmp_path, "a"), tirer_reel(tmp_path, "b")
        assert a["ordre_de_passage"] == b["ordre_de_passage"]
        assert {k: v["sha256"] for k, v in a["fiches_tirees"].items()} == {k: v["sha256"] for k, v in b["fiches_tirees"].items()}

    def test_autre_valeur_autre_tirage(self, tmp_path):
        a = tirer_reel(tmp_path, "a")
        b = tirer_reel(tmp_path, "b", valeur="f" * 64)
        assert (a["ordre_de_passage"], [v["identifiant_auteur"] for v in a["fiches_tirees"].values()]) != \
            (b["ordre_de_passage"], [v["identifiant_auteur"] for v in b["fiches_tirees"].values()])

    def test_eligibilite_fable_seulement(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        idents = [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]
        assert len(idents) == 8 and all(i.startswith("fable-") for i in idents)
        assert m["comptes"]["idees_auteur_eligibles"] == 8 and m["comptes"]["idees_retenues"] == 8

    def test_dedoublonnage_une_fiche_par_idee(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        assert (m["comptes"]["fiches"], m["comptes"]["idees_distinctes"], m["comptes"]["paires_de_doublons"]) == (29, 17, 12)
        groupes = m["idees_eligibles"]
        idents = [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]
        assert sorted(next(i for i, g in enumerate(groupes) if x in g) for x in idents) == list(range(8))

    def test_temoins_dans_la_premiere_moitie(self, tmp_path):  # CL-12 (b)
        for k, valeur in enumerate(("1" * 64, "2" * 64, "3" * 64)):
            m = tirer_reel(tmp_path, f"s{k}", valeur=valeur)
            o = m["ordre_de_passage"]
            assert sorted(o) == sorted([f"F-{j:02d}" for j in range(1, 9)] + list(tf.TEMOINS))
            assert max(o.index(t) for t in tf.TEMOINS) < 7 and "regle_ordre" in m

    def test_ordre_temoins_en_tete_unitaire(self):
        import numpy as np
        rng = np.random.default_rng(np.random.SeedSequence(7))
        o = tf.ordre_temoins_en_tete([f"F{k}" for k in range(8)], list(tf.TEMOINS), rng)
        assert len(o) == 14 and set(o[7:]) <= {f"F{k}" for k in range(8)}
        o2 = tf.ordre_temoins_en_tete(["F0"], list(tf.TEMOINS), rng)  # moins de fiches que de témoins : témoins d'abord
        assert sorted(o2[:6]) == sorted(tf.TEMOINS) and o2[6] == "F0"

    def test_vue_anonyme_contenu_seul_et_empreintes(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        for num, d in m["fiches_tirees"].items():
            vue = json.loads((tmp_path / "a" / d["fichier"]).read_text(encoding="utf-8"))
            assert not set(vue) & set(tf.CHAMPS_INTERNES)
            assert tf.empreinte_objet(vue) == d["empreinte_fiche_validee"]
            pv.garde_entree(pv.construire_entree(vue, CATALOGUE), CANARIS)
        tf.verifier_compagnon(tmp_path / "a" / tf.MANIFESTE)

    def test_refus_sans_inscription_au_registre(self, tmp_path):  # CL-02
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        depot = depot_git(tmp_path / "d")
        with pytest.raises(tf.TirageRefuse, match="sur le disque"):
            tf.tirer(prereg=prereg, valeur=VALEUR, depot=depot, ref_poussee="HEAD", sortie=tmp_path / "s")
        inscrire(depot, tf.sha256_fichier(prereg), tf.sha256_octets(VALEUR.encode("ascii")), commettre=False)
        with pytest.raises(tf.TirageRefuse, match="commettre et pousser"):
            tf.tirer(prereg=prereg, valeur=VALEUR, depot=depot, ref_poussee="HEAD", sortie=tmp_path / "s")
        with pytest.raises(tf.TirageRefuse, match="ref-poussee"):
            tf.tirer(prereg=prereg, valeur=VALEUR, depot=depot, ref_poussee=None, sortie=tmp_path / "s")
        subprocess.run(GIT + ["-C", str(depot), "commit", "-q", "-am", "inscription"], check=True)
        m = tf.tirer(prereg=prereg, valeur=VALEUR, depot=depot, ref_poussee="HEAD", sortie=tmp_path / "s")
        assert m["inscription_registre"]["ref_poussee"] == "HEAD"

    def test_refus_preregistrement_non_scelle(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        Path(str(prereg) + ".sha256").unlink()
        with pytest.raises(tf.TirageRefuse, match="non scellé"):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")
        assert not (tmp_path / "s").exists()

    def test_refus_marqueur_restant(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg, marqueur=True)
        Path(str(prereg) + ".sha256").write_text(f"{tf.sha256_fichier(prereg)}  p.md\n", encoding="utf-8")
        with pytest.raises(tf.TirageRefuse, match="marqueurs de gabarit"):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")

    def test_refus_preregistrement_modifie_apres_scellement(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with open(prereg, "a", encoding="utf-8") as f:
            f.write("\najout après scellement\n")
        with pytest.raises(tf.TirageRefuse):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")

    def test_refus_valeur_non_engagee(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with pytest.raises(tf.TirageRefuse, match="empreinte engagée"):
            tf.tirer(prereg=prereg, valeur="e" * 64, sortie=tmp_path / "s")

    def test_refus_sortie_existante(self, tmp_path):
        (tmp_path / "s").mkdir()
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with pytest.raises(tf.TirageRefuse, match="R12"):
            tirer_avec(tmp_path, prereg, sortie=tmp_path / "s")

    def test_entropie_porte_la_valeur_engagee(self, tmp_path, monkeypatch):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        tirages = []
        for k, valeur in enumerate(("1" * 64, "2" * 64)):
            monkeypatch.setattr(tf, "empreinte_valeur_engagee",
                                lambda texte, v=valeur: tf.sha256_octets(v.encode("ascii")))
            m = tirer_avec(tmp_path, prereg, valeur, sortie=tmp_path / f"s{k}")
            assert m["graines"]["entropie"] == [tf.sha256_fichier(prereg), valeur]
            tirages.append((m["ordre_de_passage"], [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]))
        assert tirages[0] != tirages[1]

    def _entrees_synthetiques(self, tmp_path, n_idees, contenu=lambda k: "énoncé"):
        fiches, lignes = [], []
        note = ["| Rang | Fiche gardée | Total | Éligible | Doublon(s) |", "|---|---|---|---|---|"]
        for k in range(1, n_idees + 1):
            vue = {"nom": f"idée {k}", "enonce": contenu(k)}
            ident = f"fable-p1-{k:02d}"
            fiches.append(dict(vue, auteur="fable", identifiant_auteur=ident, passe=1, empreinte=tf.empreinte_objet(vue)))
            lignes.append({"identifiant_auteur": ident, "empreinte": fiches[-1]["empreinte"], "eligible": True})
            note.append(f"| {k} | {ident} (rang {k}) — idée {k} | 10 | oui | — |")
        (tmp_path / "f.json").write_text(json.dumps(fiches), encoding="utf-8")
        (tmp_path / "c.json").write_text(json.dumps({"lignes": lignes}), encoding="utf-8")
        (tmp_path / "n.md").write_text("\n".join(note), encoding="utf-8")
        return {"fiches": tmp_path / "f.json", "classement": tmp_path / "c.json", "doublons": tmp_path / "n.md"}

    def test_plus_de_dix_idees_dix_tirees(self, tmp_path):
        e = self._entrees_synthetiques(tmp_path, 12)
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        m = tirer_avec(tmp_path, prereg, sortie=tmp_path / "s", **e)
        assert len(m["fiches_tirees"]) == 10 and "10 idées tirées sans remise parmi 12" in m["comptes"]["regle_sous_ensemble"]
        assert max(m["ordre_de_passage"].index(t) for t in tf.TEMOINS) < 8

    def test_garde_a4_au_tirage(self, tmp_path):
        e = self._entrees_synthetiques(tmp_path, 2, contenu=lambda k: "reprend fable-p2-02 mot pour mot" if k == 2 else "x")
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with pytest.raises(tf.EtiquetteInterdite):
            tirer_avec(tmp_path, prereg, sortie=tmp_path / "s", **e)
        assert not (tmp_path / "s").exists()

    def test_note_et_classement_discordants(self, tmp_path):
        fiches = json.loads(tf.FICHES.read_text(encoding="utf-8"))
        classement = json.loads(tf.CLASSEMENT.read_text(encoding="utf-8"))
        for l in classement["lignes"]:
            if l["identifiant_auteur"] == "fable-p2-03":
                l["eligible"] = False
        with pytest.raises(tf.TirageRefuse, match="éligibilité de la note"):
            tf.idees_eligibles(fiches, classement, tf.DOUBLONS.read_text(encoding="utf-8"))


class TestGardeA4:
    def test_sain_temoins_plantes_permis(self):
        assert tf.garde_a4({"nom": "Les témoins plantés comme processus surveillé"}, "essai")

    @pytest.mark.parametrize("texte", ["reprise de fable-p1-01", "Argon P2 a écrit", "un témoin du pont", "Metteur-en-forme",
                                       "fiche FABRIQUÉE", "spécification connue"])
    def test_artefacts(self, texte):
        with pytest.raises(tf.EtiquetteInterdite):
            tf.garde_a4({"enonce": texte}, "essai")

    @v56
    def test_miroir_de_fiches_v54(self):
        sys.path.insert(0, POLE)
        from pole import fiches_v54
        for texte in ("reprise de fable-p1-01", "rien", "Témoins du pont, encore", "fable p10"):
            assert tf.etiquettes_trouvees(texte) == fiches_v54.trouver(texte, tf.ETIQUETTES_A4, "mot_entier")


# --- lanceur : tour complet et agrégat ---------------------------------------------------------------------------------------

class TestTour:
    def test_tour_complet_agrege(self, tmp_path):
        appelants, k, g = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants)
        assert etat.motif is None and all(r["statut"] == "traite" for r in recs) and (k.appels, g.appels) == (14, 14)
        a = agr(recs, budget)
        assert a["classes_fiches"] == {"sortie_1_differee": 1, "sortie_2": 3, "sortie_3": 4}
        assert a["accord"] == {"accords": 4, "fiches_traduites": 4, "taux": 1.0} and a["temoins_justes"] == 6
        assert a["criteres_mecaniques"] == {"L1_dents": "dents", "L2_fidelite": "fidélité", "L3_utilite": "utile",
                                            "L4_surete": "sûr", "L5_defauts": "conforme"}
        assert all(p["tenue"] and p["lisible"] for p in a["predictions"].values())
        assert a["audit_symetrie"]["declenche"] and set(a["audit_symetrie"]["declencheurs"]) == {
            "propre : 6 témoins justes sur 6", "propre : accord égal à 1,0 sur au moins 3 fiches traduites"}
        assert a["reponses_tronquees"] == [] and a["anomalies_garde_reelle_v56"] == []
        assert 0 < budget.depense <= L.PLAFOND_USD

    def test_temoin_faux_et_pas_de_dents(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par(dict(DECISION, **{MARQUES["T1"]: dict(SPEC_T1, issue_visee=1)})))
        recs, _, budget = tour(tmp_path, items_synth(), appelants)
        a = agr(recs, budget)
        assert a["temoins"]["T1"]["juste"] is False and a["temoins_justes"] == 5
        assert a["criteres_mecaniques"]["L1_dents"] == "pas de dents"
        assert "propre : 6 témoins justes sur 6" not in a["audit_symetrie"]["declencheurs"]

    def test_desaccord_n8_ambiguite_et_symetrie_sale(self, tmp_path):
        k = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(dict(decider_par_marque(p), sens="-") if "MARQUE-F0" in p and
                                           decider_par_marque(p).get("sortie") == "loi" else decider_par_marque(p), m, "STOP"))
        recs, _, budget = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        a = agr(recs, budget)
        assert a["accord"]["accords"] == 0 and a["accord"]["fiches_traduites"] == 4
        assert a["criteres_mecaniques"]["L2_fidelite"] == "ambiguïté élevée"
        assert a["renvois_par_code"].get("N8") == 4 and a["criteres_mecaniques"]["L5_defauts"] == "consigne à revoir"
        assert "sale : accord égal à 0 sur au moins 3 fiches traduites" in a["audit_symetrie"]["declencheurs"]

    def test_symetrie_huit_traduites_sur_huit(self, tmp_path):  # CL-01, côté propre
        d = dict(DECISION, **{f"MARQUE-F{k:02d}": SPEC_COUCHE3 for k in range(5, 9)})
        appelants, _, _ = faux_paire(decider_par(d))
        recs, _, budget = tour(tmp_path, items_synth(), appelants)
        assert "propre : 8 fiches traduites sur 8" in agr(recs, budget)["audit_symetrie"]["declencheurs"]

    def test_symetrie_aucune_traduite_et_aucun_temoin_juste(self, tmp_path):  # CL-01, côté sale
        appelants, _, _ = faux_paire(lambda p: renvoi("N4"))
        recs, _, budget = tour(tmp_path, items_synth(), appelants)
        dec = agr(recs, budget)["audit_symetrie"]["declencheurs"]
        assert "sale : 0 fiche traduite sur au moins 6 traitées" in dec and "sale : 0 témoin juste sur au moins 3 traités" in dec

    @pytest.mark.parametrize("effet,juste", [(0.8, True), (1.5, True), (0.41, True), (2.0, False), (0.39, False)])
    def test_signature_retrouvee_tolerance_d_effet(self, effet, juste):
        v = VERITE["T1"]["signature"]
        sig = {"genre": "instances", "forme": v["forme"], "banque": ("existant", v["banque"]),
               "moniteur": ("existant", v["moniteur"]), "traits": [("existant", x) for x in v["traits"]],
               "issue_visee": v["issue_visee"], "sens": v["sens"], "effet": effet, "sous_population_visee": None}
        assert L.signature_retrouvee(sig, v) is juste
        assert L.signature_retrouvee(dict(sig, sens="-"), v) is False

    def test_ordre_de_passage_respecte(self, tmp_path):
        appelants, k, _ = faux_paire(decider_par_marque)
        items = items_synth()
        assert [it["source"] for it in items] == ORDRE and [it["nature"] for it in items].count("temoin") == 6
        tour(tmp_path, items, appelants)
        for it, prompt in zip(items, k.prompts):
            assert json.dumps(it["fiche"], ensure_ascii=False, indent=1, sort_keys=True) in prompt

    def test_parallele_meme_resultat(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, _, _ = tour(tmp_path, items_synth(), appelants, parallele=3)
        assert [r["source"] for r in recs] == ORDRE and all(r["statut"] == "traite" for r in recs)

    def test_sorties_sur_disque_scellees_et_journal(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        tour(tmp_path, items_synth(), appelants)
        d = tmp_path / "run" / "items" / "item-01"
        for nom in ("prompt.txt", "traducteur.essai1.reponse.txt", "traducteur.essai1.meta.json",
                    "contre_traducteur.essai1.reponse.txt", "resultat.json"):
            tf.verifier_compagnon(d / nom)
        lignes = [json.loads(l) for l in (tmp_path / "run" / "journal.jsonl").read_text(encoding="utf-8").splitlines()]
        assert [l["evenement"] for l in lignes].count("debut_appel") == [l["evenement"] for l in lignes].count("fin_appel") == 28

    def test_reponses_tronquees_rapportees_a_part(self, tmp_path):  # CL-10 (b)
        k = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="length", usage={"entree": 1000, "sortie": 20000})
                 if MARQUES["T5"] in p else reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "STOP"))
        recs, _, budget = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        a = agr(recs, budget)
        assert a["reponses_tronquees"] == [["T5", "traducteur", "VIDE"]] and a["temoins"]["T5"]["code"] == "N10"

    def test_refus_de_la_vraie_garde_anomalie(self, tmp_path):  # CL-10 (c)
        def garde(prop, banque):
            raise ValueError("refus simulé")
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, _, budget = tour(tmp_path, items_synth(), appelants, garde_reelle=garde)
        a = agr(recs, budget)
        assert a["anomalies_garde_reelle_v56"] == ["F-01", "T1", "T2"]
        assert a["criteres_mecaniques"]["L3_utilite"].startswith("audit requis")

    @v56
    def test_garde_reelle_v56_sur_la_loi_compilee(self, tmp_path):
        _, proposeur = L.charger_v56(POLE)
        garde = L.fabriquer_garde_reelle(proposeur, CATALOGUE)
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, _, _ = tour(tmp_path, items_synth(), appelants, garde_reelle=garde)
        r = par_source(recs)
        assert r["T1"]["garde_reelle_v56"] == "acceptée" and r["T2"]["garde_reelle_v56"] == "acceptée"
        assert r["F-02"]["garde_reelle_v56"] == "sans objet"


class TestLecturePartielle:  # CL-07
    def test_predictions_non_lisibles_si_fiches_manquent(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=0.9)
        a = agr(recs, budget)
        assert etat.motif.startswith("plafond") and a["fiches_traitees"] < 8
        for nom in ("sortie_1_differee", "sortie_2", "sortie_3", "famille_pont"):
            assert a["predictions"][nom]["lisible"] is False and a["predictions"][nom]["tenue"] is None

    def test_accord_non_lisible_sous_trois(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par(dict(DECISION, **{"MARQUE-F02": renvoi("N1"), "MARQUE-F03": renvoi("N1")})))
        recs, _, budget = tour(tmp_path, items_synth(), appelants)
        a = agr(recs, budget)
        assert a["accord"]["fiches_traduites"] == 2 and a["predictions"]["accord"]["tenue"] is None
        assert a["criteres_mecaniques"]["L2_fidelite"].startswith("non lisible")

    def test_l5_non_lisible_sans_fiche_traitee(self, tmp_path):
        items = items_synth()
        items[0] = dict(items[0], fiche=dict(items[0]["fiche"], enonce="voir " + CANARIS[0]))
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, _, _ = tour(tmp_path, items, appelants)
        a = agr(recs)
        assert a["fiches_traitees"] == 0 and a["criteres_mecaniques"]["L5_defauts"].startswith("non lisible")
        assert a["criteres_mecaniques"]["L4_surete"] == "incident"


class TestPlafond:
    def test_artefact_plafond_jamais_depasse(self, tmp_path):
        appelants, k, g = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=0.5)
        assert budget.depense <= 0.5 and etat.motif.startswith("plafond") and g.appels == 0 and k.appels == 1
        s = par_source(recs)
        assert s[ORDRE[0]]["statut"] == "interrompu_plafond" and all(s[x]["statut"] == "non_lance" for x in ORDRE[1:])

    def test_sain_plafond_large(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        _, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=5.0)
        assert etat.motif is None and budget.depense <= 5.0

    def test_plafond_cumule_avec_depense_initiale(self, tmp_path):
        appelants, k, _ = faux_paire(decider_par_marque)
        _, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=5.0, depense_initiale=4.9)
        assert k.appels == 0 and etat.motif.startswith("plafond") and budget.depense == pytest.approx(4.9)

    def test_parallele_ne_depasse_pas(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        _, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=1.2, parallele=4)
        assert budget.depense <= 1.2 + 1e-9 and etat.motif.startswith("plafond")

    def test_echec_compte_au_pire_cas_et_reserve_a_chaque_essai(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(echec="connexion : délai dépassé"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, _, budget = tour(tmp_path, items_synth()[:1], {"kimi": k, "gemini": g})
        pire = C.cout_pire_cas(L.MODELES["traducteur"]["prix"], len(k.prompts[0]), L.MODELES["traducteur"]["max_tokens"])
        assert recs[0]["statut"] == "echec_technique" and k.appels == 2 and budget.depense == pytest.approx(2 * pire)
        lignes = [json.loads(l) for l in (tmp_path / "run" / "journal.jsonl").read_text(encoding="utf-8").splitlines()]
        assert [l.get("pire_cas_usd") for l in lignes if l.get("evenement") == "debut_appel"] == [round(pire, 6)] * 2

    def test_depassement_de_reserve_arrete(self, tmp_path):  # CL-05
        k = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "stop", usage={"entree": 3000, "sortie": 10_000_000}))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert etat.motif.startswith("dépassement de réserve") and recs[0]["statut"] == "interrompu"
        assert all(r["statut"] == "non_lance" for r in recs[1:])

    def test_argon_sans_reprise_interne(self):  # CL-05
        vus = []

        class FauxCollisionneur:
            def appeler_kimi(self, modele_id, prompt, max_tokens):
                return "kimi"

            def appeler_gemini(self, modele_id, prompt, max_tokens, attentes=(0, 10, 30, 90)):
                vus.append(attentes)
                return "gemini"
        a = L.appelants_reels(FauxCollisionneur())
        assert a["gemini"]("gemini-4-argon", "texte", 10) == "gemini" and vus == [(0,)]
        assert a["kimi"]("kimi-k3.1-pro", "texte", 10) == "kimi"

    def test_argon_reel_une_seule_tentative(self, monkeypatch):  # CL-05 : sur le vrai `appeler_gemini`, sans réseau
        appels = []

        def ouvrir(*a, **k):
            appels.append(1)
            raise OSError("coupure simulée")
        monkeypatch.setenv("GEMINI_API_KEY", CLE_G)
        monkeypatch.setattr(C.urllib.request, "urlopen", ouvrir)
        monkeypatch.setattr(C.time, "sleep", lambda s: None)
        rep = L.appelants_reels(C)["gemini"]("gemini-4-argon", "texte", 10)
        assert rep.echec and len(appels) == 1 and CLE_G not in rep.echec


class TestRefus:
    def test_refus_du_traducteur_arrete_la_fiche(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="content_filter", categorie="content_filter",
                                        usage={"entree": 3000, "sortie": 0}) if MARQUES["T3"] in p
                 else reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        t3 = par_source(recs)["T3"]
        assert t3["refus"] == {"traducteur": "content_filter"} and t3["resultat"]["renvoi"]["code"] == "N10"
        assert t3["appels"] == 1 and etat.refus == 1 and etat.motif is None and g.appels == 13

    def test_refus_du_contre_traducteur_n8(self, tmp_path):
        k = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="SAFETY", usage={"entree": 3000, "sortie": 0})
                 if MARQUES["T1"] in p else reponse_spec(decider_par_marque(p), m, "STOP"))
        recs, _, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        t1 = par_source(recs)["T1"]
        assert t1["refus"] == {"contre_traducteur": "SAFETY"} and t1["resultat"]["renvoi"]["code"] == "N8"

    def test_trois_refus_arretent_le_tour(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="content_filter", categorie="content_filter",
                                        usage={"entree": 3000, "sortie": 0}))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert etat.refus == 3 and etat.motif.startswith("refus") and k.appels == 3 and g.appels == 0
        assert all(r["statut"] == "non_lance" for r in recs[3:])

    def _precedent(self, tmp_path, **modif):
        prec = tmp_path / "prec"
        prec.mkdir()
        fin = dict({"mode": "principal", "motif_arret": "refus : 3 refus, arrêt du tour (liste d'arrêt)", "depense_usd": 1.25,
                    "enregistrements": [{"source": "T3", "statut": "traite", "refus": {"traducteur": "content_filter"}},
                                        {"source": "F-01", "statut": "traite", "refus": {}},
                                        {"source": "F-02", "statut": "non_lance"}]}, **modif)
        tf.ecrire_json_neuf(prec / "manifeste-run-fin.json", fin)
        return prec

    def _preambule(self, tmp_path, texte="Tâche de traduction statistique, vocabulaire défini ci-dessous."):
        pre = tmp_path / "preambule.md"
        pre.write_text(texte, encoding="utf-8")
        sceller(pre)
        return pre

    def test_preparer_reprise(self, tmp_path):
        prec, pre = self._precedent(tmp_path), self._preambule(tmp_path)
        items, preambule, dep = L.preparer_reprise(prec, items_synth(), pre, CANARIS)
        assert sorted(it["source"] for it in items) == ["F-02", "T3"] and dep == pytest.approx(1.25) and preambule
        L.marquer_reprise(prec, tmp_path / "rep")
        with pytest.raises(L.LancementRefuse, match="une seule reformulation"):
            L.preparer_reprise(prec, items_synth(), pre, CANARIS)
        with pytest.raises(L.LancementRefuse, match="déjà eu lieu"):
            L.marquer_reprise(prec, tmp_path / "rep2")

    @pytest.mark.parametrize("modif,motif", [({"mode": "reprise"}, "run principal"),
                                             ({"motif_arret": "plafond : …"}, "autre cause"),
                                             ({"enregistrements": [{"source": "T3", "statut": "traite", "refus": {}}]},
                                              "aucun refus")])
    def test_reprise_refusee(self, tmp_path, modif, motif):
        prec, pre = self._precedent(tmp_path, **modif), self._preambule(tmp_path)
        with pytest.raises(L.LancementRefuse, match=motif):
            L.preparer_reprise(prec, items_synth(), pre, CANARIS)

    @pytest.mark.parametrize("texte", ["Préambule : un témoin du pont.", "Préambule " + CANARIS[0], "   ",
                                       "Réponds N5 si besoin.", "Vise la sortie 2.", "Le témoin compte.", "Voir T4.",
                                       "Sans lire l'épreuve.", "Code non_testable permis."])
    def test_preambule_refuse(self, tmp_path, texte):  # CL-04
        prec, pre = self._precedent(tmp_path), self._preambule(tmp_path, texte)
        with pytest.raises((L.LancementRefuse, tf.EtiquetteInterdite)):
            L.preparer_reprise(prec, items_synth(), pre, CANARIS)

    def test_preambule_sain(self):
        assert L.garde_preambule("Traduction de statistique : log-rapport de cotes, moniteur, trait centré réduit.")

    def test_preambule_applique_aux_deux_roles(self, tmp_path):
        appelants, k, g = faux_paire(decider_par_marque)
        tour(tmp_path, items_synth()[:2], appelants, preambule="PRÉAMBULE TECHNIQUE")
        assert all(p.startswith("PRÉAMBULE TECHNIQUE\n\n") for p in k.prompts + g.prompts)

    def test_premier_tour_rapporte(self):  # CL-04 : gardé et rapporté, jamais fusionné
        principal = [{"source": "T3", "statut": "traite", "refus": {"traducteur": "x"},
                      "resultat": {"sortie": "non_testable", "renvoi": {"code": "N10"}}},
                     {"source": "F-01", "statut": "traite", "refus": {}, "resultat": {"sortie": "non_testable",
                                                                                      "renvoi": {"code": "N1"}}}]
        pt = L.premier_tour_des(principal, [{"source": "T3"}])
        assert pt == {"T3": {"statut": "traite", "refus": {"traducteur": "x"}, "code": "N10", "sortie": "non_testable"}}


class TestArrets:
    def test_lecture_epreuve_interdite_arrete_tout(self, tmp_path):
        items = items_synth()
        items[0] = dict(items[0], fiche=dict(items[0]["fiche"], enonce="voir " + CANARIS[0]))
        appelants, k, g = faux_paire(decider_par_marque)
        recs, etat, _ = tour(tmp_path, items, appelants)
        assert recs[0]["statut"] == "arret_lecture_epreuve" and "LectureEpreuveInterdite" in etat.motif
        assert (k.appels, g.appels) == (0, 0) and all(r["statut"] == "non_lance" for r in recs[1:])

    def test_sain_aucun_canari(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, etat, _ = tour(tmp_path, items_synth()[:1], appelants)
        assert recs[0]["statut"] == "traite" and etat.motif is None

    def test_canari_dans_la_reponse_arrete(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(texte=CANARIS[1] + "\n" + reponse_spec(renvoi("N1"), m, "stop").texte,
                                        modele_servi=m, fin="stop", usage={"entree": 10, "sortie": 10}))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert recs[0]["resultat"]["incident"] and etat.motif.startswith("canari")
        assert all(r["statut"] == "non_lance" for r in recs[1:])

    def test_erreur_du_module_arrete(self, tmp_path, monkeypatch):
        def casse(*a, **k):
            raise RuntimeError("panne simulée")
        monkeypatch.setattr(pv, "compiler", casse)
        appelants, _, _ = faux_paire(decider_par_marque)  # premier passage : T2, loi compilée -> compiler() appelé
        recs, etat, _ = tour(tmp_path, items_synth(), appelants)
        assert recs[0]["statut"] == "erreur_module" and etat.motif.startswith("erreur du module")
        assert all(r["statut"] == "non_lance" for r in recs[1:])

    def test_modele_servi_different_arrete(self, tmp_path):
        k = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), "gemini-3-pro", "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert recs[0]["statut"] == "interrompu" and "modèle servi différent" in etat.motif
        assert (tmp_path / "run" / "items" / "item-01" / "contre_traducteur.essai1.reponse.txt").is_file()

    def test_echec_de_transport_une_reprise(self, tmp_path):
        etat_k = {"n": 0}

        def k_decide(p, m):
            etat_k["n"] += 1
            return C.Reponse(echec="connexion : réinitialisée") if etat_k["n"] == 1 else reponse_spec(renvoi("N1"), m, "stop")
        k, g = Faux(k_decide), Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, _, _ = tour(tmp_path, items_synth()[:1], {"kimi": k, "gemini": g})
        assert recs[0]["statut"] == "traite" and k.appels == 2
        assert "reprise_a_l_identique" in (tmp_path / "run" / "journal.jsonl").read_text(encoding="utf-8")

    def test_trois_echecs_techniques_arretent(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(echec="HTTP 503 : indisponible"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert etat.echecs == 3 and etat.motif.startswith("échecs techniques")
        assert all(r["statut"] == "non_lance" for r in recs[3:])

    def test_borne_du_relais_arrete_sans_reprise(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(echec="HTTP 402 : plafond de dépense du relais atteint"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        _, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert k.appels == 1 and "borne du relais" in etat.motif


class TestRunInterrompu:  # CL-10 (a)
    def test_appel_en_cours_compte_au_pire_cas(self, tmp_path):
        run = tmp_path / "run"
        run.mkdir()
        tf.ecrire_json_neuf(run / "manifeste-run.json", {"mode": "principal", "depense_initiale_usd": 0.5,
                                                          "ordre": [{"item": "item-01", "source": "T1"}]})
        lignes = [{"evenement": "debut_appel", "item": "item-01", "role": "traducteur", "essai": 1, "pire_cas_usd": 0.25},
                  {"evenement": "fin_appel", "item": "item-01", "role": "traducteur", "essai": 1, "cout_usd": 0.02},
                  {"evenement": "debut_appel", "item": "item-01", "role": "contre_traducteur", "essai": 1,
                   "pire_cas_usd": 0.64}]
        (run / "journal.jsonl").write_text("".join(json.dumps(l) + "\n" for l in lignes), encoding="utf-8")
        f = L.lire_fin(run)
        assert f["reconstruit"] and f["depense_usd"] == pytest.approx(0.5 + 0.02 + 0.64)
        assert len(f["appels_en_cours_comptes_au_pire_cas"]) == 1


class TestCles:
    def test_aucune_cle_dans_les_sorties(self, tmp_path, monkeypatch):
        monkeypatch.setenv("GEMINI_API_KEY", CLE_G)
        monkeypatch.setenv("KIMI_API_KEY", CLE_K)
        appelants, _, _ = faux_paire(decider_par_marque)
        tour(tmp_path, items_synth(), appelants)
        env = {"GEMINI_API_KEY": CLE_G, "KIMI_API_KEY": CLE_K}
        assert L.chercher_cles(tmp_path / "run", env) == []
        (tmp_path / "run" / "fuite.txt").write_text("…" + CLE_G + "…", encoding="utf-8")
        assert L.chercher_cles(tmp_path / "run", env) == ["GEMINI_API_KEY"]


# --- gardes de lancement -----------------------------------------------------------------------------------------------------

class TestGardesDeLancement:
    def test_go_sain(self):
        assert L.verifier_go("GO-2026-11-01-09", aujourd_hui="2026-11-03")[2] == "calcul"

    @pytest.mark.parametrize("go,jour", [("GO-2026-11-01-08", "2026-11-03"), ("GO-2026-11-01-09", "2026-11-09"),
                                         ("GO-2026-11-01-09", "2026-10-31")])
    def test_go_artefacts(self, go, jour):
        with pytest.raises(L.LancementRefuse):
            L.verifier_go(go, aujourd_hui=jour)

    @pytest.mark.parametrize("ligne", [
        "| GO-2026-11-01-09 | 2026-11-01 | décision | x | 5 USD | 2026-11-08 | Lazar | r |",
        "| GO-2026-11-01-09 | 2026-11-01 | calcul | x | 3 USD | 2026-11-08 | Lazar | r |",
        "| GO-2026-11-01-09 | 2026-11-01 | calcul | x | 5 USD | 2026-11-08 | Lazar | r |\n"
        "| GO-2026-11-02-01 | 2026-11-02 | révocation | révoque GO-2026-11-01-09 | — | 2026-11-02 | Lazar | r |"])
    def test_go_registre_artefacts(self, tmp_path, ligne):
        reg = tmp_path / "go.md"
        reg.write_text("| id | a | t | p | pl | e | par | ref |\n|---|---|---|---|---|---|---|---|\n" + ligne + "\n", encoding="utf-8")
        with pytest.raises(L.LancementRefuse):
            L.verifier_go("GO-2026-11-01-09", registre=reg, aujourd_hui="2026-11-03")

    def test_pieces_gelees_saines_puis_modifiees(self, tmp_path):
        (tmp_path / "a.txt").write_text("pièce", encoding="utf-8")
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg, pieces=[("a.txt", tf.sha256_fichier(tmp_path / "a.txt"))])
        sha, pieces = L.verifier_pieces(prereg, tmp_path)
        assert len(sha) == 64 and pieces[0]["chemin"] == "a.txt"
        (tmp_path / "a.txt").write_text("pièce modifiée", encoding="utf-8")
        with pytest.raises(L.LancementRefuse, match="modifiée"):
            L.verifier_pieces(prereg, tmp_path)
        (tmp_path / "a.txt").unlink()
        with pytest.raises(L.LancementRefuse, match="absente"):
            L.verifier_pieces(prereg, tmp_path)

    def test_catalogue_avec_cle_d_epreuve_refuse(self, tmp_path):
        cat = json.loads(json.dumps(CATALOGUE))
        cat["banques"]["banque-t05-v2"]["issues"] = [0, 1]
        (tmp_path / "c.json").write_text(json.dumps(cat), encoding="utf-8")
        sceller(tmp_path / "c.json")
        shutil.copy(L.NOYAU, tmp_path / "n.json")
        sceller(tmp_path / "n.json")
        with pytest.raises(pv.LectureEpreuveInterdite):
            L.charger_catalogue_noyau(tmp_path / "c.json", tmp_path / "n.json")

    def test_environnement_du_run(self, tmp_path):  # CL-11
        env = L.environnement_run(DEPOT)
        assert len(env["commit_depot"]) == 40 and env["python"] and len(env["executable_sha256"]) == 64
        assert any(d.lower().startswith("pytest==") for d in env["distributions"])
        with pytest.raises(L.LancementRefuse, match="commit"):
            L.etat_du_depot(tmp_path)


def valider_factice(brut, auteur, indice, passe=1):
    """Faux validateur (forme seule) ; le vrai (`ideation_v2.valider_fiche_ideation`) est joué au groupe v56."""
    if set(brut) != set(L.CHAMPS_GABARIT):
        raise ValueError("champs hors gabarit")
    return dict(brut, auteur=auteur, passe=passe, identifiant_auteur=f"{auteur}-p{passe}-{indice:02d}", empreinte="0" * 64)


def ecrire_temoins(dossier, sceller_aussi=False, **remplacer):
    dossier.mkdir(parents=True, exist_ok=True)
    for t in tf.TEMOINS:
        f = remplacer.get(t) or temoin_conforme(t, 6000)
        (dossier / f"{t}.json").write_text(json.dumps(f, ensure_ascii=False), encoding="utf-8")
        if sceller_aussi:
            sceller(dossier / f"{t}.json")


class TestTemoins:
    def test_sain(self, tmp_path):
        ecrire_temoins(tmp_path / "t")
        temoins, emp = L.charger_temoins(tmp_path / "t", valider=valider_factice, canaris=CANARIS)
        assert sorted(temoins) == list(tf.TEMOINS) and not set(temoins["T1"]) & set(tf.CHAMPS_INTERNES)
        assert all(L.LONGUEUR_SERVIE[0] <= e["taille_servie"] <= L.LONGUEUR_SERVIE[1] for e in emp.values())

    def test_sans_validateur_refus(self, tmp_path):
        ecrire_temoins(tmp_path / "t")
        with pytest.raises(L.LancementRefuse, match="aucun repli"):
            L.charger_temoins(tmp_path / "t", valider=None)

    @pytest.mark.parametrize("cas", ["court", "etiquette", "cle_en_trop", "canari", "absent"])
    def test_artefacts(self, tmp_path, cas):
        f = temoin_conforme("T4", 6000)
        if cas == "court":
            f = temoin_conforme("T4", 0)
        elif cas == "etiquette":
            f["piege"] += " Écrit par le metteur en forme."
        elif cas == "cle_en_trop":
            f["temoin"] = True
        elif cas == "canari":
            f["piege"] += " Voir " + CANARIS[2] + "."
        ecrire_temoins(tmp_path / "t", T4=f)
        if cas == "absent":
            (tmp_path / "t" / "T6.json").unlink()
        with pytest.raises((L.LancementRefuse, tf.TirageRefuse)):
            L.charger_temoins(tmp_path / "t", valider=valider_factice, canaris=CANARIS)

    @pytest.mark.parametrize("t,modif,motif", [
        ("T1", lambda f: f["loi_predictive"].update(prediction=PRED_T1.replace("0,8", "0,9")), "0,8"),
        ("T2", lambda f: f["loi_predictive"].update(signe="+"), "signe -"),
        ("T3", lambda f: f["loi_predictive"].update(prediction=PRED_T3.replace("écart de 0", "écart nul")), "0,40"),
        ("T4", lambda f: f["loi_predictive"].update(prediction="un gain de 12 minutes"), "aucun nombre"),
        ("T5", lambda f: f["loi_predictive"].update(metrique="relecture humaine"), "Lean"),
        ("T6", lambda f: f["loi_predictive"].update(prediction=PRED_T6.replace("la classe la plus haute", "l'issue 1")),
         "aucun chiffre"),
        ("T6", lambda f: f["loi_predictive"].update(espace_instances="épisodes de banque-t05-v2"), "aucun chiffre"),
        ("T2", lambda f: f.update(nom=f["nom"] + " (T2)"), "étiquette"),
    ])
    def test_transcription_des_descriptions(self, tmp_path, t, modif, motif):  # CL-03, CL-09
        f = temoin_conforme(t, 6000)
        modif(f)
        ecrire_temoins(tmp_path / "t", **{t: f})
        with pytest.raises(L.LancementRefuse, match=motif):
            L.charger_temoins(tmp_path / "t", valider=valider_factice, canaris=CANARIS)

    def test_temoins_scelles_exiges_au_lancement(self, tmp_path):  # CL-09
        ecrire_temoins(tmp_path / "t")
        with pytest.raises(L.LancementRefuse, match="non scellé"):
            L.charger_temoins(tmp_path / "t", valider=valider_factice, canaris=CANARIS, exiger_scelles=True)
        ecrire_temoins(tmp_path / "u", sceller_aussi=True)
        _, emp = L.charger_temoins(tmp_path / "u", valider=valider_factice, canaris=CANARIS, exiger_scelles=True)
        reg = tmp_path / "decisions.md"
        reg.write_text("".join(f"| {t} | `{e['sha256']}` |\n" for t, e in emp.items() if t != "T6"), encoding="utf-8")
        with pytest.raises(L.LancementRefuse, match="T6"):
            L.verifier_registre_temoins(emp, reg)
        with open(reg, "a", encoding="utf-8") as fh:
            fh.write(f"| T6 | `{emp['T6']['sha256']}` |\n")
        assert L.verifier_registre_temoins(emp, reg)

    @v56
    def test_vrai_validateur_v56(self, tmp_path):
        ideation_v2, _ = L.charger_v56(POLE)
        ecrire_temoins(tmp_path / "t")
        temoins, _ = L.charger_temoins(tmp_path / "t", valider=ideation_v2.valider_fiche_ideation, canaris=CANARIS)
        assert len(temoins) == 6
        mauvais = temoin_conforme("T5", 6000)
        mauvais["type"] = "theoreme"
        ecrire_temoins(tmp_path / "u", T5=mauvais)
        with pytest.raises(L.LancementRefuse, match="validateur"):
            L.charger_temoins(tmp_path / "u", valider=ideation_v2.valider_fiche_ideation, canaris=CANARIS)


def transcription(tmp_path, utilisations):
    lignes = [{"type": "assistant", "message": {"content": [{"type": "tool_use", "name": n, "input": i}]}}
              for n, i in utilisations]
    lignes.insert(0, {"type": "user", "message": {"content": "consigne : ni pont/, ni verite-temoins-v1.json"}})
    p = tmp_path / "transcription.jsonl"
    p.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in lignes), encoding="utf-8")
    return p


D = "/home/user/controle-ia-travail/donnees/epreuve-fraiche-pont-v1"
SAINES = [("Read", {"file_path": f"{D}/consigne-metteur-en-forme-temoins-v2.md"}),
          ("Bash", {"command": f"mkdir -p {D}/temoins"}),
          ("Write", {"file_path": f"{D}/temoins/T1.json", "content": "{}"}),
          ("Bash", {"command": f"cd {D} && /home/user/controle-ia-travail/.venv/bin/python -I -B lancer_epreuve_pont_v2.py "
                               "verifier-temoins --pole-v56 /tmp/x/v56-epreuve-pont/orchestrateur-v56"}),
          ("Bash", {"command": f"sha256sum {D}/temoins/T*.json"})]


class TestTranscription:  # CL-09
    def test_saine(self, tmp_path):
        r = L.verifier_transcription(transcription(tmp_path, SAINES))
        assert r == {"utilisations": 5, "signalees": []}

    @pytest.mark.parametrize("mauvaise", [
        ("Read", {"file_path": f"{D}/verite-temoins-v1.json"}),
        ("Read", {"file_path": f"{D}/preregistrement-epreuve-pont-v2.md"}),
        ("Grep", {"pattern": "T1", "path": f"{D}/fiches-tirees"}),
        ("Bash", {"command": f"cat {D}/pont/pont_v1.py"}),
        ("Bash", {"command": f"sed -n 1,50p {D}/lancer_epreuve_pont_v2.py"}),
        ("Read", {"file_path": f"{D}/lancer_epreuve_pont_v2.py"}),
        ("Read", {"file_path": f"{D}/catalogue-public-t05-v2-pont-v1.json"}),
    ])
    def test_artefacts(self, tmp_path, mauvaise):
        r = L.verifier_transcription(transcription(tmp_path, SAINES + [mauvaise]))
        assert len(r["signalees"]) == 1

    def test_illisible_ou_vide_refus(self, tmp_path):
        p = tmp_path / "t.jsonl"
        p.write_text("ceci n'est pas du JSON\n", encoding="utf-8")
        with pytest.raises(L.LancementRefuse, match="illisible"):
            L.verifier_transcription(p)
        with pytest.raises(L.LancementRefuse, match="aucune utilisation"):
            L.verifier_transcription(transcription(tmp_path, []))


# --- bout en bout : lancer() avec toutes ses gardes, faux appelants, vrai code v56 --------------------------------------------

@v56
class TestBoutEnBout:
    @pytest.fixture
    def monde(self, tmp_path, monkeypatch):
        depot = depot_git(tmp_path / "depot")
        dossier = depot / "epreuve"
        dossier.mkdir(parents=True)
        for src, nom in ((L.CATALOGUE, "catalogue.json"), (L.NOYAU, "noyau.json"), (L.VERITE, "verite.json")):
            shutil.copy(src, dossier / nom)
            sceller(dossier / nom)
        pieces = [(f"epreuve/{n}", tf.sha256_fichier(dossier / n)) for n in ("catalogue.json", "noyau.json", "verite.json")]
        prereg = dossier / "prereg.md"
        ecrire_prereg(prereg, VALEUR, pieces=pieces)
        inscrire(depot, tf.sha256_fichier(prereg), tf.sha256_octets(VALEUR.encode("ascii")))
        tf.tirer(prereg=prereg, valeur=VALEUR, sortie=dossier / "fiches-tirees", depot=depot, ref_poussee="HEAD")
        ecrire_temoins(dossier / "temoins", sceller_aussi=True)
        inscrire(depot, *[tf.sha256_fichier(dossier / "temoins" / f"{t}.json") for t in tf.TEMOINS])
        for nom, val in (("DEPOT", depot), ("PREREG", prereg), ("CATALOGUE", dossier / "catalogue.json"),
                         ("NOYAU", dossier / "noyau.json"), ("VERITE", dossier / "verite.json"),
                         ("TIREES", dossier / "fiches-tirees"), ("TEMOINS_DOSSIER", dossier / "temoins")):
            monkeypatch.setattr(L, nom, val)
        monkeypatch.setattr(L, "verifier_go", lambda go_id, **k: [go_id] if go_id == L.GO_ATTENDU else
                            (_ for _ in ()).throw(L.LancementRefuse("GO")))
        return dossier

    def args(self, sortie, **k):
        return argparse.Namespace(pole_v56=POLE, sortie=str(sortie), parallele=2, **k)

    def test_lancer_puis_reprendre_un_refus(self, monde, tmp_path):
        env = {"GO_ID": "GO-2026-11-01-09", "GEMINI_API_KEY": CLE_G}

        def kimi(p, m):
            if MARQUES["T4"] in p and "PRÉAMBULE" not in p:
                return C.Reponse(texte="", modele_servi=m, fin="content_filter", categorie="content_filter",
                                 usage={"entree": 3000, "sortie": 0})
            return reponse_spec(decider_par_marque(p), m, "stop")
        appelants = {"kimi": Faux(kimi), "gemini": Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "STOP"))}
        code, a = L.lancer(self.args(tmp_path / "run1"), appelants=appelants, c=C, environnement=env)
        assert code == 0 and a["cles_trouvees_dans_les_sorties"] == []
        assert a["fiches_traitees"] == 8 and a["temoins_traites"] == 6 and a["refus"] == 1
        assert a["temoins"]["T4"]["juste"] is False and a["temoins"]["T1"]["juste"] is True
        assert a["garde_reelle_v56"]["T1"] == "acceptée" and a["anomalies_garde_reelle_v56"] == []
        for nom in ("manifeste-run.json", "manifeste-run-fin.json", "agregat-v2.json", "journal.jsonl", "environnement-run.json"):
            tf.verifier_compagnon(tmp_path / "run1" / nom)
        debut = L.lire_json(tmp_path / "run1" / "manifeste-run.json")
        assert len(debut["commit_depot"]) == 40 and "attentes=(0,)" in debut["appel_argon"]
        env_run = L.lire_json(tmp_path / "run1" / "environnement-run.json")
        assert env_run["commit_depot"] == debut["commit_depot"] and env_run["distributions"] and env_run["python"]
        assert debut["environnement_sha256"] == tf.sha256_fichier(tmp_path / "run1" / "environnement-run.json")
        with pytest.raises(L.LancementRefuse, match="R12"):
            L.lancer(self.args(tmp_path / "run1"), appelants=appelants, c=C, environnement=env)
        pre = monde / "preambule.md"
        pre.write_text("PRÉAMBULE : tâche de traduction statistique, vocabulaire défini.", encoding="utf-8")
        sceller(pre)
        code, b = L.lancer(self.args(tmp_path / "run2", run_precedent=str(tmp_path / "run1"), preambule=str(pre)),
                           reprise=True, appelants=appelants, c=C, environnement=env)
        assert code == 0 and b["reformules"] == ["T4"] and b["temoins"]["T4"]["juste"] is True and b["temoins_justes"] == 6
        assert b["reformules_premier_tour"]["T4"]["code"] == "N10" and b["depense_usd"] > a["depense_usd"]
        tf.verifier_compagnon(tmp_path / "run2" / "agregat-reprise-v2.json")
        with pytest.raises(L.LancementRefuse, match="une seule reformulation"):
            L.lancer(self.args(tmp_path / "run3", run_precedent=str(tmp_path / "run1"), preambule=str(pre)),
                     reprise=True, appelants=appelants, c=C, environnement=env)

    def test_refus_commit_illisible(self, monde, tmp_path):  # CL-11
        shutil.rmtree(L.DEPOT / ".git")
        with pytest.raises(L.LancementRefuse, match="commit"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})
        assert not (tmp_path / "r" / "environnement-run.json").exists()

    def test_refus_sans_go(self, monde, tmp_path):
        with pytest.raises(L.LancementRefuse):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-08"})
        assert not (tmp_path / "r").exists()

    def test_refus_sans_temoins(self, monde, tmp_path):
        shutil.rmtree(monde / "temoins")
        with pytest.raises(L.LancementRefuse, match="témoin absent"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_refus_temoin_non_scelle(self, monde, tmp_path):
        Path(str(monde / "temoins" / "T3.json") + ".sha256").unlink()
        with pytest.raises(L.LancementRefuse, match="T3 non scellé"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_refus_temoins_non_inscrits(self, monde, tmp_path):
        reg = L.DEPOT / "registres" / "decisions.md"
        reg.write_text("# Décisions (essai, inscriptions retirées)\n", encoding="utf-8")
        with pytest.raises(L.LancementRefuse, match="absentes de registres/decisions.md"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_refus_sans_fiches_tirees(self, monde, tmp_path):
        shutil.rmtree(monde / "fiches-tirees")
        with pytest.raises(L.LancementRefuse, match="fiches tirées absentes"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_refus_preregistrement_non_scelle(self, monde, tmp_path):
        Path(str(L.PREREG) + ".sha256").unlink()
        with pytest.raises(tf.TirageRefuse, match="non scellé"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_agreger_un_run_interrompu(self, monde, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        L.lancer(self.args(tmp_path / "run1"), appelants=appelants, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})
        fin = L.lire_fin(tmp_path / "run1")
        assert fin["mode"] == "principal" and not fin.get("reconstruit")
        (tmp_path / "run1" / "manifeste-run-fin.json").rename(tmp_path / "run1" / "fin-mise-de-cote.json")
        f2 = L.lire_fin(tmp_path / "run1")
        assert f2["reconstruit"] and f2["depense_usd"] == pytest.approx(fin["depense_usd"], abs=1e-5)
        assert f2["appels_en_cours_comptes_au_pire_cas"] == []
