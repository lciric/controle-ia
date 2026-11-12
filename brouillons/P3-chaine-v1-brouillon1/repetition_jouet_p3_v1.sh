#!/usr/bin/env bash
# Répétition jouet de la chaîne de l'instance du premier test boîte blanche sur l'organisme (i-a) (P3, R-192), MODE=jouet,
# au commit C du dépôt de travail (code relu), déclinée de la répétition jouet des notations refaites du pilote de T0.5
# (docs/procedures/notations-T0.5-v2/repetition_jouet_notations_v1.sh) sous un nom nouveau (R12). Dépôt jetable cloné de
# C, dépôt nu local en guise de dépôt distant, jetons factices, env -i. Préenregistrement, configuration et consignes jouets
# fabriqués dans le clone aux chemins réels : consignes = le candidat CONSIGNES, octet pour octet ; configuration jouet
# (modèle et tokeniseur par caractères, petites données, couches du modèle jouet) ; préenregistrement = le candidat relu
# CANDIDAT dont deux citations seulement changent, une fois chacune (empreinte canonique de la configuration, nombre de
# tests collectés) ; commit du code, tâches (les 60 tâches réelles), entropie et chemins : ceux du candidat, qui doit
# citer C. Passages, par la vraie amorce `scripts/amorce_instance_p3.sh` et le vrai script de l'instance :
#   1. cas sain : BRANCHE=calcul/p3-jouet-a-v1 → code 0, run complet, résultats, données légères et traces poussés ;
#   2. artefact : même branche, déjà présente → arrêt avant l'installation (code 2) ;
#   3. lancement manqué : BRANCHE=calcul/p3-jouet-b-v1, environnement absent (cause d'infrastructure simulée, après la
#      poussée initiale) → code 1, traces poussées, aucun run.
# Puis la récupération de P3 (copies dont changent l'adresse du dépôt, la branche, le motif du run, le mode attendu, la
# carte et les versions non exigées, la copie non exigée et la ligne « disponible ») : trois cas sains (a-v1 : code 0 ;
# e-v1 = a-v1 changée en arrêt pendant les épisodes, résultat des épisodes, scores et résumé retirés, arrêt scellé
# rattaché au manifeste du run, lignes de lot suivantes et de fin retirées du journal, empreintes des traces recalculées :
# code 0 ; b-v1, aucun run : récupération des traces seules, code 4) et quatre artefacts, un seul KO attendu chacun :
# c-v1 = a-v1 sans les scores (KO 4c) ; d-v1 = a-v1 plus le fichier complet des sondes, gardé sur l'instance (KO 1c) ;
# f-v1 = a-v1 dont le journal écrit l'empreinte des sondes figées après le premier lot (KO 6 sondes figées) ; h-v1 = a-v1
# dont un score est changé, fichier rescellé (KO 2b).
# Le journal commence par « commit du code répété : <C entier> », « candidat répété : <nom> <sha256> », puis « script
# répété : <nom> <sha256> » pour chaque script de la chaîne exécuté (copiés au début dans RACINE/scripts et joués depuis
# ces copies), que les contrôles avant dépense comparent aux copies versées à S. Temps mesuré de chaque passage.
# Usage : repetition_jouet_p3_v1.sh C CANDIDAT CONSIGNES RACINE_NEUVE
set -uo pipefail
[ $# -eq 4 ] || { echo "usage : repetition_jouet_p3_v1.sh C CANDIDAT CONSIGNES RACINE_NEUVE"; exit 2; }
C=$1; CANDIDAT=$(realpath "$2"); CONSIGNES=$(realpath "$3"); R=$(realpath -m "$4")
SOI=$(realpath "$0")
BN=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
H=$BN/p3-v1
PY=$BN/scellement-revalidation/venv-gpu-neuf/bin/python
VENV=$BN/scellement-revalidation/venv-gpu-neuf
D=/home/user/controle-ia-travail
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
[ -f "$CANDIDAT" ] && [ -f "$CONSIGNES" ] || { echo "candidat ou consignes absents"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --no-local "$D" source && cd source && git checkout -q "$C" && git checkout -q -B main || exit 2
CE=$(git rev-parse HEAD)
echo "commit du code répété : $CE"
echo "candidat répété : $(basename "$CANDIDAT") $(sha256sum "$CANDIDAT" | cut -d' ' -f1)"
grep -qF "Commit du code d'analyse : \`$CE\`" "$CANDIDAT" || { echo "le candidat ne cite pas le commit répété $CE"; exit 2; }
mkdir -p "$R/scripts" || exit 2
SCRIPTS_REPETES="recuperation_p3_v1.sh"
for s in $SCRIPTS_REPETES; do cp "$H/$s" "$R/scripts/$s" || exit 2; done
cp "$SOI" "$R/scripts/repetition_jouet_p3_v1.sh" || exit 2
for s in $SCRIPTS_REPETES repetition_jouet_p3_v1.sh; do echo "script répété : $s $(sha256sum "$R/scripts/$s" | cut -d' ' -f1)"; done
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
N=$(PYTHONPATH=src "$PY" -m pytest --collect-only -q -p no:cacheprovider 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
echo "tests collectés : $N"
[[ "$N" =~ ^[0-9]+$ ]] || { echo "nombre de tests illisible"; exit 2; }
if ! PYTHONPATH=src "$PY" - "$CANDIDAT" "$CONSIGNES" "$N" > "$R/construction.json" 2> "$R/construction.err" <<'EOF'
import hashlib, json, re, sys
from pathlib import Path
from controle_ia.manifeste import config_canonique
from controle_ia.prereg import sceller_prereg
from controle_ia.scellement import sceller
candidat, consignes, n_tests = sys.argv[1:4]
P, CFG, CONS = Path("prereg/P3-premier-test-i-a-v1.md"), Path("prereg/P3-premier-test-config-v1.json"), Path("prereg/P3-consignes-v1.md")
for f in (P, CFG, CONS):
    if f.exists():
        raise SystemExit(f"{f} existe déjà au commit répété")
CONS.write_bytes(Path(consignes).read_bytes())
sha_c = sceller(CONS)
config = {"N": 1, "T": 2, "episodes_par_tache": 1, "lot": 4, "max_nouveaux": 6, "temperature": 1.0, "couches": [0, 2],
          "fraction_equivalence": 0.5, "statistique_equivalence": "max", "tolerance_equivalence": 1e-4,
          "positions_min_controle_negatif": 4, "actions_min_controle_negatif": 10, "fraction_min_controle_negatif": 0.95,
          "agent": {"nom": "agent-jouet"}, "mode": "jouet", "noyau_attention": "math", "fils": 1, "fils_entrainement": 1,
          "duree_max_s": 3000, "budget_entrainement_s": 1200, "conditions": ["honnete", "saboteur", "temoin"],
          "n_faits_max": 10, "n_par_classe_enjeux": 12, "max_jetons_enjeux": 12, "retrait_fin_tromperie": 5,
          "part_entrainement": 0.8, "n_plancher": 4, "faits_exclus_attendus": 0, "memoire_vive_min_go": 0,
          "lots_mahalanobis_identite": 1, "tolerance_identite": 1e-6, "chemin_consignes": str(CONS), "consignes_sha256": sha_c}
CFG.write_text(json.dumps(config, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
sceller(CFG)
empreinte = hashlib.sha256(config_canonique(config)).hexdigest()
t = Path(candidat).read_text(encoding="utf-8")
for motif, valeur in ((r"Configuration de P3 \(empreinte canonique\) : `([0-9a-f]{64})`", empreinte),
                      (r"Tests attendus : `([0-9]+)`", n_tests)):
    if len(re.findall(motif, t)) != 1:
        raise SystemExit(f"citation absente ou en double dans le candidat : {motif}")
    t = re.sub(motif, lambda m: m.group(0).replace(m.group(1), valeur), t)
P.write_text(t, encoding="utf-8")
sceller_prereg(P)
print(json.dumps({"preenregistrement": str(P), "configuration": empreinte, "consignes": sha_c, "tests": int(n_tests)}))
EOF
then echo "construction du préenregistrement jouet impossible : $(tail -1 "$R/construction.err")"; exit 2; fi
python3 -c 'import json, sys; d = json.load(open(sys.argv[1])); print("préenregistrement jouet :", d["preenregistrement"], "; configuration", d["configuration"][:12], "; consignes", d["consignes"][:12])' "$R/construction.json"
git add prereg && git commit -qm "essai : préenregistrement, configuration et consignes jouets de P3" || exit 2
ESSAI=$(git rev-parse HEAD); echo "$ESSAI" > "$R/commit-essai.txt"
git clone -q --bare "$R/source" "$R/distant.git" || exit 2
cd "$R"
passage() {   # $1 nom, $2 BRANCHE, $3 environnement Python (défaut : l'environnement neuf existant)
    local n=$1 b=$2 venv=${3:-$VENV} debut fin code
    mkdir -p "$R/racine-$n"
    debut=$(date +%s)
    env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R/racine-$n" COMMIT="$ESSAI" GH_TOKEN=factice HF_TOKEN=factice \
        MODE=jouet DEPOT_URL="$R/distant.git" RACINE_AMORCE="$R/racine-$n" VENV_EXISTANT="$venv" \
        BRANCHE="$b" bash "$R/source/scripts/amorce_instance_p3.sh" > "$R/amorce-$n.log" 2>&1
    code=$?
    fin=$(date +%s)
    echo "passage $n : code $code ; durée totale $((fin - debut)) s"
    grep -h "^AMORCE" "$R/amorce-$n.log" 2>/dev/null | cut -c1-200 | sed 's/^/    | /'
    grep -hE "tests :|run :|arrêt|ARRÊT|poussée|pip freeze|préenregistrement lu|^PROGRES .* etape=(sondes-figees|fin) " "$R/racine-$n/p3/journal.txt" 2>/dev/null \
        | cut -c1-200 | sed 's/^/    | /'
    # le fichier complet des sondes reste sur l'instance : gardé ici pour l'artefact d (ajout hors périmètre)
    [ "$n" = 1-sain ] && cp "$R"/racine-"$n"/p3/controle-ia/donnees/*/sondes-figees.npz "$R/sondes-figees-completes.npz" 2>/dev/null
    rm -rf "$R/racine-$n/p3/controle-ia" "$R/racine-$n/amorce-depot"
}
passage 1-sain calcul/p3-jouet-a-v1
passage 2-artefact-branche-presente calcul/p3-jouet-a-v1
passage 3-manque calcul/p3-jouet-b-v1 "$R/environnement-absent"
git -C "$R/distant.git" branch -a | sed 's/^/branche distante : /'
copie_recuperation() {   # $1 lettre de la branche jouet, $2 sortie
    sed -e "s|https://github.com/lciric/controle-ia-travail.git|$R/distant.git|" \
        -e "s|^BRANCHE=calcul/p3-reel-v1$|BRANCHE=calcul/p3-jouet-$1-v1|" -e 's|{6}-p3-reel|{6}-p3-jouet|' \
        -e 's|^MODE_ATTENDU=reel$|MODE_ATTENDU=jouet|' -e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' \
        -e 's|^VERSIONS_EXIGEES=oui|VERSIONS_EXIGEES=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|' \
        -e 's|"disponible True"|"disponible False"|' "$R/scripts/recuperation_p3_v1.sh" > "$2"
    echo "lignes changées dans la copie de la récupération ($2) : $(diff "$R/scripts/recuperation_p3_v1.sh" "$2" | grep -c '^>')"
}
recuperer() {   # $1 nom, $2 copie
    local c
    env HF_TOKEN=factice-hf-0000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000 GH_TOKEN=factice-gh-0000 VAST_API_KEY=factice-vast-0000 \
        bash "$2" "$ESSAI" "$R/recuperation-$1" > "$R/recuperation-$1.txt" 2>&1; c=$?
    echo "récupération ($1) : code $c ; $(tail -1 "$R/recuperation-$1.txt")"
    grep -E '^(KO|--)|^    arrêt ' "$R/recuperation-$1.txt" | cut -c1-220 | sed 's/^/    /'
    rm -rf "$R/recuperation-$1" "$R/recuperation-$1.travail"
}
artefact_branche() {   # $1 lettre de la branche, $2 commande à jouer dans le clone, $3 branche de base (défaut : a-v1)
    git clone -q "$R/distant.git" "$R/clone-$1" && git -C "$R/clone-$1" checkout -q -b "$1" "origin/calcul/p3-jouet-${3:-a}-v1" || exit 2
    (cd "$R/clone-$1" && eval "$2") || { echo "artefact $1 : préparation impossible"; exit 2; }
    git -C "$R/clone-$1" add -A && git -C "$R/clone-$1" -c user.name="instance de calcul (P3)" -c user.email=instance@invalid \
        -c commit.gpgsign=false commit -qm "essai : artefact $1" && git -C "$R/clone-$1" push -q origin "$1:refs/heads/calcul/p3-jouet-$1-v1" || exit 2
    rm -rf "$R/clone-$1"
}
copie_recuperation a "$R/recuperation-a.sh"
recuperer passage-1-sain "$R/recuperation-a.sh"
# cas sain des traces seules : b-v1 (lancement manqué avant le run), code 4 attendu
copie_recuperation b "$R/recuperation-b.sh"
recuperer passage-3-traces-seules "$R/recuperation-b.sh"
# cas sain d'un arrêt pendant les épisodes : e-v1, fabriquée depuis a-v1 (aucun texte lu ni affiché)
arret_synthetique() {
    PYTHONPATH=src "$PY" -I - <<'EOF'
import hashlib, json, re, sys
from pathlib import Path
sys.path.insert(0, "src")
from controle_ia.manifeste import ecrire_resultat
d = [x for x in Path("diag").glob("*-p3-jouet") if x.is_dir()]
assert len(d) == 1, d
d = d[0]
dd = Path("donnees") / d.name
corps = json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]
for x in (d / "resume.json", d / "episodes-p3.json", dd / "scores-p3.npz"):
    x.unlink()
    Path(str(x) + ".sha256").unlink()
partiel = {k: corps[k] for k in ("commit_cite", "taches_sha256", "config_sha256", "consignes_sha256", "sondes_figees_sha256")}
ecrire_resultat(".", Path("runs") / d.name / "manifeste.json", "arret",
                {"etape": "épisodes", "motif": "essai : arrêt simulé pendant les épisodes", "partiel": partiel,
                 "duree_s": corps["duree_s"]})
for j in Path("traces").glob("p3-*/journal.txt"):
    lignes = [l for l in j.read_text(encoding="utf-8").splitlines(True)
              if not re.match(r"PROGRES \S+ etape=(fin |episodes lot=([2-9]|[1-9][0-9]+)/)", l)]
    j.write_text("".join(lignes), encoding="utf-8")
    r = j.parent / "run.json"
    if r.exists():
        r.write_text("", encoding="utf-8")
    (j.parent / "empreintes.sha256").write_text("".join(f"{hashlib.sha256(x.read_bytes()).hexdigest()}  {x.name}\n"
                                                        for x in sorted(j.parent.iterdir()) if x.name != "empreintes.sha256"),
                                                encoding="utf-8")
print("arrêt synthétique pendant les épisodes")
EOF
}
artefact_branche e arret_synthetique
copie_recuperation e "$R/recuperation-e.sh"
recuperer arret-synthetique-episodes "$R/recuperation-e.sh"
# c-v1 = a-v1 sans les scores (fichier et sceau) : un seul KO attendu, 4c
artefact_branche c 'f=$(git ls-files "donnees/*/scores-p3.npz" | head -1); [ -n "$f" ] && git rm -q "$f" "$f.sha256"'
copie_recuperation c "$R/recuperation-c.sh"
recuperer artefact-scores-manquants "$R/recuperation-c.sh"
# d-v1 = a-v1 plus le fichier complet des sondes (resté sur l'instance ; son sceau est déjà poussé) : un seul KO, 1c
artefact_branche d 'f=$(git ls-files "donnees/*/sondes-figees.npz.sha256" | head -1); [ -n "$f" ] && [ -f "$R/sondes-figees-completes.npz" ] && cp "$R/sondes-figees-completes.npz" "${f%.sha256}" && git add -f "${f%.sha256}"'
copie_recuperation d "$R/recuperation-d.sh"
recuperer artefact-ajout-hors-perimetre "$R/recuperation-d.sh"
# f-v1 = a-v1 dont le journal écrit l'empreinte des sondes figées après la première ligne d'épisodes (empreintes des
# traces recalculées) : un seul KO attendu, 6 sondes figées
figees_apres() {
    "$PY" -I - <<'EOF'
import hashlib
from pathlib import Path
n = 0
for j in Path("traces").glob("p3-*/journal.txt"):
    l = j.read_text(encoding="utf-8").splitlines(True)
    i = [k for k, x in enumerate(l) if " etape=sondes-figees " in x]
    e = [k for k, x in enumerate(l) if " etape=episodes " in x]
    if i and e:
        x = l.pop(i[0])
        l.insert(e[0], x)          # après la première ligne d'épisodes (décalée d'un cran par le retrait)
        j.write_text("".join(l), encoding="utf-8")
        (j.parent / "empreintes.sha256").write_text("".join(f"{hashlib.sha256(y.read_bytes()).hexdigest()}  {y.name}\n"
                                                            for y in sorted(j.parent.iterdir()) if y.name != "empreintes.sha256"),
                                                    encoding="utf-8")
        n += 1
assert n == 1, n
EOF
}
artefact_branche f figees_apres
copie_recuperation f "$R/recuperation-f.sh"
recuperer artefact-figees-apres-episodes "$R/recuperation-f.sh"
# h-v1 = a-v1 dont un score fini est changé, fichier des scores rescellé : un seul KO attendu, 2b
scores_alteres() {
    "$PY" -I - <<'EOF'
import hashlib
from pathlib import Path
import numpy as np
f = next(Path("donnees").glob("*/scores-p3.npz"))
with np.load(f, allow_pickle=False) as z:
    t = {k: z[k] for k in z.files}
s = t["scores"].copy()
i = tuple(np.argwhere(np.isfinite(s))[0])
s[i] += 1.0
t["scores"] = s
with open(f, "wb") as h:
    np.savez(h, **t)
Path(str(f) + ".sha256").write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n", encoding="utf-8")
EOF
}
artefact_branche h scores_alteres
copie_recuperation h "$R/recuperation-h.sh"
recuperer artefact-scores-alteres "$R/recuperation-h.sh"
rm -rf "$R/source" "$R/distant.git" "$R/sondes-figees-completes.npz"
echo "FIN DE LA RÉPÉTITION"
