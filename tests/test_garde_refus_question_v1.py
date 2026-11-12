"""Essais R5 de la garde refus-question v1 (R-514).

R5 : toute garde d'arrêt testée sur un cas sain et sur un artefact ; aucun repli silencieux.
"""
import json
import pytest

from controle_ia.garde_refus_question_v1 import (
    ACCEPTE, ERREUR, REFUSE, VERSION,
    AppelantSimule, BilanGarde, ResultatSonde,
    classifier_reponse, construire_prompt_sonde,
    extraire_question, sonder_modeles, sonder_un_modele,
)

QUESTION_SAINE = (
    "Quelles méthodes permettraient de mesurer la diversité des propositions "
    "d'un organisme évolutif dans un espace de conception à haute dimension ?"
)

QUESTION_LONGUE = "A" * 1000


# ---------- Cas sain ----------

class TestCasSain:
    """Un modèle qui accepte la question doit rendre ACCEPTE."""

    def test_modele_unique_accepte(self):
        appelant = AppelantSimule()
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["opus-5-5"])
        assert len(bilan.modeles_acceptes) == 1
        assert bilan.modeles_acceptes == ["opus-5-5"]
        assert not bilan.tous_refuses
        assert bilan.modeles_refuses == []

    def test_plusieurs_modeles_acceptent(self):
        appelant = AppelantSimule()
        modeles = ["opus-5-5", "fable-5-1", "gemini-argon"]
        bilan = sonder_modeles(appelant, QUESTION_SAINE, modeles)
        assert len(bilan.modeles_acceptes) == 3
        assert not bilan.tous_refuses

    def test_question_sha256_calculee(self):
        import hashlib
        appelant = AppelantSimule()
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m1"])
        attendu = hashlib.sha256(QUESTION_SAINE.encode("utf-8")).hexdigest()
        assert bilan.question_sha256 == attendu

    def test_extrait_court_non_tronque(self):
        extrait = extraire_question(QUESTION_SAINE, 500)
        assert "[…tronqué" not in extrait
        assert extrait == QUESTION_SAINE

    def test_extrait_long_tronque(self):
        extrait = extraire_question(QUESTION_LONGUE, 500)
        assert "[…tronqué pour la sonde de pré-vol]" in extrait
        assert len(extrait) < len(QUESTION_LONGUE)

    def test_prompt_sonde_contient_extrait(self):
        prompt = construire_prompt_sonde("un extrait")
        assert "un extrait" in prompt
        assert "remue-méninges" in prompt

    def test_bilan_to_dict(self):
        appelant = AppelantSimule()
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m1"])
        d = bilan.to_dict()
        assert d["version"] == VERSION
        assert d["tous_refuses"] is False
        assert len(d["sondes"]) == 1
        assert d["sondes"][0]["statut"] == ACCEPTE

    def test_classifier_reponse_accepte(self):
        statut, motif = classifier_reponse("end_turn", None, "Compris, je suis prêt.")
        assert statut == ACCEPTE
        assert motif == ""


# ---------- Artefact : refus ----------

class TestArtefact:
    """Un modèle qui refuse doit être consigné et retiré, sans repli silencieux."""

    def test_refus_stop_reason(self):
        """stop_reason=refusal → REFUSE."""
        reponses = {"m-refus": {"texte": "", "stop_reason": "refusal", "categorie": None}}
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m-refus"])
        assert bilan.modeles_refuses == ["m-refus"]
        assert bilan.modeles_acceptes == []
        assert bilan.tous_refuses

    def test_refus_categorie_gemini(self):
        """Catégorie de sécurité Gemini → REFUSE."""
        reponses = {"m-gem": {"texte": "", "stop_reason": "SAFETY", "categorie": "SAFETY"}}
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m-gem"])
        assert bilan.modeles_refuses == ["m-gem"]
        assert bilan.tous_refuses

    def test_refus_reponse_vide(self):
        """Réponse vide → REFUSE."""
        reponses = {"m-vide": {"texte": "", "stop_reason": "end_turn", "categorie": None}}
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m-vide"])
        assert bilan.modeles_refuses == ["m-vide"]

    def test_refus_textuel(self):
        """Refus exprimé dans le texte → REFUSE."""
        reponses = {"m-txt": {"texte": "I cannot assist with this topic.",
                              "stop_reason": "end_turn", "categorie": None}}
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m-txt"])
        assert bilan.modeles_refuses == ["m-txt"]
        sonde = bilan.modeles_sondes[0]
        assert "refus_textuel" in sonde.motif

    def test_refus_textuel_francais(self):
        """Refus en français → REFUSE."""
        reponses = {"m-fr": {"texte": "Je ne peux pas répondre à cette question.",
                             "stop_reason": "end_turn", "categorie": None}}
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m-fr"])
        assert bilan.modeles_refuses == ["m-fr"]

    def test_mixte_accepte_et_refuse(self):
        """Un modèle refuse, l'autre accepte → seul le refusant est retiré."""
        reponses = {"m-refus": {"texte": "", "stop_reason": "refusal", "categorie": None}}
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m-ok", "m-refus"])
        assert bilan.modeles_acceptes == ["m-ok"]
        assert bilan.modeles_refuses == ["m-refus"]
        assert not bilan.tous_refuses

    def test_tous_refusent_code_2(self):
        """Tous les modèles refusent → bilan.tous_refuses."""
        reponses = {
            "m1": {"texte": "", "stop_reason": "refusal", "categorie": None},
            "m2": {"texte": "I cannot assist with this.", "stop_reason": "end_turn", "categorie": None},
        }
        appelant = AppelantSimule(reponses)
        bilan = sonder_modeles(appelant, QUESTION_SAINE, ["m1", "m2"])
        assert bilan.tous_refuses
        assert len(bilan.modeles_refuses) == 2

    def test_erreur_exception(self):
        """Exception pendant l'appel → ERREUR (pas ACCEPTE, pas de repli silencieux)."""
        class AppelantQuiCasse:
            def appeler(self, modele, prompt, max_tokens):
                raise ConnectionError("réseau coupé")

        r = sonder_un_modele(AppelantQuiCasse(), "m-err", "prompt")
        assert r.statut == ERREUR
        assert "ConnectionError" in r.motif

    def test_erreur_ne_compte_pas_comme_accepte(self):
        """Un modèle en erreur n'est pas compté comme accepté."""
        class AppelantQuiCasse:
            def appeler(self, modele, prompt, max_tokens):
                raise RuntimeError("boom")

        appelant_mixte = type("M", (), {
            "appeler": lambda self, m, p, mt: (
                (_ for _ in ()).throw(RuntimeError("boom"))
                if m == "m-err"
                else {"texte": "OK", "stop_reason": "end_turn", "categorie": None}
            )
        })()
        # Plus simple :
        class AppelantMixte:
            def appeler(self, modele, prompt, max_tokens):
                if modele == "m-err":
                    raise RuntimeError("boom")
                return {"texte": "OK prêt", "stop_reason": "end_turn", "categorie": None}

        bilan = sonder_modeles(AppelantMixte(), QUESTION_SAINE, ["m-ok", "m-err"])
        assert bilan.modeles_acceptes == ["m-ok"]
        assert bilan.modeles_en_erreur == ["m-err"]
        assert "m-err" not in bilan.modeles_acceptes


# ---------- Classifier ----------

class TestClassifier:
    def test_refusal_stop(self):
        assert classifier_reponse("refusal", None, "")[0] == REFUSE

    def test_gemini_safety(self):
        assert classifier_reponse("SAFETY", "SAFETY", "")[0] == REFUSE

    def test_gemini_prohibited(self):
        assert classifier_reponse("stop", "PROHIBITED_CONTENT", "blah")[0] == REFUSE

    def test_vide(self):
        assert classifier_reponse("end_turn", None, "")[0] == REFUSE

    def test_espaces_seuls(self):
        assert classifier_reponse("end_turn", None, "   \n  ")[0] == REFUSE

    def test_accepte_normal(self):
        assert classifier_reponse("end_turn", None, "Compris.")[0] == ACCEPTE

    def test_refus_textuel_cannot(self):
        s, m = classifier_reponse("end_turn", None, "I cannot assist with that request.")
        assert s == REFUSE
        assert "i cannot" in m

    def test_refus_textuel_unable(self):
        s, _ = classifier_reponse("end_turn", None, "I'm unable to help with this topic.")
        assert s == REFUSE
