set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
timeout 20 bash -c 'until curl -sS --noproxy "*" --max-time 2 -o /dev/null "$1" 2>/dev/null; do sleep 0.5; done' _ "http://127.0.0.1:$PORT_RELAIS/relais/etat" || echo "ARRET : relais muet après 20 secondes"
curl -sS --noproxy '*' --max-time 10 "http://127.0.0.1:$PORT_RELAIS/relais/etat" > "$RELAIS_P/etat-avant-v1.json"
"$PY" -I -c "
import json,sys
e=json.load(open(sys.argv[1])); p=open(sys.argv[2]).read().strip()
garde=('version','pid','modeles_permis','plafond_usd','reserve_par_appel_usd','max_appels','appels','depense_usd','prix_entree_usd_par_million','prix_sortie_usd_par_million','prix_cache_usd_par_million','recherche_officielle')
print({k:v for k,v in e.items() if k in garde or 'cle' in k or 'env' in k})
print('numero de processus conforme' if str(e.get('pid'))==p else 'ARRET : numero de processus different')
" "$RELAIS_P/etat-avant-v1.json" "$RELAIS_P/relais.pid"
