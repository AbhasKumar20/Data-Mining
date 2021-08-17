
import pandas as pd
import csv

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


with open('./Question2/category-ids.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Category_Name','Category_ID'])
    for x in category_mapping:
        csv_writer.writerow([x,category_mapping[x]])

print("output file category-ids.csv produced in folder Question2.")