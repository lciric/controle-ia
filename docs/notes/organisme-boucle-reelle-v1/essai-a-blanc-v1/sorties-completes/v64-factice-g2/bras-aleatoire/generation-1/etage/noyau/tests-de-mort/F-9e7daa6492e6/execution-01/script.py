import json, runpy
LOI = '{"biais":[0.0,0.0,0.0],"poids":[[0.074841,-2.453587],[-0.554428,-0.469738],[-0.178949,-2.014562]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
