
import pandas as pd
import csv
import networkx as nx
import json


with open("./Helpers/articles.json", "r") as read_file:
    articles=json.load(read_file)


G = nx.read_edgelist("./Question4/edges.csv", create_using=nx.DiGraph, nodetype=str,delimiter=',')

df = pd.read_csv("./Question2/category-ids.csv",sep=",")

category_paths={}
for x,y in zip(df['Category_Name'], df['Category_ID']):
    category_paths[y]={}
    category_paths[y]['Name']=x
    

cols=['A','B','C','D','E']
df = pd.read_csv("./Data/paths_finished.tsv",sep="\t",names=cols)
df=df[16:]
paths=list(df['D'])
actual_paths={}
i=17;
for x in paths:
    actual_paths['line'+str(i)]={}
    y=x.split(';')
    actual_paths['line'+str(i)]['source']=articles[y[0]]['id']
    actual_paths['line'+str(i)]['destination']=articles[y[-1]]['id']
    path=[]
    if '<' in y:
        for item in y:
            if item !='<':
                path.append(articles[item]['id'])
            if item =='<':
                path.pop()
        
    else:
        for item in y:
            path.append(articles[item]['id'])
    
    actual_paths['line'+str(i)]['human_path']=path
    actual_paths['line'+str(i)]['shortest_path']=nx.shortest_path(G, source=articles[y[0]]['id'], target=articles[y[-1]]['id'])
    
    i+=1


df = pd.read_csv("./Question3/article-categories.csv",sep=",")


article_categories={}
for x,y in zip(df['Article_ID'], df['Category_IDs']):
    article_categories[x]=y




for x in category_paths:
    count_human=0
    count_shortest=0
    for y in actual_paths:
        for z in actual_paths[y]['human_path']:
            if x in article_categories[z]:
                count_human+=1
                break
        
        for z in actual_paths[y]['shortest_path']:
            if x in article_categories[z]:
                count_shortest+=1
                break
                
    category_paths[x]['h_paths']=count_human
    category_paths[x]['s_paths']=count_shortest
    

for x in category_paths:
    count_human=0
    count_shortest=0
    for y in actual_paths:
        for z in actual_paths[y]['human_path']:
            if x in article_categories[z]:
                count_human+=1

        
        for z in actual_paths[y]['shortest_path']:
            if x in article_categories[z]:
                count_shortest+=1
                
                
    category_paths[x]['hp_total']=count_human
    category_paths[x]['sp_total']=count_shortest
                

with open('./Question8/category-paths.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Category_ID','Number_of_human_paths_traversed','Number_of_human_times_traversed','Number_of_shortest_paths_traversed','Number_of_shortest_times_traversed'])
    for x in category_paths:
        csv_writer.writerow([x,category_paths[x]['h_paths'],category_paths[x]['hp_total'],category_paths[x]['s_paths'],category_paths[x]['sp_total']])

 
print("output file category-paths.csv produced in folder Question8")