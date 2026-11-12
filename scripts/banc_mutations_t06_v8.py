"""Banc de mutations CIBLÉ du lanceur de T0.6, v6 (R-1660, sur la base de la v5, R-1657 : C-V5-1 à C-V5-3 ; même méthode que les bancs v1 à v4 : chaque garde mutée dans
une copie du code doit faire échouer l'essai qui l'éprouve ; « tuée » seulement au code 1 de pytest avec « failed » ; un témoin vert est
exigé ; rien du dépôt n'est touché). Les 112 mutations de la v4 ne sont pas rejouées : `lancer_t06_v8.sh` n'en change que les blocs de
`creation`, `apres-creation` et `surveillance` visés ici.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_t06_v8.py [SORTIE.json]
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
COPIES = ("src/controle_ia", "tests", "scripts", "pyproject.toml", "prereg/P3-consignes-v1.md", "prereg/P3-consignes-v1.md.sha256",
          "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v2.json", "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v3.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v4.json", "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon2.json", "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon3.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v1.json", "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v1.json", "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e2-v2.json", "docs/notes/g0-deux-semaines-v1/config-t06-epreuve-e3-v2.json", ".claude/hooks/garde_calcul.py", "docs/sources/invites-2606.08892-v1", "brouillons/ordres-t06-e2-e3-v5")
T_CF, T_SE = "tests/test_t06_v2_configuration.py", "tests/test_t06_v2_session.py"
T_CF3, T_FA, T_LJ, T_SC = ("tests/test_t06_v3_configuration.py", "tests/test_t06_v3_familles.py", "tests/test_t06_v4_lanceur_jouet.py",
                           "tests/test_t06_v4_scripts.py")
T_CF4, T_FA3 = "tests/test_t06_v4_configuration.py", "tests/test_t06_v4_familles.py"
CF, LE, SE, LA2 = ("src/controle_ia/t06/configuration_v2.py", "src/controle_ia/t06/lecture_v2.py", "src/controle_ia/t06/session_v2.py",
                   "src/controle_ia/t06/lanceur_v2.py")
CF3, LA, FV2 = "src/controle_ia/t06/configuration_v3.py", "src/controle_ia/t06/lanceur_v3.py", "src/controle_ia/sondes/familles_v2.py"
CF4, LA4, FV3 = "src/controle_ia/t06/configuration_v4.py", "src/controle_ia/t06/lanceur_v4.py", "src/controle_ia/sondes/familles_v3.py"
S3 = "src/controle_ia/t06/session_v3.py"
AM, LN = "scripts/amorce_instance_t06_v4.sh", "scripts/lancer_t06_v4.sh"

AM5 = "scripts/amorce_instance_t06_v6.sh"
TA = "tests/test_t06_v6_amorce.py"
TC = "tests/test_t06_cibles_invisibles_v1.py"
PILOTE = "src/controle_ia/environnements/pilote_a.py"
LN5, S4, GEN3 = "scripts/lancer_t06_v8.sh", "src/controle_ia/t06/session_v7.py", "brouillons/ordres-t06-e2-e3-v5/pieces/generer_ordres_v5.py"
T5 = "tests/test_t06_v8_scripts.py"
# (nom, fichier, ancien, nouveau, essai, -k)
MUTATIONS_V8 = [
    ("C-V5-1 : recherche par identifiant au lieu du filtre", LN5, 'search offers "$FILTRE"', 'search offers "id=$OFFRE_ARG"', T5, "cas_sain"),
    ("C-V5-1 : machines refusées non exclues", LN5, '"$CARTE" "$EXCL")', '"$CARTE" "")', T5, "cas_sain"),
    ("C-V5-1 : plus de limite de trois essais", LN5, '[ "${ESSAIS:-0}" -lt 3 ]', '[ "${ESSAIS:-0}" -lt 99 ]', T5, "artefacts_liste_vide"),
    ("C-V5-1 : rang suivant sans vérifier l'inventaire", LN5, '--raw > "$D/instances-apres.json" 2>/dev/null && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" "$ETIQ" >/dev/null', '--raw > "$D/instances-apres.json" 2>/dev/null && true', T5, "artefacts_liste_vide"),
    ("C-V5-1 : identifiant donné à la main admis", LN5, '[ "$OFFRE_ARG" = auto ] ||', 'true ||', T5, "artefacts_liste_vide"),
    ("C-V5-1 : recherche filtrée sans le disque demandé (--storage)", LN5, '-o dph_total --storage "$DISQUE" --raw > "$D/offres.json"', '-o dph_total --raw > "$D/offres.json"', T5, "cas_sain"),
    ("C-V5-2 : HF_TOKEN exigé aussi en mode jouet", LN5, '[ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ]', '[ "${#HF_L}" -ge 8 ]', T5, "surveillance_sans_hf"),
    ("C-V5-2 : HF_TOKEN jamais exigé", LN5, '[ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ]', 'true', T5, "surveillance_sans_hf"),
    ("C-V5-3 : texte au plafond de 200", LN5, 'dépense cumulée ≥ $PLC USD (plafond', 'dépense cumulée ≥ 200 USD (plafond', T5, "surveillance_sans_hf"),
    ("C-V5-1 (session) : liste dans l'ordre reçu, pas du prix croissant", S4, 'for rang, o in enumerate(sorted((o for o in offres if isinstance(o, dict)), key=cle), 1):', 'for rang, o in enumerate((o for o in offres if isinstance(o, dict)), 1):', T5, "session_v7"),
    ("C-V5-1 (session) : machine exclue admise", S4, '        if str(o.get("machine_id")) in exclues:', '        if False:', T5, "session_v7"),
    ("C-V5-1 (session) : liste vide non signalée", S4, '    if not offres:\n        raise GardeSession("recherche filtrée : liste VIDE', '    if False:\n        raise GardeSession("recherche filtrée : liste VIDE', T5, "session_v7"),
    ("C-V5-1 (session) : prix maximal absent du filtre", S4, "f\"disk_space>={b['disque_min_go']} dph_total<={c['prix_max_usd_h']}\"", "f\"disk_space>={b['disque_min_go']}\"", T5, "session_v7"),
    ("C-V5-1 (session) : bornes de l'offre non vérifiées", S4, 'r = s2.verifier_offre([o], config, carte)', 'r = {"id": int(o["id"]), "prix_carte": float(o["dph_total"]), "prix_stockage": 0.0, "telechargement": 0.0, "telechargement_forfait_usd": 0.0, "carte": "x", "machine_id": o.get("machine_id")}', T5, "session_v7"),
    ("R-1660 (session) : fiabilité absente du filtre de création", S4, " reliability>={FIABILITE_MIN_OFFRE} inet_down>=", " inet_down>=", T5, "filtre"),
    ("R-1660 (session) : seuil de fiabilité abaissé", S4, "FIABILITE_MIN_OFFRE = 0.98", "FIABILITE_MIN_OFFRE = 0.9", T5, "filtre"),
    ("R-1660 (ordres) : filtre de lecture de l'ordre d'E3 non lu dans le lanceur", GEN3, 'return session_v7.filtre_recherche(json.load(open(racine / CFG_E3, encoding="utf-8")), "course")', 'return "num_gpus=1 rentable=true gpu_name=A100_SXM4 reliability>=0.98 inet_down>=500 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=150 dph_total<=1.3"', T5, "ordre_e3_v5"),
    ("R-1660 (ordres) : filtre d'E3 lu sans la fiabilité", GEN3, 'return session_v7.filtre_recherche(json.load(open(racine / CFG_E3, encoding="utf-8")), "course")', 'return session_v7.filtre_recherche(json.load(open(racine / CFG_E3, encoding="utf-8")), "course").replace(" reliability>=0.98", "")', T5, "ordre_e3_v5"),
    # --- R-1677 : amorce (clonage réduit, refus qui attend)
    ("R-1677 (amorce) : clonage complet (sans --no-checkout)", AM5, '--filter=blob:none --no-checkout "$DEPOT_URL"', '--filter=blob:none "$DEPOT_URL"', TA, "clonage_reduit_extraction_partielle_ligne"),
    ("R-1677 (amorce) : clonage sans filtre de blobs", AM5, '--filter=blob:none --no-checkout "$DEPOT_URL"', '--no-checkout "$DEPOT_URL"', TA, "clonage_reduit_extraction_partielle_ligne"),
    ("R-1677 (amorce) : extraction partielle jamais posée", AM5, 'SP_MSG=$(printf \'%s\\n\' "$CHEMINS_CLONAGE" | git -C "$R/amorce-depot" sparse-checkout set --no-cone --stdin 2>&1) ||', 'SP_MSG=$(true) ||', TA, "clonage_reduit_extraction_partielle_ligne"),
    ("R-1677 (amorce) : échec de l'extraction partielle (set) ignoré", AM5, '|| refus "extraction partielle impossible (sparse-checkout set) :', '|| true "extraction partielle impossible (sparse-checkout set) :', TA, "extraction_partielle_impossible"),
    ("R-1677 (amorce) : échec de l'extraction partielle (init) ignoré", AM5, '|| refus "extraction partielle impossible (sparse-checkout init) :', '|| true "extraction partielle impossible (sparse-checkout init) :', TA, "extraction_partielle_impossible"),
    ("R-1677 (amorce) : dossier des PDF de tiers dans la liste", AM5, "/docs/notes/\n/docs/procedures/", "/docs/notes/\n/docs/sources/pdf/\n/docs/procedures/", TA, "clonage_reduit_extraction_partielle_ligne or sparse_liste"),
    ("R-1677 (amorce) : ligne CLONAGE absente", AM5, 'echo "AMORCE $(date -u +%FT%TZ) : CLONAGE mode=$MODE', ': "AMORCE $(date -u +%FT%TZ) : CLONAGE mode=$MODE', TA, "clonage_reduit_extraction_partielle_ligne"),
    ("R-1677 (amorce) : attente du refus de 18 s au lieu de 180 s", AM5, "REFUS_ATTENTE_S=180", "REFUS_ATTENTE_S=18", TA, "constante_de_180"),
    ("R-1677 (amorce) : attente du refus pilotable en exploitation", AM5, '[ "$ESSAI" = 1 ] && REFUS_ATTENTE_S=', 'REFUS_ATTENTE_S=', TA, "constante_de_180"),
    ("R-1677 (amorce) : refus sans attente", AM5, 'rien ne part"; attente_refus; detruire', 'rien ne part"; detruire', TA, "refus_annonce"),
    ("R-1677 (amorce) : refus précoce sans attente", AM5, 'rien ne part"; attente_refus; echo "refus : $1" > "$R/t06-detruire"', 'rien ne part"; echo "refus : $1" > "$R/t06-detruire"', TA, "refus_precoce"),
    # --- R-1683 : amorce v6 (message de git gardé)
    ("R-1683 (amorce) : message de git jeté (set)", AM5, "--no-cone --stdin 2>&1)", "--no-cone --stdin 2>/dev/null)", TA, "message_de_git"),
    ("R-1683 (amorce) : message de git jeté (init)", AM5, "sparse-checkout init --no-cone 2>&1)", "sparse-checkout init --no-cone 2>/dev/null)", TA, "message_de_git"),
    # --- R-1683 : lanceur v8 (présence, journal, masquage)
    ("R-1683 (session) : liste vide lue comme une absence", S4, "    if inventaire is None or inventaire == []:\n        return None", "    if inventaire is None or inventaire == []:\n        return False", TA, "presence_tri_etat or main_codes"),
    ("R-1683 (session) : motifs d'introuvable vidés", S4, 'MOTIFS_INTROUVABLE = ("not found", "no such", "does not exist", "introuvable", "404")', "MOTIFS_INTROUVABLE = ()", TA, "presence_tri_etat or main_codes"),
    ("R-1683 (session) : réponse illisible déclarée introuvable", S4, '            return False\n        raise GardeSession("réponse de show instance illisible")', '            return False\n        return False', TA, "presence_tri_etat or main_codes"),
    ("R-1683 (session) : inventaire illisible déclaré absent", S4, 'return 2 if (len(argv) == 3 and argv[0] in ("presente", "seule")) else 1', 'return 1', TA, "main_codes"),
    ("R-1683 (session) : toute instance déclarée présente", S4, 'return any(str(i.get("id")) == str(ident) for i in inventaire)', 'return True', TA, "presence_tri_etat"),
    ("R-1683 (lanceur) : tail de 2000 lignes", LN5, "--tail 20000 2>&1", "--tail 2000 2>&1", TA, "non_vide_sans_l_instance_deux_fois"),
    ("R-1683 (lanceur) : un seul relevé de la liste suffit à l'arrêt", LN5, 'sleep "${ABSENCE_ATTENTE_S:-15}"; liste_presente; [ "$LP" = 1 ] && ARR=1; fi', 'ARR=1; fi', TA, "puis_presente_n_arrete_pas"),
    ("R-1683 (lanceur) : un seul relevé de l'instance seule suffit à l'arrêt", LN5, 'sleep "${ABSENCE_ATTENTE_S:-15}"; seule_presente; [ "$SP" = 4 ] && ARR=1; fi', 'ARR=1; fi', TA, "introuvable_une_fois"),
    ("R-1683 (lanceur) : pas d'escalade après trois relevés", LN5, 'if [ "$NONET" -ge 3 ]; then', 'if [ "$NONET" -ge 999 ]; then', TA, "non_etablie_trois_fois"),
    ("R-1683 (lanceur) : alertes d'inventaire seulement dans le fichier", LN5, 'echo "$m" >> "$D/surveillance.txt"; echo "$m"', 'echo "$m" >> "$D/surveillance.txt"', TA, "non_etablie_trois_fois"),
    ("R-1683 (lanceur) : liste vide qui donne ARRET mort sans passer par l'instance seule", LN5, 'if [ "$ARR" = 0 ] && [ "$LP" != 0 ]; then', 'if [ "$ARR" = 0 ] && [ "$LP" != 0 ]; then ARR=1; fi; if false; then', TA, "une_liste_vide_n_est_pas"),
    ("R-1683 (lanceur) : journal brut écrit avant masquage", LN5, '--tail 20000 2>&1 | masquer > "$D/journal-dernier.tmp"', '--tail 20000 2>&1 | tee "$D/journal-tour.txt" | masquer > "$D/journal-dernier.tmp"', TA, "masquage_par_un_tube"),
    ("R-1683 (lanceur) : clés de plus de 7 caractères non masquées", LN5, "if v and len(v) >= 8:", "if v and len(v) >= 99:", TA, "masquage_par_un_tube"),
    ("R-1683 (lanceur) : inventaire écrit sans masquage", LN5, 'show instances --raw 2>/dev/null | masquer >', 'show instances --raw 2>/dev/null | cat >', TA, "masquage_par_un_tube"),
    ("R-1683 (lanceur) : réponse de show instance écrite sans masquage", LN5, 'show instance "$ID" --raw 2>&1 | masquer >', 'show instance "$ID" --raw 2>&1 | cat >', TA, "masquage_par_un_tube"),
    ("R-1683 (lanceur) : clé courte admise", LN5, '{ [ -z "$V" ] || [ "${#V}" -ge 8 ]; }', '{ true; }', TA, "moins_de_8"),
    ("R-1683 (lanceur) : copie du journal écrasée par un relevé sans journal", LN5, "grep -q '^AMORCE ' \"$D/journal-dernier.txt\" && cp -f", "cp -f", TA, "copie_survit"),
    ("R-1677 (session) : inet_down absent du filtre", S4, " inet_down>={INET_DOWN_MIN_MBPS}", "", T5, "filtre"),
    ("R-1677 (session) : seuil de débit abaissé", S4, "INET_DOWN_MIN_MBPS = 500", "INET_DOWN_MIN_MBPS = 50", T5, "filtre"),
    # --- R-1679 : cibles invisibles (constructeur muté qui lirait tache["cibles"])
    ("R-1683 (cibles) : tache_de qui recopie les cibles dans l'énoncé", PILOTE, 'return Tache(donnee["identifiant"], donnee["questions"],', 'return Tache(donnee["identifiant"], donnee["questions"] + json.dumps(donnee.get("cibles")),', TC, "aucune_invite_ni_aucun_resultat_ne_porte_les_cibles and v4"),
    ("R-1686 (session) : cuda_max_good absent du filtre", S4, " cuda_max_good>={CUDA_MAX_GOOD_MIN}", "", T5, "cuda_max_good_garde_locale"),
    ("R-1686 (session) : seuil de CUDA abaissé", S4, "CUDA_MAX_GOOD_MIN = 13.0", "CUDA_MAX_GOOD_MIN = 12.0", T5, "cuda_max_good_garde_locale"),
    ("R-1686 (session) : garde locale de CUDA retirée", S4, "        if cuda < CUDA_MAX_GOOD_MIN:", "        if False:", T5, "cuda_max_good_garde_locale"),
    ("R-1686 (session) : clé cuda_max_good absente tolérée", S4, 'cuda = float(o["cuda_max_good"])', 'cuda = float(o.get("cuda_max_good", 99.0))', T5, "cuda_max_good_garde_locale"),
    ("R-1686 (amorce) : carte invisible sans refus", AM5, '    refus "carte invisible pour torch (torch.cuda.is_available() faux)', '    true "carte invisible pour torch (torch.cuda.is_available() faux)', TA, "carte_invisible_pour_torch"),
    ("R-1686 (amorce) : carte invisible sans consigner la cause", AM5, '    consigner_arret "contrôle de la carte"\n', '    true\n', TA, "carte_invisible_pour_torch"),
    ("R-1686 (amorce) : version du pilote non citée", AM5, "pilote ${PILOTE:-inconnu}, CUDA de torch", "pilote inconnu, CUDA de torch", TA, "carte_invisible_pour_torch"),
    ("R-1686 (amorce) : la garde de la carte vaut aussi en jouet", AM5, 'if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"', 'if ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"', TA, "carte_invisible_n_arrete_pas"),
]
MUTATIONS = MUTATIONS_V8
TEMOINS = [("témoin lanceur v7", T5, None), ("témoin amorce v6", TA, "clonage or refus or v8 or v7 or session_v7")]


def copier(base: Path) -> None:
    for c in COPIES:
        s, d = RACINE / c, base / c
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, symlinks=True, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(s, d)
    for x in ("runs", "diag", "donnees", "registres"):
        (base / x).mkdir(exist_ok=True)
    shutil.copy2(RACINE / "registres" / "go.md", base / "registres" / "go.md")


def pytest_sur(d: Path, essai: str, k: str | None) -> tuple[int, str]:
    cmd = [PYTHON, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", essai] + (["-k", k] if k else [])
    r = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=1800, env={**os.environ, "PYTHONPATH": "src"})
    return r.returncode, r.stdout[-400:]


def main(argv: list[str]) -> int:
    rapide = "--rapide" in argv
    filtre = next((a.split("=", 1)[1] for a in argv if a.startswith("--filtre=")), None)       # ne rejoue que les mutations dont le nom contient ce texte
    sortie = next((a for a in argv if a.endswith(".json")), None)
    res = []
    with tempfile.TemporaryDirectory(prefix="banc-t06-v8-") as t:
        base = Path(t) / "base"
        copier(base)
        for nom, essai, k in TEMOINS:
            if filtre and not any(f in m[0] for m in MUTATIONS if m[4] == essai for f in filtre.split("|")):
                continue
            if rapide and essai in (T_LJ, T_SC):
                continue
            code, fin = pytest_sur(base, essai, k)
            statut = "VERT" if code == 0 else "ROUGE"
            res.append({"temoin": nom, "statut": statut, "fin": fin.strip().splitlines()[-1] if fin.strip() else ""})
            print(f"{statut} {nom}", flush=True)
        for nom, fichier, ancien, nouveau, essai, k in MUTATIONS:
            if filtre and not any(f in nom for f in filtre.split("|")):
                continue
            if rapide and essai in (T_LJ, T_SC):
                continue
            d = Path(t) / "m"
            shutil.copytree(base, d, symlinks=True)
            f = d / fichier
            s = f.read_text(encoding="utf-8")
            if s.count(ancien) != 1:
                res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": s.count(ancien)})
                print(f"INAPPLICABLE {nom} ({s.count(ancien)} occurrences)", flush=True)
                shutil.rmtree(d)
                continue
            f.write_text(s.replace(ancien, nouveau), encoding="utf-8")
            code, fin = pytest_sur(d, essai, k)
            tuee = code == 1 and "failed" in fin
            res.append({"mutation": nom, "fichier": fichier, "essai": essai, "k": k, "code": code, "statut": "TUÉE" if tuee else "SURVIVANTE",
                        "fin": fin.strip().splitlines()[-1] if fin.strip() else ""})
            print(f"{'TUÉE' if tuee else 'SURVIVANTE'} {nom}", flush=True)
            shutil.rmtree(d)
    survivantes = [r for r in res if r.get("statut") in ("SURVIVANTE", "INAPPLICABLE", "ROUGE")]
    print(f"FIN DU BANC DE MUTATIONS T0.6 v8 ; mutations {len([r for r in res if 'mutation' in r])} (dont {len(MUTATIONS_V8)} des corrections C-V5-1 à C-V5-3), témoins {len([r for r in res if 'temoin' in r])}, survivantes ou inapplicables ou témoins rouges : {len(survivantes)}")
    if sortie:
        Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
