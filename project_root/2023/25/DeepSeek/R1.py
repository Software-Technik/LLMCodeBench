import sys
from collections import deque, defaultdict
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
    dist = {start: 0}
    parent = {start: None}
    q = deque([start])
    max_dist = 0
    farthest = start
    while q:
        node = q.popleft()
        if dist[node] > max_dist:
            max_dist = dist[node]
            farthest = node
        for neighbor in M[node]:
            if (node, neighbor) in exclusions:
                continue
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                parent[neighbor] = node
                q.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest = neighbor
    path = []
    cur = farthest
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return len(dist), path, farthest

def part1(text):
    M = parse_input(text)
    start = next(iter(M))
    _, path1, stop = bfs(start, M)

    for s1, d1 in pairwise(path1):
        exclusions1 = {(s1, d1), (d1, s1)}
        _, path2, _ = bfs(start, M, exclusions1)
        for s2, d2 in pairwise(path2):
            exclusions2 = exclusions1 | {(s2, d2), (d2, s2)}
            _, path3, _ = bfs(start, M, exclusions2)
            for s3, d3 in pairwise(path3):
                exclusions3 = exclusions2 | {(s3, d3), (d3, s3)}
                lena, _, _ = bfs(start, M, exclusions3)
                if lena != len(M):
                    return lena * (len(M) - lena)

    return "No 3-edge cut found"

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)}")