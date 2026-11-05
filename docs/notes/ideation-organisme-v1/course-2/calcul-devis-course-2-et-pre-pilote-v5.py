"""Calcul du devis v5 de la course 2 (génération 1, trois bras de bisociation) et du pré-pilote recentré (brouillon 5).

Lignée session-depot (sous-agent), 31 octobre 2026. Aucun appel réseau, aucune dépense : arithmétique et tirages sur des
bases écrites ci-dessous, chacune marquée OBSERVÉ (registre ou journal cité), SOURCÉ (fichier cité) ou SUPPOSÉ.
Remplace calcul-devis-course-2-et-pre-pilote-v4.py (inchangé, R12).
Usage (interpréteur du système, numpy 2.5.3) :
  python3 -I calcul-devis-course-2-et-pre-pilote-v5.py > calcul-devis-course-2-et-pre-pilote-v5.sortie.txt
Avec un autre numpy, seule la première ligne (versions) peut changer ; les tirages viennent de default_rng (PCG64).
Graines (R9) : numpy.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)), cle_de_tache recopiée à l'identique
de src/controle_ia/manifeste.py (8 premiers octets du SHA-256 du nom de tâche).
"""
import hashlib
import sys

import numpy as np

RACINE = 20261031
TIRAGES = 20000


def cle_de_tache(tache: str) -> int:
    return int.from_bytes(hashlib.sha256(tache.encode("utf-8")).digest()[:8], "big")


def generateur(tache: str) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(tache),)))


# ================================================================ PRIX (USD par million de jetons : entrée, sortie)
PRIX = {
    "opus": (4.0, 20.0),    # SOURCÉ : table du skill claude-api (cache du 2026-10-06) ; collisionneur_v2.py (0e63febd…)
    "sonnet": (2.0, 10.0),  # SOURCÉ : table du skill claude-api (cache du 2026-10-06) ; le v4 le comptait au prix d'Opus
    "fable": (10.0, 50.0),  # SOURCÉ : table du skill claude-api ; collisionneur_v2.py
    "kimi": (2.0, 10.0),    # SOURCÉ (page lue le 30 oct.) ; OBSERVÉ conforme (depenses l. 255 ; journaux des relais)
    "argon": (8.3, 41.5),   # entrée : borne lue par Lazar (R-718) ; sortie SUPPOSÉ (commande_argon_v3d.py) ;
                            # OBSERVÉ cohérent : 2 452 / 10 164 jetons -> 0,44 (l. 256) ; 1 665 / 9 609 + 4 requêtes -> 0,61 (l. 261)
}
RECHERCHE = 0.01          # SOURCÉ : « web searches at $10 per 1,000 » (skill claude-api, shared/managed-agents-core.md l. 205,
                          # prix de liste) ; SUPPOSÉ : même prix par l'API Messages
RECHERCHE_PIRE = 0.05     # prix du dépôt pour la recherche d'Argon (commande_argon_v3d.py l. 82), pris comme pire


def cout(modele, entree, sortie):
    pe, ps = PRIX[modele]
    return entree * pe / 1e6 + sortie * ps / 1e6


# ================================================================ COUPURES DE KIMI (OBSERVÉ, 30 oct.)
# Appels longs de Kimi journalisés le 30 octobre : juge des 29 fiches (2 appels, 1 coupé à 300,7 s, 2,03 compté au pire) ;
# texte III v1 (1 appel) et v2 (3 appels) sans coupure ; tour étroit (4 appels, 1 coupé, 0,355 compté au pire) ;
# tour P-041 (au moins 3 appels, 1 coupé, 0,48 compté au pire ; l. 262, R-864). Soit >= 3 coupures sur ≈ 13 appels longs.
# Un appel coupé est compté au pire par le relais (réservation), puis rejoué : le surcoût compté est la réservation.
# Rapport réservation ÷ coût réel de l'appel rejoué : 2,03 / 0,755 = 2,7 ; 0,355 / 0,2246 = 1,6 ; 0,48 / ≈ 0,20 = 2,4.
P_COUPURE = 0.2
KAPPAS = (2.7, 1.6, 2.4)
FACTEUR_KIMI = 1 + P_COUPURE * float(np.mean(KAPPAS))   # ≈ 1,45 : facteur de la dépense comptée sur les postes de Kimi

# ================================================================ COÛTS UNITAIRES (attendu de base, avant coupure)
U = {
    # OBSERVÉ : Kimi juge en lot (29 fiches, un appel) : 222 635 / 31 010 jetons, 0,755 USD (l. 255)
    "juge_kimi_lot": cout("kimi", 222_635 / 29, 31_010 / 29),
    # SUPPOSÉ : Kimi juge en appel isolé (une fiche par appel, É6 du brouillon 5) : 8 000 / 4 000 (raisonnement)
    #           -> 0,056 ; même ordre que la base 0,057 du v3, gardée
    "juge_kimi_isole": 0.057,
    # OBSERVÉ en coût : Opus 3,31 / 29 fiches en 6 appels ; Argon 2,28 / 29 (l. 252)
    "juge_opus": 3.31 / 29,
    "juge_argon": 2.28 / 29,
    # SUPPOSÉ (v3) : lecture d'aiguillage = moitié d'un jugement d'Opus
    "aiguillage": cout("opus", 8_500, 1_150),
    # SUPPOSÉ (v3) : antériorité 25 000 / 5 000 au prix d'Opus, plus 5 recherches
    "anteriorite": cout("opus", 25_000, 5_000) + 5 * RECHERCHE,
    # SUPPOSÉ (brouillon 3) : lecture d'étiquettes d'une fiche par un lecteur, au prix d'Opus
    "etiquette": cout("opus", 4_000, 450),
    # OBSERVÉ : médiane des 7 appels longs de Kimi réussis du collisionneur (0,137 à 0,241 ; journaux run-texte-III-*)
    "fusion": float(np.median([0.1577, 0.1367, 0.2043, 0.2204, 0.2246, 0.2408, 0.2002])),
    # SUPPOSÉ (brouillon 3) : relecture d'un rendu par Fable 5.1
    "relecteur": cout("fable", 3_000, 340),
    # rendus d'un témoin : Kimi et Argon au prix d'un jugement isolé (brouillon 5) ; T = Sonnet 5.5, 5 000 / 2 500 (SUPPOSÉ)
    "rendu_kimi": 0.057,
    "rendu_argon": 2.28 / 29,
    "rendu_sonnet": cout("sonnet", 5_000, 2_500),
    # passes de proposeur (8 fiches, course) : Kimi SUPPOSÉ (v4 : 250 000 / 75 000, aucune mesure) ;
    # Argon OBSERVÉ : 6,00 USD pour 2 passes de 8 en course 1 (l. 250)
    "passe_kimi": cout("kimi", 250_000, 75_000),
    "passe_argon": 6.00 / 2,
    # Kimi, passe de 10 fiches du pré-pilote : SUPPOSÉ (brouillon 3, v4 : 300 000 / 140 000)
    "passe_kimi_pp": cout("kimi", 300_000, 140_000),
    # contrôles d'Argon : OBSERVÉ 1,75 USD pour un lancement (course 1, l. 250) ; SUPPOSÉ : un lancement par sous-session
    "controle_argon": 1.75,
    # rédacteur (Sonnet 5.5), coût d'un squelette ou d'une fiche courte : 2 000 jetons de sortie (v4) au prix de Sonnet
    "redaction_fiche": cout("sonnet", 0, 2_000),
}
PIRE = {  # coûts unitaires au pire (v3/v4 sauf mention)
    "juge_kimi_lot": 0.153,                # v3 ; couvre une coupure au pire (0,026 × 3,7 = 0,096)
    "juge_kimi_isole": 0.057 * (1 + 2.7),   # une coupure au pire (κ 2,7) puis l'appel rejoué : 0,21
    "juge_opus": 0.153, "juge_argon": 0.105, "aiguillage": 0.153,
    "anteriorite": 3 * cout("opus", 25_000, 5_000) + 5 * RECHERCHE_PIRE,   # × 3 sur les jetons, recherches à 0,05
    "etiquette": 1.5 * cout("opus", 4_000, 450),
    "fusion": 0.2408 * (1 + 2.7),         # appel long de Kimi le plus cher observé (0,241), coupé une fois au pire puis rejoué : 0,89
    "passe_kimi": 4.75,                   # v4 : 9,5 par sous-session
    "passe_argon": 1.34 * 6.00 / 2,       # relecteur du v4, défaut 2 : observé × 1,34
    "controle_argon": 3.0,                # v4
}

# familles d'incertitude : (médiane, écart-type du logarithme) ; dispersions tirées des intervalles à 80 % de P11
# (brouillon 5, l. 134) : sigma = ln(haut / bas) / (2 × 1,2816) ; médianes de P11 seulement où la base n'est pas observée.
def sig(bas, haut):
    return float(np.log(haut / bas) / (2 * 1.2816))


FAM = {
    "juge_kimi": (1.0, sig(0.8, 3.0)),     # P11 : 1,4 [0,8 ; 3,0] ; médiane 1,0 : base observée (lot) ou recoupée (isolé)
    "argon": (1.0, sig(0.7, 1.5)),         # P11
    "opus": (1.0, sig(0.8, 1.4)),          # P11
    "anteriorite": (1.2, sig(0.6, 3.0)),   # P11
    "aiguilleur": (1.0, sig(0.5, 2.0)),    # P11
    "passe_kimi": (1.2, sig(0.6, 3.8)),    # P11 (aucune mesure de Kimi proposeur)
    "fusion": (1.0, sig(0.5, 3.0)),        # P11 donne 1,3 sur la base 0,40 ; base désormais observée : médiane 1,0
    "passe_argon": (1.0, sig(0.7, 1.5)),   # base observée ; dispersion d'Argon (P11)
    "autre": (1.0, 0.35),                  # SUPPOSÉ (hors P11) : rédacteur, relecteur, rendus, étiquettes, contrôles
}


# ================================================================ STRUCTURE : un poste = liste de composantes
# composante = (base USD, famille, nombre d'appels de Kimi exposés à la coupure)
def comp(base, fam, kimi=0):
    return (base, fam, kimi)


def attendu(comps):
    return sum(b * (FACTEUR_KIMI if k else 1.0) for b, _, k in comps)


def tirer_comps(comps, g, n, z_commun, rho):
    tot = np.zeros(n)
    for b, fam, k in comps:
        m, s = FAM[fam]
        z = np.sqrt(rho) * z_commun + np.sqrt(1 - rho) * g.standard_normal(n)
        c = b * np.exp(np.log(m) + s * z)
        if k:
            coup = g.binomial(k, P_COUPURE, n)
            kap = g.choice(np.array(KAPPAS), size=n)
            c = c + coup * kap * c / k
        tot += c
    return tot


# ================================================================ PRÉ-PILOTE (brouillon 5, ordre B des étapes)
N_FONDS = 28                 # brouillon 5 : 28 fonds uniques (P 10, N 13, C 3, G 2), un rendu chacun
REND = {"kimi": 9, "argon": 9, "sonnet": 10}
N_AIG = 56                   # brouillon 5, É4 : 28 rendus, 10 passe 1, 6 difficiles, 12 concrets
N_FUSIONS_PP = 3             # trois bras, une paire chacun (S23, k = 1)
N_ANT = 8
P_SECONDE = 0.43             # brouillon 5 : seconde version des témoins si C5 échoue en première version


def redacteur_pp(m6b=False):
    sortie = N_FONDS * 2_000 + N_ANT * 2_500 + 6 * 2_500 + 8 * 2_000 + 24 * 500 + (4 * 2_500 if m6b else 0)
    return cout("sonnet", 6 * 45_000, sortie), sortie


red_att, red_sortie = redacteur_pp()
rendus = [comp(REND["kimi"] * U["rendu_kimi"], "juge_kimi", REND["kimi"]),
          comp(REND["argon"] * U["rendu_argon"], "argon"),
          comp(REND["sonnet"] * U["rendu_sonnet"], "autre")]
seconde = [comp(0.6 * red_att, "autre")] + rendus + [comp(30 * U["relecteur"], "autre"),
                                                     comp(N_FONDS * U["aiguillage"], "aiguilleur")]
# étapes : nom, composantes, plafond de relais du brouillon 5, plafond ajusté (recalculé : quantile 95 %), rôle, rang de sacrifice
ETAPES = [
    ("É0 appels de contrôle (cinq modèles)", [comp(0.01, "autre")], 0.5, 0.5, "P", None),
    ("É1 rédacteur (Sonnet 5.5) : 28 squelettes, 8 antériorités, 6 difficiles, 8 voisines, 24 éléments de l'axe 7",
     [comp(red_att, "autre")], 3.3, 3.3, "P", None),
    ("É2 Kimi, passe 1 (10 fiches, ≈ 4 appels)", [comp(U["passe_kimi_pp"], "passe_kimi", 4)], 3.0, None, "P", None),
    ("É3 rendus : Kimi 9, Argon 9, T (Sonnet 5.5) 10", rendus, 2.8, 2.8, "P", None),
    ("É4 aiguilleur 56, second lecteur 10, adjudicateur, nouvel essai",
     [comp((N_AIG + 10) * U["aiguillage"] + 0.05 + 0.3, "aiguilleur")], 5.5, 5.5, "P", None),
    ("É5 relecteur (Fable 5.1), 30 rendus au plus", [comp(30 * U["relecteur"], "autre")], 1.9, 1.9, "P", None),
    ("É5bis seconde version des témoins (si C5 échoue, probabilité 0,43)", seconde, 6.6, 6.6, "P2", None),
    ("É6 trois juges sur 28 rendus, un appel par fiche",
     [comp(N_FONDS * U["juge_opus"], "opus"), comp(N_FONDS * U["juge_argon"], "argon"),
      comp(N_FONDS * U["juge_kimi_isole"], "juge_kimi", N_FONDS)], 11.6, 11.6, "P", None),
    ("É7 passe « tableau » de Kimi, aiguilleur et second lecteur sur elle",
     [comp(U["passe_kimi_pp"], "passe_kimi", 4), comp(20 * U["aiguillage"], "aiguilleur")], 4.6, 4.6, "S", 4),
    ("É7 lectures d'étiquettes : 10 fiches × 3 grilles × 2 lecteurs", [comp(60 * U["etiquette"], "autre")], 1.0, None, "P", None),
    ("É7 fusions (3, Kimi), aiguilleur et trois juges sur elles",
     [comp(N_FUSIONS_PP * U["fusion"], "fusion", N_FUSIONS_PP), comp(N_FUSIONS_PP * U["aiguillage"], "aiguilleur"),
      comp(N_FUSIONS_PP * U["juge_opus"], "opus"), comp(N_FUSIONS_PP * U["juge_argon"], "argon"),
      comp(N_FUSIONS_PP * U["juge_kimi_isole"], "juge_kimi", N_FUSIONS_PP)], 3.5, 3.5, "S", 1),
    ("É7 Opus, table seule de l'axe 7 (24 éléments)", [comp(0.7, "opus")], 1.0, 1.0, "S", 3),
    ("É8 paraphrases (rédacteur, Sonnet 5.5)", [comp(0.6 / 2, "autre")], 0.7, 0.7, "P", None),
    ("É9 antériorité (Opus 5.5 avec recherche), 8 fiches", [comp(N_ANT * U["anteriorite"], "anteriorite")], 6.0, 6.0, "S", 2),
]
REDUCTION_E9 = ([comp(4 * U["anteriorite"], "anteriorite")], 3.0)    # brouillon 5 : M6 réduite à 4 fiches

# options du brouillon 5, configuration recommandée (CP5-05 : non chiffrée au brouillon 5)
M6B = [comp(cout("sonnet", 0, 4 * 2_500), "autre"), comp(4 * 0.10, "autre"), comp(4 * U["anteriorite"], "anteriorite")]
APPARIES = [comp(2 * U["rendu_kimi"], "juge_kimi", 2), comp(2 * U["rendu_argon"], "argon"), comp(4 * U["aiguillage"], "aiguilleur")]


def etapes_config(recommandee, q=0.95):
    et = [list(e) for e in ETAPES]
    if recommandee:   # D-g (b) : M6b ajouté à É1 (rédaction) et É9 (vérification, protégée) ; D-i (2) : 4 rendus appariés en É3
        et[1][1] = et[1][1] + [M6B[0]]
        et[3][1] = et[3][1] + APPARIES[:2]
        et[4][1] = et[4][1] + [APPARIES[2]]
        et.append(["É9b M6b, 4 fiches d'antériorité non citée (protégée)", M6B[1:], 2.5, 2.5, "P", None])
    for i, e in enumerate(et):   # plafond ajusté = quantile q de l'étape, arrondi au demi-dollar supérieur
        e[3] = plafond_q(e[1], f"devis-v5-plafond-q95-{e[0]}", q)
    return et


def plafond_q(comps, tache, q, n=TIRAGES):
    g = generateur(tache)   # même graine pour tous les q : mêmes tirages, quantiles différents
    t = tirer_comps(comps, g, n, g.standard_normal(n), 0.0)
    return float(np.ceil(2 * np.quantile(t, q)) / 2)


def simuler_pp(plafond, arret, caps_ajustes, recommandee, tache, rho=0.0, n=TIRAGES, q=0.95, souple=False):
    # souple : une étape protégée qui atteint son plafond de relais peut continuer sur la marge restante sous le plafond
    # S17 (plafond − cumul − attendu des étapes restantes) ; proposé ici pour le brouillon 6, SUPPOSÉ
    et = etapes_config(recommandee, q)
    g = generateur(tache)
    z_c = g.standard_normal(n)
    tirs = [tirer_comps(e[1], g, n, z_c, rho) for e in et]
    tir_red = tirer_comps(REDUCTION_E9[0], g, n, z_c, rho)
    seconde_lieu = g.random(n) < P_SECONDE
    caps = [e[3] if caps_ajustes else e[2] for e in et]
    cap_red = plafond_q(REDUCTION_E9[0], "devis-v5-plafond-q95-reduction-E9", q) if caps_ajustes else REDUCTION_E9[1]
    att = [attendu(e[1]) for e in et]
    att_red = attendu(REDUCTION_E9[0])
    i_e9 = next(i for i, e in enumerate(et) if e[0].startswith("É9 antériorité"))
    i_sec = next(i for i, e in enumerate(et) if e[4] == "P2")
    depense = np.zeros(n)
    sacrifice = np.zeros(n, bool)
    protegee_non_lancee = np.zeros(n, bool)
    coupee_protegee = np.zeros(n, bool)
    arret_touche = np.zeros(n, bool)
    retire = {k: np.zeros(n, bool) for k in ("fusions", "M6 réduite", "table seule", "passe tableau")}
    nom_rang = {1: "fusions", 2: "M6 réduite", 3: "table seule", 4: "passe tableau"}
    for t in range(n):
        actif = [True] * len(et)
        reduite = False
        actif[i_sec] = bool(seconde_lieu[t])
        cumul = 0.0
        for i, e in enumerate(et):
            if not actif[i]:
                continue
            role = e[4]

            def cap_i(j):
                return cap_red if (j == i_e9 and reduite) else caps[j]

            def att_j(j):
                if j == i_sec and j > i:
                    return att[j]
                return att_red if (j == i_e9 and reduite) else att[j]

            # règle de sacrifice d'A1 : projection = cumul + plafond de E + attendu des étapes restantes
            while True:
                proj = cumul + (cap_i(i) if actif[i] else 0.0) + sum(att_j(j) for j in range(i + 1, len(et)) if actif[j])
                if proj <= plafond:
                    break
                cand = [(et[j][5], j) for j in range(i, len(et)) if actif[j] and et[j][4] == "S" and not (j == i_e9 and reduite)]
                if not cand:
                    break
                rang, j = min(cand)
                sacrifice[t] = True
                retire[nom_rang[rang]][t] = True
                if j == i_e9:
                    reduite = True
                else:
                    actif[j] = False
            if not actif[i]:
                continue
            est_sacrifiable = role == "S" and not (i == i_e9 and reduite)
            if cumul >= arret and est_sacrifiable:
                arret_touche[t] = True
                sacrifice[t] = True
                retire[nom_rang[e[5]]][t] = True
                continue
            if cumul + cap_i(i) > plafond:
                if est_sacrifiable:
                    sacrifice[t] = True
                    retire[nom_rang[e[5]]][t] = True
                else:
                    protegee_non_lancee[t] = True
                continue
            d = tir_red[t] if (i == i_e9 and reduite) else tirs[i][t]
            cap_eff = cap_i(i)
            if souple and not est_sacrifiable:
                marge = plafond - cumul - sum(att_j(j) for j in range(i + 1, len(et)) if actif[j])
                cap_eff = max(cap_eff, marge)
            if d > cap_eff:
                d = cap_eff
                if not est_sacrifiable:
                    coupee_protegee[t] = True
            cumul += d
        depense[t] = cumul
    return {"depense": depense, "sacrifice": sacrifice, "protegee_non_lancee": protegee_non_lancee,
            "coupee_protegee": coupee_protegee, "arret": arret_touche, "retire": retire}


# ================================================================ COURSE 2 = GÉNÉRATION 1
FICHES = 16      # par proposeur et par sous-session (2 passes de 8)
TEMOINS = 8      # par lot et par sous-session (v3, v4) ; témoins réutilisés du pré-pilote, sans rendu nouveau (SUPPOSÉ)
NOTABLES = 10    # antériorité par sous-session (v3, v4)
LECTURES_PAR_FICHE = 6   # 3 grilles (liste fermée, vocabulaire Gu-Krenn, niches du bras méta) × 2 lecteurs


def course(ss, fusions_par_ss, juges_isoles=False, controles_par_ss=True, temoins=TEMOINS, notables=NOTABLES):
    fk = fa = ss * FICHES
    nf = ss * fusions_par_ss
    nt = ss * temoins
    jk = "juge_kimi_isole" if juges_isoles else "juge_kimi_lot"
    n_lots_kimi = (fa + nt) if juges_isoles else ss       # un lot par sous-session, ou un appel par fiche
    nctl = ss if controles_par_ss else 1
    na = fk + fa + nf
    nant = ss * notables + nf // 2
    ne = ss * 2 * 8 * LECTURES_PAR_FICHE                     # passe 1 des deux proposeurs (8 + 8 fiches)
    P = []   # (poste, appels, composantes, pire)
    P.append((f"Kimi proposeur ({ss} × 2 passes de 8)", f"≈ {6 * ss}", [comp(2 * ss * U["passe_kimi"], "passe_kimi", 6 * ss)],
              2 * ss * PIRE["passe_kimi"]))
    P.append((f"Argon proposeur ({ss} × 2 passes de 8)", f"≈ {2 * ss} à {6 * ss}", [comp(2 * ss * U["passe_argon"], "passe_argon")],
              2 * ss * PIRE["passe_argon"]))
    P.append((f"Contrôles d'Argon ({nctl} lancement{'s' if nctl > 1 else ''})", f"{nctl} lot{'s' if nctl > 1 else ''}",
              [comp(nctl * U["controle_argon"], "autre")], nctl * PIRE["controle_argon"]))
    P.append((f"Aiguilleur ({na} : fiches et fusions, avant tout juge)", na, [comp(na * U["aiguillage"], "aiguilleur")],
              na * PIRE["aiguillage"]))
    n_par_argon = fk + nf + nt
    n_par_kimi = fa + nt
    P.append((f"Juges croisés : Argon sur {n_par_argon} (fiches de Kimi, fusions, témoins) ; Kimi sur {n_par_kimi} (fiches d'Argon, témoins)",
              f"Argon ≈ {2 * ss} ; Kimi {n_lots_kimi}",
              [comp(n_par_argon * U["juge_argon"], "argon"), comp(n_par_kimi * U[jk], "juge_kimi", n_lots_kimi)],
              n_par_argon * PIRE["juge_argon"] + n_par_kimi * PIRE[jk]))
    no = fk + fa + nf + nt
    P.append((f"Opus 5.5 troisième juge ({no})", f"≈ {6 * ss}", [comp(no * U["juge_opus"], "opus")], no * PIRE["juge_opus"]))
    P.append((f"Antériorité ({nant} : {notables} notables par sous-session, la moitié des fusions)", nant,
              [comp(nant * U["anteriorite"], "anteriorite")], nant * PIRE["anteriorite"]))
    P.append((f"Lectures d'étiquettes ({ne} : 16 fiches de passe 1 × 3 grilles × 2 lecteurs, par sous-session)", ne,
              [comp(ne * U["etiquette"], "autre")], ne * PIRE["etiquette"]))
    P.append((f"Fusions par Kimi ({nf} : 3 bras, une paire par session)", nf, [comp(nf * U["fusion"], "fusion", nf)],
              nf * PIRE["fusion"]))
    P.append(("Tableau minimal (programme) ; appels de contrôle", "—", [comp(0.01, "autre")], 0.5))
    return P


def imprimer_course(titre, P):
    print(f"\n== {titre} ==")
    print("poste | appels | attendu de base USD | attendu compté (coupures de Kimi) USD | pire USD")
    ta = tp = 0.0
    for nom, appels, comps, pire in P:
        base = sum(c[0] for c in comps)
        a = attendu(comps)
        ta += a
        tp += pire
        print(f"{nom} | {appels} | {base:.2f} | {a:.2f} | {pire:.2f}")
    print(f"TOTAL | | | {ta:.2f} | {tp:.2f}")
    return ta, tp


def tirer_course(P, tache, rho=0.0, n=TIRAGES):
    g = generateur(tache)
    z_c = g.standard_normal(n)
    tot = np.zeros(n)
    for _, _, comps, _ in P:
        tot += tirer_comps(comps, g, n, z_c, rho)
    return tot


# ================================================================ SORTIES
print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; racine {RACINE} ; tirages {TIRAGES}")
print("prix (USD par million, entrée / sortie) : " + " ; ".join(f"{k} {v[0]} / {v[1]}" for k, v in PRIX.items())
      + f" ; recherche {RECHERCHE} (pire {RECHERCHE_PIRE})")
print(f"coupures de Kimi : probabilité {P_COUPURE} par appel ; réservation ÷ coût {KAPPAS} ; facteur compté {FACTEUR_KIMI:.3f}")
print("coûts unitaires de base (USD) : " + " ; ".join(f"{k} {v:.4f}" for k, v in U.items()))
print("coûts unitaires au pire (USD) : " + " ; ".join(f"{k} {v:.3f}" for k, v in PIRE.items()))
print("dispersions (médiane ; écart-type du logarithme) : " + " ; ".join(f"{k} {m} ; {s:.2f}" for k, (m, s) in FAM.items()))
print(f"rédacteur du pré-pilote : 270 000 jetons d'entrée, {red_sortie} de sortie, {red_att:.2f} USD (Sonnet 5.5)")

for recommandee in (False, True):
    et = etapes_config(recommandee)
    print(f"\n== Pré-pilote, brouillon 5, {'configuration recommandée (D-g (b), D-i (2))' if recommandee else 'texte du brouillon (D-g (a), D-i (1))'} ==")
    et90 = etapes_config(recommandee, 0.90)
    print("étape | attendu b5 (bases v3) | attendu compté v5 | médiane tirée | plafond de relais b5 | P(dépasse le plafond b5) | "
          "plafond au quantile 90 % | plafond au quantile 95 % | rôle")
    gd = generateur("devis-v5-diagnostic-etapes")
    B5 = {0: None, 1: 2.6, 2: 2.0, 3: 2.0, 4: 4.1, 5: 1.4, 6: 4.9, 7: 7.0, 8: 3.1, 9: 0.75, 10: 2.1, 11: 0.7, 12: 0.6, 13: 2.0}
    s_att = s_cap = s_capa = s_cap90 = 0.0
    for i, e in enumerate(et):
        a = attendu(e[1])
        b5 = B5.get(i)
        td = tirer_comps(e[1], gd, TIRAGES, gd.standard_normal(TIRAGES), 0.0)
        print(f"{e[0]} | {'—' if b5 is None else b5} | {a:.2f} | {np.median(td):.2f} | {e[2]} | {np.mean(td > e[2]):.2f} | {et90[i][3]} | {e[3]} | "
              f"{e[4]}{'' if e[5] is None else '(' + str(e[5]) + ')'}")
        if e[4] != "P2":
            s_att += a
        s_cap += e[2]
        s_capa += e[3]
        s_cap90 += et90[i][3]
    a_sec = attendu(seconde)
    print(f"total attendu sans seconde version {s_att:.2f} ; seconde version {a_sec:.2f} si elle a lieu, pondérée {P_SECONDE * a_sec:.2f} ; "
          f"total attendu pondéré {s_att + P_SECONDE * a_sec:.2f} ; somme des plafonds de relais : b5 {s_cap:.1f}, quantile 90 % {s_cap90:.1f}, quantile 95 % {s_capa:.1f}")

print("\n== Pré-pilote : règle d'A1 étape par étape (rapports P11 recalés ; coupures de Kimi tirées) ==")
RES_PP = {}
for (plaf, arret, caps_aj, q, reco, rho, nom) in (
        (45, 40, False, None, False, 0.0, "plafond 45, arrêt 40, plafonds de relais du brouillon 5, texte du brouillon"),
        (45, 40, False, None, True, 0.0, "plafond 45, arrêt 40, plafonds de relais du brouillon 5, configuration recommandée"),
        (45, 40, True, 0.90, True, 0.0, "plafond 45, arrêt 40, plafonds au quantile 90 %, configuration recommandée"),
        (50, 45, True, 0.90, True, 0.0, "plafond 50, arrêt 45, plafonds au quantile 90 %, configuration recommandée"),
        (50, 45, True, 0.90, True, 0.5, "idem, rapports corrélés entre postes (rho 0,5)"),
        (45, 40, True, 0.90, True, 0.0, "plafond 45, arrêt 40, plafonds au quantile 90 % SOUPLES, configuration recommandée"),
        (50, 45, True, 0.90, True, 0.0, "plafond 50, arrêt 45, plafonds au quantile 90 % SOUPLES, configuration recommandée"),
        (50, 45, True, 0.90, True, 0.5, "idem SOUPLES, rapports corrélés entre postes (rho 0,5)"),
        (45, 40, True, 0.95, True, 0.0, "plafond 45, arrêt 40, plafonds au quantile 95 %, configuration recommandée"),
        (50, 45, True, 0.95, True, 0.0, "plafond 50, arrêt 45, plafonds au quantile 95 %, configuration recommandée"),
        (55, 50, True, 0.95, True, 0.0, "plafond 55, arrêt 50, plafonds au quantile 95 %, configuration recommandée"),
        (32, 28, False, None, True, 0.0, "plafond 32, arrêt 28 (GO-2026-10-30-07 tel quel), plafonds du brouillon 5, configuration recommandée")):
    souple = "SOUPLES" in nom
    r = simuler_pp(plaf, arret, caps_aj, reco, "devis-v5-pre-pilote", rho, q=q if q else 0.95, souple=souple)
    RES_PP[(plaf, caps_aj, q, reco, rho, souple)] = r
    d = r["depense"]
    ret = " ; ".join(f"{k} {np.mean(v):.2f}" for k, v in r["retire"].items())
    print(f"{nom} : dépense médiane {np.median(d):.1f}, quantile 90 % {np.quantile(d, 0.9):.1f}, quantile 99 % {np.quantile(d, 0.99):.1f} ; "
          f"P(sacrifice ou réduction) {np.mean(r['sacrifice']):.2f} ({ret}) ; P(arrêt d'étape touché) {np.mean(r['arret']):.2f} ; "
          f"P(étape protégée non lancée) {np.mean(r['protegee_non_lancee']):.3f} ; P(étape protégée coupée par son relais) {np.mean(r['coupee_protegee']):.3f}")

# complément conditionnel (brouillon 5, CP4-10) recalé
compl = [comp(24 * U["redaction_fiche"], "autre"), comp(8 * U["rendu_kimi"], "juge_kimi", 8), comp(8 * U["rendu_argon"], "argon"),
         comp(8 * U["rendu_sonnet"], "autre"), comp(24 * U["relecteur"], "autre"), comp(24 * U["aiguillage"], "aiguilleur"),
         comp(24 * U["juge_opus"], "opus"), comp(24 * U["juge_argon"], "argon"), comp(24 * U["juge_kimi_isole"], "juge_kimi", 24)]
gc = generateur("devis-v5-complement")
tcompl = tirer_comps(compl, gc, TIRAGES, gc.standard_normal(TIRAGES), 0.0)
print(f"\ncomplément conditionnel (24 fonds) : attendu compté {attendu(compl):.2f} (b5 : 11,6) ; médiane {np.median(tcompl):.1f} ; "
      f"quantile 90 % {np.quantile(tcompl, 0.9):.1f} ; P(> 17,5, plafond b5) {np.mean(tcompl > 17.5):.3f}")

# course
RES_C = {}
for ss in (4, 3, 2):
    for fps, lect in ((6, "B"), (3, "A")):
        P = course(ss, fps)
        if ss == 4:
            RES_C[(ss, lect)] = imprimer_course(
                f"Course, {ss} sous-sessions, lecture {lect} ({fps * ss} fusions : "
                f"{'une paire par bras et par proposeur, ≈ 12 par proposeur (R-642, n° 268)' if lect == 'B' else 'une paire par bras et par sous-session (brouillon 5, S22 k = 1)'})",
                P)
        else:
            RES_C[(ss, lect)] = (sum(attendu(c) for _, _, c, _ in P), sum(p for *_, p in P))

print("\n== Variantes de la course (attendu compté ; pire ; médiane et quantile 90 % tirés) ==")
TC = {}
for rho in (0.0, 0.5):
    for ss in (4, 3, 2):
        for fps, lect in ((6, "B"), (3, "A")):
            TC[(ss, lect, rho)] = tirer_course(course(ss, fps), "devis-v5-course", rho)
for ss in (4, 3, 2):
    for lect in ("B", "A"):
        a, p = RES_C[(ss, lect)]
        t0, t5 = TC[(ss, lect, 0.0)], TC[(ss, lect, 0.5)]
        print(f"{ss} sous-sessions, lecture {lect} : attendu {a:.1f} ; pire {p:.1f} ; médiane {np.median(t0):.1f} ; quantile 90 % "
              f"{np.quantile(t0, 0.9):.1f} ; corrélé (rho 0,5) : médiane {np.median(t5):.1f}, quantile 90 % {np.quantile(t5, 0.9):.1f}")
for nom, P in (("4 sous-sessions, lecture B, juges en appel isolé (une fiche par appel)", course(4, 6, juges_isoles=True)),
               ("4 sous-sessions, lecture B, un seul lancement (contrôles d'Argon une fois)", course(4, 6, controles_par_ss=False)),
               ("4 sous-sessions, lecture B, allégée (4 témoins par lot, antériorité sur 6 notables)", course(4, 6, temoins=4, notables=6))):
    a = sum(attendu(c) for _, _, c, _ in P)
    p = sum(x for *_, x in P)
    print(f"{nom} : attendu {a:.1f} ; pire {p:.1f}")
ant_var = course(4, 6)[6]
print(f"recherche à 0,05 USD au lieu de 0,01 (lecture B, 4 sous-sessions, {ant_var[1]} fiches) : + {ant_var[1] * 5 * 0.04:.1f} USD attendus")

print("\n== Ce que la course peut faire selon le plafond total (dépense du pré-pilote tirée par la règle d'A1 au plafond 50, "
      "plafonds au quantile 90 % souples, configuration recommandée) ==")
for rho in (0.0, 0.5):
    dpp = RES_PP[(50, True, 0.90, True, rho, True)]["depense"]
    for lect in ("B", "A"):
        for total in (110, 140, 160, 180):
            reste = total - dpp
            c4, c3, c2 = TC[(4, lect, rho)], TC[(3, lect, rho)], TC[(2, lect, rho)]
            t4 = np.mean(c4 <= reste)
            t3 = np.mean((c4 > reste) & (c3 <= reste))
            t2 = np.mean((c3 > reste) & (c2 <= reste))
            t0 = np.mean(c2 > reste)
            print(f"rho {rho} ; lecture {lect} ; plafond total {total} : reste médian {np.median(reste):.1f} ; course à 4 : {t4:.2f} ; "
                  f"à 3 : {t3:.2f} ; à 2 : {t2:.2f} ; aucune : {t0:.3f}")

print("\n== Sensibilité (R4) : coupure d'une étape protégée par son relais, plafond 45 / 40, plafonds du brouillon 5, "
      "configuration recommandée ==")
i_etiq = next(j for j, e in enumerate(ETAPES) if "étiquettes" in e[0])
ETAPES[i_etiq] = (ETAPES[i_etiq][0] + " [compte du brouillon 5 : 30 lectures]", [comp(30 * U["etiquette"], "autre")], 1.0, None, "P", None)
for moitie in (False, True):
    if moitie:
        for k, (m, s_) in list(FAM.items()):
            FAM[k] = (m, s_ / 2)
    r = simuler_pp(45, 40, False, True, "devis-v5-pre-pilote")
    print(f"lectures d'étiquettes au compte du brouillon 5 (30) ; dispersions {'divisées par deux' if moitie else 'de P11'} : "
          f"P(étape protégée coupée par son relais) {np.mean(r['coupee_protegee']):.3f} ; dépense médiane {np.median(r['depense']):.1f}")
print("fin")
