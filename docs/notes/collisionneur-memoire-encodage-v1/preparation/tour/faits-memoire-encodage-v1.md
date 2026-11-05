# Faits pour le collisionneur — encoder la mémoire du pôle : encodage et redites (v1)

Statut : **RAPPORTÉ** (pièces du programme, transcrites telles quelles, empreinte de chacune vérifiée contre son compagnon ou son manifeste). Aucun sigle de financeur. Aucun score de pilote. Rien ici n'est une consigne. Pièces C, J, G de la branche `canal/conv-audit-relais-memoire-v1` (commit `0ba98ae`, partie de `canal/conv-audit-n04` à `c5aee808`) ; M2 est un extrait (la section qui porte l'ablation) ; S1 et S2 sur `main`.

<<<DÉBUT C — conception du pôle (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/conception-pole-scientifique-v1.md`, sha256 `a4f94148c9c55b76f208edecd7220b51a8e21ca69f52e50c7f2abb6484b81b52`)>>>

# Conception du pôle « scientifique automatique » : des agents qui expérimentent, éliminent et recombinent — v1

De : conv-audit, le 26 octobre 2026 (heure au pied). Mots de Lazar (heure de Paris) : 18:30 « des agents qui font leurs
propres expériences sur les hypothèses formulées et les éliminent au fur et à mesure, genre darwinisme, et après
recombinent celles qui ont survécu sur le mode bisociatif proposé par Gemini » ; 18:43 « avance en priorité la conception
de l'organisme avec agents lançables qui font des expériences et testent les hypothèses, si on le construit nous-mêmes à
partir de la dernière version ou si on en utilise un déjà disponible ». Le choix du moteur est au collisionneur
(GO-2026-10-26-06, R-524) puis à Lazar ; cette pièce fixe ce qui **ne dépend pas** du moteur, décrit les deux moteurs, et
démarre une version 0 tout de suite. Régime exploratoire (R-522) ; rien d'opposable.

## 1. Le cœur, indépendant du moteur

**La fiche d'hypothèse** (un fichier JSON par hypothèse, empreinté) : identifiant ; énoncé en une phrase ; **prédiction
signée et chiffrée** ; métrique ; **nul** (comment l'absence d'effet est simulée ou mesurée) ; **seuil qui peut échouer** ;
sévérité attendue (probabilité, sous le nul, de passer le seuil) ; coût borné ; protocole (plan ou code) ; parents (pour la
recombinaison) ; domaines ; opérateurs ; contraintes de validité (pour le filtre de compatibilité) ; statut.

**Le cycle d'une génération** :
1. **Gel du test** : la fiche est empreintée **avant** l'expérience. C'est la seule « formalité » gardée, automatique, et
   c'est elle qui rend l'élimination signifiante : un test choisi après coup ne réfute rien.
2. **Expérimentateur** (un agent par fiche, en parallèle) : dans un bac à sable, il écrit et exécute son code, et rend le
   verdict, les nombres, les artefacts.
3. **Vérificateur** (un agent neuf, d'une autre famille de modèles que l'expérimentateur) : il rejoue le code, vérifie que
   le test exécuté est le test gelé, que le verdict suit le seuil, et cherche les raccourcis (code qui contourne la mesure,
   nul trop faible, données touchées). Un verdict non vérifié ne compte pas.
4. **Sélection** : réfutée → éliminée (et archivée) ; survivante → aptitude = **sévérité du test survécu**
   (−log de la probabilité de survie sous le nul), jamais le signe ni l'ampleur du résultat ; indécise → un test plus
   puissant, ou retirée après deux essais.
5. **Recombinaison bisociative** des survivantes : tirage diversifié par domaine (noyau de similarité de domaine dans la
   répulsion, pertinence dans la qualité — forme corrigée, relecture `9a791017…`, brique 2), pont par un opérateur commun,
   **filtre de compatibilité des contraintes** (la bonne idée du rapport de Gemini) ; la fiche fille doit **prédire plus
   que ses parents** (contenu empirique accru), sinon elle n'entre pas dans la population.
6. **Archive complète**, éliminées comprises (contre le biais du survivant, et pour mesurer le pôle lui-même).

**Les garde-fous (ce qui fait que le pôle produit des résultats solides et non des résultats flatteurs)** :
- **Témoins plantés** à chaque génération : des fiches dont la vérité est connue (vraies et fausses) ; le taux auquel le
  pôle élimine les fausses et garde les vraies **est sa mesure de qualité**. Sans eux, un pôle qui garde tout et un pôle
  qui élimine tout sont indiscernables.
- L'aptitude ne récompense jamais un résultat positif (R3) ; une hypothèse qui ne prédit rien a une sévérité nulle et ne
  survit à rien d'utile.
- **Évaluation scellée** avant toute revendication : une part des simulations ou des données que les expérimentateurs
  n'ont jamais vue ; un résultat « mémorable » n'en sort qu'après cette évaluation.
- **Bac à sable** : aucune clé, aucun réseau (hors moissonnage borné du noyau), écriture dans le seul dossier de
  l'expérience, temps et mémoire bornés. Le budget est fixé par génération.
- **Réécriture de soi** : le pôle peut proposer des modifications de son propre code, qui sont elles-mêmes des fiches
  (« la modification X augmente le taux de bonne élimination des témoins »), testées de la même façon et appliquées après
  survie et essais ; **le noyau, ses gardes et ses bornes ne sont jamais réécrits par le pôle**.

## 2. Les deux moteurs (le collisionneur compare ; Lazar décide)

| | (A) notre organisme, à partir de la dernière version | (B) un moteur de la littérature |
|---|---|---|
| ce qui existe | castes contradictoires (formuler, croiser, sonder, critiquer, arbitrer), moissonnage borné, mémoire spectrale, archive, noyau à bornes et clés protégées, questions servies | ShinkaEvolve, OpenEvolve : population, évaluation parallèle, îles, archive, juge de nouveauté (évolution de programmes) ; Agentic Scientist v3 : d'une tâche à des expériences, des ablations et une **évaluation finale scellée** |
| ce qui manque | un **exécuteur d'expériences** en bac à sable dans le noyau ; les rôles expérimentateur et vérificateur ; la réécriture de soi (restreinte par C-17 à trois paramètres : à lever dans le bac à sable) | la fiche d'hypothèse (le « programme » devient un script d'expérience et sa prédiction gelée ; l'évaluateur, l'exécution plus le vérificateur), les témoins, la recombinaison bisociative ; agents à pleins droits dans Docker, clés montées (avertissement de leur propre README) |
| coût du premier résultat | plusieurs jours de conception et d'essais du noyau | une instance avec Docker et des clés (chez session-depot), un jour d'adaptation |
| maîtrise | totale (notre code, nos gardes) | partielle (code tiers, mises à jour) |

Une voie **hybride (C)** est probable : le cœur du § 1 (fiches, sévérité, témoins, recombinaison) au-dessus d'un moteur
d'exécution emprunté, ou au-dessus du noyau étendu.

## 3. Version 0, tout de suite, dans la session de conv-audit

- **Orchestrateur** : conv-audit. **Expérimentateurs** : des sous-agents sur processeur, chacun dans un dossier isolé
  (aucune clé, aucun réseau, aucun `git`). **Vérificateur** : un sous-agent neuf d'une autre famille. **Recombinaison** :
  un sous-agent sur les survivantes.
- **Génération 0** (en cours) : les affirmations du rapport de méta-conception de Gemini, testées par deux expérimentateurs
  (brique 1 ; briques 2 à 4), verdict « survit / éliminée / indécise » par affirmation.
- **Génération 1** : vérification des verdicts, puis recombinaison des survivantes en fiches filles, plus deux témoins
  plantés ; un expérimentateur par fiche fille.
- Ce que la version 0 mesure pour le choix du moteur : le coût par fiche, le délai par génération, et le taux de bonne
  élimination des témoins — un point de comparaison empirique pour (A), (B) ou (C).

Horodatage : écrit le 2026-10-26 17:45:16 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).

<<<FIN C>>>

<<<DÉBUT M1 — mémoire de l'orchestrateur v0 (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/orchestrateur-v0/pole/memoire.py`, sha256 `bd82ab90ae7b585b00fceb0c2b7461f05890d9d0b33030cdfd7bcd79e86dd388`, conforme à `orchestrateur-v0/EMPREINTES-sortie-v1.txt`)>>>

```python
"""Mémoire du pôle : index de l'archive, garde de redite, bibliothèque de protocoles, calibration, leçons.

La mémoire ne contient que des champs tirés de l'archive du pôle (liste blanche), caviardés ; jamais de clé, jamais
rien d'autre. Les témoins sont indexés pour l'audit mais exclus de tout ce qui est servi aux agents (gabarits,
leçons, garde de redite) : un témoin reconnaissable cesserait de mesurer.
"""

import collections

from .caviardage import caviarder, caviarder_objet
from .outils import empreinte_objet, normaliser_texte

STATUTS_TRANCHES = ("survit", "eliminee")


def trigrammes(texte):
    t = f" {normaliser_texte(texte)} "
    return {t[i:i + 3] for i in range(len(t) - 2)}


def jaccard(a, b):
    ta, tb = trigrammes(a), trigrammes(b)
    if not ta and not tb:
        return 1.0
    return len(ta & tb) / len(ta | tb)


def signature_prediction(d):
    """Ce qui fait la prédiction : signe, valeur, métrique normalisée, seuil — et la loi engagée en sélection par pari."""
    pred = d.get("prediction") or {}
    loi = d.get("loi_predictive")
    return (pred.get("signe"), float(pred.get("valeur", 0.0)), normaliser_texte(d.get("metrique", "")),
            float(d.get("seuil", 0.0)), empreinte_objet(loi) if loi else None)


def brier(paires):
    """Score de Brier de prévisions p contre issues y ∈ {0, 1} : moyenne de (p − y)²."""
    paires = list(paires)
    if not paires:
        return None
    return sum((p - y) ** 2 for p, y in paires) / len(paires)


class Memoire:
    def __init__(self, active=True, seuil_redite=0.5, seuil_severe=0.05, nb_gabarits=3, longueur_lecon=1500):
        self.active = active
        self.seuil_redite = seuil_redite
        self.seuil_severe = seuil_severe
        self.nb_gabarits = nb_gabarits
        self.longueur_lecon = longueur_lecon
        self.index = {}
        self.lecons = []

    # --- (1) index de l'archive -------------------------------------------------------------------------------
    def indexer(self, fiche, issue, generation):
        code = issue.get("code") or {}
        entree = {
            "identifiant": fiche.identifiant, "enonce": fiche.enonce, "statut": fiche.statut,
            "verdict_declare": issue.get("verdict_declare"), "verdict_final": issue.get("verdict_final"),
            "motif": issue.get("motif"), "desaccord": bool(issue.get("desaccord")),
            "severite_attendue": fiche.severite_attendue,
            "aptitude": fiche.aptitude() if fiche.statut == "survit" else None,
            "prediction": fiche.prediction, "metrique": fiche.metrique, "seuil": fiche.seuil,
            "loi_predictive": fiche.loi_predictive,
            "protocole": fiche.protocole, "domaines": list(fiche.domaines), "operateurs": list(fiche.operateurs),
            "code": {"chemin": code.get("chemin"), "sha256": code.get("sha256")},
            "generation": generation, "source": issue.get("famille_source", fiche.famille_source()),
            "temoin": fiche.temoin is not None, "verite_temoin": fiche.temoin, "parents": list(fiche.parents),
        }
        self.index[fiche.identifiant] = caviarder_objet(entree)[0]
        return self.index[fiche.identifiant]

    def _entrees(self, temoins=False):
        return [e for _, e in sorted(self.index.items()) if temoins or not e["temoin"]]

    # --- (2) garde de redite ----------------------------------------------------------------------------------
    def chercher_redites(self, enonce):
        proches = []
        for e in self._entrees():
            if e["statut"] == "eliminee":
                j = jaccard(enonce, e["enonce"])
                if j >= self.seuil_redite:
                    proches.append((e["identifiant"], round(j, 4)))
        return sorted(proches, key=lambda x: (-x[1], x[0]))

    def garde_redite(self, fiche):
        """Une redite d'une éliminée est refusée, sauf si `ce_qui_change[id]` est rempli et que la prédiction diffère."""
        if not self.active:
            return {"accepte": True, "motif": "mémoire inactive", "proches": []}
        proches = self.chercher_redites(fiche.enonce)
        refus = []
        for ident, j in proches:
            justification = (fiche.ce_qui_change or {}).get(ident, "").strip()
            if not justification:
                refus.append(f"{ident} (jaccard {j}) : champ « ce qui change par rapport à {ident} » absent")
            elif signature_prediction(fiche.vers_dict()) == signature_prediction(self.index[ident]):
                refus.append(f"{ident} (jaccard {j}) : prédiction identique à celle de l'éliminée")
        if refus:
            return {"accepte": False, "motif": "redite d'une éliminée : " + " ; ".join(refus), "proches": proches}
        motif = "aucune éliminée proche" if not proches else "redite justifiée par une prédiction nouvelle"
        return {"accepte": True, "motif": motif, "proches": proches}

    # --- (3) bibliothèque de protocoles -----------------------------------------------------------------------
    def gabarits(self):
        severes = [e for e in self._entrees() if e["statut"] == "survit" and e["severite_attendue"] <= self.seuil_severe]
        severes.sort(key=lambda e: (e["severite_attendue"], e["identifiant"]))
        return [{"identifiant": e["identifiant"], "protocole": e["protocole"], "metrique": e["metrique"],
                 "severite_attendue": e["severite_attendue"]} for e in severes[:self.nb_gabarits]]

    # --- (4) registre de calibration --------------------------------------------------------------------------
    def registre_calibration(self):
        groupes = collections.defaultdict(list)
        for e in self._entrees(temoins=True):
            if e["statut"] in STATUTS_TRANCHES:
                groupes[e["source"]].append(e)
        registre = {}
        for source, entrees in sorted(groupes.items()):
            paires = [(e["severite_attendue"], 1.0 if e["statut"] == "survit" else 0.0) for e in entrees]
            nulles = [p for p, e in zip(paires, entrees) if e["verite_temoin"] == "fausse"]
            survie = sum(y for _, y in paires) / len(paires)
            moyenne = sum(p for p, _ in paires) / len(paires)
            registre[source] = {
                "nombre_de_fiches": len(paires), "brier": brier(paires), "severite_annoncee_moyenne": moyenne,
                "survie_observee": survie, "exces_de_survie": survie - moyenne,
                "nombre_sous_nul_connu": len(nulles), "brier_sous_nul_connu": brier(nulles),
            }
        return {"par_source": registre,
                "lecture": ("Brier de la sévérité annoncée (probabilité de survie sous le nul) contre la survie observée. "
                            "Sous un nul connu (témoins faux), c'est une mesure de calibration ; ailleurs, l'écart mêle "
                            "calibration et proportion d'hypothèses vraies : seuls les témoins tranchent.")}

    # --- (5) leçons de génération -----------------------------------------------------------------------------
    def resume_pour_synthese(self, generation):
        entrees = [e for e in self._entrees() if e["generation"] <= generation]
        motifs = collections.Counter(e["motif"] or "?" for e in entrees if e["statut"] != "survit")
        par_domaine = collections.defaultdict(lambda: [0, 0])
        for e in entrees:
            if e["statut"] in STATUTS_TRANCHES:
                for d in e["domaines"]:
                    par_domaine[d][0] += e["statut"] == "eliminee"
                    par_domaine[d][1] += 1
        return {
            "generation": generation,
            "comptes_par_statut": dict(collections.Counter(e["statut"] for e in entrees)),
            "causes_frequentes": motifs.most_common(5),
            "elimination_par_domaine": {d: {"eliminees": v[0], "tranchees": v[1]} for d, v in sorted(par_domaine.items())},
            "protocoles_qui_ont_fonctionne": self.gabarits(),
            "desaccords_experimentateur_verificateur": sum(e["desaccord"] for e in entrees),
            "redites_refusees": sum(e["statut"] == "refusee (redite)" for e in entrees),
        }

    def ajouter_lecon(self, generation, texte):
        propre = caviarder(str(texte))[0].strip()[:self.longueur_lecon]
        self.lecons.append({"generation": generation, "texte": propre})
        return propre

    def derniere_lecon(self):
        return self.lecons[-1] if self.lecons else None

    def texte_consigne(self, role):
        """Ce que la mémoire sert à un agent : gabarits (expérimentateurs) et dernière leçon (tous)."""
        if not self.active:
            return ""
        morceaux = []
        if role == "experimentateur":
            gabarits = self.gabarits()
            if gabarits:
                lignes = [f"- [{g['identifiant']}] sévérité annoncée {g['severite_attendue']} ; métrique : {g['metrique']} ; "
                          f"protocole : {g['protocole']}" for g in gabarits]
                morceaux.append("Gabarits de protocoles ayant survécu à un test sévère :\n" + "\n".join(lignes))
        lecon = self.derniere_lecon()
        if lecon and role in ("experimentateur", "recombinaison"):
            morceaux.append(f"Leçons de la génération {lecon['generation']} :\n{lecon['texte']}")
        return "\n\n".join(morceaux)

    def instantane(self):
        return {"active": self.active, "seuil_redite": self.seuil_redite, "seuil_severe": self.seuil_severe,
                "index": self.index, "lecons": self.lecons, "gabarits": self.gabarits(),
                "calibration": self.registre_calibration()}
```

<<<FIN M1>>>

<<<DÉBUT M2 — LISEZMOI de l'orchestrateur v0, section « Démonstrations (simulation) », qui porte l'ablation de la mémoire (extrait, lignes 112 à 127, de `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/orchestrateur-v0/LISEZMOI-orchestrateur-v1.md`, sha256 `39101ffb8e4404fc7a5dafea4f4d80ad841e9c87a4c359323bf103c6f97db481`)>>>

## Démonstrations (simulation)

- `demo/demonstration-v1/` (mode seuil ; trois générations ; six fiches ; `bilan.json` `149239de…`) : 3 témoins faux testés,
  aucun gardé ; 4 vrais, aucun éliminé ; tricheurs vus (verdict sans calcul → indécise, test changé → rejetée) ; une fiche
  retirée après deux essais indécis ; filtre de compatibilité actif (« discret » contre « continu ») ; 8,6 dollars simulés.
- `demo/demonstration-pari-v1/` (mode pari ; trois générations ; `bilan.json` `1c6838c2…`) : lancé **sans tricheurs** pour
  montrer les filles jugées contre le nul augmenté (gains 0,19, 0,61, 0,17 nat pour les promues, −0,44 pour une éliminée) ;
  deux redites refusées par la mémoire ; témoins : 0 faux gardé, 0 vrai éliminé.
- `demo/ablation-memoire-v1/` (20 graines appariées, trois générations ; `comparaison-memoire-v1.json` `91b5742b…` ; archives
  brutes zippées `archives-par-graine-v1.zip` `34e6a312…`) : une seule redite d'éliminée proposée sur 26 fiches nouvelles ;
  testée sans mémoire, refusée avec ; témoins identiques dans les deux bras ; la mémoire coûte l'agent de synthèse (152,7
  contre 150,8 dollars simulés). **Aucune conclusion** : les agents simulés ne lisent pas la mémoire, l'écart ne mesure que
  le mécanisme, et l'effectif de redites est trop petit.
- Les populations de démonstration ont été retouchées (opérateurs partagés) pour que la recombinaison ait des ponts ; ce sont
  des illustrations de mécanique, pas des mesures.

<<<FIN M2>>>

<<<DÉBUT J — note du juge v1 (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/experience-1-juge/conception-experience-1-juge-v1.md`, sha256 `560f4a4cd985f28f2a9fcb838644c2dab62c81d983a5d255e4fe84eb07f1a217`)>>>

# Conception de l'expérience 1 du pôle — le juge v1 contre la dérive non modélisée — v1 (note de conception, pas un préenregistrement)

Écrite par la lignée conv-audit le 27 octobre 2026, à partir de 06:37 UTC (heure lue sur `date -u`), juste avant la
passation de la lignée à une instance nouvelle sur un autre compte (mot de Lazar, 07:33 heure de Paris). **Rien de ce qui
suit n'est codé ni exécuté** : c'est l'analyse et le plan, pour que l'instance nouvelle code, préenregistre et livre sans
refaire le raisonnement. Mode exploratoire (R-522) ; R1 et R3 gardées pour l'expérience elle-même.

## 1. Le défaut à corriger (orchestrateur v0)

Le juge v0 (`orchestrateur-v0/pole/selection_pari.py`) promeut une fiche si la richesse
W_t = Π_{s≤t} p_h(x_s) / max_{q∈𝓛} Π_{s≤t} q(x_s) atteint 1/α à un instant quelconque (inférence universelle ; inégalité
de Ville). 𝓛 = prédicteurs aveugles au domaine : marginale ajustée sur les tirages frais, uniforme, moyennes glissantes
(fenêtres 5, 10, 20, 50). Le nul visé est « les traits des instances n'apprennent rien sur les issues » (issues
indépendantes des traits). Contrôle T1b de v0 (`demo/experience-critere-v1/controles-fatals-v1.json`, `2b86b37f…`) : dans
un monde où la marginale dérive linéairement dans le temps (K = 3 issues, 200 tirages), une loi **aveugle** qui connaît la
dérive est promue **652 fois sur 1 000** (α = 0,05). Le nul composite contient toutes les structures temporelles
(dérive, rupture, autocorrélation, calendrier) ; 𝓛 n'en couvre que quelques-unes. Ajouter des familles de dérive
(logit linéaire, une rupture) ne fait que déplacer le trou : une sinusoïde, une marche aléatoire ou un calendrier
déterministe y échappent.

## 2. La correction proposée : ordre d'exécution secret et membre « urne »

1. **Ordre d'exécution tiré au hasard, après le gel.** L'orchestrateur tire une permutation π (graine dérivée d'une
   graine maîtresse **tenue par le noyau**, jamais dans la vue d'un agent, et de l'empreinte de l'engagement gelé) ; le
   monde (l'expérience) traite les instances du plan dans l'ordre π ; chaque issue est rangée à l'indice de son instance
   dans le plan ; l'évaluation se fait dans l'ordre du plan. Sous le nul (issues indépendantes des traits, structure
   temporelle quelconque), la suite des issues dans l'ordre du plan est **échangeable et indépendante des traits**.
   - **Pourquoi pas permuter seulement l'ordre d'évaluation** : le plan d'instances est dans l'engagement ; permuter les
     couples (instance, issue) révèle la permutation par les instances elles-mêmes ; une loi peut alors retrouver l'heure
     de chaque instance et exploiter la dérive. Seul l'ordre d'**exécution** convient.
2. **Membre « urne » dans 𝓛** : le maximum, sur toutes les lois échangeables, de la probabilité des t premières issues,
   soit Π_k c_k(t)! / t! (c_k(t) : nombre d'issues k parmi les t premières). La loi vraie sous le nul étant échangeable,
   le dénominateur la domine à chaque instant ; W_t est donc majorée par un rapport de vraisemblance à la loi vraie,
   martingale positive d'espérance 1 ; Ville donne P(sup_t W_t ≥ 1/α) ≤ α, **exactement, sans modéliser la dérive**.
   - **Pourquoi l'urne est nécessaire** : une loi aveugle qui connaît la composition exacte des issues (calendrier
     déterministe) prédit « sans remise » ; son gain sur la marginale ajustée vaut
     ½(K−1)·ln 2π + ½ Σ_k ln c_k − ½ ln n, soit **≈ 5,5 nats** pour K = 3 et n = 200 (composition égale), au-dessus du seuil
     ln 20 ≈ 3,0 : sans urne, elle serait promue presque toujours, même avec l'ordre secret. Avec l'urne, sa richesse
     reste ≤ 1. Pour une dérive aléatoire (tirages indépendants, comme le monde de T1b), le gain est faible (de l'ordre du
     dixième de nat).
   - **Coût** : l'urne dépasse la marginale ajustée d'environ 5,5 nats (n = 200, K = 3) : perte de puissance sur les
     petits effets ; les grands effets n'y perdent presque rien (leur gain croît comme n).
3. **Exigences** : l'heure d'exécution n'est jamais un trait d'instance ; l'engagement déclare le plan d'exécution
   (« ordre secret ») ; l'évaluateur refuse des issues produites sous un autre plan (garde essayée sur un cas sain et sur
   un artefact, R5) ; en exécution réelle, c'est le noyau qui impose l'ordre (il appelle l'expérience instance par
   instance, ou vérifie l'ordre par les horodatages) ; un agent qui ignorerait l'ordre rendrait la garantie caduque.
4. **Limites** : (a) si les traits d'une instance se mesurent au moment de l'exécution (état d'un modèle qui change), le
   temps fuit dans les traits et le nul « issues indépendantes des traits » n'est plus celui qu'on croit ; (b) le nul
   augmenté des filles (parents, mélanges, enveloppes) n'est qu'approché sous dérive (la loi vraie devient un mélange
   moyenné dans le temps ; les membres « parent mélangé à une loi aveugle » l'approchent) : à contrôler (T1b-fille).

## 3. L'expérience 1 à préenregistrer (proposition)

- **Juge v1** = v0 + ordre d'exécution secret + urne (autres membres inchangés). Dossier neuf (`orchestrateur-pole-v2`) ;
  v0 jamais écrasé (R12).
- **Contrôles fatals** (chacun ≤ α ; 1 000 répétitions ; 200 tirages frais ; K = 3 ; dimension 2 ; α = 0,05 ; borne de
  Wilson rapportée) : T1a (trois nuls), T6, les sept tricheurs, T3 composante nette fausse, T9 ; **batterie T1b** : loi
  aveugle « calendrier » (connaît p_t) et loi aveugle « composition » (sans remise) sous six structures absentes de 𝓛 —
  dérive linéaire (celle de v0), rupture à n/2, sinusoïde (période n/3), marche aléatoire des logits (écart 0,15 par pas),
  calendrier déterministe par blocs, monde auto-excité (moyenne glissante de fenêtre 10, ou renforcement de Pólya) ;
  **T1b-fille** : fille = parent + connaissance de la dérive, monde = parent + dérive, contre le nul augmenté.
- **Artefacts, qui doivent être vus** (taux > α ; sinon le contrôle n'a pas de dents, R5) : juge v0 (ordre naturel, sans
  urne) sur la batterie (au moins la dérive linéaire, 652/1 000 connu) ; juge v1 **sans urne** sous calendrier déterministe
  avec la loi « composition » (prédit ≥ 0,9) ; facultatif : permutation de l'ordre d'évaluation au lieu de l'ordre
  d'exécution, avec une loi qui retrouve l'heure par l'instance (prédit élevé).
- **Puissance** (rapportée ; lecture minimale gelée) : fille réellement neuve ≥ 0,90 (v0 : 0,993) ; T3 composante nette
  vraie ε = 0,2 ≥ 0,90 (v0 : 0,996), ε = 0,05 rapportée (v0 : 0,913) ; loi de domaine vraie tirée au hasard ; loi vraie +
  dérive.
- **Prédictions signées** : tous les contrôles fatals ≤ α sous v1 (attendu bien en dessous, Ville étant conservatrice) ;
  artefacts vus ; perte de puissance sur la fille neuve ≤ 0,05.
- **Lecture** : juge v1 adopté pour le pôle si tous les contrôles fatals passent et si la puissance sur la fille neuve
  est ≥ 0,90 ; sinon non adopté (et l'on dit ce qui a cédé). Les deux sens sont lus (R3, R4).
- **Graines** : graine maîtresse neuve tirée au scellement (pas 20261026, celle de l'exploration v0) ; un pilote de
  conception sur une autre graine, s'il est fait, est déclaré dans le texte (R-473).
- **Qui** : l'instance nouvelle de conv-audit code et essaie, écrit le préenregistrement court, le fait contre-lire par un
  sous-agent neuf ; session-depot scelle avant lecture (R1), exécute sur processeur — **voie (c), purement synthétique :
  aucune activation, GO-2026-10-26-08 inutile pour cette expérience** —, fait contre-lire (R2) et rend le résultat.
- **Ce qu'elle ne dit pas** : des mondes simulés ; ni agents réels ni données réelles. Ensuite : relais de clé tenu par
  le noyau, une génération réelle de deux fiches, témoins sur données réelles (par exemple la rétrodiction arXiv, où les
  issues des paires sont échangeables par tirage et la vérité connue après coup).

## 4. Plan de code (pour l'instance nouvelle)

- `selection_pari.py` : loi `sans_remise` (composition déclarée ; p_k = (c_k − vus_k)/(n − t), plancher) ; membre
  `urne` (trajectoire Σ_k ln c_k(t)! − ln t!, par `math.lgamma`) ; `construire_engagement(..., plan_execution)` ;
  `tirer_frais(..., plan_execution="ordre_secret")` (le monde voit z_π(t), son propre passé dans l'ordre du temps, et t ;
  issues rangées par indice du plan ; empreinte de π consignée, π recalculable par le noyau) ; `evaluer` refuse un plan
  d'exécution non déclaré ; `BIBLIOTHEQUE_STANDARD_V1` = v0 + urne.
- `controles_pari.py` (nouveau nom de version, ou module `controles_pari_v1.py`) : lois de monde « calendrier » (un
  vecteur de probabilités par instant, tiré d'avance) et « déterministe » ; batterie T1b, T1b-fille, artefacts, puissance.
- Essais : trajectoire de l'urne contre une énumération exhaustive pour n ≤ 6 ; placement des issues par indice du plan ;
  garde de refus (cas sain et artefact) ; essai de fumée de validité à peu de répétitions, sur une graine distincte de
  celle de l'expérience.

<<<FIN J>>>

<<<DÉBUT G1 — génération 0 : synthèse (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/generation-0/synthese-generation-0-v1.md`, sha256 `51a32aec567842d4a41fa59290f04478bac9213070180c83b769219c18d2303c`)>>>

# Pôle scientifique automatique — synthèse de la génération 0 (les hypothèses de l'organisme sur sa propre structure, testées) — v1

De : conv-audit, le 2026-10-26 18:13:27 UTC. Génération 0 : les affirmations du rapport de méta-conception v6.3 de l'essaim de Gemini
(`96d12112…`) testées par calcul indépendant, sur processeur, par deux expérimentateurs (brique 1 : `5b7011b1…` ; briques
2 à 4 : `929cbc32…`), runs déterministes relancés. Régime exploratoire (R-522), non opposable. **Pas encore vérifié par un
agent d'une autre famille** (étape suivante du pôle).

## Verdict

Sur dix-huit affirmations testées : **cinq survivent, dix sont éliminées, trois indécises.** Les deux briques
« mathématiquement fondées » du rapport (le noyau de tirage, la répulsion sur graphe de ligne) **tombent** ; les deux
idées qui survivent sont des correctifs, dont l'un est le mien et l'autre le contraire de ce que j'avais écrit. Surtout,
**le rapport décrit un code qui n'existe pas** : ni `_score_pertinence_texte`, ni la décomposition de Cholesky, ni le
log-déterminant qu'il prétend réutiliser ne sont dans la v6.2.1 — la refonte est bâtie sur une lecture fausse du code.

## Ce qui survit (à réutiliser dans le pôle)

- **La mémoire spectrale actuelle est aveugle aux textes réels** (rappel du plus proche voisin 0,000, hasard 0,038 ;
  accord 0,014). Vrai défaut, à corriger.
- **Normaliser la somme des hachages avant le relèvement** : meilleur gain mesuré (rappel +0,135 ; accord 0,014 → 0,48
  sur 27 textes réels).
- **SimHash sur n-grammes** préserve la morphologie au niveau du mot (aire 0,987 contre 0,458) ; indécis au niveau du
  texte.
- **Le correctif du noyau de tirage** (diversité de domaine dans le noyau, pertinence dans la qualité, opérateur
  réintroduit après tirage) : diversité 0,90 à 0,95 pour un hasard de 0,74, qualité gardée, pas de dégénérescence.
- **Le filtre de compatibilité des contraintes** : utile (fusions contradictoires 57 % → 0 % sur lexique propre), mais
  fragile sur du bruit réaliste (57 % → 34 %, rappel 0,61) ; à garder, à ne pas surestimer.

## Ce qui est éliminé

- Le noyau « PSD par produit de Schur » du rapport : **1 000 violations sur 1 000** (λ_min médian −0,715) ; réparé par
  γ ≥ 0,37, il repousse justement les paires qu'il visait.
- L'égalité « trace = 1 − ⟨d,d⟩² » : fausse (la trace vaut 14 + ⟨d,d⟩²) ; la forme trace récompense la similarité de
  domaine.
- « La répulsion détruit les pivots de Swanson » : réfutée sur l'organisme réel (les termes saturés de la génération 18
  sont des mots-outils, aucun pivot) ; le graphe de ligne proposé coûte C(d_B, 2) et bloque 78 % des ponts.
- Le diagnostic « v² écrase par explosion de variance » (σ1 est une direction moyenne, pas une variance) ; « Koopman sur
  bruit blanc amplifie la variance isotrope » ; « SHA-256 maximalement non informatif » ; le protocole P1 (un encodage
  nul le passe à 100 %) ; le critère d'arrêt par convergence du spectre (absent du code) ; mon propre correctif de
  recentrage (sans effet) ; le rang effectif 1,82 annoncé (vrai : 3,96).

## Ce que la génération 0 établit pour le choix du moteur

- La voie « perfectionner notre organisme » part d'une **refonte fausse sur le code** : à refaire sur le vrai code, avec
  les deux correctifs survivants seulement. Le moissonnage et le tri réels de la v6.2.1 ne sont pas ceux que le rapport
  décrit — à relire avant toute conception.
- La génération 0 a coûté 0 dollar (processeur) et a éliminé dix affirmations sur dix-huit par des tests qui pouvaient
  échouer : c'est le mode de fonctionnement visé pour le pôle.

## Suite

1. Vérification de ces verdicts par un agent neuf d'une autre famille (étape « vérificateur » du pôle).
2. Relecture v2 pour Gemini (corrigée par ces essais, mes erreurs comprises), sur une branche à part ; Lazar la lui
   transmet.
3. Génération 1 : recombinaison des cinq survivants en fiches filles + témoins plantés, dans l'orchestrateur du pôle.

<<<FIN G1>>>

<<<DÉBUT G2 — génération 0 : essais de la brique 1 (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/generation-0/brique1/essais-brique1-spectre-v1.md`, sha256 `5b7011b10db0edd5f2dfb0bbbc7a5079421aa9c0ef044b318e8a9efae527c39c`)>>>

# Essais de la brique 1 de la méta-conception : encodage et mémoire spectrale (v1)

Lignée conv-audit, sous-agent. Horodatage (temps universel) : 2026-10-26T18:04:39Z.
Travail sur processeur seul, bibliothèque standard de Python, sans réseau ni dépôt ; Python lancé avec `-I -B`.
Statut : essais **exploratoires, non préenregistrés**. Ils servent à juger les affirmations du rapport et à écrire un protocole qui, lui, devra être scellé (R1) et contre-lu (R2) avant d'être lancé. Aucun chiffre ici n'est un résultat décisif.

## Verdict

- **Diagnostic du rapport : partiel.** Le terme v² porte 97,7 % de l'énergie des vecteurs relevés réels, et les cinq premières directions propres vivent à 98 % ou plus sur les cinq coordonnées carrées. Mais σ1 n'est pas une « variance qui explose » : c'est la direction moyenne commune des carrés (toujours positifs), qui explique 98 % de σ1. Le code normalise déjà chaque vecteur en sortie. Le rapport σ1/σ6 = 60,96 se factorise en 5,41 (effet de moyenne, σ1/σ5) × 11,28 (effet d'échelle carrés/linéaires, σ5/σ6), et le second croît avec le nombre de jetons.
- **Remède (ii), normaliser la base avant relèvement : partiel, et c'est le meilleur levier d'information.** Le rappel du plus proche voisin gagne +0,135 [0,114 ; 0,156] sur 180 corpus. La corrélation avec l'étalon passe de 0,37 à 0,60, et de 0,014 à 0,48 sur le corpus réel. σ1/σ6 baisse fortement : de 76,5–94,6 à 9,1–9,4 à 50 cycles quand le vocabulaire partagé reste à 30 % ou moins, et d'un facteur 35 en moyenne sur les corpus statiques. Il ne passe pourtant sous 12 que dans 17 % des corpus statiques, et vaut encore 18,1 à 50 cycles avec 60 % de vocabulaire partagé.
- **Centrage (iii) seul : insuffisant.** σ1/σ6 ne passe jamais sous 12 (22 à 3664 en statique ; moyennes de 27 à 31 en générations, aucun flux sous 12). L'information est inchangée : −0,007 [−0,015 ; 0,002]. Combiné à (ii), le centrage passe le seuil dans 30 flux sur 30, sans aucune information supplémentaire.
- **SimHash : gain établi au niveau du mot, par construction ; indécis au niveau du texte.**
  - Mot : aire sous la courbe 0,987 contre 0,458 pour SHA-256, mais seulement 0,870 face aux mots de même suffixe.
  - Texte : +0,025 en synthétique, +0,083 avec flexions, −0,148 sur le corpus réel.
  - Spectre : le remède complet SimHash + normalisation échoue à P1 (14,1 à 17,0 à 50 cycles, 0 flux sur 30 sous 12).
- **P1 : non valide comme test.** Il peut échouer, mais pour de mauvaises raisons :
  - l'encodage nul, sans aucune information, le passe dans 100 % des cas ;
  - les corpus les mieux encodés l'échouent ;
  - avec centrage, il est acquis d'avance dans le régime de l'organisme.

  Une version qui peut échouer est proposée au § 5.

## 1. Cadre et entrées

- J'ai lu `fournis/organisme/` : `memoire_isvd.py` en entier, le § 2.11 de `CONCEPTION.md`, et dans `principal.py` les passages sur les traces et sur l'arrêt (lignes 872 à 935, 1310 à 1325, 1380 à 1392, 1845 à 1860, 1925 à 1960, 1990 à 2150). J'ai aussi lu `fournis/rapport-meta-conception.md` en entier et `fournis/memoire-isvd-gen18.json`.
- J'ai écrit uniquement sous `sortie/`.
- Empreintes SHA-256 des entrées :
  - `fournis/organisme/memoire_isvd.py` : `e39295c5d3d04a45ef3024347bf30ee6744aee88fd77ea058e2c8f231f3e1710`. La copie `sortie/organisme_copie/memoire_isvd.py` est identique (vérifié).
  - `fournis/memoire-isvd-gen18.json` : `4866918f475555cef7ad2fae2ed05a1a855f54239741bcf187f1cd24ef7b0857`.
  - `fournis/rapport-meta-conception.md` : `96d12112c8d8d7e376943fa42fc0a4d6faed52b7ed09ae9ecac981c65949c6cf`.
- Chaque chiffre ci-dessous provient de `sortie/resultats/*-v1.json`. Les tableaux complets sont regénérés par `lire_resultats_v1.py` dans `resultats/tableaux-v1.md`, qui donne l'empreinte de chaque fichier lu.

## 2. Méthode

### 2.1 Encodages et variantes

Variantes demandées :

- **(i) Code tel quel.** `extraire_vecteur_koopman` : la base est la somme des SHA-256 par jeton ; le relèvement applique v, sin v ou v² selon l'indice modulo 3 ; la norme vaut 1 en sortie.
- **(ii) Remède du rapport.** La base est ramenée à norme 1 avant le relèvement ; relèvement et normalisation sont ensuite inchangés.
- **(iii) Centrage.** Encodage (i), mais la moyenne pondérée des exemplaires est retranchée avant le spectre.
- **(iv)** (ii) et (iii) combinés.

Variantes de référence ajoutées :

- **(v)** SimHash sur 3-grammes de caractères (projection), normalisé puis relevé : c'est le remède complet du rapport, appliqué au texte entier.
- **(vi)** (v) et centrage.
- **v_bin, vi_bin** : version binaire de SimHash.
- **« nul »** : une direction aléatoire par texte (graine tirée du SHA-256 du texte). Il ne porte aucune information.
- **« base »** : base SHA-256 normée, sans relèvement. Elle montre l'information disponible avant le relèvement.

Définition du SimHash :

- On découpe en 3-grammes chaque jeton bordé par « # ».
- La coordonnée i (de 0 à 15) d'un 3-gramme g vaut +1 si le bit i des 32 premiers bits de SHA-256(« brique1-simhash3-v1| » + g) vaut 1, et −1 sinon.
- La projection est la somme des vecteurs de signes ; la version binaire en prend le signe.
- La table effectivement utilisée est consignée dans `resultats/table-signes-simhash-essai3-v1.tsv` (345 3-grammes).

Tokeniseur : c'est celui de l'organisme, soit `[a-zA-Z0-9_\\]+` sur le texte en minuscules. Les lettres accentuées coupent donc les mots : « évaluation » devient « valuation ».

### 2.2 Mémoire

- **Statique.** On décompose Σ w ψψᵀ (ou la dispersion centrée) d'un corpus de deux façons : par le Jacobi du code (120 itérations) et par un Jacobi cyclique mené à convergence. Les rapports cités sont ceux de la décomposition exacte, sauf mention contraire.
- **Générations.** 50 générations de 40 traces, avec la construction de l'organisme : m = U Σ Uᵀ + Σ w ψψᵀ, troncature au rang 6, Σ arrondi à 6 décimales. On garde la version du code et la version exacte.
  - Pour (i), l'appel direct à `mettre_a_jour_memoire_isvd` et le chemin du pilote donnent des Σ **identiques bit à bit** sur les 30 flux.
  - Les variantes centrées gardent la moyenne courante et le poids total, et mettent à jour la dispersion par la formule des axes parallèles. Sans troncature, cette mise à jour égale le calcul d'un bloc à 1,4·10⁻⁶ près, écart dû à l'arrondi de Σ.

### 2.3 Corpus

- **Synthétiques.**
  - Vocabulaires : 5 domaines de 50 mots, 40 mots-outils, 30 mots de méthode. Les listes sont disjointes (vérifié). Tirage selon une loi de Zipf d'exposant 1.
  - `p_commun` est la part des jetons tirés du vocabulaire partagé (2/3 de mots-outils, 1/3 de mots de méthode). 20 % des textes sont des ponts entre deux domaines. Les poids sont uniformes sur [0,6 ; 0,9].
  - Grille statique : N ∈ {12, 25, 50} × p_commun ∈ {0 ; 0,3 ; 0,6} × 20 graines, soit 180 corpus de 30 à 300 jetons.
  - Régime générationnel : 20 à 100 jetons et 10 graines par niveau de vocabulaire partagé. Repères réels : les 27 textes réels ont 16 à 82 jetons, et les 40 mots-outils font 24,5 % des jetons des 12 exemplaires réels.
- **Réel d'ancrage.** 27 textes : les 12 exemplaires uniques du json et les 15 références moissonnées citées au § 3 du rapport. Réserve : ces 12 exemplaires sont ceux que la mémoire a retenus, donc les plus alignés sur u1.

### 2.4 Mesure d'information (fixée avant les essais 2 à 5)

- **Rappel au premier rang (noté R@1), mesure principale.**
  - Pour chaque texte i, on cherche son plus proche voisin par cosinus dans l'espace de la variante : ψ pour (i), (ii) et (v) ; ψ − μ pour (iii), (iv) et (vi).
  - C'est un succès si ce voisin appartient à l'ensemble des plus proches voisins de i par similarité de Jaccard des ensembles de jetons, ex aequo compris.
  - Le niveau du hasard est la moyenne de |étalon|/(N − 1).
  - On la calcule aussi sur les coordonnées de rang 6, c'est-à-dire ce que garde la mémoire.
- **Mesure secondaire.** Corrélation de rang de Spearman, sur toutes les paires, entre cosinus et Jaccard (ci-dessous « Spearman »).
- **Garde testée sur un cas sain et sur un artefact (R5).** Sacs de mots complets : R@1 = 0,88 (hasard 0,021). Encodage nul : R@1 = 0,02.
- **Graines.** On utilise `random.Random(graine)`, le même générateur que `random.seed`. La graine est formée des 8 premiers octets de SHA-256(« 20261026|tâche|indices »). La règle et la graine maîtresse sont consignées dans chaque manifeste de résultat.

## 3. Résultats

### Essai 1 — forme du spectre et origine

**Spectre réel** (json, génération 18) :

- σ1/σ6 = 60,963. Le rapport écrit 60,9, par troncature ; l'arrondi donne 61,0.
- σ1/σ5 = 5,406 et σ5/σ6 = 11,276.
- Part de chaque vecteur propre sur (linéaires ; sinus ; carrés) :
  - u1 : (0,02 ; 0 ; 0,98) ;
  - u2 à u5 : (0 ; 0 ; 1,00) ;
  - u6 : (0,99 ; 0 ; 0).
- Les composantes de u1 sur les cinq carrés sont toutes positives : 0,51 ; 0,37 ; 0,57 ; 0,39 ; 0,33.
- Les coordonnées sinus sont absentes des six directions.
- Sur les 12 exemplaires réels, 97,7 % de |ψ|² est sur les carrés, et ⟨ψ, u1⟩ vaut 0,922 en moyenne (minimum 0,895).

**Reproduction** :

- En générations (18 cycles de 40 traces), σ1/σ6 vaut 74,6 ± 12,0, 93,9 ± 16,0 et 89,7 ± 7,3 pour p_commun = 0 ; 0,3 ; 0,6. C'est le même ordre de grandeur que 61.
- La somme des σ vaut 532 à 533, contre 513 dans le json.
- La structure propre est la même : u1 à u5 sont à 0,99 ou plus sur les carrés, u6 à 0,98 ou plus sur les linéaires.
- Sur le corpus réel d'ancrage, traité en un seul lot, σ1/σ6 = 84,7.

**Origine 1 : la direction moyenne.**

- Part de σ1 portée par la moyenne, W‖μ‖²/σ1 :
  - 0,980 sur le corpus réel ;
  - 0,976 sur les 180 corpus statiques ;
  - 0,960 à 0,981 en générations.
- Quotient de Rayleigh μ̂ᵀMμ̂/σ1 : 0,9993 sur le réel, 0,997 en statique.
- |⟨u1, μ̂⟩| : 0,9996 sur le réel, 0,997 à 0,999 en générations.
- ⟨ψ, μ̂⟩ moyen : 0,830 sur le réel ; de 0,53 (3 jetons) à 0,81 (300 jetons).
- Réserve sur l'expression « quasi rang 1 » du brief : σ1 ne porte que 52 % de la trace réelle (rang effectif 3,96). σ2 à σ5 sont la variance des carrés autour de leur moyenne.

**Origine 2 : l'effet d'échelle.** Balayage en longueur (N = 50, p_commun = 0,3, 10 graines, encodage (i)) :

| jetons | part des carrés dans ψ | σ1/σ6 | σ1/σ5 | σ5/σ6 |
|---|---|---|---|---|
| 3 | 0,521 | 4,9 | 4,2 | 1,2 |
| 10 | 0,805 | 10,7 | 7,1 | 1,5 |
| 30 | 0,950 | 38,5 | 9,6 | 4,1 |
| 60 | 0,984 | 122,1 | 11,9 | 11,2 |
| 100 | 0,994 | 380,3 | 16,6 | 23,0 |
| 300 | 0,9996 | 6063 | 28,5 | 226,0 |

- σ5/σ6 (carrés contre linéaires) croît comme le nombre de jetons. σ1/σ5 (moyenne contre variance des carrés) croît lentement.
- Les deux hypothèses du brief sont confirmées : (a) l'échelle de la base, (b) la direction commune des carrés.

**Information sous (i).**

- Sur le corpus réel, R@1 = 0,000 (hasard 0,038) et Spearman = 0,014.
- La base SHA-256 avant relèvement garde pourtant Spearman = 0,570 et R@1 = 0,148.
- C'est donc le relèvement non normalisé qui efface la similarité, pas le hachage.

### Essai 2 — quatre variantes, mêmes corpus, mêmes graines

**180 corpus statiques** (30 à 300 jetons ; hasard de R@1 : 0,056) :

| variante | σ1/σ6 moyen [min ; max] | part ≤ 12 | R@1 | R@1 rang 6 | Spearman | Spearman rang 6 |
|---|---|---|---|---|---|---|
| (i) code | 848 [30 ; 14042] | 0 | 0,224 | 0,221 | 0,369 | 0,368 |
| (ii) base normée | 24,0 [7,2 ; 93,9] | 0,17 | 0,359 | 0,346 | 0,599 | 0,595 |
| (iii) centrage | 284 [22 ; 3664] | 0 | 0,217 | 0,216 | 0,345 | 0,344 |
| (iv) (ii) + (iii) | 12,3 [3,3 ; 65,3] | 0,60 | 0,362 | 0,353 | 0,543 | 0,544 |
| (v) SimHash | 31,7 [8,8 ; 84,0] | 0,01 | 0,383 | 0,373 | 0,580 | 0,577 |
| (vi) SimHash centré | 18,5 [5,0 ; 77,9] | 0,29 | 0,384 | 0,367 | 0,559 | 0,560 |
| nul | 2,4 [1,5 ; 4,5] | 1,00 | 0,059 | 0,055 | −0,003 | −0,002 |
| base sans relèvement | 23,4 [8,2 ; 81,3] | 0,11 | 0,381 | 0,362 | 0,621 | 0,616 |

Différences appariées de R@1, avec intervalle à 95 % par rééchantillonnage (n = 180) :

- (ii) − (i) = +0,135 [0,114 ; 0,156] ;
- (iii) − (i) = −0,007 [−0,015 ; 0,002] ;
- (iv) − (i) = +0,138 [0,117 ; 0,159] ;
- (iv) − (ii) = +0,003 [−0,005 ; 0,012].

**50 cycles (P1 au pied de la lettre)** : σ1/σ6 à la génération 50, et nombre de flux sous 12 sur 10 :

| variante | p_commun 0 | p_commun 0,3 | p_commun 0,6 |
|---|---|---|---|
| (i) | 76,5 (0/10) | 94,6 (0/10) | 89,8 (0/10) |
| (ii) | 9,1 (10/10) | 9,4 (10/10) | 18,1 (0/10) |
| (iii) | 26,9 (0/10) | 31,0 (0/10) | 27,2 (0/10) |
| (iv) | 8,9 (10/10) | 4,8 (10/10) | 2,7 (10/10) |
| (v) SimHash + normalisation | 15,5 (0/10) | 14,1 (0/10) | 17,0 (0/10) |
| (vi) | 14,2 (0/10) | 9,3 (10/10) | 4,4 (10/10) |
| nul | 1,2 (10/10) | 1,2 (10/10) | 1,2 (10/10) |

**Corpus réel d'ancrage** (27 textes ; hasard de R@1 : 0,038) :

| variante | σ1/σ6 | R@1 | Spearman |
|---|---|---|---|
| (i) | 84,7 | 0,000 | 0,014 |
| (ii) | 6,27 | 0,222 | 0,479 |
| (iii) | 13,85 | 0,037 | 0,003 |
| (iv) | 3,41 | 0,222 | 0,278 |
| (v) | 5,45 | 0,074 | 0,198 |
| nul | 2,10 | 0,000 | −0,024 |
| base | 5,39 | 0,148 | 0,570 |

Lecture :

- **(ii)** fait disparaître l'effet d'échelle. La part des carrés dans ψ tombe de 98 % à 11 % (60 jetons). σ5/σ6 à la génération 18 passe de 7,1–10,2 à 1,2–3,6. L'information est rendue : Spearman 0,60, contre 0,62 pour la base nue.
- Sous (ii), la direction commune persiste : W‖μ‖²/σ1 vaut 0,87 en statique et 0,65 à 0,97 en générations. σ1/σ6 dépasse donc 12 dès que le vocabulaire partagé ou la longueur augmentent : 18,1 à p_commun = 0,6, 34,3 à 300 jetons.
- **(iii)** retire la direction moyenne : |⟨u1, μ̂⟩| passe de 0,998 à 0,18 en statique. Il ne retire pas l'effet d'échelle : u1 à u4 restent sur les carrés. Aucun gain d'information.
- **(iv)** aplatit le spectre sans gagner d'information sur (ii). Spearman baisse même : 0,543 contre 0,599, et 0,278 contre 0,479 sur le réel. L'étalon de Jaccard contient en effet le recouvrement des mots-outils, que le centrage retire.

### Essai 3 — SimHash contre SHA-256 par jeton

On compare trois familles de 30 paires :

- **fléchies** : spectral/spectrale, spectral/spectraux, martingale/martingales, normalise/normalisation… ;
- **sans rapport** : les mêmes mots, appariés avec un décalage ;
- **sans rapport de même suffixe** : optimisation/organisation, regularisation/popularisation, gradient/ingredient…

Cosinus moyen ± écart-type :

| représentation | fléchies | sans rapport | même suffixe | aire fl./sans rapport | aire fl./même suffixe |
|---|---|---|---|---|---|
| SHA-256 par jeton | −0,015 ± 0,277 | 0,023 ± 0,254 | −0,032 ± 0,292 | 0,458 | 0,502 |
| SimHash, projection | 0,728 ± 0,157 | 0,055 ± 0,256 | 0,433 ± 0,252 | 0,987 | 0,870 |
| SimHash, binaire | 0,567 ± 0,185 | 0,100 ± 0,265 | 0,317 ± 0,264 | 0,917 | 0,783 |
| SimHash projection, normée puis relevée | 0,749 ± 0,155 | 0,043 ± 0,257 | 0,457 ± 0,269 | 0,986 | 0,883 |
| cosinus exact des 3-grammes (étalon) | 0,711 ± 0,093 | 0,010 ± 0,041 | 0,480 ± 0,152 | 1,000 | 0,913 |

- Corrélation de Spearman avec l'étalon exact : 0,859 pour la projection SimHash, 0,680 pour le binaire, −0,068 pour SHA-256.
- Au niveau du texte, différences de R@1 par rapport à (ii) :
  - (v) − (ii) = +0,025 [0,008 ; 0,042] sur les 180 corpus ;
  - corpus fléchi (la moitié des mots de contenu au pluriel) avec étalon par lemmes : (v) − (ii) = +0,083 [0,051 ; 0,115] ;
  - corpus réel : 0,074 contre 0,222 (Spearman 0,198 contre 0,479) ;
  - version binaire : v_bin − (ii) = −0,094 [−0,116 ; −0,074].

Lecture :

- Le gain annoncé existe au niveau du mot, mais il est acquis par construction : c'est la définition même d'un hachage de 3-grammes. Il amène des faux voisins de même suffixe (cosinus 0,43).
- Au niveau du texte, la somme des SHA-256 par jeton n'est pas « maximalement non informative » : la base garde Spearman = 0,62.
- Le gain de SimHash sur le texte est petit en synthétique, et de signe contraire sur le seul corpus réel disponible.

### Essai 4 — critère d'arrêt

**Le code v6.2.1 n'a pas de critère de convergence spectrale.**

- `fin_conception.json` s'écrit dans trois cas (`principal.py`, lignes 2103 à 2106) :
  - score interne ≥ 0,78 et au moins 2 exemplaires ;
  - ronde ≥ 2 et score ≥ 0,65 ;
  - dernière ronde.
- La mémoire n'entre que par « au moins 2 exemplaires ». Cette condition est vraie dès la première génération : 12 exemplaires retenus sur tous les flux.
- `CONCEPTION.md` § 2.11.4 annonce que l'organisme écrit `fin_conception.json` « dès que son score interne de Bregman-Tsallis et sa mémoire ISVD atteignent le seuil de convergence ». La partie mémoire n'est pas implémentée.
- Un changement d'encodage ne change donc rien à l'arrêt actuel.

**Critère hypothétique testé.**

- σ̂ = Σ / somme(Σ) sur le rang 6, et d(g) = max_k |σ̂_k(g) − σ̂_k(g − 1)|.
- Arrêt à la première génération où deux d(g) consécutifs sont inférieurs à ε.

Génération de déclenchement (médiane [minimum – maximum] sur 10 flux) :

| p_commun | ε | (i) | (iv) | nul |
|---|---|---|---|---|
| 0 | 0,005 | 9 [7–11] | 11 [6–15] | 11 [9–15] |
| 0 | 0,002 | 15 [11–19] | 25 [11–33] | 23 [18–28] |
| 0,3 | 0,005 | 8 [6–12] | 13 [8–15] | 11 [8–14] |
| 0,3 | 0,002 | 18 [11–22] | 24 [19–30] | 24 [10–33] |
| 0,6 | 0,005 | 8 [5–10] | 13 [9–16] | 11 [8–15] |
| 0,6 | 0,002 | 14 [7–28] | 28 [16–33] | 27 [20–30] |

d(g) décroît en 1/g pour toutes les variantes, encodage nul compris. À p_commun = 0,3, pour (i), (iv) et nul :

- d(10)·10 = 0,029 ; 0,048 ; 0,041 ;
- d(50)·50 = 0,035 ; 0,050 ; 0,050.

Lecture :

- À ε fixe, passer de (i) à (iv) retarde l'arrêt d'un facteur 1,2 à 2,0 pour ε ≤ 0,005. Un re-étalonnage serait donc nécessaire si un tel critère existait.
- Mais le critère déclenche aux mêmes générations sous l'encodage nul. Sur une mémoire qui accumule sans oubli, il mesure la dilution d'un lot dans la somme, pas une convergence.
- Un critère spectral éventuel doit être rapporté à un nul (permutation des lots, ou suivi de d(g)·g), jamais à un ε fixe.

Effet de bord de la troncature au rang 6 :

- Elle perd 1,2 à 1,5 % de l'énergie de chaque lot sous (i), 18 à 33 % sous (iv), et 62 % sous l'encodage nul.
- Le sous-espace de la mémoire reste proche de celui de l'accumulation sans troncature : recouvrement de 0,96 à 0,997 sous (i) et de 0,91 à 0,92 sous (iv).
- Seul l'encodage nul gèle son sous-espace (recouvrement 0,57 à 0,59).

### Essai 5 — P1 peut-il échouer, ou est-il acquis d'avance ?

P1 du rapport : « σ1/σ6 passe de 60,9 à ≤ 12 sur 50 cycles grâce à la normalisation sphérique pré-Koopman ».

1. **Il peut échouer.**
   - (ii) à p_commun = 0,6 : 18,1, avec 0 flux sur 10 sous 12 ;
   - (ii) sur 300 jetons : 34,3 ;
   - remède complet SimHash + normalisation : 14,1 à 17,0, avec 0 flux sur 30 sous 12.

   Il n'est donc pas acquis pour (ii) seul.
2. **Il est passé par un encodage sans information.** L'encodage nul reste à σ1/σ6 ≤ 4,5 dans 100 % des corpus et des flux (moyennes : 2,4 en statique, 1,2 en générations), avec Spearman ≈ 0.
3. **Il échoue là où l'information est la mieux conservée.** Sur des corpus structurés (2, 3 ou 5 domaines, 200 à 300 jetons, sans ponts), (iv) donne σ1/σ6 de 16 à 97 selon les corpus (moyennes par cellule de 19 à 60 ; aucun des 60 corpus sous 12), avec Spearman = 0,47 à 0,81. Un corpus à k domaines a k − 1 grandes valeurs propres centrées, donc un σ1/σ6 grand dès que k − 1 < 6.
4. **Avec centrage, il est acquis dans le régime de l'organisme** : (iv) passe dans 30 flux sur 30, avec σ1/σ6 de 2,5 à 9,7 selon les flux.
5. **Sa référence n'est pas fixe.** Le σ1/σ6 de v6.2.1 varie de 58,6 à 65,3 entre les générations 13 et 18 de l'archive, et croît avec la longueur des traces.

Conclusion : P1 est un test échouable, mais son issue dépend du vocabulaire partagé, de la longueur et du nombre de domaines, pas de l'information conservée. Un spectre plat est la signature du bruit isotrope.

**Variante de P1 donnée par la caste 2.** Elle annonce un rang effectif exp(−Σσ̂ ln σ̂) passant de 1,82 à ≥ 3,40. Or le json donne 3,96 avec σ̂ = σ/Σσ, et 1,98 avec σ²/Σσ². Aucune lecture ne donne 1,82, et avec la formule écrite, v6.2.1 dépasse déjà 3,40.

## 4. Verdicts par affirmation du rapport

| # | Affirmation (lieu dans le rapport) | Verdict | Chiffre qui le montre |
|---|---|---|---|
| A1 | « v² écrase le spectre (σ1 = 269 ≫ σ6 = 4,41) » (synthèse, castes 4 et 5) | partielle | v² porte 97,7 % de l'énergie réelle, et u1–u5 sont à 98 % ou plus sur les carrés. Mais σ1 est la direction moyenne (W‖μ‖²/σ1 = 0,98), pas une variance. Sa valeur absolue suit l'accumulation sans oubli : en simulation, Σσ = 532 à la génération 18 pour environ 540 de poids injecté. |
| A2 | « due à l'absence de normalisation avant v² ; la normalisation sphérique l'empêche » (§ 2, caste 4) | partielle | L'effet d'échelle disparaît : σ5/σ6 passe de 7,1–10,2 à 1,2–3,6. La direction commune reste : W‖μ‖²/σ1 = 0,65–0,97. σ1/σ6 dépasse 12 dans 83 % des corpus statiques. |
| A3 | « Koopman sur bruit blanc amplifie la variance isotrope » (caste 2) | réfutée | Le spectre est fortement anisotrope : σ1/σ6 = 61, et cinq directions sur six occupent les cinq coordonnées carrées. |
| A4 | « SHA-256 vers R¹⁶ est maximalement non informatif ; les cosinus se concentrent » (castes 1 et 3) | réfutée (niveau du texte) | Base SHA-256 : Spearman 0,621 (statique) et 0,570 (réel) ; R@1 0,381 contre 0,056 au hasard. Écart-type des cosinus de mots : 0,25 à 0,29. |
| A5 | « SHA-256 détruit la topologie locale ; SimHash 3-grammes préserve le cosinus » (synthèse, caste 2) | établie au niveau du mot, par construction | Aire sous la courbe 0,987 contre 0,458 ; Spearman 0,859 avec le cosinus exact. Réserve : 0,870 face aux mots de même suffixe. |
| A6 | La géométrie de la mémoire gagne avec SimHash (implicite) | partielle | +0,025 [0,008 ; 0,042] en synthétique et +0,083 avec flexions ; −0,148 sur le corpus réel ; version binaire −0,094. |
| A7 | P1 : « σ1/σ6 de 60,9 à ≤ 12 grâce à la normalisation sphérique » (prédiction) | partielle | (ii) donne 9,1–9,4 à p_commun ≤ 0,3, mais 18,1 à 0,6. SimHash + normalisation donne 14,1–17,0 (0 flux sur 30). |
| A8 | P1 est un protocole falsifiable qui atteste le gain | réfutée | L'encodage nul passe dans 100 % des cas sans aucune information. Les corpus structurés bien encodés échouent (0 sur 60). Avec centrage, 30 flux sur 30 passent. |
| A9 | Variante de la caste 2 : rang effectif de 1,82 à ≥ 3,40 | réfutée | Le json donne 3,96 (ou 1,98) ; v6.2.1 dépasse déjà 3,40. |
| A10 | « Le rang 6 capture la dérive des moments pairs ; filtre aveugle » (caste 4) | établie | u1–u5 sont sur les carrés. Sous (i), sur le corpus réel : R@1 = 0,000, Spearman = 0,014. |
| A11 | La mémoire spectrale entre dans l'arrêt par un « seuil de convergence » (CONCEPTION.md § 2.11.4) | réfutée | Le code ne lit que « au moins 2 exemplaires » (`principal.py`, lignes 2103 à 2106). |

## 5. Protocole P1′ — une version qui peut échouer

À sceller avant tout calcul (R1), puis à faire contre-lire par un sous-agent neuf (R2).

- **Hypothèse.** L'encodage proposé garde dans la mémoire de rang 6 plus de similarité entre textes que l'encodage v6.2.1.
- **Métrique principale.**
  - Corrélation de rang de Spearman, sur toutes les paires d'un corpus, entre deux grandeurs :
    - le cosinus des coordonnées de rang 6, avec les vecteurs propres tels que la mémoire les stocke ;
    - la similarité de Jaccard des ensembles de jetons.
  - Moyenne sur le banc de corpus.
  - Métrique secondaire : R@1 de rang 6.
  - σ1/σ6 est rapporté pour description, jamais comme seuil.
  - Le R@1 n'est pas retenu comme métrique principale parce qu'il reste faible sur les corpus très structurés. À l'essai 5, il vaut 0,05 à 0,14 sous (iv), soit deux à cinq fois le hasard, alors que la corrélation de Spearman sépare nettement (iv) du nul : 0,47 à 0,81 contre ≈ 0.
- **Nuls.**
  1. L'encodage v6.2.1, apparié corpus par corpus.
  2. L'encodage aléatoire, avec une direction par texte.
  3. 1000 permutations des textes dans chaque corpus, qui donnent le 95e centile nul de la corrélation.
- **Seuil**, fixé avant les données. L'essai réussit si trois conditions sont réunies ; sinon il échoue :
  - gain moyen ≥ +0,10 sur v6.2.1 ;
  - borne basse de l'intervalle à 95 % (rééchantillonnage apparié) > 0 ;
  - corrélation au-dessus du 95e centile de permutation dans au moins 90 % des corpus.
- **Banc figé.**
  - Une grille synthétique à graines scellées, qui inclut p_commun = 0,6 et des textes de 300 jetons.
  - Le corpus réel d'ancrage tiré de `fournis/`.
  - Une moisson réelle neuve, jamais vue, d'au moins 100 traces.
- **Lecture symétrique (R4).** Un gain sur le synthétique accompagné d'un gain négatif sur le réel vaut réserve, pas succès.
- **S'il faut aussi un critère spectral.**
  - Analyse parallèle de Horn sur la mémoire centrée : on compte les valeurs propres qui dépassent le 95e centile de la valeur propre de même rang sous l'encodage aléatoire de même taille.
  - On l'accompagne d'une prédiction chiffrée, par exemple au moins k − 1 pour un corpus à k domaines. Ce critère peut échouer dans les deux sens.
- **Indication, non opposable** (seuil écrit après avoir vu ces données exploratoires) :
  - (ii) contre (i) : 0,595 contre 0,368 (+0,23) ; sur le corpus réel, 0,450 contre 0,011.
  - P1′ échouerait en revanche pour SimHash face à (ii) : 0,577 contre 0,595, soit −0,02.

## 6. Réserves

- **Corpus synthétiques** : petit vocabulaire (250 mots de contenu), donc un recouvrement de Jaccard plus fort qu'en réel. Le corpus réel ne compte que 27 textes, dont 12 sélectionnés par la mémoire elle-même.
- **Séparation Domaine/Opérateur du rapport** : non testée, car le lexique n'est pas spécifié. SimHash est appliqué au texte entier. Le verdict A7 sur le remède complet vaut pour cette lecture seulement.
- **Étalon par jetons** : il est aveugle à la morphologie. L'étalon par lemmes ne couvre que des pluriels synthétiques.
- **Jacobi du code** : il n'est pas convergé en 120 itérations. L'écart reste sous 0,26 % sur σ1 à σ6 sous (i) et atteint 4,5 % sous (ii) en statique (0,16 % sur une matrice générique). Les rapports code et exact restent à moins de 4 % en générations, et aucun verdict n'en dépend.
- **Poids et bonus** : poids uniformes ; aucun bonus multi-familles, car aucun mot-clé n'apparaît dans les corpus synthétiques.
- **Statut** : exploratoire, sans contre-lecture par un sous-agent neuf, puisque le brief interdit les sous-agents. À signaler pour R2.
- **Brouillons** : les sorties des passes de mise au point sont rangées sans modification dans `resultats/brouillons-1/`. Elles ont été produites par des versions antérieures des scripts, dont les empreintes figurent dans leurs manifestes. Aucun chiffre de ce rapport n'en vient.

## 7. Fichiers et empreintes (SHA-256)

Scripts (lancés par `python3 -I -B pilote_brique1_v1.py <essai> --horodatage "$(date -u +%Y-%m-%dT%H:%M:%SZ)"`) :

- `pilote_brique1_v1.py` : `d08f794c1d4b690183e6d55dd60fce373ff602fd2964143407aace40a874d38c`
- `brique1_communs_v1.py` : `7b2fa00e636b8e416ad4b7f4fafaab9e63697bca3d823c9d855c215c2767fcca`
- `simhash_ngrammes_v1.py` : `01ad6d0aa0305eb8528151cc81fb7e2b8413b7f88ef401a3a3ef49756b4913af`
- `lire_resultats_v1.py` : `7665c25a3bc07ccdc08ac9b5ced3417ef3c30fbb78c7a280a1ce6911cbce9352`
- `organisme_copie/memoire_isvd.py` : `e39295c5d3d04a45ef3024347bf30ee6744aee88fd77ea058e2c8f231f3e1710`

Résultats (chaque manifeste porte l'horodatage, la version de Python 3.13.17, les graines et les empreintes ci-dessus) :

- `resultats/verifications-v1.json` : `29bc36a4c46e2f150c3b6b30fe61ce2095f373b9489c30a8f59029916b20c2f4`
- `resultats/reel-v1.json` : `5da88e60d38854527c216b1afd4dc2d24d78d272003876fbfda97ebbd8de04c2`
- `resultats/essai1-v1.json` : `a91504917924fd8e3390ee12558390e369d7f20c372480b060ed68fcfb6fa59c`
- `resultats/essai2-v1.json` : `6c67454c2c5366b28cd427fcfdec78790519516fe55060a26f623612b75ea543`
- `resultats/essai3-v1.json` : `c3ef827f396023cd666969db1d670318648309b47e6bef92d140749e9bdf1c01`
- `resultats/essai5-v1.json` : `47e55bd15fced9d7d51d569fbe580b6abb119d426556c8387f6d1eb2a932b9df`
- `resultats/generations-v1.json` (essais 1, 2 et 4) : `017fefe007cbb49358c24bea5ada2eb027e23d097c95b4f219b4d638c3583f28`
- `resultats/table-signes-simhash-essai3-v1.tsv` : `88e5a66e202c791a70cd51e3abf4dd13825eaa7b985d727fd26c7d03958782b4`
- `resultats/tableaux-v1.md` : `a2f6c6694d65dad68b73bf2ffc955cab824ca697bd071c5c028137687f242f7a`

Chaque fichier a un compagnon `.sha256`, vérifiable par `sha256sum -c` depuis son dossier.

## 8. Génération 0 — sélection par réfutation (une ligne par affirmation)

Affirmations du rapport :

- B1-01 « Le terme v² domine la mémoire spectrale » — **survit** — 97,7 % de |ψ|² réel sur les carrés ; u1–u5 à 98 % ou plus sur les carrés.
- B1-02 « σ1 = 269 traduit une explosion de variance due à v² » — **éliminée** — σ1 est la direction moyenne (W‖μ‖²/σ1 = 0,98 ; quotient de Rayleigh 0,9993) ; sa valeur suit le poids accumulé (en simulation, Σσ = 532 pour environ 540 injectés).
- B1-03 « La normalisation sphérique pré-Koopman supprime l'écrasement d'échelle par v² » — **survit** — part des carrés de 98 % à 11 % ; σ5/σ6 de 7,1–10,2 à 1,2–3,6.
- B1-04 « Cette normalisation suffit à ramener σ1/σ6 ≤ 12 » — **indécise** — 17 % des corpus statiques ; 10 flux sur 10 à p_commun ≤ 0,3 mais 0 sur 10 à 0,6 ; 6,27 sur le corpus réel.
- B1-05 « Koopman sur bruit blanc amplifie la variance isotrope » — **éliminée** — σ1/σ6 = 61, une seule direction propre hors des carrés.
- B1-06 « SHA-256 vers 16 dimensions est maximalement non informatif, cosinus concentrés » — **éliminée** — base : Spearman 0,62 (statique) et 0,57 (réel) ; R@1 0,381 contre 0,056.
- B1-07 « SimHash 3-grammes préserve la proximité morphologique que SHA-256 détruit » — **survit** — aire 0,987 contre 0,458 ; faux voisins de même suffixe : 0,870.
- B1-08 « SimHash améliore la géométrie de la mémoire au niveau du texte » — **indécise** — +0,025 et +0,083 en synthétique ; −0,148 sur le réel.
- B1-09 « SimHash + normalisation sphérique ramène σ1/σ6 ≤ 12 sur 50 cycles » — **éliminée** — 14,1 à 17,0, 0 flux sur 30 (texte entier ; séparation Domaine/Opérateur non testée).
- B1-10 « P1 atteste le gain de la v6.3 » — **éliminée** — encodage nul : 100 % sous 12 (≤ 4,5 partout) ; corpus structurés bien encodés : 0 sur 60.
- B1-11 « Rang effectif de 1,82 en v6.2.1 » (caste 2) — **éliminée** — 3,96 (σ) ou 1,98 (σ²) sur le json.
- B1-12 « Le rang 6 suit les moments pairs et devient aveugle à la similarité » (caste 4) — **survit** — sous (i), sur le réel : R@1 = 0,000 (hasard 0,038) ; Spearman = 0,014.
- B1-13 « La mémoire spectrale entre dans l'arrêt par un seuil de convergence » (CONCEPTION.md § 2.11.4) — **éliminée** — seule condition lue : au moins 2 exemplaires (`principal.py`, lignes 2103 à 2106).

Hypothèses du brief (pas du rapport) :

- H-a « La base non normalisée a des composantes qui croissent avec le nombre de jetons » — **survit** — σ5/σ6 passe de 1,2 (3 jetons) à 226 (300 jetons).
- H-b « Les carrés ont une direction commune que la normalisation par vecteur n'enlève pas » — **survit** (sauf « quasi rang 1 ») — 97 à 98 % de σ1 ; mais σ1 ne fait que 52 % de la trace (rang effectif 3,96).
- H-c1 « Le centrage seul suffit à passer P1 » — **éliminée** — jamais sous 12 (22 à 3664 en statique ; moyennes de 27 à 31 en générations, 0 flux sur 30).
- H-c2 « (ii) + centrage rend P1 acquis d'avance dans le régime de l'organisme » — **survit** — 30 flux sur 30 sous 12 (2,5 à 9,7), sans gain d'information sur (ii) (+0,003 [−0,005 ; 0,012]).
- H-d « Un critère de Cauchy à ε fixe reste valable après un changement d'encodage » — **éliminée** — médianes de déclenchement multipliées par 1,2 à 2,0 (ε ≤ 0,005) ; l'encodage nul déclenche aux mêmes générations.

<<<FIN G2>>>

<<<DÉBUT S1 — synthèse du tour « pôle scientifique automatique » (R-525 ; `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md`, sha256 `4d6ddf40d99084fbdfad9c7bf14a350fd718516fe519498d7e4b58837d56d1fd`)>>>

# Pôle « scientifique automatique » — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 26 octobre 2026 par la lignée « session-depot », à partir des neuf cellules du tour (GO-2026-10-26-06, R-524 ; `donnees/collisionneur-pole-scientifique-v1`, `0fbf92d`). Matériau de décision, jamais une consigne. Rien d'opposable (R7) ; les étiquettes RAPPORTÉ / HYPOTHÈSE sont celles des modèles.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours (conception, équipe rouge croisée, riposte), neuf cellules valides, aucun refus, 7,82 USD.
- **Réserve forte** : la pièce C (méta-conception v6.3 et sa relecture) **n'a pas été servie** ; les trois modèles le signalent et refusent de conclure sur la recombinaison bisociative (point 3). Demandée à conv-audit (n° 76).

## Verdict en cinq lignes

1. **« Perfectionner le nôtre » et « adopter un système de la littérature » sont rejetés tels quels par les trois.** La réponse convergente est une **voie hybride ancrée sur notre noyau**.
2. Ce qui a de la valeur chez nous, ce n'est pas l'organisme, c'est **le noyau** : clés jamais exposées, bornes d'appels/temps/moisson, et surtout, depuis la correction C-17, l'agent ne peut plus soumettre de code brut (gabarit de trois paramètres bornés). C'est une sûreté acquise.
3. **La première expérience n'est pas « quel moteur », c'est « notre critère de sélection promeut-il du faux ? ».** Processeur seul, moins de 20 USD, cette semaine. Si le filtre laisse passer les paris couverts et les hypothèses à domaine étroit, **n'importe quel** générateur (le nôtre ou celui de la littérature) converge vers des artefacts de Goodhart.
4. **Agentic Scientist v3 est écarté** tant que ses agents héritent des clés (sûreté), malgré son évaluation finale scellée.
5. La capacité « réécrire son propre code » (point 4) **n'existe pas** chez nous aujourd'hui (C-17 l'a retirée pour la sûreté) : elle est à **concevoir sous bac à sable**, pas à « perfectionner ».

## Les points de convergence des trois modèles

- **Architecture recommandée** : garder le noyau (sûreté), y greffer l'idéation/mutation d'un moteur de la littérature **en conteneur sans clés** *si* la première expérience montre notre grammaire bornée insuffisante, et ajouter un **évaluateur figé tenu par le noyau, hors des agents** — absent des deux voies aujourd'hui.
- **Sélection darwinienne sans Goodhart** : sévérité *ex ante* — le test et le nul sont **figés par le noyau avant** l'expérience, les tirages sont **frais après** l'engagement de l'hypothèse. Nul **composite** (bibliothèque de prédicteurs aveugles au domaine ; inférence universelle de Wasserman–Ramdas) pour que l'inégalité de Ville tienne même si le nul n'est pas exactement connu. **Contenu** d'une hypothèse = risque déclaré (divergence à une référence) × couverture du domaine : un pari couvert est classé bas, une hypothèse qui ne prédit rien ne survit pas.
- **Qui écrit le test** : avec nul figé et tirages après dépôt, peu importe (Ville tient) — mais c'est **à vérifier**, et c'est l'objet de la première expérience.
- **Recombinaison bisociative** (sous réserve de la pièce C) : forme minimale = tirage (éloignement des domaines × similarité d'opérateur sur arbre syntaxique **canonisé**) + filtre mécanique de contraintes + fusion ; test sur des mondes à isomorphismes plantés **contre un tirage stratifié recevant exactement le même prompt et le même filtre** ; réfutée si l'écart < ~12 points.
- **Validité de construit des sondes** (B soulève, C adopte) : une sonde linéaire qui lit une **transcription** mesure la représentation du **lecteur**, pas forcément l'état interne de l'agent qui a agi. À garder pour tout le programme.

## La première expérience (convergente, chiffrée par les trois)

**Valider le critère de sélection**, avant tout choix de moteur. Processeur seul, activations réelles mises en cache, moins de 20 USD, deux à trois jours.
1. Étalonnage A/A : deux courses identiques pour fixer le plancher de bruit.
2. Duel sur une population à vérité connue (hypothèses vraies, biais de sous-population, **paris couverts**) : (bras 1) un sélecteur **mécanique** *ex ante* sans appel de modèle, qui choisit les instances où l'hypothèse et le nul divergent le plus ; (bras 2) le même, plus un agent « réfutateur » d'une autre espèce ; (bras 3) la sélection par score moyen (le témoin faible).
3. Contrôles **fatals** : parasite de Kelly et nul dans la bibliothèque → promotion ≤ α ; paris couverts promus seulement si leur part nette est vraie. Un échec invalide le critère et **arrête tout**.
4. Règle d'arrêt : si le bras 1 (mécanique, zéro appel) élimine ≥ 95 % des fausses hypothèses et égale le bras 2 (réfutateur modèle) à un bruit près, on **économise définitivement** les appels du réfutateur et on passe au duel « grammaire bornée contre Python libre sous prison du noyau », qui, lui, tranche la voie.

## Ce qu'aucun modèle n'a pu établir (tous en HYPOTHÈSE)

- Que l'organisme apprenne d'une génération à l'autre, ou que ses castes calibrent mieux qu'une auto-cohérence à budget égal, ou que la mémoire ISVD apporte quelque chose (aucune ablation dans les faits).
- Que la bisociation batte un tirage stratifié (pièce C absente).
- Que les critères de sélection corrigés résistent vraiment (écrits, non courus).
- Qu'un banc synthétique planté prédise le réel (B et A proposent un pont à mesurer).

## Pour toi, maintenant

- **Décision de voie** : hybride ancrée sur le noyau (recommandation des trois). Ce n'est pas un nœud bloquant tout de suite — la première expérience est faisable sans trancher la voie.
- **Dépense** : la première expérience est sur processeur, quasi gratuite (quelques appels de contrôle). Un préenregistrement minimal scellé (R1) suffirait à la lancer.
- **À débloquer** : la pièce C (méta-conception) pour le volet recombinaison.

<<<FIN S1>>>

<<<DÉBUT S2 — synthèse du tour « recombinaison bisociative » (R-527 ; `docs/notes/pole-scientifique-automatique/synthese-recombinaison-v1.md`, sha256 `47490973ce85c18bb1c2a15511a830e61e9b2cf43b9ccc083271e8dde12bc65a`)>>>

# Recombinaison bisociative — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 26 octobre 2026 par « session-depot », à partir des neuf cellules du tour (GO-2026-10-26-07, R-526 ; `donnees/collisionneur-recombinaison-v1`, `19aa452`). Matériau de décision, jamais une consigne. Étiquettes RAPPORTÉ / HYPOTHÈSE conservées des modèles.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Neuf cellules valides, aucun refus, 8,86 USD. **Toutes les pièces servies** (méta-conception, relecture, génération 0 de conv-audit, synthèse R-525). Pièce C4 (test « ponts plantés ») non rendue au départ.

## Verdict en cinq lignes

1. **Le tirage déterminantal d'origine est mort** : son noyau n'est pas semi-défini positif (1 000 violations sur 1 000, génération 0 de conv-audit) et il récompense la *similarité* de domaine, l'inverse de ce qu'on veut. La méta-conception de Gemini citait en outre des fonctions **absentes** du vrai code v6.2.1.
2. **La forme corrigée est juste algébriquement, mais incomplète.** Elle cède sur quatre points : quand la représentation de domaine porte le gabarit ou le style ; sur les opérateurs « moyeux » et les jargons rares fabriqués (il faut rareté **et** structure) ; sur les homonymes ; et dans les petits corpus sans pont, faute d'abstention.
3. **Les deux équipes rouges trouvent le même trou, plus grave que le tirage** : le critère « la fille prédit plus que ses parents » est **franchissable à coût nul** par des tricheurs scriptés (enveloppe harmonique aveugle, copie renommée, pari couvert, adimensionnement, jargon rare). L'attaque la plus forte : une simple enveloppe bat la conjonction même sur un anti-oracle.
4. **La première expérience n'est donc pas « quel tirage », c'est « le critère de contenu résiste-t-il aux tricheurs ? »** — processeur seul, ~0 USD, cette semaine, aucun appel de fusion. C'est le **même principe que la première expérience du pôle** (valider le juge avant de choisir le moteur), appliqué à la recombinaison.
5. **Pour la version 0** : recombiner des **hypothèses** du pôle (observable, prédiction), pas des articles ; tirage **stratifié** sur domaine estimé (le témoin que personne n'attaque) + appariement par opérateur **forcé après le tirage** + filtre de compatibilité ; le noyau déterminantal corrigé n'est adopté que s'il bat la stratification à budget égal sur étiquettes **estimées et bruitées** (indécis, c'est l'expérience 1).

## Ce qui survit aux essais sur processeur (génération 0, RAPPORTÉ, non réaudité)

1. Normalisation des hachages SimHash 3-grammes avant relèvement (+0,135 de rappel ; accord topologique 0,014 → 0,48).
2. Noyau corrigé L = diag(q)·(S + εI)·diag(q), S_ij = ⟨d_i, d_j⟩² (diversité de domaine dans la répulsion, pertinence dans la qualité), Sinkhorn sur S seul : 0,90 à 0,95 de paires de domaines distincts sans perte de qualité.
3. **Attraction d'opérateur hors du noyau déterminantal** : appariement forcé après le tirage (0,995 à 1,00 sur étiquettes propres).
4. Filtre de pivots par fréquence de fond externe (rejette les « hubs » génériques).
5. Filtre lexical de compatibilité : ramène les fusions contradictoires de 55,9 % à 34,4 %.

## La première expérience (convergente, chiffrée par les trois)

**Valider le critère de contenu contre des tricheurs, avant tout appel de fusion.** Processeur seul, ~0 USD, moins de dix minutes, réutilise l'infrastructure NumPy de la génération 0.
- Faire passer au critère et au monde planté une **batterie de tricheurs scriptés** : tricheur de forme, copie-renommée, **enveloppe aveugle**, fille constante, pari couvert, adimensionnement. Aucun appel de modèle.
- Issue 1 : un tricheur promu au-delà de α **invalide le critère avant toute dépense** — on s'arrête là.
- Issue 2 : aucun tricheur promu → le banc devient opposable, et on passe au plan factoriel {noyau continu, grille discrète} × {lexique, arbre d'opérateurs} à budget égal, sur étiquettes **estimées et bruitées**, pour trancher entre la grille (A et C) et le noyau corrigé (B).
- Règle de contenu durcie : une fille doit **battre l'enveloppe harmonique de 2 δ₀** (pas seulement la conjonction), avec une règle de score propre sur données fraîches, trois familles de modèles distinctes (générateur, extracteur, fusionneur), et des lois tenues hors calibrage.

## Ce qu'aucun modèle n'a établi (tout HYPOTHÈSE)

- Qu'une fusion par modèle de langue accroisse vraiment le contenu empirique (plutôt qu'une juxtaposition ou une copie).
- Qu'un critère mécanique sépare un vrai pont d'un homonyme.
- Que le tirage déterminantal batte la stratification à budget égal, sur étiquettes estimées.
- Qu'un signal d'opérateur batte une prédiction de liens classique sur la littérature réelle.
- C4 absente : aucun monde planté réel n'a encore été couru (le test de conv-audit est en cours).

## Pour toi, maintenant

- **Forme v0** : stratification + opérateur après tirage + filtre, avec abstention ; le noyau corrigé en réserve, à départager par l'expérience 1.
- **La première expérience est sur processeur, quasi gratuite, et elle va droit vers un résultat net** : soit elle casse notre critère (et nous épargne une dépense), soit elle le rend opposable. conv-audit en écrit déjà le code ; je l'exécuterai sous préenregistrement scellé.
- **Convergence des deux tours** : avant de dépenser sur un moteur (pôle) ou un tirage (recombinaison), valider le juge contre des tricheurs à coût nul. C'est le chemin solide.

<<<FIN S2>>>
