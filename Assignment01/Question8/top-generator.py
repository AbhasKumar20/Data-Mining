
print('Question 8 Python Script top-generator.py running........')

import json
import csv
import math
import pandas as pd

with open("./Input_Files/cases.json", "r") as read_file:
    cases=json.load(read_file)

#=================== Writing Output For Question 8=========================

#------------- Finding top 5 Hotspots/Coldspots Weekly--------------------
df=pd.read_csv("./Question6/zscore-week.csv")
zscore_record=df.to_dict('records')
neighbor_week_hotspot={}
state_week_hotspot={}
neighbor_week_coldspot={}
state_week_coldspot={}
for i in range(1,26):
    neighbor_hotspot=[]
    state_hotspot=[]
    neighbor_coldspot=[]
    state_coldspot=[]
    for x in zscore_record:
        if x['WeekID']==i and x['NeighborhoodZscore']>1:
            neighbor_hotspot.append((x['DistrictID'],x['NeighborhoodZscore']))
        if x['WeekID']==i and x['NeighborhoodZscore']<-1:
            neighbor_coldspot.append((x['DistrictID'],x['NeighborhoodZscore']))
        if x['WeekID']==i and x['StateZscore']>1:
            state_hotspot.append((x['DistrictID'],x['StateZscore']))
        if x['WeekID']==i and x['StateZscore']<-1:
            state_coldspot.append((x['DistrictID'],x['StateZscore']))
        
    neighbor_week_hotspot['Week'+str(i)]=neighbor_hotspot
    neighbor_week_coldspot['Week'+str(i)]=neighbor_coldspot
    state_week_hotspot['Week'+str(i)]=state_hotspot
    state_week_coldspot['Week'+str(i)]=state_coldspot


with open('./Question8/top-week.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['WeekID','Method','Spot', 'DistrictID1','DistrictID2','DistrictID3','DistrictID4','DistrictID5'])   
    for i in range(1,26):
        neighbor_hotspot=sorted(neighbor_week_hotspot['Week'+str(i)], key = lambda x: x[1])
        if len(neighbor_hotspot)==0:
            csv_writer.writerow([i,'Neighborhood','Hot', ' ',' ',' ',' ',' '])
        else:
            csv_writer.writerow([i,'Neighborhood','Hot',neighbor_hotspot[-1][0],neighbor_hotspot[-2][0],neighbor_hotspot[-3][0],neighbor_hotspot[-4][0],neighbor_hotspot[-5][0]])

        neighbor_coldspot=sorted(neighbor_week_coldspot['Week'+str(i)], key = lambda x: x[1])
        if len(neighbor_coldspot)==0:
            csv_writer.writerow([i,'Neighborhood','Cold', ' ',' ',' ',' ',' '])
        else:
            csv_writer.writerow([i,'Neighborhood','Cold',neighbor_coldspot[0][0],neighbor_coldspot[1][0],neighbor_coldspot[2][0],neighbor_coldspot[3][0],neighbor_coldspot[4][0]])

        state_hotspot=sorted(state_week_hotspot['Week'+str(i)], key = lambda x: x[1])
        if len(state_hotspot)<3:
            if len(state_hotspot)==0:
                csv_writer.writerow([i,'State','Hot', ' ',' ',' ',' ',' '])
            if len(state_hotspot)==2:
                csv_writer.writerow([i,'State','Hot',state_hotspot[-1][0],state_hotspot[-2][0],' ',' ',' '])

        state_coldspot=sorted(state_week_coldspot['Week'+str(i)], key = lambda x: x[1])
        if len(state_coldspot)<4:
            if len(state_coldspot)==0:
                csv_writer.writerow([i,'State','Cold', ' ',' ',' ',' ',' '])
            if len(state_coldspot)==2:
                csv_writer.writerow([i,'State','Cold',state_coldspot[0][0],state_coldspot[1][0],' ',' ',' '])
              
        else:
            csv_writer.writerow([i,'State','Cold',state_coldspot[0][0],state_coldspot[1][0],state_coldspot[2][0],state_coldspot[3][0],state_coldspot[4][0]])

#------------- Finding top 5 Hotspots/Coldspots Monthly --------------------

df=pd.read_csv("./Question6/zscore-month.csv")
zscore_record=df.to_dict('records')
neighbor_week_hotspot={}
state_week_hotspot={}
neighbor_week_coldspot={}
state_week_coldspot={}
for i in range(1,8):
    neighbor_hotspot=[]
    state_hotspot=[]
    neighbor_coldspot=[]
    state_coldspot=[]
    for x in zscore_record:
        if x['MonthID']==i and x['NeighborhoodZscore']>1:
            neighbor_hotspot.append((x['DistrictID'],x['NeighborhoodZscore']))
        if x['MonthID']==i and x['NeighborhoodZscore']<-1:
            neighbor_coldspot.append((x['DistrictID'],x['NeighborhoodZscore']))
        if x['MonthID']==i and x['StateZscore']>1:
            state_hotspot.append((x['DistrictID'],x['StateZscore']))
        if x['MonthID']==i and x['StateZscore']<-1:
            state_coldspot.append((x['DistrictID'],x['StateZscore']))
        
    neighbor_week_hotspot['Month'+str(i)]=neighbor_hotspot
    neighbor_week_coldspot['Month'+str(i)]=neighbor_coldspot
    state_week_hotspot['Month'+str(i)]=state_hotspot
    state_week_coldspot['Month'+str(i)]=state_coldspot


with open('./Question8/top-month.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['MonthID','Method','Spot', 'DistrictID1','DistrictID2','DistrictID3','DistrictID4','DistrictID5'])   
    for i in range(1,8):
        neighbor_hotspot=sorted(neighbor_week_hotspot['Month'+str(i)], key = lambda x: x[1])
        if len(neighbor_hotspot)==0:
            csv_writer.writerow([i,'Neighborhood','Hot', ' ',' ',' ',' ',' '])
        else:
            csv_writer.writerow([i,'Neighborhood','Hot',neighbor_hotspot[-1][0],neighbor_hotspot[-2][0],neighbor_hotspot[-3][0],neighbor_hotspot[-4][0],neighbor_hotspot[-5][0]])

        neighbor_coldspot=sorted(neighbor_week_coldspot['Month'+str(i)], key = lambda x: x[1])
        if len(neighbor_coldspot)==0:
            csv_writer.writerow([i,'Neighborhood','Cold', ' ',' ',' ',' ',' '])
        else:
            csv_writer.writerow([i,'Neighborhood','Cold',neighbor_coldspot[0][0],neighbor_coldspot[1][0],neighbor_coldspot[2][0],neighbor_coldspot[3][0],neighbor_coldspot[4][0]])

        state_hotspot=sorted(state_week_hotspot['Month'+str(i)], key = lambda x: x[1])
        if len(state_hotspot)==0:
            csv_writer.writerow([i,'State','Hot', ' ',' ',' ',' ',' '])
        else:
            csv_writer.writerow([i,'State','Hot',state_hotspot[-1][0],state_hotspot[-2][0],state_hotspot[-3][0],state_hotspot[-4][0],state_hotspot[-5][0]])

        state_coldspot=sorted(state_week_coldspot['Month'+str(i)], key = lambda x: x[1])
        if len(state_coldspot)<3:
            if len(state_coldspot)==0:
                csv_writer.writerow([i,'State','Cold', ' ',' ',' ',' ',' '])
            if len(state_coldspot)==2:
                csv_writer.writerow([i,'State','Cold',state_coldspot[0][0],state_coldspot[1][0],' ',' ',' '])
              
        else:
            csv_writer.writerow([i,'State','Cold',state_coldspot[0][0],state_coldspot[1][0],state_coldspot[2][0],state_coldspot[3][0],state_coldspot[4][0]])

#------------- Finding top 5 Hotspots/Coldspots Overall--------------------

df=pd.read_csv("./Question6/zscore-overall.csv")
zscore_record=df.to_dict('records')

neighbor_hotspot=[]
state_hotspot=[]
neighbor_coldspot=[]
state_coldspot=[]
for x in zscore_record:
    if x['NeighborhoodZscore']>1:
        neighbor_hotspot.append((x['DistrictID'],x['NeighborhoodZscore']))
    if x['NeighborhoodZscore']<-1:
        neighbor_coldspot.append((x['DistrictID'],x['NeighborhoodZscore']))
    if x['StateZscore']>1:
        state_hotspot.append((x['DistrictID'],x['StateZscore']))
    if x['StateZscore']<-1:
        state_coldspot.append((x['DistrictID'],x['StateZscore']))
    
with open('./Question8/top-overall.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['OverallID','Method','Spot', 'DistrictID1','DistrictID2','DistrictID3','DistrictID4','DistrictID5'])   
    neighbor_hotspot=sorted(neighbor_hotspot, key = lambda x: x[1])
    csv_writer.writerow([1,'Neighborhood','Hot',neighbor_hotspot[-1][0],neighbor_hotspot[-2][0],neighbor_hotspot[-3][0],neighbor_hotspot[-4][0],neighbor_hotspot[-5][0]])

    neighbor_coldspot=sorted(neighbor_coldspot, key = lambda x: x[1])
    csv_writer.writerow([1,'Neighborhood','Cold',neighbor_coldspot[0][0],neighbor_coldspot[1][0],neighbor_coldspot[2][0],neighbor_coldspot[3][0],neighbor_coldspot[4][0]])

    state_hotspot=sorted(state_hotspot, key = lambda x: x[1])
    csv_writer.writerow([1,'State','Hot',state_hotspot[-1][0],state_hotspot[-2][0],state_hotspot[-3][0],state_hotspot[-4][0],state_hotspot[-5][0]])

    state_coldspot=sorted(state_coldspot, key = lambda x: x[1])
    csv_writer.writerow([1,'State','Cold',state_coldspot[0][0],state_coldspot[1][0],state_coldspot[2][0],state_coldspot[3][0],state_coldspot[4][0]])

#=================== Writing Output For Question 8 Ends=========================

"""
For intial weeks districts like Delh and Chandhigarh are not there in weekly hotspots as these were the only districts in their respective state and instruction was to take state standard Deviation in such cases as '0' hence Z-score was not applicable for such districts, although they were having significant confirmed cases. This results in empty entries in the intial weeks.
"""

print('Output files top-week.csv  top-month.csv  top-overall.csv produced in Folder Question8')
