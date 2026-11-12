set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
date -u; echo "code de fin de la lecture : $(cat "$CONSOLES/code-lecture-principale-v1.txt")"
curl -sS --noproxy '*' --max-time 10 "http://127.0.0.1:$PORT_RELAIS/relais/etat" > "$RELAIS_P/etat-apres-v1.json"
"$PY" -I -c "
import json,sys
e=json.load(open(sys.argv[1]))
print({k:e.get(k) for k in ('pid','appels','depense_usd','engage_usd','restant_usd','refus','refus_modele','ecarts_modele_servi','usages_absents','delais_depasses','appels_au_dessus_de_la_reserve','reponses_par_statut')})
" "$RELAIS_P/etat-apres-v1.json"
P=$(cat "$RELAIS_P/relais.pid"); test "$("$PY" -I -c "import json,sys; print(json.load(open(sys.argv[1]))['pid'])" "$RELAIS_P/etat-apres-v1.json")" = "$P" && kill "$P"
timeout 30 tail --pid="$P" -f /dev/null; kill -0 "$P" 2>/dev/null && echo "ARRET : relais $P toujours vivant" || echo "relais $P arrêté"
"$PY" -I -c "
import json,sys
m=json.load(open(sys.argv[1]))
cf=m.get('controle_format') or {}
print('code', m.get('code_de_sortie'), 'arret', m.get('arret'), 'lecteurs_arretes', m.get('lecteurs_arretes'))
print('comptes', json.dumps(m.get('comptes')))
print('feu_vert', cf.get('feu_vert'), 'motifs', cf.get('motifs'), 'extrapolation_dollars', cf.get('extrapolation_dollars'), 'plafond_restant_dollars', cf.get('plafond_restant_dollars'))
print('par_lecteur', json.dumps(cf.get('par_lecteur')))
print('depense_estimee_dollars', repr(m.get('depense_estimee_dollars')), 'reserve_restante_dollars', m.get('reserve_restante_dollars'), 'tentatives_interrompues', m.get('tentatives_interrompues_comptees_au_pire'))
print('empreinte_reglages', m.get('empreinte_reglages'), 'relais_max_appels', m.get('relais_max_appels'), 'commit', m.get('commit'))
print('sorties', json.dumps(m.get('sorties')))
" "$PRINC/manifeste-lecture-phase1-v4.json"
sha256sum "$PRINC"/* "$RELAIS_P"/* | tee "$CR/empreintes-lecture-principale-v1.txt"
