import sys
import math

def part1(text: str) -> int:
    lines = text.splitlines()
    directions = lines[0]
    nodes = {}
    for line in lines[2:]:
        node, _, neighbors = line.partition(' ')
        neighbors = neighbors[3:-1].split(', ')
        nodes[node] = neighbors

    current_node = "AAA"
    total = 0
    dir_len = len(directions)
    while current_node != "ZZZ":
        direction = directions[total % dir_len]
        current_node = nodes[current_node][0 if direction == 'L' else 1]
        total += 1
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    directions = lines[0]
    nodes = {}
    start_nodes = []
    for line in lines[2:]:
        node, _, neighbors = line.partition(' ')
        neighbors = neighbors[3:-1].split(', ')
        nodes[node] = neighbors
        if node.endswith('A'):
            start_nodes.append(node)

    z_indexes = []
    dir_len = len(directions)
    for start_node in start_nodes:
        current_node = start_node
        steps = 0
        while not current_node.endswith('Z'):
            direction = directions[steps % dir_len]
            current_node = nodes[current_node][0 if direction == 'L' else 1]
            steps += 1
        z_indexes.append(steps)

    return math.lcm(*z_indexes)

input_file = sys.argv[1]
with open(input_file) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")