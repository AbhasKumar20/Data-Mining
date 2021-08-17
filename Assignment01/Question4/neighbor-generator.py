
print('Question 4 Python Script neighbor-generator.py running........')

import json
import csv
import math

with open("./Input_Files/cases.json", "r") as read_file:
    cases=json.load(read_file)

#=========================================   Writing csv output for Question4    ==================================

with open('./Question4/neighbor-week.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'WeekID', 'Neighbormean', 'Neighborstdev'])
    for x in cases:
        for i in range(1,26):
            total_cases=0
            for y in cases[x]['neighbors']:
                total_cases+=cases[y]['weeks'][str(i)]-cases[y]['weeks'][str(i-1)]
            mean=total_cases/len(cases[x]['neighbors'])
            sum=0
            for y in cases[x]['neighbors']:
                sum+=(((cases[y]['weeks'][str(i)]-cases[y]['weeks'][str(i-1)])-mean)**2)
            sd=math.sqrt(sum/len(cases[x]['neighbors']))
            csv_writer.writerow([cases[x]['districtid'],i,round(mean,2),round(sd,2)])

with open('./Question4/neighbor-month.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictId', 'MonthID', 'Neighbormean', 'Neighborstdev'])
    for x in cases:
        for i in range(1,8):
            total_cases=0
            sum=0
            if i==1:
                for y in cases[x]['neighbors']:
                    total_cases+=(cases[y]['months'][str(i)]-cases[y]['weeks']['0'])
                mean=total_cases/len(cases[x]['neighbors'])
                
                for y in cases[x]['neighbors']:
                    sum+=(((cases[y]['months'][str(i)]-cases[y]['weeks']['0'])-mean)**2)
                sd=math.sqrt(sum/len(cases[x]['neighbors']))
                csv_writer.writerow([cases[x]['districtid'],i,round(mean,2),round(sd,2)])
            else:
                for y in cases[x]['neighbors']:
                    total_cases+=cases[y]['months'][str(i)]-cases[y]['months'][str(i-1)]
                mean=total_cases/len(cases[x]['neighbors'])
                for y in cases[x]['neighbors']:
                    sum+=(((cases[y]['months'][str(i)]-cases[y]['months'][str(i-1)])-mean)**2)
                sd=math.sqrt(sum/len(cases[x]['neighbors']))
                csv_writer.writerow([cases[x]['districtid'],i,round(mean,2),round(sd,2)])

with open('./Question4/neighbor-overall.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'OverallID', 'Neighbormean', 'Neighborstdev'])
    for x in cases:
            total_cases=0
            for y in cases[x]['neighbors']:
                total_cases+=cases[y]['year']['1']
            mean=total_cases/len(cases[x]['neighbors'])
            sum=0
            for y in cases[x]['neighbors']:
                sum+=(((cases[y]['year']['1'])-mean)**2)
            sd=math.sqrt(sum/len(cases[x]['neighbors']))
            csv_writer.writerow([cases[x]['districtid'],1,round(mean,2),round(sd,2)])

#=========================================   Writing csv output for Question4  Ends     ==================================

print('Output files neighbor-week.csv  neighbor-month.csv  neighbor-overall.csv produced in Folder Question4')
