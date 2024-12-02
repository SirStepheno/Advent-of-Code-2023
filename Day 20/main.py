import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.DiGraph()

with open("Day 20/input_test.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    for line in lines:
        sender, recievers = line.split(" -> ")
        if sender[0] in ["&", "%"]:
            sender = sender[1:]
        recievers = recievers.split(", ")
        for reciever in recievers:
            G.add_edge(sender, reciever)

# Get state of a note
print(G.nodes['a'])

pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, edge_color='black')

plt.show()

def part_one():
    pass

def part_two():
    pass

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))