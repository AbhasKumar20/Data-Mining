
import pandas as pd
import csv
import json
import collections

with open("./Helpers/articles.json", "r") as read_file:
    articles=json.load(read_file)
    
with open("./Helpers/category_paths.json", "r") as read_file:
    category_paths=json.load(read_file)
    
with open("./Helpers/actual_paths.json", "r") as read_file:
    actual_paths=json.load(read_file)

cols=['A','B','C','D','E']
df2= pd.read_csv("./Data/paths_finished.tsv",sep="\t",names=cols)

i=1;
for x in df2['D'][16:]:
    y=x.split(';')
    cat_source=[]
    cat_dest=[]
    for c in articles[y[0]]['category']:
        cat_source.append(c)
        for m in category_paths[c]['parents']:
            cat_source.append(m)
    for c in articles[y[1]]['category']:
        cat_dest.append(c)
        for m in category_paths[c]['parents']:
            cat_dest.append(m)
            
    
    actual_paths['line'+str(i)]['cat_source']=list(set(cat_source))
    actual_paths['line'+str(i)]['cat_dest']=list(set(cat_dest))
    
    i+=1
    
sd_pairs={}
for x in actual_paths:
    for y in actual_paths[x]['cat_source']:
        for z in actual_paths[x]['cat_dest']:
            sd_pairs[(y,z)]={}



for x in sd_pairs:
    ratios=[]
    for y in actual_paths:
        if (x[0] in actual_paths[y]['cat_source']) and (x[1] in actual_paths[y]['cat_dest']):
            ratios.append(len(actual_paths[y]['human_path'])/len(actual_paths[y]['shortest_path']))
    sd_pairs[x]['avg_ratio']=sum(ratios)/len(ratios)

sd_pairs = collections.OrderedDict(sorted(sd_pairs.items()))
with open('./Question11/category-ratios.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['From_Category','To_Category','Ratio_of_human_to_shortest'])
    
    for x in sd_pairs:
        csv_writer.writerow([x[0],x[1],round(sd_pairs[x]['avg_ratio'],2)])

print("output file category-ratios.csv produced in folder Question11")