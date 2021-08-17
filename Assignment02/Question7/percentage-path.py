
import pandas as pd
import csv
import json



with open("./Helpers/articles.json", "r") as read_file:
    articles=json.load(read_file)

cols=['A','B','C','D','E']
df = pd.read_csv("./Data/paths_finished.tsv",sep="\t",names=cols)
df=df[16:]
paths=list(df['D'])
path_info={}
i=1;
for x in paths:
    path_info['line'+str(i)]={}
    y=x.split(';')
    path_info['line'+str(i)]['source']=y[0]
    path_info['line'+str(i)]['destination']=y[-1]
    
    if '<' in y:
        
        path_info['line'+str(i)]['len_c']=len(y)-1
        path_info['line'+str(i)]['len_wc']=len(y)-(2*(y.count('<'))+1)
        
    else:
        path_info['line'+str(i)]['len_c']=len(y)-1
        path_info['line'+str(i)]['len_wc']=len(y)-1
    
    i+=1



SPD_file = open("./Data/shortest-path-distance-matrix.txt",mode='r')
SPD=SPD_file.readlines()


for x in path_info:
    path_info[x]['SPD']=int(SPD[16+int(articles[path_info[x]['source']]['id'][1:])][int(articles[path_info[x]['destination']]['id'][1:])-1])
    



def counter(t,s):
    
    
    Total_paths=0
    equal=0
    greater_1=0
    greater_2=0
    greater_3=0
    greater_4=0
    greater_5=0
    greater_6=0
    greater_7=0
    greater_8=0
    greater_9=0
    greater_10=0
    greater_11=0

    for x in path_info:
        Total_paths+=1
        if path_info[x]['SPD']==path_info[x][t]:
            equal+=1
        if (path_info[x][t]-path_info[x]['SPD'])==1:
            greater_1+=1

        if (path_info[x][t]-path_info[x]['SPD'])==2:
            greater_2+=1

        if (path_info[x][t]-path_info[x]['SPD'])==3:
            greater_3+=1

        if (path_info[x][t]-path_info[x]['SPD'])==4:
            greater_4+=1

        if (path_info[x][t]-path_info[x]['SPD'])==5:
            greater_5+=1

        if (path_info[x][t]-path_info[x]['SPD'])==6:
            greater_6+=1

        if (path_info[x][t]-path_info[x]['SPD'])==7:
            greater_7+=1

        if (path_info[x][t]-path_info[x]['SPD'])==8:
            greater_8+=1

        if (path_info[x][t]-path_info[x]['SPD'])==9:
            greater_9+=1

        if (path_info[x][t]-path_info[x]['SPD'])==10:
            greater_10+=1

        if (path_info[x][t]-path_info[x]['SPD'])>=11:
            greater_11+=1

    
    location='./Question7/'+s
    with open(location, mode='w') as output_file:
        csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Equal_Length','Larger_by_1','Larger_by_2','Larger_by_3','Larger_by_4','Larger_by_5','Larger_by_6','Larger_by_7','Larger_by_8','Larger_by_9','Larger_by_10','Larger_by_more_than_10'])
        csv_writer.writerow([ str(round((equal/Total_paths)*100,2))+" %",str(round((greater_1/Total_paths)*100,2))+" %",
                             str(round((greater_2/Total_paths)*100,2))+" %",
                             str(round((greater_3/Total_paths)*100,2))+" %",str(round((greater_4/Total_paths)*100,2))+" %",
                             str(round((greater_5/Total_paths)*100,2))+" %",str(round((greater_6/Total_paths)*100,2))+" %",
                            str(round((greater_7/Total_paths)*100,2))+" %",str(round((greater_8/Total_paths)*100,2))+" %",
                            str(round((greater_9/Total_paths)*100,2))+" %",str(round((greater_10/Total_paths)*100,2))+" %",
                             str(round((greater_11/Total_paths)*100,2))+" %"])

counter("len_wc","percentage-paths-no-back.csv")
counter("len_c","percentage-paths-back.csv")


print("output file percentage-paths-no-back.csv produced in folder Question7")
print("output file percentage-paths-back.csv produced in folder Question7")
