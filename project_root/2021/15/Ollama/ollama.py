import numpy as np
import networkx as nx

def dijkstra(cost, row_idx, col_idx):
    w, h = len(cost), len(cost[0])
    G = nx.grid_2d_graph(w, h, create_using=nx.DiGraph())
    nx.set_edge_attributes(G, {e: cost[e[1][0]][e[1][1]] for e in G.edges()}, "cost")
    return nx.shortest_path_length(G, source=(row_idx, col_idx), target=(w - 1, h - 1), weight="cost")

def part1(data):
    df = np.array([[int(x) for x in line ] for line in data.splitlines()])
    return dijkstra(df, 0, 0)

def part2(data):
    df = np.array([[int(c) - 1 for c in line] for line in data.splitlines() % 9 + 1 for i in range(5)]
    row = np.hstack([(df + i - 1) % 9 + 1 for i in range(5)])
    df = np.vstack([(row + i - 1) % 9 + 1 for i in range(5)])
    max_cost, min_cost = np.max(df), np.min(df)
    w, h = len(cost), len(cost[0])
    G = nx.grid_2d_graph(w + 4, h + 4, create_using=nx.DiGraph())
    edge_attributes = {e: -1 for e in G.edges()}
    for (r, c) in product(range(5), repeat=2):
        G.nodes[(r * w, c * h)]["cost"] = df[r][c]
        G.add_edge((r * w + 4, c * h + 4), None)
    return dijkstra(cost, 0, 0)

with open(sys.argv[1]) as f:
    data = f.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")