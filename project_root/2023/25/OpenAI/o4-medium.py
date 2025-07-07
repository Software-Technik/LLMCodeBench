import sys
from collections import defaultdict, deque

def parse_input(text):
    M = defaultdict(list)
    for line in text.strip().splitlines():
        src, dst = line.split(': ')
        for de in dst.split():
            M[src].append(de)
            M[de].append(src)
    return M

def bfs(start, M, excl):
    visited = {start}
    parent = {start: None}
    dq = deque([(start, 0)])
    farthest = start
    maxd = 0
    while dq:
        node, d = dq.popleft()
        if d > maxd:
            maxd = d
            farthest = node
        for nei in M[node]:
            if (node, nei) in excl or nei in visited:
                continue
            visited.add(nei)
            parent[nei] = node
            dq.append((nei, d + 1))
    return len(visited), parent, farthest

def part1(text):
    M = parse_input(text)
    n = len(M)
    start = next(iter(M))
    _, parent1, stop1 = bfs(start, M, set())
    path1 = []
    node = stop1
    while node is not None:
        path1.append(node)
        node = parent1[node]
    path1.reverse()
    for i in range(len(path1) - 1):
        s1, d1 = path1[i], path1[i + 1]
        excl1 = {(s1, d1), (d1, s1)}
        _, parent2, stop2 = bfs(start, M, excl1)
        path2 = []
        node = stop2
        while node is not None:
            path2.append(node)
            node = parent2[node]
        path2.reverse()
        for j in range(len(path2) - 1):
            s2, d2 = path2[j], path2[j + 1]
            excl2 = excl1 | {(s2, d2), (d2, s2)}
            _, parent3, stop3 = bfs(start, M, excl2)
            path3 = []
            node = stop3
            while node is not None:
                path3.append(node)
                node = parent3[node]
            path3.reverse()
            for k in range(len(path3) - 1):
                s3, d3 = path3[k], path3[k + 1]
                excl3 = excl2 | {(s3, d3), (d3, s3)}
                lena, _, _ = bfs(start, M, excl3)
                if lena != n:
                    return lena * (n - lena)
    return "No 3-edge cut found"

if __name__ == "__main__":
    text = open(sys.argv[1]).read()
    print(part1(text))