import json, runpy
LOI = '{"biais":[0.291533,-0.071947,0.234424],"poids":[[-1.188405,-1.530944],[-2.333854,2.943803],[2.256413,-3.584806]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
