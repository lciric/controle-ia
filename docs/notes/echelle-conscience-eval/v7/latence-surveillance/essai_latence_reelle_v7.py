#!/usr/bin/env python3
"""Retard de la demande d'arrêt de `surveiller_echelle_v7.sh` aux réglages RÉELS (lignée « session-depot », 27 octobre
2026 ; CLU-02, CLU-03). Non décisif. Script de la surveillance lu tel quel dans l'arbre des outils au commit donné
(arbre propre exigé), exécuté avec PAS_S, APPEL_S et ATTENTE_ARRET_S retirés de l'environnement (défauts : 60 s, 30 s,
20 s ; ATTENTE_ARRET_S ramené à 0 pour l'essai, il ne joue qu'après la demande d'arrêt). Faux outil vastai : celui des
tests v7 (appels de LENTEUR secondes avant l'arrêt). Repris de l'essai de la contre-lecture n° 6
(`v7/contre-lecture-cl6/scripts/latence_reelle_v6.py`), sur la v7, avec deux cas de plus :
  (a) appels de 29 s, plafond 2 s après le départ (pire cas attendu : ≈ 58 s après le plafond) ;
  (b) appels bloqués (300 s), coupés à 30 s, plafond 2 s après le départ ;
  (c) appels instantanés, plafond 40 s après le départ : la pause (60 s) s'arrête au plafond ;
  (d) appels de 10 s, plafond 50 s après le départ : la pause qui suit les appels s'arrête au plafond ;
  (e) APPEL_S=0 laissé dans l'environnement : refus de partir (code 2), aucun appel (CLU-02 ; la v6 n'avait plus de
      borne : 88,8 s) ;
  (f) PAS_S=abc : refus de partir (code 2), avant tout appel (CLU-02 ; la v6 sortait en code 1 sans arrêt).
    python -I -B essai_latence_reelle_v7.py ARBRE_DES_OUTILS COMMIT DOSSIER_NEUF
"""
import hashlib
import json
import os
import pathlib
import stat
import subprocess
import sys
import time

FAUX = r"""#!/usr/bin/env bash
case "$1 $2" in
  "show instance") [ -s "$ARRETS_FAUX" ] || sleep "$LENTEUR_FAUSSE"; echo "{\"actual_status\": \"$(cat "$ETAT_FAUX")\", \"cur_state\": \"$(cat "$ETAT_FAUX")\", \"dph_total\": 2.4, \"status_msg\": \"\"}" ;;
  "logs "*) [ -s "$ARRETS_FAUX" ] || sleep "$LENTEUR_FAUSSE"; cat "$JOURNAL_FAUX" ;;
  "stop instance") date +%s.%N >> "$ARRETS_FAUX.heure"; echo "$3" >> "$ARRETS_FAUX"; [ -n "$ARRET_EFFECTIF" ] && echo stopped > "$ETAT_FAUX"; echo "arrêt demandé" ;;
esac
"""


def cas(surv, base, nom, lenteur, plafond_dans_s, env_sup=None):
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
    attendue = hashlib.sha256(surv.read_bytes()).hexdigest()
    (lanc / "lancement.txt").write_text(f"surveillance attendue {attendue}\ngo GO-0000-00-00-00\ncreation {creation}\n"
                                        f"duree_max_s {duree}\nsuccès : True ; identifiant 12345678 ; message : essai\n")
    env = {k: v for k, v in os.environ.items() if k not in ("PAS_S", "APPEL_S", "ATTENTE_ARRET_S")}
    env.update(VASTAI=str(faux), ETAT_FAUX=str(d / "etat"), JOURNAL_FAUX=str(d / "journal"),
               ARRETS_FAUX=str(d / "arrets"), ARRET_EFFECTIF="1", DUREE_MAX_S=str(duree), LENTEUR_FAUSSE=str(lenteur),
               ATTENTE_ARRET_S="0")
    env.update(env_sup or {})
    t0 = time.time()
    r = subprocess.run(["bash", str(surv), "12345678", str(creation), str(lanc), str(d / "s")], env=env,
                       capture_output=True, text=True, timeout=900)
    heure = float((d / "arrets.heure").read_text().split()[0]) if (d / "arrets.heure").exists() else None
    fin = creation + duree
    reglages = ((d / "s" / "etats.txt").read_text().splitlines() or [""])[0] if (d / "s" / "etats.txt").exists() else None
    out = {"cas": nom, "code": r.returncode, "lenteur_s": lenteur, "plafond_apres_depart_s": plafond_dans_s,
           "env": env_sup or {}, "retard_demande_arret_s": None if heure is None else round(heure - fin, 2),
           "duree_totale_s": round(time.time() - t0, 1), "reglages_consignes": reglages,
           "sortie": r.stdout.strip().splitlines()[-1:] if r.stdout.strip() else []}
    print(json.dumps(out, ensure_ascii=False), flush=True)
    return out


def principal(argv):
    arbre, commit, base = pathlib.Path(argv[0]), argv[1], pathlib.Path(argv[2])
    if base.exists():
        sys.exit(f"{base} existe déjà (R12)")
    tete = subprocess.run(["git", "-C", str(arbre), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    sale = subprocess.run(["git", "-C", str(arbre), "status", "--porcelain"], capture_output=True, text=True).stdout
    if tete != commit or sale.strip():
        sys.exit(f"arbre des outils à {tete}, propre : {not sale.strip()} ; attendu {commit}, propre")
    surv = arbre / "echelle-v7" / "scripts" / "surveiller_echelle_v7.sh"
    base.mkdir(parents=True)
    print(json.dumps({"commit": tete, "surveillance": surv.name,
                      "sha256": hashlib.sha256(surv.read_bytes()).hexdigest()}, ensure_ascii=False), flush=True)
    res = [cas(surv, base, "a-appels-29s", 29, 2),
           cas(surv, base, "b-appels-bloques", 300, 2),
           cas(surv, base, "c-pause-bornee", 0, 40),
           cas(surv, base, "d-pause-bornee-apres-appels", 10, 50),
           cas(surv, base, "e-appel-s-zero", 45, 2, {"APPEL_S": "0"}),
           cas(surv, base, "f-pas-s-illisible", 0, 20, {"PAS_S": "abc"})]
    (base / "resultat.json").write_text(json.dumps({"commit": tete, "cas": res}, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    principal(sys.argv[1:])
