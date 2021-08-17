
import json
import csv

with open("./Helpers/articles.json", "r") as read_file:
    articles=json.load(read_file)

SPD_file = open("./Data/shortest-path-distance-matrix.txt",mode='r')
SPD=SPD_file.readlines()

SPD=SPD[17:]
for line,x in zip(SPD,articles):
    edges=[]
    for i in range(4604):
        if line[i]=='1':
            edges.append('A'+str(i+1).zfill(4))
            
    articles[x]['edges']=edges


with open('./Question4/edges.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['From_ArticleID','To_ArticleID'])
    for x in articles:
        for i in range(len(articles[x]['edges'])):
            csv_writer.writerow([articles[x]['id'],articles[x]['edges'][i]])
            

with open('./Helpers/articles.json', "w") as file_write:
    json.dump(articles, file_write)

print("output file edges.csv produced in folder Question4.")