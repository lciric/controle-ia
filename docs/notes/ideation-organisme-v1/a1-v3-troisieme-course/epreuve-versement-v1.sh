#!/usr/bin/env bash
# Épreuve du versement « partie de main » du lanceur durable d'A1-v3 (`MachineV2.verser`, `MachineV3.verser`), à jouer par la
# mère depuis sa session, contre GitHub. Même suite git que la machine : la branche ne doit pas exister (R12) ; clone superficiel,
# partiel et clairsemé de `main` (`--depth 1 --filter=blob:none --sparse --single-branch --branch main`) ; `sparse-checkout` du seul
# dossier versé ; branche neuve ; un fichier ; commit ; poussée ; vérification par `ls-remote`. Branche jetable :
# `essai/a1-v3-versement-epreuve-v1` (le dossier versé porte son nom, comme sur la machine). Aucun jeton dans la commande : l'accès
# vient du mandataire de la session. Rien n'est supprimé par ce script : la branche jetable reste, à supprimer ensuite par la mère
# si elle le décide (`git push https://github.com/lciric/controle-ia-travail.git --delete essai/a1-v3-versement-epreuve-v1`).
# Usage : bash epreuve-versement-v1.sh [DOSSIER_NEUF]   (défaut : /tmp/epreuve-versement-a1-v3-v1, qui ne doit pas exister)
# Codes : 0 épreuve réussie (poussée vérifiée par ls-remote, branche partie de main) ; 2 échec, avec l'étape.
set -uo pipefail
URL="${URL_EPREUVE:-https://github.com/lciric/controle-ia-travail.git}"  # le dépôt de travail ; essai local : file://…
case "$URL" in https://github.com/lciric/controle-ia-travail.git|file:///*) ;;
    *) echo "adresse $URL refusée : le dépôt de travail seul (jamais lciric/controle-ia, copie expurgée publique)"; exit 2;; esac
BRANCHE="essai/a1-v3-versement-epreuve-v1"
V="${1:-/tmp/epreuve-versement-a1-v3-v1}"
DELAI=240                                                  # comme DELAI_GIT_S du lanceur (v2, v3)
etape() { echo "$(date -u +%FT%TZ) $*"; }
echec() { etape "ÉCHEC : $*"; exit 2; }
[ -e "$V" ] && echec "$V existe déjà (R12) : donner un dossier neuf"
etape "épreuve du versement « partie de main » : $URL ; branche $BRANCHE ; copie $V ; $(git --version)"
DISTANT=$(timeout -k 5 $DELAI git ls-remote "$URL" "refs/heads/$BRANCHE") || echec "ls-remote initial (code $?)"
[ -z "$DISTANT" ] || echec "branche $BRANCHE déjà présente (R12) : rien n'est écrasé"
MAIN=$(timeout -k 5 $DELAI git ls-remote "$URL" refs/heads/main | cut -f1) || echec "ls-remote de main (code $?)"
t0=$(date +%s)
timeout -k 5 $DELAI git clone -q --depth 1 --filter=blob:none --sparse --single-branch --branch main "$URL" "$V" \
    || echec "clone superficiel, partiel et clairsemé (code $?)"
etape "clone en $(( $(date +%s) - t0 )) s ; $(du -sk "$V" | cut -f1) Ko sur le disque ; tête $(git -C "$V" rev-parse HEAD) ; main distant $MAIN"
timeout -k 5 $DELAI git -C "$V" sparse-checkout set "$BRANCHE" || echec "sparse-checkout set (code $?)"
git -C "$V" checkout -q -b "$BRANCHE" || echec "checkout -b (code $?)"
mkdir -p "$V/$BRANCHE" || echec "dossier versé"
printf 'Épreuve du versement du lanceur durable d A1-v3 (branche jetable), %s\n' "$(date -u +%FT%TZ)" > "$V/$BRANCHE/epreuve.txt"
git -C "$V" add -f "$BRANCHE" || echec "add (code $?)"
git -C "$V" -c user.name=epreuve-versement-a1-v3 -c user.email=epreuve@invalid commit -q \
    -m "Épreuve du versement « partie de main » du lanceur durable d'A1-v3 (branche jetable)" || echec "commit (code $?)"
LOCAL=$(git -C "$V" rev-parse HEAD); PARENT=$(git -C "$V" rev-parse HEAD^)
etape "commit $LOCAL ; parent $PARENT ; fichiers du commit : $(git -C "$V" show --stat --format= HEAD | tail -1)"
t1=$(date +%s)
timeout -k 5 $DELAI git -C "$V" push -q "$URL" "HEAD:refs/heads/$BRANCHE" || echec "poussée (code $?)"
VU=$(timeout -k 5 $DELAI git ls-remote "$URL" "refs/heads/$BRANCHE" | cut -f1) || echec "ls-remote final (code $?)"
etape "poussée en $(( $(date +%s) - t1 )) s ; local $LOCAL ; distant ${VU:-absent}"
[ "$VU" = "$LOCAL" ] || echec "poussée non vérifiée par ls-remote"
[ "$PARENT" = "$MAIN" ] || etape "note : main a bougé entre le ls-remote et le clone (parent $PARENT, main lu $MAIN)"
etape "ÉPREUVE RÉUSSIE : $BRANCHE = $LOCAL, partie de main ($PARENT), vérifiée par ls-remote ; copie gardée dans $V"
