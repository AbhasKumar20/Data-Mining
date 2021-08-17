
print('Question 2 Python Script case-generator.py running.........')

import json
from collections import OrderedDict
import csv
import requests
import pandas as pd
from difflib import SequenceMatcher


with open("./Input_Files/neighbor-districts.json", "r") as read_file:
    raw_data=json.load(read_file)

df= pd.read_csv("./Input_Files/districts.csv")
data_df=df[['Date', 'District','Confirmed']]

#=========================================================   Preprocessing starts     ===================================================

del raw_data['bijapur_district/Q1727570']
arranged_data=OrderedDict(sorted(raw_data.items(), key=lambda t: t[0]))

district_names=list(arranged_data.keys())
raw_districts=district_names


district_names=[x.split('/')[0] for x in district_names]
district_names=sorted([x.replace('_district','') for x in district_names])
new_districts=district_names
district_list=set(data_df.District.values)-{'CAPF Personnel','BSF Camp','Airport Quarantine','Evacuees','Foreign Evacuees','Italians','Other Region','Other State','Unknown'}
raw_district_list=sorted(set(district_list))

district_list=[x.lower() for x in district_list]
district_list=sorted([x.replace(" ","") for x in district_list])

#----keeping Mapping intact--------------------------
district_dict={}
id=1001
for key,x in zip(sorted(district_list),sorted(raw_district_list)):
    district_dict[key]={}
    district_dict[key]['alias']=x
    district_dict[key]['districtid']=id
    id+=1

data1={}
id=101
for x,y in zip(sorted(new_districts),sorted(raw_districts)):
    data1[x]={}
    data1[x]['alias']=y
    data1[x]['districtid']=id
    data1[x]['neighbors']=arranged_data[y]
    id+=1

#---------------------------------------------

#--------------District Matching--------------------------------
lst=set(district_list)
matched_pair=[]
still_missing=[]
for x in district_names:
    max=0.74
    flag=-1
    for y in lst:
        s=SequenceMatcher(a=x,b=y).ratio()
        if ((x[0]==y[0]) and (s>0.75) and (s>max)):
            max=s
            pair=y
            flag=1
    if flag==1:
        matched_pair.append((x,pair))
        lst-={pair}
        #print(x,pair,max)
    if flag==-1 and (x not in still_missing):
        still_missing.append(x)

#-----------------------------------------------------------


neighbor_districts={}
matched_district_csv=[]
for x,y in matched_pair:
    neighbor_districts[data1[x]['alias']]={}
    neighbor_districts[data1[x]['alias']]['districtid']=data1[x]['districtid']
    neighbor_districts[data1[x]['alias']]['neighbors']=arranged_data[data1[x]['alias']]
    matched_district_csv.append(district_dict[y]['alias'])

unmatched_district_csv=(set(raw_district_list)- set(matched_district_csv))
#------------ Matching Delhi------------------------------------------------
delhi_list=[]
for x in still_missing:
    if '_delhi' in x:
        delhi_list.append(x)
delhi_neighbor=set()
for x in delhi_list:
    delhi_neighbor |= set(arranged_data[data1[x]['alias']])


neighbor_districts['delhi/Q107941']={}
neighbor_districts['delhi/Q107941']['districtid']=0
neighbor_districts['delhi/Q107941']['neighbors']=delhi_neighbor
unmatched_district_csv=sorted(set(raw_district_list)-set(matched_district_csv))
still_missing=set(still_missing)-set(delhi_list)
unmatched_district_csv=set(unmatched_district_csv)-{'Delhi'}

#-------------------------------------------------------------
#-------------Matching Mumbai-------------------------------------------

mumbai_list=[]
for x in still_missing:
    if 'mumbai' in x:
        mumbai_list.append(x)

mumbai_neighbor=set()
for x in mumbai_list:
    mumbai_neighbor |= set(arranged_data[data1[x]['alias']])

neighbor_districts['mumbai/Q943099']={}
neighbor_districts['mumbai/Q943099']['districtid']=1
neighbor_districts['mumbai/Q943099']['neighbors']=mumbai_neighbor

still_missing=set(still_missing)-set(mumbai_list)
unmatched_district_csv=set(unmatched_district_csv)-{'Railway Quarantine','Others','Mumbai','Airport Quarantine','Evacuees','Foreign Evacuees','Italians','Other Region','Other State'}
#---------------------------------------------------------------------------------

merged_matching_csv={'Delhi':'delhi/Q107941','Mumbai':'mumbai/Q943099'}
manually_matched={'Bhadohi':'sant_ravidas_nagar','Amroha':'jyotiba_phule_nagar','Palakkad':'palghat','Karbi Anglong':'east_karbi_anglong','Ganganagar':'sri_ganganagar','S.P.S. Nellore':'sri_potti_sriramulu_nellore','West Champaran':'pashchim_champaran', 'West Singhbhum':'pashchimi_singhbhum','Balasore':'baleshwar','Kaimur':'kaimur_(bhabua)','Hooghly':'hugli','East Champaran':'purba_champaran','East Singhbhum':'purbi_singhbhum','Tirunelveli':'tirunelveli_kattabo','Dang':'the_dangs','Nilgiris':'the_nilgiris','S.A.S. Nagar':'sahibzada_ajit_singh_nagar','Lakhimpur Kheri':'kheri','Beed':'bid','Ballari':'bellary','Y.S.R. Kadapa':'ysr'}
unmatched_district_csv=set(unmatched_district_csv)-set([x for x in manually_matched.keys()])
still_missing=set(still_missing)-set([x for x in manually_matched.values()])
for key,value in manually_matched.items():
    neighbor_districts[data1[value]['alias']]={}
    neighbor_districts[data1[value]['alias']]['districtid']=6
    neighbor_districts[data1[value]['alias']]['neighbors']=arranged_data[data1[value]['alias']]

#------ Working with Districts of different state with Same Name------------------------------
duplicate_districts=['bilaspur/Q1478939','bilaspur/Q100157','balrampur/Q1948380','balrampur/Q16056268','pratapgarh/Q1585433','pratapgarh/Q1473962','hamirpur/Q2019757','hamirpur/Q2086180','aurangabad/Q43086','aurangabad/Q592942']
for x in duplicate_districts:
    neighbor_districts[x]={}
    neighbor_districts[x]['districtid']=0
    neighbor_districts[x]['neighbors']=raw_data[x]

neighbor_districts=OrderedDict(sorted(neighbor_districts.items(), key=lambda t: t[0]))

id=101
for x in neighbor_districts:
    neighbor_districts[x]['districtid']=id
    id+=1
#--------------------------------------------------------------------------------------------------
""" Generate Date """
import datetime
dates=[]
start='2020-03-15'
end='2020-09-05'
start = datetime.datetime.strptime(start, '%Y-%m-%d')
end = datetime.datetime.strptime(end, '%Y-%m-%d')
step = datetime.timedelta(days=1)
while start<=end:
    dates.append(start.date())
    start+=step
imp_dates_week=[]
imp_dates_week.append((dates[0],0))
j=1
for i in range(len(dates)):
     if(i%7==6):
        imp_dates_week.append((dates[i],j))
        j+=1
imp_dates_month=[('2020-03-31',1),('2020-04-30',2),('2020-05-31',3),('2020-06-30',4),('2020-07-31',5),('2020-08-31',6),('2020-09-05',7)]
populate_dict={}
populate_dict["weeks"]={}
populate_dict["months"]={}
for x in imp_dates_week:
    populate_dict["weeks"][str(x[1])]={}
    populate_dict["weeks"][str(x[1])]=0

for x in imp_dates_month:
    populate_dict['months'][str(x[1])]={}
    populate_dict['months'][str(x[1])]=0

populate_dict['year']={'1':0}

cases={}
for x,y in matched_pair:
    cases[district_dict[y]['alias']]={}
    cases[district_dict[y]['alias']]['weeks']=populate_dict['weeks'].copy()
    cases[district_dict[y]['alias']]['months']=populate_dict['months'].copy()
    cases[district_dict[y]['alias']]['year']=populate_dict['year'].copy()


cases['Delhi']={}
cases['Delhi']['weeks']=populate_dict['weeks'].copy()
cases['Delhi']['months']=populate_dict['months'].copy()
cases['Delhi']['year']=populate_dict['year'].copy()

cases['Mumbai']={}
cases['Mumbai']['weeks']=populate_dict['weeks'].copy()
cases['Mumbai']['months']=populate_dict['months'].copy()
cases['Mumbai']['year']=populate_dict['year'].copy()


for x in manually_matched:
    cases[x]={}
    cases[x]['weeks']=populate_dict['weeks'].copy()
    cases[x]['months']=populate_dict['months'].copy()
    cases[x]['year']=populate_dict['year'].copy()
    
"""          Confirmed cases from 15 march to 25 April since for this period data was missing in District.csv(Input File)           """

cases['Delhi']['weeks']['0']=7
cases['Mumbai']['weeks']['0']=26

cases['Delhi']['weeks']['1']=27
cases['Mumbai']['weeks']['1']=64
cases['Chandigarh']['weeks']['1']=5

cases['Delhi']['weeks']['2']=49
cases['Mumbai']['weeks']['2']=181
cases['Chandigarh']['weeks']['2']=8

cases['Delhi']['weeks']['3']=445
cases['Mumbai']['weeks']['3']=635
cases['Chandigarh']['weeks']['3']=18
cases['Jaipur']['weeks']['3']=69
cases['Jodhpur']['weeks']['3']=60
cases['Udaipur']['weeks']['3']=3

cases['Delhi']['weeks']['4']=1069
cases['Mumbai']['weeks']['4']=1761
cases['Chandigarh']['weeks']['4']=19
cases['Jaipur']['weeks']['4']=233
cases['Jodhpur']['weeks']['4']=207
cases['Udaipur']['weeks']['4']=4

cases['Delhi']['weeks']['5']=1893
cases['Mumbai']['weeks']['5']=3648
cases['Chandigarh']['weeks']['5']=23
cases['Jaipur']['weeks']['5']=450
cases['Jodhpur']['weeks']['5']=448
cases['Udaipur']['weeks']['5']=7

cases['Delhi']['weeks']['6']=2625
cases['Mumbai']['weeks']['6']=7628
cases['Chandigarh']['weeks']['6']=28
cases['Jaipur']['weeks']['6']=694
cases['Jodhpur']['weeks']['6']=590
cases['Udaipur']['weeks']['6']=8

#--------------------------------------------------------- For Month March------------------------


cases['Delhi']['months']['1']=120
cases['Mumbai']['months']['1']=302
cases['Chandigarh']['months']['1']=15
#---------------------------------------------------------------------------------------------


df= pd.read_csv("./Input_Files/districts.csv")
data_df=df[['Date', 'District','Confirmed','State']]
records=data_df.to_dict('records')

#---------------------------------------- Working for Duplicate Districts------------------------------
duplicate_districts_csv=['Aurangabad','Bilaspur','Balrampur','Hamirpur','Pratapgarh']
duplicate_districts_state=[]
for x in records:
    if x['District'] in duplicate_districts_csv and (x['District'],x['State']) not in duplicate_districts_state:
        duplicate_districts_state.append((x['District'],x['State']))

for x in duplicate_districts_csv:
    del cases[x]

for x in cases:
    for y in records:
        if x==y['District']:
            cases[x]['stateid']=y['State']
            continue
merged_duplicate_districts=[]
for x,y in duplicate_districts_state:
    cases[x+'_'+y]={}
    cases[x+'_'+y]['weeks']=populate_dict['weeks'].copy()
    cases[x+'_'+y]['months']=populate_dict['months'].copy()
    cases[x+'_'+y]['year']=populate_dict['year'].copy()
    cases[x+'_'+y]['stateid']=y
    merged_duplicate_districts.append(x+'_'+y)

#------------------------------------- Counting Confirmed Cases Weekly,Monthly and for Overall----------------------------------
for d in imp_dates_week:
    if d[1]>=7:
        for x in records:
            if x['Date']==str(d[0]) and x['District'] in [a.split('_')[0] for a in cases.keys()]:
                if x['District'] in [a.split('_')[0] for a in merged_duplicate_districts]:
                    cases[x['District']+'_'+x['State']]['weeks'][str(d[1])]=x['Confirmed']
            if x['Date']==str(d[0]) and x['District'] in cases.keys():
                cases[x['District']]['weeks'][str(d[1])]=x['Confirmed']

for d in imp_dates_month:
    if 2<=d[1]<=6:
        for x in records:
            if x['Date']==str(d[0]) and x['District'] in [a.split('_')[0] for a in cases.keys()]:
                if x['District'] in [a.split('_')[0] for a in merged_duplicate_districts]:
                    cases[x['District']+'_'+x['State']]['months'][str(d[1])]=x['Confirmed']
            if x['Date']==str(d[0]) and x['District'] in cases.keys():
                cases[x['District']]['months'][str(d[1])]=x['Confirmed']
    if d[1]==7:
        for x in records:
            if x['Date']==str(d[0]) and x['District'] in [a.split('_')[0] for a in cases.keys()]:
                if x['District'] in [a.split('_')[0] for a in merged_duplicate_districts]:
                    cases[x['District']+'_'+x['State']]['months'][str(d[1])]=x['Confirmed']
                    cases[x['District']+'_'+x['State']]['year']['1']=x['Confirmed']

            if x['Date']==str(d[0]) and x['District'] in cases.keys():
                cases[x['District']]['months'][str(d[1])]=x['Confirmed']
                cases[x['District']]['year']['1']=x['Confirmed']
#----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------- Generating Neighbors of each District --------------------------

neighbors={}
for x,y in sorted(matched_pair):
    neighbors[district_dict[y]['alias']]=data1[x]['neighbors']
for x,y in manually_matched.items():
    neighbors[x]=data1[y]['neighbors']

output={}
for x in neighbors:
    l=[]
    l=neighbors[x]
    l=[i.split('/')[0] for i in l]
    l=[i.replace('_district','') for i in l]
    neighbor=[]
    for y in l:
        if y in [a for a,b in matched_pair ]:
            for a,b in matched_pair:
                if y==a:
                    neighbor.append(district_dict[b]['alias'])

        if y in manually_matched.values():
            for k in manually_matched:
                if y==manually_matched[k]:
                    neighbor.append(k)

    output[x]={}
    output[x]=neighbor

output['Delhi']=['Gurugram','Sonipat','Faridabad','Gautam Buddha Nagar','Ghaziabad','Baghpat','Jhajjar']
output['Mumbai']=['Thane']


output['Aurangabad_Maharashtra']=output.pop('Aurangabad')
output['Bilaspur_Himachal Pradesh']=output.pop('Bilaspur')
output['Hamirpur_Himachal Pradesh']=output.pop('Hamirpur')
output['Pratapgarh_Rajasthan']=output.pop('Pratapgarh')
output['Balrampur_Uttar Pradesh']=output.pop('Balrampur')


for x in ['Aurangabad_Maharashtra','Bilaspur_Himachal Pradesh','Hamirpur_Himachal Pradesh','Pratapgarh_Rajasthan','Balrampur_Uttar Pradesh']:
    for key in output:
        if x.split('_')[0] in output[key]:
            output[key]=[a.replace(x.split('_')[0],x) for a in output[key]]

duplicate_districts_neighbors={'Pratapgarh_Uttar Pradesh':['jaunpur/Q1356060', 'rae_bareilly/Q1321157', 'prayagraj/Q1773426', 'amethi/Q1071494', 'kaushambi/Q1946937', 'sultanpur/Q1356154', 'fatehpur/Q1946829'],'Hamirpur_Uttar Pradesh':['kanpur_nagar/Q2089152', 'mahoba/Q1815322', 'kanpur_dehat/Q610612', 'jhansi/Q1937885', 'jalaun/Q2089115', 'banda/Q2131759', 'fatehpur/Q1946829'],'Balrampur_Chhattisgarh' :['gumla/Q2295865', 'sonbhadra/Q607798', 'surajpur/Q16938031', 'jashpur/Q2577551', 'garhwa/Q2302076', 'singrauli/Q2668638', 'latehar/Q2244762', 'surguja/Q1805075'],'Aurangabad_Bihar': ['arwal/Q42917', 'gaya/Q49173', 'palamu/Q1797254', 'rohtas/Q100085'],'Bilaspur_Chhattisgarh' :['mungeli/Q13476249', 'baloda_bazar/Q15663455', 'korba/Q2299121', 'anuppur/Q2299093', 'janjgir-champa/Q2575633', 'koriya/Q2295896']}

for x in duplicate_districts_neighbors:
    l=[]
    l=duplicate_districts_neighbors[x]
    l=[i.split('/')[0] for i in l]
    l=[i.replace('_district','') for i in l]
    neighbor=[]
    for y in l:
        if y in [a for a,b in matched_pair ]:
            for a,b in matched_pair:
                if y==a:
                    neighbor.append(district_dict[b]['alias'])

        if y in manually_matched.values():
            for k in manually_matched:
                if y==manually_matched[k]:
                    neighbor.append(k)
    
    output[x]={}
    output[x]=neighbor

for x in output['Aurangabad_Bihar']:
    output[x]=[a.replace('Aurangabad_Maharashtra','Aurangabad_Bihar') for a in output[x]]
for x in output['Bilaspur_Chhattisgarh']:
    output[x]=[a.replace('Bilaspur_Himachal Pradesh','Bilaspur_Chhattisgarh') for a in output[x]]
for x in output['Balrampur_Chhattisgarh']:
    output[x]=[a.replace('Balrampur_Uttar Pradesh','Balrampur_Chhattisgarh') for a in output[x]]
for x in output['Pratapgarh_Uttar Pradesh']:
    output[x]=[a.replace('Pratapgarh_Rajasthan','Pratapgarh_Uttar Pradesh') for a in output[x]]
for x in output['Hamirpur_Uttar Pradesh']:
    output[x]=[a.replace('Hamirpur_Himachal Pradesh','Hamirpur_Uttar Pradesh') for a in output[x]]

for x in cases:
    cases[x]['neighbors']=output[x]
#---------------------------------------------------------------------------------------------------------------------
cases=OrderedDict(sorted(cases.items(), key=lambda t: t[0]))
id=101
for x in cases:
    cases[x]['districtid']=id
    id+=1

cases['Thane']['neighbors']+=['Mumbai']
for x in cases['Delhi']['neighbors']:
    cases[x]['neighbors']+=['Delhi']

#-------------------------------- My main File having all info of a district ================

with open("./Input_Files/cases.json", "w") as outfile:
    json.dump(cases, outfile)


#==================================.   Writing csv output for Question2           =========================

with open('./Question2/cases-week.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID','WeekID','Cases'])
    for x in cases:
        for i in range(1,26):
            csv_writer.writerow([cases[x]['districtid'],i,cases[x]['weeks'][str(i)]-cases[x]['weeks'][str(i-1)]])

with open('./Question2/cases-month.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID','MonthID','Cases'])
    for x in cases:
        for i in range(1,8):
            if i==1:
                csv_writer.writerow([cases[x]['districtid'],i,cases[x]['months'][str(i)]-cases[x]['weeks']['0']])

            else:
                csv_writer.writerow([cases[x]['districtid'],i,cases[x]['months'][str(i)]-cases[x]['months'][str(i-1)]])

with open('./Question2/cases-overall.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['DistrictID','OverallID','Cases'])
    for x in cases:
        csv_writer.writerow([cases[x]['districtid'],1,cases[x]['year'][str(1)]])
            

#=========================================   Writing csv output for Question2 Ends          ==================================

print('Output files cases-week.csv  cases-month.csv  cases-overall.csv produced in Folder Question2')
