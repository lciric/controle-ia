# Audit du verdict de la validation décisive du nul v9 — v1

Lecteur : sous-agent neuf de la session mère (règle R13 : n'a écrit ni le préenregistrement, ni son code, ni ses essais, ni ses contre-lectures, ni la vérification courte, et n'a pas lancé la course). Début 2026-11-08 10:10 UTC, fin 10:13 UTC (`date -u`). Aucune variable d'environnement lue, aucun réseau, aucune dépense, rien écrit dans l'arbre de la sortie.

Abréviations : TEXTE = `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` de `/home/user/wt-organisme-66dbcf1-w` (arbre détaché à `66dbcf1960dff4370a44e5f90d5ecc216f5b60cb`, propre) ; SORTIE = `/home/user/wt-sortie-nul-v9/diag/validation-nul-v9-v1/` (commit `0705eb0e87c9cb49947eb5b7a6abd61dbef128dc`, arbre propre).

## 1. Intégrité, pas à pas

| # | contrôle | résultat |
|---|---|---|
| 1 | TEXTE : `sha256sum` | `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb` = empreinte de la consigne, = compagnon `.sha256` du texte, = champ `preenregistrement.sha256` de la sortie. Égal. |
| 2 | Les 14 empreintes de la section 12 (bloc délimité) contre les fichiers de la copie : `sha256sum -c` | 14 sur 14 OK. |
| 3 | Les 14 empreintes du manifeste (`reglages.code_du_banc_sha256`) et de la sortie (`preenregistrement.empreintes_du_code_verifiees`) contre les fichiers de la copie | aucun écart (script en ligne, calcul par `hashlib`). Le manifeste porte aussi `code_sha256` (115 fichiers du dossier de code) : `pole/nul_v9.py` = `7ae450df…e46ee95`, `pole/nul_v8.py` = `cc452aaf…b976b888`, comme la section 12. |
| 4 | Empreintes de la SORTIE : chaque `.sha256` contre son fichier (`sha256sum -c`, 9 fichiers dont le LISEZ-MOI) | tous OK ; chaque empreinte figure aussi dans la table du LISEZ-MOI (8 sur 8). `sortie/banc-tricheurs-v9.json` `be22bf67…43d7`, `sortie/manifeste.json` `84559597…4afc`, conformes à la consigne. |
| 5 | Graine (section 4) | `int(sha256(TEXTE), 16)` recalculé = `reglages.entropie_racine` (38343129695488081123730001133079774509792561579847260681839260094342449862907) ; ≥ 2^64 (espace décisif). Égal. |
| 6 | Commande, répétitions, processus | manifeste : mode `decisif`, `repetitions` 1000, `processus` 2, `duree_max_s` 172800.0 (48 h), 31 lignes (18 fatales, 1 artefact requis, 5 puissance, 7 mesures), chemin `prereg/preenregistrement-validation-nul-v9-v1.md` ; sortie : `mode` decisif, 1000 répétitions sur chacune des 31 lignes, aucun `--lignes`. La commande exacte n'est écrite que dans le LISEZ-MOI (lanceuse) : elle est conforme à la section 5 (même options, `--duree-max-s` non passé) ; écart mineur, voir réserves : l'interprète est celui du venv (Python 3.13.18, numpy 2.4.6, `-I -B`) et le préfixe `nice -n 10` de la section 5 n'est pas écrit dans la commande rapportée (sans effet sur le calcul). |
| 7 | Code de fin 0 | `journaux/code-validation-v9-v1.txt` : `0` ; cohérent avec la sortie (`fatales_au_dessus_de_alpha` vide, `artefacts_non_vus` vide : code 0 par `code_de_sortie`). |
| 8 | Heures | `journaux/lancement-utc.txt` 08:16:01Z ; fin 09:46:43Z (LISEZ-MOI) : 1 h 30 min 42 s = 5 442 s ; `duree_s` de la sortie = 5442.1. Cohérent, et bien sous les 48 h. |
| 9 | Contrôles avant lancement (section 14, étapes 1 et 6) | `journaux/debut-essais.txt` 08:12:12Z (avant le lancement). `essais-nul-v9-v1.log` : `37 passed, 35 subtests passed in 45.42s` (attendu 37 et 35). `mutations-nul-v9-v1.log` : 43 lignes « tuée », dernière ligne `mutations : 43 ; tuées pour la raison attendue : 43 ; tuées pour une autre raison : 0 ; défaut du banc : 0 ; survivantes : 0 ; non appliquées : 0`, `témoin après restauration : 26 essais, 0 en échec`. Conforme. Aucun « error », « warn » ni « Traceback » dans la console ni dans le journal des essais. |
| 10 | Liste d'arrêt (section 9) | aucune garde déclenchée : pas de code 2 ni 3 ; pas de `ArretDuree` (5 442 s contre 172 800 s), pas de ligne en erreur (31 lignes toutes avec 1 000 répétitions), pas de richesse non finie, pas de monotonie violée (A2 : aucune perte négative ; `apparie_v8.perte` ≥ 0 partout ; les pertes égalent taux v8 moins taux v9 sur les 5 lignes de puissance). |

Chemins et empreintes des chiffres cités plus bas : SORTIE `sortie/banc-tricheurs-v9.json` (`be22bf67dcbe118f05269cafda40ded31cf7003141d07a7e9131d3d0597043d7`) sauf mention contraire.

## 2. Lecture à la lettre (section 7)

### 2.1 Issue écrite par `lire_v9` du code gelé
Champ `lecture.issue` du fichier de sortie : **« puissance perdue »** ; `lecture.issue_suspendue_par_audit` : false ; `lecture.audits` : liste vide. Le code gelé (`demonstrations/banc_tricheurs_v9.py` `7e4bff59…6e24e44`, fonction `lire_v9`, lignes 368 à 457) applique l'ordre de la section 7 : fatale non tenue → « trou » ; sinon perte non tenue → « puissance perdue » ; sinon artefact non tenu → « banc sans dents » ; sinon tout tenu → « confirmé » ; sinon « précision insuffisante ».

### 2.2 Recalcul indépendant
Script ci-dessous (bibliothèque standard seulement, rationnels exacts pour les valeurs p, aucun import du code du dépôt) ; exécuté par `python3 -I recalcul_verdict_v9.py …/sortie/banc-tricheurs-v9.json` à 10:10:58 UTC. Sortie résumée :

- 18 lignes fatales : 0 promotion sur 1 000 pour chacune ; valeur p de H0 « taux ≥ α » = 5,29·10⁻²³ pour chacune (seuil de Holm le plus sévère 0,05/18 ≈ 0,0028) : **18 « tenues »**. Aucune « non tenue ». (Maximum de promotions compatible avec « tenue » : 31 à 38 selon le rang, section 6.)
- 3 artefacts : T01|v1 411/1 000 (Clopper-Pearson unilatéral 95 % : [0,3851 ; 0,4373]) ; M01 sous v8 apparié 986/1 000 ([0,9782 ; 0,9915]) ; M02 sous v8 apparié 972/1 000 ([0,9618 ; 0,9800]) : bornes basses > 0,05, **3 « tenus »**.
- 5 pertes appariées (marge 0,05, Holm sur 5 lignes) : fraîche neuve 6/1 000, p(H0 d ≥ 0,05) = 1,7·10⁻¹⁵ : **tenue** ; fille neuve 38/1 000, p = 0,0433 > 0,05/4 : non jugeable ; I01 43/1 000, p = 0,173 : non jugeable ; F03 46/1 000, p = 0,312 : non jugeable ; **I02 105/1 000, p(H0 d ≤ 0,05) = 1,6·10⁻¹² ≤ 0,05/5 : non tenue** (Clopper-Pearson unilatéral 95 % de la perte : [0,0894 ; 0,1223]).
- Ordre de la section 7 : aucune fatale non tenue ; une perte non tenue (I02) : **« puissance perdue »**.
- **Les deux lectures coïncident** : issue, 18 états des fatales, 3 états des artefacts, 5 états des pertes (la sortie écrit « non jugeable (précision insuffisante) », le script « non jugeable » : même état) et liste d'audits (vide) sont égaux (dernière ligne du script : `True`).

Bornes de Clopper-Pearson des pertes recalculées (unilatérales 95 %, hors correction de Holm, à titre d'information ; la décision passe par les valeurs p et Holm) : fille neuve [0,0286 ; 0,0495], fraîche neuve [0,0026 ; 0,0118], I01 [0,0330 ; 0,0551], I02 [0,0894 ; 0,1223], F03 [0,0356 ; 0,0584].

### 2.3 Script de recalcul (en entier)
```python
# Recalcul indépendant de l'issue du banc v9 (texte scellé, sections 6, 7, 8) à partir des seuls champs de la sortie.
# N'importe aucun code du dépôt ; bibliothèque standard seulement. Usage : python3 -I recalcul_verdict_v9.py banc-tricheurs-v9.json
import json, sys
from fractions import Fraction
from math import comb, lgamma, log, exp

ALPHA = Fraction(1, 20)      # section 3 : alpha = 0,05
NIVEAU = Fraction(1, 20)     # section 6 : niveau familial de Holm 0,05
GAMMA = 0.05                 # section 6 : bornes de Clopper-Pearson unilatérales à 95 %
MARGE = Fraction(1, 20)      # annexe A : marge 0,05 sur chacune des 5 lignes de puissance
TOL = 1e-6                   # section 4 : P1a, log W <= 1e-6

def cdf(x, n, p):            # P(X <= x), exact (rationnels)
    if x < 0: return Fraction(0)
    return sum(Fraction(comb(n, i)) * p**i * (1 - p)**(n - i) for i in range(0, min(x, n) + 1))
def sf(x, n, p):             # P(X >= x), exact
    if x <= 0: return Fraction(1)
    return sum(Fraction(comb(n, i)) * p**i * (1 - p)**(n - i) for i in range(x, n + 1))
def holm(pv):                # Holm descendant, niveau 0,05
    ordre = sorted(pv, key=lambda c: (pv[c], c)); rej = set()
    for j, c in enumerate(ordre):
        if pv[c] > NIVEAU / (len(ordre) - j): break
        rej.add(c)
    return rej
def lpmf(i, n, p): return lgamma(n+1)-lgamma(i+1)-lgamma(n-i+1)+i*log(p)+(n-i)*log(1-p)
def fcdf(x, n, p): return sum(exp(lpmf(i, n, p)) for i in range(x + 1)) if 0 < p < 1 else 1.0
def fsf(x, n, p): return sum(exp(lpmf(i, n, p)) for i in range(x, n + 1)) if 0 < p < 1 else 1.0
def cp(x, n):                # Clopper-Pearson unilatérales 95 % (bas, haut), bissection
    def bis(f, a, b):
        for _ in range(200):
            c = (a + b) / 2
            a, b = (c, b) if f(c) < 0 else (a, c)
        return (a + b) / 2
    bas = 0.0 if x == 0 else bis(lambda p: fsf(x, n, p) - GAMMA, 1e-12, 1 - 1e-12)
    haut = 1.0 if x == n else bis(lambda p: GAMMA - fcdf(x, n, p), 1e-12, 1 - 1e-12)
    return bas, haut

b = json.load(open(sys.argv[1]))
R = {f"{x['ligne']}|{x['reglage']}": x for x in b["resultats"]}
fat = {c: x for c, x in R.items() if x["role"] == "fatale"}
puis = {x["ligne"]: x for x in R.values() if x["role"] == "puissance"}
assert len(R) == 31 and len(fat) == 18 and len(puis) == 5
assert all(x["repetitions"] == 1000 for x in R.values())
LIN = ("T01","T02","T03u","T03b","T04","T09l","T17s","nul_exact"); MOR = tuple(f"M0{i}" for i in range(1, 8)); LOG = ("T05s","T09g")

# 1. lignes fatales (section 6 : Holm sur 18 lignes)
ph = {c: cdf(x["promues"], x["repetitions"], ALPHA) for c, x in fat.items()}   # H0 taux >= alpha
pb = {c: sf(x["promues"], x["repetitions"], ALPHA) for c, x in fat.items()}     # H0 taux <= alpha
ten, ced = holm(ph), holm(pb)
fatales = {c: "tenue" if c in ten else "non tenue" if c in ced else "non jugeable" for c in sorted(fat)}
# 2. artefacts : bornes basses de Clopper-Pearson > alpha
art = {"T01|v1": (R["T01|v1"]["promues"], 1000), "M01|v8 apparié": (R["M01|v9"]["apparie_v8"]["promues"], 1000),
       "M02|v8 apparié": (R["M02|v9"]["apparie_v8"]["promues"], 1000)}
artefact = {}
for c, (k, n) in sorted(art.items()):
    bas, haut = cp(k, n); artefact[c] = "tenue" if bas > 0.05 else "non tenue" if haut < 0.05 else "non jugeable"
# 3. pertes appariées (section 6 : Holm sur 5 lignes, marge 0,05)
qh = {n: cdf(x["apparie_v8"]["perdues"], 1000, MARGE) for n, x in puis.items()}   # H0 d >= marge
qb = {n: sf(x["apparie_v8"]["perdues"], 1000, MARGE) for n, x in puis.items()}    # H0 d <= marge
th, cb = holm(qh), holm(qb)
perte = {n: "tenue" if n in th else "non tenue" if n in cb else "non jugeable" for n in sorted(puis)}
# 4. issue, dans l'ordre de la section 7
if "non tenue" in fatales.values(): issue = "trou"
elif "non tenue" in perte.values(): issue = "puissance perdue"
elif any(v != "tenue" for v in artefact.values()): issue = "non concluant (banc sans dents)"
elif all(v == "tenue" for v in list(fatales.values()) + list(perte.values())): issue = "confirmé"
else: issue = "non concluant (précision insuffisante)"
# 5. audits (section 8)
aud = []
for c, x in sorted(fat.items()):
    if x["ligne"] in LIN + MOR + LOG and x["promues"] > 0: aud.append("A1 " + c)
    if x["ligne"] in LIN + MOR and x["log_w_max_max"] > TOL: aud.append("A4 " + c)
    if x["ligne"] in MOR:
        pm = sum(v for d, v in x["dominants"].items() if d.startswith("morceaux:"))
        if pm < 500: aud.append(f"A5 {c} {pm}/1000")
k = R["T01|v1"]["promues"] / 1000
if not 0.10 <= k <= 0.90: aud.append("A3 T01|v1")
for l in ("M01", "M02"):
    if R[l + "|v9"]["apparie_v8"]["promues"] / 1000 < 0.50: aud.append("A3 " + l + " v8")
for n, x in puis.items():
    if x["apparie_v8"]["taux"] - x["taux"] < 0: aud.append("A2 " + n)
logmax_log = {c: fat[c]["log_w_max_max"] for c in fat if fat[c]["ligne"] in LOG}
p1b = any(fat[c]["promues"] > 0 or fat[c]["log_w_max_max"] > 0.25 for c in fat if fat[c]["ligne"] in LOG)
etage1 = all(v == "tenue" for v in fatales.values()) and all(v == "tenue" for v in artefact.values()) and not p1b

print("issue recalculée :", issue)
print("fatales :", fatales)
print("artefacts :", artefact, {c: cp(*art[c]) for c in art})
print("pertes :", perte, {n: puis[n]["apparie_v8"]["perdues"] for n in puis})
print("pertes, bornes Clopper-Pearson :", {n: cp(puis[n]["apparie_v8"]["perdues"], 1000) for n in sorted(puis)})
print("p Holm (H0 d>=marge) :", {n: float(qh[n]) for n in sorted(qh)}); print("p Holm (H0 d<=marge) :", {n: float(qb[n]) for n in sorted(qb)})
print("fatales : promues max", max(x["promues"] for x in fat.values()), "; p (H0 taux>=alpha) =", float(ph[sorted(ph)[0]]))
print("audits déclenchés :", aud); print("log W max T05s/T09g :", logmax_log, "; règle P1b déclenchée :", p1b)
print("premier étage de « puissance perdue » :", etage1)
print("coïncidence avec lecture du fichier :", issue == b["lecture"]["issue"] and fatales == b["lecture"]["fatales"]
      and artefact == b["lecture"]["artefact"] and {n: v.replace(" (précision insuffisante)", "") for n, v in b["lecture"]["perte_de_puissance"].items()} == perte
      and aud == b["lecture"]["audits"])
```
Sortie complète du script (10:10:58 UTC) : voir 2.2 ; en plus : `audits déclenchés : []`, `log W max T05s/T09g : T05s −0,0058, T09g −0,0059 ; règle P1b déclenchée : False`, `premier étage de « puissance perdue » : True`.

## 3. Audit de symétrie (R4), section 8

Déclencheurs relevés champ par champ (code gelé et script indépendant, mêmes résultats) :

| audit | condition | observé | déclenché |
|---|---|---|---|
| A1 | promotion sur une ligne refusée par construction (classes linéaire, par morceaux, log-linéaire) | 0 promotion sur les 18 lignes fatales, dont T05s et T09g | non |
| A2 | perte négative | pertes 0,038 ; 0,006 ; 0,043 ; 0,105 ; 0,046, toutes ≥ 0 | non |
| A3 | T01|v1 hors [0,10 ; 0,90] ; M01 ou M02 sous v8 apparié sous 0,50 | 0,411 ; 0,986 ; 0,972 | non |
| A4 | log W > 10⁻⁶ sur une ligne linéaire ou par morceaux | maximum observé −5,1·10⁻¹⁰ (M01) ; −3,1·10⁻¹⁰ (M02) ; −1,7·10⁻⁹ (M06) ; −6,0·10⁻¹⁰ (M07) ; partout négatif | non |
| A5 | membre par morceaux dominant à moins de 500/1 000 sur une ligne M | M01 999, M02 997, M03 1 000, M04 998, M05 993, M06 997, M07 912 (parmi les quatre premiers dominants rapportés) | non |
| P1b | T05s ou T09g : promotion ou log W max > +0,25 | 0 promotion ; −0,0058 et −0,0059 | non |
| A6 | toute issue « trou », « puissance perdue » ou « non concluant » : même audit avant lecture | issue « puissance perdue » : audit ci-dessous | à faire (fait) |

Aucun déclencheur de A1 à A5 ni de P1b : l'issue n'est pas suspendue. **A6 (relecture écrite d'une issue décevante comme d'une issue trop belle)**, faite ici :

1. Membres dominants (champ `dominants` de chaque ligne fatale) : sur chaque ligne M, le membre qui doit dominer domine : M01 `morceaux:sous_population` 991 ; M02 seuils z0 491 + z1 506 ; M03 sous-population 987 ; M04 seuils 492 + 506 ; M05 sous-population 536, seuils 457 ; M06 seuils 494 + 503 ; M07 seuils 448 + 463, `ajuste_log:archive:S2` 88 (le repère L3 du texte disait 10 sur 100 : cohérent, « à lire, pas un défaut »). Le refus des lignes M vient donc bien du membre par morceaux.
2. Dents du banc : M01 et M02 sont promus à 986/1 000 et 972/1 000 sous le v8 apparié (log W médian +38,8 et +28,8 sous v8 contre −0,0 et −0,19 sous v9) : le trou existe et le v9 le ferme. M03 à M07 sous v8 apparié : 969, 897, 433, 949, 573 sur 1 000 (rapportés sans critère).
3. Propreté : un résultat « tout à zéro » sur 18 lignes est trop propre pour ne pas être regardé. Les 18 valeurs sont 0/1 000, comme prédit (P1a), avec p = 5,3·10⁻²³ chacune. Lecture : (i) les lignes M ont un log W max de l'ordre de −10⁻⁹ à −10⁻² : le monde est un sommet du membre par morceaux (mélange à poids sur le bord du simplexe), l'écart de certificat y est nul, donc W touche 1 sans le dépasser ; c'est la signature attendue d'un certificat exact, pas d'un seuil trop bas, et la marge à la tolérance de A4 (10⁻⁶) est de trois ordres de grandeur ; (ii) les lignes linéaires ont un log W médian de −1,5 à −2,9 : surajustement normal ; (iii) la ligne T12a (monde au nul, fiche hors classe) a un log W max de +3,17 et 99ᵉ centile +0,63 sans aucune promotion : le banc n'est donc pas aveugle aux richesses positives, et la ligne n'est promue dans aucune des 1 000 répétitions (la décision d'une fille exige aussi la marge 2δ₀). Je ne trouve pas de défaut. **Réserve de lecture** (non un défaut) : toutes les prédictions P1 à P7 sont vraies, y compris les intervalles étroits de P4 à P6 ; le texte déclare que les prédictions ont été écrites après les lectures préalables L1 à L5 (section 4) et « ne décident pas de l'issue » : à lire comme une confirmation d'un modèle déjà vu à 100 répétitions, pas comme une preuve indépendante.
4. Pertes : l'issue « puissance perdue » repose sur I02 seule (105/1 000, p = 1,6·10⁻¹²) ; le sens ne dépend pas du choix de la famille de Holm (la perte de I02 est « non tenue » même à la valeur p brute, 1,6·10⁻¹² contre 0,05). La borne haute de Clopper-Pearson de F03 (0,0584) et de I01 (0,0551) dépasse la marge, celle de la fille neuve (0,0495) non, mais Holm ne rejette pas : trois lignes « non jugeables », comme le texte le prévoyait (section 6 : à la marge 0,05, une vraie perte de 0,04 est « tenue » avec une probabilité de 0,19 à 0,41 seulement).
5. Pertes et P4/P5 : toutes dans leurs intervalles (I02 : perte 0,105 dans [0,06 ; 0,17], puissance v9 0,381 dans [0,30 ; 0,52]).

Aucune des conséquences de la section 8 (course invalide d'office, « non concluant (réserve log-linéaire) ») ne s'applique. Pas d'audit écrit qui suspende l'issue : l'audit A6 ci-dessus conclut sans défaut.

## 4. Lignes mesurées (sans critère, section 11), taux v9 [borne basse ; borne haute CP 95 %] / v8 apparié
T07 0,009 [0,0047 ; 0,0157] / 0,020 ; T12b 0,840 [0,8197 ; 0,8588] / 0,899 ; H01 0,860 [0,8407 ; 0,8777] / 0,958 ; H02 0,145 [0,1270 ; 0,1646] / 0,965 ; H03 0,928 [0,9131 ; 0,9410] / 0,951 ; H04 0,236 [0,2140 ; 0,2591] / 0,967 ; H05 0,090 [0,0755 ; 0,1063] / 0,994. Source : `lecture.mesures`. Ces lignes sont hors de la classe couverte, déclarées sans seuil : elles ne disent rien de la validité du v9 sur sa classe (section 11), et elles montrent qu'il reste exposé hors de sa classe (profondeur 2, produit de lois : H01, H03 promus à plus de 85 %).
