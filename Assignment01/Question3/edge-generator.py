
print('Question 3 Python Script edge-generator.py running......')
import json
import csv
with open("./Input_Files/cases.json", "r") as read_file:
    cases=json.load(read_file)
#=========================================   Writing csv output for Question3       ==================================

with open('./Question3/edge-graph.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID','NeighborID'])
    for x in cases:
        for y in cases[x]['neighbors']:
            csv_writer.writerow([cases[x]['districtid'],cases[y]['districtid']])

#=========================================   Writing csv output for Question3  Ends     ==================================

print('Output file edge-graph.csv produced in Folder Question3')
