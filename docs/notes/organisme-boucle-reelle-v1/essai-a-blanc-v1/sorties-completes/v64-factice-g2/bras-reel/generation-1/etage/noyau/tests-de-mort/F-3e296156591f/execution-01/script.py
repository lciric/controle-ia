import json, runpy
LOI = '{"biais":[0.193545,0.803919,-0.712358],"poids":[[0.607401,0.060074],[-1.118315,3.57873],[1.472229,-2.832305]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
