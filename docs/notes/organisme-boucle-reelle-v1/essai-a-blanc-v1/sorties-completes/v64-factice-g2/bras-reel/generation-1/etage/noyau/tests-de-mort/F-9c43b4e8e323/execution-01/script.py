import json, runpy
LOI = '{"biais":[0.102458,0.282748,-0.522896],"poids":[[0.291356,-0.186537],[-2.130803,3.028271],[0.603575,-3.276739]],"type":"softmax"}'
ev = runpy.run_path('tranche/evaluateur_lois_v62.py')
ev['ecrire_gains'](json.loads(LOI), 'tranche/episodes.csv', 'gains.csv')
