import json
print json.dumps({'9': 5, '6': 7}, sort_keys=True,indent=4, separators=(',', ': '))
