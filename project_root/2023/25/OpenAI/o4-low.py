import sys
from collections import defaultdict, deque

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
    parent = {}
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in M[node]:
            if (node, nei) in exclusions or nei in dist:
                continue
            dist[nei] = dist[node] + 1
            parent[nei] = node
            q.append(nei)
    count = len(dist)
    stop = max(dist, key=dist.get)
    path = []
    cur = stop
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    path.reverse()
    return count, dist, parent, stop, path

def part1(text):
    M = parse_input(text)
    start = next(iter(M))
    _, _, _, stop, path1 = bfs(start, M)
    n = len(M)
    for i in range(len(path1)-1):
        s1, d1 = path1[i], path1[i+1]
        exc1 = {(s1,d1),(d1,s1)}
        _, _, _, stop2, path2 = bfs(start, M, exc1)
        for j in range(len(path2)-1):
            s2, d2 = path2[j], path2[j+1]
            exc2 = exc1 | {(s2,d2),(d2,s2)}
            _, _, _, stop3, path3 = bfs(start, M, exc2)
            for k in range(len(path3)-1):
                s3, d3 = path3[k], path3[k+1]
                exc3 = exc2 | {(s3,d3),(d3,s3)}
                cnt, *_ = bfs(start, M, exc3)
                if cnt != n:
                    return cnt * (n - cnt)
    return "No 3-edge cut found"

if __name__ == "__main__":
    text = open(sys.argv[1]).read()
    print(part1(text))