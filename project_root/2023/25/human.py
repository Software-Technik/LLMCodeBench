import sys
from collections import defaultdict
from heapq import heappop, heappush
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
    visited = {start: (0, [start])}
    heap = [(0, start, [start])]
    while heap:
        dist, node, path = heappop(heap)
        for de in M[node]:
            if (node, de) in exclusions:
                continue
            if de not in visited:
                visited[de] = (dist + 1, path + [de])
                heappush(heap, (dist + 1, de, path + [de]))
    return len(visited), visited, node

def part1(text):
    M = parse_input(text)
    start = next(iter(M))
    _, visited, stop = bfs(start, M)

    for s1, d1 in pairwise(visited[stop][1]):
        exclusions1 = {(s1, d1), (d1, s1)}
        _, visited2, _ = bfs(start, M, exclusions1)
        for s2, d2 in pairwise(visited2[stop][1]):
            exclusions2 = exclusions1 | {(s2, d2), (d2, s2)}
            _, visited3, _ = bfs(start, M, exclusions2)
            for s3, d3 in pairwise(visited3[stop][1]):
                exclusions3 = exclusions2 | {(s3, d3), (d3, s3)}
                lena, _, _ = bfs(start, M, exclusions3)
                if lena != len(M):
                    return lena * (len(M) - lena)

    return "No 3-edge cut found"

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)}")