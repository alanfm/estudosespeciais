import networkx as nx
import matplotlib.pyplot as plt

def create_mst_from_edge_list(edge_list):
    G = nx.Graph()

    for edge in edge_list:
        src, dest, weight = edge
        G.add_edge(src, dest, weight=weight)

    mst_edges = nx.minimum_spanning_edges(G, algorithm='kruskal', data=False)
    mst = G.edge_subgraph(mst_edges)

    return mst

def plot_graph(graph):
    pos = nx.spring_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

# Exemplo de uso:
edge_list = [
    [0, 1, 6],
    [0, 2, 7],
    [1, 2, 3],
    [1, 4, 1],
    [2, 3, 1],
    [1, 3, 1],
    [3, 4, 55],
    [3, 5, 10],
    [5, 4, 20],
    [5, 6, 3],
    [2, 6, 4],
    [6, 7, 4],
    [7, 8, 1],
    [7, 9, 10],
    [9, 8, 1],
]

mst = create_mst_from_edge_list(edge_list)
plot_graph(mst)
