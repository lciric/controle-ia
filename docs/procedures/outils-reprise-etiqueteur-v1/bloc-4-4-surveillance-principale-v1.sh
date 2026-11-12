set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
D="$PRINC"; P=$(cat "$CONSOLES/lecture-principale.pid"); kill -0 "$P" 2>/dev/null && echo "processus $P actif" || echo "processus $P fini"
"$PY" -I -c "
import json,sys,collections
d=sys.argv[1]
for L in 'AB':
    st=collections.Counter(); n=0; c=0.0
    for nom in (f'reponses-phase1-{L}-v4.encours.jsonl',):
        try:
            for x in open(f'{d}/{nom}',encoding='utf-8'):
                if x.strip(): r=json.loads(x); st[(r.get('lecture'), r.get('statut'))]+=1
        except FileNotFoundError: pass
    try:
        for x in open(f'{d}/journal-phase1-{L}-v4.jsonl',encoding='utf-8'):
            if x.strip(): r=json.loads(x); n+=1; c+=float(r.get('cout_estime') or 0)
    except FileNotFoundError: pass
    print(L, dict(st), 'tentatives', n, 'cout_estime_dollars', round(c,4))
" "$D"
