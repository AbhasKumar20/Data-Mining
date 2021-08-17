
import pandas as pd
import csv
import json


df = pd.read_csv("./Data/articles.tsv",sep="\t")
articles={}
empty=[]
for x in range(1,4605):
    articles[df['# The list of all articles.'][10+x-1]]={}
    articles[df['# The list of all articles.'][10+x-1]]['id']='A'+(str(x)).zfill(4)
    articles[df['# The list of all articles.'][10+x-1]]['category']=list(empty)



cols=['A','B']
df = pd.read_csv("./Data/categories.tsv",sep="\t",names=cols)

categories=list(df['B'][12:])
category=[]
for x in categories:
    category.append(x.split(','))

category_mapping={}
category_mapping['subject']='C0001'

level_2=[]
level_3=[]
level_4=[]


for x in category:
    x=x[0].split('.')
    if len(x)==2:
        y=x[0]+'.'+x[1]
        if y not in level_2:
            level_2.append(y)
    if len(x)==3:
        y=x[0]+'.'+x[1]
        if y not in level_2:
            level_2.append(y)
        y=y+'.'+x[2]
        if y not in level_3:
            level_3.append(y)
    
    if len(x)==4:
        y=x[0]+'.'+x[1]
        if y not in level_2:
            level_2.append(y)
        y=y+'.'+x[2]
        if y not in level_3:
            level_3.append(y)
        y=y+'.'+x[3]
        if y not in level_4:
            level_4.append(y)

num=1
Levels=[sorted(level_2),sorted(level_3),sorted(level_4)]
for x in Levels:
    for i in range(len(x)):
        num=num+1
        category_mapping[x[i]]='C'+(str(num)).zfill(4)



df=df.iloc[12: ]
for x,y in zip(df['A'],df['B']):
    articles[x]['category'].append(category_mapping[y])
    
for x in articles:
    if len(articles[x]['category'])==0:
        articles[x]['category'].append('C0001')
    

with open('./Question3/article-categories.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Article_ID','Category_IDs'])
    for x in articles:
        if len(articles[x]['category'])==1:
            csv_writer.writerow([articles[x]['id'],articles[x]['category'][0]])
        else:
            
            csv_writer.writerow([articles[x]['id'],articles[x]['category']])
        
        


with open('./Helpers/articles.json', "w") as file_write:
    json.dump(articles, file_write)

print("output_file article-categories.csv produced in folder Question3.")