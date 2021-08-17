
print('Question 7 Python Script method-spot-generator.py running........')

import json
import csv
import math
import pandas as pd

with open("./Input_Files/cases.json", "r") as read_file:
    cases=json.load(read_file)

#======================================   Writing csv output for Question7  ==================================

#-------------- Finding Hotspots/Coldspots Weekly---------------------
df=pd.read_csv("./Question6/zscore-week.csv")
zscore_record=df.to_dict('records')
with open('./Question7/method-spot-week.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['WeekID','Method','Spot','DistrictID' ])
    for x in zscore_record:
        if x['NeighborhoodZscore']>1:
            csv_writer.writerow([x['WeekID'],'Neighborhood','Hot',x['DistrictID']])
        if x['NeighborhoodZscore']<-1:
            csv_writer.writerow([x['WeekID'],'Neighborhood','Cold',x['DistrictID']])
        if x['StateZscore']>1:
            csv_writer.writerow([x['WeekID'],'State','Hot',x['DistrictID']])
        if x['StateZscore']<-1:
            csv_writer.writerow([x['WeekID'],'State','Cold',x['DistrictID']])
        
#-------------- Finding Hotspots/Coldspots Monthly---------------------
df=pd.read_csv("./Question6/zscore-month.csv")
zscore_record=df.to_dict('records')
with open('./Question7/method-spot-month.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['MonthID','Method','Spot','DistrictID'])
    for x in zscore_record:
        if x['NeighborhoodZscore']>1:
            csv_writer.writerow([x['MonthID'],'Neighborhood','Hot',x['DistrictID']])
        if x['NeighborhoodZscore']<-1:
            csv_writer.writerow([x['MonthID'],'Neighborhood','Cold',x['DistrictID']])
        if x['StateZscore']>1:
            csv_writer.writerow([x['MonthID'],'State','Hot',x['DistrictID']])
        if x['StateZscore']<-1:
            csv_writer.writerow([x['MonthID'],'State','Cold',x['DistrictID']])


#-------------- Finding Hotspots/Coldspots Overall---------------------
df=pd.read_csv("./Question6/zscore-overall.csv")
zscore_record=df.to_dict('records')
with open('./Question7/method-spot-overall.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['OverallID','Method','Spot','DistrictID' ])
    for x in zscore_record:
        if x['NeighborhoodZscore']>1:
            csv_writer.writerow([x['OverallID'],'Neighborhood','Hot',x['DistrictID']])
        if x['NeighborhoodZscore']<-1:
            csv_writer.writerow([x['OverallID'],'Neighborhood','Cold',x['DistrictID']])
        if x['StateZscore']>1:
            csv_writer.writerow([x['OverallID'],'State','Hot',x['DistrictID']])
        if x['StateZscore']<-1:
            csv_writer.writerow([x['OverallID'],'State','Cold',x['DistrictID']])

#======================================   Writing csv output for Question7  ==================================

print('Output files method-spot-week.csv  method-spot-month.csv  method-spot-overall.csv produced in Folder Question7')
