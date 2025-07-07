import sys
from collections import defaultdict
from heapq import heappush, heappop
from itertools import pairwise

def parse_input(text):
    M = defaultdict(set)
    for line in text.strip().splitlines():
        src, dst = line.split(': ')
        for de in dst.split():
            M[src].add(de)
            M[de].add(src)
    return M

def bfs(start, M, exclusions):
    visited = {start}
    parent = {}
    heap = [(0, start)]
    stop = start
    hp = heappop; hpush = heappush; ML = M; excl = exclusions
    visited_add = visited.add; visited_contains = visited.__contains__; p_set = parent.__setitem__
    while heap:
        d, node = hp(heap)
        stop = node
        for nb in ML[node]:
            if (node, nb) in excl or visited_contains(nb): continue
            visited_add(nb)
            p_set(nb, node)
            hpush(heap, (d+1, nb))
    return len(visited), parent, stop

def part1(text):
    M = parse_input(text)
    start = next(iter(M))
    total = len(M)
    b = bfs
    _, parent, stop = b(start, M, frozenset())
    path = [stop]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    for s1, d1 in pairwise(path):
        e1 = frozenset(((s1, d1), (d1, s1)))
        _, parent2, _ = b(start, M, e1)
        path2 = [stop]
        while path2[-1] != start:
            path2.append(parent2[path2[-1]])
        path2.reverse()
        for s2, d2 in pairwise(path2):
            e2 = e1 | frozenset(((s2, d2), (d2, s2)))
            _, parent3, _ = b(start, M, e2)
            path3 = [stop]
            while path3[-1] != start:
                path3.append(parent3[path3[-1]])
            path3.reverse()
            for s3, d3 in pairwise(path3):
                e3 = e2 | frozenset(((s3, d3), (d3, s3)))
                rcount, _, _ = b(start, M, e3)
                if rcount != total:
                    return rcount * (total - rcount)
    return "No 3-edge cut found"

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)}")