import sys
from collections import defaultdict, deque

def parse_input(text):
    M = defaultdict(set)
    for line in text.strip().splitlines():
        src, dst = line.split(': ')
        connections = dst.split()
        M[src].update(connections)
        for de in connections:
            M[de].add(src)
    return M

def bfs(start, M, exclusions=frozenset()):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for de in M[node]:
            if (node, de) in exclusions or de in visited:
                continue
            visited.add(de)
            queue.append((de, dist + 1))
    return len(visited)

def part1(text):
    M = parse_input(text)
    start = next(iter(M))
    initial_length = bfs(start, M)

    for s1 in M:
        for d1 in M[s1]:
            exclusions1 = frozenset({(s1, d1), (d1, s1)})
            visited2_length = bfs(start, M, exclusions1)

            if visited2_length == initial_length:
                continue

            for s2 in M:
                for d2 in M[s2]:
                    if (s2, d2) in exclusions1:
                        continue
                    exclusions2 = exclusions1 | frozenset({(s2, d2), (d2, s2)})
                    visited3_length = bfs(start, M, exclusions2)

                    if visited3_length == initial_length:
                        continue

                    for s3 in M:
                        for d3 in M[s3]:
                            if (s3, d3) in exclusions2:
                                continue
                            exclusions3 = exclusions2 | frozenset({(s3, d3), (d3, s3)})
                            lena = bfs(start, M, exclusions3)
                            if lena != len(M):
                                return lena * (len(M) - lena)

    return "No 3-edge cut found"

if __name__ == '__main__':
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)}")