"""Banc de mutations du lanceur de T0.6, v3 (même méthode que les v1 et v2 : chaque garde mutée, affaiblie ou retirée, dans
une copie du code doit faire échouer l'essai qui l'éprouve ; « tuée » seulement au code 1 de pytest avec « failed » ; un
témoin vert est exigé pour chaque essai visé ; rien du dépôt n'est touché). Toutes les mutations de la v2 sont rejouées sur
les fichiers v3 qui les portent (`lanceur_v3.py`, `amorce_instance_t06_v3.sh`, `lancer_t06_v3.sh`, avec les essais v3 ;
`configuration_v2.py`, `lecture_v2.py`, `session_v2.py` sont partagés tels quels par la v3, avec leurs essais v2 ; les deux
gardes C03 vivent dans `lanceur_v2.py`, importées par la v3, éprouvées par les essais v3), plus les mutations des corrections
C-V3-1 à C-V3-4 de la contre-lecture neuve.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_t06_v3.py [SORTIE.json] [--rapide]

`--rapide` écarte les mutations dont l'essai est la répétition jouet ou les scripts (les plus longs).
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
          "docs/notes/g0-deux-semaines-v1/config-t06-jouet-v4.json", "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon2.json",
          "docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon3.json", ".claude/hooks/garde_calcul.py", "docs/sources/invites-2606.08892-v1")
T_CF, T_SE = "tests/test_t06_v2_configuration.py", "tests/test_t06_v2_session.py"
T_CF3, T_FA, T_LJ, T_SC = ("tests/test_t06_v3_configuration.py", "tests/test_t06_v3_familles.py", "tests/test_t06_v3_lanceur_jouet.py",
                           "tests/test_t06_v3_scripts.py")
CF, LE, SE, LA2 = ("src/controle_ia/t06/configuration_v2.py", "src/controle_ia/t06/lecture_v2.py", "src/controle_ia/t06/session_v2.py",
                   "src/controle_ia/t06/lanceur_v2.py")
CF3, LA, FV2 = "src/controle_ia/t06/configuration_v3.py", "src/controle_ia/t06/lanceur_v3.py", "src/controle_ia/sondes/familles_v2.py"
AM, LN = "scripts/amorce_instance_t06_v3.sh", "scripts/lancer_t06_v3.sh"

# (nom, fichier, ancien, nouveau, essai, -k)
MUTATIONS_V2 = [
    ("C04 : clé inconnue admise", CF, "    if inconnues:\n        raise GardeArret", "    if False:\n        raise GardeArret", T_CF, "artefacts"),
    ("C04 : temoin_lexical non nul admis", CF, '        if config[cle] is not None:\n            raise GardeArret(f"{cle} : non branché', '        if False:\n            raise GardeArret(f"{cle} : non branché', T_CF, "artefacts"),
    ("L04 : pas déclarés non vérifiés avant la dépense", CF, '    if config["decisions"]["DT-1"] == "b" and attendus != declares:', "    if False:", T_LJ, "pas_declares_faux"),
    ("L04 : unité du lot incohérente admise", CF, '    if (di["unite_du_lot"] == "transcription") != (di["mode"] == "transcription"):', "    if False:", T_CF, "artefacts"),
    ("L11 : dernier jour après la fin du GO admis", CF, "    if dernier >= fin.date():\n        raise GardeArret", "    if False:\n        raise GardeArret", T_CF, "artefacts"),
    ("L11 : fin du GO hors UTC admise", CF, "    if fin.tzinfo is None or fin.utcoffset() != timezone.utc.utcoffset(None):", "    if False:", T_CF, "artefacts"),
    ("L05 : règle inversée", LE, "    if si_au_dessus_seulement:\n        if not au_dessus:\n            return NON_AU_DESSUS\n        return NON_INTERPRETABLE if trivial else AU_DESSUS\n",
     "    if si_au_dessus_seulement:\n        if trivial:\n            return NON_INTERPRETABLE\n        return AU_DESSUS if au_dessus else NON_AU_DESSUS\n", T_CF, "etat_du_jeu_v2"),
    ("C06 : exclusions par adaptateur non comptées", LE, "        if excl is not None and total and excl / total > PART_EXCLUES_MAX:", "        if False:", T_CF, "reserves_cout"),
    ("C06 : contrôle négatif non écrit sous A", LE, '    if controle_negatif == "non concluant":\n        sortie.append', "    if False:\n        sortie.append", T_CF, "reserves_cout"),
    ("C08 : dépense antérieure non cumulée", SE, "    cumulee = ant + tel + instance", "    cumulee = instance", T_SE, "depense_cumulee"),
    ("C08 : heure d'épuisement sans les tentatives antérieures", SE, "    reste = PLAFOND_USD - ant - tel", "    reste = PLAFOND_USD", T_SE, "depense_cumulee"),
    ("C12 : carte non vérifiée", SE, '    if o.get("gpu_name") != c["nom_offre"]:\n        raise GardeSession', "    if False:\n        raise GardeSession", T_SE, "offre"),
    ("C12 : mémoire vive non vérifiée", SE, '    if not (_fini(o.get("cpu_ram")) and o["cpu_ram"] >= b["memoire_vive_min_mo"]):', "    if False:", T_SE, "offre_artefacts"),
    ("C12 : cœurs non vérifiés", SE, '    if not (_fini(o.get("cpu_cores_effective")) and o["cpu_cores_effective"] >= b["coeurs_effectifs_min"]):', "    if False:", T_SE, "offre_artefacts"),
    ("C12 : téléchargement non vérifié", SE, '    if not (_fini(tel) and 0 <= tel <= b["telechargement_max_usd_go"]):', "    if False:", T_SE, "offre_artefacts"),
    ("C15 : prix de la carte non borné", SE, '    if not (_fini(prix) and 0 < prix <= c["prix_max_usd_h"]):', "    if not (_fini(prix) and 0 < prix):", T_SE, "offre_artefacts"),
    ("C12 : instance du programme ignorée", SE, "    if presentes:\n        raise GardeSession", "    if False:\n        raise GardeSession", T_SE, "instances"),
    ("L11 : fin du GO non comparée à l'échéance du registre", SE, "    if fin != attendue:\n        raise GardeSession", "    if False:\n        raise GardeSession", T_SE, "calendrier"),
    ("L11 : dernier jour de création dépassé admis", SE, "    if j > dernier:\n        raise GardeSession", "    if False:\n        raise GardeSession", T_SE, "calendrier"),
    ("C03 : place disque non exigée (lanceur_v2, importé par la v3)", LA2, "    if libre < exige:\n        raise GardeArret", "    if False:\n        raise GardeArret", T_LJ, "place_disque"),
    ("C03 : arrondi silencieux vers l'infini (lanceur_v2, importé par la v3)", LA2, "            if not np.all(np.isfinite(a)) or float(np.abs(a).max(initial=0.0)) > FLOAT16_MAX:", "            if False:", T_LJ, "demi_precision"),
    ("C11 : morceau trop gros admis", LA, "    if taille > MORCEAU_MAX_OCTETS:\n        if len(courant) < 2:", "    if False:\n        if len(courant) < 2:", T_LJ, "borne_de_remplissage or scenario"),
    ("C11 : borne des morceaux relâchée", LA, "MORCEAU_MAX_OCTETS = 90_000_000", "MORCEAU_MAX_OCTETS = 95_000_000", T_LJ, "repetition_jouet_v3 and paquet_gele"),
    ("C02 : lignes A, B, C imprimées sur run.json", LA, 'from .lanceur_v2 import (CLES_RESUME_SCELLEES_SEULEMENT, ActivationsDemi, actions_de_la_couche, exiger_place_disque, pire_cas_octets,\n                         resume_imprimable)',
     'from .lanceur_v2 import (CLES_RESUME_SCELLEES_SEULEMENT, ActivationsDemi, actions_de_la_couche, exiger_place_disque, pire_cas_octets)\n\n\ndef resume_imprimable(resume):\n    return dict(resume)', T_LJ, "repetition_jouet_v3 and paquet_gele"),
    ("C01 : état des jeux décisifs dans PROGRES", LA, '    progres(etape="test-croise", jeux=2, duree_s=durees["decisif"])',
     '    progres(etape="test-croise", jeux=2, duree_s=durees["decisif"], sens1=jeux["sens1"]["decisif"]["etat"])', T_LJ, "repetition_jouet_v3 and paquet_gele"),
    ("C01 : aire du jeu décisif dans PROGRES", LA, '    progres(etape="test-croise", jeux=2, duree_s=durees["decisif"])',
     '    progres(etape="test-croise", jeux=2, duree_s=durees["decisif"], a=jeux["sens1"]["decisif"].get("aire"))', T_LJ, "repetition_jouet_v3 and paquet_gele"),
    ("C07 : jeu décisif par jeu_croise (arrêt possible)", LA, "            return tc.jeu_ou_echec(sondes, planchers, actions, pos, \"honnete\", plis, n_t,", "            return tc.jeu_croise(sondes, planchers, actions, pos, \"honnete\", plis, n_t,", T_LJ, "echec_sans_arret"),
    ("C01 (amorce) : ligne PROGRES à mot interdit relayée", AM, '    if printf \'%s\\n\' "$ligne" | grep -qiE "$MOTIF_INTERDIT"; then', '    if false; then', T_SC, "cas_sain"),
    ("C11 (amorce) : fichier de plus de 90 Mo non refusé", AM, '        if [ "$t" -gt "$MORCEAU_MAX" ]; then', '        if false; then', T_SC, "trop_gros"),
    ("C13 (amorce) : second démarrage après fin normale détruit", AM, '    if [ -e "$R/t06-fin-normale" ] || [ -e "$R/t06-depense-epuisee" ]; then', '    if false; then', T_SC, "cas_sain"),
    ("L11 (amorce) : fin du GO non comparée à la configuration", AM, '[ "$FIN_CONFIG" = "$FIN_GO" ] || refus', 'true || refus', T_SC, "calendrier_et_de_depense"),
    ("C08 (amorce) : DEPENSE_EPUISEE_UTC_S non exigée", AM, '    case "$DEP" in \'\'|*[!0-9]*) refus_precoce "DEPENSE_EPUISEE_UTC_S absente ou non entière (C08 : heure d\'épuisement des 200 USD, calculée à la création)";; esac',
     '    case "$DEP" in \'\'|*[!0-9]*) DEP=0;; esac', T_SC, "calendrier_et_de_depense"),
    ("C14 (minuterie) : rien de consigné à l'échéance", AM, 'if [ "$raison" = "échéance" ]; then echo "$(date -u +%FT%TZ) ÉCHÉANCE $ECH atteinte (C14) : consignation et poussée des résultats partiels avant la destruction" >> "$J"; consigner "échéance"; fi',
     'true', T_SC, "minuterie"),
    ("C08 (minuterie) : rien à l'heure de dépense épuisée", AM, '    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t06-depense-epuisee" ]; then', '    if false; then', T_SC, "minuterie"),
    ("C10 (amorce) : poussée initiale refusée ignorée", AM, '|| refus "poussée initiale de la branche $BRANCHE refusée (droit d\'écriture du jeton ?)"', '|| true', T_SC, "poussee_initiale"),
    ("C09 (session) : garde illisible → POURSUIVRE", LN, '            ILLISIBLES=$((ILLISIBLES + 1))', '            ILLISIBLES=0; DEC=POURSUIVRE', T_SC, "surveillance_v3"),
    ("C12 (session) : offre hors des bornes admise", LN, '|| { echo "offre $OFFRE hors des bornes du point 9 : $OF : nœud, pas de création"; exit 3; }', '|| true', T_SC, "commande_de_creation"),
    ("C12 (session) : instance présente admise", LN, '|| { echo "$INV : nœud, pas de création"; exit 3; }', '|| true', T_SC, "commande_de_creation"),
    ("C08 (session) : dépense déjà au plafond admise", LN, '    [ "$code_dep" = 0 ] || { echo "dépense cumulée déjà au plafond ou illisible ($DEP) : nœud, pas de création"; exit 3; }', '    true', T_SC, "commande_de_creation"),
    ("L11 (session) : calendrier non vérifié aux contrôles", LN, '|| { echo "calendrier de la configuration (L11) : $CAL : pas de création"; exit 2; }', '|| true', T_SC, "controles_artefacts"),
    ("C10 (session) : place disque non exigée", LN, '[ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }', 'true', T_SC, "disque_simule"),
]
MUTATIONS_V3 = [
    ("C-V3-1 : borne de remplissage égale à la borne du fichier (v2)", LA, "MORCEAU_TABLEAUX_MAX_OCTETS = 85_000_000", "MORCEAU_TABLEAUX_MAX_OCTETS = 90_000_000", T_LJ, "bornes_reelles or (repetition_jouet_v3 and paquet_gele)"),
    ("C-V3-1 : fichier trop gros = arrêt au lieu d'une réécriture en deux (v2)", LA, "    if taille > MORCEAU_MAX_OCTETS:\n        if len(courant) < 2:", "    if taille > MORCEAU_MAX_OCTETS:\n        if True:", T_LJ, "borne_de_remplissage or scenario"),
    ("C-V3-1 : garde d'avant les épisodes retirée", LA, "    if pire > borne:\n        raise GardeArret", "    if False:\n        raise GardeArret", T_LJ, "garde_action"),
    ("C-V3-2 (amorce) : contrôle de l'heure de dépense épuisée remis avant le second démarrage (v2)", AM,
     'if [ -d "$R/amorce-depot" ]; then\n    # C-V3-2', '[ "$(date +%s)" -lt "$DEP" ] || detruire "démarrage après l\'heure de dépense épuisée (C08) : aucun calcul"\nif [ -d "$R/amorce-depot" ]; then\n    # C-V3-2', T_SC, "second_demarrage_apres_depense"),
    ("C-V3-2 (amorce) : sommeil au lieu de la destruction après la dépense épuisée", AM, '        if [ -e "$R/t06-depense-epuisee" ] || [ "$(date +%s)" -ge "$DEP" ]; then', '        if false; then', T_SC, "second_demarrage_apres_depense"),
    ("C-V3-2 (amorce) : commits en attente non poussés au second démarrage", AM, '        [ -f "$R/t06-consigner.sh" ] && timeout -k 10 1200 bash "$R/t06-consigner.sh" "second démarrage"', '        true', T_SC, "second_demarrage_apres_depense or cas_sain"),
    ("C-V3-3 (session) : offre relue sans --storage (v2)", LN, '"$VAST" search offers "id=$OFFRE" --storage "$DISQUE" --raw', '"$VAST" search offers "id=$OFFRE" --raw', T_SC, "commande_de_creation"),
    ("C-V3-4 : essai d'égalité sauté avant l'usage", LA, "    return sonde, seqs, fv2.verifier_egalite_au_paquet_gele(sonde, int(graine))",
     '    return sonde, seqs, {"calcul": sonde.calcul, "n_jetons": 256, "graine": int(graine), "ecart_relatif_max": 0.0, "tolerance": 1e-12, "egal": True}', T_LJ, "couples_mahalanobis"),
    ("C-V3-4 : formule v2 fausse (P ignorée)", FV2, "        return ((z @ self.P) * z).sum(axis=1)", "        return (z * z).sum(axis=1)", T_FA, "meme_interface"),
    ("C-V3-4 : tolérance de l'essai d'égalité relâchée", FV2, "TOLERANCE_EGALITE = 1e-12", "TOLERANCE_EGALITE = 1e-6", T_FA, "cas_sain_et_artefact"),
    ("C-V3-4 : écart hors tolérance admis", FV2, '    if not resultat["egal"]:\n        raise GardeArret', '    if False:\n        raise GardeArret', T_FA, "cas_sain_et_artefact"),
    ("C-V3-4 (configuration) : défaut v2 au lieu du paquet gelé", CF3, "DEFAUT_MAHALANOBIS = PAQUET_GELE", "DEFAUT_MAHALANOBIS = \"produit_matriciel_v2\"", T_CF3, "conformes"),
    ("C-V3-4 (configuration) : valeur inconnue admise", CF3, "    if calcul not in CALCULS_MAHALANOBIS:\n        raise GardeArret", "    if False:\n        raise GardeArret", T_CF3, "artefacts"),
    ("C-V3-4 (lanceur) : calcul de la configuration ignoré (toujours le paquet gelé)", LA, "    calcul = calcul_mahalanobis(config)\n    n_t, n_p, n_pl", "    calcul = fv2.PAQUET_GELE\n    n_t, n_p, n_pl", T_LJ, "couples_mahalanobis or (repetition_jouet_v3 and produit)"),
]
MUTATIONS = MUTATIONS_V2 + MUTATIONS_V3
TEMOINS = [("témoin configuration et lecture v2", T_CF, None), ("témoin session v2", T_SE, None), ("témoin configuration v3", T_CF3, None),
           ("témoin familles v2", T_FA, None), ("témoin lanceur jouet v3", T_LJ, None), ("témoin scripts v3", T_SC, None)]


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
    sortie = next((a for a in argv if a.endswith(".json")), None)
    res = []
    with tempfile.TemporaryDirectory(prefix="banc-t06-v3-") as t:
        base = Path(t) / "base"
        copier(base)
        for nom, essai, k in TEMOINS:
            if rapide and essai in (T_LJ, T_SC):
                continue
            code, fin = pytest_sur(base, essai, k)
            statut = "VERT" if code == 0 else "ROUGE"
            res.append({"temoin": nom, "statut": statut, "fin": fin.strip().splitlines()[-1] if fin.strip() else ""})
            print(f"{statut} {nom}", flush=True)
        for nom, fichier, ancien, nouveau, essai, k in MUTATIONS:
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
    print(f"FIN DU BANC DE MUTATIONS T0.6 v3 ; mutations {len([r for r in res if 'mutation' in r])} (dont {len(MUTATIONS_V3)} des corrections "
          f"C-V3-1 à C-V3-4), témoins {len([r for r in res if 'temoin' in r])}, survivantes ou inapplicables ou témoins rouges : {len(survivantes)}")
    if sortie:
        Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not survivantes else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
