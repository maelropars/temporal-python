import sys
import json

bigtotal = 0;
if (len(sys.argv) > 1):
  cpt = 1

  while (cpt < len(sys.argv)) :
      filename = sys.argv[cpt]
      print("############# Parsing " + filename )

      with open(filename, 'r') as f:
        data = json.load(f)

      # Output: {'name': 'Bob', 'languages': ['English', 'French']}
      #print(json.dumps(data, indent=4, sort_keys=True))

      countedList = []
      ignoredList = []
      for i in data:
        if (i['eventType'].endswith('STARTED')):
          countedList.append(i['eventType'])
        else:
          ignoredList.append(i['eventType'])
      print("")
      #for j in data:
      #  print(j['eventId'] + " " +j['eventType'])
      #print(countedList)
      #print("")
      #print(ignoredList)
      #print("")
      bigtotal += len(countedList)
      print("total number of activities : " + str(len(countedList)))
      print("total number of ignored events : " + str(len(ignoredList)))
      cpt += 1
print("total for all files : " + str(bigtotal))