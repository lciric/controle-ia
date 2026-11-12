import json, runpy
LOI = '{"biais":[0.0,0.0,0.0],"poids":[[-0.76202,0.0],[-1.954237,0.0],[-0.572456,0.0]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
