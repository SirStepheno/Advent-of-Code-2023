import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.DiGraph()

# Add 10 nodes with 'on' or 'off' state
for i in range(10):
    G.add_node(200, state='on' if i % 2 == 0 else 'off')

# Add edges between nodes
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)]
G.add_edges_from(edges)

# Define positions for nodes
pos = nx.spring_layout(G)

# Define node colors based on their state
# node_colors = ['green' if G.nodes[node]['state'] == 'on' else 'red' for node in G.nodes]

# Get nodes connected to node 0, in right direction
print(list(G.successors(0)))

# Draw the graph
nx.draw(G, pos, with_labels=True, edge_color='black')

# Display the plot
plt.show()