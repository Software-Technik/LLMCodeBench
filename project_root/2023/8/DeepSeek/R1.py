import sys
import math

def part1(text: str) -> int:
    lines = text.splitlines()
    directions_str = lines[0]
    directions = [0 if d == 'L' else 1 for d in directions_str]
    nodes = {}
    for line in lines[2:]:
        node, _, neighbors = line.split(maxsplit=2)
        neighbors = neighbors[1:-1].split(", ")
        nodes[node] = neighbors

    current_node = "AAA"
    direction_index = 0
    total = 0
    n_directions = len(directions)
    while current_node != "ZZZ":
        neighbors = nodes[current_node]
        current_node = neighbors[directions[direction_index]]
        direction_index = (direction_index + 1) % n_directions
        total += 1
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    directions_str = lines[0]
    directions = [0 if d == 'L' else 1 for d in directions_str]
    nodes = {}
    start_nodes = []
    for line in lines[2:]:
        node, _, neighbors = line.split(maxsplit=2)
        neighbors = neighbors[1:-1].split(", ")
        nodes[node] = neighbors
        if node.endswith("A"):
            start_nodes.append(node)

    z_indexes = []
    n_directions = len(directions)
    for start_node in start_nodes:
        current_node = start_node
        steps = 0
        direction_index = 0
        while not current_node.endswith("Z"):
            neighbors = nodes[current_node]
            current_node = neighbors[directions[direction_index]]
            direction_index = (direction_index + 1) % n_directions
            steps += 1
        z_indexes.append(steps)

    return math.lcm(*z_indexes)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")