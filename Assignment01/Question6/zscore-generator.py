
print('Question 6 Python Script zscore-generator.py running........')

import json
import csv
import math
import pandas as pd

with open("./Input_Files/cases.json", "r") as read_file:
    cases=json.load(read_file)

#======================================== Writing csv output for Question6 ================================

#========================== Calculation of Z-scores for Weeks====================
df= pd.read_csv("./Question2/cases-week.csv")
cases_record=df.to_dict('records')
df= pd.read_csv("./Question4/neighbor-week.csv")
neighbor_record=df.to_dict('records')
df= pd.read_csv("./Question5/state-week.csv")
state_record=df.to_dict('records')



with open('./Question6/zscore-week.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'WeekID', 'NeighborhoodZscore', 'StateZscore'])
    for x,y,z in zip(cases_record,neighbor_record,state_record):
        if y['Neighborstdev']==0:
            z_neighbor=0
        else:
            z_neighbor=(x['Cases']-y['Neighbormean'])/y['Neighborstdev']
        
        if z['Statestdev']==0:
            z_state=0
        else:
            z_state=(x['Cases']-z['Statemean'])/z['Statestdev']
        
        csv_writer.writerow([x['DistrictID'], x['WeekID'], round(z_neighbor,2) , round(z_state,2)])
        

#========================== Calculation of Z-scores for Months====================

df= pd.read_csv("./Question2/cases-month.csv")
cases_record=df.to_dict('records')
df= pd.read_csv("./Question4/neighbor-month.csv")
neighbor_record=df.to_dict('records')
df= pd.read_csv("./Question5/state-month.csv")
state_record=df.to_dict('records')



with open('./Question6/zscore-month.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'MonthID', 'NeighborhoodZscore', 'StateZscore'])
    for x,y,z in zip(cases_record,neighbor_record,state_record):
        if y['Neighborstdev']==0:
            z_neighbor=0
        else:
            z_neighbor=(x['Cases']-y['Neighbormean'])/y['Neighborstdev']
        
        if z['Statestdev']==0:
            z_state=0
        else:
            z_state=(x['Cases']-z['Statemean'])/z['Statestdev']
        
        csv_writer.writerow([x['DistrictID'], x['MonthID'], round(z_neighbor,2) , round(z_state,2)])

#========================Calculation Z-scores for Overall ==================

df= pd.read_csv("./Question2/cases-overall.csv")
cases_record=df.to_dict('records')
df= pd.read_csv("./Question4/neighbor-overall.csv")
neighbor_record=df.to_dict('records')
df= pd.read_csv("./Question5/state-overall.csv")
state_record=df.to_dict('records')

with open('./Question6/zscore-overall.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID', 'OverallID', 'NeighborhoodZscore', 'StateZscore'])
    for x,y,z in zip(cases_record,neighbor_record,state_record):
        if y['Neighborstdev']==0:
            z_neighbor=0
        else:
            z_neighbor=(x['Cases']-y['Neighbormean'])/y['Neighborstdev']
        if z['Statestdev']==0:
            z_state=0
        else:
            z_state=(x['Cases']-z['Statemean'])/z['Statestdev']
        
        csv_writer.writerow([x['DistrictID'],1, round(z_neighbor,2) , round(z_state,2)])
#=========================================   Writing csv output for Question6 Ends    ==================================

print('Output files zscore-week.csv  zscore-month.csv  zscore-overall.csv produced in Folder Question6')
