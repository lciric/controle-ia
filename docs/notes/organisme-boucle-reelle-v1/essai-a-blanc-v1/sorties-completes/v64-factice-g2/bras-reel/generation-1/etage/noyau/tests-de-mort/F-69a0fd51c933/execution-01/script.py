import json, runpy
LOI = '{"biais":[0.322783,0.440009,0.460976],"poids":[[0.214517,-1.24113],[-0.207753,3.494381],[-0.116416,-4.0]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
