#!/usr/bin/env bash
# Pose le fichier de clé de l'utilisateur distinct « argon » (marche à suivre du lancement de l'idéation, étape 6.2 ; mot
# direct de Lazar du 29 octobre 2026, ≈ 10:15 UTC : « (a) sur les deux : go »). La clé vient de la variable
# GEMINI_API_KEY_2 de la session ; elle n'est jamais affichée, jamais passée en argument, jamais écrite ailleurs que dans
# /home/argon/.cle-gemini (600, argon:argon). Aucune valeur de clé dans ce fichier. Usage : bash scripts/poser_cle_argon_v1.sh
set -euo pipefail
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
id argon >/dev/null 2>&1 || { echo "utilisateur argon absent" >&2; exit 2; }
[ ! -e /home/argon/.cle-gemini ] || { echo "/home/argon/.cle-gemini existe déjà (R12 : on n'écrase pas)" >&2; exit 2; }
( umask 077; printf '%s\n' "$GEMINI_API_KEY_2" > /home/argon/.cle-gemini )
chown argon:argon /home/argon/.cle-gemini; chmod 600 /home/argon/.cle-gemini
printf 'clé posée : %s octets, droits %s\n' "$(stat -c %s /home/argon/.cle-gemini)" "$(stat -c '%A %U:%G' /home/argon/.cle-gemini)"
