
import pandas as pd
import csv
import json
import collections

cols=['A','B','C','D','E','F']
df1= pd.read_csv("./Data/paths_unfinished.tsv",sep="\t",names=cols)

with open("./Helpers/articles.json", "r") as read_file:
    articles=json.load(read_file)
    
with open("./Helpers/category_paths.json", "r") as read_file:
    category_paths=json.load(read_file)



unfinished_pairs={}
i=18
for x,y in zip(list(df1['D'][16:]),list(df1['E'][16:])):
    unfinished_pairs['line'+str(i)]={}
    if ';' in x:
        x=x.split(';')[0]
        
        if x in articles.keys():
            unfinished_pairs['line'+str(i)]['source']=articles[x]['category']
    else:
        if x in articles.keys():
            unfinished_pairs['line'+str(i)]['source']=articles[x]['category']
        
    
    if y in articles.keys():
        unfinished_pairs['line'+str(i)]['dest']=articles[y]['category']
    else:
        unfinished_pairs['line'+str(i)]['dest']=['C0001']
    
    i+=1



for x in unfinished_pairs:
    source=[]
    dest=[]
    for y in unfinished_pairs[x]['source']:
        source.append(y)
        source+=category_paths[y]['parents']
    for y in unfinished_pairs[x]['dest']:
        dest.append(y)
        dest+=category_paths[y]['parents']
    
    unfinished_pairs[x]['source']=source
    unfinished_pairs[x]['dest']=dest
    
        

sd_pairs={}
for x in unfinished_pairs:
    for y in unfinished_pairs[x]['source']:
        for z in unfinished_pairs[x]['dest']:
            sd_pairs[(y,z)]={}

cols=['A','B','C','D','E']
df2= pd.read_csv("./Data/paths_finished.tsv",sep="\t",names=cols)


finished_pairs={}
i=17
for x in df2['D'][16:]:
    x=x.split(';')
    finished_pairs['line'+str(i)]={}
    finished_pairs['line'+str(i)]['source']=articles[x[0]]['category']
    finished_pairs['line'+str(i)]['dest']=articles[x[-1]]['category']
    
    i+=1



for x in finished_pairs:
    source=[]
    dest=[]
    for y in finished_pairs[x]['source']:
        source.append(y)
        source+=category_paths[y]['parents']
    for y in finished_pairs[x]['dest']:
        dest.append(y)
        dest+=category_paths[y]['parents']
    
    finished_pairs[x]['source']=source
    finished_pairs[x]['dest']=dest
    

for x in finished_pairs:
    for y in finished_pairs[x]['source']:
        for z in finished_pairs[x]['dest']:
            sd_pairs[(y,z)]={}



actual_finished_paths={}
i=17;
for x in df2['D'][16:]:
    actual_finished_paths['line'+str(i)]={}
    y=x.split(';')
    path=[]
    cat_path=[]
    if '<' in y:
        for item in y:
            if item !='<':
                path.append(item)
            if item =='<':
                path.pop()
        
    else:
        for item in y:
            path.append(item)
            
    for p in path:
        for c in articles[p]['category']:
            cat_path.append(c)
            for m in category_paths[c]['parents']:
                cat_path.append(m)
            
    
    actual_finished_paths['line'+str(i)]['human_path']=list(set(cat_path))
    
    i+=1
    
actual_unfinished_paths={}
i=18;
for x,y in zip(list(df1['D'][16:]),list(df1['E'][16:])):
    actual_unfinished_paths['line'+str(i)]={}
    x=x.split(';')
    path=[]
    cat_path=[]
    if '<' in x:
        for item in x:
            if item !='<':
                path.append(item)
            if item =='<':
                path.pop()
        
    else:
        for item in x:
            path.append(item)
            
    for p in path:
        for c in articles[p]['category']:
            cat_path.append(c)
            for m in category_paths[c]['parents']:
                cat_path.append(m)
            
    if y in articles.keys():
        for c in articles[y]['category']:
            cat_path.append(c)
            for m in category_paths[c]['parents']:
                cat_path.append(m)
    else:
        cat_path.append('C0001')
            
    
    actual_unfinished_paths['line'+str(i)]['human_path']=list(set(cat_path))
    
    i+=1
    
for x in sd_pairs:
    count=0
    for y in actual_finished_paths:
        if (x[0] in actual_finished_paths[y]['human_path']) and (x[1] in actual_finished_paths[y]['human_path']):
            count+=1
    sd_pairs[x]['finished_count']=count
    
    count=0
    for y in actual_unfinished_paths:
        if (x[0] in actual_unfinished_paths[y]['human_path']) and (x[1] in actual_unfinished_paths[y]['human_path']):
            count+=1
    sd_pairs[x]['unfinished_count']=count
    


sd_pairs = collections.OrderedDict(sorted(sd_pairs.items()))
with open('./Question10/category-pairs.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['From_Category','To_Category','Percentage_of_finished_paths','Percentage_of_unfinished_paths'])
    
    for x in sd_pairs:
        c=sd_pairs[x]['finished_count']
        d=sd_pairs[x]['unfinished_count']
        t=c+d
        csv_writer.writerow([x[0],x[1],round((c/t)*100,2),round((d/t)*100,2)])

print("Output file category-pairs.csv produced in folder Question10")