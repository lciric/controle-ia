"""Blocs de la simulation de T0.3 (prereg/T0.3-simulation-lemme-theoreme-v1.md).

Chaque bloc renvoie des comptes bruts (alarmes, violations, écarts), sans aucune lecture :
la lecture gelée est dans `lecture.py`. Graines : une tâche nommée par usage (R9), dérivée de
l'entropie consignée ; nombres aléatoires communs au sein d'un groupe (mêmes épisodes honnêtes
pour toutes les attaques du groupe), ce qui rend exactes les vérifications trajectorielles.
"""
from __future__ import annotations

import math

import numpy as np

from ..agregateurs import (autocorrelation_lag1, balayage, balayage_multi, co_elevation,
                           correlation_inter_agents, detecteur_e, dispersion_agents, max_par_action,
                           page_cusum, somme_terminale, suites_wald_wolfowitz)
from ..agregateurs.processus_e import log_e_bilateral, log_e_unilateral, trajectoire_e
from ..gardes import GardeArret
from ..manifeste import generateur
from . import attaques as att
from . import calibrage as cal
from . import lots as L
from .lois import facteur_variance_ar1, tirer

TOL_REL = 1e-9          # tolérance des vérifications trajectorielles (relative à n₀)
TOL_SEUIL = 1e-9        # écart au seuil en deçà duquel une alarme est « à égalité » (exclue)


class Contexte:
    """Grille, graines du manifeste, seuils et ρ ; aucun état caché."""

    def __init__(self, grille: dict, graines: dict, suffixe: str = "", facteur_R: int = 1):
        self.grille = grille
        self.graines = graines
        self.alpha = float(grille["alpha"])
        self.suffixe = suffixe
        self.facteur_R = int(facteur_R)
        self.seuils: dict[str, dict[str, float]] = {}
        self.rho: dict[int, dict[str, float]] = {}

    def rng(self, tache: str) -> np.random.Generator:
        nom = tache + self.suffixe
        if nom not in self.graines:
            raise GardeArret(f"tâche {nom!r} absente du manifeste (R9)")
        return generateur(self.graines[nom])

    def R(self, cle: str) -> int:
        return int(self.grille["tailles"][cle]) * self.facteur_R

    def rho_de(self, n0: int, cote: str = "unilateral") -> float:
        if n0 not in self.rho:
            self.rho[n0] = {c: cal.rho_optimal(n0, self.alpha, c)[0] for c in ("unilateral", "bilateral")}
        return self.rho[n0][cote]

    def seuil(self, cfg: str, alarme: str) -> float:
        try:
            return self.seuils[cfg][alarme]
        except KeyError:
            raise GardeArret(f"seuil {alarme!r} non calibré pour {cfg!r}") from None


def morceaux(R: int, n0: int):
    taille = max(500, min(R, 4_000_000 // max(n0, 1)))
    fait = 0
    while fait < R:
        r = min(taille, R - fait)
        yield r
        fait += r


def nom_statistique(alarme: str) -> str:
    for suffixe in ("_ville", "_cal"):
        if alarme.endswith(suffixe):
            return alarme[: -len(suffixe)]
    return alarme


def calculer(Xb, statistiques, ctx: Contexte, mus=None) -> dict[str, np.ndarray]:
    """Valeurs des statistiques demandées sur un lot (R, N, T) déjà standardisé."""
    Xb = L.verifier_lot(Xb)
    R, N, T = Xb.shape
    n0 = N * T
    out = {}
    serie_u = None
    for s in dict.fromkeys(statistiques):
        if s == "somme":
            out[s] = L.lot_somme(Xb)
        elif s == "somme_bilat":
            out[s] = np.abs(L.lot_somme(Xb))
        elif s == "max":
            out[s] = L.lot_max(Xb)
        elif s.startswith("glissante_"):
            out[s] = L.lot_glissante(Xb, int(s.split("_")[1]))
        elif s == "balayage_multi":
            out[s] = L.lot_balayage_multi(Xb)
        elif s == "page":
            out[s] = L.lot_page(Xb, 0.5)
        elif s == "detecteur_e":
            out[s] = L.lot_detecteur_e(Xb)
        elif s == "e_unilat":
            if serie_u is None:
                serie_u = L.serie_e(L.ordre(Xb), ctx.rho_de(n0, "unilateral"), "unilateral")
            out[s] = serie_u.max(axis=1)
        elif s == "e_bilat":
            out[s] = L.lot_e_max(Xb, ctx.rho_de(n0, "bilateral"), "bilateral")
        elif s == "e_terminal":
            out[s] = L.lot_e_terminal(Xb, ctx.rho_de(n0, "unilateral"))
        elif s.startswith("co_elevation_"):
            m = s.split("_")[2]
            out[s] = L.lot_co_elevation(Xb, N if m == "N" else int(m))
        elif s == "autocorr":
            out[s] = L.lot_autocorr(Xb)
        elif s == "autocorr_abs":
            out[s] = L.lot_autocorr(Xb, absolue=True)
        elif s == "suites":
            out[s] = L.lot_suites(Xb)
        elif s == "correlation_agents":
            out[s] = L.lot_correlation_agents(Xb)
        elif s == "dispersion_agents":
            out[s] = L.lot_dispersion_agents(Xb, mus)
        else:
            raise GardeArret(f"statistique {s!r} inconnue")
    return out


def alarmes(valeurs: dict, liste, ctx: Contexte, cfg: str) -> dict[str, np.ndarray]:
    return {a: valeurs[nom_statistique(a)] >= ctx.seuil(cfg, a) for a in liste}


def exiger_multiensemble(a, b, quoi: str, axe: int = 1) -> None:
    """Garde : un arrangement de classe C préserve exactement le multi-ensemble de chaque épisode."""
    if not np.array_equal(np.sort(a, axis=axe), np.sort(b, axis=axe)):
        raise GardeArret(f"{quoi} : multi-ensemble non préservé (liste d'arrêt)")


def _std(Xb, sigma_utilise: float = 1.0):
    return Xb / sigma_utilise if sigma_utilise != 1.0 else Xb


# ---------------------------------------------------------------------------------------------
# Calibrage sous P₀, taux effectifs, gardes d'équivalence
# ---------------------------------------------------------------------------------------------
def seuils_exacts(spec: dict, alpha: float, alarme: str, n0: int) -> float:
    loi = spec["loi"]
    facteur = facteur_variance_ar1(float(loi["phi"]), int(loi["T"])) if loi["type"] == "ar1" else 1.0
    if alarme == "somme":
        return cal.seuil_somme_exact(alpha, n0, facteur_variance=facteur)
    if alarme == "somme_bilat":
        return cal.seuil_somme_exact(alpha, n0, bilateral=True, facteur_variance=facteur)
    if alarme == "max" and facteur == 1.0:
        return cal.seuil_max_exact(alpha, n0)
    raise GardeArret(f"pas de seuil exact pour {alarme!r} sous {loi}")


def calibrer(ctx: Contexte, cfg: str) -> dict:
    """Seuils de la configuration cfg, puis taux effectif de chaque alarme sous P₀ (échantillon
    indépendant). Renvoie les comptes bruts ; les gardes sont appliquées par l'appelant."""
    spec = ctx.grille["configs"][cfg]
    loi, liste = spec["loi"], spec["alarmes"]
    N, T = int(loi["N"]), int(loi["T"])
    n0 = N * T
    exacts = set(spec.get("exacts", []))
    mus = loi.get("mus")
    a_calibrer = [a for a in liste if not a.endswith("_ville") and a not in exacts]
    seuils = {}
    for a in liste:
        if a.endswith("_ville"):
            seuils[a] = cal.seuil_ville(ctx.alpha)
        elif a in exacts:
            seuils[a] = seuils_exacts(spec, ctx.alpha, a, n0)
    if a_calibrer:
        stats_cal = sorted({nom_statistique(a) for a in a_calibrer})
        g = ctx.rng(f"calib/{cfg}")
        valeurs = {s: [] for s in stats_cal}
        for r in morceaux(ctx.R("R_cal"), n0):
            v = calculer(tirer(g, r, loi), stats_cal, ctx, mus)
            for s in stats_cal:
                valeurs[s].append(v[s])
        for a in a_calibrer:
            seuils[a] = cal.seuil_mc(np.concatenate(valeurs[nom_statistique(a)]), ctx.alpha)
    non_finis = sorted(a for a, t in seuils.items() if not math.isfinite(t))
    if non_finis:
        raise GardeArret(f"{cfg} : seuils non finis {non_finis} (liste d'arrêt)")
    ctx.seuils[cfg] = seuils
    g0 = ctx.rng(f"p0/{cfg}")
    comptes = {a: 0 for a in liste}
    R0 = 0
    for r in morceaux(ctx.R("R0"), n0):
        al = alarmes(calculer(tirer(g0, r, loi), [nom_statistique(a) for a in liste], ctx, mus), liste, ctx, cfg)
        for a in liste:
            comptes[a] += int(al[a].sum())
        R0 += r
    genres = {a: ("ville" if a.endswith("_ville") else "exact" if a in exacts else
                  "mc_discret" if nom_statistique(a) == "suites" else "mc") for a in liste}
    return {"cfg": cfg, "loi": loi, "n0": n0, "seuils": seuils, "genres": genres, "R_cal": ctx.R("R_cal"),
            "R0": R0, "alarmes_p0": comptes, "garde": bool(spec.get("garde", False)),
            "garde_exclus": list(spec.get("garde_exclus", [])), "rho": ctx.rho.get(n0)}


def garde_p0(res: dict, alpha: float, z: float) -> list[str]:
    """Gardes de calibrage (liste d'arrêt) : renvoie les manquements, vide si tout va bien."""
    if not res["garde"]:
        return []
    manques = []
    R0, Rc = res["R0"], res["R_cal"]
    v = alpha * (1 - alpha)
    for a, k in res["alarmes_p0"].items():
        if a in res.get("garde_exclus", []):
            continue
        p = k / R0
        genre = res["genres"][a]
        if genre == "exact" and abs(p - alpha) > z * math.sqrt(v / R0):
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f} ≠ α (seuil exact)")
        elif genre == "mc" and abs(p - alpha) > z * math.sqrt(v / R0 + v / Rc):
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f} ≠ α (seuil Monte-Carlo)")
        elif genre == "mc_discret" and p > alpha + z * math.sqrt(v / R0 + v / Rc):
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f} > α (seuil Monte-Carlo, statistique discrète)")
        elif genre == "ville" and p > alpha + z * math.sqrt(v / R0):
            manques.append(f"{res['cfg']}/{a} : taux sous P₀ {p:.4f} > α (Ville)")
    return manques


REFERENCES = {
    "somme": lambda X, ctx: somme_terminale(X),
    "somme_bilat": lambda X, ctx: abs(somme_terminale(X)),
    "max": lambda X, ctx: max_par_action(X),
    "glissante_5": lambda X, ctx: balayage(X, 5),
    "glissante_10": lambda X, ctx: balayage(X, 10),
    "balayage_multi": lambda X, ctx: balayage_multi(X),
    "page": lambda X, ctx: page_cusum(X, 0.5),
    "detecteur_e": lambda X, ctx: detecteur_e(X),
    "e_unilat": lambda X, ctx: float(np.max(trajectoire_e(X, 0.0, 1.0, ctx.rho_de(X.size), "unilateral"))),
    "e_bilat": lambda X, ctx: float(np.max(trajectoire_e(X, 0.0, 1.0, ctx.rho_de(X.size, "bilateral"), "bilateral"))),
    "e_terminal": lambda X, ctx: float(log_e_unilateral(somme_terminale(X), float(X.size), 1.0, ctx.rho_de(X.size))),
    "co_elevation_2": lambda X, ctx: co_elevation(X, 2),
    "co_elevation_3": lambda X, ctx: co_elevation(X, 3),
    "co_elevation_N": lambda X, ctx: co_elevation(X, X.shape[0]),
    "autocorr": lambda X, ctx: autocorrelation_lag1(X),
    "autocorr_abs": lambda X, ctx: autocorrelation_lag1(X, absolue=True),
    "suites": lambda X, ctx: suites_wald_wolfowitz(X),
    "correlation_agents": lambda X, ctx: correlation_inter_agents(X),
}


def equivalence(ctx: Contexte, cfg: str, n_episodes: int) -> dict:
    """Garde : statistiques vectorisées = références scalaires de `agregateurs`, épisode par épisode."""
    spec = ctx.grille["configs"][cfg]
    loi = spec["loi"]
    mus = loi.get("mus")
    stats = sorted({nom_statistique(a) for a in spec["alarmes"]})
    Xb = tirer(ctx.rng(f"equivalence/{cfg}"), n_episodes, loi)
    v = calculer(Xb, stats, ctx, mus)
    ecarts = {}
    for s in stats:
        if s == "dispersion_agents":
            ref = np.array([dispersion_agents(Xb[i], mus) for i in range(n_episodes)])
        else:
            ref = np.array([REFERENCES[s](Xb[i], ctx) for i in range(n_episodes)])
        ecarts[s] = float(np.max(np.abs(ref - v[s]) / np.maximum(1.0, np.abs(ref))))
    return {"cfg": cfg, "n_episodes": n_episodes, "ecart_relatif_max": ecarts}


# ---------------------------------------------------------------------------------------------
# P1 — lemme d'additivité (classe M)
# ---------------------------------------------------------------------------------------------
def _loi_gauss(N, T):
    return {"type": "iid", "marginale": "gauss", "N": N, "T": T}


def bloc_P1a(ctx: Contexte) -> dict:
    g = ctx.grille["P1a"]
    sortie = []
    for N, T in g["configs"]:
        n0, cfg = N * T, f"gauss_{N}x{T}"
        rho = ctx.rho_de(n0)
        h, c_s, c_m = cal.seuil_ville(ctx.alpha), ctx.seuil(cfg, "somme"), ctx.seuil(cfg, "max")
        for B in g["B"]:
            base = f"P1a/{N}x{T}/B{B}"
            gY = ctx.rng(f"{base}/Y")
            cellules = []
            for schema in g["schemas"]:
                if N == 1 and schema in ("un_agent", "reparti"):
                    continue
                for m in g["m"]:
                    if m > n0 or (schema == "un_agent" and m > T):
                        continue
                    for genre in (["egaux", "dirichlet"] if schema == "aleatoire" else ["egaux"]):
                        cellules.append({"schema": schema, "m": m, "genre": genre,
                                         "rng": ctx.rng(f"{base}/{schema}/m{m}/{genre}"),
                                         "R": 0, "disc_somme": 0, "disc_eterm": 0, "ecart_max": 0.0,
                                         "alarmes_somme": 0, "alarmes_eterm": 0, "alarmes_max": 0,
                                         "alarmes_e_unilat": 0})
            Rtot = ref_s = ref_e = egal_s = egal_e = 0
            for r in morceaux(ctx.R("R"), n0):
                Y = tirer(gY, r, _loi_gauss(N, T))
                y = L.ordre(Y)
                SY = L.lot_somme(Y) + B
                lY = log_e_unilateral(SY, float(n0), 1.0, rho)
                aS, aE = SY >= c_s, lY >= h
                tS, tE = np.abs(SY - c_s) <= TOL_SEUIL * n0, np.abs(lY - h) <= TOL_SEUIL
                Rtot += r
                ref_s += int(aS.sum())
                ref_e += int(aE.sum())
                egal_s += int(tS.sum())
                egal_e += int(tE.sum())
                for c in cellules:
                    P = att.positions(c["schema"], c["m"], N, T, r, c["rng"], y)
                    d = att.decalages(c["genre"], c["m"], B, r, c["rng"])
                    X = L.depuis_ordre(att.appliquer_decalages(y, P, d), N, T)
                    v = calculer(X, ["somme", "e_terminal", "max", "e_unilat"], ctx)
                    c["R"] += r
                    c["ecart_max"] = max(c["ecart_max"], float(np.max(np.abs(v["somme"] - SY))))
                    xs, xe = v["somme"] >= c_s, v["e_terminal"] >= h
                    c["disc_somme"] += int(((xs != aS) & ~tS).sum())
                    c["disc_eterm"] += int(((xe != aE) & ~tE).sum())
                    c["alarmes_somme"] += int(xs.sum())
                    c["alarmes_eterm"] += int(xe.sum())
                    c["alarmes_max"] += int((v["max"] >= c_m).sum())
                    c["alarmes_e_unilat"] += int((v["e_unilat"] >= h).sum())
            for c in cellules:
                del c["rng"]
            sortie.append({"N": N, "T": T, "n0": n0, "B": B, "R": Rtot, "alarmes_ref_somme": ref_s,
                           "alarmes_ref_eterm": ref_e, "egalites_somme": egal_s, "egalites_eterm": egal_e,
                           "tolerance_ecart": TOL_REL * n0, "cellules": cellules})
    return {"groupes": sortie}


def bloc_P1b(ctx: Contexte) -> dict:
    g = ctx.grille["P1b"]
    sortie = []
    for N, T in g["configs"]:
        n0, cfg = N * T, f"gauss_{N}x{T}"
        c_s = ctx.seuil(cfg, "somme")
        for B in g["B"]:
            base = f"P1b/{N}x{T}/B{B}"
            gY, gP = ctx.rng(f"{base}/Y"), ctx.rng(f"{base}/positions")
            R = k = 0
            for r in morceaux(ctx.R("R"), n0):
                y = L.ordre(tirer(gY, r, _loi_gauss(N, T)))
                P = att.positions("aleatoire", g["m"], N, T, r, gP)
                x = att.appliquer_decalages(y, P, att.decalages("egaux", g["m"], B, r, gP))
                k += int((L.lot_somme(L.depuis_ordre(x, N, T)) >= c_s).sum())
                R += r
            sortie.append({"N": N, "T": T, "n0": n0, "B": B, "m": g["m"], "R": R, "alarmes_somme": k})
    return {"cellules": sortie}


# ---------------------------------------------------------------------------------------------
# P2 — effondrement du max
# ---------------------------------------------------------------------------------------------
def bloc_P2(ctx: Contexte) -> dict:
    g = ctx.grille["P2"]
    N, T = g["config"]
    n0, cfg = N * T, f"gauss_{N}x{T}"
    c_m, c_s = ctx.seuil(cfg, "max"), ctx.seuil(cfg, "somme")
    sortie = []
    for B in g["B"]:
        for m in g["m"]:
            base = f"P2/B{B}/m{m}"
            gY, gP = ctx.rng(f"{base}/Y"), ctx.rng(f"{base}/positions")
            R = km = ks = 0
            for r in morceaux(ctx.R("R_P2"), n0):
                y = L.ordre(tirer(gY, r, _loi_gauss(N, T)))
                P = att.positions("aleatoire", m, N, T, r, gP)
                X = L.depuis_ordre(att.appliquer_decalages(y, P, att.decalages("egaux", m, B, r, gP)), N, T)
                km += int((L.lot_max(X) >= c_m).sum())
                ks += int((L.lot_somme(X) >= c_s).sum())
                R += r
            sortie.append({"B": B, "m": m, "n0": n0, "R": R, "alarmes_max": km, "alarmes_somme": ks})
    return {"cfg": cfg, "cellules": sortie, "seuil_max": c_m}


# ---------------------------------------------------------------------------------------------
# P3 — lecture toujours valide : calendrier, borne terminale, détection à temps
# ---------------------------------------------------------------------------------------------
def bloc_P3(ctx: Contexte) -> dict:
    g = ctx.grille["P3"]
    h = cal.seuil_ville(ctx.alpha)
    sortie = []
    ordre_calendriers = g["calendriers"]      # du plus avancé au plus reporté, aléatoire à part
    for N, T in g["configs"]:
        n0 = N * T
        rho = ctx.rho_de(n0)
        for B in g["B"]:
            base = f"P3/{N}x{T}/B{B}"
            gY = ctx.rng(f"{base}/Y")
            gen = {(m, s): ctx.rng(f"{base}/m{m}/{s}") for m in g["m"] for s in ordre_calendriers}
            res = {(m, s): {"alarmes": 0, "premiere_somme": 0} for m in g["m"] for s in ordre_calendriers}
            viol = {m: {"debut>uniforme": 0, "uniforme>fin": 0, "debut>aleatoire": 0, "aleatoire>fin": 0,
                        "fin>terminal": 0} for m in g["m"]}
            R = kt = 0
            for r in morceaux(ctx.R("R"), n0):
                y = L.ordre(tirer(gY, r, _loi_gauss(N, T)))
                ST = np.sort(y, axis=1).sum(axis=1) + B
                lt = log_e_unilateral(ST, float(n0), 1.0, rho)
                at, tt = lt >= h, np.abs(lt - h) <= TOL_SEUIL
                kt += int(at.sum())
                R += r
                for m in g["m"]:
                    al, eg = {}, {}
                    for s in ordre_calendriers:
                        P = att.positions(s, m, N, T, r, gen[(m, s)])
                        x = att.appliquer_decalages(y, P, att.decalages("egaux", m, B, r, gen[(m, s)]))
                        le = L.serie_e(x, rho, "unilateral")
                        mx = le.max(axis=1)
                        al[s], eg[s] = mx >= h, np.abs(mx - h) <= TOL_SEUIL
                        res[(m, s)]["alarmes"] += int(al[s].sum())
                        f = L.premiere_alarme(le, h)
                        res[(m, s)]["premiere_somme"] += int(f[f >= 0].sum())
                    for cle, (a, b) in {"debut>uniforme": ("debut", "uniforme"), "uniforme>fin": ("uniforme", "fin"),
                                        "debut>aleatoire": ("debut", "aleatoire"),
                                        "aleatoire>fin": ("aleatoire", "fin")}.items():
                        viol[m][cle] += int((al[b] & ~al[a] & ~eg[a] & ~eg[b]).sum())
                    viol[m]["fin>terminal"] += int((at & ~al["fin"] & ~tt & ~eg["fin"]).sum())
            sortie.append({"N": N, "T": T, "n0": n0, "B": B, "R": R, "rho": rho, "alarmes_terminal": kt,
                           "cellules": [{"m": m, "calendrier": s, **res[(m, s)]} for (m, s) in res],
                           "violations": {str(m): viol[m] for m in g["m"]}})
    return {"groupes": sortie}


def bloc_P34(ctx: Contexte) -> dict:
    g = ctx.grille["P34"]
    N, T = g["config"]
    if N != 1:
        raise GardeArret("P3.4 : N = 1 requis (datation de l'alarme sur l'axe du temps)")
    n0, cfg = T, f"gauss_1x{T}"
    rho = ctx.rho_de(n0)
    seuils = {a: ctx.seuil(cfg, a) for a in g["alarmes"]}
    sortie = []
    for B in g["B"]:
        for m in g["m"]:
            gY = ctx.rng(f"P34/B{B}/m{m}/Y")
            comptes = {a: {"a_temps": 0, "d_ici_n0": 0} for a in g["alarmes"]}
            R = 0
            for r in morceaux(ctx.R("R"), n0):
                y = L.ordre(tirer(gY, r, _loi_gauss(1, T)))
                P = att.positions("fin", m, 1, T, r, gY)
                x = att.appliquer_decalages(y, P, att.decalages("egaux", m, B, r, gY))
                series = {}
                for a in g["alarmes"]:
                    s = nom_statistique(a)
                    if s not in series:
                        series[s] = {"e_unilat": lambda: L.serie_e(x, rho, "unilateral"),
                                     "page": lambda: L.serie_page(x, 0.5),
                                     "detecteur_e": lambda: L.serie_detecteur_e(x),
                                     "glissante_10": lambda: L.serie_glissante(x, 10),
                                     "balayage_multi": lambda: L.serie_balayage_multi(x)}[s]()
                    f = L.premiere_alarme(series[s], seuils[a])
                    comptes[a]["a_temps"] += int(((f >= 0) & (f < n0 - 1)).sum())
                    comptes[a]["d_ici_n0"] += int((f >= 0).sum())
                R += r
            sortie.append({"B": B, "m": m, "n0": n0, "R": R, "comptes": comptes})
    return {"cfg": cfg, "cellules": sortie, "seuils": seuils}


# ---------------------------------------------------------------------------------------------
# P4 — T1 (invariance trajectorielle) et T2 (impossibilité sans structure)
# ---------------------------------------------------------------------------------------------
def _arranger(nom: str, y, rng, iterations: int):
    if nom == "tri_croissant":
        return att.tri_croissant(y)
    if nom.startswith("bloc_top_"):
        return att.bloc_top_r(y, int(nom.split("_")[2]), rng)[0]
    if nom.startswith("top_") and nom.endswith("_fin"):
        return att.top_r_a_la_fin(y, int(nom.split("_")[1]))
    if nom == "apparie_autocorr":
        x, debut = att.bloc_top_r(y, 5, rng)
        return att.apparier(x, debut, 5, "autocorr", rng, iterations)[0]
    raise GardeArret(f"arrangement {nom!r} inconnu")


def bloc_P4(ctx: Contexte) -> dict:
    g = ctx.grille["P4"]
    sortie = []
    for N, T in g["configs"]:
        n0, cfg = N * T, f"gauss_{N}x{T}"
        liste = ctx.grille["configs"][cfg]["alarmes"]
        sym = ["somme", "max", "e_terminal"]
        arr_T1 = [a for a in g["arrangements_T1"] if N == 1 or a != "apparie_autocorr"]
        gY = ctx.rng(f"P4/{N}x{T}/Y")
        gA = {a: ctx.rng(f"P4/{N}x{T}/{a}") for a in arr_T1}
        gR = {a: ctx.rng(f"P4/{N}x{T}/{a}/rebrassage") for a in g["arrangements_T2"]}
        t1 = {a: {"valeurs_differentes": {s: 0 for s in sym}, "discordances": {s: 0 for s in sym}} for a in arr_T1}
        t2 = {a: {al: 0 for al in liste} for a in g["arrangements_T2"]}
        R = 0
        for r in morceaux(ctx.R("R"), n0):
            Y = tirer(gY, r, _loi_gauss(N, T))
            y = L.ordre(Y)
            vY = calculer(Y, sym, ctx)
            aY = alarmes(vY, sym[:2], ctx, cfg)
            aY["e_terminal"] = vY["e_terminal"] >= cal.seuil_ville(ctx.alpha)
            for a in arr_T1:
                X = L.depuis_ordre(_arranger(a, y, gA[a], g["iterations_appariement"]), N, T)
                exiger_multiensemble(L.ordre(X), y, f"P4 : arrangement {a}")
                vX = calculer(X, sym, ctx)
                aX = alarmes(vX, sym[:2], ctx, cfg)
                aX["e_terminal"] = vX["e_terminal"] >= cal.seuil_ville(ctx.alpha)
                for s in sym:
                    t1[a]["valeurs_differentes"][s] += int(np.count_nonzero(vX[s] != vY[s]))
                    t1[a]["discordances"][s] += int(np.count_nonzero(aX[s] != aY[s]))
                if a in g["arrangements_T2"]:
                    X2 = L.depuis_ordre(att.rebrassage(L.ordre(X), gR[a]), N, T)
                    exiger_multiensemble(L.ordre(X2), y, f"P4 : rebrassage de {a}")
                    al = alarmes(calculer(X2, [nom_statistique(x) for x in liste], ctx), liste, ctx, cfg)
                    for x in liste:
                        t2[a][x] += int(al[x].sum())
            R += r
        sortie.append({"N": N, "T": T, "n0": n0, "R": R, "T1": t1, "T2": t2})
    return {"configs": sortie}


def bloc_P43(ctx: Contexte) -> dict:
    g = ctx.grille["P43"]
    cfg = g["config"]
    loi = ctx.grille["configs"][cfg]["loi"]
    N, T = int(loi["N"]), int(loi["T"])
    gY, gT, gI = ctx.rng("P43/Y"), ctx.rng("P43/rebrassage_total"), ctx.rng("P43/rebrassage_intra_agent")
    c = ctx.seuil(cfg, "dispersion_agents")
    R = kt = ki = 0
    for r in morceaux(ctx.R("R"), N * T):
        Y = tirer(gY, r, loi)
        Xt = L.depuis_ordre(att.rebrassage(L.ordre(Y), gT), N, T)
        Xi = att.rebrassage_intra_agent(Y, gI)
        exiger_multiensemble(L.ordre(Xt), L.ordre(Y), "P4.3 : rebrassage total")
        exiger_multiensemble(Xi, Y, "P4.3 : rebrassage intra-agent", axe=2)
        kt += int((L.lot_dispersion_agents(Xt, loi["mus"]) >= c).sum())
        ki += int((L.lot_dispersion_agents(Xi, loi["mus"]) >= c).sum())
        R += r
    return {"cfg": cfg, "R": R, "alarmes_total": kt, "alarmes_intra_agent": ki}


# ---------------------------------------------------------------------------------------------
# P5 — T3 : dommage structuré, garanties locales, attaquant adaptatif
# ---------------------------------------------------------------------------------------------
def bloc_P5_temps(ctx: Contexte) -> dict:
    g = ctx.grille["P5_temps"]
    N, T = 1, int(g["T"])
    n0, cfg = T, f"gauss_1x{T}"
    liste = g["alarmes"]
    c5 = ctx.seuil(cfg, "glissante_5")
    noms = [f"bloc_r{r}" for r in g["r"]] + ["apparie_autocorr", "apparie_suites"]
    gY = ctx.rng("P5/temps/Y")
    gA = {a: ctx.rng(f"P5/temps/{a}") for a in noms}
    res = {a: {"alarmes": {x: 0 for x in liste}, "viol_glissante": 0, "viol_page": 0, "borne_glissante": 0,
               "borne_sans_alarme": 0, "ecart_hors_tolerance": 0, "r": None} for a in noms}
    R = 0
    for r in morceaux(ctx.R("R"), n0):
        y = L.ordre(tirer(gY, r, _loi_gauss(N, T)))
        tri = np.sort(y, axis=1)
        arrs = {}
        for rr in g["r"]:
            arrs[f"bloc_r{rr}"] = (att.bloc_top_r(y, rr, gA[f"bloc_r{rr}"])[0], rr, None)
        for cible in ("autocorr", "suites"):
            a = f"apparie_{cible}"
            x0, debut = att.bloc_top_r(y, 5, gA[a])
            xa, ecart = att.apparier(x0, debut, 5, cible, gA[a], g["iterations_appariement"])
            if cible == "autocorr":
                Z = xa - xa.mean(axis=1, keepdims=True)
                hors = np.abs(ecart) / (Z * Z).sum(axis=1) > g["tolerance_autocorr"]
            else:
                hors = np.abs(ecart) > g["tolerance_suites"]
            arrs[a] = (xa, 5, hors)
        for a, (x, rr, hors) in arrs.items():
            exiger_multiensemble(x, tri, f"P5 : arrangement {a}")
            X = L.depuis_ordre(x, N, T)
            v = calculer(X, [nom_statistique(s) for s in liste], ctx)
            al = alarmes(v, liste, ctx, cfg)
            vr = tri[:, -rr]                       # r-ième plus haute valeur de l'épisode
            res[a]["r"] = rr
            for s in liste:
                res[a]["alarmes"][s] += int(al[s].sum())
            res[a]["viol_page"] += int((v["page"] < rr * (vr - 0.5) - TOL_REL * n0).sum())
            if rr >= 5:
                res[a]["viol_glissante"] += int((v["glissante_5"] < 5 * vr - TOL_REL * n0).sum())
                borne = 5 * vr >= c5
                res[a]["borne_glissante"] += int(borne.sum())
                res[a]["borne_sans_alarme"] += int((borne & ~al["glissante_5"]).sum())
            if hors is not None:
                res[a]["ecart_hors_tolerance"] += int(hors.sum())
        R += r
    return {"cfg": cfg, "R": R, "n0": n0, "arrangements": res}


def bloc_P5_agents(ctx: Contexte) -> dict:
    g = ctx.grille["P5_agents"]
    N, T = g["config"]
    n0, cfg = N * T, f"gauss_{N}x{T}"
    liste = g["alarmes"]
    gY, gA = ctx.rng("P5/agents/Y"), ctx.rng("P5/agents/co_elevation_top")
    comptes = {x: 0 for x in liste}
    R = viol = 0
    for r in morceaux(ctx.R("R"), n0):
        Y = tirer(gY, r, _loi_gauss(N, T))
        X, _ = att.co_elevation_top(Y, g["mc"], gA)
        exiger_multiensemble(L.ordre(X), L.ordre(Y), "P5 : co-élévation")
        vr = np.sort(L.ordre(Y), axis=1)[:, -g["mc"]]
        v = calculer(X, [nom_statistique(s) for s in liste], ctx)
        al = alarmes(v, liste, ctx, cfg)
        for s in liste:
            comptes[s] += int(al[s].sum())
        viol += int((v[f"co_elevation_{g['mc']}"] < g["mc"] * vr - TOL_REL * n0).sum())
        R += r
    return {"cfg": cfg, "mc": g["mc"], "R": R, "n0": n0, "alarmes": comptes, "viol_co_elevation": viol}


# ---------------------------------------------------------------------------------------------
# P6 — classe K (copules)
# ---------------------------------------------------------------------------------------------
def _bloc_lois(ctx: Contexte, cellules: list[dict], tache: str) -> list[dict]:
    sortie = []
    for c in cellules:
        loi, cfg, liste = c["loi"], c["cfg"], c["alarmes"]
        N, T = int(loi["N"]), int(loi["T"])
        gX = ctx.rng(f"{tache}/{c['nom']}")
        comptes = {x: 0 for x in liste}
        R = 0
        for r in morceaux(ctx.R("R"), N * T):
            al = alarmes(calculer(tirer(gX, r, loi), [nom_statistique(s) for s in liste], ctx), liste, ctx, cfg)
            for s in liste:
                comptes[s] += int(al[s].sum())
            R += r
        sortie.append({"nom": c["nom"], "role": c["role"], "cfg": cfg, "loi": loi, "R": R, "alarmes": comptes})
    return sortie


def bloc_P6(ctx: Contexte) -> dict:
    return {"cellules": _bloc_lois(ctx, ctx.grille["P6"]["cellules"], "P6")}


# ---------------------------------------------------------------------------------------------
# P7 — T4 : somme séquentielle unilatérale sous arrangements dominés
# ---------------------------------------------------------------------------------------------
def bloc_P7(ctx: Contexte) -> dict:
    g = ctx.grille["P7"]
    N, T = 1, int(g["T"])
    n0, cfg = T, f"gauss_1x{T}"
    rho = ctx.rho_de(n0)
    h = cal.seuil_ville(ctx.alpha)
    liste = g["alarmes"]
    gY = ctx.rng("P7/Y")
    res = {a: {"alarmes": {x: 0 for x in liste}, "viol_inclusion_haute": 0, "viol_inclusion_basse": 0,
               "viol_sommes_partielles": 0} for a in g["arrangements"]}
    R = kY = 0
    for r in morceaux(ctx.R("R"), n0):
        y = L.ordre(tirer(gY, r, _loi_gauss(N, T)))
        SY = np.cumsum(y, axis=1)
        mY = L.serie_e(y, rho, "unilateral").max(axis=1)
        aY, tY = mY >= h, np.abs(mY - h) <= TOL_SEUIL
        lt = log_e_unilateral(np.sort(y, axis=1).sum(axis=1), float(n0), 1.0, rho)
        at, tt = lt >= h, np.abs(lt - h) <= TOL_SEUIL
        kY += int(aY.sum())
        for a in g["arrangements"]:
            x = _arranger(a, y, None, 0)
            exiger_multiensemble(x, y, f"P7 : arrangement {a}")
            v = calculer(L.depuis_ordre(x, N, T), [nom_statistique(s) for s in liste], ctx)
            al = alarmes(v, liste, ctx, cfg)
            for s in liste:
                res[a]["alarmes"][s] += int(al[s].sum())
            mX = v["e_unilat"]
            aX, tX = mX >= h, np.abs(mX - h) <= TOL_SEUIL
            res[a]["viol_inclusion_haute"] += int((aX & ~aY & ~tX & ~tY).sum())
            res[a]["viol_inclusion_basse"] += int((at & ~aX & ~tt & ~tX).sum())
            res[a]["viol_sommes_partielles"] += int((np.cumsum(x, axis=1) - SY > TOL_REL * n0).any(axis=1).sum())
        R += r
    return {"cfg": cfg, "R": R, "n0": n0, "rho": rho, "alarmes_honnete_e_unilat": kY, "arrangements": res}


# ---------------------------------------------------------------------------------------------
# P8 — validité hors hypothèses ; variante conforme par épisodes honnêtes entiers
# ---------------------------------------------------------------------------------------------
def bloc_P8(ctx: Contexte) -> dict:
    g = ctx.grille["P8"]
    sortie = []
    for s in g["reglages"]:
        loi, su = s["loi"], float(s.get("sigma_utilise", 1.0))
        N, T = int(loi["N"]), int(loi["T"])
        n0, cfg = N * T, f"gauss_{N}x{T}"
        liste = g["alarmes"]
        gX = ctx.rng(f"P8/{s['nom']}")
        comptes = {x: 0 for x in liste}
        R = 0
        for r in morceaux(ctx.R("R"), n0):
            X = _std(tirer(gX, r, loi), su)
            al = alarmes(calculer(X, [nom_statistique(x) for x in liste], ctx), liste, ctx, cfg)
            for x in liste:
                comptes[x] += int(al[x].sum())
            R += r
        conformes = {st: [] for st in g["conforme"]["statistiques"]}
        K, nt, Lc = int(g["conforme"]["K"]), int(g["conforme"]["n_test"]), int(g["conforme"]["L"])
        for l in range(Lc):
            gC = ctx.rng(f"P8/{s['nom']}/conforme/{l}")
            vc = calculer(_std(tirer(gC, K, loi), su), g["conforme"]["statistiques"], ctx)
            vt = calculer(_std(tirer(gC, nt, loi), su), g["conforme"]["statistiques"], ctx)
            for st in g["conforme"]["statistiques"]:
                conformes[st].append(int((vt[st] >= cal.seuil_conforme(vc[st], ctx.alpha)).sum()))
        sortie.append({"nom": s["nom"], "loi": loi, "sigma_utilise": su, "cfg": cfg, "R": R, "alarmes": comptes,
                       "conforme": {"K": K, "n_test": nt, "L": Lc, "alarmes_par_tirage": conformes,
                                    "taux_theorique": cal.taux_conforme(K, ctx.alpha)}})
    return {"reglages": sortie}


BLOCS = {"P1a": bloc_P1a, "P1b": bloc_P1b, "P2": bloc_P2, "P3": bloc_P3, "P34": bloc_P34, "P4": bloc_P4,
         "P43": bloc_P43, "P5_temps": bloc_P5_temps, "P5_agents": bloc_P5_agents, "P6": bloc_P6,
         "P7": bloc_P7, "P8": bloc_P8}
