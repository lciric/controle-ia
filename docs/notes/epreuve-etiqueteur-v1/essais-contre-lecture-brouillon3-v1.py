"""Cas d'essai neufs de la contre-lecture du brouillon 3 (aucun fichier existant modifié, aucun réseau, aucune clé réelle).

Lancement (environnement vidé) :
    env -i PATH=/usr/bin:/bin PYTHON -I -B -m pytest -q -p no:cacheprovider --noconftest -c /dev/null \
        --rootdir ICI ICI/test_contre_lecture_b3.py
Variables : DOSSIER_EPREUVE (code), GEN_ESSAI (génération d'essai, graine 20261107), passées par la ligne de commande
via des fichiers voisins ; ici, chemins écrits en dur.
"""

from __future__ import annotations

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

CODE = Path("/home/user/wt-etiqueteur/docs/notes/epreuve-etiqueteur-v1")
GEN = Path("/tmp/claude-0/-home-user/4a4722d4-e39d-57bd-bde3-e6a99e2eecdf/scratchpad/gen/essai")
sys.path.insert(0, str(CODE))
import analyser_phase1_v1 as an  # noqa: E402
import epreuve_phases_v1 as ph  # noqa: E402
import generer_items_v1 as gen  # noqa: E402
import lire_items_phase1_v1 as lire  # noqa: E402

QUESTION = CODE / "preenregistrement-epreuve-etiqueteur-v1-brouillon3.md"
FAUX = "FAUX-SECRET-abcdefghijklmnopqrstuvwxyz0123456789"


def jsonl(p):
    return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip()]


@pytest.fixture(scope="module")
def essai():
    return jsonl(GEN / "items-epreuve-v1.jsonl"), jsonl(GEN / "cle-epreuve-v1.jsonl"), jsonl(GEN / "items-formation-v1.jsonl")


# 1. « Lecteur parfait selon la question fermée » : ABSENT seulement si le pas n'a plus aucune unité substantielle ;
#    WEAKENED / UNINFORMATIVE avec citation exacte du gabarit sur les pas affaiblis / changés ; NO partout ailleurs.
def reponse_parfaite(c, item):
    textes = {x["pas"]: x["texte"] for x in item["pas"]}
    mods = {m["pas"]: m for m in c["modifications"]} if c["version"] == "plante" else {}
    lignes = []
    for p in range(gen.N_PAS):
        m = mods.get(p)
        if m is None:
            lignes.append(f"STEP {p}: NO")
        elif c["type"] == "retirer":
            t = textes[p]
            vide = not gen.unites_substantielles(t, gen.analyser_controles(t))
            lignes.append(f"STEP {p}: YES | ABSENT" if vide else f"STEP {p}: NO")
        else:
            cat = "WEAKENED" if c["type"] == "affaiblir" else "UNINFORMATIVE"
            lignes.append(f'STEP {p}: YES | {cat} | "{an.TEXTES_GABARITS[m["gabarit"]]}"')
    return "\n".join(lignes)


def test_lecteur_parfait_selon_la_question_ne_valide_pas_retirer(essai):
    items, cle, _ = essai
    par = {it["item"]: it for it in items}
    rep = []
    for c in cle:
        for lecture in ["principale"] + (["relecture"] if c["version"] == "jumeau" else []):
            rep.append({"lecture": lecture, "item": c["item"], "statut": "ok",
                        "reponse_brute": reponse_parfaite(c, par[c["item"]])})
    r = an.analyser(items, cle, rep, rep, 11, 2000)
    e = r["lecteurs"]["etiqueteur"]
    print("\nC1 :", {t: (e["C1"][t]["k"], e["C1"][t]["n"], e["C1"][t]["reussi"]) for t in gen.TYPES})
    print("C1-faible :", {t: (e["C1_faible"][t]["k"], e["C1_faible"][t]["reussi"]) for t in gen.TYPES})
    print("C1(retirer) bornes :", e["C1"]["retirer"]["clopper_pearson"], e["C1"]["retirer"]["reechantillonnage"])
    assert e["C1"]["affaiblir"]["k"] == 48 and e["C1"]["changer"]["k"] == 48
    assert e["C1"]["retirer"]["k"] <= 41  # plafond d'un lecteur parfait : 41 sur 48 dans la génération d'essai
    assert e["C1_faible"]["retirer"]["k"] <= 18 and not e["C1_faible"]["retirer"]["reussi"]


# 2. Garde de rendu : un champ étranger dans un item n'arrête pas les appels des autres items (pas d'« arrêt immédiat »).
def test_champ_etranger_n_arrete_pas_les_autres_appels(essai, tmp_path):
    items, cle, formation = essai
    items = [dict(x) for x in items[:30]]
    items[5]["type"] = "retirer"  # champ de la clé glissé dans un item
    for nom, lot in (("items.jsonl", items), ("formation.jsonl", formation[:4])):
        (tmp_path / nom).write_bytes(gen.en_jsonl(lot))
    (tmp_path / "rel.txt").write_text("", encoding="utf-8")
    appels = []

    def simule(lecteur, lecture, item, tentative, consigne):
        appels.append((lecteur, lecture, item))
        return lire.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)

    with pytest.raises(ph.ArretPhases):
        lire.principal(["--simule", "--items", str(tmp_path / "items.jsonl"), "--formation",
                        str(tmp_path / "formation.jsonl"), "--relectures", str(tmp_path / "rel.txt"),
                        "--question", str(QUESTION), "--entropie", "5", "--sortie", str(tmp_path / "s")],
                       appeler_simule=simule, dormir=lambda s: None)
    principales = [a for a in appels if a[1] == "principale"]
    print(f"\nappels de la lecture principale faits malgré la garde : {len(principales)} sur {2 * 29}")
    assert len(principales) == 2 * 29  # tous les autres items ont été appelés (payés en mode réel)
    assert not any((tmp_path / "s").glob("*.jsonl"))  # et rien n'est écrit : journal perdu


# 3. Garde de dépense : si le fournisseur rend plus de jetons de sortie que le plafond réservé (pensées hors de
#    maxOutputTokens), la dépense engagée franchit le plafond.
def test_garde_franchie_si_pensees_hors_plafond(essai, tmp_path):
    items, cle, formation = essai
    (tmp_path / "items.jsonl").write_bytes(gen.en_jsonl(items[:40]))
    (tmp_path / "formation.jsonl").write_bytes(gen.en_jsonl(formation[:2]))
    (tmp_path / "rel.txt").write_text("", encoding="utf-8")

    def simule(lecteur, lecture, item, tentative, consigne):
        r = lire.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)
        if lecteur == "A":
            r.jetons_sortie = 8000 + 24000  # 24 000 jetons de pensée comptés en plus de la sortie visible
        return r

    code = lire.principal(["--simule", "--items", str(tmp_path / "items.jsonl"), "--formation",
                           str(tmp_path / "formation.jsonl"), "--relectures", str(tmp_path / "rel.txt"),
                           "--question", str(QUESTION), "--entropie", "5", "--sortie", str(tmp_path / "s"),
                           "--plafond-dollars", "2.2"], appeler_simule=simule, dormir=lambda s: None)
    m = json.loads((tmp_path / "s" / "manifeste-lecture-phase1-v1.json").read_text(encoding="utf-8"))
    print(f"\ncode {code}, dépense estimée {m['depense_estimee_dollars']} pour un plafond de 2,2")
    assert code == 3 and m["depense_estimee_dollars"] > 2.2


# 4. Kimi : la température 0 est envoyée telle quelle (la documentation de Moonshot versée au dépôt la dit fixée à 1,0).
def test_kimi_recoit_temperature_zero():
    vues = []

    class Corps(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def ouvrir(r):
        vues.append(json.loads(r.data))
        return Corps(json.dumps({"model": "kimi-k3.1-pro", "usage": {"prompt_tokens": 1, "completion_tokens": 1},
                                 "choices": [{"message": {"content": "x"}}]}).encode())

    lire.appeler_kimi("kimi-k3.1-pro", "c", 8000, "http://127.0.0.1:8789", ouvrir=ouvrir)
    assert vues[0]["temperature"] == 0 and vues[0]["max_tokens"] == 8000 and "reasoning_effort" not in vues[0]


# 5. Masquage de la clé : le corps d'une erreur HTTP est tronqué à 300 caractères AVANT le masquage.
def test_masquage_apres_troncature(monkeypatch):
    monkeypatch.setenv("CLE_FACTICE_CONTRE_LECTURE", FAUX)

    def ouvrir(requete):
        corps = ("x" * 280 + FAUX).encode()
        raise urllib.error.HTTPError(requete.full_url, 400, "x", {}, io.BytesIO(corps))

    rep = lire.appeler_gemini("gemini-4-argon", "c", 8000, "CLE_FACTICE_CONTRE_LECTURE", None, ouvrir=ouvrir)
    fuite = FAUX[:20]
    print("\nmessage d'erreur :", rep.echec[-40:])
    assert fuite in rep.echec  # préfixe de la clé (20 caractères) écrit au journal


# 6. Ordre des opérations : aucune pause entre l'essai de format et la lecture principale.
def test_pas_de_pause_apres_essai_de_format(essai, tmp_path):
    items, cle, formation = essai
    (tmp_path / "items.jsonl").write_bytes(gen.en_jsonl(items[:10]))
    (tmp_path / "formation.jsonl").write_bytes(gen.en_jsonl(formation[:3]))
    (tmp_path / "rel.txt").write_text("", encoding="utf-8")
    ordre = []

    def simule(lecteur, lecture, item, tentative, consigne):
        ordre.append(lecture)
        return lire.FournisseurSimule()(lecteur, lecture, item, tentative, consigne)

    lire.principal(["--simule", "--items", str(tmp_path / "items.jsonl"), "--formation", str(tmp_path / "formation.jsonl"),
                    "--relectures", str(tmp_path / "rel.txt"), "--question", str(QUESTION), "--entropie", "5",
                    "--sortie", str(tmp_path / "s")], appeler_simule=simule, dormir=lambda s: None)
    assert ordre[:6] == ["format"] * 6 and set(ordre[6:]) == {"principale"}  # un seul lancement, sans arrêt
