import pandas as pd

data = pd.read_excel(path, sheetname = "sheetname")
data = pd.DataFrame(data)

# sort data with lift over 1
data['Lift'] = data['lift'].apply(lambda x: x)
data = data [data['Lift'] >= 1]
data = data.sort_values(by = ['Lift'])

# liberizing frozenset of apriori result
lst1 = []
lst2 = []
for i in list(data.index):
    a = data['antecedents'][i]
    a = a.replace("frozenset","")
    a = a.replace("(","")
    a = a.replace("{","")
    a = a.replace("'","")
    a = a.replace(")","")
    a = a.replace("}","")
    lst1.append(a)
    b = data['consequents'][i]
    b = b.replace("frozenset","") 
    b = b.replace("(","")
    b = b.replace("{","")
    b = b.replace("'","")
    b = b.replace("}","")
    b = b.replace(")","")
    lst2.append(b)
data['Antecedents'] = lst1
data['Consequents'] = lst2
data.drop(['antecedents', 'consequents', 'length', 'length2'], axis = 1) # delete the old (frozenset) item columns

# Visualization - using networkx
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def draw_graph(rules):
    G = nx.DiGraph()
      
    ## Setting Node Name
    for i in list(rules.index):
        a = rules['Antecedents'][i]
        b = rules['Consequents'][i]
        c = rules['lift'][i]
        G.add_edge(a, b, weight = c)
    
    ## Setting Node Size
    #def nodesize():
    #    lst = []
    #    for (u,v,d) in G.edges(data=True):
    #        support1 = list(data['antecedent support'][data['Antecedents'] == u])[0] * 20000 #this value for bigger node_size
    #        support2 = list(data['consequent support'][data['Consequents'] == v])[0] * 20000
    #        support = (support1, support2)
    #        lst.append(support)
    #    return lst
    
    ## Setting Graph variables
    pos = nx.spring_layout(G)
    edges = G.edges()
    # node_size = list(data['support'] * 50000)
    labels = [[(u,v) for (u, v, d) in G.edges(data=True)]]
    weights = [d['weight'] for (u, v, d) in G.edges(data=True)]
    edge_labels = { (u,v): round(d['weight'],3) for u,v,d in G.edges(data=True) }
    
    ## Labeling node name as Korean
    import matplotlib.font_manager as fm

    font_location = "C:/Users/user/Desktop/08SeoulNamsanB.ttf" 
    font_name = fm.FontProperties(fname = font_location).get_name()
    matplotlib.rc('font', family = font_name)
    
    ## Drawing Graph
    nx.draw_networkx_nodes(G, pos, node_color = 'yellow', node_size = 3000)
    nx.draw_networkx_edges(G, pos, edgelist = edges, edge_color = 'black', width = weights)
    nx.draw_networkx_edge_labels(G, pos, font_size = 20, edge_labels = edge_labels)
    nx.draw_networkx_labels(G, pos, font_size = 20, font_family = "08SeoulNamsan")
    # nx.draw_networkx_edges(G, pos, alpha=0.5, style='dashed')

    data.head()
    plt.axis('off')
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(10, 10)
    plt.show()
    fig.savefig("C:/Users/user/Desktop/연관분석 시각화/Impactamin graph - Premium.png")
 
 draw_graph(data)
