import sys
import networkx as nx

def part1(data):
    orbits = {}
    for line in data:
        a, b = line.split(')')
        if a in orbits:
            orbits[a].add(b)
        else:
            orbits[a] = {b}

    changed = True
    while changed:
        changed = False
        for key in list(orbits.keys()):
            for val in orbits[key].copy():
                if val in orbits:
                    for candidate in orbits[val]:
                        if candidate not in orbits[key]:
                            orbits[key].add(candidate)
                            changed = True
    return sum(len(v) for v in orbits.values())

def part2(data):
    graph = nx.Graph()
    graph.add_edges_from(line.split(')') for line in data)
    return nx.shortest_path_length(graph, "YOU", "SAN") - 2

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
print(f"{part1(data)} {part2(data)}")