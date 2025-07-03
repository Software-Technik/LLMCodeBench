import sys
import networkx

def part1(data):
    entries = list(map(lambda x: (x.split(")")[0], x.split(")")[1]), data))

    orbits = dict()

    for a,b in entries:
        if a in orbits: orbits[a].add(b)
        else: orbits[a] = set([b])

    keepGoing = True
    loop = 0

    while keepGoing:
        keepGoing = False
        loop += 1

        for keyA in orbits:
            for val in orbits[keyA].copy():
                if not val in orbits:
                    continue
                for candidate in orbits[val]:
                    if candidate != val and candidate not in orbits[keyA]:
                        keepGoing = True
                        orbits[keyA].add(candidate)

    return sum(map(len, orbits.values())) 

def part2(data):
    entries = list(map(lambda x: x.split(")"), data))
    graph = networkx.Graph()
    graph.add_edges_from(entries)
    return networkx.shortest_path_length(graph, "YOU", "SAN") - 2

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")