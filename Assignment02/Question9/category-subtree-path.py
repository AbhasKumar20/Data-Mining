

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

for x in category_paths:
    empty=[]
    y=category_paths[x]['Name'].split('.')
    l="subject"
    empty.append('C0001')
    for i in range(1,len(y)-1):
        l=l+'.'+y[i]
        for id in category_paths:
            if category_paths[id]['Name']==l:
                empty.append(id)
    
    category_paths[x]['parents']=empty
    category_paths[x]['h_paths']=0
    category_paths[x]['s_paths']=0
    category_paths[x]['hp_total']=0
    category_paths[x]['sp_total']=0
    

    

cols=['A','B','C','D','E']
df = pd.read_csv("./Data/paths_finished.tsv",sep="\t",names=cols)
df=df[16:]
paths=list(df['D'])
actual_paths={}
i=1;
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
    for y in actual_paths:
        for z in actual_paths[y]['human_path']:
            if x in article_categories[z]:
                category_paths[x]['h_paths']+=1
                for p in category_paths[x]['parents']:
                    category_paths[p]['h_paths']+=1

                break
        
        for z in actual_paths[y]['shortest_path']:
            if x in article_categories[z]:
                category_paths[x]['s_paths']+=1
                for p in category_paths[x]['parents']:
                    category_paths[p]['s_paths']+=1
                
                break
                

    

for x in category_paths:
    for y in actual_paths:
        for z in actual_paths[y]['human_path']:
            if x in article_categories[z]:
                category_paths[x]['hp_total']+=1
                for p in category_paths[x]['parents']:
                    category_paths[p]['hp_total']+=1
                    

        
        for z in actual_paths[y]['shortest_path']:
            if x in article_categories[z]:
                category_paths[x]['sp_total']+=1
                for p in category_paths[x]['parents']:
                    category_paths[p]['sp_total']+=1
                
                
                

with open('./Question9/category-subtree-paths.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Category_ID','Number_of_human_paths_traversed','Number_of_human_times_traversed','Number_of_shortest_paths_traversed','Number_of_shortest_times_traversed'])
    for x in category_paths:
        csv_writer.writerow([x,category_paths[x]['h_paths'],category_paths[x]['hp_total'],category_paths[x]['s_paths'],category_paths[x]['sp_total']])


with open('./Helpers/articles.json', "w") as file_write:
    json.dump(articles, file_write)
    
with open('./Helpers/category_paths.json', "w") as file_write:
    json.dump(category_paths, file_write)
    
with open('./Helpers/actual_paths.json', "w") as file_write:
    json.dump(actual_paths, file_write)


print( "output file category-subtree-paths.csv produced in folder Question9" )