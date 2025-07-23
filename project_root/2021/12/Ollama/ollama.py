import sys

def find_path(current_node, visited_small, repeat, path_count):
    if current_node == "end":
        return 1
    paths = 0
    for neighbor in edges[current_node]:
        if neighbor.isupper() or neighbor not in visited_small:
            paths += find_path(neighbor, visited_small | {neighbor} if neighbor.islower() else visited_small, repeat, path_count)
        elif repeat and neighbor in visited_small:
            paths += find_path(neighbor, visited_small, False, path_count)
    return paths

def part1():
    return find_path("start", {"start"}, True, 0)

def part2():
    return find_path("start", {"start"}, False, 0)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]
    from collections import defaultdict
    edges = defaultdict(set)
    for a, b in (line.split("-") for line in data):
        if a != "end":
            edges[a].add(b)
        if b != "start":
            edges[b].add(a)

sys.stdout.write(f"{part1()} {part2()}")