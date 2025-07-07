import sys
import math

def part1(text: str) -> int:
    lines = text.splitlines()
    directions = lines[0]
    nodes = {line.split(maxsplit=2)[0]: line.split(maxsplit=2)[2][1:-1].split(", ") for line in lines[2:]}

    current_node = "AAA"
    direction_index, total = 0, 0

    while current_node != "ZZZ":
        neighbors = nodes[current_node]
        direction = directions[direction_index] == "R"
        current_node = neighbors[direction]
        direction_index = (direction_index + 1) % len(directions)
        total += 1

    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    directions = lines[0]
    nodes = {line.split(maxsplit=2)[0]: line.split(maxsplit=2)[2][1:-1].split(", ") for line in lines[2:]}

    start_nodes = [node for node in nodes if node.endswith("A")]
    z_indexes = []

    for start_node in start_nodes:
        current_node = start_node
        steps, direction_index = 0, 0

        while not current_node.endswith("Z"):
            neighbors = nodes[current_node]
            direction = directions[direction_index] == "R"
            current_node = neighbors[direction]
            direction_index = (direction_index + 1) % len(directions)
            steps += 1

        z_indexes.append(steps)

    return math.lcm(*z_indexes)

input_file = sys.argv[1]
with open(input_file) as f:
    text = f.read()

sys.stdout.write(f"{part1(text)} {part2(text)}")