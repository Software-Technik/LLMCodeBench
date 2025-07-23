import sys
import networkx as nx

def part1(data):
    orbits = {}
    for line in data:
        a, b = line.split(')')
        if a not in orbits: orbits[a] = set()
        orbits[a].add(b)
        if b not in orbits: orbits[b] = set()

    count = 0
    to_visit = ['COM']

    while to_visit:
        current = to_visit.pop()
        count += len(orbits.get(current, set()))
        to_visit.extend(orbits.get(current, set()))

    return count

def part2(data):
    graph = nx.Graph(data.split(')'))
    return nx.shortest_path_length(graph, 'YOU', 'SAN') - 2

data = open(sys.argv[1]).read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")