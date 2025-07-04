import sys

def parse_input(filepath):
    with open(filepath) as f:
        lines = [line.strip() for line in f if line.strip()]
    connections = []
    doubles = []
    for line in lines:
        a, b = map(int, line.split("/"))
        if a != b:
            connections.append((a, b))
        else:
            doubles.append(a)
    return connections, doubles

def calc_score(path, doubles):
    score = sum(2 * n for n in path)
    length = len(path)
    used = set()
    for n in path:
        if n in doubles and n not in used:
            score += 2 * n
            length += 1
            used.add(n)
    score -= path[-1] if path else 0
    return length, score

def solve(connections, doubles):
    max_score = 0
    longest_strongest = (0, 0)  # (length, score)
    visited = set()

    def dfs(path, current_node):
        nonlocal max_score, longest_strongest

        for i, (a, b) in enumerate(connections):
            if i in visited:
                continue
            if a == current_node or b == current_node:
                visited.add(i)
                next_node = b if a == current_node else a
                path.append(next_node)
                dfs(path, next_node)
                path.pop()
                visited.remove(i)
        length, score = calc_score(path, doubles)
        max_score = max(max_score, score)
        longest_strongest = max(longest_strongest, (length, score))

    dfs([], 0)
    return max_score, longest_strongest[1]

# ---------- Entrée fichier et exécution ----------
input_file = sys.argv[1]
connections, doubles = parse_input(input_file)
part1, part2 = solve(connections, doubles)

print(part1)
print(part2)