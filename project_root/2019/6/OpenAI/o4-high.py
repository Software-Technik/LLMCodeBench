import sys

def part1(data):
    parent = {}
    for line in data:
        a,b = line.split(")")
        parent[b] = a
    total = 0
    for node in parent:
        while node in parent:
            total += 1
            node = parent[node]
    return total

def part2(data):
    parent = {}
    for line in data:
        a,b = line.split(")")
        parent[b] = a
    steps = {}
    node = parent["YOU"]
    d = 0
    while True:
        steps[node] = d
        if node not in parent: break
        node = parent[node]
        d += 1
    node = parent["SAN"]
    d = 0
    while node not in steps:
        node = parent[node]
        d += 1
    return steps[node] + d

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()
    sys.stdout.write(f"{part1(data)} {part2(data)}")