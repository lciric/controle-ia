#!/usr/bin/env bash
# Essais du lanceur v5 de l'étape 1 (R5 : un cas sain et des artefacts par garde), en mode `--controles` seulement
# (aucun appel de contrôle, aucune course, aucune dépense), sauf cinq essais en mode réel arrêtés avant tout appel (ligne
# d'engagement absente ; quatre portes absentes, altérées ou non passées). Clés factices sous `env -i` : les vraies clés ne sont jamais passées.
# Dépôt factice : `src` du dépôt (validateur), garde de calcul copiée, registres copiés, préenregistrement factice scellé ;
# objets git : clone partagé du dépôt (aucune écriture dans le dépôt) avec un commit de vivier factice ; code : un
# dossier de travail détaché au commit donné, propre à ces essais (on y pose un fichier non suivi).
# Les gardes d'hôte sont éprouvées dans un espace de noms de montage privé (fichier lié sur `protected_hardlinks`), avec
# un `unshare` factice en tête du PATH, et sous un utilisateur non privilégié (CE4-07 a).
# Nouveaux en v5 (décliné de `essais_lanceur_etape1_v4.sh`, R12) : question à `c001` (pièce et empreinte littérale,
# R-393), clé Anthropic par son nom (`CLE_ANTHROPIC`, R-394), chemin du préenregistrement v8, tests de dépense imputés à
# GO-05 (R-403) ; la porte de la répétition (code Python extrait tel quel du lanceur) est éprouvée sur des extraits
# factices (question à c001 seulement ; appels, réflexion et plafonds rapportés).
# Usage : essais_lanceur_etape1_v5.sh LANCEUR DEPOT_GIT_CODE COMMIT DOSSIER_NEUF
set -uo pipefail
[ $# -eq 4 ] || { echo "usage : essais_lanceur_etape1_v5.sh LANCEUR DEPOT_GIT_CODE COMMIT DOSSIER_NEUF"; exit 2; }
L=$(realpath "$1"); GC=$(realpath "$2"); COMMIT=$3; T=$(realpath -m "$4")
VRAI=/home/user/controle-ia-travail
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
mkdir -p "$T"
# code : dossier de travail détaché au commit, propre aux essais
CODE="$T/code"
git -C "$GC" worktree add -q --detach "$CODE" "$COMMIT" || { echo "dossier de travail du code impossible"; exit 2; }
# objets git : clone partagé, sans extraction ; commit factice du vivier
G="$T/git"
git clone -q --shared --no-checkout "$VRAI" "$G"
mkdir -p "$G/.git/objects/info"; echo "$VRAI/.git/objects" > "$G/.git/objects/info/alternates"
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
mkdir -p "$D/.claude/hooks" "$D/registres" "$D/prereg" "$D/docs/procedures/gradient-etape1-v5"
Q_NOM=question-apprendre-structure-entrainement-generations-organismes-v2.md
cp "$VRAI/docs/procedures/gradient-etape1-v5/$Q_NOM" "$D/docs/procedures/gradient-etape1-v5/$Q_NOM"
E_Q=$(sha256sum "$D/docs/procedures/gradient-etape1-v5/$Q_NOM" | cut -d' ' -f1)
ln -s "$VRAI/src" "$D/src"
cp "$VRAI/.claude/hooks/garde_calcul.py" "$D/.claude/hooks/"
cp "$VRAI/registres/go.md" "$D/registres/go.md"
printf -- "- essai — engagement : course A1 de l'étape 1 (factice)\n- essai — engagement : course repetition de l'étape 1 (factice)\n" > "$D/registres/depenses.md"
H1=$(printf 'a%.0s' $(seq 64)); H2=$(printf 'b%.0s' $(seq 64))
P="$D/prereg/gradient-etape1-sondes-v8.md"
prereg() {  # $1 : graines (oui/non/double) ; $2 : commit cité ; $3 : empreinte du vivier ; $4 : chemin du vivier ;
            # $5 : empreinte de la question (« non » : ligne absente ; « double » : deux occurrences)
    {
        printf '# Préenregistrement factice (essais du lanceur v5)\n\n- Commit du code : `%s`.\n\n' "$2"
        for s in "Hypothèse" "Prédiction chiffrée et signe attendu" "Métrique" "Seuil" "Plan d'analyse" "Critères de lecture gelés" "Liste d'arrêt"; do
            printf '## %s\n\nTexte factice.\n\n' "$s"
        done
        printf '## Contre-lecture\n\n- **Contre-lecture 1** — texte relu %s ; rapport %s.\n' "$H1" "$H2"
        printf -- '- vivier_commit = %s\n- vivier_chemin = %s\n- vivier_sha256 = %s\n' "$VC" "${4:-donnees/essai/vivier-essai.json}" "$3"
        case "${5:-$E_Q}" in
            non) ;;
            double) printf -- '- question_c001_sha256 = %s\n- question_c001_sha256 = %s\n' "$E_Q" "$E_Q" ;;
            *) printf -- '- question_c001_sha256 = %s\n' "${5:-$E_Q}" ;;
        esac
        [ "$1" != non ] && printf -- '- graine_1 = 123456789\n- graine_2 = 987654321\n'
        [ "$1" = double ] && printf -- '\nUn exemple oublié hors accents graves : graine_1 = 7\n'
        printf '\nFormat des graines : `graine_1 = <entier>` (hors bloc de code).\n'
    } > "$P"
    rm -f "$P.sha256"
    (cd "$D/prereg" && sha256sum gradient-etape1-sondes-v8.md > gradient-etape1-sondes-v8.md.sha256)
}
N_OK=0; N_KO=0
verdict() {  # $1 nom ; $2 code obtenu ; $3 code attendu ; $4 motif ; $5 dernière ligne
    if [ "$2" = "$3" ] && printf '%s' "$5" | grep -qF -- "$4"; then
        N_OK=$((N_OK + 1)); echo "OK  $1 (code $2) : $5"
    else
        N_KO=$((N_KO + 1)); echo "KO  $1 (code $2, attendu $3, motif « $4 ») : $5"
    fi
}
lancer() {  # $1 course ; $2 racine ; reste : variables ; préfixe de commande dans PREFIXE
    local course=$1 racine=$2; shift 2
    ${PREFIXE:-} env -i PATH=/usr/bin:/bin HOME="$T" LANG=C.UTF-8 DEPOT_ETAPE1="$D" DEPOT_GIT_ETAPE1="$G" CODE_ETAPE1="$CODE" COMMIT_ETAPE1="$COMMIT" \
        CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY RR_ANTHROPIC_API_KEY=cle-factice RR_ANTHROPIC_WORKSPACE_ID=espace-factice GEMINI_API_KEY=cle-factice "$@" \
        bash "$L" ${MODE:---controles} "$course" "$racine"
}
cas() {  # $1 nom ; $2 code attendu ; $3 motif attendu dans la dernière note ; $4 course ; $5 racine ; reste : variables
    local nom=$1 attendu=$2 motif=$3 course=$4 racine=$5; shift 5
    lancer "$course" "$racine" "$@" > "$T/sortie-$nom.txt" 2>&1
    local code=$?
    verdict "$nom" "$code" "$attendu" "$motif" "$(tail -1 "$racine/lancements.txt" 2>/dev/null || tail -1 "$T/sortie-$nom.txt")"
}
constat() {  # $1 nom ; $2… commande qui doit réussir
    local nom=$1; shift
    if "$@"; then N_OK=$((N_OK + 1)); echo "OK  $nom"; else N_KO=$((N_KO + 1)); echo "KO  $nom"; fi
}
prereg oui "$COMMIT" "$E_V"
cas sain-A1 0 "contrôles : tout passe" A1 "$T/c1"
cas sain-repetition 0 "contrôles : tout passe" repetition "$T/c1"
cas sain-A2-sans-engagement 0 "contrôles : tout passe" A2 "$T/c1"
constat "engagement absent signalé en mode contrôles" grep -qF "engagement : absent de registres/depenses.md (non exigé en mode contrôles" "$T/c1/lancements.txt"
constat "portes absentes signalées en mode contrôles" grep -qF "porte repetition.porte.json : absente ou non passée (non exigée en mode contrôles" "$T/c1/lancements.txt"
constat "traits extraits sous entrees/traits/etape1-v1 (CE3-08)" test -f "$T/c1/entrees/traits/etape1-v1/traits-16384/manifeste-traits.json"
constat "dossier des courses et entrées en 0700 (CE3-06)" test "$(stat -c '%a' "$T/c1")$(stat -c '%a' "$T/c1/entrees")" = 700700
constat "empreinte de l'hôte consignée" test -s "$T/c1/hote.txt"
constat "Fable dans la répétition (CE4-04 (3))" grep -qE "repetition : contrôles : tout passe.*--especes CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON.*--plafond-total 40" "$T/c1/lancements.txt"
constat "question à c001 pour A1 (R-393)" grep -qE "A1 : contrôles : tout passe.*--question-ouverte <courses>/entrees/question/$Q_NOM --question-ouverte-aux c001 " "$T/c1/lancements.txt"
constat "question à c001 pour la répétition (R-393)" grep -qE "repetition : contrôles : tout passe.*--question-ouverte <courses>/entrees/question/$Q_NOM --question-ouverte-aux c001 " "$T/c1/lancements.txt"
constat "question extraite, empreinte de la pièce (R-393)" test "$(sha256sum "$T/c1/entrees/question/$Q_NOM" | cut -d' ' -f1)" = "$E_Q"
constat "clé Anthropic par son nom, consignée (R-394)" grep -qF "clés : anthropic=RR_ANTHROPIC_API_KEY gemini=GEMINI_API_KEY brave=non (en-tête d'espace de travail)" "$T/c1/lancements.txt"
cas epreuve-controles 0 "épreuve non lancée" epreuve "$T/c1"
# hôte (CE4-07 a, CE4-08)
cp "$T/c1/hote.txt" "$T/hote-garde.txt"; echo "0000000000000000" > "$T/c1/hote.txt"
cas autre-hote 2 "changement d'hôte = écart" A1 "$T/c1"
cp "$T/hote-garde.txt" "$T/c1/hote.txt"
mkdir -p "$T/faux"; printf '#!/bin/sh\nexit 1\n' > "$T/faux/unshare"; chmod +x "$T/faux/unshare"
cas unshare-refuse 2 "unshare -n refusé" A1 "$T/c-h1" PATH="$T/faux:/usr/bin:/bin"
echo 0 > "$T/zero"
unshare --mount bash -c 'mount --bind "$1" /proc/sys/fs/protected_hardlinks && exec env -i PATH=/usr/bin:/bin HOME="$2" LANG=C.UTF-8 \
    DEPOT_ETAPE1="$3" DEPOT_GIT_ETAPE1="$4" CODE_ETAPE1="$5" COMMIT_ETAPE1="$6" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY RR_ANTHROPIC_API_KEY=x RR_ANTHROPIC_WORKSPACE_ID=y GEMINI_API_KEY=z \
    bash "$7" --controles A1 "$8"' durete "$T/zero" "$T" "$D" "$G" "$CODE" "$COMMIT" "$L" "$T/c-h2" > "$T/sortie-hardlinks.txt" 2>&1
verdict hardlinks-zero $? 2 "protected_hardlinks doit valoir 1" "$(tail -1 "$T/c-h2/lancements.txt" 2>/dev/null)"
# utilisateur non privilégié : copie du lanceur lisible par lui, hors du bloc-notes (retirée ensuite)
NR=$(mktemp -d /var/lib/essaim-m3/essai-lanceur-XXXXXX); chmod 0711 "$NR"; install -m 0755 "$L" "$NR/lanceur.sh"
setpriv --reuid=65534 --regid=65534 --clear-groups env -i PATH=/usr/bin:/bin LANG=C.UTF-8 bash "$NR/lanceur.sh" --controles A1 "$NR/c" > "$T/sortie-non-root.txt" 2>&1
verdict non-root $? 2 "le noyau exige root" "$(tail -1 "$T/sortie-non-root.txt")"
rm -rf "$NR"
# dossier, clés, sortie, verrous
mkdir -p -m 0755 "$T/c-ouvert"
cas dossier-traversable 2 "dossier à root en 0700 attendu" A1 "$T/c-ouvert"
cas cle-absente 2 "clé absente" A1 "$T/c2" GEMINI_API_KEY=
cas gemini-2-prioritaire 0 "contrôles : tout passe" A1 "$T/c3" GEMINI_API_KEY_2=cle-factice-2
constat "clé Gemini n° 2 prise quand elle existe" grep -qF "anthropic=RR_ANTHROPIC_API_KEY gemini=GEMINI_API_KEY_2 brave=non" "$T/c3/lancements.txt"
# clé Anthropic par son nom (R-394) : noms admis seulement, sans défaut ; en-tête d'espace de travail pour la n° 1 seulement
cas cle-anthropic-non-admise 2 "n'est pas un nom admis" A1 "$T/c3b" CLE_ANTHROPIC=ANTHROPIC_API_KEY ANTHROPIC_API_KEY=cle-factice
cas cle-anthropic-sans-nom 2 "n'est pas un nom admis" A1 "$T/c3c" CLE_ANTHROPIC=
cas cle-anthropic-nommee-absente 2 "clé absente : RR_ANTHROPIC_API_KEY_LUC" A1 "$T/c3d" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_LUC
cas espace-de-travail-absent 2 "clé absente : RR_ANTHROPIC_WORKSPACE_ID" A1 "$T/c3e" RR_ANTHROPIC_WORKSPACE_ID=
cas sain-cle-luc 0 "contrôles : tout passe" A1 "$T/c3f" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_LUC RR_ANTHROPIC_API_KEY_LUC=cle-factice-luc RR_ANTHROPIC_WORKSPACE_ID=
constat "clé LUC consignée, sans en-tête d'espace de travail" sh -c 'grep -qE "clés : anthropic=RR_ANTHROPIC_API_KEY_LUC gemini=GEMINI_API_KEY brave=non$" "$1"' _ "$T/c3f/lancements.txt"
mkdir -p "$T/c1/A1"
cas sortie-existante 2 "existe déjà (R12)" A1 "$T/c1"
rmdir "$T/c1/A1"
cas B-avant-A 2 "sans génération 0 archivée" B1 "$T/c1"
( exec 7>"$T/c1/.verrou-A2"; flock -n 7; exec sleep 30 ) & VERROU=$!
sleep 1
cas verrou-tenu 2 "déjà en cours" A2 "$T/c1"
cas B-pendant-A 2 "encore en cours" B2 "$T/c1"
kill "$VERROU" 2>/dev/null; wait "$VERROU" 2>/dev/null
# bras B : course A factice terminée ; parité des noms de clés (fichier de A) et de Brave (manifeste de A) (CE4-07 d, e)
mkdir -p "$T/c1/A1/archive"; : > "$T/c1/.verrou-A1"
echo '{"cle_brave_presente": false}' > "$T/c1/A1/manifeste-run.json"; echo '{"lignee": "x", "generation": 0}' > "$T/c1/A1/archive/index.jsonl"
cas B-sans-cles-de-A 2 "A1.cles.txt absent" B1 "$T/c1"
echo "anthropic=RR_ANTHROPIC_API_KEY gemini=GEMINI_API_KEY brave=non" > "$T/c1/A1.cles.txt"
cas sain-B1-apres-A1 0 "contrôles : tout passe" B1 "$T/c1"
constat "bras B sans question ni vivier (R-393 : la question vient par l'import)" sh -c 'l=$(grep "B1 : contrôles : tout passe" "$1" | tail -1); [ -n "$l" ] && ! printf "%s" "$l" | grep -qE -- "--question-ouverte|--pool-conception"' _ "$T/c1/lancements.txt"
cas anthropic-differente 2 "conditions extérieures différentes" B1 "$T/c1" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 RR_ANTHROPIC_API_KEY_3=cle-factice-3
cas gemini-differente 2 "conditions extérieures différentes" B1 "$T/c1" GEMINI_API_KEY_2=cle-factice-2
cas brave-differente-fichier 2 "conditions extérieures différentes" B1 "$T/c1" BRAVE_API_KEY=cle-factice
echo '{"cle_brave_presente": true}' > "$T/c1/A1/manifeste-run.json"
cas brave-differente-manifeste 2 "manifeste de A1" B1 "$T/c1"
echo '{"cle_brave_presente": false}' > "$T/c1/A1/manifeste-run.json"
# répétition B : même chemin, à partir de la répétition
cas repetition-B-avant 2 "sans génération 0 archivée" repetition-B "$T/c1"
mkdir -p "$T/c1/repetition/archive"; : > "$T/c1/.verrou-repetition"
echo '{"cle_brave_presente": false}' > "$T/c1/repetition/manifeste-run.json"; echo '{"lignee": "x", "generation": 0}' > "$T/c1/repetition/archive/index.jsonl"
echo "anthropic=RR_ANTHROPIC_API_KEY gemini=GEMINI_API_KEY brave=non" > "$T/c1/repetition.cles.txt"
cas sain-repetition-B 0 "contrôles : tout passe" repetition-B "$T/c1"
constat "répétition B : --depuis, sans entraînement, plafond 10" grep -qE "repetition-B : contrôles : tout passe.*--depuis <courses>/repetition.*--entrainements-max 0.*--plafond-total 10" "$T/c1/lancements.txt"
# portes (CE4-04 (2), CE4-08) : saines, puis altérée, puis d'un autre hôte, puis non réussie
H=$(cat "$T/c1/hote.txt")
for p in repetition repetition-B; do printf '{"course": "%s", "hote": "%s", "reussie": true, "raisons": []}\n' "$p" "$H" > "$T/c1/$p.porte.json"; done
printf '{"hote": "%s", "duree_s": 8100, "ecart_max_s": 61, "battements": 135}\n' "$H" > "$T/c1/epreuve-duree.json"
for f in repetition.porte.json repetition-B.porte.json epreuve-duree.json; do (cd "$T/c1" && sha256sum "$f" > "$f.sha256"); done
cas sain-portes 0 "contrôles : tout passe" A2 "$T/c1"
constat "trois portes passées" test "$(grep -c 'porte .* : passée' "$T/c1/lancements.txt")" -ge 3
mkdir -p -m 0700 "$T/c-p1"; cp "$T/c1/hote.txt" "$T/c-p1/"
printf '{"course": "repetition", "hote": "%s", "reussie": true}\n' "$H" > "$T/c-p1/repetition.porte.json"; echo "0000  repetition.porte.json" > "$T/c-p1/repetition.porte.json.sha256"
MODE=" " cas reel-porte-alteree 2 "porte repetition.porte.json : absente, altérée" A1 "$T/c-p1"
printf '{"course": "repetition", "hote": "ffffffffffffffff", "reussie": true}\n' > "$T/c-p1/repetition.porte.json"; (cd "$T/c-p1" && sha256sum repetition.porte.json > repetition.porte.json.sha256)
MODE=" " cas reel-porte-autre-hote 2 "porte repetition.porte.json : absente, altérée" A1 "$T/c-p1"
printf '{"course": "repetition", "hote": "%s", "reussie": false, "raisons": ["claude-opus-5-5 : amorçage REFUS"]}\n' "$H" > "$T/c-p1/repetition.porte.json"; (cd "$T/c-p1" && sha256sum repetition.porte.json > repetition.porte.json.sha256)
MODE=" " cas reel-porte-non-reussie 2 "porte repetition.porte.json : absente, altérée" A1 "$T/c-p1"
printf '{"course": "repetition", "hote": "%s", "reussie": true}\n' "$H" > "$T/c-p1/repetition.porte.json"; (cd "$T/c-p1" && sha256sum repetition.porte.json > repetition.porte.json.sha256)
printf '{"hote": "%s", "duree_s": 3600, "ecart_max_s": 61}\n' "$H" > "$T/c-p1/epreuve-duree.json"; (cd "$T/c-p1" && sha256sum epreuve-duree.json > epreuve-duree.json.sha256)
cp "$T/c1/repetition-B.porte.json" "$T/c1/repetition-B.porte.json.sha256" "$T/c-p1/"
MODE=" " cas reel-epreuve-courte 2 "porte epreuve-duree.json : absente, altérée" A1 "$T/c-p1"
# épreuve : déjà faite → refus (R12)
cas epreuve-deja-faite 2 "épreuve déjà faite ou en cours" epreuve "$T/c1"
# préenregistrement : non scellé, sans le commit, sans graines, occurrence double, vivier faux ou absent du commit
mv "$P.sha256" "$T/compagnon"
cas prereg-non-scelle 2 "préenregistrement non scellé" A1 "$T/c4"
mv "$T/compagnon" "$P.sha256"
prereg oui "0000000000000000000000000000000000000000" "$E_V"
cas prereg-sans-commit 2 "ne cite pas le commit" A1 "$T/c5"
prereg non "$COMMIT" "$E_V"
cas graine-absente 2 "graine_1 absente du préenregistrement" A1 "$T/c6"
prereg double "$COMMIT" "$E_V"
cas graine-en-double 2 "« graine_1 = … » y figure 2 fois" A1 "$T/c6"
prereg oui "$COMMIT" "$(printf 'c%.0s' $(seq 64))"
cas vivier-faux 2 "vivier : empreinte différente" A1 "$T/c7"
prereg oui "$COMMIT" "$E_V" donnees/essai/absent.json
cas vivier-absent-du-commit 2 "absent du commit" A1 "$T/c7b"
# question (R-393) : empreinte absente, en double, différente ; pièce absente du dépôt
prereg oui "$COMMIT" "$E_V" "" non
cas question-absente-du-prereg 2 "question_c001_sha256 absent du préenregistrement" A1 "$T/c7c"
prereg oui "$COMMIT" "$E_V" "" double
cas question-en-double 2 "« question_c001_sha256 = … » y figure 2 fois" A1 "$T/c7c"
prereg oui "$COMMIT" "$E_V" "" "$(printf 'd%.0s' $(seq 64))"
cas question-alteree 2 "d'empreinte différente de question_c001_sha256" A1 "$T/c7d"
prereg oui "$COMMIT" "$E_V"
mv "$D/docs/procedures/gradient-etape1-v5/$Q_NOM" "$T/question-garde.md"
cas question-piece-absente 2 "absente des entrées ou d'empreinte différente" A1 "$T/c7e"
mv "$T/question-garde.md" "$D/docs/procedures/gradient-etape1-v5/$Q_NOM"
# entrées altérées après extraction
cas sain-c8 0 "contrôles : tout passe" A1 "$T/c8"
f=$(ls "$T/c8/entrees/traits/etape1-v1/traits-16384/"*.npz | head -1); chmod u+w "$f"; printf 'x' >> "$f"
cas traits-alteres 2 "traits : un fichier diffère" A1 "$T/c8"
# extraction simultanée (CE4-07 f) : A1 et A2 ensemble sur un dossier neuf, trois fois
for k in 1 2 3; do
    mkdir -m 0700 "$T/c-sim$k"
    lancer A1 "$T/c-sim$k" > "$T/sortie-sim$k-A1.txt" 2>&1 & p1=$!
    lancer A2 "$T/c-sim$k" > "$T/sortie-sim$k-A2.txt" 2>&1 & p2=$!
    wait $p1; c1=$?; wait $p2; c2=$?
    verdict "extraction-simultanee-$k" "$c1$c2" 00 "2 courses passées" "$(grep -c 'contrôles : tout passe' "$T/c-sim$k/lancements.txt") courses passées"
done
# code : commit cité différent du code ; fichier non suivi dans le code (CE4-07 b)
prereg oui "0000000000000000000000000000000000000000" "$E_V"
cas code-autre-commit 2 "code : HEAD" A1 "$T/c9" COMMIT_ETAPE1=0000000000000000000000000000000000000000
prereg oui "$COMMIT" "$E_V"
echo "x = 1" > "$CODE/essaim-m3-refonte-v1/essaim_m3/noyau/non_suivi_essai.py"
cas code-fichier-non-suivi 2 "arbre de travail modifié ou fichier non suivi" A1 "$T/c9b"
rm "$CODE/essaim-m3-refonte-v1/essaim_m3/noyau/non_suivi_essai.py"
# GO refusés (registre sans GO-2026-10-24-05 ; sans GO-2026-10-24-07)
cp "$D/registres/go.md" "$T/go-garde.md"
grep -v "^| GO-2026-10-24-05 |" "$T/go-garde.md" > "$D/registres/go.md"
cas go-refuse-GO-2026-10-24-05 2 "garde de calcul : GO-2026-10-24-05 refusé" A1 "$T/c10-GO-2026-10-24-05"
# R-403 : les tests de dépense sont imputés à GO-05 ; un registre sans GO-07 (échu le 26 octobre) ne bloque plus rien
grep -v "^| GO-2026-10-24-07 |" "$T/go-garde.md" > "$D/registres/go.md"
cas go-07-absent-sans-effet 0 "contrôles : tout passe" A1 "$T/c10-GO-2026-10-24-07"
cp "$T/go-garde.md" "$D/registres/go.md"
# mode réel sans ligne d'engagement : arrêt avant tout appel
MODE=" " cas reel-sans-engagement 2 "aucune ligne « engagement : course A2" A2 "$T/c11"
# porte de la répétition (R-393) : le code Python de la porte, extrait tel quel du lanceur, sur des extraits factices
awk '/porte\.json\.neuf" <<.PY. \|\| true$/{f=1; next} f && /^PY$/{exit} f' "$L" > "$T/porte.py"
constat "porte extraite du lanceur" grep -qF 'if course == "repetition":' "$T/porte.py"
extrait() {  # $1 fichier ; $2 où la question est posée : c001 | c001+g000 | aucune ; $3 statut d'amorçage
    python3 -I -B - "$1" "$2" "${3:-ORGANISME_VALIDE}" <<'PY'
import json, sys
lignees = ["claude-fable-5-1", "claude-opus-5-5", "gemini-argon"]
ou = sys.argv[2]
gens, ev = [], [{"etape": "amorcage", "lignee": l, "statut": sys.argv[3]} for l in lignees]
for l in lignees:
    for phase, g in (("conception", 1), ("conception", 2), (None, 0)):
        e = {"lignee": l, "phase": phase, "generation": g, "statut": "OK", "invalide": False, "n_appels": 3,
             "services": {"entrainements": {"OK": 1}, "recherches": {"arxiv": {"OK": 1}}, "telechargements": {"OK": 1}},
             "appels": {"par_espece": {"CLAUDE_FABLE_5_1": {"n": 3, "par_statut": {"OK": 1, "TRONQUE": 2}}},
                        "max_tokens_demandes": {"4096": 3}}}
        e["appels"]["par_espece"]["CLAUDE_FABLE_5_1"]["reflexion_par_statut"] = {"TRONQUE": 2}
        nom = ("c" if phase else "g") + f"{g:03d}"
        if nom in ou.split("+"):
            e["question_ouverte"] = {"posee": True, "reponse": nom == "c001", "octets": 10, "sha256": "0" * 64, "probleme": None}
        gens.append(e)
json.dump({"evenements": ev, "generations": gens}, open(sys.argv[1], "w"))
PY
}
porte_essai() {  # $1 nom ; $2 extrait ; $3 course ; $4 attendu (true/false) ; $5 motif dans les raisons
    local r; r=$(python3 -I -B "$T/porte.py" "$2" "$3" 0 hote-essai CLAUDE_FABLE_5_1 CLAUDE_OPUS_5_5 GEMINI_ARGON 2>&1)
    verdict "$1" "$(printf '%s' "$r" | python3 -I -B -c 'import json,sys; print(str(json.load(sys.stdin)["reussie"]).lower())' 2>/dev/null)" "$4" "$5" "$r"
}
extrait "$T/extrait-c001.json" c001; extrait "$T/extrait-c001-g000.json" c001+g000; extrait "$T/extrait-aucune.json" aucune
extrait "$T/extrait-B.json" aucune ORGANISME_IMPOSE_VALIDE
porte_essai porte-question-c001-saine "$T/extrait-c001.json" repetition true '"reponse_question_c001": true'
porte_essai porte-appels-par-espece-rapportes "$T/extrait-c001.json" repetition true '"appels_par_espece": {"CLAUDE_FABLE_5_1": {"OK": 9, "TRONQUE": 18}}, "max_tokens_demandes": {"4096": 27}, "reflexion_par_espece": {"CLAUDE_FABLE_5_1": {"TRONQUE": 18}}'
porte_essai porte-question-aussi-a-g000 "$T/extrait-c001-g000.json" repetition false "question posée à [('', 0), ('conception', 1)]"
porte_essai porte-question-non-posee "$T/extrait-aucune.json" repetition false "claude-fable-5-1 : question posée à [] (attendu : c001 seulement)"
porte_essai porte-repetition-B-sans-condition-de-question "$T/extrait-B.json" repetition-B true '"reussie": true'
git -C "$GC" worktree remove --force "$CODE"
echo "bilan : $N_OK réussis, $N_KO en échec"
[ "$N_KO" = 0 ]
