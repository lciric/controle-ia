"""Lecteur du coût déclaré neuf (P-015, « Lecteur du coût » ; T0.6, métrique), sous nom neuf : le module de lecture de P3
(`environnements.propositions.heures_declarees`) reste tel quel (R12).

Défauts corrigés par rapport au lecteur de P3 :
- les milliers séparés par une espace (« 1 000 », « 10 000 GPU-hours », espace insécable comprise) sont lus comme un seul
  nombre (le lecteur de P3 lisait 1) ;
- un nombre collé à des lettres (« 120h ») n'est plus lu par repli sur un préfixe (« 12 ») : le nombre entier est lu.
Conservé de P3 : le premier nombre du champ fait foi ; « 1,000 » est un millier (convention anglaise de l'agent), « 1,5 »
une virgule décimale ; suffixe « k » = ×1 000. Les formes douteuses (plusieurs nombres, multiplication, intervalle,
suffixe « k », milliers à l'espace) sont consignées à côté, jamais corrigées en silence. Un coût lisible est un nombre fini
strictement positif ; 0 et l'absence sont consignés comme illisibles (le log10 l'exige).
"""
from __future__ import annotations

import math
import re

from ..environnements.propositions import lire_action

ESPACES = "[   ]"
_MILLIERS_ESPACE = rf"\d{{1,3}}(?:{ESPACES}\d{{3}})+(?:[.,]\d+)?"
_MILLIERS_VIRGULE = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?"
_SIMPLE = r"\d+(?:[.,]\d+)?"
NOMBRE = re.compile(rf"(?<![\d.,])(?P<n>{_MILLIERS_ESPACE}|{_MILLIERS_VIRGULE}|{_SIMPLE})(?!\d)"
                    rf"(?:{ESPACES}*(?P<k>[kK])(?![A-Za-z]))?")
_MULTIPLICATION = re.compile(r"\d\s*[×xX*]\s*\d")
_INTERVALLE = re.compile(r"\d\s*(?:–|—|-|to)\s*\d")
_SUFFIXE_K = re.compile(r"\d\s*[kK](?![A-Za-z])")
_MILLIERS_ESPACE_SEUL = re.compile(rf"(?<![\d.,])\d{{1,3}}(?:{ESPACES}\d{{3}})+(?![\d,])")


def valeur_du_nombre(n: str, k: str | None) -> float:
    n = re.sub(ESPACES, "", n)
    if re.fullmatch(_MILLIERS_VIRGULE, n):
        v = float(n.replace(",", ""))
    else:
        v = float(n.replace(",", "."))
    return v * 1000.0 if k else v


def lire_cout(champ: str | None) -> dict:
    """Lecture du champ COST : `cout` (premier nombre, None si aucun), et les formes consignées."""
    champ = champ or ""
    nombres = list(NOMBRE.finditer(champ))
    cout = valeur_du_nombre(nombres[0]["n"], nombres[0]["k"]) if nombres else None
    return {"cout": cout, "cout_present": bool(champ.strip()), "cout_plusieurs_nombres": len(nombres) > 1,
            "cout_multiplication": bool(_MULTIPLICATION.search(champ)), "cout_intervalle": bool(_INTERVALLE.search(champ)),
            "cout_suffixe_k": bool(_SUFFIXE_K.search(champ)), "cout_milliers_espace": bool(_MILLIERS_ESPACE_SEUL.search(champ))}


def cout_action(texte: str) -> dict:
    """Coût déclaré de l'action (champ COST lu par `lire_action`, gelé), par le lecteur neuf ; `valide` : action lisible."""
    a = lire_action(texte)
    return {"valide": bool(a.valide), **lire_cout(a.champs.get("COST"))}


def cout_lisible(c) -> bool:
    return isinstance(c, (int, float)) and not isinstance(c, bool) and math.isfinite(c) and c > 0
