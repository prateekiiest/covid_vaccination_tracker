import networkx as nx
import community
import matplotlib.pyplot as plt
from sklearn.metrics.cluster import normalized_mutual_info_score
from numpy.random import choice

def utility(node_i,S, G):
    total_utility = 0
    k_i = G.degree[node_i]
    for node_j in S:
        if node_i != node_j:
            curr_edges = A[node_i][node_j]

            k_j = G.degree[node_j]
            m = G.number_of_edges()
            degree_prod = (k_i*k_j)/(2.0*m)

            indiv_utility = curr_edges - degree_prod
            total_utility += indiv_utility
    return total_utility

# %% [code]
def partitionModularity(mod_list,G):
    totalModularity = 0
    for node_i in range(G.number_of_nodes()):
        totalModularity += utility(node_i,np.where(mod_list==mod_list[node_i])[0],G)
    return (totalModularity/(G.number_of_edges()*2.0))



## we show a simple calculation of modularity w.r.t karate dataset

G = nx.karate_club_graph()
nx.draw(G)


totalEdges = G.number_of_edges()
totalNodes= G.number_of_nodes()
A = nx.to_numpy_array(G)
# %% [code]

# considering only 3 communities (analogy with 3 wards) = C1,C2,C3
S = np.array([("C" + str(choice(3))) for i in range(G.number_of_nodes())])
nodesList = [node_k for node_k in range(G.number_of_nodes())]

partitionModularity(S, G)