"""Préchargement des modèles et chargement hors ligne (pilote de T0.5, SI-02) : cas sains et artefacts (R5), sans
réseau ni modèle réel (point de contrôle jouet écrit au format du cache de huggingface_hub)."""
from __future__ import annotations

import shutil
import socket

import pytest
import torch

import controle_ia.harnais.modeles as M
from controle_ia.gardes import GardeArret
from controle_ia.harnais.modeles import modele_jouet, tokeniseur_caracteres_chat

REV = "0cb88a4f764b7a12671c53f0838cd831a0843b95"
NOM = "meta-llama/Llama-3.2-3B-Instruct"


def _cache_jouet(racine, rev=REV, nom=NOM):
    """Cache au format de huggingface_hub : models--<org>--<nom>/snapshots/<révision>/, point de contrôle jouet en
    bfloat16 (configuration, poids en safetensors, tokeniseur)."""
    snap = racine / ("models--" + nom.replace("/", "--")) / "snapshots" / rev
    snap.mkdir(parents=True)
    tok = tokeniseur_caracteres_chat()
    m = modele_jouet(5, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64).to(torch.bfloat16)
    m.save_pretrained(snap)
    tok.save_pretrained(snap)
    return snap


@pytest.fixture
def sans_reseau(monkeypatch):
    """Toute connexion réseau échoue : un chargement qui tenterait le réseau le montrerait. Seule exception, mise hors
    jeu ici : le registre des agents de huggingface_hub (en-tête « user-agent »), chargé une fois par processus, au
    mieux, et sans effet sur les fichiers (une panne le rend vide, rien ne s'arrête)."""
    from huggingface_hub.utils import _detect_agent
    monkeypatch.setattr(_detect_agent, "_registry", _detect_agent._EMPTY_REGISTRY)
    tentatives = []

    def refuser(self, *a, **k):
        tentatives.append(a)
        raise OSError("réseau interdit dans ce test")
    monkeypatch.setattr(socket.socket, "connect", refuser)
    monkeypatch.setattr(socket.socket, "connect_ex", refuser)
    return tentatives


def test_charger_modele_hors_ligne_depuis_le_cache(tmp_path, sans_reseau):
    """Cas sain : fichiers en cache à la révision figée, aucun accès au réseau ; poids identiques au point de contrôle."""
    snap = _cache_jouet(tmp_path)
    m, tok = M.charger_modele(NOM, REV, "bfloat16", "cpu", hors_ligne=True, cache_dir=str(tmp_path))
    from transformers import AutoModelForCausalLM
    direct = AutoModelForCausalLM.from_pretrained(str(snap), dtype=torch.bfloat16)
    a, b = m.state_dict(), direct.state_dict()
    assert a.keys() == b.keys() and all(torch.equal(a[k], b[k]) for k in a)
    assert len(tok) == len(tokeniseur_caracteres_chat()) and sans_reseau == []


def test_charger_modele_hors_ligne_sans_cache_arrete_sans_reseau(tmp_path, sans_reseau):
    """Artefacts : révision absente du cache, ou poids retirés : arrêt immédiat, aucune tentative de téléchargement."""
    _cache_jouet(tmp_path)
    with pytest.raises(OSError):
        M.charger_modele(NOM, "1" * 40, "bfloat16", "cpu", hors_ligne=True, cache_dir=str(tmp_path))
    for f in (tmp_path / ("models--" + NOM.replace("/", "--")) / "snapshots" / REV).glob("*.safetensors"):
        f.unlink()
    with pytest.raises(OSError):
        M.charger_modele(NOM, REV, "bfloat16", "cpu", hors_ligne=True, cache_dir=str(tmp_path))
    assert sans_reseau == []


def test_precharger_modele_cas_sain_et_artefacts(tmp_path, monkeypatch):
    """Cas sain : téléchargement à la révision figée, motifs sans les poids d'origine ; artefacts : modèle hors liste
    blanche, révision non figée, poids absents, dossier d'une autre révision."""
    import huggingface_hub
    appels = []
    source = _cache_jouet(tmp_path / "source")

    def telecharger(repo_id, revision, allow_patterns, cache_dir=None, **k):
        appels.append((repo_id, revision, tuple(allow_patterns)))
        d = tmp_path / "cache" / revision
        if not d.exists():
            shutil.copytree(source, d)
        return str(d)
    monkeypatch.setattr(huggingface_hub, "snapshot_download", telecharger)
    assert M.precharger_modele(NOM, REV).endswith(REV)
    assert appels[0][:2] == (NOM, REV) and "model*.safetensors" in appels[0][2]
    assert not any("original" in x or x == "*" for x in appels[0][2])
    with pytest.raises(GardeArret, match="hors liste blanche"):
        M.precharger_modele("org/inconnu", REV)
    with pytest.raises(GardeArret, match="révision figée"):
        M.precharger_modele(NOM, "main")
    for f in (tmp_path / "cache" / REV).glob("*.safetensors"):
        f.unlink()
    with pytest.raises(GardeArret, match="préchargement incomplet"):
        M.precharger_modele(NOM, REV)
    monkeypatch.setattr(huggingface_hub, "snapshot_download",
                        lambda repo_id, revision, allow_patterns, cache_dir=None, **k: str(source))
    shutil.move(str(source), str(tmp_path / "autre"))
    autre = tmp_path / "source2" / ("2" * 40)
    shutil.copytree(tmp_path / "autre", autre)
    monkeypatch.setattr(huggingface_hub, "snapshot_download",
                        lambda repo_id, revision, allow_patterns, cache_dir=None, **k: str(autre))
    with pytest.raises(GardeArret, match="pas dans la révision"):
        M.precharger_modele(NOM, REV)
