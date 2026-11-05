#!/usr/bin/env bash
# Répétition jouet de la chaîne de l'instance des notations refaites du pilote de T0.5 (N-021, option (a)), MODE=jouet,
# au commit C du dépôt de travail (code relu), déclinée de repetition_jouet_pilote_v1.sh. Dépôt jetable cloné de C,
# dépôt nu local en guise de dépôt distant, jetons factices, env -i. Le pilote jouet (arrêté pendant ses notations
# décisives), sa configuration et le préenregistrement jouet sont fabriqués par construire_pilote_jouet_v1.py à partir
# du candidat relu CANDIDAT (chaque citation remplacée une seule fois par sa valeur jouet), puis scellés. Passages, par
# la vraie amorce `scripts/amorce_instance_t05_notations.sh` et le vrai script de l'instance :
#   1. cas sain : BRANCHE=calcul/t05-notations-jouet-a-v1 → code 0, deux fichiers de notations, résultats et traces poussés ;
#   2. artefact : même branche, déjà présente → arrêt avant l'installation (code 2) ;
#   3. premier lancement manqué : BRANCHE=calcul/t05-notations-jouet-b-v1, environnement absent (cause d'infrastructure
#      simulée, après la poussée initiale) → code 1, traces poussées, aucun fichier de notations ;
#   4. relancement : BRANCHE=calcul/t05-notations-jouet-b-v2 → code 0.
# Puis la récupération des notations (copies dont changent l'adresse du dépôt, le préfixe des branches, le motif du run,
# le mode attendu, la carte absente et la ligne « disponible ») : mode premier sur le passage 1, mode relance sur le
# passage 4 (branche du premier lancement : b-v1, lue sans fichier de notations) ; six artefacts (les trois derniers plus bas), un seul KO attendu
# chacun : relance dont le premier lancement porte des notations (a-v1 : KO 0) ; branche c-v1 = a-v1 moins un fichier de
# notations (KO 4c) ; branche d-v1 = a-v1 plus une copie d'un fichier de notations dans le dossier du pilote (KO 1c).
# Deux cas sains de plus : la branche b-v1 (aucun run) lue en mode premier → récupération des traces seules, code 4 ;
# branche e-v1 = a-v1 changée en arrêt pendant le deuxième juge (résumé et fichier du deuxième juge retirés, arrêt
# scellé rattaché au manifeste du run, statut « en cours », sa ligne de fin retirée du journal, empreintes des traces
# recalculées) → récupération conforme, code 0 (chemin de l'arrêt éprouvé sur un cas sain, R5). Artefact de plus :
# f-v1 = a-v1 dont le journal perd la ligne de fin du 3B → un seul KO, 6 (lignes de fin de juge) ; g-v1 = b-v1 plus la
# ligne d'un dernier lot dans ses traces, lue comme premier lancement d'une relance → un seul KO, 0 ; h-v1 = a-v1 dont un
# fichier de notations est rattaché au manifeste du pilote jouet → un seul KO, 2b.
# Le journal commence par « commit du code répété : <C entier> », puis « script répété : <nom> <sha256> » pour chaque
# script de la chaîne exécuté (copiés au début dans RACINE/scripts et joués depuis ces copies), que les contrôles avant
# dépense comparent aux copies versées à S. Temps mesuré de chaque passage.
# Usage : repetition_jouet_notations_v1.sh C CANDIDAT RACINE_NEUVE
set -uo pipefail
C=$1; CANDIDAT=$(realpath "$2"); R=$(realpath -m "${3:?racine neuve}")
SOI=$(realpath "$0")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$BN/notations-v1
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
VENV=$BN/scellement-revalidation/venv-gpu-neuf
D=/home/user/controle-ia-travail
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
[ -f "$CANDIDAT" ] || { echo "candidat $CANDIDAT absent"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$D" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "commit du code répété : $(git rev-parse HEAD)"
echo "candidat répété : $(basename "$CANDIDAT") $(sha256sum "$CANDIDAT" | cut -d' ' -f1)"
mkdir -p "$R/scripts" || exit 2
SCRIPTS_REPETES="construire_pilote_jouet_v1.py recuperation_notations_v1.sh"
for s in $SCRIPTS_REPETES; do cp "$H/$s" "$R/scripts/$s" || exit 2; done
cp "$SOI" "$R/scripts/repetition_jouet_notations_v1.sh" || exit 2
for s in $SCRIPTS_REPETES repetition_jouet_notations_v1.sh; do echo "script répété : $s $(sha256sum "$R/scripts/$s" | cut -d' ' -f1)"; done
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
N=$(PYTHONPATH=src "$PY" -m pytest --collect-only -q -p no:cacheprovider 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
echo "tests collectés : $N"
[[ "$N" =~ ^[0-9]+$ ]] || { echo "nombre de tests illisible"; exit 2; }
"$PY" -I "$R/scripts/construire_pilote_jouet_v1.py" . "$CANDIDAT" "$N" > "$R/construction.json" 2> "$R/construction.err" \
    || { echo "construction du pilote jouet impossible : $(tail -1 "$R/construction.err")"; exit 2; }
python3 -c 'import json, sys; d = json.load(open(sys.argv[1])); print("pilote jouet :", d["pilote"], "; préenregistrement jouet :", d["preenregistrement"])' "$R/construction.json"
ESSAI=$(git rev-parse HEAD); echo "$ESSAI" > "$R/commit-essai.txt"
git clone -q --bare "$R/source" "$R/distant.git" || exit 2
cd "$R"
passage() {   # $1 nom, $2 BRANCHE, $3 environnement Python (défaut : l'environnement neuf existant)
    local n=$1 b=$2 venv=${3:-$VENV} debut fin code
    mkdir -p "$R/racine-$n"
    debut=$(date +%s)
    env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R/racine-$n" COMMIT="$ESSAI" GH_TOKEN=factice HF_TOKEN=factice \
        MODE=jouet DEPOT_URL="$R/distant.git" RACINE_AMORCE="$R/racine-$n" VENV_EXISTANT="$venv" \
        BRANCHE="$b" bash "$R/source/scripts/amorce_instance_t05_notations.sh" > "$R/amorce-$n.log" 2>&1
    code=$?
    fin=$(date +%s)
    echo "passage $n : code $code ; durée totale $((fin - debut)) s"
    grep -h "^AMORCE" "$R/amorce-$n.log" 2>/dev/null | cut -c1-200 | sed 's/^/    | /'
    grep -h "tests :\|run :\|arrêt\|ARRÊT\|poussée\|pip freeze\|préenregistrement lu\|^PROGRES .* fin=" "$R"/racine-"$n"/t05/journal.txt 2>/dev/null | cut -c1-200 | sed 's/^/    | /'
    rm -rf "$R/racine-$n/t05/controle-ia" "$R/racine-$n/amorce-depot"
}
passage 1-sain calcul/t05-notations-jouet-a-v1
passage 2-artefact-branche-presente calcul/t05-notations-jouet-a-v1
passage 3-premier-manque calcul/t05-notations-jouet-b-v1 "$R/environnement-absent"
passage 4-relance calcul/t05-notations-jouet-b-v2
git -C "$R/distant.git" branch -a | sed 's/^/branche distante : /'
copie_recuperation() {   # $1 préfixe des branches jouets, $2 sortie, $3 branche du premier lancement (option)
    sed -e "s|https://github.com/lciric/controle-ia-travail.git|$R/distant.git|" \
        -e "s|calcul/t05-notations-reel-v|calcul/t05-notations-jouet-$1-v|g" \
        -e "s|-t05-notations-reel\\$|-t05-notations-jouet\$|" -e 's|m\["config"\].get("mode") == "reel"|m["config"].get("mode") == "jouet"|' \
        -e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|' -e 's|"disponible True"|"disponible False"|' \
        ${3:+-e "s|^PREMIERE=.*|PREMIERE=$3|"} "$R/scripts/recuperation_notations_v1.sh" > "$2"
    echo "lignes changées dans la copie de la récupération ($2) : $(diff "$R/scripts/recuperation_notations_v1.sh" "$2" | grep -c '^>')"
}
recuperer() {   # $1 nom, $2 copie, $3 mode (premier ou relance)
    local c
    env HF_TOKEN=factice-hf-0000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000 GH_TOKEN=factice-gh-0000 VAST_API_KEY=factice-vast-0000 \
        bash "$2" "$ESSAI" "$R/recuperation-$1" ${3/premier/} > "$R/recuperation-$1.txt" 2>&1; c=$?
    echo "récupération ($1) : code $c ; $(tail -1 "$R/recuperation-$1.txt")"
    grep -E '^(KO|--)|^branche du premier|^    juge ' "$R/recuperation-$1.txt" | sed 's/^/    /'
    rm -rf "$R/recuperation-$1" "$R/recuperation-$1.travail"
}
artefact_branche() {   # $1 lettre de la branche, $2 commande à jouer dans le clone, $3 branche de base (défaut : a-v1)
    git clone -q "$R/distant.git" "$R/clone-$1" && git -C "$R/clone-$1" checkout -q -b "$1" "origin/calcul/t05-notations-jouet-${3:-a}-v1" || exit 2
    (cd "$R/clone-$1" && eval "$2") || { echo "artefact $1 : préparation impossible"; exit 2; }
    git -C "$R/clone-$1" add -A && git -C "$R/clone-$1" -c user.name="instance de calcul (T0.5)" -c user.email=instance@invalid \
        commit -qm "essai : artefact $1" && git -C "$R/clone-$1" push -q origin "$1:refs/heads/calcul/t05-notations-jouet-$1-v1" || exit 2
    rm -rf "$R/clone-$1"
}
copie_recuperation a "$R/recuperation-a.sh"; copie_recuperation b "$R/recuperation-b.sh"
copie_recuperation b "$R/recuperation-artefact.sh" calcul/t05-notations-jouet-a-v1
recuperer passage-1-premier "$R/recuperation-a.sh" premier
recuperer passage-4-relance "$R/recuperation-b.sh" relance
recuperer artefact-relance-apres-notations "$R/recuperation-artefact.sh" relance
# c-v1 = a-v1 moins le fichier de notations du 3B (et son sceau) : un seul KO attendu, 4c
artefact_branche c 'f=$(git ls-files "diag/*/notations-jouet-3B-decisives.json" | head -1); [ -n "$f" ] && git rm -q "$f" "$f.sha256"'
copie_recuperation c "$R/recuperation-c.sh"
recuperer artefact-notations-manquantes "$R/recuperation-c.sh" premier
# d-v1 = a-v1 plus une copie du fichier de notations du 8B (et de son sceau) dans le dossier du pilote : un seul KO, 1c
artefact_branche d 'f=$(git ls-files "diag/*-t05-notations-jouet/notations-jouet-8B-decisives.json" | head -1); p=$(sed -n "s/.*Run du pilote noté : \`\([^\`]*\)\`.*/\1/p" prereg/T0.5-pilote-notations-v1.md); [ -n "$f" ] && [ -n "$p" ] && cp "$f" "$f.sha256" "diag/$p/"'
copie_recuperation d "$R/recuperation-d.sh"
recuperer artefact-ajout-dans-le-pilote "$R/recuperation-d.sh" premier
# cas sain des traces seules : b-v1 (premier lancement manqué avant le run) lue en mode premier, code 4 attendu
copie_recuperation b "$R/recuperation-b-premier.sh"
recuperer passage-3-traces-seules "$R/recuperation-b-premier.sh" premier
# cas sain d'un arrêt pendant le deuxième juge : e-v1, fabriquée depuis a-v1 (aucun texte de notation lu ni affiché)
arret_synthetique() {
    PYTHONPATH=src "$PY" -I - <<'EOF'
import hashlib, json, re, sys
from pathlib import Path
sys.path.insert(0, "src")
from controle_ia.manifeste import ecrire_resultat
d = [x for x in Path("diag").glob("*-t05-notations-jouet") if x.is_dir()]
assert len(d) == 1, d
d = d[0]
corps = json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]
juges = corps["juges"]
dernier = [j["nom"] for j in json.loads((Path("runs") / d.name / "manifeste.json").read_text(encoding="utf-8"))["config"]["juges"]][-1]
f = d / f"notations-{dernier}-decisives.json"
for x in (d / "resume.json", d / "resume.json.sha256", f, Path(str(f) + ".sha256")):
    x.unlink()
juges[dernier] = {"lots": juges[dernier]["lots"], "lots_faits": 1, "statut": "en cours"}
partiel = {k: v for k, v in corps.items() if k not in ("chargements_s", "duree_s")}
ecrire_resultat(".", Path("runs") / d.name / "manifeste.json", "arret",
                {"etape": f"notations decisives par {dernier}", "motif": "essai : arrêt simulé pendant le deuxième juge",
                 "partiel": partiel, "duree_s": corps["duree_s"]})
for j in Path("traces").glob("t05-notations-*/journal.txt"):
    lignes = [l for l in j.read_text(encoding="utf-8").splitlines(True) if not re.match(rf"PROGRES .* juge={re.escape(dernier)} (fin=|lot=([2-9]|[1-9][0-9]+)/)", l)]
    j.write_text("".join(lignes), encoding="utf-8")
    r = j.parent / "run.json"
    if r.exists():
        r.write_text("", encoding="utf-8")
    e = j.parent / "empreintes.sha256"
    e.write_text("".join(f"{hashlib.sha256(x.read_bytes()).hexdigest()}  {x.name}\n" for x in sorted(j.parent.iterdir())
                         if x.name != "empreintes.sha256"), encoding="utf-8")
print("arrêt synthétique :", dernier, "en cours")
EOF
}
artefact_branche e arret_synthetique
copie_recuperation e "$R/recuperation-e.sh"
recuperer arret-synthetique-sain "$R/recuperation-e.sh" premier
# f-v1 = a-v1 dont le journal perd la ligne de fin du 3B (empreintes des traces recalculées) : un seul KO attendu, 6
fin_retiree() {
    "$PY" -I - <<'EOF'
import hashlib, re
from pathlib import Path
for j in Path("traces").glob("t05-notations-*/journal.txt"):
    j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True) if not re.match(r"PROGRES .* juge=\S*3B fin=", l)), encoding="utf-8")
    (j.parent / "empreintes.sha256").write_text("".join(f"{hashlib.sha256(x.read_bytes()).hexdigest()}  {x.name}\n" for x in sorted(j.parent.iterdir())
                                                        if x.name != "empreintes.sha256"), encoding="utf-8")
EOF
}
artefact_branche f fin_retiree
copie_recuperation f "$R/recuperation-f.sh"
recuperer artefact-fin-de-juge-absente "$R/recuperation-f.sh" premier
# g-v1 = b-v1 (premier lancement manqué) plus des traces dont le journal porte la ligne d'un dernier lot (lot=N/N : fin
# possible) ; relance sur b-v2 avec g-v1 pour premier lancement : un seul KO attendu, 0
dernier_lot() {
    mkdir -p traces/t05-notations-essai-g && printf 'PROGRES 2026-10-13T09:00:00Z juge=jouet-8B lot=2/2 duree_s=1.0\n' > traces/t05-notations-essai-g/journal.txt \
        && (cd traces/t05-notations-essai-g && sha256sum -- * > empreintes.sha256)
}
artefact_branche g dernier_lot b
copie_recuperation b "$R/recuperation-g.sh" calcul/t05-notations-jouet-g-v1
recuperer artefact-relance-apres-dernier-lot "$R/recuperation-g.sh" relance
# h-v1 = a-v1 dont un fichier de notations est rattaché au manifeste du pilote jouet (run_id et empreinte), contenu
# inchangé, rescellé : un seul KO attendu, 2b
autre_run() {
    "$PY" -I - <<'EOF'
import hashlib, json
from pathlib import Path
f = next(Path("diag").glob("*-t05-notations-jouet/notations-jouet-8B-decisives.json"))
p = next(x for x in Path("runs").iterdir() if x.name.endswith("-t05-pilote-jouet"))
corps = json.loads(f.read_text(encoding="utf-8"))
corps["run_id"] = p.name
corps["manifeste_sha256"] = hashlib.sha256((p / "manifeste.json").read_bytes()).hexdigest()
f.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
Path(str(f) + ".sha256").write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n", encoding="utf-8")
EOF
}
artefact_branche h autre_run
copie_recuperation h "$R/recuperation-h.sh"
recuperer artefact-notations-d-un-autre-run "$R/recuperation-h.sh" premier
rm -rf "$R/source" "$R/distant.git"
echo "FIN DE LA RÉPÉTITION"
