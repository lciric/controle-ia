"""Registre de dépense cumulée de la mini-course (Kimi et Argon seuls, GO-2026-11-01-12), version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot) ; rien n'a été lancé par le rédacteur. Partagé par les deux
commandes externes (`commande_kimi_v2.py`, `commande_argon_v56_nuit_v1.py`) et par les deux contrôles du lanceur : c'est la
**garde de plafond cumulée au pire cas avant chaque appel** (gabarit de l'épreuve du pont, `lancer_epreuve_pont_v2.py`,
classe `Budget`), tenue hors de l'orchestrateur, dans un fichier du dossier du run.

Règle, sous verrou exclusif (`fcntl.flock` sur `<registre>.verrou`), avant tout envoi :

    réglé + engagé + pire cas de l'appel <= plafond cumulé (10 USD)                       (garde 1)
    réglé de l'étape + engagé de l'étape + pire cas <= plafond dur de l'étape             (garde 2, si l'étape est connue)

- « réglé » = somme des coûts des lignes `fin` ; « engagé » = somme des pires cas des lignes `debut` **sans** ligne `fin`
  (un appel tué avant son règlement reste compté à son pire cas, pour toujours : côté prudent) ;
- le plafond dur de l'étape est celui que le noyau v56 transmet par la porte « environnement » (`PLAFOND_ETAPE_USD`,
  `ETAPE_POLE`) ; la garde 2 porte sur les deux fournisseurs ensemble (même registre), comme le noyau ;
- une ligne illisible, un identifiant en double, une `fin` sans `debut` : refus (`RegistreIllisible`), jamais un repli.

Format : une ligne JSON par événement, jamais de texte de consigne ni de réponse, jamais de clé :
    {"type": "debut", "id", "quand_utc", "fournisseur", "role", "modele", "etape", "pire_cas_usd"}
    {"type": "fin", "id", "quand_utc", "cout_usd", "statut", "code", "cout_origine", "depassement_reserve"}
Bibliothèque standard seulement.
"""

import datetime
import fcntl
import json
import math
import os
import uuid

VERSION = "registre-depense-cumulee-v1"
EPS = 1e-9


class RegistreIllisible(RuntimeError):
    pass


class PlafondCumule(RuntimeError):
    """La garde refuse l'appel : rien n'est envoyé."""


def _maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _reel(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) and v >= 0


def lire(chemin):
    """Rend la liste des événements ; lève `RegistreIllisible` sur toute ligne non conforme."""
    if not os.path.exists(chemin):
        return []
    evenements, debuts, fins = [], set(), set()
    with open(chemin, encoding="utf-8") as f:
        for n, ligne in enumerate(f, 1):
            if not ligne.strip():
                continue
            try:
                e = json.loads(ligne)
            except ValueError:
                raise RegistreIllisible(f"registre {chemin} : ligne {n} illisible") from None
            if not isinstance(e, dict) or e.get("type") not in ("debut", "fin") or not isinstance(e.get("id"), str):
                raise RegistreIllisible(f"registre {chemin} : ligne {n} non conforme")
            if e["type"] == "debut":
                if e["id"] in debuts or not _reel(e.get("pire_cas_usd")):
                    raise RegistreIllisible(f"registre {chemin} : ligne {n} : début en double ou pire cas invalide")
                debuts.add(e["id"])
            else:
                if e["id"] not in debuts or e["id"] in fins or not _reel(e.get("cout_usd")):
                    raise RegistreIllisible(f"registre {chemin} : ligne {n} : fin sans début, en double ou coût invalide")
                fins.add(e["id"])
            evenements.append(e)
    return evenements


def etat(chemin, etape=None):
    """{regle_usd, engage_usd, appels, en_cours, par_etape: {étape: {regle, engage}}, par_fournisseur: {...}}."""
    ev = lire(chemin)
    debuts = {e["id"]: e for e in ev if e["type"] == "debut"}
    fins = {e["id"]: e for e in ev if e["type"] == "fin"}
    regle = sum(float(f["cout_usd"]) for f in fins.values())
    engage = sum(float(d["pire_cas_usd"]) for i, d in debuts.items() if i not in fins)
    par_etape, par_fournisseur = {}, {}
    for i, d in debuts.items():
        for cle, table in ((d.get("etape") or "sans_etape", par_etape), (d.get("fournisseur") or "inconnu", par_fournisseur)):
            x = table.setdefault(cle, {"regle_usd": 0.0, "engage_usd": 0.0, "appels": 0})
            x["appels"] += 1
            if i in fins:
                x["regle_usd"] += float(fins[i]["cout_usd"])
            else:
                x["engage_usd"] += float(d["pire_cas_usd"])
    sortie = {"version": VERSION, "regle_usd": round(regle, 6), "engage_usd": round(engage, 6), "appels": len(debuts),
              "en_cours": sorted(i for i in debuts if i not in fins), "par_etape": par_etape, "par_fournisseur": par_fournisseur,
              "depassements_reserve": sum(1 for f in fins.values() if f.get("depassement_reserve"))}
    if etape is not None:
        sortie["etape"] = par_etape.get(etape, {"regle_usd": 0.0, "engage_usd": 0.0, "appels": 0})
    return sortie


class _Verrou:
    def __init__(self, chemin):
        self.chemin = chemin + ".verrou"

    def __enter__(self):
        self.f = open(self.chemin, "a", encoding="utf-8")
        fcntl.flock(self.f.fileno(), fcntl.LOCK_EX)
        return self

    def __exit__(self, *exc):
        fcntl.flock(self.f.fileno(), fcntl.LOCK_UN)
        self.f.close()
        return False


def _ajouter(chemin, objet):
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def reserver(chemin, *, plafond_cumule_usd, pire_cas_usd, fournisseur, role, modele, etape=None, plafond_etape_usd=None):
    """Garde 1 et garde 2 sous verrou ; rend l'identifiant de l'appel ; lève `PlafondCumule` (rien n'est écrit) sinon."""
    if not _reel(plafond_cumule_usd) or plafond_cumule_usd <= 0:
        raise PlafondCumule("plafond cumulé invalide")
    if not _reel(pire_cas_usd):
        raise PlafondCumule(f"pire cas invalide ({pire_cas_usd!r})")
    if not os.path.isdir(os.path.dirname(os.path.abspath(chemin))):
        raise RegistreIllisible(f"dossier du registre absent : {os.path.dirname(os.path.abspath(chemin))}")
    with _Verrou(chemin):
        e = etat(chemin, etape)
        total = e["regle_usd"] + e["engage_usd"] + pire_cas_usd
        if total > plafond_cumule_usd + EPS:
            raise PlafondCumule(f"garde cumulée : {e['regle_usd']:.4f} réglés + {e['engage_usd']:.4f} engagés + pire cas "
                                f"{pire_cas_usd:.4f} > {plafond_cumule_usd:g} USD : appel refusé, rien envoyé")
        if etape is not None and plafond_etape_usd is not None:
            x = e["etape"]
            t_e = x["regle_usd"] + x["engage_usd"] + pire_cas_usd
            if t_e > float(plafond_etape_usd) + EPS:
                raise PlafondCumule(f"garde d'étape ({etape}) : {x['regle_usd']:.4f} réglés + {x['engage_usd']:.4f} engagés + pire "
                                    f"cas {pire_cas_usd:.4f} > plafond dur {float(plafond_etape_usd):.2f} USD : appel refusé")
        ident = uuid.uuid4().hex
        _ajouter(chemin, {"type": "debut", "id": ident, "quand_utc": _maintenant(), "fournisseur": fournisseur, "role": role,
                          "modele": modele, "etape": etape, "plafond_etape_usd": plafond_etape_usd,
                          "pire_cas_usd": round(float(pire_cas_usd), 6), "version": VERSION})
    return ident


def regler(chemin, ident, *, cout_usd, pire_cas_usd, statut, code, cout_origine):
    """Ligne `fin` ; `depassement_reserve` vrai si le coût lu passe le pire cas réservé (liste d'arrêt : la commande le dit)."""
    cout = float(cout_usd) if _reel(cout_usd) else float(pire_cas_usd)
    with _Verrou(chemin):
        _ajouter(chemin, {"type": "fin", "id": ident, "quand_utc": _maintenant(), "cout_usd": round(cout, 6), "statut": statut,
                          "code": int(code), "cout_origine": cout_origine,
                          "depassement_reserve": cout > float(pire_cas_usd) + 1e-12})
    return cout > float(pire_cas_usd) + 1e-12


def restant(chemin, plafond_cumule_usd):
    e = etat(chemin)
    return max(0.0, float(plafond_cumule_usd) - e["regle_usd"] - e["engage_usd"])


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "etat":
        print(json.dumps(etat(sys.argv[2]), ensure_ascii=False, indent=1))
        sys.exit(0)
    if len(sys.argv) == 4 and sys.argv[1] == "restant":
        print(f"{restant(sys.argv[2], float(sys.argv[3])):.4f}")
        sys.exit(0)
    print("usage : registre_depense_cumulee_v1.py etat REGISTRE | restant REGISTRE PLAFOND", file=sys.stderr)
    sys.exit(2)
