import random
import  array,queue
def generate_connected_graph(n:int,m:int):
    '''

    :param n: number of vertices
    :param m: number of edges
    :return: random generated an connected graph with n vertices and
             m edges represented by adjacent matrix
    '''

    min_edges = n - 1
    if m < min_edges:
        raise ValueError('num_edges less than minimum (%i)' % min_edges)
    # Check max edges
    max_edges = n * (n - 1) /2
    if m > max_edges:
        raise  ValueError('num_edges more than maximum (%i)' % max_edges)

    graph_adjacent_matrix = [[0 for i in range(n)] for j in range(n)]

    nodes = list(range(n))

    # generate a random path contains all nodes
    node_current = random.choice(nodes)
    graph_edge = []
    for count in range(n-1):
        nodes.remove(node_current)
        node_next = random.choice(nodes)
        graph_adjacent_matrix[node_current][node_next] = 1
        graph_adjacent_matrix[node_next][node_current] = 1
        graph_edge.append((node_current,node_next))
        node_current = node_next
    edges = []

    for i in range(n-1):
        for j in range(i+1,n):
            if graph_adjacent_matrix[i][j] !=1:
                edges.append((i,j))

    count_edges = n-1
    while count_edges < m:
        edge = random.choice(edges)
        #print(edge)
        if edge[0] != edge[1] and graph_adjacent_matrix[edge[0]][edge[1]] !=1:
            edges.remove(edge)
            graph_edge.append(edge)
            graph_adjacent_matrix[edge[0]][edge[1]] = 1
            graph_adjacent_matrix[edge[1]][edge[0]] = 1
            count_edges = count_edges+1
        #print(graph_adjacent_matrix)
    return graph_adjacent_matrix,graph_edge

def BFS(adjacent_matrix:list):
    bfs_tree = []
    visited = []
    q = queue.Queue()
    num_nodes = len(adjacent_matrix)
    root = random.randint(0,num_nodes-1)
    q.put(root)
    visited.append(root)
    bfs_tree.append((root,root))
    level_dict = dict()
    level_dict[root] = 0
    count_level= 1
    while not q.empty() and len(visited) != num_nodes:
        curr_node = q.get()
        level = []
        for i in range(num_nodes):
            if adjacent_matrix[curr_node][i] ==1 and i not in visited:
                level_dict[i] = count_level
                visited.append(i)
                level.append((curr_node,i))
                q.put(i)
        count_level = count_level+1
        bfs_tree.append(level)
    return bfs_tree,level_dict







