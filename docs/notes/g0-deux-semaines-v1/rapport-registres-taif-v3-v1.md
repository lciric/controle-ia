# Rapport — registres pour le fonds, version 3 (promesses lues dans la candidature envoyée) — v1

- **Auteur** : développeur neuf (sous-agent, modèle Claude Fable 5.1), consigne de la session mère du 8 novembre 2026.
- **Heure** : 2026-11-08, de 14:59 à 15:15 UTC environ (`date -u` : 2026-11-08 15:12:12 UTC à la génération des tables).
- **Objet** : `scripts/registres_taif_v2.py` lisait les promesses de la table « promis → livré » dans
  `livrables/candidature-ea-funds-v1/proposal-v1.md` (version EA Funds : 91 740 USD, douze mois). La v3 les lit dans la
  candidature réellement envoyée au Transformative AI Fund le 7 octobre 2026 :
  `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` (texte extrait du PDF par `pdftotext -layout`,
  420 lignes, scellé, empreinte `b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0` ; 58 630 USD, sept mois
  à partir du 1er décembre 2026). Tout le reste du script est inchangé, hors les renvois de noms (v2 → v3).
- **Règles tenues** : aucune cellule ni aucun compte saisi à la main (tout vient du script) ; toute cellule sans source est
  vide ; aucune estimation ; aucune lecture de `donnees/`, de `diag/`, de `docs/notes/bras-attaque/` ni des résultats de
  `runs/` (manifestes seuls, comme la v2) ; aucun fichier existant modifié (script v2, essais v2, `livrables/registres-taif-v3/`
  et ses compagnons intacts) ; aucun `.sha256` écrit ; aucun commit, aucune poussée, aucun réseau, aucune clé, aucune
  dépense ; commandes longues sous `timeout 900 nice -n 10`. Les fichiers neufs sont : le script v3, les essais v3, le dossier
  `livrables/registres-taif-v4/` (six fichiers), ce rapport. Remarque : la session mère a pris des instantanés en cours de
  travail (commits `4d57da65`, `0f31746e`) ; les versions finales sont celles dont les empreintes suivent, la mère scelle.

## 1. Fichiers produits et empreintes (sha256, `sha256sum`, sans compagnon)

| fichier | sha256 |
|---|---|
| `scripts/registres_taif_v3.py` (1 626 lignes) | `3e4e15c0076a46211a045e5155391b6f91db997a31f08c2acb2f9d341d438e9b` |
| `tests/test_registres_taif_v3.py` (729 lignes, 26 fonctions d'essai, 28 cas) | `6a5d10f86bcb4ab00324f287ee48cb59827df1dd07297befd514809fdfcbe544` |
| `livrables/registres-taif-v4/promis-livre-v3.md` | `af868f16b4d1cb6b5cbcdf468305128147011df078a553443837e2d727c7514d` |
| `livrables/registres-taif-v4/calibration-v3.md` | `0f1bca5aa900bffed944b9f7c0b2b5f1b2a137b2b3c8337c9b0b28e3d881c0f4` |
| `livrables/registres-taif-v4/cout-par-resultat-v3.md` | `537fd93afdef88d47fe182f68611393f118e3d0341ce2013689c6639ca722d62` |
| `livrables/registres-taif-v4/total-depenses-v3.md` | `123be1a7e1c345574d451a0e4ee31f3193f6b7fc1a522f2e293934e03b94ea21` |
| `livrables/registres-taif-v4/journal-depenses-v3.txt` | `6c08483c3dc90f90f4f21aadc495f50dd0dcf5f1e91047f9e40501deb41d79c6` |
| `livrables/registres-taif-v4/sources-v3.json` | `a6d15d1a98a7ee37aa9d26fdc3b49c4143677e06a3e7bfe5c87b513beaeb9224` |

Commande : `PYTHONPATH=src timeout 900 nice -n 10 python scripts/registres_taif_v3.py --sortie livrables/registres-taif-v4`
(dossier neuf ; jour lu par `date -u`, jour seul : 2026-11-08 ; code de retour 0). **Déterminisme vérifié** : un second
lancement, dans la même minute, vers `/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/registres-v4-bis`
donne les mêmes octets pour les six fichiers (`diff -r` vide).

Le dossier de sortie par défaut du script est `livrables/registres-taif-v4/` et non `registres-taif-v3/` : ce dernier nom
porte déjà les sorties scellées de la v2 (fichiers `*-v2.*` et compagnons), qu'un lancement par défaut aurait écrasées (R12).

Essais : `PYTHONPATH=src timeout 900 nice -n 10 python -m pytest -q tests/test_registres_taif_v3.py` → **28 passés** (les 19
essais de la v2 repris et adaptés aux noms v3 et à la candidature factice à la mise en page extraite, plus 7 fonctions
nouvelles dont une paramétrée sur trois sections, soit 9 cas, un sain et un artefact par règle changée, section 3) ;
`tests/test_registres_taif_v2.py` → **19 passés** (toujours vert ; les deux fichiers ensemble : 47 passés en 1,8 s).

## 2. Diff v2 → v3 (`diff scripts/registres_taif_v2.py scripts/registres_taif_v3.py`, 415 lignes, tel quel)

```diff
2c2
< """Quatre tables pour l'entretien avec le Transformative AI Fund, produites par script, sans cellule saisie à la main — v2.
---
> """Quatre tables pour l'entretien avec le Transformative AI Fund, produites par script, sans cellule saisie à la main — v3.
4,6c4,7
< Sorties (dossier `livrables/registres-taif-v2/` par défaut) :
<     promis-livre-v2.md        une ligne par critère de la porte G0 et par promesse de la candidature (sections 6, 7, 8) ;
<     calibration-v2.md         une ligne par prédiction préenregistrée (préenregistrements scellés de `prereg/`), suivie
---
> Sorties (dossier `livrables/registres-taif-v4/` par défaut ; `livrables/registres-taif-v3/` porte les sorties scellées de la v2) :
>     promis-livre-v3.md        une ligne par critère de la porte G0 et par promesse de la candidature réellement envoyée au
>                               fonds le 7 octobre 2026 (sections 6, 7, 8 du texte extrait du PDF) ;
>     calibration-v3.md         une ligne par prédiction préenregistrée (préenregistrements scellés de `prereg/`), suivie
8,11c9,12
<     cout-par-resultat-v2.md   une ligne par run décisif et par GO de calcul (registre des dépenses) ;
<     total-depenses-v2.md      somme des dépenses de la phase 0 par un analyseur strict du registre des dépenses ;
<     journal-depenses-v2.txt   chaque ligne du registre des dépenses non sommée, avec sa raison ;
<     sources-v2.json           chaque cellule non vide → chemin, ligne(s), empreinte sha256 du fichier lu ; `comptes` ;
---
>     cout-par-resultat-v3.md   une ligne par run décisif et par GO de calcul (registre des dépenses) ;
>     total-depenses-v3.md      somme des dépenses de la phase 0 par un analyseur strict du registre des dépenses ;
>     journal-depenses-v3.txt   chaque ligne du registre des dépenses non sommée, avec sa raison ;
>     sources-v3.json           chaque cellule non vide → chemin, ligne(s), empreinte sha256 du fichier lu ; `comptes` ;
14c15,34
< Changements de règle par rapport à la v1 (`scripts/registres_taif_v1.py`, intacte) :
---
> Changement par rapport à la v2 (`scripts/registres_taif_v2.py`, intacte) — seule la source des promesses change :
>     la table « promis → livré » lit la candidature envoyée au fonds, `docs/sources/candidature-taif-2026-10-07/
>     proposal_v2_TAIF_2026-10-07.txt` (texte extrait du PDF par `pdftotext -layout`, scellé), et non plus la version
>     EA Funds `livrables/candidature-ea-funds-v1/proposal-v1.md`. Règles de lecture de la mise en page extraite
>     (`section_texte`, `items_indentes`, `table_alignee`) : un titre de section est une ligne « N. Titre » à la colonne 0,
>     la section court jusqu'au titre suivant ; les puces de la section 6 et de la section 8 ont perdu leur glyphe :
>     une puce est une suite de lignes indentées, une puce nouvelle commence à une ligne indentée qui débute par une
>     majuscule quand la puce courante finit par une fin de phrase (« . », « ! », « ? »), ou à une ligne numérotée
>     « 1. », « 2. » ; une ligne à la colonne 0 ou vide clôt la puce ; le paragraphe « Gate G0 » est la suite des lignes
>     à la colonne 0 qui commence par « Gate G0 » ; la table de la section 7 a ses colonnes alignées par espaces :
>     les débuts de colonnes sont ceux des cellules de la ligne d'en-tête (« Months », « Period », « Work », « Gates… »),
>     une ligne dont la cellule « Months » commence par un chiffre ouvre une ligne de calendrier, une ligne indentée
>     dont la cellule « Months » est vide la continue (cellules recollées par un espace), une ligne vide ou à la colonne 0
>     la clôt. Une section absente, un en-tête de table absent : aucune ligne pour cette section et un signalement
>     (`signalements` de `sources-v3.json`), jamais une exception ni une ligne devinée. Les identifiants gardent la
>     convention de la v2 : C6-k dans l'ordre du texte, C6-G0, C7-k par ligne du calendrier, C8-k par livrable puis par
>     critère de succès. La date promise des lignes C8 vient du titre de la section 7 (« seven months from 1 December
>     2026 »). Calibration, coût par résultat, total des dépenses, sources, déterminisme : inchangés.
> 
> Changements de règle de la v2 par rapport à la v1 (`scripts/registres_taif_v1.py`, intacte), repris tels quels :
17,18c37,38
<        calibration rendue (`compter_issues_table_md`), jamais saisis ; ils sont écrits en fin de `calibration-v2.md` et
<        sous la clé `comptes` de `sources-v2.json`.
---
>        calibration rendue (`compter_issues_table_md`), jamais saisis ; ils sont écrits en fin de `calibration-v3.md` et
>        sous la clé `comptes` de `sources-v3.json`.
39c59
<     PYTHONPATH=src python scripts/registres_taif_v2.py [--racine .] [--sortie livrables/registres-taif-v2] [--jour AAAA-MM-JJ]
---
>     PYTHONPATH=src python scripts/registres_taif_v3.py [--racine .] [--sortie livrables/registres-taif-v4] [--jour AAAA-MM-JJ]
53c73
< VERSION = "registres-taif-v2"
---
> VERSION = "registres-taif-v3"
78c98
<     "candidature": "livrables/candidature-ea-funds-v1/proposal-v1.md",
---
>     "candidature": "docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt",
733a754,873
> # Mise en page du texte extrait du PDF envoyé (`pdftotext -layout`) : titres « N. Titre » à la colonne 0, puces sans glyphe,
> # table du calendrier à colonnes alignées par espaces (v3).
> _TITRE_SECTION_TEXTE = re.compile(r"^\x0c?(\d{1,2})\. \S")        # un saut de page (« \x0c ») peut précéder un titre
> _ITEM_NUMEROTE = re.compile(r"^\s+(\d+)\.\s+(\S.*)$")
> _FIN_DE_PHRASE = re.compile(r"[.!?]\s*$")
> _LIGNE_INDENTEE = re.compile(r"^\s+(\S.*)$")
> _CELLULE_ALIGNEE = re.compile(r"\S+(?: \S+)*")                # une cellule : des mots séparés d'un seul espace
> _ENTETE_CALENDRIER = re.compile(r"^\s*Months\s{2,}Period\s{2,}Work\s{2,}\S")
> TOLERANCE_COLONNE = 2
> 
> 
> class FichierTexte(Fichier):
>     """Texte extrait d'un PDF : lignes coupées sur « \\n » seul, pour que les numéros cités soient ceux du fichier
>     (`str.splitlines` couperait aussi sur les sauts de page « \\x0c » de `pdftotext`, et décalerait tous les numéros)."""
> 
>     def __init__(self, racine: Path, rel: str, scelle: bool = False):
>         super().__init__(racine, rel, scelle)
>         self.lignes = self.chemin.read_text(encoding="utf-8").split("\n")
>         if self.lignes and self.lignes[-1] == "":            # fin de fichier : pas une ligne de plus
>             self.lignes.pop()
> 
> 
> def section_texte(f: Fichier, numero: int) -> tuple[tuple[int, str] | None, list[tuple[int, str]]]:
>     """Section « N. Titre » d'un texte extrait : (ligne de titre, lignes jusqu'au prochain titre « M. … » à la colonne 0).
>     Sans titre portant ce numéro : (None, [])."""
>     for i, l in enumerate(f.lignes):
>         m = _TITRE_SECTION_TEXTE.match(l)
>         if m and int(m.group(1)) == numero:
>             fin = len(f.lignes)
>             for j in range(i + 1, len(f.lignes)):
>                 if _TITRE_SECTION_TEXTE.match(f.lignes[j]):
>                     fin = j
>                     break
>             return (i + 1, l), [(k + 1, f.lignes[k]) for k in range(i + 1, fin)]
>     return None, []
> 
> 
> def items_indentes(lignes: list[tuple[int, str]]) -> list[dict]:
>     """Puces d'une liste dont le glyphe a été perdu à l'extraction : [{'lignes': [n°…], 'texte': '…'}].
>     Une puce est une suite de lignes indentées. Une puce nouvelle commence à une ligne indentée numérotée (« 1. »), ou à
>     une ligne indentée qui débute par une majuscule quand la puce courante finit par une fin de phrase (« . », « ! »,
>     « ? ») ; toute autre ligne indentée continue la puce courante (recollée par un espace). Une ligne vide ou à la
>     colonne 0 clôt la puce courante (les étiquettes « Deliverables. », « Success. » et le paragraphe « Gate G0 » ne sont
>     pas des puces)."""
>     items: list[dict] = []
>     courante: dict | None = None
>     for no, l in lignes:
>         m_num = _ITEM_NUMEROTE.match(l)
>         m_ind = _LIGNE_INDENTEE.match(l)
>         if m_num:
>             courante = {"lignes": [no], "texte": m_num.group(2).strip()}
>             items.append(courante)
>         elif m_ind:
>             texte = m_ind.group(1).strip()
>             nouvelle = courante is None or (texte[:1].isupper() and bool(_FIN_DE_PHRASE.search(courante["texte"])))
>             if nouvelle:
>                 courante = {"lignes": [no], "texte": texte}
>                 items.append(courante)
>             else:
>                 courante["lignes"].append(no)
>                 courante["texte"] = f"{courante['texte']} {texte}"
>         else:
>             courante = None
>     return items
> 
> 
> def paragraphe_colonne_0(lignes: list[tuple[int, str]], debut: str) -> tuple[list[int], str]:
>     """Paragraphe à la colonne 0 qui commence par `debut` : ses lignes consécutives non vides, recollées par un espace."""
>     nos, textes = [], []
>     for no, l in lignes:
>         l = l.lstrip("\x0c")                                  # un saut de page devant la ligne ne l'indente pas
>         if not nos:
>             if l.startswith(debut):
>                 nos.append(no)
>                 textes.append(l.strip())
>         elif l.strip() and not l.startswith((" ", "\t", "\x0c")):
>             nos.append(no)
>             textes.append(l.strip())
>         else:
>             break
>     return nos, " ".join(textes)
> 
> 
> def table_alignee(lignes: list[tuple[int, str]]) -> tuple[list[dict], str]:
>     """Table d'un texte extrait avec `-layout` (section 7) : ([{'lignes': [n°…], 'cellules': [...]}], erreur).
>     Les débuts de colonnes sont les positions des cellules de la ligne d'en-tête (« Months », « Period », « Work »,
>     « Gates and outputs ») ; une cellule d'une ligne va à la dernière colonne dont le début est ≤ sa position + tolérance.
>     Une ligne dont la première cellule commence par un chiffre ouvre une ligne de calendrier ; une ligne indentée dont la
>     première cellule est vide la continue (cellules recollées par un espace) ; une ligne vide ou à la colonne 0 la clôt
>     et finit la table. Sans en-tête : ([], raison)."""
>     entete = next(((no, l) for no, l in lignes if _ENTETE_CALENDRIER.match(l)), None)
>     if entete is None:
>         return [], "en-tête « Months … Period … Work … » absent"
>     debuts = [m.start() for m in _CELLULE_ALIGNEE.finditer(entete[1])]
> 
>     def cellules(l: str) -> list[str]:
>         cells = [""] * len(debuts)
>         for m in _CELLULE_ALIGNEE.finditer(l):
>             k = max((i for i, d in enumerate(debuts) if d <= m.start() + TOLERANCE_COLONNE), default=0)
>             cells[k] = f"{cells[k]} {m.group(0)}".strip()
>         return cells
> 
>     rangs: list[dict] = []
>     courante: dict | None = None
>     for no, l in lignes:
>         if no <= entete[0]:
>             continue
>         l = l.replace("\x0c", " ")                            # un saut de page garde la position des colonnes
>         c = cellules(l)
>         if c[0] and c[0][0].isdigit():
>             courante = {"lignes": [no], "cellules": c}
>             rangs.append(courante)
>         elif courante is not None and not c[0] and l.startswith(" ") and l.strip():
>             courante["lignes"].append(no)
>             courante["cellules"] = [f"{a} {b}".strip() for a, b in zip(courante["cellules"], c)]
>         elif rangs:
>             break
>     return rangs, "" if rangs else "aucune ligne de calendrier sous l'en-tête"
> 
> 
735,736c875,876
<     T = "promis-livre-v2"
<     cand = Fichier(racine, CHEMINS["candidature"], scelle=True)
---
>     T = "promis-livre-v3"
>     cand = FichierTexte(racine, CHEMINS["candidature"], scelle=True)
829,892c969,1045
<     # (b) Candidature, section 6 « Progress to date » : chaque puce est une promesse de ce qui existe.
<     s6 = cand.section(r"^6\. Progress to date")
<     titre6 = next((l for _, l in cand.chercher(r"^## 6\. ")), "")
<     periode6 = re.sub(r"^## 6\. Progress to date\s*", "", titre6).strip("() ")
<     k = 0
<     for no, l in s6:
<         m = re.match(r"^- \*\*(.+?)\*\*\s*(.*)$", l)
<         if m:
<             k += 1
<             lid = f"C6-{k}"
<             texte = f"{m.group(1)} {m.group(2)}"
<             tache = next((t for motif, t in REGLES_CANDIDATURE if re.search(motif, texte, re.I)), None)
<             S.cellule(T, lid, "promesse", cand, [no])
<             S.cellule(T, lid, "date_promise", cand, [no])
<             piece, sha = piece_de_tache(tache, lid)
<             lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(texte, 260),
<                            "date_promise": f"déclaré fait à la candidature ({periode6})", "etat": etat_de_tache(tache, lid),
<                            "piece": piece, "sha256": sha, "glissement": glissement(tache, lid)})
<         elif l.startswith("Gate G0"):
<             lid = "C6-G0"
<             S.cellule(T, lid, "promesse", cand, [no])
<             S.cellule(T, lid, "date_promise", cand, [no])
<             m2 = re.search(r"\(([^)]*\d{4})\)", l)
<             etat_txt, gl = "", ""
<             if crit_etat["ligne"]:
<                 etat_txt = (f"prouvés : {', '.join(sorted(crit_etat['prouves']))} ; "
<                             f"restent : {', '.join(sorted(crit_etat['restent']))}")
<                 S.cellule(T, lid, "etat", etat, [crit_etat["ligne"]])
<             if noeud_g0:
<                 gl = tronquer(re.sub(r"^.*?Porte de sortie\s*:\s*", "", noeud_g0[0][1]), 160)
<                 S.cellule(T, lid, "glissement", etat, [noeud_g0[0][0]])
<             if n027:
<                 S.cellule(T, lid, "glissement_decision", deci, [n027[0][0]])
<             lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(l, 300),
<                            "date_promise": m2.group(1) if m2 else "", "etat": etat_txt, "piece": "", "sha256": "",
<                            "glissement": gl})
< 
<     # (c) Candidature, section 7 « Timeline » : une ligne par période.
<     k = 0
<     for no, l in cand.section(r"^7\. Timeline"):
<         c = cellules_table(l)
<         if len(c) >= 4 and re.match(r"^\d", c[0]):
<             k += 1
<             lid = f"C7-{k}"
<             S.cellule(T, lid, "promesse", cand, [no])
<             S.cellule(T, lid, "date_promise", cand, [no])
<             etat_txt = etat_periode(c[1], jour)
<             if etat_txt:
<                 S.cellule(T, lid, "etat", cand, [no], "période de la ligne comparée au jour du script")
<             lignes.append({"id": lid, "source": "candidature, section 7", "promesse": tronquer(f"{c[2]} → {c[3]}", 260),
<                            "date_promise": f"mois {c[0]} ({c[1]})", "etat": etat_txt, "piece": "", "sha256": "", "glissement": ""})
< 
<     # (d) Candidature, section 8 « Deliverables and success criteria ».
<     k = 0
<     for no, l in cand.section(r"^8\. Deliverables"):
<         m = re.match(r"^(?:- |\d+\. )(.*)$", l)
<         if m:
<             k += 1
<             lid = f"C8-{k}"
<             S.cellule(T, lid, "promesse", cand, [no])
<             S.cellule(T, lid, "date_promise", cand, [no])
<             lignes.append({"id": lid, "source": "candidature, section 8", "promesse": tronquer(m.group(1), 260),
<                            "date_promise": "fin des 12 mois (section 7)", "etat": "", "piece": "", "sha256": "",
<                            "glissement": ""})
---
>     # (b) Candidature envoyée, section 6 « Progress to date » : chaque puce (glyphe perdu à l'extraction) est une promesse
>     # de ce qui existe ; le paragraphe « Gate G0 » à la colonne 0 donne la ligne C6-G0.
>     titre6, s6 = section_texte(cand, 6)
>     if titre6 is None or not re.match(r"^6\. Progress to date", titre6[1]):
>         S.signaler("section 6 « Progress to date » absente de la candidature : aucune ligne C6", cand, titre6[0] if titre6 else 0,
>                    titre6[1] if titre6 else "")
>         s6 = []
>     periode6 = re.sub(r"^6\. Progress to date\s*", "", titre6[1]).strip("() ") if titre6 else ""
>     for k, it in enumerate(items_indentes(s6), 1):
>         lid = f"C6-{k}"
>         texte = it["texte"]
>         tache = next((t for motif, t in REGLES_CANDIDATURE if re.search(motif, texte, re.I)), None)
>         S.cellule(T, lid, "promesse", cand, it["lignes"])
>         S.cellule(T, lid, "date_promise", cand, it["lignes"] + [titre6[0]], "puce de la section 6 ; période lue dans le titre de la section")
>         piece, sha = piece_de_tache(tache, lid)
>         lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(texte, 260),
>                        "date_promise": f"déclaré fait à la candidature ({periode6})", "etat": etat_de_tache(tache, lid),
>                        "piece": piece, "sha256": sha, "glissement": glissement(tache, lid)})
>     nos_g0, texte_g0 = paragraphe_colonne_0(s6, "Gate G0")
>     if nos_g0:
>         lid = "C6-G0"
>         S.cellule(T, lid, "promesse", cand, nos_g0)
>         S.cellule(T, lid, "date_promise", cand, nos_g0)
>         m2 = re.search(r"\(([^)]*\d{4})\)", texte_g0)
>         etat_txt, gl = "", ""
>         if crit_etat["ligne"]:
>             etat_txt = (f"prouvés : {', '.join(sorted(crit_etat['prouves']))} ; "
>                         f"restent : {', '.join(sorted(crit_etat['restent']))}")
>             S.cellule(T, lid, "etat", etat, [crit_etat["ligne"]])
>         if noeud_g0:
>             gl = tronquer(re.sub(r"^.*?Porte de sortie\s*:\s*", "", noeud_g0[0][1]), 160)
>             S.cellule(T, lid, "glissement", etat, [noeud_g0[0][0]])
>         if n027:
>             S.cellule(T, lid, "glissement_decision", deci, [n027[0][0]])
>         lignes.append({"id": lid, "source": "candidature, section 6", "promesse": tronquer(texte_g0, 300),
>                        "date_promise": m2.group(1) if m2 else "", "etat": etat_txt, "piece": "", "sha256": "",
>                        "glissement": gl})
>     elif s6:
>         S.signaler("paragraphe « Gate G0 » absent de la section 6 : aucune ligne C6-G0", cand, titre6[0], titre6[1])
> 
>     # (c) Candidature envoyée, section 7 « Timeline » : une ligne par ligne du calendrier (table à colonnes alignées,
>     # une ligne de calendrier peut courir sur plusieurs lignes physiques, recollées).
>     titre7, s7 = section_texte(cand, 7)
>     if titre7 is None or not re.match(r"^7\. Timeline", titre7[1]):
>         S.signaler("section 7 « Timeline » absente de la candidature : aucune ligne C7", cand, titre7[0] if titre7 else 0,
>                    titre7[1] if titre7 else "")
>         titre7, s7 = None, []
>     rangs, erreur7 = table_alignee(s7) if s7 else ([], "")
>     if erreur7:
>         S.signaler(f"table de la section 7 illisible ({erreur7}) : aucune ligne C7", cand, titre7[0], titre7[1])
>     for k, r in enumerate(rangs, 1):
>         lid = f"C7-{k}"
>         c = r["cellules"] + [""] * max(0, 4 - len(r["cellules"]))
>         S.cellule(T, lid, "promesse", cand, r["lignes"])
>         S.cellule(T, lid, "date_promise", cand, r["lignes"])
>         etat_txt = etat_periode(c[1], jour)
>         if etat_txt:
>             S.cellule(T, lid, "etat", cand, r["lignes"], "période de la ligne comparée au jour du script")
>         lignes.append({"id": lid, "source": "candidature, section 7", "promesse": tronquer(f"{c[2]} → {c[3]}", 260),
>                        "date_promise": f"mois {c[0]} ({c[1]})", "etat": etat_txt, "piece": "", "sha256": "", "glissement": ""})
> 
>     # (d) Candidature envoyée, section 8 « Deliverables and success criteria » : livrables (puces sans glyphe) puis
>     # critères de succès (numérotés « 1. ») ; la date promise est la période du titre de la section 7.
>     titre8, s8 = section_texte(cand, 8)
>     if titre8 is None or not re.match(r"^8\. Deliverables", titre8[1]):
>         S.signaler("section 8 « Deliverables and success criteria » absente de la candidature : aucune ligne C8", cand,
>                    titre8[0] if titre8 else 0, titre8[1] if titre8 else "")
>         s8 = []
>     periode7 = re.sub(r"^7\. Timeline\s*", "", titre7[1]).strip("() ") if titre7 else ""
>     date_c8 = f"fin de la période (section 7 : {periode7})" if periode7 else ""
>     for k, it in enumerate(items_indentes(s8), 1):
>         lid = f"C8-{k}"
>         S.cellule(T, lid, "promesse", cand, it["lignes"])
>         if date_c8:
>             S.cellule(T, lid, "date_promise", cand, it["lignes"] + [titre7[0]], "période lue dans le titre de la section 7")
>         lignes.append({"id": lid, "source": "candidature, section 8", "promesse": tronquer(it["texte"], 260),
>                        "date_promise": date_c8, "etat": "", "piece": "", "sha256": "", "glissement": ""})
1061c1214
<     T = "calibration-v2"
---
>     T = "calibration-v3"
1169c1322
<     T = "cout-par-resultat-v2"
---
>     T = "cout-par-resultat-v3"
1274c1427
<     T = "total-depenses-v2"
---
>     T = "total-depenses-v3"
1324c1477
<     out = ["# Total des dépenses de la phase 0 — v2", "",
---
>     out = ["# Total des dépenses de la phase 0 — v3", "",
1330c1483
<            "(« premier relevé », « cumulés », « déjà imputé ») ou une fourchette vont au journal `journal-depenses-v2.txt`, "
---
>            "(« premier relevé », « cumulés », « déjà imputé ») ou une fourchette vont au journal `journal-depenses-v3.txt`, "
1333c1486
<            f"Jour du script (`date -u`) : {jour}. Version : `{VERSION}`. Sources de chaque cellule : `sources-v2.json`.", "",
---
>            f"Jour du script (`date -u`) : {jour}. Version : `{VERSION}`. Sources de chaque cellule : `sources-v3.json`.", "",
1338c1491
<            "Le total relevé est la valeur de la clé `total_depenses_phase0` de `sources-v2.json` (marqueur `<<TOTAL_DEPENSES_PHASE0>>` de la page pour le fonds).", "",
---
>            "Le total relevé est la valeur de la clé `total_depenses_phase0` de `sources-v3.json` (marqueur `<<TOTAL_DEPENSES_PHASE0>>` de la page pour le fonds).", "",
1364c1517
<            "Sources de chaque cellule : `sources-v2.json`.", "",
---
>            "Sources de chaque cellule : `sources-v3.json`.", "",
1404c1557
<         "Registre de calibration des prédictions préenregistrées — v2",
---
>         "Registre de calibration des prédictions préenregistrées — v3",
1408c1561
<         "citées dans `sources-v2.json`) ; « sans objet » est une issue à part ; sans verdict scellé : ligne du registre des "
---
>         "citées dans `sources-v3.json`) ; « sans objet » est une issue à part ; sans verdict scellé : ligne du registre des "
1415,1417c1568,1571
<         "promis-livre-v2.md": rendre_table(
<             "Promis → livré — v2", "Une ligne par critère de la porte G0 (programme v2) et par promesse de la candidature "
<             "(sections 6, 7, 8 de `proposal-v1.md`). L'état et la cause du glissement viennent de `registres/etat.md` ; "
---
>         "promis-livre-v3.md": rendre_table(
>             "Promis → livré — v3", "Une ligne par critère de la porte G0 (programme v2) et par promesse de la candidature "
>             "envoyée au fonds le 7 octobre 2026 (sections 6, 7, 8 de "
>             f"`{CHEMINS['candidature']}`, texte extrait du PDF). L'état et la cause du glissement viennent de `registres/etat.md` ; "
1420,1422c1574,1576
<         "calibration-v2.md": calib_md,
<         "cout-par-resultat-v2.md": rendre_table(
<             "Coût réel par résultat — v2",
---
>         "calibration-v3.md": calib_md,
>         "cout-par-resultat-v3.md": rendre_table(
>             "Coût réel par résultat — v3",
1427c1581
<             "Le total strict de la phase 0 est dans `total-depenses-v2.md`.",
---
>             "Le total strict de la phase 0 est dans `total-depenses-v3.md`.",
1429,1430c1583,1584
<         "total-depenses-v2.md": rendre_total_depenses(A, par_go, par_tache, jour),
<         "journal-depenses-v2.txt": rendre_journal_depenses(A, jour),
---
>         "total-depenses-v3.md": rendre_total_depenses(A, par_go, par_tache, jour),
>         "journal-depenses-v3.txt": rendre_journal_depenses(A, jour),
1436,1437c1590,1591
<               "comptes": {"promis-livre-v2": len(promis), "calibration-v2": len(calib), "cout-par-resultat-v2": len(cout),
<                           "total-depenses-v2": {"par_go": len(par_go), "par_tache": len(par_tache)},
---
>               "comptes": {"promis-livre-v3": len(promis), "calibration-v3": len(calib), "cout-par-resultat-v3": len(cout),
>                           "total-depenses-v3": {"par_go": len(par_go), "par_tache": len(par_tache)},
1445c1599
<     (sortie / "sources-v2.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
---
>     (sortie / "sources-v3.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
1453c1607
<     ap.add_argument("--sortie", default="livrables/registres-taif-v2")
---
>     ap.add_argument("--sortie", default="livrables/registres-taif-v4")
```

Lecture du diff : (i) en-tête de module (docstring : sorties v3, paragraphe « Changement par rapport à la v2 », commande) ;
(ii) `VERSION`, `CHEMINS["candidature"]`, défaut de `--sortie` ; (iii) un bloc neuf de 120 lignes avant `table_promis`
(expressions régulières de la mise en page extraite, `FichierTexte`, `section_texte`, `items_indentes`,
`paragraphe_colonne_0`, `table_alignee`) ; (iv) les blocs (b), (c), (d) de `table_promis` réécrits pour cette mise en page ;
(v) partout ailleurs, seuls les renvois de noms (`-v2` → `-v3` dans les noms de fichiers de sortie, les clés de `comptes`
et de `cellules`, les titres « — v2 » → « — v3 », la phrase « sections 6, 7, 8 de `proposal-v1.md` » → chemin du texte
envoyé). Les fonctions de calibration, de coût par résultat, du total des dépenses, du journal, du rendu et de `construire`
ne changent que par ces renvois : `grep` des différences hors des zones (i) à (iv) ne montre que des lignes portant « v2 »
ou « v3 ».

`FichierTexte` est nécessaire pour la provenance : `str.splitlines()` (classe `Fichier`, inchangée) coupe aussi sur les
huit sauts de page « \x0c » du texte extrait (l. 51, 101, 154, 207, 258, 312, 365, 421), ce qui décalait tous les numéros de
ligne cités de cinq à six ; la coupe sur « \n » seul rend les numéros du fichier (essai
`test_fichier_texte_numeros_de_ligne_malgre_les_sauts_de_page`). Un saut de page devant un titre (« \x0c4. Two papers… »,
l. 101) est un titre quand même.

## 3. Comptes (ceux du script, cités tels quels)

`livrables/registres-taif-v4/sources-v3.json`, clé `comptes` :

```
{"calibration": {"confirmees": 47, "non_concluantes": 8, "par_issue": {"confirmée": 47, "contradictoire": 9,
  "mixte (plusieurs identifiants, issues différentes)": 1, "non atteinte": 6, "non citée par le verdict": 20, "non concluante": 8,
  "non déclenchée": 2, "non encore lue (run décisif fait, aucun verdict scellé)": 15, "rapportée sans verdict (descriptive)": 3,
  "registre des décisions (sans verdict scellé)": 58, "réfutée": 5, "sans objet": 6, "sans run décisif cité par un manifeste": 55},
  "refutees": 5, "sans_objet": 6, "taux_confirmation": "47 / 60 = 0,783", "taux_confirmation_valeur": 0.7833, "total": 235, "tranchees": 60},
 "calibration-v3": 235, "cout-par-resultat-v3": 199, "manifestes_lus": 45, "preregs_lus": 39, "promis-livre-v3": 31,
 "total-depenses-v3": {"par_go": 118, "par_tache": 9}, "verdicts_lus": 17}
```

Dépenses (clés `total_depenses_phase0` et `total_depenses_phase0_detail`) : **`"645,42"`** ;
`{"estime_usd_a_part": "111,87", "lignes_estimees": 50, "lignes_non_sommees": 187, "lignes_sommees": 136, "releve_usd": "645,42"}`.
Signalements : 221 (187 « dépense non sommée », 23 « dépense sans GO cité sur la ligne », 11 « GO cité sous forme abrégée,
non résolu ») ; **aucun signalement sur la candidature** (les trois sections et l'en-tête du calendrier sont lus). Fichiers
lus : 100, chacun avec son empreinte dans `fichiers_lus`.

**Promis → livré : 31 lignes (v3) contre 31 (v2)** : 8 critères de G0 (programme), 7 puces de la section 6 + C6-G0, 6 lignes
du calendrier (section 7), 9 lignes de la section 8 (5 livrables, 4 critères de succès) ; cellules vides : 83 sur 248 (même
compte que la v2, par coïncidence de structure : la candidature envoyée a autant de puces et de lignes que la version EA Funds).

**Comparaison avec `livrables/registres-taif-v3/sources-v2.json` (sorties scellées de la v2, générées plus tôt le 8 novembre)** :
promis-livre 31 = 31 ; calibration 235 lignes = 235 ; total relevé 645,42 USD = 645,42 USD ; lignes sommées 136 = 136. Mais
les comptes par issue (sorties scellées : 44 confirmées / 55 tranchées = 0,800, 16 verdicts lus ; v4 : 47 / 60 = 0,783,
17 verdicts lus), le coût par résultat (198 → 199 lignes), les totaux par GO (117 → 118), l'estimé à part (111,85 → 111,87 USD,
49 → 50 lignes) et le journal (185 → 187 lignes) **ne sont pas identiques**. La cause n'est pas le script : les registres ont
bougé entre les deux générations (`registres/depenses.md` `6f783d583ff0…` → `a6437706f864…` ; `registres/decisions.md`
`591132d8a6e2…` → `1b4d912f0745…` ; `registres/etat.md` et `registres/go.md` aussi ; un verdict de plus,
`docs/verdicts/verdict-etiqueteur-phase1-v1.md`). Preuve : le script v2 intact, relancé à la même seconde que la v3
(15:12:12 UTC, vers le bloc-notes), donne exactement les mêmes comptes (`calibration`, `cout-par-resultat`, `total-depenses`,
`total_depenses_phase0_detail`, 221 signalements) et les mêmes empreintes de fichiers lus hors candidature ; ses quatre
tables communes (`calibration`, `cout-par-resultat`, `total-depenses`, `journal-depenses`) sont **identiques à l'octet** aux
tables v3 une fois les renvois de noms substitués (`-v2` → `-v3`, « — v2 » → « — v3 »). Seule la source des promesses change,
comme demandé ; les chiffres opposables sont ceux du lancement scellé par la mère, pas ceux de ce rapport.

## 4. Les changements de règle et leurs essais

Mise en page du texte extrait (`pdftotext -layout`) : les titres de section sont des lignes « N. Titre » à la colonne 0
(pas de `#`) ; les glyphes de puces des sections 6 et 8 sont perdus (toutes les lignes d'une liste sont indentées de quatre ou
cinq espaces, la première ligne d'une puce comme ses suites) ; la table de la section 7 a quatre colonnes alignées par
espaces (débuts aux positions 1, 12, 31, 106) et une ligne du calendrier court sur deux ou trois lignes physiques ; les
critères de succès sont numérotés « 1. » à « 4. », indentés.

**Règle 1 — section d'un texte extrait** (`section_texte`) : titre `^\x0c?(\d{1,2})\. \S`, section jusqu'au titre suivant.
Sain : sections 6, 7, 8 trouvées aux lignes 266, 287, 307 (titre 6 : « 6. Progress to date (phase 0, since 5 October 2026) »,
d'où la date promise « déclaré fait à la candidature (phase 0, since 5 October 2026) », inchangée). Artefact : section
absente → aucune ligne pour elle, un signalement, les autres sections et les critères de G0 rendus, aucune exception
(`test_section_absente_aucune_ligne_et_signalement`, paramétré sur 6, 7, 8) ; sans section 7, la date promise des lignes
C8 reste vide (cellule sans source).

**Règle 2 — puces sans glyphe** (`items_indentes`) : une puce nouvelle commence à une ligne indentée numérotée, ou à une
ligne indentée qui débute par une majuscule quand la puce courante finit par « . », « ! » ou « ? » ; toute autre ligne
indentée continue la puce (recollée par un espace) ; une ligne vide ou à la colonne 0 clôt la puce. Sain : sur le texte
réel, les sept puces de la section 6 (l. 267 à 283) et les neuf de la section 8 sont rendues telles que le texte les écrit
(section 5) ; sur la candidature factice, une puce de trois lignes dont la deuxième commence par une majuscule
(« H200 … ») sans fin de phrase avant elle reste une seule puce (`test_section6_puces_recollees`). Artefact (limite écrite
de la règle) : une puce dont une phrase finit en bout de ligne et dont la suite reprend par une majuscule serait coupée en
deux (`test_section8_livrables_puis_criteres_numerotes`, dernier bloc) ; le texte réel n'a pas ce cas (vérifié ligne à
ligne, section 5). Le paragraphe « Gate G0 » (deux lignes à la colonne 0, l. 284-285) est recollé par
`paragraphe_colonne_0` ; absent → signalement (`test_section6_sans_paragraphe_gate_g0_signale`).

**Règle 3 — table du calendrier** (`table_alignee`) : débuts de colonnes lus sur la ligne d'en-tête « Months … Period …
Work … Gates and outputs » ; une cellule va à la dernière colonne dont le début est ≤ sa position + 2 ; une ligne dont la
cellule « Months » commence par un chiffre ouvre une ligne de calendrier, une ligne indentée dont la cellule « Months » est
vide la continue, une ligne vide ou à la colonne 0 la clôt et finit la table. Sain : les six lignes du calendrier réel
(l. 289-291, 292-293, 294-295, 296-297, 298-300, 301-302) sont recollées ; sur la candidature factice, une ligne coupée en
trois (cellule « Work ») et une coupée en deux (cellule « Gates ») donnent une ligne C7 chacune, période telle que le texte
(`test_section7_ligne_du_calendrier_coupee_recollee`). Artefact : en-tête absent → aucune ligne C7, signalement « table de
la section 7 illisible (en-tête « Months … Period … Work … » absent) », section 8 rendue quand même, aucune exception
(`test_section7_sans_entete_signalee_sans_exception`) ; en-tête sans ligne de calendrier → raison « aucune ligne de
calendrier sous l'en-tête ».

**Règle 4 — date promise des lignes C8** : la v2 écrivait « fin des 12 mois (section 7) » en dur ; la v3 la lit dans le
titre de la section 7 : « fin de la période (section 7 : seven months from 1 December 2026) », et cite la ligne du titre
(287) avec la ligne de la puce dans `sources-v3.json`.

**Numéros de ligne** (`FichierTexte`) : voir section 2 ; essai sain et artefact dans
`test_fichier_texte_numeros_de_ligne_malgre_les_sauts_de_page` (`Fichier` citerait la ligne 11 pour un titre qui est la
ligne 10 du fichier factice).

## 5. Vérification à la main : chaque promesse est une phrase du texte envoyé

Lecture du texte `proposal_v2_TAIF_2026-10-07.txt` (l. 266-319) contre `promis-livre-v3.md` et les lignes citées par
`sources-v3.json` (`cellules.promis-livre-v3.<id>.promesse.lignes`). Les apostrophes courbes du texte (« pilot’s »,
« paper’s ») sont gardées telles quelles.

| id | lignes citées | début de la promesse (texte envoyé) | date promise rendue | vérifié |
|---|---|---|---|---|
| C6-1 | 267-269 | « Literature verified on primary sources. We retrieved and hashed 98 arXiv PDFs. … 147 correction lines on our own documents. » | déclaré fait à la candidature (phase 0, since 5 October 2026) | oui, trois lignes recollées |
| C6-2 | 270-271 | « Theory. A mathematical note fixes … confirmed 31 of 31 predictions. » | idem | oui |
| C6-3 | 272-275 | « Activation harness validated on Llama-3.1-8B-Instruct, on a rented H200 (criterion 1 of gate G0), … and tested guards. » (tronquée à 260 caractères dans la cellule, règle de la v2) | idem | oui, quatre lignes |
| C6-4 | 276-278 | « Research-sabotage environment v0 under construction. … The pilot runs before the grant starts. » (tronquée à 260) | idem | oui, trois lignes |
| C6-5 | 279-281 | « Code, with tests: model-organism adapters … In total, 602 automated tests. » | idem | oui, trois lignes |
| C6-6 | 282 | « Pre-registration drafts for gate G1, Paper C (HC1–HC3), the organisms and the probes. » | idem | oui |
| C6-7 | 283 | « Compute spent: about $20. » | idem | **oui, présente** |
| C6-G0 | 284-285 | « Gate G0 (at the start of the grant, December 2026) still requires organisms with a dose–response, … and the closing of the literature check. » | at the start of the grant, December 2026 | oui, deux lignes à la colonne 0 |
| C7-1 | 289-291 | « Close G0. Paper C: deference of judges under the five attack families (HC1); probes under the same attacks (HC2, HC2b). Paper A: organisms and dose–response in the research-sabotage environment → G0 » | mois 1 (Dec 2026) | oui |
| C7-2 | 292-293 | « Paper C: impersonation (HC3), displacement tax (HC4). Paper A: 2 × 2 design → GC » | mois 2 (Jan 2027) | oui |
| C7-3 | 294-295 | « Paper C: countermeasures (HC5), benign g and the acceptance test (HC6). Paper A: lemma and theorem on real activations → — » | mois 3 (Feb 2027) | oui (« — » est la cellule « Gates » du texte) |
| C7-4 | 296-297 | « Write Paper C. Paper A: complete the 2 × 2 design → Paper C on arXiv and at a workshop; G1 » | mois 4 (Mar 2027) | oui, cellule « Gates » recollée |
| C7-5 | 298-300 | « Paper A: adaptive attacks (content, then fine-tuning and reinforcement learning against the probe), interventions (H6), validity and robustness (H8). Write Paper A → Paper A on arXiv; conference submission (NeurIPS 2027 if ready, otherwise ICLR 2028) » | mois 5–6 (Apr–May 2027) | oui, trois lignes, deux cellules recollées |
| C7-6 | 301-302 | « Release of code, organisms, probes and pre-registrations; replications requested by reviewers; final report → Final report » | mois 7 (Jun 2027) | oui |
| C8-1 | 309-310 | « Two papers: C (arXiv and a workshop by month 4, then a short conference paper) and A (arXiv and a conference submission by month 7). Paper B in the ambitious scenario. » | fin de la période (section 7 : seven months from 1 December 2026) | oui, une seule puce dans le texte |
| C8-2 | 311 | « Open code: harness, tested aggregators, the reconstruction of the research-sabotage environment. » | idem | oui |
| C8-3 | 312 | « Model organisms and probes. » (ligne précédée d'un saut de page) | idem | oui |
| C8-4 | 313 | « Pre-registrations and sealed results. » | idem | oui |
| C8-5 | 314 | « A pre-deployment acceptance test for monitors (HC6). » | idem | oui |
| C8-6 | 316 | « 1. The deference law and the displacement tax are measured (Paper C). » | idem | oui |
| C8-7 | 317 | « 2. The lemma and the negative theorem are proven and tested on real activations within the 2 × 2 design (Paper A). » | idem | oui |
| C8-8 | 318 | « 3. A construct-validity verdict on what the probes measure stands even if H1 fails. » | idem | oui |
| C8-9 | 319 | « 4. In the ambitious scenario, the security(N) curve and the diversification/coordination trade-off are established (Paper B). » | idem | oui |

Les lignes de la section 7 portent la période telle que le texte l'écrit (mois 1 = Dec 2026, … mois 7 = Jun 2027) ; au jour
du script (2026-11-08), les six sont « à venir (période non commencée au jour du script) » (règle `etat_periode` de la v2,
inchangée : le début de période est comparé au mois du jour). Les liaisons aux tâches de la phase 0 (`REGLES_CANDIDATURE`,
inchangées) donnent les mêmes tâches qu'en v2 : C6-1 → T0.2, C6-2 → T0.3, C6-3 → T0.4, C6-4 → T0.5, C6-5 → T0.1,
C6-6 → T0.9, C6-7 → aucune (cellules d'état vides).

## 6. Ce qui n'a pu être extrait, et les limites

- **Rien des sections 6, 7, 8 n'est resté inextrait** : 7 + 1 + 6 + 9 lignes, chacune citant ses lignes du texte ; aucun
  signalement sur la candidature.
- **Troncature** : les cellules « promis » de C6-3, C6-4 et C7-5 sont coupées à 260 caractères (« … »), règle `tronquer` de la
  v2, inchangée ; le texte entier est aux lignes citées.
- **Ordre des critères de succès** : le texte envoyé place « deference law » (C8-6) avant « lemma » (C8-7), l'inverse de la
  version EA Funds ; les identifiants suivent le texte envoyé, comme demandé. La matrice de traçabilité qui reprend les
  identifiants C8-x de la v2 doit en tenir compte (C8-1 n'est plus « Three papers » mais « Two papers … Paper B in the
  ambitious scenario », C8-6 et C8-7 sont permutées, C8-9 porte « In the ambitious scenario »).
- **Glyphes de puces perdus** : la règle « majuscule après une fin de phrase ouvre une puce » est une règle écrite sur la
  mise en page, pas une lecture du sens ; elle est juste sur ce texte (vérifié ligne à ligne, section 5) et peut couper à
  tort une puce dont une phrase finit en bout de ligne et dont la suite reprend par une majuscule. Toute nouvelle version du
  texte est à relire sur ce point.
- **Table du calendrier** : les positions de colonnes sont lues sur l'en-tête, avec une tolérance de deux caractères ;
  une cellule « Work » qui déborderait sur la colonne « Gates » (jamais le cas avec `-layout` sur ce texte) irait dans
  « Gates ». La cellule « Gates » de C7-3 est « — », telle que le texte l'écrit.
- **Date promise des lignes C8** : dérivée du titre de la section 7 (règle 4) ; sans section 7, elle reste vide.
- **Comptes de calibration et de dépenses** : identiques à ceux du script v2 relancé au même instant, pas à ceux des sorties
  scellées du matin, parce que les registres ont bougé (section 3) ; les chiffres opposables sont ceux que la mère scellera.
