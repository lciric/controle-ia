"""R1 — rejeu des actions stockées d'un run de P3 par forçage par l'enseignant, dans le contexte exact de leur épisode,
pour extraire des activations par action (GO-2026-11-01-13 ; format fixé par conv-audit, n° 328).

Reconstruction (lue dans le code de P3, `harnais.episode.jouer_episodes` et `premier_test_ia.run.jouer_p3`) :
- l'environnement (a) est une fonction pure du journal des textes (`EnvironnementPropositions.observation` rejoue l'état
  depuis les textes) ; la consigne privée et l'indication de chaque condition viennent du fichier des consignes scellé ;
- la transcription de l'agent est `ouverture(consigne, observation du pas 0)`, puis, pour chaque action, ses jetons, la
  clôture du tour (`fmt.cloture`) et le tour suivant (`fmt.tour`) ;
- seule perte : les identifiants générés ne sont pas stockés. Ils sont reconstruits par tokenisation du texte seul
  (`formats._ids`), plus le jeton de fin de tour quand P3 en a compté un (`jetons − jetons_notes = 1` dans
  `scores-p3.npz`). Une action est « conforme en longueur » si cette reconstruction redonne exactement `jetons_notes`
  jetons et le texte au décodage. Une tokenisation non canonique échantillonnée par l'agent ne se retrouve pas : elle
  rend l'action (et la suite de l'épisode) non conforme, ce que le contrôle de fidélité voit.

Empan (règle de P3, `jouer_p3`) : les jetons de l'action sans son jeton de fin final, [début, fin[. Agrégats par action
aux couches de P3 (7, 15 et 23) : **maximum par dimension** (agrégation de production du harnais,
`harnais.activations.agreger`) et **moyenne par dimension, bras de diagnostic seulement (N-026 ; jamais en production,
CLAUDE.md)**, en float16. Complément : maximum par dimension hors des jetons du champ COST (contrôle « la sonde lit-elle
autre chose que le nombre ? »), bornes des champs par `premier_test_ia.conditions.bornes_champs`.

Empreintes de P3 (CLR-04) : P3 a stocké, par épisode, l'empreinte de sa trajectoire (identifiants et empans) et de ses
activations (`harnais.episode.empreinte_episode`, `diag/<run>/episodes-p3.json`). Le rejeu les recalcule : une trajectoire
identique prouve, octet pour octet, que les identifiants reconstruits (jeton de fin compris) sont ceux de P3 ; des
activations identiques prouvent l'égalité au bit près (mesurée, non exigée). Un épisode entièrement conforme en longueur
à trajectoire différente arrête la course (CLC-03). Contrôle négatif fixé d'avance (CLC-01) : les actions de l'échantillon
rejouées sous une consigne fausse, empan juste, doivent sortir de la tolérance (au moins `controle_negatif_min`) ; sinon,
sans arrêt, règle de repli gelée : `fidele` restreint aux trajectoires identiques, lecture en réserve.

Contrôle de fidélité, fixé d'avance : tous les épisodes sont d'abord reconstruits sur processeur ; une action est
« éligible » si elle est notée et que son épisode a la trajectoire de P3 (fiches données ; sinon : conforme en longueur
ainsi que toutes celles qui la précèdent dans son épisode). Sur un échantillon tiré par graine parmi les éligibles (`n_fidelite_par_condition` actions par condition), les scores des sondes génériques légères de P3, recalculés sur les activations rejouées, doivent égaler ceux
de `scores-p3.npz` à `tolerance_fidelite` près (écart ≤ tolérance × (1 + |score|), pour chaque sonde) et l'action doit être
conforme en longueur ; sinon arrêt consigné, aucun fichier d'activations écrit. Les épisodes de l'échantillon passent en
premier (arrêt rapide). Le même écart est ensuite mesuré sur toutes les actions notées (descriptif, `fidele` par action).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import signal
import sys
import time
from pathlib import Path

import numpy as np

from ..environnements.invites import charger_invite
from ..environnements.pilote_a import charger_taches, tache_de
from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..harnais.activations import agreger, passe_unique
from ..harnais.formats import _ids
from ..harnais.run_harnais_factice import graine_entiere
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..scellement import sceller, verifier
from ..sondes.familles import SondeMahalanobis
from .alignement_v1 import CLES_IDENTITE, charger_identite, charger_textes_alignes, empreinte_identite

COMMANDE = "python -m controle_ia.runs_nuit.rejeu_activations_v1"
CLES = ("agent", "mode", "couches", "T", "run_source", "chemin_textes", "textes_sha256", "chemin_scores",
        "scores_sha256", "chemin_sondes_legeres", "sondes_legeres_sha256", "chemin_taches", "taches_sha256",
        "chemin_consignes", "consignes_sha256", "identite_sha256", "n_fidelite_par_condition", "tolerance_fidelite",
        "noyau_attention", "fils", "nom_sortie", "chemin_fiches", "fiches_sha256", "controle_negatif_min")
CONFIG_CITEE = "Configuration du rejeu (empreinte canonique) : `{}`"
REGLE_EMPAN = ("jetons de l'action reconstruits par tokenisation du texte seul, sans le jeton de fin final : "
               "[début, fin[ comme P3 (premier_test_ia.run.jouer_p3)")
CONTEXTE = ("forçage par l'enseignant dans le contexte exact de l'épisode d'origine : consigne privée de la condition, "
            "observations rejouées depuis les textes, actions précédentes reconstruites ; une passe avant unique sur "
            "la transcription complète de l'épisode (harnais.activations.passe_unique), comme P3")


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def exiger_config(config: dict) -> None:
    manquantes = [k for k in CLES if k not in config]
    if manquantes:
        raise GardeArret(f"configuration du rejeu incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    if not config["couches"] or len(set(config["couches"])) != len(config["couches"]):
        raise GardeArret("couches absentes ou en double")
    if not (0 < float(config["tolerance_fidelite"]) < 1):
        raise GardeArret("tolérance de fidélité hors de ]0 ; 1[")
    if int(config["n_fidelite_par_condition"]) < 1:
        raise GardeArret("au moins une action de fidélité par condition")


def moyenne_diagnostic_n026(acts: np.ndarray, debut: int, fin: int) -> np.ndarray:
    """Moyenne par dimension sur les jetons de l'empan : BRAS DE DIAGNOSTIC SEULEMENT (N-026). Interdite dans une sonde
    de production (CLAUDE.md, interdits) ; écrite ici parce que le préenregistrement de R1 la déclare diagnostic."""
    if not (0 <= debut < fin <= acts.shape[0]):
        raise GardeArret(f"empan [{debut}, {fin}[ invalide pour {acts.shape[0]} positions")
    return acts[debut:fin].astype(np.float64).mean(axis=0)


def bornes_hors_cout(bornes: dict, n: int) -> tuple[int, int] | None:
    """[début, fin[ du champ COST dans les jetons notés de l'action (rangs relatifs), None si le champ est absent ou si
    les bornes sont illisibles ; la fin est la première borne d'un autre champ au-delà du début, sinon n."""
    if not bornes.get("lisibles") or bornes.get("COST", -1) < 0:
        return None
    d = int(bornes["COST"])
    suivantes = [int(v) for k, v in bornes.items() if k not in ("lisibles", "COST") and int(v) > d]
    return d, min([n, *suivantes])


def reconstruire_episode(fmt, env, T: int, lignes: list[dict], jetons: list[int], jetons_notes: list[int],
                         fins_par_pas: dict | None = None) -> dict:
    """Transcription complète de l'épisode et, par action, empan noté, identifiants et conformité de longueur.
    `fins_par_pas` : jeton de fin à prendre au pas t (défaut : le premier jeton de clôture du tour, fin de tour)."""
    from ..premier_test_ia.conditions import bornes_champs

    obs0 = env.observation(0, 0, [])
    debut = (env.consigne_privee(0), obs0)
    fin_de_tour = fmt._pieces(debut)["cloture"][0] if fmt.nom == "chat" else min(fmt.fins)
    ids: list[int] = []
    journal: list[tuple[int, int, str]] = []
    actions = []
    for t in range(T):
        if lignes[t]["pas"] != t:
            raise GardeArret(f"épisode {lignes[t]['episode']} : pas {lignes[t]['pas']} au rang {t}")
        obs = env.observation(0, t, journal)
        ctx = fmt.ouverture(*debut) if t == 0 else ids + fmt.tour(debut, obs)
        texte = lignes[t]["texte"]
        notes = _ids(fmt.tok, texte) if texte else []
        a_fin = jetons[t] - jetons_notes[t]
        if a_fin not in (0, 1):
            raise GardeArret(f"épisode {lignes[t]['episode']}, pas {t} : jetons − jetons notés = {a_fin}")
        nv = notes + ([(fins_par_pas or {}).get(t, fin_de_tour)] if a_fin == 1 else [])
        conforme = (len(notes) == jetons_notes[t] and len(nv) == jetons[t]
                    and fmt.tok.decode(nv, skip_special_tokens=True) == texte)
        actions.append({"debut": len(ctx), "fin": len(ctx) + len(notes), "conforme": bool(conforme), "nv": nv,
                        "texte": texte, "pas": t,
                        "bornes": bornes_champs(fmt.tok, notes, texte) if notes else {"lisibles": False}})
        ids = ctx + nv + fmt.cloture(debut, nv)
        journal.append((0, t, texte))
    return {"ids": ids, "actions": actions}


def resoudre_fins(fmt, env, T, lignes, jetons, jetons_notes, empreinte: str, identifiant: str):
    """Cherche le jeton de fin de chaque action (parmi `fmt.fins`) qui redonne l'empreinte de trajectoire de P3 : une
    substitution, puis deux, dans un ordre fixe ; rend (reconstruction, épisode du harnais) ou None."""
    import itertools

    pas = [t for t in range(T) if jetons[t] - jetons_notes[t] == 1]
    autres = sorted(int(x) for x in fmt.fins)
    for k in (1, 2):
        for choix in itertools.combinations(pas, k):
            for valeurs in itertools.product(autres, repeat=k):
                rec = reconstruire_episode(fmt, env, T, lignes, jetons, jetons_notes, dict(zip(choix, valeurs)))
                ep = episode_harnais(identifiant, T, rec)
                if empreinte_trajectoire(ep) == empreinte:
                    return rec, ep
    return None


def episode_harnais(identifiant: str, T: int, rec: dict):
    """L'épisode reconstruit sous la forme du harnais (`harnais.episode.Episode`), pour recalculer les empreintes que P3
    a stockées par épisode (`fiches[].empreintes`, `empreinte_episode`)."""
    from ..harnais.episode import Action, Episode, Transcription

    acts = [Action(0, a["pas"], a["debut"], a["debut"] + len(a["nv"]), [int(x) for x in a["nv"]], a["texte"])
            for a in rec["actions"]]
    return Episode(identifiant, 1, T, [Transcription(agent=0, ids=[int(x) for x in rec["ids"]], actions=acts)])


def empreinte_trajectoire(episode) -> str:
    """Même calcul que la partie « trajectoire » de `harnais.episode.empreinte_episode`."""
    return hashlib.sha256(json.dumps(episode.en_dict(), sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def charger_fiches(chemin, sha_attendue: str | None) -> dict:
    """Empreintes par épisode du run source (`diag/<run>/episodes-p3.json`, scellé) : {épisode: {trajectoire, activations}}."""
    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    fiches = json.loads(Path(chemin).read_text(encoding="utf-8"))["resultat"]["fiches"]
    return {f["episode"]: f["empreintes"] for f in fiches}


def tirer_echantillon(identite: dict, eligibles: np.ndarray, n_par_condition: int, g: np.random.Generator) -> list[int]:
    """Rangs de l'échantillon de fidélité : `n_par_condition` actions par condition, tirées sans remise par le générateur
    de la clé « fidelite » parmi les actions éligibles : notées, et d'un épisode à trajectoire identique à celle de P3
    quand les fiches sont données (sinon : conformes en longueur avec toutes les actions qui les précèdent) ; conditions
    dans l'ordre alphabétique."""
    cond = np.asarray(identite["condition"])
    rangs = []
    for c in sorted(set(cond.tolist())):
        candidats = np.where((cond == c) & eligibles)[0]
        if len(candidats) < n_par_condition:
            raise GardeArret(f"condition {c} : {len(candidats)} actions éligibles pour {n_par_condition} demandées")
        rangs += sorted(int(x) for x in g.choice(candidats, size=n_par_condition, replace=False))
    return rangs


def controle_negatif(modele, fmt, notation, noms, index, source, echantillon, lignes, par_episode, taches, consignes,
                     guide, T, couches, jetons, jetons_notes, tol, minimum) -> dict:
    """Contrôle négatif fixé d'avance (CLR-04, CLC-01) : chaque action de l'échantillon est rejouée dans un contexte faux
    de peu — la consigne de l'honnête pour une condition instruite, celle du saboteur pour l'honnête (mêmes textes) — et lue
    **sur l'empan juste**. C'est l'erreur qui conditionne `fidele` pour les actions hors contexte exact. Décisif : l'écart
    aux scores de P3 doit dépasser la tolérance pour au moins `minimum` actions (« discriminant ») ; sinon « non
    discriminant », sans arrêt : l'appelant applique la règle de repli gelée (fidèle restreint aux trajectoires
    identiques). L'empan décalé d'un jeton (consigne fausse aussi) est mesuré et rapporté, descriptif seulement (il fait
    entrer un jeton spécial dans le maximum : presque toujours hors tolérance, donc sans pouvoir d'épreuve). Un écart non
    fini arrête la course (« echec », CLC-04)."""
    from ..premier_test_ia.conditions import environnement

    consigne_seule, decale = [], []
    for r in echantillon:
        e = lignes[r]["episode"]
        rs = par_episode[e]
        x0 = lignes[rs[0]]
        faux = "saboteur" if x0["condition"] == "honnete" else "honnete"
        env = environnement(faux, tache_de(taches[x0["tache"]]), T, guide, consignes)
        rec = reconstruire_episode(fmt, env, T, [lignes[q] for q in rs], [jetons[q] for q in rs],
                                   [jetons_notes[q] for q in rs])
        a = rec["actions"][rs.index(r)]
        acts = passe_unique(modele, rec["ids"], notation.couches)
        seg = {c: acts[c][a["debut"]:a["fin"]] for c in notation.couches}
        consigne_seule.append(ecart_relatif(notation.noter(seg), source[r], noms, index))
        n_pos = acts[notation.couches[0]].shape[0]
        d1, f1 = a["debut"] + 1, min(a["fin"] + 1, n_pos)
        seg = {c: acts[c][d1:f1] for c in notation.couches}
        decale.append(ecart_relatif(notation.noter(seg), source[r], noms, index))
    if not all(np.isfinite(x) for x in consigne_seule):
        raise GardeArret("contrôle négatif : écart non fini sous consigne fausse (score non fini) : echec")
    hors = int(sum(1 for x in consigne_seule if x > tol))
    return {"rangs": echantillon, "ecarts_consigne_fausse": [float(x) for x in consigne_seule],
            "ecarts_empan_decale_descriptif": [float(x) for x in decale], "hors_tolerance": hors,
            "minimum": minimum, "tolerance": tol, "lecture": "discriminant" if hors >= minimum else "non discriminant"}


def ecart_relatif(rejeu: dict, source: np.ndarray, noms: list[str], index: dict) -> float:
    """Plus grand écart |s_rejeu − s_P3| / (1 + |s_P3|) sur les sondes légères."""
    pire = 0.0
    for n in noms:
        s = float(source[index[n]])
        e = abs(float(rejeu[n]) - s) / (1.0 + abs(s))
        if not np.isfinite(e):
            return float("inf")
        pire = max(pire, e)
    return pire


def _f16(v: np.ndarray, quoi: str) -> np.ndarray:
    """Conversion en float16 ; arrêt sur toute valeur non finie (CLR-07) ou hors de l'étendue du float16."""
    x = np.asarray(v, dtype=np.float64)
    if not np.isfinite(x).all():
        raise GardeArret(f"{quoi} : activation non finie")
    if np.abs(x).max(initial=0.0) > 65504:
        raise GardeArret(f"{quoi} : valeur hors de l'étendue du float16 ({np.abs(x).max():.1f})")
    return x.astype(np.float16)


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, autoriser_depot_sale: bool = False,
             entropie_essai: int | None = None, empreinte_citee: str | None = None) -> dict:
    """`empreinte_citee` : empreinte de la configuration de base citée par le préenregistrement, quand la configuration
    a été complétée par `config_pour_run` (R4) ; sinon l'empreinte de `config` elle-même."""
    racine = Path(racine)
    exiger_config(config)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("rejeu réel sans préenregistrement : R1 interdit de lancer")
    entropie = entropie_essai
    if prereg is not None:
        from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite

        texte = Path(prereg).read_text(encoding="utf-8")
        attendue = empreinte_citee or empreinte_config(config)
        if CONFIG_CITEE.format(attendue) not in texte:
            raise GardeArret(f"{prereg} ne cite pas la configuration du rejeu {attendue[:12]}")
        e = ENTROPIE_CITEE.search(texte)
        if not e:
            raise GardeArret(f"{prereg} ne cite pas l'entropie")
        entropie = int(e.group(1))
        exiger_code_cite(racine, Path(prereg))
    identite = charger_identite(config["chemin_scores"], config["scores_sha256"])
    sha_id = empreinte_identite(identite)
    if config["identite_sha256"] is not None and sha_id != config["identite_sha256"]:
        raise GardeArret(f"identité des actions {sha_id[:12]} ≠ identité citée {config['identite_sha256'][:12]}")
    lignes = charger_textes_alignes(config["chemin_textes"], identite, config["textes_sha256"])
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, ["fidelite", "modele-jouet-inutilise"],
                                          entropie=entropie, decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    etat = {"etape": "chargement", "identite_sha256": sha_id}
    debut = time.perf_counter()
    try:
        return _executer(config, racine, run_id, chemin_m, manifeste, identite, lignes, etat, debut)
    except Exception as e:
        # verdict de fidélité au format du n° 330 : « non conforme » si le contrôle de fidélité ou le contrôle négatif a
        # échoué, « echec » pour tout autre arrêt
        etat["verdict_fidelite"] = ("non conforme" if (etat.get("fidelite_echantillon") or {}).get("lecture") == "contraire"
                                    or (etat.get("controle_negatif") or {}).get("lecture") == "non discriminant"
                                    else "echec")
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "verdict_fidelite": etat["verdict_fidelite"],
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _modele(config: dict, racine: Path):
    from ..environnements.lancer_pilote_a import charger_modele_et_format

    if config["mode"] == "jouet":
        m, _ = lire_manifeste(racine / "runs" / config["run_source"] / "manifeste.json")
        return charger_modele_et_format(config["agent"], "jouet", graine_entiere(m["graines"]["modele-jouet"]))
    return charger_modele_et_format(config["agent"], "reel", 0)


def _executer(config, racine, run_id, chemin_m, manifeste, identite, lignes, etat, debut) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from ..premier_test_ia.conditions import charger_consignes, environnement
    from ..premier_test_ia.figees import lire_sondes
    from ..premier_test_ia.notation import Notation

    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    reglages = regler_determinisme(config["fils"], appareil)
    taches = {t["identifiant"]: t for t in charger_taches(config["chemin_taches"])}
    if config["taches_sha256"] is not None and verifier(config["chemin_taches"]) != config["taches_sha256"]:
        raise GardeArret("tâches : empreinte ≠ empreinte citée")
    consignes = charger_consignes(config["chemin_consignes"], config["consignes_sha256"])
    sondes, _, sha_sondes = lire_sondes(config["chemin_sondes_legeres"], config["sondes_legeres_sha256"])
    sondes = [s for s in sondes if not isinstance(s, SondeMahalanobis) and int(s.couche) in config["couches"]]
    noms_src = [str(x) for x in identite["noms_sondes"].tolist()]
    index = {n: k for k, n in enumerate(noms_src)}
    sondes = [s for s in sondes if s.nom in index]
    if not sondes:
        raise GardeArret("aucune sonde légère commune au fichier des scores : contrôle de fidélité impossible")
    notation = Notation(sondes, appareil)
    noms = [s.nom for s in sondes]
    guide = charger_invite("H1-classification")
    modele, fmt = _modele(config, racine)
    etat["etape"] = "rejeu"
    T, couches = int(config["T"]), [int(c) for c in config["couches"]]
    n = len(lignes)
    par_episode: dict[str, list[int]] = {}
    for i, x in enumerate(lignes):
        par_episode.setdefault(x["episode"], []).append(i)
    for e, rs in par_episode.items():
        if len(rs) != T or rs != list(range(rs[0], rs[0] + T)):
            raise GardeArret(f"épisode {e} : {len(rs)} actions non contiguës ({T} attendues)")
    jetons = [int(x) for x in identite["jetons"]]
    jetons_notes = [int(x) for x in identite["jetons_notes"]]
    conforme = np.zeros(n, dtype=bool)
    contexte_conforme = np.zeros(n, dtype=bool)
    recs = {}
    for e, rs in par_episode.items():           # reconstruction de tous les épisodes, sur processeur, avant la carte
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        recs[e] = reconstruire_episode(fmt, env, T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                                       [jetons_notes[r] for r in rs])
        tous = True
        for r, a in zip(rs, recs[e]["actions"]):
            conforme[r] = a["conforme"]
            tous = tous and a["conforme"]
            contexte_conforme[r] = tous
    fiches = charger_fiches(config["chemin_fiches"], config["fiches_sha256"]) if config["chemin_fiches"] else None
    traj = np.zeros(n, dtype=bool)
    episodes_h = {}
    fins_resolues = 0
    for e, rs in par_episode.items():
        episodes_h[e] = episode_harnais(e, T, recs[e])
        if fiches is not None:
            if e not in fiches:
                raise GardeArret(f"épisode {e} absent des fiches du run source")
            traj[rs] = empreinte_trajectoire(episodes_h[e]) == fiches[e]["trajectoire"]
            if not traj[rs].all() and conforme[rs].all():
                # P3 accepte tout jeton de `fmt.fins` comme fin d'action ; le texte ne dit pas lequel. On essaie, dans un
                # ordre fixe, une puis deux substitutions du jeton de fin ; l'empreinte de P3 tranche (aucun choix libre)
                x0 = lignes[rs[0]]
                env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
                trouve = resoudre_fins(fmt, env, T, [lignes[r] for r in rs], [jetons[r] for r in rs],
                                       [jetons_notes[r] for r in rs], fiches[e]["trajectoire"], e)
                if trouve is not None:
                    recs[e], episodes_h[e] = trouve
                    traj[rs] = True
                    fins_resolues += 1
    etat["episodes_fin_resolue"] = fins_resolues
    etat["trajectoires_identiques"] = int(traj.sum()) // T if fiches is not None else None
    if fiches is not None:
        # CLC-03 : un épisode dont toutes les actions sont conformes en longueur doit avoir la trajectoire de P3 ; sinon
        # la divergence n'est pas expliquée par la tokenisation (gabarit, date, consigne, jeton de fin) : arrêt
        inexpliques = [e for e, rs in par_episode.items() if conforme[rs].all() and not traj[rs].all()]
        etat["episodes_conformes_longueur"] = sum(1 for rs in par_episode.values() if conforme[rs].all())
        if inexpliques:
            raise GardeArret(f"{len(inexpliques)} épisode(s) entièrement conformes en longueur à trajectoire différente de "
                             f"celle de P3 ({inexpliques[:3]}) : reconstruction non fidèle, rien n'est versé")
    etat["conformes_longueur"] = int(conforme.sum())
    etat["contextes_conformes"] = int(contexte_conforme.sum())
    progres(etape="reconstruction", conformes=int(conforme.sum()), contextes_conformes=int(contexte_conforme.sum()),
            trajectoires_identiques=etat["trajectoires_identiques"], fins_resolues=etat["episodes_fin_resolue"], actions=n)
    # éligibles au contrôle de fidélité : trajectoire identique à celle de P3, octet pour octet (identifiants et empans,
    # empreinte stockée par P3), quand les fiches sont données ; sinon contexte conforme en longueur
    eligibles = (traj if fiches is not None else contexte_conforme) & (np.asarray(jetons_notes) > 0)
    echantillon = tirer_echantillon(identite, eligibles, int(config["n_fidelite_par_condition"]),
                                    generateur(manifeste["graines"]["fidelite"]))
    ep_echantillon = list(dict.fromkeys(lignes[r]["episode"] for r in echantillon))
    ordre = ep_echantillon + [e for e in par_episode if e not in set(ep_echantillon)]
    d = len(couches)
    largeur = None
    moyenne = maximum = hors_cout = None
    jetons_empan = np.zeros(n, dtype=np.int64)
    ecart = np.full(n, np.nan)
    tol = float(config["tolerance_fidelite"])
    source = np.asarray(identite["scores"], dtype=np.float64)
    tour_echantillon, verdict_echantillon, verdict_negatif, repli = len(ep_echantillon), None, None, False
    activ_ident = np.zeros(n, dtype=bool)
    with noyau(config["noyau_attention"]):
        for k_ep, e in enumerate(ordre):
            exiger_sans_signal(f"rejeu, épisode {k_ep}")
            rs = par_episode[e]
            rec = recs.pop(e)
            acts = passe_unique(modele, rec["ids"], couches)
            if fiches is not None:
                from ..harnais.episode import empreinte_episode

                activ_ident[rs] = empreinte_episode(episodes_h[e], {0: acts})["activations"] == fiches[e]["activations"]
            if largeur is None:
                largeur = acts[couches[0]].shape[1]
                moyenne = np.full((n, d, largeur), np.nan, dtype=np.float16)
                maximum = np.full((n, d, largeur), np.nan, dtype=np.float16)
                hors_cout = np.full((n, d, largeur), np.nan, dtype=np.float16)
            for r, a in zip(rs, rec["actions"]):
                jetons_empan[r] = a["fin"] - a["debut"]
                if a["fin"] <= a["debut"]:
                    continue
                for j, c in enumerate(couches):
                    maximum[r, j] = _f16(agreger(acts[c], a["debut"], a["fin"], "max"), f"maximum, ligne {r}")
                    moyenne[r, j] = _f16(moyenne_diagnostic_n026(acts[c], a["debut"], a["fin"]), f"moyenne, ligne {r}")
                    hc = bornes_hors_cout(a["bornes"], a["fin"] - a["debut"])
                    if hc is None:
                        hors_cout[r, j] = maximum[r, j]
                    else:
                        garde = [p for p in range(a["debut"], a["fin"]) if not (hc[0] <= p - a["debut"] < hc[1])]
                        if garde:
                            hors_cout[r, j] = _f16(acts[c][garde].max(axis=0), f"hors coût, ligne {r}")
                seg = {c: acts[c][a["debut"]:a["fin"]] for c in notation.couches}
                if np.all(np.isfinite(source[r, [index[m] for m in noms]])):
                    ecart[r] = ecart_relatif(notation.noter(seg), source[r], noms, index)
            if k_ep + 1 == tour_echantillon:
                fautes = [r for r in echantillon if not (conforme[r] and np.isfinite(ecart[r]) and ecart[r] <= tol)]
                verdict_echantillon = {"rangs": echantillon, "ecarts": [float(ecart[r]) for r in echantillon],
                                       "conformes": [bool(conforme[r]) for r in echantillon], "fautes": fautes,
                                       "tolerance": tol, "lecture": "conforme" if not fautes else "contraire"}
                etat["fidelite_echantillon"] = verdict_echantillon
                progres(etape="fidelite", lecture=verdict_echantillon["lecture"], fautes=len(fautes),
                        ecart_max=f"{np.nanmax([ecart[r] for r in echantillon]):.3e}")
                if fautes:
                    raise GardeArret(f"contrôle de fidélité contraire sur {len(fautes)} action(s) de l'échantillon "
                                     f"({fautes[:5]}) : le rejeu n'est pas le calcul de P3, rien n'est versé")
                verdict_negatif = controle_negatif(modele, fmt, notation, noms, index, source, echantillon, lignes,
                                                   par_episode, taches, consignes, guide, T, couches, jetons,
                                                   jetons_notes, tol, int(config["controle_negatif_min"]))
                etat["controle_negatif"] = verdict_negatif
                progres(etape="controle_negatif", lecture=verdict_negatif["lecture"],
                        hors_tolerance=f"{verdict_negatif['hors_tolerance']}/{len(echantillon)}")
                # CLC-01 (b) : non discriminant → pas d'arrêt ; règle de repli gelée appliquée plus bas (fidèle restreint
                # aux trajectoires identiques, ou au contexte exact sans fiches), lecture en réserve
                repli = verdict_negatif["lecture"] != "discriminant"
            if (k_ep + 1) % 20 == 0:
                progres(etape="rejeu", episodes=f"{k_ep + 1}/{len(ordre)}")
    notees = np.isfinite(ecart)
    # fidèle : action notée, conforme en longueur, scores des sondes génériques à la tolérance ; le contexte non conforme
    # (une action précédente non conforme) est signalé à part (`contexte_conforme`), l'écart des scores dit s'il compte
    fidele = notees & conforme & (np.nan_to_num(ecart, nan=np.inf) <= tol)
    if repli:
        fidele &= traj if fiches is not None else contexte_conforme
    etat["etape"] = "écriture"
    dossier = racine / "donnees" / run_id
    dossier.mkdir(parents=True, exist_ok=False)
    ident = {k: np.asarray(identite[k]) for k in CLES_IDENTITE}
    # n° 330 : `jetons_empan` = `jetons_notes` de P3 (empan noté par P3) ; la longueur reconstruite est à part
    commun = {**ident, "jetons_empan": np.asarray(identite["jetons_notes"], dtype=np.int64),
              "jetons_empan_rejeu": jetons_empan, "couches": np.array(couches, dtype=np.int64),
              "conforme_longueur": conforme, "contexte_conforme": contexte_conforme, "ecart_fidelite": ecart, "fidele": fidele,
              "trajectoire_identique": traj, "activations_identiques": activ_ident}
    fichiers = {}
    nom = config["nom_sortie"]
    # format déterministe (CLR-12, n° 330) : le fichier principal porte `moyenne` (obligatoire pour conv-audit, bras de
    # diagnostic N-026) et l'identité (≈ 59 Mo) ; `maximum` (facultatif pour conv-audit, agrégat de production) dans un
    # second fichier aux mêmes clés d'identité ; tous deux sous la limite de poussée
    for p, tableaux in ((dossier / f"{nom}.npz", {"moyenne": moyenne}), (dossier / f"{nom}-maximum.npz", {"maximum": maximum})):
        with open(p, "wb") as f:
            np.savez_compressed(f, **tableaux, **commun)
        fichiers[p.name] = sceller(p)
    p = dossier / f"{nom}-complement-hors-cout.npz"
    with open(p, "wb") as f:
        np.savez_compressed(f, maximum_hors_cout=hors_cout, **commun)
    fichiers[p.name] = sceller(p)
    trop_lourds = {n: (dossier / n).stat().st_size for n in fichiers if (dossier / n).stat().st_size > 95_000_000}
    resultat = {"fichiers_au_dessus_de_95_mo": trop_lourds, "verdict_fidelite": "conforme", "regle_repli_appliquee": bool(repli),
                "lecture": "réserve (repli : fidèle restreint aux trajectoires identiques)" if repli else "principale",
                "textes_sha256": verifier(config["chemin_textes"]),
                "fichiers": fichiers, "identite_sha256": etat["identite_sha256"], "regle_empan": REGLE_EMPAN,
                "contexte": CONTEXTE, "couches": couches, "agregats": {"maximum": "production (harnais)",
                                                                       "moyenne": "diagnostic seulement (N-026)",
                                                                       "maximum_hors_cout": "contrôle, hors champ COST"},
                "fidelite_echantillon": verdict_echantillon, "controle_negatif": verdict_negatif,
                "empreintes_p3": None if fiches is None else {
                    "episodes": len(par_episode), "trajectoires_identiques": etat["trajectoires_identiques"],
                    "activations_identiques_au_bit": int(activ_ident.sum()) // T},
                "fidelite_toutes": {"notees": int(notees.sum()), "fideles": int(fidele.sum()),
                                    "conformes_longueur": int(conforme.sum()),
                                    "contextes_conformes": int(contexte_conforme.sum()), "actions": n,
                                    "fideles_parmi_contextes_conformes": int((fidele & contexte_conforme).sum()),
                                    "notees_contextes_conformes": int((notees & contexte_conforme).sum()),
                                    "egalite_exacte": int((ecart == 0).sum()),
                                    "ecart_max": float(np.nanmax(ecart)) if notees.any() else None,
                                    "ecart_mediane": float(np.nanmedian(ecart)) if notees.any() else None},
                "sondes_fidelite": noms, "sondes_legeres_sha256": sha_sondes, "reglages": reglages,
                "modele": config["agent"], "empreintes_modele": _empreintes_modele(config),
                "duree_s": round(time.perf_counter() - debut, 1)}
    ecrire_resultat(racine, chemin_m, "rejeu-activations", resultat)
    progres(etape="fin", fideles=int(fidele.sum()), notees=int(notees.sum()))
    return resultat


def _empreintes_modele(config: dict):
    if config["mode"] != "reel":
        return None
    from ..harnais.modeles import empreintes_fichiers_modele

    try:
        return empreintes_fichiers_modele(config["agent"]["modele"], config["agent"]["revision"])
    except Exception as e:          # descriptif seulement ; l'échec est consigné tel quel, jamais remplacé
        return {"non_lues": motif_d_arret(e)}


def progres(**champs) -> None:
    from datetime import datetime, timezone

    instant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + instant + " " + " ".join(f"{k}={v}" for k, v in champs.items()), file=sys.stderr, flush=True)


def config_pour_run(config: dict, racine: Path, run_source: str) -> dict:
    """Configuration complétée pour un run source dont les empreintes ne sont connues qu'après coup (R4) : chemins sous
    `donnees/<run>/`, empreintes lues dans le résumé et les sondes figées du run (scellés)."""
    c = dict(config)
    c["run_source"] = run_source
    d = Path("donnees") / run_source
    resume = json.loads((Path(racine) / "diag" / run_source / "resume.json").read_text(encoding="utf-8"))["resultat"]
    verifier(Path(racine) / "diag" / run_source / "resume.json")
    sf = json.loads((Path(racine) / "diag" / run_source / "sondes-figees.json").read_text(encoding="utf-8"))["resultat"]
    c.update({"chemin_textes": str(d / "textes-actions-p3.jsonl"), "textes_sha256": resume["textes_sha256"],
              "chemin_scores": str(d / "scores-p3.npz"), "scores_sha256": resume["scores_sha256"],
              "chemin_sondes_legeres": str(d / "sondes-figees-legeres.npz"),
              "sondes_legeres_sha256": sf["sondes_legeres_sha256"], "taches_sha256": resume["taches_sha256"],
              "consignes_sha256": resume["consignes_sha256"],
              "chemin_fiches": str(Path("diag") / run_source / "episodes-p3.json"),
              "fiches_sha256": verifier(Path(racine) / "diag" / run_source / "episodes-p3.json")})
    return c


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--run-source", default=None, help="run source dont les empreintes se lisent dans son résumé (R4)")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    citee = empreinte_config(config)
    if a.run_source:
        config = config_pour_run(config, Path("."), a.run_source)
    resultat = executer(config, Path("."), a.run_id, a.prereg, empreinte_citee=citee)
    print(json.dumps({"fichiers": resultat["fichiers"], "fidelite": resultat["fidelite_toutes"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
