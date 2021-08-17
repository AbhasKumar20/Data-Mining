"""----------------------------------------------Question 06-----------------------------------------"""
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
    


with open('./Question6/finished-paths-no-back.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Human_Path_Length','Shortest_Path_Length','Ratio'])
    for x in path_info:
        csv_writer.writerow([ path_info[x]['len_wc'],path_info[x]['SPD'],round(path_info[x]['len_wc']/path_info[x]['SPD'],2)])
    

with open('./Question6/finished-paths-back.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Human_Path_Length','Shortest_Path_Length','Ratio'])
    for x in path_info:
        csv_writer.writerow([ path_info[x]['len_c'],path_info[x]['SPD'],round(path_info[x]['len_c']/path_info[x]['SPD'],2)])



with open('./Helpers/articles.json', "w") as file_write:
    json.dump(articles, file_write)


print("output file finished-paths-no-back.csv produced in folder Question6.")
print("output file finished-paths-back.csv produced in folder Question6.")
