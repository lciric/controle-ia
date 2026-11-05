"""Tests du collisionneur v2, sans aucun appel réseau : les API sont remplacées par des doubles."""
import io
import json
import urllib.error
from pathlib import Path

import pytest

import collisionneur_v2 as cv

FAITS = "# Faits\n\n## Fait 1 (statut : VÉRIFIÉ)\nUn fait.\n\n## Socle technique\nUn socle.\n"
LONG = "Paragraphe de travail. " * 80  # ≈ 1 840 caractères : au-delà de toute troncature à 500


def texte_ok(etiquette):
    return f"# {etiquette}\n\n{LONG}\n\n{cv.MARQUEUR}\n"


class Doubles:
    """Appelants factices : `regles` donne, par identifiant de modèle, une liste de réponses à servir dans l'ordre ;
    au-delà, une réponse OK. Chaque appel est consigné."""

    def __init__(self, regles=None):
        self.regles = {k: list(v) for k, v in (regles or {}).items()}
        self.appels = []

    def _servir(self, modele_id, prompt, max_tokens):
        self.appels.append({"modele": modele_id, "prompt": prompt, "max_tokens": max_tokens})
        file = self.regles.get(modele_id)
        if file:
            return file.pop(0)
        fin = "STOP" if modele_id.startswith("gemini") else "end_turn"
        return cv.Reponse(texte=texte_ok(f"réponse {len(self.appels)}"), modele_servi=modele_id,
                          identifiant=f"id-{len(self.appels)}", fin=fin, usage={"entree": 1000, "sortie": 2000})

    def appelants(self):
        return {"anthropic": self._servir, "gemini": self._servir}


def faits(tmp_path, texte=FAITS, nom="faits.md"):
    chemin = tmp_path / nom
    chemin.write_bytes(texte.encode("utf-8"))
    return str(chemin)


def arbitrage(tmp_path, texte):
    chemin = tmp_path / "arbitrage.md"
    chemin.write_text(texte, encoding="utf-8")
    return str(chemin)


def lancer(argv, doubles):
    return cv.principal(argv, appelants=doubles.appelants())


def cellules(dossier):
    return sorted(p.stem for p in (Path(dossier) / "cellules").glob("*.md"))


# ---------- parcours complet ----------

def test_parcours_complet_et_verification(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert len(cellules(dossier)) == 6
    arb = arbitrage(tmp_path, "RETENUES: E1-T2-attaque-meta-A, E1-T2-attaque-meta-C\n\nJe garde A et C ; B est "
                              "écarté parce qu'il confond méthode et résultat.\n")
    assert lancer(["etage2", "--sortie", str(dossier), "--arbitrage", arb], d) == cv.CODE_FINI
    assert len(cellules(dossier)) == 15
    assert cv.verifier(dossier) == []
    # II.1 ne reçoit que les canons retenus, et la décision de l'arbitre
    p21 = [a["prompt"] for a in d.appels if "Tour II.1" in a["prompt"]]
    assert len(p21) == 3
    for p in p21:
        assert "PIÈCE E1-T2-attaque-meta-A " in p and "PIÈCE E1-T2-attaque-meta-C " in p
        assert "PIÈCE E1-T2-attaque-meta-B " not in p
        assert "B est écarté" in p
    # ce que reçoit I.2 : les trois textes du tour I.1, complets
    p12 = [a["prompt"] for a in d.appels if "Tour I.2" in a["prompt"]][0]
    for l in cv.LETTRES:
        texte = (dossier / "cellules" / f"E1-T1-meta-{l}.md").read_text(encoding="utf-8")
        assert len(texte) > 1500 and texte in p12
    # aucune réponse brute de l'API n'est écrite : pas de fichier JSON hors du journal
    assert not list(dossier.rglob("*.json"))


def test_seuls_les_blocs_texte_sont_injectes(tmp_path):
    d = Doubles({"claude-fable-5-1": [cv.Reponse(texte=texte_ok("A"), modele_servi="claude-fable-5-1",
                                                 fin="end_turn", types_blocs=["thinking", "text"],
                                                 usage={"entree": 10, "sortie": 10})]})
    dossier = tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert "signature" not in (dossier / "journal.jsonl").read_text(encoding="utf-8")


# ---------- blocs vides et relance ----------

def test_bloc_vide_relance_avec_plafond_plus_haut(tmp_path):
    vide = cv.Reponse(texte="", modele_servi="claude-fable-5-1", fin="max_tokens", types_blocs=["thinking"],
                      usage={"entree": 7000, "sortie": 64000})
    d, dossier = Doubles({"claude-fable-5-1": [vide]}), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    essais = cv.essais_journal(dossier, "E1-T1-meta-A")
    assert [e["statut"] for e in essais] == ["VIDE", "OK"]
    assert [e["max_tokens"] for e in essais] == [64000, 128000]
    assert cv.verifier(dossier) == []


def test_vide_deux_fois_ferme_la_porte(tmp_path):
    vide = cv.Reponse(texte="", modele_servi="claude-opus-5-5", fin="max_tokens", usage={"entree": 1, "sortie": 1})
    d, dossier = Doubles({"claude-opus-5-5": [vide, vide]}), tmp_path / "run"
    code = lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d)
    assert code == cv.CODE_PORTE
    assert not any("Tour I.2" in a["prompt"] for a in d.appels)
    assert "E1-T1-meta-B" not in cellules(dossier)
    assert "VIDE" in (dossier / "etat.md").read_text(encoding="utf-8")


def test_sortie_coupee_relance(tmp_path):
    coupe = cv.Reponse(texte="Début d'une réponse coupée", modele_servi="gemini-4-argon", fin="MAX_TOKENS",
                       usage={"entree": 1, "sortie": 32000})
    d, dossier = Doubles({"gemini-4-argon": [coupe]}), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    essais = cv.essais_journal(dossier, "E1-T1-meta-C")
    assert [e["statut"] for e in essais] == ["TRONQUE", "OK"]
    assert [e["max_tokens"] for e in essais] == [32000, 65536]
    # la réponse coupée est gardée comme essai, jamais comme cellule
    assert "coupée" not in (dossier / "cellules" / "E1-T1-meta-C.md").read_text(encoding="utf-8")


# ---------- substitution de modèle, échec, plafond ----------

def test_modele_different_arrete_tout(tmp_path):
    usurpe = cv.Reponse(texte=texte_ok("faux"), modele_servi="claude-3-5-sonnet", fin="end_turn",
                        usage={"entree": 1, "sortie": 1})
    d, dossier = Doubles({"claude-fable-5-1": [usurpe]}), tmp_path / "run"
    code = lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d)
    assert code == cv.CODE_MODELE
    assert len(d.appels) == 1  # aucun autre appel après l'écart
    assert cellules(dossier) == []
    assert cv.essais_journal(dossier)[0]["statut"] == "MODELE_DIFFERENT"


def test_modele_absent_de_la_reponse_arrete(tmp_path):
    sans = cv.Reponse(texte=texte_ok("x"), modele_servi=None, fin="STOP", usage={"entree": 1, "sortie": 1})
    d, dossier = Doubles({"gemini-4-argon": [sans]}), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_MODELE


def test_echec_api_arrete_sans_repli(tmp_path):
    echec = cv.Reponse(echec="HTTP 404 NotFoundError : model not found")
    d, dossier = Doubles({"claude-opus-5-5": [echec]}), tmp_path / "run"
    code = lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d)
    assert code == cv.CODE_ECHEC
    assert [a["modele"] for a in d.appels] == ["claude-fable-5-1", "claude-opus-5-5"]


def test_exception_imprevue_consignee_et_arret(tmp_path):
    def casse(modele_id, prompt, max_tokens):
        raise RuntimeError("réseau tombé")
    dossier = tmp_path / "run"
    code = cv.principal(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)],
                        appelants={"anthropic": casse, "gemini": casse})
    assert code == cv.CODE_ECHEC
    assert cv.essais_journal(dossier)[0]["statut"] == "ECHEC"


def test_plafond_arrete_avant_tout_appel(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    code = lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier), "--plafond-usd", "0.5"], d)
    assert code == cv.CODE_PLAFOND
    assert d.appels == []
    assert not (dossier / "essais").exists()


# ---------- refus ----------

def test_refus_definitif_puis_absence_acceptee(tmp_path):
    refus = cv.Reponse(texte="", modele_servi="claude-opus-5-5", fin="refusal", categorie="reasoning_extraction",
                       usage={"entree": 1, "sortie": 0})
    d, dossier = Doubles({"claude-opus-5-5": [refus]}), tmp_path / "run"
    f = faits(tmp_path)
    assert lancer(["etage1", "--faits", f, "--sortie", str(dossier)], d) == cv.CODE_PORTE
    appels_b = lambda: [a for a in d.appels if a["modele"] == "claude-opus-5-5"]
    assert len(appels_b()) == 1  # pas de relance d'un refus
    # reprise sans décision : la porte reste fermée et le refus n'est pas renvoyé
    assert lancer(["etage1", "--sortie", str(dossier)], d) == cv.CODE_PORTE
    assert len(appels_b()) == 1
    # décision de l'arbitre : continuer sans la cellule refusée
    code = lancer(["etage1", "--sortie", str(dossier), "--accepter-absence", "E1-T1-meta-B"], d)
    assert code == cv.CODE_FINI
    assert len(appels_b()) == 2  # le seul nouvel appel à B est sa cellule I.2
    p12 = [a["prompt"] for a in d.appels if "Tour I.2" in a["prompt"]]
    assert all("PIÈCE ABSENTE E1-T1-meta-B" in p and "statut : REFUS" in p for p in p12)
    journal = cv.lire_journal(dossier)
    assert any(e.get("decision") == "absence_acceptee" and e["cellule"] == "E1-T1-meta-B" for e in journal)
    assert cv.essais_journal(dossier, "E1-T1-meta-B")[0]["categorie_refus"] == "reasoning_extraction"
    assert cv.verifier(dossier) == []


# ---------- entrées immuables, arbitrage ----------

def test_faits_differents_refuses_en_reprise(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    autres = faits(tmp_path, FAITS + "Ajout.\n", "autres.md")
    assert lancer(["etage1", "--faits", autres, "--sortie", str(dossier)], d) == cv.CODE_USAGE


def test_faits_crlf_acceptes_en_reprise(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    f = faits(tmp_path, FAITS.replace("\n", "\r\n"))
    assert lancer(["etage1", "--faits", f, "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert lancer(["etage1", "--faits", f, "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert b"\r" not in (dossier / "faits.md").read_bytes()


def test_reprise_ne_relance_pas_les_cellules_valides(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    n = len(d.appels)
    assert lancer(["etage1", "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert len(d.appels) == n


@pytest.mark.parametrize("texte", ["Pas de ligne retenues\n", "RETENUES: E1-T1-meta-A\n", "RETENUES: \n"])
def test_arbitrage_invalide(tmp_path, texte):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert lancer(["etage2", "--sortie", str(dossier), "--arbitrage", arbitrage(tmp_path, texte)], d) == cv.CODE_USAGE


def test_etage2_exige_un_arbitrage(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert lancer(["etage2", "--sortie", str(dossier)], d) == cv.CODE_USAGE


def test_jamais_ecraser(tmp_path):
    cv.ecrire_neuf(tmp_path / "x.md", "un")
    with pytest.raises(FileExistsError):
        cv.ecrire_neuf(tmp_path / "x.md", "deux")


# ---------- vérificateur ----------

def run_complet(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    return dossier


def test_verifier_detecte_une_cellule_modifiee(tmp_path):
    dossier = run_complet(tmp_path)
    chemin = dossier / "cellules" / "E1-T1-meta-A.md"
    chemin.write_text(chemin.read_text(encoding="utf-8") + "ajout\n", encoding="utf-8")
    assert any("E1-T1-meta-A" in p for p in cv.verifier(dossier))


def test_verifier_detecte_une_piece_tronquee_meme_journal_refait(tmp_path):
    dossier = run_complet(tmp_path)
    base = dossier / "essais" / "E1-T2-attaque-meta-A.essai1.prompt.txt"
    prompt = base.read_text(encoding="utf-8")
    texte_b = (dossier / "cellules" / "E1-T1-meta-B.md").read_text(encoding="utf-8")
    tronque = prompt.replace(texte_b, texte_b[:500])
    assert tronque != prompt
    # falsification complète : prompt, son sceau et le journal réécrits ensemble
    base.write_text(tronque, encoding="utf-8")
    Path(str(base) + ".sha256").write_text(f"{cv.empreinte(tronque)}  {base.name}\n", encoding="utf-8")
    lignes = (dossier / "journal.jsonl").read_text(encoding="utf-8").splitlines()
    refaites = []
    for l in lignes:
        e = json.loads(l)
        if e.get("cellule") == "E1-T2-attaque-meta-A" and e.get("essai") == 1:
            e["sha256_prompt"] = cv.empreinte(tronque)
        refaites.append(json.dumps(e, ensure_ascii=False, sort_keys=True))
    (dossier / "journal.jsonl").write_text("\n".join(refaites) + "\n", encoding="utf-8")
    problemes = cv.verifier(dossier)
    assert any("E1-T1-meta-B injectée tronquée" in p for p in problemes)


def test_verifier_detecte_un_fichier_inattendu(tmp_path):
    dossier = run_complet(tmp_path)
    cv.ecrire_neuf(dossier / "cellules" / "E1-T1-meta-C-argon-cli.md", "écrit à la main")
    assert any("inattendu" in p for p in cv.verifier(dossier))


def test_verifier_detecte_une_cellule_sans_essai_ok(tmp_path):
    dossier = run_complet(tmp_path)
    (dossier / "cellules" / "E1-T2-attaque-meta-C.md").unlink()
    (dossier / "cellules" / "E1-T2-attaque-meta-C.md.sha256").unlink()
    cv.ecrire_neuf(dossier / "cellules" / "E1-T2-attaque-meta-C.md", "texte simulé [MOCK FALLBACK]")
    assert any("E1-T2-attaque-meta-C" in p for p in cv.verifier(dossier))


# ---------- lecture des réponses Gemini ----------

def test_gemini_parties_de_reflexion_exclues():
    rep = cv.lire_reponse_gemini({"modelVersion": "gemini-4-argon", "responseId": "r1",
                                  "candidates": [{"finishReason": "STOP", "content": {"parts": [
                                      {"text": "réflexion", "thought": True}, {"text": "réponse"}]}}],
                                  "usageMetadata": {"promptTokenCount": 5, "candidatesTokenCount": 7,
                                                    "thoughtsTokenCount": 11}})
    assert rep.texte == "réponse" and rep.usage == {"entree": 5, "sortie": 18}
    assert cv.statut_reponse("gemini", rep) == "OK"


@pytest.mark.parametrize("rep,statut", [
    ({"candidates": [{"finishReason": "SAFETY", "content": {"parts": []}}]}, "REFUS"),
    ({"promptFeedback": {"blockReason": "OTHER"}}, "REFUS"),
    ({"candidates": [{"finishReason": "MAX_TOKENS", "content": {"parts": [{"text": "r", "thought": True}]}}]}, "VIDE"),
    ({"candidates": [{"finishReason": "MAX_TOKENS", "content": {"parts": [{"text": "début"}]}}]}, "TRONQUE"),
    ({"candidates": []}, "VIDE"),
    ({"candidates": [{"finishReason": "OTHER", "content": {"parts": [{"text": "x"}]}}]}, "ANOMALIE"),
])
def test_gemini_statuts(rep, statut):
    assert cv.statut_reponse("gemini", cv.lire_reponse_gemini(rep)) == statut


@pytest.mark.parametrize("fin,texte,statut", [
    ("end_turn", "ok", "OK"), ("end_turn", "  ", "VIDE"), ("max_tokens", "", "VIDE"),
    ("max_tokens", "début", "TRONQUE"), ("refusal", "", "REFUS"), ("pause_turn", "x", "ANOMALIE"),
])
def test_anthropic_statuts(fin, texte, statut):
    assert cv.statut_reponse("anthropic", cv.Reponse(texte=texte, fin=fin)) == statut


def test_modele_conforme():
    assert cv.modele_conforme("claude-opus-5-5", "claude-opus-5-5")
    assert cv.modele_conforme("gemini-4-argon", "gemini-4-argon-001")
    assert not cv.modele_conforme("claude-opus-5-5", "claude-opus-5")
    assert not cv.modele_conforme("claude-fable-5-1", "claude-3-5-sonnet")
    assert not cv.modele_conforme("gemini-4-argon", None)


def test_gemini_cle_jamais_dans_les_messages(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "CLE-SECRETE-123")

    def ouvre(requete, context=None, timeout=None):
        assert "CLE-SECRETE-123" not in requete.full_url
        raise urllib.error.HTTPError(requete.full_url, 400, "mauvais", {},
                                     io.BytesIO(b'{"error": "cle CLE-SECRETE-123 refusee"}'))
    monkeypatch.setattr(cv.urllib.request, "urlopen", ouvre)
    rep = cv.appeler_gemini("gemini-4-argon", "p", 10, attentes=(0,))
    assert rep.echec and "CLE-SECRETE-123" not in rep.echec and "[clé]" in rep.echec


def test_gemini_reprend_apres_429(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "k")
    corps = json.dumps({"modelVersion": "gemini-4-argon", "candidates": [
        {"finishReason": "STOP", "content": {"parts": [{"text": "ok"}]}}]}).encode()
    reponses = [urllib.error.HTTPError("u", 429, "trop", {}, io.BytesIO(b"{}")), corps]

    class Corps(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def ouvre(requete, context=None, timeout=None):
        r = reponses.pop(0)
        if isinstance(r, Exception):
            raise r
        return Corps(r)
    monkeypatch.setattr(cv.urllib.request, "urlopen", ouvre)
    rep = cv.appeler_gemini("gemini-4-argon", "p", 10, attentes=(0, 0))
    assert rep.echec is None and rep.texte == "ok"


# ---------- appel Anthropic : forme exacte de la requête, avec les vrais types du SDK ----------

def test_anthropic_requete_et_extraction(monkeypatch):
    anthropic = pytest.importorskip("anthropic")
    from anthropic.types import Message
    message = Message.model_validate({
        "id": "msg_test", "type": "message", "role": "assistant", "model": "claude-opus-5-5",
        "content": [{"type": "thinking", "thinking": "", "signature": "opaque"},
                    {"type": "text", "text": "première partie, "}, {"type": "text", "text": "seconde partie"}],
        "stop_reason": "end_turn", "stop_sequence": None,
        "usage": {"input_tokens": 12, "output_tokens": 34}})
    vus = {}

    class Flux:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def get_final_message(self):
            return message

    class Messages:
        def stream(self, **kwargs):
            vus.update(kwargs)
            return Flux()

    class Client:
        def __init__(self, **kwargs):
            vus["client"] = kwargs
            self.messages = Messages()
    monkeypatch.setattr(anthropic, "Anthropic", Client)
    rep = cv.appeler_anthropic("claude-opus-5-5", "prompt", 64000)
    assert set(vus) == {"client", "model", "max_tokens", "output_config", "messages"}
    assert vus["output_config"] == {"effort": "high"} and vus["max_tokens"] == 64000
    assert "temperature" not in vus and "thinking" not in vus and "fallbacks" not in vus
    assert rep.texte == "première partie, seconde partie"
    assert rep.modele_servi == "claude-opus-5-5" and rep.fin == "end_turn"
    assert rep.usage == {"entree": 12, "sortie": 34} and rep.types_blocs == ["thinking", "text", "text"]


def test_devis_par_etage(tmp_path, capsys):
    sous_totaux = cv.devis(faits(tmp_path))
    assert set(sous_totaux) == {1, 2, 3} and all(v > 0 for v in sous_totaux.values())
    assert sous_totaux[1] + sous_totaux[2] < cv.PLAFOND_DEFAUT_USD
    assert sous_totaux[3] < cv.PLAFOND_DEFAUT_USD
    assert "étage 3" in capsys.readouterr().out


# ---------- étage III : question ciblée de l'arbitre ----------

QUESTION = "# Question\n\nLa pince tient-elle ? Jev en mâchoire externe, sondes et axe de douleur en interne.\n"


def question(tmp_path, texte=QUESTION):
    chemin = tmp_path / "question.md"
    chemin.write_text(texte, encoding="utf-8")
    return str(chemin)


def test_etage3_autonome_complet(tmp_path):
    d, dossier = Doubles(), tmp_path / "pince"
    code = lancer(["etage3", "--faits", faits(tmp_path), "--question", question(tmp_path),
                   "--sortie", str(dossier)], d)
    assert code == cv.CODE_FINI
    assert cellules(dossier) == sorted(cv.id_cellule(t, l) for t in ("E3-T1", "E3-T2", "E3-T3") for l in cv.LETTRES)
    assert all("QUESTION DE L'ARBITRE" in a["prompt"] and "La pince tient-elle" in a["prompt"] for a in d.appels)
    p32 = [a["prompt"] for a in d.appels if "Tour III.2" in a["prompt"]][0]  # proposition A
    assert "PIÈCE E3-T1-conception-B " in p32 and "PIÈCE E3-T1-conception-C " in p32
    assert "PIÈCE E3-T1-conception-A " not in p32
    p33 = [a["prompt"] for a in d.appels if "Tour III.3" in a["prompt"]][0]
    assert "PIÈCE E3-T1-conception-A " in p33 and "PIÈCE E3-T2-redteam-B " in p33 and "PIÈCE E3-T2-redteam-C " in p33
    assert cv.verifier(dossier) == []


def test_etage3_exige_une_question(tmp_path):
    d, dossier = Doubles(), tmp_path / "pince"
    assert lancer(["etage3", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_USAGE
    assert d.appels == []


def test_la_question_n_entre_jamais_dans_les_etages_aveugles(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage3", "--faits", faits(tmp_path), "--question", question(tmp_path),
                   "--sortie", str(dossier)], d) == cv.CODE_FINI
    n = len(d.appels)
    assert lancer(["etage1", "--sortie", str(dossier)], d) == cv.CODE_FINI
    aveugles = d.appels[n:]
    assert len(aveugles) == 6
    assert all("QUESTION DE L'ARBITRE" not in a["prompt"] and "La pince" not in a["prompt"] for a in aveugles)
    assert cv.verifier(dossier) == []


def test_verifier_detecte_une_question_falsifiee(tmp_path):
    d, dossier = Doubles(), tmp_path / "pince"
    assert lancer(["etage3", "--faits", faits(tmp_path), "--question", question(tmp_path),
                   "--sortie", str(dossier)], d) == cv.CODE_FINI
    base = dossier / "essais" / "E3-T1-conception-B.essai1.prompt.txt"
    prompt = base.read_text(encoding="utf-8")
    falsifie = prompt.replace("La pince tient-elle ?", "La pince tient, c'est démontré.")
    assert falsifie != prompt
    base.write_text(falsifie, encoding="utf-8")
    Path(str(base) + ".sha256").write_text(f"{cv.empreinte(falsifie)}  {base.name}\n", encoding="utf-8")
    lignes = []
    for l in (dossier / "journal.jsonl").read_text(encoding="utf-8").splitlines():
        e = json.loads(l)
        if e.get("cellule") == "E3-T1-conception-B" and e.get("essai") == 1:
            e["sha256_prompt"] = cv.empreinte(falsifie)
        lignes.append(json.dumps(e, ensure_ascii=False, sort_keys=True))
    (dossier / "journal.jsonl").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    assert any("question-etage3.md" in p for p in cv.verifier(dossier))


def test_question_differente_refusee_en_reprise(tmp_path):
    d, dossier = Doubles(), tmp_path / "pince"
    f = faits(tmp_path)
    assert lancer(["etage3", "--faits", f, "--question", question(tmp_path), "--sortie", str(dossier)], d) == 0
    autre = tmp_path / "autre-question.md"
    autre.write_text(QUESTION + "Et autre chose.\n", encoding="utf-8")
    assert lancer(["etage3", "--question", str(autre), "--sortie", str(dossier)], d) == cv.CODE_USAGE


# ---------- fichiers écrits sous Windows (Bloc-notes) ----------

def test_marque_d_ordre_des_octets_et_crlf_acceptees(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    f = tmp_path / "faits-bom.md"
    f.write_bytes(b"\xef\xbb\xbf" + FAITS.replace("\n", "\r\n").encode("utf-8"))
    assert lancer(["etage1", "--faits", str(f), "--sortie", str(dossier)], d) == cv.CODE_FINI
    assert not (dossier / "faits.md").read_bytes().startswith(b"\xef\xbb\xbf")
    arb = tmp_path / "arbitrage-bom.md"
    arb.write_bytes(b"\xef\xbb\xbf" + "RETENUES: E1-T2-attaque-meta-A\r\n\r\nDécision.\r\n".encode("utf-8"))
    assert lancer(["etage2", "--sortie", str(dossier), "--arbitrage", str(arb)], d) == cv.CODE_FINI
    assert cv.verifier(dossier) == []


def test_fichier_ansi_refuse_avec_un_message_clair(tmp_path, capsys):
    d, dossier = Doubles(), tmp_path / "run"
    f = tmp_path / "faits-ansi.md"
    f.write_bytes("Fait vérifié, socle établi.\n".encode("cp1252"))
    assert lancer(["etage1", "--faits", str(f), "--sortie", str(dossier)], d) == cv.CODE_USAGE
    assert lancer(["devis", "--faits", str(f)], d) == cv.CODE_USAGE
    assert "UTF-8" in capsys.readouterr().err
    assert d.appels == []


# ---------- Jev, quatrième pôle : auditeur, jamais participant ----------

class DoubleJev:
    """Jev factice : valeurs marquées (0.123456, 0.654321) pour vérifier qu'elles n'entrent dans aucun prompt."""

    def __init__(self, reponses=None, modele="jev-1.14.0"):
        self.reponses = list(reponses or [])
        self.modele = modele
        self.appels = []

    def __call__(self, etat, questions):
        self.appels.append({"etat": etat, "questions": questions})
        if self.reponses:
            return self.reponses.pop(0)
        answers = {}
        for nom, q in questions.items():
            if q["type"] == "noul":
                answers[nom] = {"type": "noul", "noul": 0.123456}
            elif q["type"] == "score":
                answers[nom] = {"type": "score", "score": 3.25, "confidence": 0.7, "probabilities": {}}
            else:
                answers[nom] = {"type": "choice", "choice": "B", "confidence": 0.654321,
                                "probabilities": {"A": 0.2, "B": 0.654321, "C": 0.145679}}
        return {"reponse": {"model": self.modele, "answers": answers,
                            "usage": {"input_tokens": 5000, "output_tokens": 128}}}


def lancer_avec_jev(argv, doubles, jev):
    appelants = doubles.appelants()
    appelants["jev"] = jev
    return cv.principal(argv, appelants=appelants)


def test_jev_jamais_appele_sans_option(tmp_path):
    d, jev, dossier = Doubles(), DoubleJev(), tmp_path / "run"
    assert lancer_avec_jev(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d, jev) == cv.CODE_FINI
    assert jev.appels == [] and not (dossier / "jev").exists()


def test_jev_audite_chaque_cellule_seule(tmp_path):
    d, jev, dossier = Doubles(), DoubleJev(), tmp_path / "run"
    code = lancer_avec_jev(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier), "--jev"], d, jev)
    assert code == cv.CODE_FINI
    assert len(jev.appels) == 6  # une par cellule, aucune comparaison conjointe
    # Jev ne lit jamais deux propositions ensemble : chaque état est le texte d'une seule cellule
    textes = {(dossier / "cellules" / f"{c}.md").read_text(encoding="utf-8") for c in cellules(dossier)}
    assert all(isinstance(a["etat"], str) and a["etat"] in textes for a in jev.appels)
    assert all(set(a["questions"]) == set(cv.QUESTIONS_JEV) for a in jev.appels)
    assert all(e["statut_jev"] == "OK" for e in cv.audits_jev(dossier))
    # les notes de Jev ne vont qu'à l'arbitre : aucune n'entre dans un prompt des modèles
    assert not any("0.123456" in a["prompt"] for a in d.appels)
    # elles sont dans un fichier à part, à lire après les cellules ; etat.md n'en donne que le chemin
    etat = (dossier / "etat.md").read_text(encoding="utf-8")
    assert "jev/notes-jev.md" in etat and "0.12" not in etat
    notes = (dossier / "jev" / "notes-jev.md").read_text(encoding="utf-8")
    assert "Lis d'abord les cellules" in notes and "0.12" in notes and "3.25" in notes
    assert cv.verifier(dossier) == []


def test_jev_en_echec_n_arrete_pas_le_run(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    jev = DoubleJev(reponses=[{"echec": "HTTP 401 : clé refusée"}] * 6)
    code = lancer_avec_jev(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier), "--jev"], d, jev)
    assert code == cv.CODE_FINI and len(cellules(dossier)) == 6
    assert {e["statut_jev"] for e in cv.audits_jev(dossier)} == {"ECHEC"}
    assert "ECHEC" in (dossier / "jev" / "notes-jev.md").read_text(encoding="utf-8")
    assert cv.verifier(dossier) == []


def test_jev_autre_modele_consigne_comme_tel(tmp_path):
    d, jev, dossier = Doubles(), DoubleJev(modele="jev-1.13.0"), tmp_path / "run"
    code = lancer_avec_jev(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier), "--jev"], d, jev)
    assert code == cv.CODE_FINI
    assert {e["statut_jev"] for e in cv.audits_jev(dossier)} == {"MODELE_DIFFERENT"}
    assert all(e["reponses"] is None for e in cv.audits_jev(dossier))  # aucune note gardée d'un autre modèle


def test_jev_ajoute_en_reprise_sans_rappeler_les_modeles(tmp_path):
    d, jev, dossier = Doubles(), DoubleJev(), tmp_path / "run"
    f = faits(tmp_path)
    assert lancer_avec_jev(["etage1", "--faits", f, "--sortie", str(dossier)], d, jev) == cv.CODE_FINI
    n = len(d.appels)
    assert lancer_avec_jev(["etage1", "--sortie", str(dossier), "--jev"], d, jev) == cv.CODE_FINI
    assert len(d.appels) == n and len(jev.appels) == 6
    assert lancer_avec_jev(["etage1", "--sortie", str(dossier), "--jev"], d, jev) == cv.CODE_FINI
    assert len(jev.appels) == 6  # rien n'est réaudité


def test_jev_compte_dans_la_depense(tmp_path):
    d, dossier = Doubles(), tmp_path / "run"
    assert lancer(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier)], d) == cv.CODE_FINI
    sans = cv.depense(dossier)
    assert lancer_avec_jev(["etage1", "--sortie", str(dossier), "--jev"], d, DoubleJev()) == cv.CODE_FINI
    assert abs(cv.depense(dossier) - sans - 6 * 5000 / 1e6 * cv.JEV["prix_entree"]) < 1e-6


def test_verifier_detecte_une_reponse_jev_modifiee(tmp_path):
    d, jev, dossier = Doubles(), DoubleJev(), tmp_path / "run"
    assert lancer_avec_jev(["etage1", "--faits", faits(tmp_path), "--sortie", str(dossier), "--jev"], d, jev) == 0
    chemin = dossier / "jev" / "E1-T1-meta-B.jev1.reponse.json"
    chemin.write_text(chemin.read_text(encoding="utf-8").replace("0.123456", "0.9"), encoding="utf-8")
    assert any("Jev, E1-T1-meta-B" in p for p in cv.verifier(dossier))


def test_jev_forme_exacte_de_la_requete_et_cle_masquee(monkeypatch):
    monkeypatch.setenv("TYPESAFE_API_KEY", "CLE-JEV-SECRETE")
    vues = {}

    def ouvre(requete, context=None, timeout=None):
        vues["url"] = requete.full_url
        vues["auth"] = requete.get_header("Authorization")
        vues["type"] = requete.get_header("Content-type")
        vues["long"] = requete.get_header("Typesafe-danger-zone-long-context")
        vues["corps"] = json.loads(requete.data.decode("utf-8"))
        raise urllib.error.HTTPError(requete.full_url, 401, "non", {},
                                     io.BytesIO(b'{"detail": "cle CLE-JEV-SECRETE invalide"}'))
    monkeypatch.setattr(cv.urllib.request, "urlopen", ouvre)
    res = cv.appeler_jev("état", cv.QUESTIONS_JEV, attentes=(0,))
    assert vues["url"] == "https://api.typesafe.ai/v1/systemone"
    assert vues["auth"] == "Bearer CLE-JEV-SECRETE" and vues["type"] == "application/json" and vues["long"] == "true"
    assert vues["corps"] == {"model": "jev-1.14.0", "state": "état", "questions": cv.QUESTIONS_JEV}
    assert "CLE-JEV-SECRETE" not in res["echec"] and "[clé]" in res["echec"]


def test_questions_jev_conformes_a_la_documentation():
    assert not hasattr(cv, "QUESTION_COMPARAISON_JEV")  # aucune question de classement
    for nom, q in cv.QUESTIONS_JEV.items():
        assert q["type"] in {"noul", "choice", "score"} and q["instructions"]
        if q["type"] == "choice":
            assert isinstance(q["criteria"], dict) and 1 <= len(q["criteria"]) <= 255
        if q["type"] == "score":
            assert isinstance(q["criteria"], list) and 1 <= len(q["criteria"]) <= 10
        if q["type"] == "noul" and "criteria" in q:
            assert set(q["criteria"]) <= {"true", "false"}


def test_commande_jev_test(capsys):
    assert cv.principal(["jev-test"], appelants={"jev": DoubleJev()}) == cv.CODE_FINI
    assert "jev-1.14.0" in capsys.readouterr().out
    assert cv.principal(["jev-test"], appelants={"jev": DoubleJev(modele="jev-latest-2")}) == cv.CODE_MODELE
    assert cv.principal(["jev-test"], appelants={"jev": DoubleJev(reponses=[{"echec": "HTTP 401"}])}) == cv.CODE_ECHEC


def test_anthropic_entete_espace_de_travail(monkeypatch):
    """v2.6 : l'en-tête anthropic-workspace-id n'est envoyé que si ANTHROPIC_WORKSPACE_ID est défini."""
    import anthropic
    vus = {}

    class Faux:
        def __init__(self, **kw):
            vus.update(kw)
            raise RuntimeError("stop avant tout appel")
    monkeypatch.setattr(anthropic, "Anthropic", Faux)
    monkeypatch.setenv("ANTHROPIC_WORKSPACE_ID", "wrkspc_essai")
    with pytest.raises(RuntimeError):
        cv.appeler_anthropic("claude-opus-5-5", "x", 10)
    assert vus["default_headers"] == {"anthropic-workspace-id": "wrkspc_essai"} and vus["max_retries"] == 4
    vus.clear()
    monkeypatch.delenv("ANTHROPIC_WORKSPACE_ID")
    with pytest.raises(RuntimeError):
        cv.appeler_anthropic("claude-opus-5-5", "x", 10)
    assert vus.get("default_headers") is None
