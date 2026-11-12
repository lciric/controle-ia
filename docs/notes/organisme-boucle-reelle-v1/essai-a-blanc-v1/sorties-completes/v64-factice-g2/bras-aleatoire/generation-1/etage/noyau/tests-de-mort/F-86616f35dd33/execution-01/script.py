import json, runpy
LOI = '{"biais":[0.0,0.0,0.0],"poids":[[0.0,0.408011],[0.0,0.964426],[0.0,-0.073672]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
