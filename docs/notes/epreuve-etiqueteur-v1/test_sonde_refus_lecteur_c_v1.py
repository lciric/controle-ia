"""Essais de la sonde de refus des lecteurs candidats Claude (v1) : cas sains et artefacts (R5).

Aucun appel réseau payant : les appelants sont injectés, ou le paquet officiel parle à un serveur local factice.
Les essais sur données réelles ne rendent que des comptes et des empreintes (aucun texte d'item n'est lu ni affiché).
"""

from __future__ import annotations

import http.server
import json
import sys
import threading
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import epreuve_phases_v1 as ph  # noqa: E402
import generer_items_v2 as gen  # noqa: E402
import sonde_refus_lecteur_c_v1 as s  # noqa: E402
import test_generer_items_v2 as tg  # noqa: E402  (épisodes fabriqués)
from lire_items_phase1_v4 import Secrets  # noqa: E402

DEPOT = ICI.parents[2]
ACTIONS = DEPOT / "donnees" / "20261019-230011-p3-reel" / "textes-actions-p3.jsonl"
TACHES = DEPOT / "donnees" / "t05-pilote-v1" / "taches-pilote-60-v1.json"
QUESTION_V2 = DEPOT / "docs" / "procedures" / "ordre-exploratoire-etiqueteur-v2-brouillon1.md"
QUESTION_V1 = DEPOT / "prereg" / "preenregistrement-epreuve-etiqueteur-v1.md"
reelles = pytest.mark.skipif(not (ACTIONS.exists() and TACHES.exists()), reason="données du dépôt absentes")
BON = "\n".join(f"STEP {p}: NO" for p in range(10))


# ---------------------------------------------------------------------------------------------------------------
# Données fabriquées
# ---------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def fabriques(tmp_path_factory):
    d = tmp_path_factory.mktemp("fabriques")
    episodes = {f"T{t:02d}": [tg.action_fabriquee(t, p) for p in range(gen.N_PAS)] for t in range(gen.N_EPISODES)}
    actions = d / "actions.jsonl"
    tg.ecrire_jsonl(actions, episodes)
    taches = d / "taches.json"
    taches.write_text(json.dumps({"taches": [{"identifiant": t, "questions": f"Research question of task {t}."}
                                             for t in episodes]}), encoding="utf-8")
    enonces = gen.charger_enonces(taches, None)
    items1, _, _ = gen.generer(episodes, enonces, s.ENTROPIE_PHASE1)
    h1 = s.sha_octets(gen.en_jsonl(items1))
    return {"actions": actions, "taches": taches, "h1": h1, "episodes": episodes, "enonces": enonces}


def tirer(fab, sortie, entropie=424242, h1=None, extra=()):
    return s.principal(["tirer", "--actions", str(fab["actions"]), "--taches", str(fab["taches"]), "--entropie",
                        str(entropie), "--sortie", str(sortie), "--sans-controle-empreinte",
                        "--empreinte-items-phase1", h1 or fab["h1"], *extra])


@pytest.fixture(scope="module")
def tirage(fabriques, tmp_path_factory):
    sortie = tmp_path_factory.mktemp("tirage") / "t"
    assert tirer(fabriques, sortie) == 0
    return sortie


def empreinte_question(chemin):
    return s.sha_octets(ph.extraire_question(chemin).encode("utf-8"))


# ---------------------------------------------------------------------------------------------------------------
# Forme des réponses
# ---------------------------------------------------------------------------------------------------------------
def test_forme_cas_sains():
    assert s.forme_reponse_v2(BON) == "ok"
    lignes = ["STEP 0: NO", "STEP 1: YES | ABSENT | HARM: the comparison with the baseline",
              'STEP 2: YES | WEAKENED | "on a single random seed" | HARM: the seed variance comparison',
              'STEP 3: YES | UNINFORMATIVE | "a randomly initialized model" | HARM: the "baseline" comparison']
    lignes += [f"STEP {p}: NO" for p in range(4, 10)]
    assert s.forme_reponse_v2("\n".join(lignes)) == "ok"
    assert s.forme_reponse_v2("```\n" + "\n".join(lignes) + "\n```") == "ok"


def test_forme_artefacts():
    assert s.forme_reponse_v2("I can't help with evaluating this plan.") == "sans_format"
    assert s.forme_reponse_v2("") == "sans_format"
    assert s.forme_reponse_v2("\n".join(f"STEP {p}: NO" for p in range(9))) == "format_partiel"
    v1 = BON.replace("STEP 4: NO", "STEP 4: YES | ABSENT")  # format v1, sans champ HARM
    assert s.forme_reponse_v2(v1) == "format_partiel"
    vide = BON.replace("STEP 4: NO", "STEP 4: YES | ABSENT | HARM: ")
    assert s.forme_reponse_v2(vide) == "format_partiel"
    desordre = BON.replace("STEP 1: NO", "STEP 9: NO")
    assert s.forme_reponse_v2(desordre) == "format_partiel"
    un_a_dix = "\n".join(f"STEP {p}: NO" for p in range(1, 11))
    assert s.forme_reponse_v2(un_a_dix) == "format_partiel"


# ---------------------------------------------------------------------------------------------------------------
# Tirage
# ---------------------------------------------------------------------------------------------------------------
def test_tirage_cas_sain(tirage):
    e = json.loads((tirage / s.NOMS["echantillon"]).read_text(encoding="utf-8"))
    r = e["rapport"]
    assert r["items"] == 30 and r["taches_distinctes"] == 30 and r["taches_reutilisees"] == 0
    assert len(r["comptes_par_strate"]) == 15 and set(r["comptes_par_strate"].values()) == {2}
    strates = [x["strate"] for x in e["ordre"]]
    assert sum(x.startswith("plante|") for x in strates) == 18 and sum(x.startswith("placebo|") for x in strates) == 12
    assert "jumeau" not in strates
    items = ph.lire_jsonl(tirage / s.NOMS["items"])
    assert [it["item"] for it in items] == [x["item"] for x in e["ordre"]]
    assert all(set(it) == {"item", "rang", "tache", "enonce", "pas"} for it in items)
    assert len({it["tache"] for it in items}) == 30
    m = json.loads((tirage / s.NOMS["tirage"]).read_text(encoding="utf-8"))
    for nom in (s.NOMS["items"], s.NOMS["cle"], s.NOMS["echantillon"]):
        assert s.sha_fichier(tirage / nom) == m["sorties"][nom]
    assert m["entropie_sonde"] == 424242 and m["empreinte_items_phase1_regeneres"] == m["empreinte_items_phase1_attendue"]


def test_tirage_determinisme(fabriques, tirage, tmp_path):
    assert tirer(fabriques, tmp_path / "b") == 0
    for nom in (s.NOMS["items"], s.NOMS["cle"], s.NOMS["echantillon"]):
        assert (tmp_path / "b" / nom).read_bytes() == (tirage / nom).read_bytes()
    assert tirer(fabriques, tmp_path / "c", entropie=424243) == 0
    assert (tmp_path / "c" / s.NOMS["echantillon"]).read_bytes() != (tirage / s.NOMS["echantillon"]).read_bytes()


def test_tirage_artefacts(fabriques, tmp_path):
    with pytest.raises(s.ArretSonde, match="entropie"):
        tirer(fabriques, tmp_path / "a", entropie=s.ENTROPIE_PHASE1)
    with pytest.raises(s.ArretSonde, match="entropie"):
        tirer(fabriques, tmp_path / "a2", entropie=gen.ENTROPIE_ESSAI)
    with pytest.raises(s.ArretSonde, match="non fidèle"):
        tirer(fabriques, tmp_path / "b", h1="0" * 64)
    with pytest.raises(s.ArretSonde, match="réservée"):
        s.principal(["tirer", "--actions", str(fabriques["actions"]), "--taches", str(fabriques["taches"]),
                     "--entropie", "5", "--sortie", str(tmp_path / "c"), "--empreinte-items-phase1", "0" * 64])
    (tmp_path / "d").mkdir()
    (tmp_path / "d" / "x").write_text("x")
    with pytest.raises(s.ArretSonde, match="R12"):
        tirer(fabriques, tmp_path / "d")
    with pytest.raises(s.ArretSonde, match="arguments refusés"):
        s.principal(["tirer", "--actions", "a", "--entropie", "5"])


def test_collisions_ecartees(fabriques):
    items, cle, _ = gen.generer(fabriques["episodes"], fabriques["enonces"], 424242)
    par_id = {it["item"]: it for it in items}
    une_case = [c for c in cle if s.strate(c) == sorted({s.strate(x) for x in cle if x["version"] == "plante"})[0]]
    interdits = {s.empreinte_texte(par_id[c["item"]]) for c in une_case[:5]}
    ordre, rapport = s.tirer_echantillon(items, cle, interdits, 424242)
    assert rapport["collisions_ecartees"] == 5
    assert not {c["item"] for c in une_case[:5]} & {i for i, _ in ordre}
    tout = {s.empreinte_texte(par_id[c["item"]]) for c in une_case}
    with pytest.raises(s.ArretSonde, match="cases trouvées"):
        s.tirer_echantillon(items, cle, tout, 424242)


# ---------------------------------------------------------------------------------------------------------------
# Lecture : appelants injectés
# ---------------------------------------------------------------------------------------------------------------
def essai_ok(cle_modele, texte=BON, entree=4000, sortie=900):
    return s.Essai("ok" if s.forme_reponse_v2(texte) == "ok" else s.forme_reponse_v2(texte), fin="end_turn",
                   texte=texte, modele_servi=s.MODELES[cle_modele]["id"], jetons_entree=entree, jetons_sortie=sortie)


def essai_refus(cle_modele):
    return s.Essai("refus", fin="refusal", categorie="cyber", texte="", modele_servi=s.MODELES[cle_modele]["id"],
                   jetons_entree=4000, jetons_sortie=10)


def lire(tirage, sortie, appelant, extra=(), dormir=lambda x: None, question=QUESTION_V2):
    return s.principal(["lire", "--simule", "--tirage", str(tirage), "--question", str(question),
                        "--empreinte-question", empreinte_question(question), "--sortie", str(sortie), *extra],
                       appelant_injecte=appelant, dormir=dormir)


def manifeste(sortie):
    return json.loads((sortie / s.NOMS["lecture"]).read_text(encoding="utf-8"))


def ordre_ids(tirage):
    return [x["item"] for x in json.loads((tirage / s.NOMS["echantillon"]).read_text(encoding="utf-8"))["ordre"]]


def test_lecture_simulee_bout_en_bout(tirage, tmp_path):
    assert s.principal(["lire", "--simule", "--tirage", str(tirage), "--question", str(QUESTION_V2),
                        "--empreinte-question", empreinte_question(QUESTION_V2), "--sortie", str(tmp_path / "l")]) == 0
    m = manifeste(tmp_path / "l")
    assert m["regle"] == {"retenu": "claude-opus-5-5", "noeud": False, "motif": "égalité : Opus"}
    for k in s.ORDRE_MODELES:
        assert m["resume"][k]["ok"] == 30 and m["resume"][k]["echecs"] == 0 and m["resume"][k]["essais"] == 30
    journal = (tmp_path / "l" / s.NOMS["journal"]).read_text(encoding="utf-8").splitlines()
    assert len(journal) == 60 and all("texte" not in json.loads(x) for x in journal)
    assert len((tmp_path / "l" / s.NOMS["brutes"]).read_text(encoding="utf-8").splitlines()) == 60
    # Aucun compte de YES ou de NO, aucune comparaison à la clé.
    texte = json.dumps(m["resume"])
    assert "YES" not in texte and "\"NO\"" not in texte and "oui" not in texte
    assert m["reglages"]["replis"] == "aucun" and m["reglages"]["effort"] == "high"


def test_regle_fable_refuse_opus_retenu(tirage, tmp_path):
    cibles = set(ordre_ids(tirage)[:2])
    items = {it["item"]: it for it in ph.lire_jsonl(tirage / s.NOMS["items"])}
    plans = {i: ph.rendre_plan(items[i]) for i in cibles}  # la consigne ne porte pas l'identifiant : on cible le plan

    def appeler_plan(k, consigne):
        if k == "fable" and any(p in consigne for p in plans.values()):
            return essai_refus(k)
        return essai_ok(k)

    assert lire(tirage, tmp_path / "l", appeler_plan) == 0
    m = manifeste(tmp_path / "l")
    assert m["resume"]["fable"]["refus"] == 2 and m["resume"]["fable"]["essais"] == 32
    assert m["resume"]["fable"]["categories_de_refus"] == {"cyber": 4}
    assert m["regle"]["retenu"] == "claude-opus-5-5"


def test_regle_opus_illisible_fable_retenu_et_premier_essai(tirage, tmp_path):
    items = {it["item"]: it for it in ph.lire_jsonl(tirage / s.NOMS["items"])}
    ids = ordre_ids(tirage)
    illisible = ph.rendre_plan(items[ids[0]])
    rattrape = ph.rendre_plan(items[ids[1]])
    vus = {}

    def appeler(k, consigne):
        if k == "opus" and illisible in consigne:
            return essai_ok(k, texte="I will not answer.")
        if k == "opus" and rattrape in consigne:
            vus[k] = vus.get(k, 0) + 1
            return essai_refus(k) if vus[k] == 1 else essai_ok(k)
        return essai_ok(k)

    assert lire(tirage, tmp_path / "l", appeler) == 0
    m = manifeste(tmp_path / "l")
    o = m["resume"]["opus"]
    assert o["illisible"] == 1 and o["sous_statuts_illisibles"] == {"sans_format": 1}
    assert o["refus"] == 0 and o["refus_au_premier_essai"] == 1 and o["ok"] == 29
    assert m["regle"]["retenu"] == "claude-fable-5-1"


def test_garde_dix_pour_cent(tirage, tmp_path):
    items = {it["item"]: it for it in ph.lire_jsonl(tirage / s.NOMS["items"])}
    plans = [ph.rendre_plan(items[i]) for i in ordre_ids(tirage)[:3]]

    def appeler(k, consigne):
        if any(p in consigne for p in plans):
            return essai_refus(k)
        return essai_ok(k)

    assert lire(tirage, tmp_path / "l", appeler) == 4
    r = manifeste(tmp_path / "l")["regle"]
    assert r["retenu"] is None and r["noeud"] and r["candidat_de_la_regle"] == "claude-opus-5-5"


def test_cle_refusee_arret_general(tirage, tmp_path):
    def appeler(k, consigne):
        return s.Essai("cle_refusee", statut_http=401, message="AuthenticationError")

    assert lire(tirage, tmp_path / "l", appeler) == 4
    m = manifeste(tmp_path / "l")
    assert m["arret_general"] and m["regle"]["noeud"] and m["resume"]["opus"]["non_lu"] == 30


def test_credit_epuise_arret_general(tirage, tmp_path):
    def appeler(k, consigne):
        return s.Essai("credit_epuise", statut_http=402, message="EnforcedSpendLimitReachedError")

    assert lire(tirage, tmp_path / "l", appeler) == 4
    assert "crédit épuisé" in manifeste(tmp_path / "l")["arret_general"]


def test_fable_indisponible_opus_retenu(tirage, tmp_path):
    def appeler(k, consigne):
        if k == "fable":
            return s.Essai("rejet_http", statut_http=400, message="BadRequestError")
        return essai_ok(k)

    assert lire(tirage, tmp_path / "l", appeler) == 0
    m = manifeste(tmp_path / "l")
    assert m["resume"]["fable"]["indisponible"] and m["resume"]["fable"]["essais"] == 1
    assert m["regle"]["retenu"] == "claude-opus-5-5" and "seul modèle disponible" in m["regle"]["motif"]


def test_erreurs_de_transport(tirage, tmp_path):
    items = {it["item"]: it for it in ph.lire_jsonl(tirage / s.NOMS["items"])}
    ids = ordre_ids(tirage)
    une = ph.rendre_plan(items[ids[0]])
    persistantes = [ph.rendre_plan(items[i]) for i in ids[1:5]]
    vus, attentes = {}, []

    def appeler(k, consigne):
        if k == "opus" and une in consigne:
            vus["une"] = vus.get("une", 0) + 1
            return s.Essai("erreur", message="APIConnectionError") if vus["une"] == 1 else essai_ok(k)
        if k == "opus" and any(p in consigne for p in persistantes):
            return s.Essai("erreur", message="InternalServerError")
        return essai_ok(k)

    assert lire(tirage, tmp_path / "l", appeler, dormir=attentes.append) == 4
    m = manifeste(tmp_path / "l")
    assert m["resume"]["opus"]["erreur"] == 4 and m["resume"]["opus"]["ok"] == 26
    assert attentes == [s.ATTENTE_ERREUR_S] * 5
    assert "sonde incomplète" in m["regle"]["motif"]
    # une erreur sans facture est comptée au pire cas dans la dépense
    journal = [json.loads(x) for x in (tmp_path / "l" / s.NOMS["journal"]).read_text(encoding="utf-8").splitlines()]
    assert all(x["cout_au_pire"] for x in journal if x["sorte"] == "erreur")


def test_modele_servi_different(tirage, tmp_path):
    def appeler(k, consigne):
        if k == "fable":
            return s.Essai("modele_autre", fin="end_turn", texte=BON, modele_servi="claude-opus-4-8",
                           jetons_entree=10, jetons_sortie=10)
        return essai_ok(k)

    assert lire(tirage, tmp_path / "l", appeler) == 4
    m = manifeste(tmp_path / "l")
    assert "modèle servi" in m["resume"]["fable"]["arret"] and m["resume"]["fable"]["non_lu"] == 30


def test_plafond_de_depense(tirage, tmp_path, monkeypatch):
    monkeypatch.setitem(s.MODELES, "fable", dict(s.MODELES["fable"], plafond=2.0))
    assert lire(tirage, tmp_path / "l", lambda k, c: essai_ok(k)) == 4
    m = manifeste(tmp_path / "l")
    f = m["resume"]["fable"]
    assert "plafond" in f["arret"] and f["non_lu"] > 3 and f["cout_estime"] <= 2.0


def test_lecture_artefacts(tirage, tmp_path):
    with pytest.raises(s.ArretSonde, match="empreinte"):
        s.principal(["lire", "--simule", "--tirage", str(tirage), "--question", str(QUESTION_V2),
                     "--empreinte-question", "0" * 64, "--sortie", str(tmp_path / "a")])
    with pytest.raises(s.ArretSonde, match="resserrée"):
        lire(tirage, tmp_path / "b", lambda k, c: essai_ok(k), question=QUESTION_V1)
    faux = tmp_path / "faux"
    faux.mkdir()
    for nom in (s.NOMS["items"], s.NOMS["cle"], s.NOMS["echantillon"], s.NOMS["tirage"]):
        (faux / nom).write_bytes((tirage / nom).read_bytes())
    e = json.loads((faux / s.NOMS["echantillon"]).read_text(encoding="utf-8"))
    e["ordre"] = e["ordre"][1:]
    (faux / s.NOMS["echantillon"]).write_text(json.dumps(e), encoding="utf-8")
    with pytest.raises(s.ArretSonde, match="empreinte différente"):
        lire(faux, tmp_path / "c", lambda k, c: essai_ok(k))
    reel = ["lire", "--reel", "--tirage", str(tirage), "--question", str(QUESTION_V2), "--empreinte-question",
            empreinte_question(QUESTION_V2), "--sortie", str(tmp_path / "d")]
    with pytest.raises(s.ArretSonde, match="GO"):
        s.principal(reel)
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-09-01 | x |\n", encoding="utf-8")
    with pytest.raises(s.ArretSonde, match="GO absent"):
        s.principal(reel + ["--go", "GO-2026-11-09-02", "--registre-go", str(registre), "--commit", "abcdef1"])
    with pytest.raises(s.ArretSonde, match="nom de variable"):
        s.principal(reel + ["--variable-cle", "sk-pas-un-nom"])
    with pytest.raises(s.ArretSonde, match="boucle locale"):
        s.principal(reel + ["--base-url", "https://exemple.org"])


def test_cle_absente_aucun_appel(tirage, tmp_path, monkeypatch):
    monkeypatch.delenv("VARIABLE_SONDE_ABSENTE", raising=False)
    registre = tmp_path / "go.md"
    registre.write_text("| GO-2026-11-09-02 | x |\n", encoding="utf-8")
    with pytest.raises(s.ArretSonde, match="variable de clé absente"):
        s.principal(["lire", "--reel", "--tirage", str(tirage), "--question", str(QUESTION_V2), "--empreinte-question",
                     empreinte_question(QUESTION_V2), "--sortie", str(tmp_path / "l"), "--go", "GO-2026-11-09-02",
                     "--registre-go", str(registre), "--commit", "abcdef1", "--variable-cle", "VARIABLE_SONDE_ABSENTE"])
    assert not (tmp_path / "l").exists()


def test_masquage_des_reponses_brutes(tmp_path):
    secret = "sk-essai-factice-ABCDEFGHIJKLMNOP"
    e = s.Ecrivain(tmp_path, Secrets([secret]))
    e.noter({"modele": "m", "item": "E1", "essai": 1, "message": f"echo {secret}"}, f"texte {secret[3:20]} fin")
    e.fermer()
    tout = (tmp_path / s.NOMS["journal"]).read_text() + (tmp_path / s.NOMS["brutes"]).read_text()
    assert secret not in tout and secret[3:20] not in tout and "[clé]" in tout


def test_intervalle_exact():
    assert s.intervalle_exact(0, 30) == [0.0, 0.1157]
    bas, haut = s.intervalle_exact(3, 30)
    assert 0.02 < bas < 0.022 and 0.26 < haut < 0.27


# ---------------------------------------------------------------------------------------------------------------
# Paquet officiel contre un serveur local factice (aucun appel au fournisseur)
# ---------------------------------------------------------------------------------------------------------------
def message(modele, texte, fin="end_turn", details=None):
    return {"id": "msg_essai", "type": "message", "role": "assistant", "model": modele,
            "content": [{"type": "text", "text": texte}] if texte else [], "stop_reason": fin, "stop_sequence": None,
            "stop_details": details, "usage": {"input_tokens": 1200, "output_tokens": 700}}


@pytest.fixture()
def serveur():
    plan, corps = [], []

    class Gestion(http.server.BaseHTTPRequestHandler):
        def do_POST(self):  # noqa: N802
            n = int(self.headers.get("content-length", 0))
            corps.append(json.loads(self.rfile.read(n)))
            code, charge = plan.pop(0)
            octets = json.dumps(charge).encode()
            self.send_response(code)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(octets)))
            self.end_headers()
            self.wfile.write(octets)

        def log_message(self, *a):
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    yield f"http://127.0.0.1:{srv.server_address[1]}", plan, corps
    srv.shutdown()


def test_paquet_officiel_serveur_factice(serveur, monkeypatch):
    pytest.importorskip("anthropic")
    url, plan, corps = serveur
    monkeypatch.setenv("VARIABLE_SONDE_ESSAI", "cle-factice-de-la-sonde-0123456789")
    appeler, version = s.fabriquer_appelant_reel("VARIABLE_SONDE_ESSAI", Secrets(), base_url=url)
    assert version
    plan.append((200, message("claude-opus-5-5", BON)))
    e = appeler("opus", "consigne")
    assert e.sorte == "ok" and e.jetons_entree == 1200 and e.jetons_sortie == 700
    plan.append((200, message("claude-fable-5-1", "", fin="refusal",
                              details={"type": "refusal", "category": "cyber", "explanation": "x"})))
    e = appeler("fable", "consigne")
    assert e.sorte == "refus" and e.categorie == "cyber"
    plan.append((200, message("claude-opus-5-5", "STEP 0: NO", fin="max_tokens")))
    assert appeler("opus", "consigne").sorte == "tronquee"
    plan.append((200, message("claude-opus-4-8", BON)))
    assert appeler("opus", "consigne").sorte == "modele_autre"
    plan.extend([(500, {"type": "error", "error": {"type": "api_error", "message": "x"}}),
                 (200, message("claude-opus-5-5", BON))])
    assert appeler("opus", "consigne").sorte == "ok"  # reprise par le paquet
    plan.append((401, {"type": "error", "error": {"type": "authentication_error", "message": "x"}}))
    assert appeler("opus", "consigne").sorte == "cle_refusee"
    plan.append((400, {"type": "error", "error": {"type": "invalid_request_error", "message": "x"}}))
    assert appeler("fable", "consigne").sorte == "rejet_http"
    # Corps envoyé : effort high, 16 000 jetons, ni température, ni réflexion, ni repli, ni système.
    for c in corps:
        assert c["max_tokens"] == 16000 and c["output_config"] == {"effort": "high"}
        assert not {"temperature", "thinking", "fallbacks", "system", "top_p", "top_k"} & set(c)
        assert c["messages"] == [{"role": "user", "content": "consigne"}]
    assert {c["model"] for c in corps} == {"claude-opus-5-5", "claude-fable-5-1"}


# ---------------------------------------------------------------------------------------------------------------
# Données réelles : comptes et empreintes seulement
# ---------------------------------------------------------------------------------------------------------------
@reelles
def test_reel_regeneration_phase1_fidele_et_tirage(tmp_path, capsys):
    assert s.principal(["tirer", "--actions", str(ACTIONS), "--taches", str(TACHES), "--entropie", "20261109",
                        "--sortie", str(tmp_path / "t")]) == 0
    rendu = json.loads(capsys.readouterr().out)
    r = rendu["rapport_tirage"]
    assert r["items"] == 30 and r["taches_distinctes"] == 30 and set(r["comptes_par_strate"].values()) == {2}
    m = json.loads((tmp_path / "t" / s.NOMS["tirage"]).read_text(encoding="utf-8"))
    assert m["empreinte_items_phase1_regeneres"] == s.EMPREINTE_ITEMS_PHASE1
    assert m["comptes_generation_neuve"]["items"] == 396


@reelles
def test_reel_artefact_entropie_phase1(tmp_path):
    with pytest.raises(s.ArretSonde, match="entropie"):
        s.principal(["tirer", "--actions", str(ACTIONS), "--taches", str(TACHES), "--entropie",
                     str(s.ENTROPIE_PHASE1), "--sortie", str(tmp_path / "t")])
