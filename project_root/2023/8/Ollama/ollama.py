import sys
from math import lcm

def solve(input: str):
    lines = input.splitlines()
    directions = lines[0]
    nodes = {}

    def get_node(path):
        if path not in nodes:
            node, _, neighbors = path.split(maxsplit=2)
            nodes[node] = neighbors[1:-1].split(", ")
        return nodes[path]

    part1_steps = 0
    current_path = "AAA"
    for i in range(len(directions) * (len(nodes) // len(set(lines[2:])))):
        if current_path == "ZZZ":
            break
        direction = directions[i % len(directions)]
        current_path = get_node(current_path)[0 if direction == 'L' else 1]
        part1_steps += 1

    def part2_steps(start):
        steps = 0
        for i in range(len(directions) * (len(nodes) // len(set(lines[2:])))):
            if start.endswith('Z'):
                return steps
            direction = directions[i % len(directions)]
            start = get_node(start)[0 if direction == 'L' else 1]
            steps += 1

    starting_paths = [path for path in nodes.keys() if path.endswith("A")]
    all_z_steps = (part2_steps(path) for path in starting_paths)
    part2_result = lcm(*all_z_steps)

    return f"{part1_steps} {part2_result}"

text = open(sys.argv[1]).read()
print(solve(text))