#!/bin/sh
# lancer-question-argon-v1.sh — pose la question « classes de déplacements de loi et statistiques ripostes » (v1) à
# Argon seul (gemini-4-argon), par l'enveloppe d'utilisateur distinct /opt/argon/appel-argon-v3.sh et la commande v2.
#
# CE FICHIER NE LANCE RIEN PAR LUI-MÊME : il est écrit par un sous-agent sans réseau ni droit de lancement. C'est la
# session qui l'exécutera, sous le GO-2026-10-29-14 (registres/go.md, plafond 6 USD, échéance 2026-11-05), en root
# (setpriv exige root), depuis une machine où l'enveloppe et le relais Gemini local sont installés. La sortie va dans un
# dossier en 700 hors du dépôt ; elle sera versée sur une branche en quarantaine et lue par un sous-agent tenu à l'écart
# de la conception des moniteurs ; rien n'en est servi à l'orchestrateur ni aux juges.
#
# Garde de pire cas (commande_argon_v2.py, avant tout envoi) : entrée gardée × 8,3 + (maxOutputTokens + provision de
# pensée 8 192) × 41,5, par million de jetons, ≤ PLAFOND_SESSION_USD. Avec la question scellée (7 783 caractères, donc
# 1 946 jetons estimés, 2 044 gardés avec la marge de 5 % ; pour ≈ 6 000 caractères : 1 575 gardés) et
# --max-sortie-jetons 32000 : 2 044 × 8,3 / 10^6 ≈ 0,017 USD + (32 000 + 8 192) × 41,5 / 10^6 ≈ 1,668 USD, soit
# ≈ 1,685 USD < 6 USD (1,681 USD pour 6 000 caractères). Le plafond paierait jusqu'à 136 071 jetons de sortie après
# provision : les 32 000 demandés sont servis en entier, sans réduction par la garde. --sortie-min-jetons garde son
# défaut (4 096). Si countTokens comptait trois fois l'estimation, le pire cas resterait ≈ 1,71 USD.
#
# Ce que fait le script : (1) vérifie l'empreinte de la question (constante ci-dessous ET fichier compagnon) ; (2) crée
# SORTIE en 700 et refuse d'écraser une sortie existante (R12) ; (3) écrit l'heure UTC de début, le GO, l'empreinte et
# la ligne de commande dans SORTIE/lancement.txt ; (4) envoie la question par la ligne convenue ; (5) écrit l'heure UTC
# de fin et le code de retour ; (6) scelle les trois fichiers de sortie (empreinte compagnon au nom nu, format
# sha256sum) ; (7) rend le code de retour de la commande (0 attendu ; 2 à 7 selon commande_argon_v2.py).
set -eu
umask 077

ICI=$(cd "$(dirname "$0")" && pwd)
QUESTION=question-argon-classes-ecart-v1.md
EMPREINTE_ATTENDUE=f13fa32a415f4f16572b63d9dcb2d9535c7d277e7ef8e66647ae6c1e89a49541
SORTIE=/root/ideation-v1/argon-classes-ecart-v1
GO_ID=GO-2026-10-29-14
export GO_ID

cd "$ICI"

# (1) empreinte de la question : constante du script, puis fichier compagnon
EMPREINTE=$(sha256sum "$QUESTION" | cut -d' ' -f1)
[ "$EMPREINTE" = "$EMPREINTE_ATTENDUE" ] || { echo "empreinte de $QUESTION inattendue : $EMPREINTE" >&2; exit 10; }
sha256sum -c --quiet "$QUESTION.sha256" || { echo "compagnon $QUESTION.sha256 non conforme" >&2; exit 10; }

# (2) dossier de sortie en 700, aucune réécriture
[ "$(id -u)" = 0 ] || { echo "setpriv exige root" >&2; exit 11; }
mkdir -p "$SORTIE"
chmod 700 "$SORTIE"
for f in reponse-argon-v1.json reponse-argon-v1.err lancement.txt; do
    [ ! -e "$SORTIE/$f" ] || { echo "$SORTIE/$f existe déjà : nouvelle version = nouveau nom (R12)" >&2; exit 12; }
done

# (3) journal de lancement
{
    echo "go: $GO_ID"
    echo "question: $ICI/$QUESTION"
    echo "empreinte_question: $EMPREINTE"
    echo "commande: printf '%s' \"\$(cat $QUESTION)\" | PLAFOND_SESSION_USD=6 ROLE_POLE=proposeur_ideation /usr/bin/timeout 1900 /usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v3.sh --max-sortie-jetons 32000"
    echo "debut_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$SORTIE/lancement.txt"

# (4) envoi : ligne convenue, seuls les chemins de sortie changent
code=0
printf '%s' "$(cat question-argon-classes-ecart-v1.md)" | PLAFOND_SESSION_USD=6 ROLE_POLE=proposeur_ideation /usr/bin/timeout 1900 /usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v3.sh --max-sortie-jetons 32000 > "$SORTIE/reponse-argon-v1.json" 2> "$SORTIE/reponse-argon-v1.err" || code=$?

# (5) fin
{
    echo "fin_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "code_retour: $code"
} >> "$SORTIE/lancement.txt"

# (6) scellement des sorties (compagnon au nom nu, format sha256sum)
cd "$SORTIE"
for f in reponse-argon-v1.json reponse-argon-v1.err lancement.txt; do
    sha256sum "$f" > "$f.sha256"
done
chmod 600 reponse-argon-v1.json reponse-argon-v1.err lancement.txt ./*.sha256

echo "fini : code $code ; sorties dans $SORTIE" >&2
exit "$code"
