import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import cm

# network graph (Chatgpt designed)
def similarity_network(data, labels=None, threshold=0.5, node_size=500, figsize=(10, 10)):
    sim = np.array(data)
    n = sim.shape[0]  
    if labels is None:
        labels = list(range(n))

    G = nx.Graph()
    G.add_nodes_from(labels)

    # 
    for i in range(n):
        for j in range(i+1, n):
            s = sim[i, j]
            if s >= threshold:
                G.add_edge(labels[i], labels[j], weight=s)

    plt.figure(figsize=figsize)

    #
    pos = nx.kamada_kawai_layout(G)

    # 
    degrees = dict(G.degree)
    node_sizes = [node_size + degrees[n]*50 for n in G.nodes()]
    node_colors = [degrees[n] for n in G.nodes()]

    #
    cmap_nodes = cm.viridis
    cmap_edges = cm.plasma

    nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors, cmap=cmap_nodes, alpha=0.9, edgecolors='black', linewidths=1.2
    )

    #
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(
        G, pos, width=[(w - threshold + 0.1)*8 for w in weights],
        edge_color=weights, edge_cmap=cmap_edges, alpha=0.7
    )

    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

    plt.title(f"Similarity Network (threshold = {threshold})", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("similarity_network.png", dpi=300, bbox_inches='tight')
    plt.close()

