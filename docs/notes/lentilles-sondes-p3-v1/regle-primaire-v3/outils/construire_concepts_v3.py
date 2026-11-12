"""Construction de la liste de mots v3 des concepts « tromperie » et « enjeux » (sondes de P3, lecture des lentilles).

29 octobre 2026. Écrit avant toute lecture de sortie des lentilles : aucune sortie réelle (v2 ou autre) n'a été lue.
Bibliothèque standard seule. Deux étapes, reproductibles :

  python3 -I -B construire_concepts_v3.py candidat --sortie <dossier>
      -> concepts-sondes-p3-v3-candidat.json (+ .sha256) et journal des exclusions
  <script v2> verifier-concepts --vocabulaire tokenizer.json --concepts <candidat>   (journal gardé)
  python3 -I -B construire_concepts_v3.py final --sortie <dossier> --journal-verification <journal du candidat>
      -> concepts-sondes-p3-v3.json (+ .sha256) : le candidat moins les mots sans jeton de début de mot

Règles d'exclusion, écrites avant la construction et appliquées dans cet ordre (méthode : regle-primaire-v3.md, §2) :
  E1 mot outil (liste fermée MOTS_OUTILS) ;
  E2 homographe de code (liste fermée HOMOGRAPHES_CODE : littéraux, mots réservés, commandes, couches d'apprentissage) ;
  E3 homographe dont le sens premier (premier sens du dictionnaire) est hors du concept, ou homographe d'une autre
     langue fréquente dans le vocabulaire (français, allemand), ou prénom (liste fermée HOMOGRAPHES_SENS) ;
  E4 mot générique retiré en v2 (life, lives, important, legal) ;
  E5 mot présent dans les deux listes candidates (retiré des deux) ;
  E6 mot sans jeton de début de mot dans le vrai vocabulaire (étape « final », lu dans le journal de verifier-concepts).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------------------------------------------------
# Candidats, par famille de sens (définitions de dictionnaire et thésaurus, de mémoire ; familles morphologiques).
# Tous les mots de la liste v2 y sont (marqués « v2 »). Construits indépendamment pour chaque concept.

CANDIDATS = {
    "tromperie": {
        "v2": ["lie", "lies", "lying", "liar", "lied", "deceive", "deceived", "deception", "deceptive", "dishonest",
               "falsely", "fake", "pretend", "pretending", "untrue", "misleading", "fraud", "cheat", "cheating", "trick",
               "fabricated", "hoax", "manipulate", "conceal"],
        "mensonge": ["liars", "untruth", "untruths", "untruthful", "falsehood", "falsehoods", "perjury", "mendacious",
                     "mendacity", "insincere", "insincerity", "disingenuous", "dishonestly", "dishonesty", "fib"],
        "tromper": ["deceives", "deceiving", "deceit", "deceitful", "deceptively", "deceiver", "delude", "deluded",
                    "fool", "fooled", "fooling", "dupe", "duped", "hoodwink", "hoodwinked", "bamboozle", "gaslight",
                    "gaslighting", "bluff", "bluffing", "bluffed", "mislead", "misleads", "misled", "misleadingly",
                    "misrepresent", "misrepresented", "misrepresenting", "misrepresentation"],
        "faux": ["false", "fakes", "faked", "faking", "fakery", "phony", "phoney", "bogus", "sham", "counterfeit",
                 "counterfeits", "forgery", "forgeries", "forger", "forge", "forged", "fictitious", "falsify",
                 "falsified", "falsifying", "falsification", "fabricate", "fabrication", "fabrications", "fabricating",
                 "doctored", "fudge", "fudged", "deepfake", "deepfakes", "spoof", "spoofed", "spoofing", "impostor",
                 "imposter", "impersonate", "impersonating", "impersonation", "masquerade", "charade", "facade",
                 "pretense", "pretence", "pretext", "pretended", "pretends", "feign", "feigned", "feigning",
                 "hypocrisy", "hypocrite", "hypocritical", "plagiarism", "plagiarized", "mock", "spurious"],
        "dissimulation_secret": ["conceals", "concealed", "concealing", "concealment", "hide", "hides", "hiding", "hid",
                                 "hidden", "secret", "secrets", "secretly", "secretive", "secrecy", "covert",
                                 "covertly", "disguise", "disguised", "disguises", "camouflage", "camouflaged",
                                 "obfuscate", "obfuscated", "obfuscation", "withhold", "withheld", "whitewash",
                                 "whitewashed", "stealthily", "sneaky", "sneakily", "sneak", "evasive", "evasion",
                                 "evade", "dissemble", "dissembling", "mask", "cover", "exposed"],
        "fraude": ["frauds", "fraudulent", "fraudulently", "fraudster", "fraudsters", "scam", "scams", "scammer",
                   "scammers", "scammed", "swindle", "swindled", "swindler", "con", "conned", "conman", "embezzle",
                   "embezzled", "embezzlement", "phishing", "rigged", "rig", "cheats", "cheated", "cheater", "cheaters",
                   "collusion", "collude", "conspiracy", "conspire", "conspired", "fleece", "crooked", "extortion",
                   "blackmail", "scandal"],
        "manipulation": ["manipulated", "manipulating", "manipulation", "manipulative", "manipulator", "manipulators",
                         "brainwash", "brainwashed", "brainwashing", "propaganda", "disinformation", "misinformation",
                         "spin"],
        "ruse": ["tricks", "tricked", "tricking", "trickery", "trickster", "tricky", "ruse", "ruses", "guile",
                 "cunning", "wily", "sly", "slyly", "devious", "deviously", "duplicity", "duplicitous", "treachery",
                 "treacherous", "betray", "betrays", "betrayal", "betrayed", "traitor", "traitors", "backstabbing",
                 "underhanded", "shady", "fishy", "scheming", "scheme", "plot", "ploy", "ploys", "stratagem",
                 "subterfuge", "chicanery", "skulduggery", "machinations", "artifice", "wiles", "decoy", "lure",
                 "lured", "trap", "hoaxes"],
    },
    "enjeux": {
        "v2": ["danger", "dangerous", "risk", "risky", "urgent", "urgency", "emergency", "critical", "crisis", "serious",
               "severe", "fatal", "death", "deadly", "safety", "threat", "harm", "lawsuit", "catastrophic", "disaster",
               "stakes", "consequences", "surgery", "bankrupt", "fired", "jail"],
        "danger": ["dangers", "dangerously", "endanger", "endangered", "endangering", "peril", "perils", "perilous",
                   "hazard", "hazards", "hazardous", "unsafe", "jeopardy", "jeopardize", "jeopardized", "jeopardizing",
                   "precarious", "treacherous", "menace", "threats", "threaten", "threatened", "threatening",
                   "threatens", "exposed", "compromised", "vulnerable"],
        "risque": ["risks", "risking", "risked", "riskier", "riskiest"],
        "urgence": ["urgently", "emergencies", "imminent", "alarming", "alarm", "desperate", "desperately", "pressing",
                    "deadline"],
        "gravite": ["grave", "gravely", "dire", "severely", "severity", "seriously", "seriousness", "critically",
                    "grim", "harrowing", "gravity", "acute", "crucial", "vital"],
        "vie_et_mort": ["life", "lives", "deaths", "dead", "die", "dies", "died", "dying", "kill", "kills", "killed",
                        "killing", "lethal", "mortal", "mortality", "fatalities", "fatality", "fatally", "casualties",
                        "casualty", "victim", "victims", "injury", "injuries", "injured", "wounded", "hurt", "survive",
                        "survived", "survival", "survivors", "overdose", "hospitalized", "livelihood", "lifesaving",
                        "stroke", "terminal"],
        "consequences": ["consequence", "consequential", "repercussions", "ramifications", "fallout", "aftermath",
                         "irreversible", "irreparable", "irrevocable", "important"],
        "catastrophe": ["catastrophe", "catastrophes", "catastrophically", "disasters", "disastrous", "calamity",
                        "calamitous", "cataclysmic", "apocalypse", "apocalyptic", "devastating", "devastation",
                        "devastated", "tragedy", "tragedies", "tragic", "ruin", "ruined", "ruinous", "meltdown", "doom",
                        "doomed", "crash", "crashed", "collapse"],
        "crise": ["crises", "turmoil", "evacuation", "evacuate", "panic", "scandal"],
        "prejudice": ["harms", "harmful", "harmed", "harming", "damage", "damages", "damaging", "breach", "breaches"],
        "juridique_financier": ["legal", "lawsuits", "sue", "sued", "litigation", "liability", "liable", "prosecution",
                                "prosecuted", "indicted", "indictment", "prison", "imprisonment", "imprisoned", "jailed",
                                "sentenced", "felony", "felonies", "criminal", "arrest", "arrested", "conviction",
                                "penalty", "fines", "bankruptcy", "insolvency", "insolvent", "foreclosure", "layoffs",
                                "blackmail", "extortion"],
    },
}

# E1 — mots outils : liste fermée (déterminants, pronoms, prépositions, conjonctions, auxiliaires, modaux, négations,
# adverbes de degré). Appliquée telle quelle, même si elle ne retire rien.
MOTS_OUTILS = set("""
a an the this that these those some any each every no none all both either neither such what which whose
i me my mine you your yours he him his she her hers it its we us our ours they them their theirs myself yourself
himself herself itself ourselves themselves who whom one ones
of in on at by for with about against between into through during before after above below to from up down out
off over under again further then once here there when where why how than as per via upon within without across
along around among toward towards onto unto
and but or nor so yet if because while although though unless until since whether
be is am are was were been being have has had having do does did doing done
can could may might must shall should will would ought
not never no yes
very too quite rather really just only also even still already almost more most less least much many few
""".split())

# E2 — homographes de code (littéraux, mots réservés et fonctions de Python et du shell, réglages courants, couches
# d'apprentissage) : liste fermée.
HOMOGRAPHES_CODE = {
    "false": "littéral booléen (False, false) ; retiré dès la v2",
    "fib": "Fibonacci en code ; retiré dès la v2",
    "mock": "objets factices des tests (unittest.mock)",
    "hidden": "couche ou état caché en apprentissage, attribut HTML hidden",
    "kill": "commande du shell et signal de processus",
    "kills": "comme kill",
    "panic": "fonction panic de Go et du noyau",
    "crash": "plantage de programme",
    "crashed": "comme crash",
    "terminal": "terminal de commande",
}

# E3 — homographes dont le premier sens du dictionnaire est hors du concept, homographes d'une autre langue, prénoms.
HOMOGRAPHES_SENS = {
    "con": "pros and cons",
    "fool": "nom : personne sotte (sens premier)",
    "forge": "forge du forgeron, « forge ahead »",
    "forged": "forgé (métal), « forged ahead »",
    "fudge": "confiserie",
    "spurious": "corrélation fallacieuse (statistique), sans intention",
    "sneak": "« sneak peek »",
    "mask": "masque (objet, masque de données)",
    "cover": "couvrir, couverture (sens premier)",
    "rig": "plateforme pétrolière, matériel",
    "fleece": "laine, veste polaire",
    "crooked": "tordu (sens premier)",
    "spin": "tourner (sens premier)",
    "tricky": "difficile (sens premier)",
    "fishy": "de poisson (sens premier)",
    "scheme": "schéma (color scheme, URL scheme)",
    "plot": "graphique, intrigue d'un récit",
    "trap": "piège matériel, interruption (trap) en informatique",
    "vulnerable": "vulnérabilité logicielle ; sens trop large",
    "alarm": "réveil, alarme d'appareil",
    "pressing": "appuyer (pressing a key)",
    "deadline": "échéance de travail ordinaire",
    "gravity": "gravité physique",
    "acute": "angle aigu ; sens médical trop étroit",
    "crucial": "évaluatif générique, comme « important » retiré en v2",
    "vital": "évaluatif générique, comme « important » retiré en v2",
    "die": "article allemand « die », dé à jouer",
    "dire": "verbe français « dire »",
    "sue": "prénom Sue",
    "hurt": "trop large (« it doesn't hurt to »)",
    "stroke": "trait, coup de pinceau",
    "collapse": "replier (interface), effondrement générique",
    "conviction": "croyance ferme (sens premier)",
    "penalty": "pénalité sportive, terme de régularisation",
    "fines": "pluriel de « fine » (fin, bien) ambigu",
}

# E4 — génériques retirés en v2, gardés retirés.
GENERIQUES_V2 = {"life": "générique (v2)", "lives": "homographe du verbe (v2)", "important": "générique (v2)",
                 "legal": "générique (v2)"}


def sha256_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ecrire_scelle(p: Path, texte: str) -> str:
    if p.exists() or Path(str(p) + ".sha256").exists():
        sys.exit(f"REFUS sortie-existe : {p} (R12)")
    p.write_text(texte, encoding="utf-8")
    sha = sha256_fichier(p)
    Path(str(p) + ".sha256").write_text(f"{sha}  {p.name}\n", encoding="utf-8")
    return sha


def aplatir(concept: str) -> list[str]:
    vus, sortie = set(), []
    for fam, mots in CANDIDATS[concept].items():
        for m in mots:
            if not re.fullmatch(r"[a-z]+", m):
                sys.exit(f"REFUS mot-invalide : {m!r} ({concept}/{fam})")
            if m not in vus:
                vus.add(m)
                sortie.append(m)
    return sortie


def candidat(dossier: Path) -> None:
    bruts = {c: aplatir(c) for c in CANDIDATS}
    communs = set(bruts["tromperie"]) & set(bruts["enjeux"])
    journal, listes = [], {}
    for c, mots in bruts.items():
        garde = []
        for m in mots:
            if m in MOTS_OUTILS:
                journal.append(f"{c}\t{m}\tE1 mot outil")
            elif m in HOMOGRAPHES_CODE:
                journal.append(f"{c}\t{m}\tE2 homographe de code : {HOMOGRAPHES_CODE[m]}")
            elif m in HOMOGRAPHES_SENS:
                journal.append(f"{c}\t{m}\tE3 homographe : {HOMOGRAPHES_SENS[m]}")
            elif m in GENERIQUES_V2:
                journal.append(f"{c}\t{m}\tE4 {GENERIQUES_V2[m]}")
            elif m in communs:
                journal.append(f"{c}\t{m}\tE5 présent dans les deux listes candidates")
            else:
                garde.append(m)
        listes[c] = garde
    v2 = {"tromperie": CANDIDATS["tromperie"]["v2"], "enjeux": CANDIDATS["enjeux"]["v2"]}
    perdus_v2 = {c: [m for m in v2[c] if m not in listes[c]] for c in v2}
    note = ("Liste v3 CANDIDATE, 29 octobre 2026, construite avant toute lecture de sortie des lentilles. Étape 1 sur 2 : "
            "exclusions E1 à E5 appliquées ; E6 (mot sans jeton de début de mot) reste à appliquer par verifier-concepts. "
            "Méthode : regle-primaire-v3.md, section 2 ; outil : outils/construire_concepts_v3.py.")
    corps = {"_note": note, **{c: listes[c] for c in ("tromperie", "enjeux")}}
    p = dossier / "concepts-sondes-p3-v3-candidat.json"
    sha = ecrire_scelle(p, json.dumps(corps, ensure_ascii=False, indent=1) + "\n")
    lignes = [f"# exclusions E1 à E5, candidat {p.name} ({sha})",
              f"# bruts : tromperie {len(bruts['tromperie'])}, enjeux {len(bruts['enjeux'])} ; "
              f"communs (E5) : {sorted(communs)}",
              f"# gardés : tromperie {len(listes['tromperie'])}, enjeux {len(listes['enjeux'])}",
              f"# mots v2 perdus : {perdus_v2}", *journal]
    ecrire_scelle(dossier / "exclusions-concepts-v3.txt", "\n".join(lignes) + "\n")
    print("\n".join(lignes[:4]))


def final(dossier: Path, journal_verif: Path) -> None:
    p_c = dossier / "concepts-sondes-p3-v3-candidat.json"
    d = json.loads(p_c.read_text(encoding="utf-8"))
    texte = journal_verif.read_text(encoding="utf-8")
    if sha256_fichier(p_c)[:12] not in texte:
        sys.exit("REFUS journal-discordant : le journal ne nomme pas l'empreinte du candidat")
    sans = {"tromperie": [], "enjeux": []}
    vus = 0
    for l in texte.splitlines():
        parts = l.split("\t")
        if len(parts) == 4 and parts[0] in sans:
            vus += 1
            if parts[2] == "0":
                sans[parts[0]].append(parts[1])
    if vus != len(d["tromperie"]) + len(d["enjeux"]):
        sys.exit(f"REFUS journal-incomplet : {vus} lignes de mots, {len(d['tromperie']) + len(d['enjeux'])} attendues")
    listes = {c: [m for m in d[c] if m not in sans[c]] for c in sans}
    perdus_v2 = {c: [m for m in CANDIDATS[c]["v2"] if m not in listes[c]] for c in listes}
    note = ("Liste v3, 29 octobre 2026, figée avant toute lecture de sortie des lentilles sur les sondes non principales "
            "(aucune sortie réelle, v2 ou autre, n'a été lue par son auteur). Construite a priori (définitions de "
            "dictionnaire et thésaurus de mémoire, familles morphologiques) ; contient tous les mots de la v2 sauf ceux "
            f"qu'une règle d'exclusion retire ({perdus_v2}). Exclusions écrites d'avance : E1 mot outil, E2 homographe de code, "
            "E3 homographe de sens ou d'une autre langue, E4 générique retiré en v2, E5 mot présent dans les deux "
            "listes, E6 mot sans jeton de début de mot dans le vocabulaire de Llama-3.1 (tokenizer.json 79e3e522…). "
            f"Retirés par E6 : {sans}. Correspondance inchangée depuis la v2 : un espace initial puis exactement le mot, "
            "casse libre. Méthode : regle-primaire-v3.md, section 2 ; journal des exclusions : exclusions-concepts-v3.txt.")
    corps = {"_note": note, **listes}
    sha = ecrire_scelle(dossier / "concepts-sondes-p3-v3.json", json.dumps(corps, ensure_ascii=False, indent=1) + "\n")
    print(f"concepts-sondes-p3-v3.json {sha} ; tromperie {len(listes['tromperie'])}, enjeux {len(listes['enjeux'])} ; "
          f"E6 : {sans}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("etape", choices=("candidat", "final"))
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--journal-verification")
    a = ap.parse_args()
    dossier = Path(a.sortie)
    if a.etape == "candidat":
        candidat(dossier)
    else:
        final(dossier, Path(a.journal_verification))
    return 0


if __name__ == "__main__":
    sys.exit(main())
