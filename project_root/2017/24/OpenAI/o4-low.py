import sys
from collections import defaultdict

def parse_input(filepath):
    with open(filepath) as f:
        lines = [line.strip() for line in f if line.strip()]
    connections = []
    doubles = set()
    for line in lines:
        a, b = map(int, line.split("/"))
        idx = len(connections)
        connections.append((a, b))
        if a == b:
            doubles.add(a)
    return connections, doubles

def solve(connections, doubles):
    adj = defaultdict(list)
    for i, (a, b) in enumerate(connections):
        adj[a].append((i, b))
        adj[b].append((i, a))
    max_score = 0
    longest_strongest = (0, 0)
    visited = [False]*len(connections)
    path = []

    def calc_score():
        s = sum(2*n for n in path)
        length = len(path)
        used = set()
        for n in path:
            if n in doubles and n not in used:
                s += 2*n
                length += 1
                used.add(n)
        if path:
            s -= path[-1]
        return length, s

    def dfs(current):
        nonlocal max_score, longest_strongest
        for i, nxt in adj[current]:
            if not visited[i]:
                visited[i] = True
                path.append(nxt)
                dfs(nxt)
                path.pop()
                visited[i] = False
        length, score = calc_score()
        if score > max_score: max_score = score
        if (length, score) > longest_strongest: longest_strongest = (length, score)

    dfs(0)
    return max_score, longest_strongest[1]

if __name__ == "__main__":
    inp = sys.argv[1]
    connections, doubles = parse_input(inp)
    p1, p2 = solve(connections, doubles)
    print(p1)
    print(p2)