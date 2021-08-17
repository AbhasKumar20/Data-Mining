
print('Question 5 Python Script state-generator.py running........')

import json
import csv
import math


with open("./Input_Files/cases.json", "r") as read_file:
    cases=json.load(read_file)

#=========================================   Writing csv output for Question5    ==================================
with open('./Question5/state-week.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'WeekID', 'Statemean', 'Statestdev'])
    for x in cases:
        for i in range(1,26):
            total_cases=0
            sum=0
            count=0
            if cases[x]['stateid']=='Delhi' or cases[x]['stateid']=='Chandigarh':
                mean=cases[x]['weeks'][str(i)]-cases[x]['weeks'][str(i-1)]
                sd=0
            else:
                for y in cases:
                    if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                        total_cases+=cases[y]['weeks'][str(i)]-cases[y]['weeks'][str(i-1)]
                        count+=1
                mean=total_cases/count
                for y in cases:
                    if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                        sum+=(((cases[y]['weeks'][str(i)]-cases[y]['weeks'][str(i-1)])-mean)**2)
                        sd=math.sqrt(sum/count)
            csv_writer.writerow([cases[x]['districtid'],i,round(mean,2),round(sd,2)])


with open('./Question5/state-month.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'MonthID', 'Statemean', 'Statestdev'])
    for x in cases:
        for i in range(1,8):
            total_cases=0
            sum=0
            count=0
            if i==1:
                if cases[x]['stateid']=='Delhi' or cases[x]['stateid']=='Chandigarh':
                    mean=cases[x]['months'][str(i)]-cases[x]['weeks'][str(i-1)]
                    sd=0
                else:
                    for y in cases:
                        if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                            total_cases+=cases[y]['months'][str(i)]-cases[y]['weeks'][str(i-1)]
                            count+=1
                    mean=total_cases/count
                    for y in cases:
                        if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                            sum+=(((cases[y]['months'][str(i)]-cases[y]['weeks'][str(i-1)])-mean)**2)
                            sd=math.sqrt(sum/count)
                csv_writer.writerow([cases[x]['districtid'],i,round(mean,2),round(sd,2)])
            else:
                if cases[x]['stateid']=='Delhi' or cases[x]['stateid']=='Chandigarh':
                    mean=cases[x]['months'][str(i)]-cases[x]['months'][str(i-1)]
                    sd=0
                else:
                    for y in cases:
                        if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                            total_cases+=cases[y]['months'][str(i)]-cases[y]['months'][str(i-1)]
                            count+=1
                    mean=total_cases/count
                    for y in cases:
                        if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                            sum+=(((cases[y]['months'][str(i)]-cases[y]['months'][str(i-1)])-mean)**2)
                            sd=math.sqrt(sum/count)
                csv_writer.writerow([cases[x]['districtid'],i,round(mean,2),round(sd,2)])
                
with open('./Question5/state-overall.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'OverallID', 'Statemean', 'Statestdev'])
    for x in cases:
        total_cases=0
        sum=0
        count=0
        if cases[x]['stateid']=='Delhi' or cases[x]['stateid']=='Chandigarh':
            mean=cases[x]['year']['1']
            sd=0
        else:
            for y in cases:
                if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                    total_cases+=cases[y]['year']['1']
                    count+=1
            mean=total_cases/count
            for y in cases:
                if (cases[y]['stateid']==cases[x]['stateid']) and x!=y:
                    sum+=(((cases[y]['year']['1'])-mean)**2)
                    sd=math.sqrt(sum/count)
        csv_writer.writerow([cases[x]['districtid'],1,round(mean,2),round(sd,2)])


#=========================================   Writing csv output for Question5 Ends    ==================================

print('Output files state-week.csv  state-month.csv  state-overall.csv produced in Folder Question5')
