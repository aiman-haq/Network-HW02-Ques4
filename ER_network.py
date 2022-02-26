import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# set of n and p, we have used these three pair of n and p
# paris used are: (100,0.06), (70, 0.12), (200, 0.67)

set_n = [100, 70, 200]
set_p = [0.06, 0.12, 0.67]


# randomly choosing n and p from the set we have provided
def choosing_n_p(set_n):
    n = random.choice(set_n)
    if n == 100:
        p = set_p[0]
    if n == 70:
        p = set_p[1]
    if n == 200:
        p = set_p[2]
    return(n,p)

# helper function to take the averages
def Average(lst):
	return round(sum(lst) / len(lst),3)

#setting n and p, you can comment this to assign you own n and p
(n,p) = choosing_n_p(set_n)
# n = 200
# p = 0.67

# G is our graph network 
G= nx.erdos_renyi_graph(n,p)
# initiallizing lists to append all 30 different values for each value pair of n and p
apl_lst= []
Avg_deg_lst =[]
Avg_CC_lst= []

# running each configuration 30 times
for i in range(30):
    G= nx.erdos_renyi_graph(n,p)
    #calculating average degree
    G_deg = nx.degree_histogram(G)
    G_deg_sum = [a * b for a, b in zip(G_deg, range(0, len(G_deg)))]
    avg_degree = sum(G_deg_sum) / G.number_of_nodes()
    Avg_deg_lst.append(avg_degree)

    
    # condition added to avoid getting invalid values of apl 
    if nx.is_connected(G):
        # calculating APL
        apl = nx.average_shortest_path_length(G)
        apl_lst.append(apl)
        # calculating apl
        G_cluster = sorted(list(nx.clustering(G).values()))
        ACC = Average(G_cluster)
        Avg_CC_lst.append(ACC)
        
# printing values of average degree, APL, Avg cluster coefficients of given n and p
print("Average degree for n = ",n, "and p = ",p, "is :", Average(Avg_deg_lst))
print("Average Path Length for n = ",n, "and p = ",p, "is :", Average(apl_lst))
print("Average Cluster Coefficient for n = ",n, "and p = ",p, "is :", Average(Avg_CC_lst))

# finding degree sequence to plot degree distribution histogram
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)

# plotting histograms
fig = plt.figure("Degree distribution of a Erdos-Renyi Network", figsize=(7, 7))
ax2 = fig.add_subplot()
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("Degree histogram")
ax2.set_xlabel("Degree")
ax2.set_ylabel("number of Nodes")

plt.show()
