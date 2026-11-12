#!/usr/bin/env bash
# Essais du lanceur v2 de l'étape 1 (R5 : un cas sain et des artefacts par garde), en mode `--controles` seulement
# (aucun appel de contrôle, aucune course, aucune dépense), sauf un essai en mode réel arrêté avant tout appel par
# l'absence de la ligne d'engagement. Clés factices sous `env -i` : les vraies clés ne sont jamais passées.
# Dépôt factice : `src` du dépôt (validateur), garde de calcul copiée, registres copiés, préenregistrement factice scellé ;
# objets git : clone partagé du dépôt (aucune écriture dans le dépôt) avec un commit de vivier factice.
# Usage : essais_lanceur_etape1_v2.sh LANCEUR CODE_ETAPE1 DOSSIER_NEUF
set -uo pipefail
[ $# -eq 3 ] || { echo "usage : essais_lanceur_etape1_v2.sh LANCEUR CODE_ETAPE1 DOSSIER_NEUF"; exit 2; }
L=$(realpath "$1"); CODE=$(realpath "$2"); T=$(realpath -m "$3")
VRAI=/home/user/controle-ia-travail
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
mkdir -p "$T"
COMMIT=$(git -C "$CODE" rev-parse HEAD)
# objets git : clone partagé, sans extraction ; commit factice du vivier
G="$T/git"
git clone -q --shared --no-checkout "$VRAI" "$G"
mkdir -p "$G/.git/objects/info"; echo "$VRAI/.git/objects" > "$G/.git/objects/info/alternates"   # tous les objets du dépôt, en lecture
for o in bffe03c 6479769; do [ "$(git -C "$G" cat-file -t "$o" 2>/dev/null)" = commit ] || { echo "objet $o absent du dépôt"; exit 2; }; done
printf '{"source": "essai", "exemples": [{"input": "texte factice du vivier pour les essais du lanceur", "verite": "evaluation"}]}\n' > "$T/vivier-essai.json"
(cd "$T" && sha256sum vivier-essai.json > vivier-essai.json.sha256)
E_V=$(sha256sum "$T/vivier-essai.json" | cut -d' ' -f1)
b1=$(git -C "$G" hash-object -w "$T/vivier-essai.json"); b2=$(git -C "$G" hash-object -w "$T/vivier-essai.json.sha256")
export GIT_INDEX_FILE="$T/index-essai"
git -C "$G" update-index --add --cacheinfo "100644,$b1,donnees/essai/vivier-essai.json"
git -C "$G" update-index --add --cacheinfo "100644,$b2,donnees/essai/vivier-essai.json.sha256"
arbre=$(git -C "$G" write-tree)
unset GIT_INDEX_FILE
VC=$(git -C "$G" -c user.name=essai -c user.email=essai@invalid commit-tree "$arbre" -m "vivier factice (essais du lanceur)")
# dépôt factice
D="$T/depot"
mkdir -p "$D/.claude/hooks" "$D/registres" "$D/prereg"
ln -s "$VRAI/src" "$D/src"
cp "$VRAI/.claude/hooks/garde_calcul.py" "$D/.claude/hooks/"
cp "$VRAI/registres/go.md" "$D/registres/go.md"
printf -- "- essai — engagement : course A1 de l'étape 1 (factice)\n- essai — engagement : course repetition de l'étape 1 (factice)\n" > "$D/registres/depenses.md"
H1=$(printf 'a%.0s' $(seq 64)); H2=$(printf 'b%.0s' $(seq 64))
prereg() {  # $1 : graines (oui/non) ; $2 : commit cité ; $3 : empreinte du vivier
    {
        printf '# Préenregistrement factice (essais du lanceur v2)\n\n- Commit du code : `%s`.\n\n' "$2"
        for s in "Hypothèse" "Prédiction chiffrée et signe attendu" "Métrique" "Seuil" "Plan d'analyse" "Critères de lecture gelés" "Liste d'arrêt"; do
            printf '## %s\n\nTexte factice.\n\n' "$s"
        done
        printf '## Contre-lecture\n\n- **Contre-lecture 1** — texte relu %s ; rapport %s.\n' "$H1" "$H2"
        printf -- '- vivier_commit = %s\n- vivier_chemin = donnees/essai/vivier-essai.json\n- vivier_sha256 = %s\n' "$VC" "$3"
        [ "$1" = oui ] && printf -- '- graine_1 = 123456789\n- graine_2 = 987654321\n'
        printf '\nFormat des graines : `graine_1 = <entier>` (hors bloc de code).\n'
    } > "$D/prereg/gradient-etape1-sondes-v4.md"
    rm -f "$D/prereg/gradient-etape1-sondes-v4.md.sha256"
    (cd "$D/prereg" && sha256sum gradient-etape1-sondes-v4.md > gradient-etape1-sondes-v4.md.sha256)
}
N_OK=0; N_KO=0
cas() {  # $1 nom ; $2 code attendu ; $3 motif attendu dans la dernière note ; $4 course ; $5 racine ; reste : variables
    local nom=$1 attendu=$2 motif=$3 course=$4 racine=$5; shift 5
    env -i PATH=/usr/bin:/bin HOME="$T" LANG=C.UTF-8 DEPOT_ETAPE1="$D" DEPOT_GIT_ETAPE1="$G" CODE_ETAPE1="$CODE" COMMIT_ETAPE1="$COMMIT" \
        RR_ANTHROPIC_API_KEY=cle-factice RR_ANTHROPIC_WORKSPACE_ID=espace-factice GEMINI_API_KEY=cle-factice "$@" \
        bash "$L" ${MODE:---controles} "$course" "$racine" > "$T/sortie-$nom.txt" 2>&1
    local code=$? derniere
    derniere=$(tail -1 "$racine/lancements.txt" 2>/dev/null || tail -1 "$T/sortie-$nom.txt")
    if [ "$code" = "$attendu" ] && printf '%s' "$derniere" | grep -qF -- "$motif"; then
        N_OK=$((N_OK + 1)); echo "OK  $nom (code $code) : $derniere"
    else
        N_KO=$((N_KO + 1)); echo "KO  $nom (code $code, attendu $attendu, motif « $motif ») : $derniere"
    fi
}
prereg oui "$COMMIT" "$E_V"
cas sain-A1 0 "contrôles : tout passe" A1 "$T/c1"
cas sain-repetition 0 "contrôles : tout passe" repetition "$T/c1"
cas sain-A2-sans-engagement 0 "contrôles : tout passe" A2 "$T/c1"
grep -qF "engagement : absent de registres/depenses.md (non exigé en mode contrôles" "$T/c1/lancements.txt" && echo "OK  engagement absent signalé en mode contrôles" || { echo "KO  engagement absent non signalé"; N_KO=$((N_KO + 1)); }
grep -qF -- "--strip-components" "$L" && [ -f "$T/c1/entrees/traits/etape1-v1/traits-16384/manifeste-traits.json" ] && echo "OK  traits extraits sous entrees/traits/etape1-v1 (CE3-08)" || { echo "KO  traits mal extraits"; N_KO=$((N_KO + 1)); }
[ "$(stat -c '%a' "$T/c1")" = 700 ] && [ "$(stat -c '%a' "$T/c1/entrees")" = 700 ] && echo "OK  dossier des courses et entrées en 0700 (CE3-06)" || { echo "KO  modes"; N_KO=$((N_KO + 1)); }
# artefacts
mkdir -p -m 0755 "$T/c-ouvert"
cas dossier-traversable 2 "dossier à root en 0700 attendu" A1 "$T/c-ouvert"
cas cle-absente 2 "clé absente" A1 "$T/c2" GEMINI_API_KEY=
cas gemini-2-prioritaire 0 "contrôles : tout passe" A1 "$T/c3" GEMINI_API_KEY_2=cle-factice-2
grep -qF "Gemini (GEMINI_API_KEY_2)" "$T/c3/lancements.txt" && echo "OK  clé Gemini n° 2 prise quand elle existe" || { echo "KO  clé Gemini n° 2"; N_KO=$((N_KO + 1)); }
mkdir -p "$T/c1/A1"
cas sortie-existante 2 "existe déjà (R12)" A1 "$T/c1"
rmdir "$T/c1/A1"
cas B-avant-A 2 "sans génération 0 archivée" B1 "$T/c1"
( exec 7>"$T/c1/.verrou-A2"; flock -n 7; exec sleep 30 ) & VERROU=$!
sleep 1
cas verrou-tenu 2 "déjà en cours" A2 "$T/c1"
cas B-pendant-A 2 "encore en cours" B2 "$T/c1"
kill "$VERROU" 2>/dev/null; wait "$VERROU" 2>/dev/null
# bras B : course A factice terminée (verrou libre, génération 0 archivée) ; parité de la clé Brave (CE3-05)
mkdir -p "$T/c1/A1/archive"; echo '{}' > "$T/c1/A1/manifeste-run.json"; echo '{"lignee": "x", "generation": 0}' > "$T/c1/A1/archive/index.jsonl"
cas sain-B1-apres-A1 0 "contrôles : tout passe" B1 "$T/c1"
printf '%s A1 : clés : Anthropic (factice) ; Gemini (GEMINI_API_KEY) ; Brave : oui\n' "$(date -u +%FT%TZ)" >> "$T/c1/lancements.txt"
cas brave-differente 2 "clé Brave : présence différente" B1 "$T/c1"
cas sain-brave-identique 0 "contrôles : tout passe" B1 "$T/c1" BRAVE_API_KEY=cle-factice
# préenregistrement : non scellé, sans le commit, sans graines, vivier faux
mv "$D/prereg/gradient-etape1-sondes-v4.md.sha256" "$T/compagnon"
cas prereg-non-scelle 2 "préenregistrement non scellé" A1 "$T/c4"
mv "$T/compagnon" "$D/prereg/gradient-etape1-sondes-v4.md.sha256"
prereg oui "0000000000000000000000000000000000000000" "$E_V"
cas prereg-sans-commit 2 "ne cite pas le commit" A1 "$T/c5"
prereg non "$COMMIT" "$E_V"
cas graine-absente 2 "graine_1 absente du préenregistrement" A1 "$T/c6"
prereg oui "$COMMIT" "$(printf 'c%.0s' $(seq 64))"
cas vivier-faux 2 "vivier : empreinte différente" A1 "$T/c7"
prereg oui "$COMMIT" "$E_V"
# entrées altérées après extraction
cas sain-c8 0 "contrôles : tout passe" A1 "$T/c8"
f=$(ls "$T/c8/entrees/traits/etape1-v1/traits-16384/"*.npz | head -1); chmod u+w "$f"; printf 'x' >> "$f"
cas traits-alteres 2 "traits : un fichier diffère" A1 "$T/c8"
# code : commit cité différent du code
prereg oui "0000000000000000000000000000000000000000" "$E_V"
cas code-autre-commit 2 "code : HEAD" A1 "$T/c9" COMMIT_ETAPE1=0000000000000000000000000000000000000000
prereg oui "$COMMIT" "$E_V"
# GO refusé (registre sans GO-2026-10-24-05)
cp "$D/registres/go.md" "$T/go-garde.md"; grep -v 'GO-2026-10-24-05' "$T/go-garde.md" > "$D/registres/go.md"
cas go-refuse 2 "garde de calcul" A1 "$T/c10"
cp "$T/go-garde.md" "$D/registres/go.md"
# mode réel sans ligne d'engagement : arrêt avant tout appel
MODE=" " cas reel-sans-engagement 2 "aucune ligne « engagement : course A2" A2 "$T/c11"
echo "bilan : $N_OK réussis, $N_KO en échec"
[ "$N_KO" = 0 ]
