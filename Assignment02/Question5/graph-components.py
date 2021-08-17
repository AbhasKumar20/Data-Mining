

import pandas as pd
import csv
import networkx as nx

G = nx.read_edgelist("./Question4/edges.csv", create_using=nx.DiGraph, nodetype=str,delimiter=',')


df = pd.read_csv("./Question4/edges.csv",sep=",")

components={}
comp_num=0

for comp in nx.strongly_connected_components(G):
    comp_num+=1
    comp=list(comp)
    components[comp_num]={}
    comp_edges=[]
    for x,y in zip(df['From_ArticleID'],df['To_ArticleID']):
        if (x in comp) and (y in comp):
            comp_edges.append((x,y))
    components[comp_num]['edges']=comp_edges
    components[comp_num]['node_count']=len(comp)
    components[comp_num]['edge_count']=len(comp_edges)

for x in components:
    if components[x]['edge_count']>0:
        G = nx.Graph()
        G.add_edges_from(components[x]['edges'])
        components[x]['diameter']=nx.diameter(G, e=None, usebounds=False)
    
    else:
        components[x]['diameter']=0


with open('./Question5/graph-components.csv', mode='w') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Nodes','Edges','Diameter'])
    for x in components:
        csv_writer.writerow([components[x]['node_count'],components[x]['edge_count'],components[x]['diameter']])
        
print("output file graph-components.csv produced in folder Question5.")