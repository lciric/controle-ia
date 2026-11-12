"""Essai R5 de R-2109 (contre-lecture du script des jeux, `docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/contre-lecture-script-jeux-v1.md`,
`d0e8f3ef…`) : dans les jeux scellés J-D et J-A, l'ordre des lignes porte l'étiquette (`assembler` écrit toujours le membre
d'étiquette 0 avant l'autre). Le module de T0.7 lit l'étiquette dans son champ, jamais au rang de ligne, et `lire_jeu` rend les
enregistrements dans un ordre canonique (tâche, paire, membre) : l'apprentissage et la validation des sondes neuves, les plis, les
tirages, les témoins lexicaux et T7-P6 ne dépendent pas de l'ordre du fichier.

- Cas sain : un jeu dont les lignes sont mélangées donne, au bit près, les mêmes résultats que le jeu dans l'ordre d'`assembler`.
- Artefact : un lecteur qui prendrait l'étiquette au rang de ligne est pris (résultats différents dès que l'ordre change)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.manifeste import graines as deriver_graines
from controle_ia.t07 import sondes_neuves_v1 as sn
from test_t07_sondes_neuves_v1 import ExtracteurFactice, construire_complet, enregistrements, phrases_concepts

JEUX = (("JD", sn.JEU_JD), ("JC", sn.JEU_JC), ("JA", sn.JEU_JA))


def comme_assembler(jeu: str) -> list[dict]:
    """Jeu jouet : membre A ou B tiré par paire (graine fixe), et, comme `assembler`, le membre d'étiquette 0 toujours écrit en
    premier : l'ordre des lignes porte l'étiquette, la lettre du membre non."""
    rng = np.random.default_rng(20261110)
    sortie = []
    recs = enregistrements(jeu)
    for k in range(0, len(recs), 2):
        a, b = dict(recs[k]), dict(recs[k + 1])          # a : étiquette 0, b : étiquette 1
        if rng.integers(2):
            a["membre"], b["membre"] = "B", "A"
        sortie += [a, b]
    assert [r["etiquette"] for r in sortie] == [0, 1] * (len(sortie) // 2)
    return sortie


def ecrire(dossier: Path, recs_par_jeu: dict, melanger: bool) -> dict:
    dossier.mkdir(parents=True, exist_ok=True)
    chemins = {}
    for cle, recs in recs_par_jeu.items():
        lignes = [json.dumps(r, ensure_ascii=False) for r in recs]
        if melanger:
            ordre = np.random.default_rng(7).permutation(len(lignes))
            lignes = [lignes[i] for i in ordre]
        chemins[cle] = dossier / f"{cle}.jsonl"
        chemins[cle].write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return chemins


def lire_au_rang(chemin: Path, jeu: str) -> list[dict]:
    """Artefact : lecteur fautif qui prend l'étiquette au rang de ligne (0, 1, 0, 1… dans l'ordre du fichier)."""
    recs = [json.loads(l) for l in Path(chemin).read_text(encoding="utf-8").splitlines() if l.strip()]
    return [{**r, "etiquette": k % 2} for k, r in enumerate(recs)]


def resultats(chemins: dict, config: dict, lire=sn.lire_jeu) -> str:
    jeux = {cle: lire(chemins[cle], jeu) for cle, jeu in JEUX}
    phrases = sn.lire_phrases_concepts(chemins["concepts"])
    graines = deriver_graines(["decoupage"], 7)
    a = sn.apprendre(jeux, phrases, ExtracteurFactice(), config, graines, ["dissimulation", "domaine"])
    empreintes = {c: [s.empreinte() for s in x["couples"]] for c, x in a["sondes"].items()}
    planchers = {n: [p.empreinte() for p in liste] for n, liste in a["planchers"].items()}
    p6 = {n: x["sonde"].empreinte() for n, x in a["p6"]["_sondes"].items()} if a["p6"] else None
    lexicaux = {c: x["empreinte"] for c, x in a["lexicaux"].items()}
    directions = [d["sonde"].empreinte() for d in a["directions"]["directions"]]
    return json.dumps({"sondes": empreintes, "planchers": planchers, "p6": p6, "lexicaux": lexicaux, "directions": directions,
                       "rapport": sans_durees(a["rapport"])}, sort_keys=True, default=str)


def sans_durees(x):
    """Le rapport sans les durées mesurées (`duree_s`, horloge) : tout le reste est comparé au bit près."""
    if isinstance(x, dict):
        return {k: sans_durees(v) for k, v in x.items() if k != "duree_s"}
    if isinstance(x, list):
        return [sans_durees(v) for v in x]
    return x


@pytest.fixture
def config(depot):
    return construire_complet(depot).config


def test_ordre_des_lignes_sans_effet_au_bit_pres(tmp_path, config):
    """Cas sain : lignes mélangées → `lire_jeu` rend les mêmes enregistrements dans le même ordre, et l'apprentissage complet
    (30 couples, principales, planchers, T7-P6, directions, témoins lexicaux, rapport et aires de validation) est égal au bit près ;
    l'étiquette lue est celle du champ (la lettre du membre, tirée, place l'étiquette 1 en tête dans une partie des paires)."""
    recs = {cle: comme_assembler(jeu) for cle, jeu in JEUX}
    ordre = ecrire(tmp_path / "ordre", recs, melanger=False)
    melange = ecrire(tmp_path / "melange", recs, melanger=True)
    for d in (ordre, melange):
        d["concepts"] = d["JD"].parent / "concepts.jsonl"
        d["concepts"].write_text(phrases_concepts(), encoding="utf-8")
    assert (tmp_path / "ordre" / "JD.jsonl").read_text() != (tmp_path / "melange" / "JD.jsonl").read_text()
    for cle, jeu in JEUX:
        a, b = sn.lire_jeu(ordre[cle], jeu), sn.lire_jeu(melange[cle], jeu)
        assert a == b and [(r["tache"], r["paire"], r["membre"]) for r in a] == sorted((r["tache"], r["paire"], r["membre"]) for r in a)
        assert any(r["etiquette"] == 1 for r in a[0::2]), "la lettre tirée doit mettre l'étiquette 1 en tête de quelques paires"
    assert resultats(ordre, config) == resultats(melange, config)


def test_lecteur_au_rang_pris(tmp_path, config):
    """Artefact : un lecteur qui lirait l'étiquette au rang de ligne donne, sur le fichier dans l'ordre d'`assembler`, les étiquettes
    du champ (l'ordre les porte), et d'autres dès que les lignes sont mélangées : ses résultats changent avec l'ordre, l'essai
    d'invariance le prend."""
    recs = {cle: comme_assembler(jeu) for cle, jeu in JEUX}
    ordre = ecrire(tmp_path / "ordre", recs, melanger=False)
    melange = ecrire(tmp_path / "melange", recs, melanger=True)
    for d in (ordre, melange):
        d["concepts"] = d["JD"].parent / "concepts.jsonl"
        d["concepts"].write_text(phrases_concepts(), encoding="utf-8")
    assert [r["etiquette"] for r in lire_au_rang(ordre["JD"], sn.JEU_JD)] == [r["etiquette"] for r in recs["JD"]]
    champ = [json.loads(l)["etiquette"] for l in melange["JD"].read_text(encoding="utf-8").splitlines() if l.strip()]
    assert [r["etiquette"] for r in lire_au_rang(melange["JD"], sn.JEU_JD)] != champ
    assert resultats(ordre, config, lire_au_rang) != resultats(melange, config, lire_au_rang)
