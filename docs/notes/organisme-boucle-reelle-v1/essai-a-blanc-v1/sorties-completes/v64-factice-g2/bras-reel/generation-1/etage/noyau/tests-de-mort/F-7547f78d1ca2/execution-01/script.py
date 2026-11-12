import json, runpy
LOI = '{"biais":[0.217954,0.456985,-0.102374],"poids":[[0.478642,-0.235238],[-1.248704,3.099517],[0.962139,-2.257039]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
