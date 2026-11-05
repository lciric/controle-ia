#!/usr/bin/env bash
# Sonde d'hôte de l'étape 1 (session-depot, 24 octobre 2026, GO-2026-10-24-07) : capacités du conteneur pour l'isolation du
# noyau (unshare -n ; espaces de noms de montage et de processus), ressources, accès réseau sortant. Aucune clé, aucun jeton.
echo "SONDE debut $(date -u +%FT%TZ)"
echo "SONDE id $(id)"
echo "SONDE noyau $(uname -r)"
grep -E '^(CapEff|CapBnd|Seccomp|NoNewPrivs)' /proc/self/status | sed 's/^/SONDE status /'
for o in "-n" "--mount --pid --fork --kill-child --mount-proc" "-rn" "-U"; do
    if unshare $o true 2>/tmp/e; then echo "SONDE unshare $o : OK"; else echo "SONDE unshare $o : KO $(head -c 160 /tmp/e | tr '\n' ' ')"; fi
done
echo "SONDE ressources nproc $(nproc) ; memoire $(free -g | awk '/Mem/{print $2}') Go ; disque libre $(df -h / | awk 'NR==2{print $4}')"
echo "SONDE python $(python3 --version 2>&1) ; unshare $(unshare --version 2>&1 | head -1)"
echo "SONDE fs protected_hardlinks=$(cat /proc/sys/fs/protected_hardlinks 2>&1) protected_symlinks=$(cat /proc/sys/fs/protected_symlinks 2>&1) max_user_namespaces=$(cat /proc/sys/user/max_user_namespaces 2>&1)"
for u in https://api.anthropic.com/v1/models https://generativelanguage.googleapis.com/ https://github.com/ https://export.arxiv.org/; do
    echo "SONDE reseau $u $(curl -s -o /dev/null -w '%{http_code}' --max-time 10 "$u" 2>&1)"
done
python3 - <<'PY' 2>&1 | sed 's/^/SONDE /'
import os
pid = os.fork()
if pid == 0:
    try:
        os.setgroups([]); os.setgid(60001); os.setuid(60001)
        print("abaissement setuid OK, uid", os.getuid())
    except Exception as e:
        print("abaissement setuid KO", type(e).__name__, e)
    os._exit(0)
os.waitpid(pid, 0)
PY
echo "SONDE fin $(date -u +%FT%TZ)"
sleep 1500
