#!/usr/bin/env python3
"""Tirage des fiches de l'« épreuve fraîche » du pont fiche de course -> fiche-loi, version 2 (GO-2026-11-01-09).

Rédigé le 1er novembre 2026 par un sous-agent neuf de session-depot ; exécuté par session-depot, **après** le scellement du
préenregistrement `preregistrement-epreuve-pont-v2.md`. Aucun appel de modèle, aucun appel réseau.

Version 2 = version 1 (`tirer_fiches_v1.py`, inchangée, R12) avec deux changements, suites de la contre-lecture 1 :
- CL-02 : le tirage refuse de courir tant que l'empreinte du préenregistrement scellé **et** celle de la valeur engagée ne sont
  pas inscrites dans `registres/decisions.md`, sur le disque **et** dans la version poussée (`--ref-poussee`, par exemple
  `origin/main`, lue par `git show`) : l'inscription date le scellement avant le tirage ;
- CL-12 (b) : les six témoins sont placés **dans la première moitié** de l'ordre de passage (positions tirées parmi les sept
  premières, fiches au hasard dans les places restantes) : un arrêt par la garde de plafond perd d'abord des fiches, jamais un
  témoin tant qu'au plus sept passages sont perdus (avec un ordre uniforme, perdre le dernier passage aurait coûté un témoin
  avec une probabilité de 0,43 ; les deux derniers, 0,69 ; les trois derniers, 0,85).

Ce que fait le script (règles du préenregistrement, section « Plan d'analyse ») :
1. refuse de tourner si le préenregistrement n'est pas scellé et conforme (`controle_ia.prereg.exiger_prereg_scelle`), ou si
   ses empreintes ne sont pas inscrites et poussées au registre des décisions (CL-02) ;
2. lit dans le préenregistrement scellé l'empreinte de la **valeur engagée** par session-depot avant le scellement, et
   vérifie que la valeur révélée (64 caractères hexadécimaux) a bien cette empreinte SHA-256 ;
3. lit des fiches **seulement** les champs `auteur`, `identifiant_auteur`, `passe`, `nom`, `empreinte` (éligibilité et
   dédoublonnage) ; le contenu est copié sans être interprété (seule son empreinte est recalculée) ;
4. ferme les idées distinctes d'après la note des doublons (paires signalées par les deux juges, groupes fermés par
   transitivité), garde les idées dont au moins une fiche est de Fable et éligible (`classement.json`, champ `eligible`) ;
5. tire, par `numpy.random.SeedSequence(entropy=[empreinte du préenregistrement scellé, valeur engagée])` (R9), quatre
   enfants dérivés par tâche : sous-ensemble d'idées (si plus de 10 ; sinon toutes, déclaré), représentant de chaque idée
   (au hasard parmi ses fiches éligibles de Fable : jamais la mieux classée, pare-feu N-053), numérotation anonyme F-01…,
   ordre de passage (six témoins T1…T6 à des places tirées dans la première moitié, fiches au hasard ailleurs) ;
6. copie le **contenu seul** de chaque fiche tirée (vue anonyme : champs internes retirés) dans `fiches-tirees/F-kk.json`,
   après la garde des métadonnées du pont et la garde A4 des étiquettes ; écrit un manifeste d'empreintes ; chaque
   fichier reçoit son compagnon `.sha256` (R6). Le dossier de sortie doit être neuf (R12).

Les aides communes (garde A4, vue anonyme, lecture du préenregistrement scellé, écriture neuve) servent aussi au lanceur.
numpy n'est importé que dans `tirer` : le lanceur, qui tourne avec le Python des appels (sans numpy), importe ce module.

Usage (Python du dépôt, numpy >= 1.25) :
    python -I -B tirer_fiches_v2.py --valeur-engagee FICHIER_DE_LA_VALEUR --ref-poussee origin/main
Le fichier contient la valeur (64 caractères hexadécimaux, une ligne) ; elle n'est jamais passée en argument.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

VERSION = "tirage-epreuve-pont-v2"
ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[1]
PREREG = ICI / "preregistrement-epreuve-pont-v2.md"
ENTREE = ICI / "entree"
FICHES = ENTREE / "fiches-validees.json"
CLASSEMENT = ENTREE / "classement.json"
DOUBLONS = ENTREE / "lecture-complementaire-doublons-argon-v1.md"
SORTIE = ICI / "fiches-tirees"
MANIFESTE = "manifeste-tirage-v2.json"
REGISTRE = "registres/decisions.md"

AUTEUR_ELIGIBLE = "fable"
NOMBRE_VISE = 10
TEMOINS = ("T1", "T2", "T3", "T4", "T5", "T6")
CHAMPS_LUS = ("auteur", "identifiant_auteur", "passe", "nom", "empreinte")
CHAMPS_INTERNES = ("auteur", "identifiant_auteur", "empreinte", "passe", "temoin")  # `ideation_v2.CHAMPS_INTERNES` (v56)
# Clés de métadonnées refusées par la garde G3 du pont (`pont_v1.CLES_META_FICHE`) : jamais dans une vue servie.
CLES_META_PONT = ("ident", "meta", "empreinte", "case", "fournisseur", "passe", "origine", "bras", "classe", "temoin")
# Garde A4 (mode « mot entier » de `fiches_v54`, après normalisation) : identifiants de la course et rôles de l'épreuve.
ETIQUETTES_A4 = ("fable p1", "fable p2", "argon p1", "argon p2", "temoin p0", "temoin du pont", "temoins du pont",
                 "metteur en forme", "fiche fabriquee", "fiches fabriquees", "epreuve fraiche du pont",
                 "specification connue")
MOTIF_IDENT = re.compile(r"\b((?:fable|argon|temoin)-p\d-\d\d)\b")
MOTIF_VALEUR_ENGAGEE = re.compile(r"Empreinte de la valeur engagée[^\n:]*:\s*`?([0-9a-f]{64})`?")


class TirageRefuse(Exception):
    pass


class EtiquetteInterdite(TirageRefuse):
    pass


# --- aides communes ---------------------------------------------------------------------------------------------------

def sha256_octets(octets):
    return hashlib.sha256(octets).hexdigest()


def sha256_fichier(chemin):
    return sha256_octets(Path(chemin).read_bytes())


def json_canonique(objet):
    return json.dumps(objet, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def empreinte_objet(objet):
    """Même convention que `outils.empreinte_objet` de l'orchestrateur v56."""
    return sha256_octets(json_canonique(objet))


def ecrire_neuf(chemin, texte):
    """Écrit un fichier qui ne doit pas exister (R12), en UTF-8 et LF, avec son compagnon `.sha256` (R6)."""
    chemin = Path(chemin)
    with open(chemin, "x", encoding="utf-8", newline="\n") as f:
        f.write(texte)
    h = sha256_fichier(chemin)
    with open(str(chemin) + ".sha256", "x", encoding="utf-8", newline="\n") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def ecrire_json_neuf(chemin, objet):
    return ecrire_neuf(chemin, json.dumps(objet, ensure_ascii=False, indent=1) + "\n")


def verifier_compagnon(chemin):
    """Empreinte d'un fichier contre son compagnon `.sha256` ; lève TirageRefuse sinon (R11 : vérifié sur disque)."""
    chemin = Path(chemin)
    comp = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not comp.is_file():
        raise TirageRefuse(f"{chemin} ou son compagnon .sha256 absent sur disque")
    lignes = [l for l in comp.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(lignes) != 1 or not re.fullmatch(r"[0-9a-f]{64}  " + re.escape(chemin.name), lignes[0]):
        raise TirageRefuse(f"compagnon illisible : {comp}")
    attendue, obtenue = lignes[0][:64], sha256_fichier(chemin)
    if attendue != obtenue:
        raise TirageRefuse(f"{chemin} : empreinte {obtenue[:12]}… différente du compagnon {attendue[:12]}…")
    return obtenue


def prereg_scelle(chemin=PREREG):
    """Empreinte du préenregistrement s'il est scellé, intact et conforme (R1, R2) ; lève TirageRefuse sinon."""
    sys.path.insert(0, str(DEPOT / "src"))
    from controle_ia.gardes import GardeArret
    from controle_ia.prereg import exiger_prereg_scelle
    try:
        return exiger_prereg_scelle(chemin)
    except GardeArret as e:
        raise TirageRefuse(f"préenregistrement non scellé ou non conforme : {e}") from None


def empreinte_valeur_engagee(texte_prereg):
    trouvees = MOTIF_VALEUR_ENGAGEE.findall(texte_prereg)
    if len(trouvees) != 1:
        raise TirageRefuse(f"empreinte de la valeur engagée : une seule ligne attendue dans le préenregistrement "
                           f"({len(trouvees)} trouvée(s))")
    return trouvees[0]


def normaliser_texte(texte):
    """Miroir de `outils.normaliser_texte` (v56) : minuscules, accents retirés, non-alphanumériques -> espace."""
    decompose = unicodedata.normalize("NFD", texte)
    sans_accents = "".join(c for c in decompose if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]+", " ", sans_accents.lower()).strip()


def etiquettes_trouvees(objet, etiquettes=ETIQUETTES_A4):
    """Miroir de `fiches_v54.trouver(…, mode="mot_entier")`."""
    plat = normaliser_texte(objet if isinstance(objet, str) else json.dumps(objet, ensure_ascii=False))
    trouvees = []
    for e in etiquettes:
        n = normaliser_texte(e)
        if n and re.search(r"(?<![0-9a-z])" + re.escape(n) + r"(?![0-9a-z])", plat):
            trouvees.append(e)
    return sorted(trouvees)


def garde_a4(objet, quoi, etiquettes=ETIQUETTES_A4):
    trouvees = etiquettes_trouvees(objet, etiquettes)
    if trouvees:
        raise EtiquetteInterdite(f"A4 : étiquette interdite dans {quoi} ({', '.join(trouvees)}) : arrêt, entrée à "
                                 "reconstruire (aucune substitution silencieuse)")
    return True


def vue_anonyme(fiche):
    """Contenu seul : champs internes retirés ; refuse une clé de métadonnée restante (garde G3 du pont)."""
    if not isinstance(fiche, dict):
        raise TirageRefuse("fiche non dictionnaire")
    vue = {k: v for k, v in fiche.items() if k not in CHAMPS_INTERNES}
    restes = sorted(k for k in vue if normaliser_texte(k).replace(" ", "_") in CLES_META_PONT)
    if restes:
        raise TirageRefuse(f"métadonnée restante dans la vue anonyme : {restes}")
    return json.loads(json.dumps(vue, ensure_ascii=False))


def taille_servie(vue):
    """Mesure de la longueur servie (même mesure que `ideation_v2.taille_servie`, v56)."""
    return len(json.dumps([vue], ensure_ascii=False, indent=1))


def inscrites_et_poussees(depot, ref, empreintes):
    """CL-02 : chaque empreinte (64 caractères hexadécimaux, en entier) figure dans `registres/decisions.md` sur le disque et
    dans sa version de la référence poussée `ref` (`git show ref:registres/decisions.md`) ; lève TirageRefuse sinon."""
    if not ref:
        raise TirageRefuse("référence poussée absente (--ref-poussee) : l'inscription au registre ne peut être vérifiée")
    disque = Path(depot) / REGISTRE
    if not disque.is_file():
        raise TirageRefuse(f"{disque} absent sur disque")
    texte = disque.read_text(encoding="utf-8")
    try:
        pousse = subprocess.run(["git", "-C", str(depot), "show", f"{ref}:{REGISTRE}"], capture_output=True, text=True,
                                check=True, timeout=60).stdout
    except (OSError, subprocess.SubprocessError) as e:
        raise TirageRefuse(f"registre de la référence {ref!r} illisible : {type(e).__name__}") from None
    for h in empreintes:
        if h not in texte:
            raise TirageRefuse(f"empreinte {h[:12]}… absente de {REGISTRE} sur le disque (inscrire, commettre, pousser)")
        if h not in pousse:
            raise TirageRefuse(f"empreinte {h[:12]}… absente de {REGISTRE} dans {ref} (commettre et pousser avant le tirage)")
    return True


def ordre_temoins_en_tete(fiches, temoins, rng):
    """CL-12 (b) : témoins à des places tirées parmi les max(⌈n/2⌉, nombre de témoins) premières, fiches au hasard ailleurs
    (ici : 6 témoins parmi les 7 premières places sur 14)."""
    n = len(fiches) + len(temoins)
    moitie = max((n + 1) // 2, len(temoins))
    places_t = sorted(int(i) for i in rng.choice(moitie, size=len(temoins), replace=False))
    t_ordre = [temoins[int(i)] for i in rng.permutation(len(temoins))]
    f_ordre = [fiches[int(i)] for i in rng.permutation(len(fiches))]
    ordre, it_t, it_f = [], iter(t_ordre), iter(f_ordre)
    for k in range(n):
        ordre.append(next(it_t) if k in places_t else next(it_f))
    return ordre


# --- idées distinctes -------------------------------------------------------------------------------------------------

def groupes_de_doublons(texte_note):
    """Lignes du tableau de la note : rang, fiche gardée, total, éligible, doublons ; rend [(membres triés, éligible)]."""
    groupes = []
    for ligne in texte_note.splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) < 5 or not cellules[0].isdigit():
            continue
        gardee = MOTIF_IDENT.findall(cellules[1])
        if not gardee:
            raise TirageRefuse(f"ligne de la note sans fiche gardée : rang {cellules[0]}")
        doublons = MOTIF_IDENT.findall(cellules[-1])
        eligible = cellules[-2]
        if eligible not in ("oui", "non"):
            raise TirageRefuse(f"colonne « Éligible » illisible au rang {cellules[0]} : {eligible!r}")
        groupes.append((sorted({gardee[0], *doublons}), eligible == "oui"))
    return groupes


def fermer_groupes(groupes):
    """Fermeture transitive (union de groupes qui partagent une fiche)."""
    parent = {}

    def racine(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for membres, _ in groupes:
        for m in membres:
            parent.setdefault(m, m)
        for m in membres[1:]:
            parent[racine(m)] = racine(membres[0])
    fermes = {}
    for m in parent:
        fermes.setdefault(racine(m), set()).add(m)
    return sorted((sorted(v) for v in fermes.values()), key=lambda g: g[0])


def idees_eligibles(fiches, classement, texte_note, auteur=AUTEUR_ELIGIBLE):
    """Idées distinctes (groupes fermés) et, pour chacune, ses fiches éligibles de l'auteur visé. Ne lit que CHAMPS_LUS."""
    lues = []
    for f in fiches:
        if not isinstance(f, dict) or any(k not in f for k in CHAMPS_LUS):
            raise TirageRefuse("fiche sans les champs d'identité attendus")
        lues.append({k: f[k] for k in CHAMPS_LUS})
    par_ident = {f["identifiant_auteur"]: f for f in lues}
    if len(par_ident) != len(lues):
        raise TirageRefuse("identifiants d'auteur en double dans les fiches validées")
    lignes = classement.get("lignes") if isinstance(classement, dict) else None
    if not isinstance(lignes, list):
        raise TirageRefuse("classement sans « lignes »")
    eligible = {}
    for l in lignes:
        i = l.get("identifiant_auteur")
        if i not in par_ident:
            raise TirageRefuse(f"fiche du classement absente des fiches validées : {i!r}")
        if l.get("empreinte") != par_ident[i]["empreinte"]:
            raise TirageRefuse(f"empreinte différente entre classement et fiches validées : {i}")
        if not isinstance(l.get("eligible"), bool):
            raise TirageRefuse(f"champ « eligible » non booléen : {i}")
        eligible[i] = l["eligible"]
    if set(eligible) != set(par_ident):
        raise TirageRefuse("le classement ne couvre pas exactement les fiches validées")
    bruts = groupes_de_doublons(texte_note)
    groupes = fermer_groupes(bruts)
    couverts = [m for g in groupes for m in g]
    if sorted(couverts) != sorted(par_ident) or len(couverts) != len(set(couverts)):
        raise TirageRefuse("les groupes de la note ne forment pas une partition des fiches validées")
    for membres, elig in bruts:  # la colonne « Éligible » de la note doit concorder avec le classement
        if any(eligible[m] for m in membres) != elig:
            raise TirageRefuse(f"éligibilité de la note différente du classement pour {membres}")
    idees = []
    for g in groupes:
        candidates = sorted(m for m in g if par_ident[m]["auteur"] == auteur and eligible[m])
        idees.append({"membres": g, "eligibles_auteur": candidates})
    compte = {"fiches": len(lues), "idees_distinctes": len(groupes),
              "paires_de_doublons": sum(len(g) - 1 for g in groupes),
              "fiches_eligibles": sum(eligible.values()),
              "fiches_auteur": sum(1 for f in lues if f["auteur"] == auteur),
              "idees_auteur_eligibles": sum(1 for i in idees if i["eligibles_auteur"])}
    return [i for i in idees if i["eligibles_auteur"]], compte, par_ident


# --- tirage -----------------------------------------------------------------------------------------------------------

def tirer(*, prereg=PREREG, valeur, fiches=FICHES, classement=CLASSEMENT, doublons=DOUBLONS, sortie=SORTIE,
          nombre_vise=NOMBRE_VISE, auteur=AUTEUR_ELIGIBLE, temoins=TEMOINS, depot=DEPOT, ref_poussee=None):
    import numpy as np
    from numpy.random import SeedSequence

    if tuple(int(x) for x in np.__version__.split(".")[:2]) < (1, 25):
        raise TirageRefuse(f"numpy >= 1.25 exigé (R9) ; trouvé {np.__version__}")
    sha_prereg = prereg_scelle(prereg)
    engagee = empreinte_valeur_engagee(Path(prereg).read_text(encoding="utf-8"))
    if not (isinstance(valeur, str) and re.fullmatch(r"[0-9a-f]{64}", valeur)):
        raise TirageRefuse("valeur engagée : 64 caractères hexadécimaux en minuscules attendus")
    if sha256_octets(valeur.encode("ascii")) != engagee:
        raise TirageRefuse("la valeur révélée n'a pas l'empreinte engagée dans le préenregistrement scellé")
    inscrites_et_poussees(depot, ref_poussee, [sha_prereg, engagee])
    sortie = Path(sortie)
    if sortie.exists():
        raise TirageRefuse(f"{sortie} existe déjà (R12 : on n'écrase jamais)")

    brut_fiches = json.loads(Path(fiches).read_text(encoding="utf-8"))
    brut_classement = json.loads(Path(classement).read_text(encoding="utf-8"))
    idees, compte, par_ident = idees_eligibles(brut_fiches, brut_classement, Path(doublons).read_text(encoding="utf-8"),
                                               auteur)
    if not idees:
        raise TirageRefuse(f"aucune idée éligible de l'auteur {auteur!r}")

    racine = SeedSequence(entropy=[int(sha_prereg, 16), int(valeur, 16)])
    taches = ("sous_ensemble", "representants", "numerotation", "ordre")
    enfants = dict(zip(taches, racine.spawn(len(taches))))
    rng = {t: np.random.default_rng(enfants[t]) for t in taches}

    if len(idees) > nombre_vise:
        choisies = sorted(int(i) for i in rng["sous_ensemble"].choice(len(idees), size=nombre_vise, replace=False))
        regle = f"{nombre_vise} idées tirées sans remise parmi {len(idees)}"
    else:
        choisies = list(range(len(idees)))
        regle = f"toutes les idées éligibles ({len(idees)}, moins de {nombre_vise + 1}) : aucune n'est écartée"
    representants = []
    for i in choisies:
        cands = idees[i]["eligibles_auteur"]
        representants.append(cands[int(rng["representants"].integers(len(cands)))])
    permutation = [int(i) for i in rng["numerotation"].permutation(len(representants))]
    numeros = {f"F-{k + 1:02d}": representants[j] for k, j in enumerate(permutation)}
    ordre = ordre_temoins_en_tete(list(numeros), list(temoins), rng["ordre"])

    par_ident_complet = {f["identifiant_auteur"]: f for f in brut_fiches}
    vues = {}
    for num, ident in numeros.items():
        vue = vue_anonyme(par_ident_complet[ident])
        if empreinte_objet(vue) != par_ident[ident]["empreinte"]:
            raise TirageRefuse(f"{num} : le contenu ne redonne pas l'empreinte de la fiche validée")
        garde_a4(vue, f"la fiche servie {num}")
        vues[num] = vue

    sortie.mkdir(parents=True, exist_ok=False)
    fichiers = {}
    for num, vue in vues.items():
        h = ecrire_json_neuf(sortie / f"{num}.json", vue)
        fichiers[num] = {"fichier": f"{num}.json", "sha256": h, "identifiant_auteur": numeros[num],
                         "empreinte_fiche_validee": par_ident[numeros[num]]["empreinte"], "taille_servie": taille_servie(vue)}
    manifeste = {
        "version": VERSION, "script_sha256": sha256_fichier(__file__),
        "preenregistrement": {"chemin": str(Path(prereg).name), "sha256": sha_prereg},
        "valeur_engagee": {"valeur": valeur, "sha256": engagee},
        "inscription_registre": {"registre": REGISTRE, "ref_poussee": ref_poussee},
        "graines": {"methode": "numpy.random.SeedSequence(entropy=[int(sha256 du préenregistrement scellé, 16), "
                               "int(valeur engagée, 16)]).spawn(4)", "entropie": [sha_prereg, valeur],
                    "taches": list(taches), "numpy": np.__version__},
        "entrees": {"fiches_validees": sha256_fichier(fiches), "classement": sha256_fichier(classement),
                    "note_doublons": sha256_fichier(doublons)},
        "comptes": dict(compte, idees_retenues=len(choisies), regle_sous_ensemble=regle),
        "idees_eligibles": [i["membres"] for i in idees],
        "fiches_tirees": fichiers,
        "temoins": list(temoins),
        "ordre_de_passage": ordre,
        "regle_ordre": ("témoins à des places tirées parmi les max(⌈n/2⌉, nombre de témoins) premières ; fiches au hasard "
                        "dans les places restantes"),
        "champs_lus": list(CHAMPS_LUS), "champs_internes_retires": list(CHAMPS_INTERNES),
        "etiquettes_a4": list(ETIQUETTES_A4),
    }
    ecrire_json_neuf(sortie / MANIFESTE, manifeste)
    return manifeste


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--valeur-engagee", required=True, help="fichier qui contient la valeur engagée (une ligne)")
    a.add_argument("--ref-poussee", required=True, help="référence git poussée qui porte l'inscription (CL-02)")
    a.add_argument("--sortie", default=str(SORTIE))
    args = a.parse_args(argv)
    valeur = Path(args.valeur_engagee).read_text(encoding="ascii").strip()
    try:
        m = tirer(valeur=valeur, sortie=args.sortie, ref_poussee=args.ref_poussee)
    except TirageRefuse as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    c = m["comptes"]
    print(f"tirage fait : {c['idees_retenues']} idées de {AUTEUR_ELIGIBLE} ({c['regle_sous_ensemble']}) ; "
          f"{len(m['ordre_de_passage'])} passages ; manifeste {Path(args.sortie) / MANIFESTE}")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
