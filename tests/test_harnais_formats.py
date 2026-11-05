"""Formats de transcription du harnais (T0.4, préparation du modèle réel) : brut et gabarit de conversation.

Garde de format testée sur un cas sain (gabarit à balises de tour) et sur des artefacts : gabarit qui
déplace la consigne vers le dernier tour (réécriture du passé), gabarit sans clôture de tour,
tokeniseur sans gabarit.
"""
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatBrut, FormatChat, verifier_format
from controle_ia.harnais.modeles import tokeniseur_caracteres, tokeniseur_caracteres_chat

OBS = ["Pas 0.", "Pas 1. Journal : 0@0: A", "Pas 2."]
REP = ["Je propose A.", "Puis B.", "Enfin C."]

# artefact : à la manière de certains gabarits, la consigne rejoint le DERNIER message de l'utilisateur
GABARIT_DEPLACE = ("{% set sys = messages[0]['content'] %}{% for m in messages[1:] %}"
                   "{% if m['role'] == 'user' %}{% if loop.last %}[INST] {{ sys }}\n\n{{ m['content'] }}[/INST]"
                   "{% else %}[INST] {{ m['content'] }}[/INST]{% endif %}"
                   "{% else %}{{ m['content'] }}{% endif %}{% endfor %}")
# artefact : rien ne ferme le tour de l'assistant
GABARIT_SANS_CLOTURE = ("{% for m in messages %}<|im_start|>{{ m['role'] }}\n{{ m['content'] }}"
                        "{% if m['role'] != 'assistant' %}<|im_end|>\n{% endif %}{% endfor %}"
                        "{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}")


def _chat():
    tok = tokeniseur_caracteres_chat()
    return tok, FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})


def test_format_brut_reproduit_le_harnais_initial():
    tok = tokeniseur_caracteres()
    f = FormatBrut(tok)
    ids = lambda s: tok(s, add_special_tokens=False)["input_ids"]
    assert f.ouverture("C.", "O.") == [tok.bos_token_id] + ids("C.") + ids("O.")
    assert f.tour(("C.", "O."), "P.") == ids("P.") and f.cloture(("C.", "O."), [5, 2]) == []
    assert verifier_format(f, "C.", ["O."], ["R."])["verifie"] is False


def test_format_chat_sain():
    tok, f = _chat()
    r = verifier_format(f, "Tu es l'agent 0.", OBS, REP)
    assert r == {"format": "chat", "verifie": True, "jetons": r["jetons"], "tours": 3}
    fin = tok.convert_tokens_to_ids("<|im_end|>")
    debut = ("Tu es l'agent 0.", OBS[0])
    assert f.cloture(debut, [40, fin]) == tok("\n", add_special_tokens=False)["input_ids"]
    assert f.cloture(debut, [40, 41]) == [fin] + tok("\n", add_special_tokens=False)["input_ids"]
    assert tok.decode(f.tour(debut, "Pas 1.")) == "<|im_start|>user\nPas 1.<|im_end|>\n<|im_start|>assistant\n"
    assert tok.decode(f.ouverture(*debut)).endswith("<|im_start|>assistant\n")


def test_format_chat_artefacts():
    tok, _ = _chat()
    tok.chat_template = GABARIT_DEPLACE
    with pytest.raises(GardeArret, match="ne prolonge pas"):
        verifier_format(FormatChat(tok), "Tu es l'agent 0.", OBS, REP)
    tok.chat_template = GABARIT_SANS_CLOTURE
    with pytest.raises(GardeArret, match="ferme le tour"):
        verifier_format(FormatChat(tok), "Tu es l'agent 0.", OBS, REP)
    with pytest.raises(GardeArret, match="sans gabarit"):
        FormatChat(tokeniseur_caracteres())
    _, f = _chat()
    with pytest.raises(GardeArret, match="autant d'observations"):
        verifier_format(f, "C.", OBS, REP[:2])
