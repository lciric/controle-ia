"""Mise en forme des transcriptions : texte brut (modèle jouet) ou gabarit de conversation (modèles instruits).

Règle du harnais : la transcription d'un agent est une suite d'identifiants de jetons, jamais
retokenisée. Un format fournit seulement les pièces à coller autour des actions générées :
- `ouverture(consigne, observation)` : début de la conversation jusqu'à l'invite de réponse ;
- `cloture(debut, action)` : ce qui ferme le tour de l'agent après l'action générée ;
- `tour(debut, observation)` : nouveau tour d'observation, jusqu'à l'invite de réponse.

`FormatChat` dérive ces pièces du gabarit du tokeniseur en rendant des conversations à contenu
sentinelle, sans jamais retokeniser une action générée. `verifier_format` (garde d'arrêt) exige que
la transcription incrémentale coïncide avec le rendu complet du gabarit sur une conversation de
contrôle ; un gabarit qui réécrit le passé (consigne déplacée vers le dernier tour, par exemple)
l'arrête.
"""
from __future__ import annotations

from ..gardes import GardeArret

SENTINELLE = "§"


def _ids(tok, texte: str) -> list[int]:
    return list(tok(texte, add_special_tokens=False)["input_ids"])


class FormatBrut:
    """Texte brut : [début de séquence] + consigne + observation, puis observations ; aucune clôture."""

    nom = "brut"

    def __init__(self, tok):
        self.tok = tok
        self.fins = {tok.eos_token_id}

    def ouverture(self, consigne: str, observation: str) -> list[int]:
        return [self.tok.bos_token_id] + _ids(self.tok, consigne) + _ids(self.tok, observation)

    def cloture(self, debut: tuple[str, str], action: list[int]) -> list[int]:
        return []

    def tour(self, debut: tuple[str, str], observation: str) -> list[int]:
        return _ids(self.tok, observation)


class FormatChat:
    """Gabarit de conversation du tokeniseur : consigne en message système, observations en messages
    utilisateur, actions en messages de l'assistant."""

    nom = "chat"

    def __init__(self, tok, fins: set[int] | None = None, variables: dict | None = None):
        """`variables` : valeurs figées passées au gabarit (une date d'en-tête, par exemple), pour qu'aucune
        transcription ne dépende du jour du lancement."""
        if not getattr(tok, "chat_template", None):
            raise GardeArret("tokeniseur sans gabarit de conversation : FormatChat impossible")
        self.tok = tok
        self.fins = set(fins) if fins else {tok.eos_token_id}
        self.variables = dict(variables or {})
        self._cache: dict[tuple[str, str], dict] = {}

    def rendre(self, messages: list[dict], invite: bool) -> list[int]:
        r = self.tok.apply_chat_template(messages, add_generation_prompt=invite, tokenize=True, return_dict=False,
                                         **self.variables)
        return [int(x) for x in r]

    @staticmethod
    def _debut(consigne: str, observation: str) -> list[dict]:
        return [{"role": "system", "content": consigne}, {"role": "user", "content": observation}]

    def _pieces(self, debut: tuple[str, str]) -> dict:
        if debut in self._cache:
            return self._cache[debut]
        consigne, observation = debut
        ouverture = self.rendre(self._debut(consigne, observation), True)
        avec_sentinelle = self.rendre(self._debut(consigne, observation)
                                      + [{"role": "assistant", "content": SENTINELLE}], False)
        sentinelle = _ids(self.tok, SENTINELLE)
        n = len(ouverture)
        if avec_sentinelle[:n] != ouverture or avec_sentinelle[n:n + len(sentinelle)] != sentinelle:
            raise GardeArret("gabarit : la réponse de l'assistant ne prolonge pas l'invite à l'identique")
        cloture = avec_sentinelle[n + len(sentinelle):]
        if not cloture:
            raise GardeArret("gabarit : aucun jeton ne ferme le tour de l'assistant")
        pieces = {"ouverture": ouverture, "cloture": cloture, "avec_sentinelle": avec_sentinelle}
        self._cache[debut] = pieces
        return pieces

    def ouverture(self, consigne: str, observation: str) -> list[int]:
        return list(self._pieces((consigne, observation))["ouverture"])

    def cloture(self, debut: tuple[str, str], action: list[int]) -> list[int]:
        c = self._pieces(debut)["cloture"]
        return list(c[1:]) if action and action[-1] == c[0] else list(c)

    def tour(self, debut: tuple[str, str], observation: str) -> list[int]:
        p = self._pieces(debut)
        consigne, premiere = debut
        r = self.rendre(self._debut(consigne, premiere) + [{"role": "assistant", "content": SENTINELLE},
                                                           {"role": "user", "content": observation}], True)
        prefixe = p["avec_sentinelle"]
        if r[:len(prefixe)] != prefixe:
            raise GardeArret("gabarit : un nouveau tour réécrit le début de la conversation")
        return r[len(prefixe):]


def verifier_format(fmt, consigne: str, observations: list[str], reponses: list[str]) -> dict:
    """Garde : transcription incrémentale (pièces + réponses tokenisées seules) = rendu complet du gabarit.

    Les réponses de contrôle simulent des actions closes par le premier jeton de clôture, comme une
    génération arrêtée par son jeton de fin de tour. Sans objet pour le format brut."""
    if fmt.nom != "chat":
        return {"format": fmt.nom, "verifie": False, "motif": "sans gabarit"}
    if len(observations) != len(reponses) or not reponses:
        raise GardeArret("vérification du format : autant d'observations que de réponses, au moins une")
    debut = (consigne, observations[0])
    ids = fmt.ouverture(consigne, observations[0])
    messages = FormatChat._debut(consigne, observations[0])
    fin_de_tour = fmt._pieces(debut)["cloture"][0]
    for k, rep in enumerate(reponses):
        if k > 0:
            ids += fmt.tour(debut, observations[k])
            messages.append({"role": "user", "content": observations[k]})
        action = _ids(fmt.tok, rep) + [fin_de_tour]
        ids += action + fmt.cloture(debut, action)
        messages.append({"role": "assistant", "content": rep})
    reference = fmt.rendre(messages, False)
    if ids != reference:
        k = next((j for j, (a, b) in enumerate(zip(ids, reference)) if a != b), min(len(ids), len(reference)))
        raise GardeArret(f"format incrémental ≠ gabarit complet (premier écart au jeton {k} ; "
                         f"{len(ids)} contre {len(reference)} jetons)")
    return {"format": fmt.nom, "verifie": True, "jetons": len(ids), "tours": len(reponses)}
