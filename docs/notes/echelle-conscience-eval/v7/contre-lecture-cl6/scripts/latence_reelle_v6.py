"""cl6 : retard de la demande d'arrêt de `surveiller_echelle_v6.sh` (script du commit, lu et exécuté tel quel depuis
l'arbre de travail, sorties dans le bac à sable) aux réglages RÉELS : PAS_S et APPEL_S non fixés (60 s et 30 s par
défaut). Faux outil vastai : celui des tests v6 (FAUX_VASTAI), appels de LENTEUR secondes avant l'arrêt.
Cas : (a) appels de 29 s, plafond 2 s après le départ (pire cas attendu : ≈ 58 s après le plafond) ;
      (b) appels bloqués (300 s), coupés à 30 s, plafond 2 s après le départ ;
      (c) appels instantanés, plafond 40 s après le départ (la pause doit s'arrêter au plafond, pas 60 s après) ;
      (d) APPEL_S=0 laissé dans l'environnement (« timeout 0 » : aucune borne), appels de 45 s, plafond 2 s après.
Usage : python -I -B latence_reelle_v6.py DOSSIER_NEUF
"""
import hashlib
import json
import os
import pathlib
import stat
import subprocess
import sys
import time

WT = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v6")
SURV = WT / "scripts" / "surveiller_echelle_v6.sh"
FAUX = r"""#!/usr/bin/env bash
case "$1 $2" in
  "show instance") [ -s "$ARRETS_FAUX" ] || sleep "$LENTEUR_FAUSSE"; echo "{\"actual_status\": \"$(cat "$ETAT_FAUX")\", \"cur_state\": \"$(cat "$ETAT_FAUX")\", \"dph_total\": 2.4, \"status_msg\": \"\"}" ;;
  "logs "*) [ -s "$ARRETS_FAUX" ] || sleep "$LENTEUR_FAUSSE"; cat "$JOURNAL_FAUX" ;;
  "stop instance") date +%s.%N >> "$ARRETS_FAUX.heure"; echo "$3" >> "$ARRETS_FAUX"; [ -n "$ARRET_EFFECTIF" ] && echo stopped > "$ETAT_FAUX"; echo "arrêt demandé" ;;
esac
"""


def cas(base, nom, lenteur, plafond_dans_s, env_sup=None):
    d = base / nom
    d.mkdir(parents=True)
    faux = d / "vastai"
    faux.write_text(FAUX)
    faux.chmod(faux.stat().st_mode | stat.S_IEXEC)
    (d / "etat").write_text("running")
    (d / "journal").write_text("ECHELLE 2026 : mesure\n")
    duree = 4500
    creation = int(time.time()) + plafond_dans_s - duree
    lanc = d / "lancement"
    lanc.mkdir()
    attendue = hashlib.sha256(SURV.read_bytes()).hexdigest()
    (lanc / "lancement.txt").write_text(f"surveillance attendue {attendue}\ngo GO-0000-00-00-00\ncreation {creation}\n"
                                        f"duree_max_s {duree}\nsuccès : True ; identifiant 12345678 ; message : essai\n")
    env = {k: v for k, v in os.environ.items() if k not in ("PAS_S", "APPEL_S", "ATTENTE_ARRET_S")}
    env.update(VASTAI=str(faux), ETAT_FAUX=str(d / "etat"), JOURNAL_FAUX=str(d / "journal"),
               ARRETS_FAUX=str(d / "arrets"), ARRET_EFFECTIF="1", DUREE_MAX_S=str(duree), LENTEUR_FAUSSE=str(lenteur),
               ATTENTE_ARRET_S="0")
    env.update(env_sup or {})
    t0 = time.time()
    r = subprocess.run(["bash", str(SURV), "12345678", str(creation), str(lanc), str(d / "s")], env=env,
                       capture_output=True, text=True, timeout=900)
    heure = float((d / "arrets.heure").read_text().split()[0]) if (d / "arrets.heure").exists() else None
    fin = creation + duree
    out = {"cas": nom, "code": r.returncode, "lenteur_s": lenteur, "plafond_apres_depart_s": plafond_dans_s,
           "env": env_sup or {}, "retard_demande_arret_s": None if heure is None else round(heure - fin, 2),
           "duree_totale_s": round(time.time() - t0, 1)}
    print(json.dumps(out, ensure_ascii=False), flush=True)
    return out


def principal():
    base = pathlib.Path(sys.argv[1])
    if base.exists():
        sys.exit(f"{base} existe déjà")
    base.mkdir(parents=True)
    res = [cas(base, "a-appels-29s", 29, 2),
           cas(base, "b-appels-bloques", 300, 2),
           cas(base, "c-pause-bornee", 0, 40),
           cas(base, "d-appel-s-zero", 45, 2, {"APPEL_S": "0"})]
    (base / "resultat.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    principal()
