import sys
import networkx as nx
import numpy as np

def part1(data):
    df = [[int(x) for x in line] for line in data.splitlines()]
    w, h = len(df), len(df[0])
    G = nx.grid_2d_graph(w, h, create_using=nx.DiGraph())
    nx.set_edge_attributes(G, {e: df[e[1][0]][e[1][1]] for e in G.edges()}, "cost")
    return nx.shortest_path_length(G, source=(0, 0), target=(w - 1, h - 1), weight="cost")

def part2(data):
    df = np.array([[int(x) for x in line] for line in data.splitlines()])
    row = np.hstack([(df + i - 1) % 9 + 1 for i in range(5)])
    df = np.vstack([(row + i - 1) % 9 + 1 for i in range(5)])
    w, h = df.shape
    G = nx.grid_2d_graph(w, h, create_using=nx.DiGraph())
    nx.set_edge_attributes(G, {e: df[e[1][0], e[1][1]] for e in G.edges()}, "cost")
    return nx.shortest_path_length(G, source=(0, 0), target=(w - 1, h - 1), weight="cost")

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")