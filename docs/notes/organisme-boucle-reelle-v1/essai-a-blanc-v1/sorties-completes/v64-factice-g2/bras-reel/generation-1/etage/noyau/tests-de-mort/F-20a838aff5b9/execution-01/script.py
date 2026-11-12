import json, runpy
LOI = '{"biais":[0.001407,0.530889,-0.33282],"poids":[[0.521358,-0.474152],[-0.894592,3.279566],[0.985158,-2.744106]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
