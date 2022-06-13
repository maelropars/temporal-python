import sys
import json
from datetime import datetime


bigtotal = 0;
if (len(sys.argv) > 1):
  cpt = 1

filename = sys.argv[1]
print("############# Parsing " + filename )

with open(filename, 'r') as f:
  data = json.load(f)
  fields = data['series'][1]['fields']
  quantity = len(fields[0]['values'])
  cpt = 0
  sumall = 0
  while (cpt < quantity):
    dt_object = str(datetime.fromtimestamp(fields[0]['values'][cpt] / 1000))
    #dt_object = str(fields[0]['values'][cpt])
    val = fields[1]['values'][cpt]
    if (val is not None):
      sumall += val
    print(str(cpt+1) + " " + dt_object + " : " + str(val))
    cpt += 1
  print ("total : " + str(sumall))
