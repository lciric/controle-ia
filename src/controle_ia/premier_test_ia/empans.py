"""Empans de jetons des données génériques de P3, dans le gabarit de dialogue de l'agent (format du harnais).

Règle du harnais : les identifiants viennent des pièces du format (`FormatChat`) et du texte tokenisé seul, jamais d'une
retokenisation d'un rendu ; une garde exige qu'ils coïncident avec le rendu complet du gabarit (`fmt.rendre`), sinon
arrêt. Le gabarit de Llama 3.1 rogne les contenus (`trim`) : les textes sont rognés avant de tokeniser.
- `jetons_reponse_forcee` (tromperie, recette de 2502.03407) : consigne système, message utilisateur, puis le fait placé
  en réponse de l'assistant ; empan : les jetons du fait sans ses `retrait_fin` derniers (5 dans la recette) ;
- `jetons_message_utilisateur` (enjeux élevés) : consigne système, puis le texte en message utilisateur ; empan : au plus
  ses `max_jetons` premiers jetons ; les identifiants s'arrêtent au dernier jeton de l'empan (causalité : les
  activations d'une position ne lisent que les positions précédentes).
"""
from __future__ import annotations

from ..gardes import GardeArret
from ..harnais.formats import SENTINELLE, FormatChat, _ids


def _exiger_chat(fmt) -> None:
    if getattr(fmt, "nom", None) != "chat":
        raise GardeArret("empans génériques : format de dialogue (FormatChat) exigé")


def jetons_reponse_forcee(fmt, consigne: str, utilisateur: str, reponse: str, retrait_fin: int = 5) -> dict:
    """Identifiants de la conversation (consigne, utilisateur, réponse imposée) et empan de la réponse sans ses
    `retrait_fin` derniers jetons. Garde : identifiants = rendu complet du gabarit."""
    _exiger_chat(fmt)
    reponse = reponse.strip()
    if not reponse:
        raise GardeArret("réponse imposée vide")
    pre = fmt.ouverture(consigne, utilisateur)
    c = _ids(fmt.tok, reponse)
    if len(c) <= retrait_fin:
        raise GardeArret(f"réponse de {len(c)} jetons : plus de {retrait_fin} exigés (empan vide sinon)")
    ids = pre + c + fmt.cloture((consigne, utilisateur), c)
    reference = fmt.rendre(FormatChat._debut(consigne, utilisateur) + [{"role": "assistant", "content": reponse}], False)
    if ids != reference:
        raise GardeArret("réponse imposée : identifiants ≠ rendu complet du gabarit")
    return {"ids": ids, "debut": len(pre), "fin": len(pre) + len(c) - retrait_fin, "jetons_reponse": len(c)}


def jetons_message_utilisateur(fmt, consigne: str, texte: str, max_jetons: int = 128) -> dict:
    """Identifiants jusqu'au dernier jeton de l'empan du texte utilisateur (au plus `max_jetons` jetons). Garde : la
    conversation complète (pièces autour du texte tokenisé seul) = rendu complet du gabarit."""
    _exiger_chat(fmt)
    texte = texte.strip()
    if not texte:
        raise GardeArret("texte utilisateur vide")
    if max_jetons < 1:
        raise GardeArret("max_jetons < 1")
    avec_sentinelle = fmt.rendre(FormatChat._debut(consigne, SENTINELLE), True)
    s = _ids(fmt.tok, SENTINELLE)
    k = next((j for j in range(len(avec_sentinelle) - len(s) + 1) if avec_sentinelle[j:j + len(s)] == s), None)
    if k is None or any(avec_sentinelle[j:j + len(s)] == s for j in range(k + 1, len(avec_sentinelle) - len(s) + 1)):
        raise GardeArret("gabarit : sentinelle introuvable ou répétée dans le rendu")
    avant, apres = avec_sentinelle[:k], avec_sentinelle[k + len(s):]
    c = _ids(fmt.tok, texte)
    reference = fmt.rendre(FormatChat._debut(consigne, texte), True)
    if avant + c + apres != reference:
        raise GardeArret("message utilisateur : identifiants ≠ rendu complet du gabarit")
    n = min(len(c), int(max_jetons))
    return {"ids": avant + c[:n], "debut": len(avant), "fin": len(avant) + n, "jetons_texte": len(c)}
