
import pandas as pd
import csv


df = pd.read_csv("./Data/articles.tsv",sep="\t")
articles={}
empty=[]
for x in range(1,4605):
    articles[df['# The list of all articles.'][10+x-1]]={}
    articles[df['# The list of all articles.'][10+x-1]]['id']='A'+(str(x)).zfill(4)
    articles[df['# The list of all articles.'][10+x-1]]['category']=list(empty)


with open('./Question1/article-ids.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Article_Name','Article_ID'])
    for x in articles:
        csv_writer.writerow([x,articles[x]['id']])

print("Output file article-ids.csv produced in folder Question1 ")