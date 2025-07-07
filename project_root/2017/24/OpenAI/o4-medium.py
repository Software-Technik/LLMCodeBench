import sys
from collections import defaultdict

def parse_input(filepath):
    with open(filepath) as f:
        return [tuple(map(int, line.strip().split("/"))) for line in f if line.strip()]

def solve(connections):
    adjacency = defaultdict(list)
    for i, (a, b) in enumerate(connections):
        adjacency[a].append(i)
        adjacency[b].append(i)
    max_strength = 0
    max_len = 0
    max_strength_at_max_len = 0

    def dfs(port, visited_mask, length, strength):
        nonlocal max_strength, max_len, max_strength_at_max_len
        found = False
        for i in adjacency.get(port, ()):
            if not (visited_mask >> i) & 1:
                found = True
                a, b = connections[i]
                next_port = b if a == port else a
                dfs(next_port, visited_mask | (1 << i), length + 1, strength + a + b)
        if not found:
            if strength > max_strength:
                max_strength = strength
            if length > max_len or (length == max_len and strength > max_strength_at_max_len):
                max_len = length
                max_strength_at_max_len = strength

    dfs(0, 0, 0, 0)
    return max_strength, max_strength_at_max_len

if __name__ == "__main__":
    connections = parse_input(sys.argv[1])
    part1, part2 = solve(connections)
    print(part1)
    print(part2)