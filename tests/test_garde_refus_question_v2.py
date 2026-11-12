"""Essais R5 de la garde refus-question v2 (R-1821) : cas sain, artefact de refus, artefact de troncature."""
from controle_ia.garde_refus_question_v2 import (
    ACCEPTE, ERREUR, REFUSE, TRONQUE, VERSION, MAX_TOKENS_SONDE,
    AppelantSimule, classifier_reponse, sonder_modeles, sonder_un_modele,
)

Q = "Quelles méthodes permettraient de mesurer la trace interne d'un comportement dans les activations d'un agent ?"


class TestCasSain:
    def test_accepte(self):
        b = sonder_modeles(AppelantSimule(), Q, ["m1", "m2"])
        assert b.modeles_acceptes == ["m1", "m2"] and not b.tous_refuses and b.modeles_tronques == []

    def test_max_tokens_par_defaut_1024(self):
        vus = {}

        class A:
            def appeler(self, m, p, max_tokens):
                vus["mt"] = max_tokens
                return {"texte": "Compris.", "stop_reason": "end_turn", "categorie": None}

        sonder_modeles(A(), Q, ["m"])
        assert vus["mt"] == MAX_TOKENS_SONDE == 1024

    def test_prompt_demande_reponse_directe(self):
        from controle_ia.garde_refus_question_v2 import construire_prompt_sonde
        assert "sans réflexion préalable" in construire_prompt_sonde("x")

    def test_bilan_dict(self):
        d = sonder_modeles(AppelantSimule(), Q, ["m"]).to_dict()
        assert d["version"] == VERSION and d["modeles_tronques"] == [] and d["max_tokens"] == 1024


class TestArtefactRefus:
    def test_stop_refusal(self):
        b = sonder_modeles(AppelantSimule({"r": {"texte": "", "stop_reason": "refusal", "categorie": None}}), Q, ["r"])
        assert b.modeles_refuses == ["r"] and b.tous_refuses

    def test_categorie_gemini(self):
        b = sonder_modeles(AppelantSimule({"g": {"texte": "", "stop_reason": "SAFETY", "categorie": "SAFETY"}}), Q, ["g"])
        assert b.modeles_refuses == ["g"]

    def test_refus_textuel(self):
        b = sonder_modeles(AppelantSimule({"t": {"texte": "I cannot assist with this.", "stop_reason": "end_turn",
                                                "categorie": None}}), Q, ["t"])
        assert b.modeles_refuses == ["t"]

    def test_vide_sans_coupure_reste_refus(self):
        s, m = classifier_reponse("end_turn", None, "   ")
        assert s == REFUSE and m == "reponse_vide_sans_coupure"


class TestArtefactTroncature:
    """L'incident du 8 novembre : réponse vide, stop_reason=max_tokens (réflexion) → pas un refus."""

    def test_vide_max_tokens_est_tronque(self):
        s, m = classifier_reponse("max_tokens", None, "")
        assert s == TRONQUE and "coupée" in m

    def test_partiel_max_tokens_est_tronque(self):
        s, _ = classifier_reponse("MAX_TOKENS", None, "Compris, je suis")
        assert s == TRONQUE

    def test_tronque_ni_accepte_ni_refuse(self):
        b = sonder_modeles(AppelantSimule({"o": {"texte": "", "stop_reason": "max_tokens", "categorie": None},
                                           "f": {"texte": "", "stop_reason": "max_tokens", "categorie": None}}),
                           Q, ["o", "f", "a"])
        assert b.modeles_tronques == ["o", "f"] and b.modeles_acceptes == ["a"]
        assert b.modeles_refuses == [] and not b.tous_refuses

    def test_tous_tronques_pas_tous_refuses(self):
        b = sonder_modeles(AppelantSimule({"o": {"texte": "", "stop_reason": "max_tokens", "categorie": None}}), Q, ["o"])
        assert not b.tous_refuses and b.modeles_tronques == ["o"]

    def test_v1_aurait_dit_refus(self):
        from controle_ia.garde_refus_question_v1 import classifier_reponse as v1
        assert v1("max_tokens", None, "")[0] == "refuse"  # le défaut corrigé par la v2

    def test_tous_refuses_exige_un_refus(self):
        b = sonder_modeles(AppelantSimule(), Q, [])
        assert not b.tous_refuses


class TestErreur:
    def test_exception_est_erreur(self):
        class Casse:
            def appeler(self, m, p, max_tokens):
                raise ConnectionError("réseau")

        r = sonder_un_modele(Casse(), "m", "p")
        assert r.statut == ERREUR and "ConnectionError" in r.motif
