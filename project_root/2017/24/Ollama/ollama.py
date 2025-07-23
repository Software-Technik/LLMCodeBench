import sys

def parse_input(filepath):
    with open(filepath) as f:
        connections = [(tuple(map(int, line.split("/")))) for line in f if (line := line.strip())]
    return {a: b for a, b in connections}, {a for a, b in connections if a == b}

def calc_score(path, doubles):
    score = sum(2 * n - (n == path[-1]) or 0, 2 * n if n not in doubles else 3 * n)
    return len(path), score

def solve(connections, doubles):
    max_score, longest_strongest = 0, (0, 0)

    def dfs(path, current_node):
        nonlocal max_score, longest_strongest
        next_node = connections[current_node]
        if next_node not in path:
            path.append(next_node)
            length, score = calc_score(path, doubles)
            longest_strongest = max(longest_strongest, (length, score))
            longest_path = dfs(path, next_node)
            if longest_strongest < (len(path), calc_score(path, doubles)[1]):
                max_score = max(max_score, longest_strongest[0])
            path.pop()
        return (len(path), sum(2 * n or 3 * n for n in path) - path[-1])

    dfs([0], 0)
    return max_score, longest_strongest[1]

input_file = sys.argv[1]
connections, doubles = parse_input(input_file)
part1, part2 = solve(connections, doubles)

print(part1)
print(part2)