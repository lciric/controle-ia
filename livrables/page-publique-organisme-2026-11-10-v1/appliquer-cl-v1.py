#!/usr/bin/env python3
"""Applique les couples de la contre-lecture v1 aux copies des deux brouillons de la page A1-v4.

Usage : python3 appliquer-cl-v1.py   (depuis n'importe quel dossier ; chemins absolus)

- Vérifie l'empreinte des trois entrées ; refuse de continuer sinon.
- Lit les couples « texte actuel -> texte corrigé » de la contre-lecture, dans l'ordre du fichier.
- Applique chaque couple à son fichier, à la suite ; refuse (sans l'appliquer) tout couple dont le
  texte actuel n'apparaît pas exactement une fois dans l'état courant du fichier.
- Remplace l'heure de la ligne « Last updated » par le marqueur <<HEURE_POUSSEE>>.
- Écrit deux variantes : v2/ (avec « Related work ») et v2-sans-related-work/ (sans ce paragraphe
  ni la ligne vide qui le suit) ; la page des résultats est la même dans les deux.
- N'écrase jamais une sortie existante (R12).
- Imprime un résumé JSON (couples appliqués ou refusés, empreintes des sorties).
"""
import hashlib
import json
import os
import re
import sys

BASE = "/home/user/page-a1v4"
PAGE = "resultats/attaque-goodhart-v2/README.md"
RACINE = "README.md"
CL = "contre-lecture-page-a1v4-v1.md"

EMPREINTES_ENTREES = {
    PAGE: "9f24f5598ac2838be648a38485c6c961ff0d5700319dbaa46266bff5d2b1c496",
    RACINE: "8e413d7801897c43dae849f712c6cdb1ac875e0532355208f03eba56cb37faa7",
    CL: "3cedcd29629598bc522b86f7900ed020f29e53855bffe0eb036bb8d2c1e0f8db",
}

NB_COUPLES_ATTENDU = 22

# Texte corrigé remplacé sur consigne de la mère (couple B2a) : la page ne nomme ni l'étiqueteur ni
# aucun autre projet ; l'écart se dit « a third-party use of the same provider during the run,
# declared; no disturbance measured ». Aucun chiffre ajouté. Vérifié contre registres/decisions.md
# R-2013 et R-2043 et contre le § 8 (l. 367) du texte scellé d306a8fa…7fe6.
SURCHARGES_CORRIGE = {
    "B2a": (
        "6. **Argon deviation** (both worlds): a third-party use of the same provider during the run, "
        "declared; no disturbance measured, no call of this run inside its window. The sealed text asks "
        "that nothing else use Argon during the run; by the project lead's decision, a disturbance "
        "reservation is written only if there was one, and the audit finds none."
    ),
}

LAST_UPDATED_ACTUEL = "Last updated: 10 November 2026, 10:18 UTC"
LAST_UPDATED_CORRIGE = "Last updated: 10 November 2026, <<HEURE_POUSSEE>> UTC"

PREFIXE_RELATED = "**Related work.**"

SORTIE_AVEC = os.path.join(BASE, "v2")
SORTIE_SANS = os.path.join(BASE, "v2-sans-related-work")


def sha256_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lire(chemin_rel: str) -> bytes:
    with open(os.path.join(BASE, chemin_rel), "rb") as f:
        return f.read()


def bloc_apres(lignes, i, etiquette):
    """Cherche, à partir de la ligne i, la ligne `etiquette` puis le bloc ```text qui suit.
    Rend (texte du bloc, indice de la ligne après la clôture)."""
    n = len(lignes)
    while i < n and lignes[i].strip() != etiquette:
        i += 1
    if i >= n:
        raise ValueError(f"étiquette introuvable : {etiquette!r}")
    i += 1
    while i < n and lignes[i].strip() == "":
        i += 1
    if i >= n or lignes[i].rstrip() != "```text":
        raise ValueError(f"bloc ```text attendu après {etiquette!r} (ligne {i + 1})")
    i += 1
    debut = i
    while i < n and lignes[i].rstrip() != "```":
        i += 1
    if i >= n:
        raise ValueError("bloc ```text non fermé")
    return "\n".join(lignes[debut:i]), i + 1


RE_ENTETE = re.compile(r"^\*\*([A-Z]\d+[a-z]?) — [^—]*? — `([^`]+)` — ")


def lire_couples(texte_cl: str):
    lignes = texte_cl.split("\n")
    entetes = [(k, m) for k, l in enumerate(lignes) for m in [RE_ENTETE.match(l)] if m]
    couples = []
    for j, (k, m) in enumerate(entetes):
        fin = entetes[j + 1][0] if j + 1 < len(entetes) else len(lignes)
        actuel, i = bloc_apres(lignes, k + 1, "Texte actuel :")
        corrige, i = bloc_apres(lignes, i, "Texte corrigé :")
        if i > fin:
            raise ValueError(f"couple {m.group(1)} : blocs au-delà de l'en-tête suivant")
        couples.append({
            "id": m.group(1),
            "fichier": m.group(2),
            "ligne_entete": k + 1,
            "actuel": actuel,
            "corrige_contre_lecture": corrige,
        })
    return couples


def main() -> int:
    # 1. Empreintes des entrées
    contenus = {}
    for rel, attendu in EMPREINTES_ENTREES.items():
        b = lire(rel)
        obtenu = sha256_octets(b)
        if obtenu != attendu:
            print(f"REFUS : empreinte de {rel} = {obtenu}, attendu {attendu}", file=sys.stderr)
            return 2
        contenus[rel] = b.decode("utf-8")

    # 2. Couples
    couples = lire_couples(contenus[CL])
    if len(couples) != NB_COUPLES_ATTENDU:
        print(f"REFUS : {len(couples)} couples lus, {NB_COUPLES_ATTENDU} attendus", file=sys.stderr)
        return 2
    ids = [c["id"] for c in couples]
    if len(set(ids)) != len(ids):
        print(f"REFUS : identifiants de couples en double : {ids}", file=sys.stderr)
        return 2
    for sid in SURCHARGES_CORRIGE:
        if sid not in ids:
            print(f"REFUS : surcharge pour un couple absent : {sid}", file=sys.stderr)
            return 2

    originaux = {PAGE: contenus[PAGE], RACINE: contenus[RACINE]}
    etat = dict(originaux)
    journal = []
    for c in couples:
        rel = c["fichier"]
        entree = {
            "id": c["id"],
            "fichier": rel,
            "ligne_entete_contre_lecture": c["ligne_entete"],
        }
        if rel not in etat:
            entree.update(applique=False, raison=f"fichier inconnu : {rel}")
            journal.append(entree)
            continue
        corrige = SURCHARGES_CORRIGE.get(c["id"], c["corrige_contre_lecture"])
        entree["texte_corrige_surcharge"] = c["id"] in SURCHARGES_CORRIGE
        n_orig = originaux[rel].count(c["actuel"])
        n_cour = etat[rel].count(c["actuel"])
        entree["occurrences_brouillon"] = n_orig
        entree["occurrences_etat_courant"] = n_cour
        if n_cour != 1:
            entree.update(applique=False,
                          raison=f"texte actuel présent {n_cour} fois dans l'état courant (1 exigé)")
            journal.append(entree)
            continue
        etat[rel] = etat[rel].replace(c["actuel"], corrige, 1)
        entree["applique"] = True
        entree["sha256_actuel"] = sha256_octets(c["actuel"].encode("utf-8"))
        entree["sha256_corrige_applique"] = sha256_octets(corrige.encode("utf-8"))
        journal.append(entree)

    # 3. Ligne « Last updated » (page des résultats)
    n_lu = etat[PAGE].count(LAST_UPDATED_ACTUEL)
    if n_lu != 1:
        print(f"REFUS : « {LAST_UPDATED_ACTUEL} » présent {n_lu} fois dans la page", file=sys.stderr)
        return 2
    if "Last updated" in etat[RACINE]:
        print("REFUS : une ligne « Last updated » existe aussi dans le README racine", file=sys.stderr)
        return 2
    etat[PAGE] = etat[PAGE].replace(LAST_UPDATED_ACTUEL, LAST_UPDATED_CORRIGE, 1)

    # 4. Variante sans « Related work »
    lignes = etat[RACINE].split("\n")
    idx = [k for k, l in enumerate(lignes) if l.startswith(PREFIXE_RELATED)]
    if len(idx) != 1:
        print(f"REFUS : {len(idx)} lignes commencent par {PREFIXE_RELATED!r} (1 exigée)", file=sys.stderr)
        return 2
    k = idx[0]
    if k + 1 >= len(lignes) or lignes[k + 1] != "":
        print("REFUS : la ligne qui suit « Related work » n'est pas vide", file=sys.stderr)
        return 2
    racine_sans = "\n".join(lignes[:k] + lignes[k + 2:])
    ligne_related = k + 1  # numéro de ligne (1-based) dans la variante avec

    # 5. Écriture (sans jamais écraser)
    sorties = {
        os.path.join(SORTIE_AVEC, RACINE): etat[RACINE],
        os.path.join(SORTIE_AVEC, PAGE): etat[PAGE],
        os.path.join(SORTIE_SANS, RACINE): racine_sans,
        os.path.join(SORTIE_SANS, PAGE): etat[PAGE],
    }
    for chemin in sorties:
        if os.path.exists(chemin):
            print(f"REFUS : la sortie existe déjà, jamais écrasée : {chemin}", file=sys.stderr)
            return 2
    for chemin, texte in sorties.items():
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, "xb") as f:
            f.write(texte.encode("utf-8"))

    resume = {
        "entrees": EMPREINTES_ENTREES,
        "couples_lus": len(couples),
        "couples_appliques": [e["id"] for e in journal if e["applique"]],
        "couples_non_appliques": [{"id": e["id"], "raison": e["raison"]} for e in journal if not e["applique"]],
        "detail": journal,
        "last_updated": {"avant": LAST_UPDATED_ACTUEL, "apres": LAST_UPDATED_CORRIGE},
        "related_work_retire_ligne_variante_avec": ligne_related,
        "sorties": {c: sha256_octets(t.encode("utf-8")) for c, t in sorties.items()},
    }
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    return 0 if not resume["couples_non_appliques"] else 1


if __name__ == "__main__":
    sys.exit(main())
