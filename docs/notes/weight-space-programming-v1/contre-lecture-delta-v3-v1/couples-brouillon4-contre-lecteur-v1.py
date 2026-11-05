"""Couples du brouillon 4 (contre-lecteur du delta v3) : écrit le JSON, puis les vérifie sur le brouillon 3 :
chaque « ancien » unique au moment de son application, dans l'ordre ; trois marqueurs « À REMPLIR » gardés.
    python3 -I -B ecrire_couples_b4.py BROUILLON3 SORTIE_JSON"""
import hashlib, json, sys
from pathlib import Path

C = [
 # K1 : nom de la branche des sorties du contrôle causal (texte v1 resté ; code v3 : causal-v3 ; v4 : par commit et ordre)
 ("(même disque, `PHASE=causal`, branche `calcul/sparks-exp7-nul-causal-v1` ; rd, l. 226-227)",
  "(même disque, sur ordre écrit « causal », section « Minuterie de destruction et redémarrages » ; sorties sur une branche neuve "
  "`calcul/sparks-exp7-nul-causal-v4-<commit court>-<NNN>` écrite par l'instance, `<commit court>` étant les douze premiers "
  "caractères de `COMMIT` et `<NNN>` le numéro de l'ordre ; rd, l. 226-227)"),
 # K2 : borne de chaque démarrage sur la machine : toutes les étapes sous timeout, pas seulement le calcul
 ("Carte : chaque démarrage est borné **sur la machine** (`timeout` de l'amorce ;",
  "Carte : chaque démarrage est borné **sur la machine** (`timeout` sur chaque étape de l'amorce, clone, lecture des ordres, "
  "gardes, lots et repli `vastai` compris, et sur le calcul ;"),
 # K3 : attente du principal : processus du lancement en cours, borne écrite
 ("quand une destruction est due, le processus principal attend la fin de la minuterie.",
  "quand une destruction est due, le processus principal attend la fin de la minuterie lancée par ce démarrage (désignée par "
  "son numéro de processus au lancement, jamais par un fichier d'un démarrage antérieur), au plus 32 minutes : dans un "
  "conteneur, la sortie du processus principal tue la minuterie. Chaque étape avant le calcul est sous `timeout` (clone et "
  "extraction 10 minutes, lecture des ordres 5 minutes, gardes 2 minutes, lot 15 minutes, `vastai destroy` 2 minutes) : sans "
  "cela, une étape bloquée garderait la carte louée jusqu'à l'échéance."),
 # K4 : branche des ordres hors calcul/, liée au commit lancé
 ("sur la branche `calcul/sparks-exp7-nul-v3-ordres`, puis redémarre.",
  "sur la branche `ordres/sparks-exp7-nul-v4-<commit court>` (hors des branches `calcul/…`, que seules les instances "
  "écrivent ; liée au commit lancé, si bien qu'une répétition, lancée à un autre commit, n'y écrit jamais), puis redémarre."),
 # K5 : ordre lié à l'instance
 ("clés fermées ; numéro égal au nom du fichier ;",
  "clés fermées ; numéro égal au nom du fichier ; champ `instance` égal à `CONTAINER_ID` ;"),
 # K6 : consignation vérifiée
 ("et le consigne fait avant d'agir.",
  "et le consigne fait avant d'agir (consignation impossible : refus, rien ne part)."),
 # K7 : deja_usd non décroissant et borne propre de la machine
 ("est **relu à chaque démarrage** pour la borne de durée (ligne du devis).",
  "est **relu à chaque démarrage** pour la borne de durée (ligne du devis) ; la machine refuse un `deja_usd` inférieur à "
  "celui du dernier ordre exécuté, et la borne de durée prend le plus grand de `deja_usd` et de la borne propre de la "
  "machine (somme des plafonds des démarrages consignés sur son disque × prix de la carte, plus la durée depuis la "
  "création × prix du stockage), qui ne passe par aucun modèle (R-1481)."),
 # K8 : risque du stockage accepté par Lazar
 ("et par la minuterie au démarrage suivant.",
  "et par la minuterie au démarrage suivant ; risque accepté par Lazar (R-1488, option (b)), borné par l'échéance de "
  "GO-2026-11-04-04 (fin du 18 novembre)."),
 # K9 : épreuves : chaque garde mutée, espace de processus, et ce qui reste à éprouver sur une vraie machine
 ("cas sain et artefact pour chaque garde (`tests/test_sparks_exp7_nul_v3.py`, banc v3). Restent, avant le scellement : le "
  "**tir réel de la minuterie avant la création** (R-1477)",
  "cas sain et artefact pour chaque garde, chacune mutée au banc (essais et banc de la version du code citée en section 2 ; "
  "minuterie et attente du principal jouées aussi dans un espace de processus à part, `unshare -pf`, comme dans un "
  "conteneur). Restent, avant le scellement : le **tir réel de la minuterie avant la création** (R-1477 : `DELETE` par la "
  "clé du conteneur, puis lecture qui ne trouve plus l'instance ; `curl` et `git` présents dans l'image ; arguments et "
  "environnement relancés tels quels par `vastai start` ; instance « arrêtée » sans carte facturée à la sortie du "
  "conteneur ; `vastai copy` possible depuis un conteneur lancé par ses arguments)"),
 # K10 : création par la session : délai, sortie, marqueur (leçons de la sonde d'A1-v3)
 ("(disque existant ; commit du disque égal à `COMMIT`, sinon refus).",
  "(disque existant ; commit du disque égal à `COMMIT`, sinon refus). La session crée l'instance par `vastai create` sous "
  "`timeout`, sortie non affichée (seuls le code de retour et l'identifiant rendu sont gardés, R-1480) ; tout code non nul "
  "ou délai dépassé pose un marqueur de création incertaine : aucune seconde création avant un inventaire sans sortie brute."),
]


def main(b3, out):
    t = Path(b3).read_bytes().decode("utf-8")
    print("brouillon 3", hashlib.sha256(t.encode()).hexdigest())
    for i, (a, n) in enumerate(C, 1):
        k = t.count(a)
        if k != 1:
            raise SystemExit(f"REFUS K{i} : {k} occurrences")
        t = t.replace(a, n)
        print(f"OK K{i} : 1 occurrence, {len(a)} → {len(n)} caractères")
    m = t.count("À REMPLIR")
    if m != 3:
        raise SystemExit(f"REFUS : {m} marqueurs")
    print("marqueurs : 3 ; texte d'essai (non versé)", hashlib.sha256(t.encode()).hexdigest())
    p = Path(out)
    if p.exists():
        raise SystemExit("REFUS : sortie existe (R12)")
    p.write_text(json.dumps([{"ancien": a, "nouveau": n} for a, n in C], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("couples", hashlib.sha256(p.read_bytes()).hexdigest())


if __name__ == "__main__":
    main(*sys.argv[1:3])
