from utils import BFS,generate_connected_graph
import networkx as nx
import matplotlib.pyplot as plt
import  matplotlib as mpl

def acyclicOrientation(graph:list):

    '''
    given a graph, generate the acyclic Orientation of the graph  by using the BFS
    :param graph:
    :return:
    '''
    num_nodes = len(graph)
    bfs_tree, level_dict = BFS(graph)
    orientation = []

    for i in range(num_nodes-1):
        for j in range(i+1,num_nodes):
            if graph[i][j] ==1:
                level1 = level_dict.get(i)
                level2 = level_dict.get(j)
                if level1 == level2:
                    orientation.append((i,j))
                elif level1 > level2:
                    orientation.append((i,j))
                else:
                    orientation.append((j,i))
    return  orientation

if __name__ == "__main__":
    #set your number of nodes and edges here
    graph,edges = generate_connected_graph(12,17)
    orientation = acyclicOrientation(graph)

    G_original = nx.Graph()
    G_original.add_edges_from(edges)
    G_orientation = nx.DiGraph()
    G_orientation.add_edges_from(orientation)


    pos = nx.circular_layout(G_orientation)
    nodes = nx.draw_networkx_nodes(G_orientation, pos,node_color='red')
    edges = nx.draw_networkx_edges(G_orientation, pos,arrowstyle='->',arrows=True,arrowsize=10,edge_cmap=plt.cm.Blues, width=2)



    plt.show()

