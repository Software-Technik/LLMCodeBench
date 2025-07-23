import sys
from collections import defaultdict, deque
from itertools import pairwise

def parse_input(text):
    M = defaultdict(set)
    for line in text.strip().splitlines():
        src, dst = line.split(': ')
        for de in dst.split():
            M[src].add(de)
            M[de].add(src)
    return M

def bfs(start, M, exclusions=set()):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for de in M[node]:
            if (node, de) in exclusions or (de, node) in exclusions:
                continue
            if de not in visited:
                visited.add(de)
                queue.append(de)
    return len(visited)

def part1(text):
    M = parse_input(text)
    nodes = list(M.keys())
    start = nodes[0]

    def find_path(start, M, exclusions):
        parent = {}
        queue = deque([start])
        parent[start] = None
        found = None
        while queue:
            node = queue.popleft()
            for de in M[node]:
                if (node, de) in exclusions or (de, node) in exclusions:
                    continue
                if de not in parent:
                    parent[de] = node
                    queue.append(de)
                    if de == nodes[-1]:
                        found = de
                        break
            if found is not None:
                break
        path = []
        if found is not None:
            current = found
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
        return path

    path = find_path(start, M, set())
    if not path:
        return "No path found"

    for s1, d1 in pairwise(path):
        exclusions1 = {(s1, d1), (d1, s1)}
        path2 = find_path(start, M, exclusions1)
        if not path2:
            continue
        for s2, d2 in pairwise(path2):
            exclusions2 = exclusions1 | {(s2, d2), (d2, s2)}
            path3 = find_path(start, M, exclusions2)
            if not path3:
                continue
            for s3, d3 in pairwise(path3):
                exclusions3 = exclusions2 | {(s3, d3), (d3, s3)}
                lena = bfs(start, M, exclusions3)
                if lena != len(M):
                    return lena * (len(M) - lena)

    return "No 3-edge cut found"

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)}")