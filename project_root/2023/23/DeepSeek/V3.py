import sys
from collections import deque

sys.setrecursionlimit(10000)

dirs = ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v"))

def part1(text):
    tiles = text.strip().splitlines()
    dimx = len(tiles[0])
    dimy = len(tiles)
    sx, sy = tiles[0].find("."), 0
    fx, fy = tiles[-1].find("."), dimy - 1

    path = [0] * (dimx * dimy)
    stack = [(sx, sy + 1, 1, False)]
    best = 0

    while stack:
        x, y, plen, backtracking = stack.pop()
        if backtracking:
            path[y * dimx + x] = 0
            continue
        if (x, y) == (fx, fy):
            if plen > best:
                best = plen
            continue
        path[y * dimx + x] = 1
        stack.append((x, y, plen, True))
        for dx, dy, dc in dirs:
            nx, ny = x + dx, y + dy
            if (tiles[ny][nx] == "." or tiles[ny][nx] == dc) and not path[ny * dimx + nx]:
                stack.append((nx, ny, plen + 1, False))
    return best

def part2(text):
    tiles = text.strip().splitlines()
    dimx = len(tiles[0])
    dimy = len(tiles)
    sx, sy = tiles[0].find("."), 0
    fx, fy = tiles[-1].find("."), dimy - 1

    branches = {(sx, sy): 0, (fx, fy): 1}
    graph = [[], []]
    visited = set()
    stack = [(sx, sy + 1, (sx, sy), 0, 1)]
    
    while stack:
        x, y, prev, last, steps = stack.pop()
        if (x, y) in visited:
            if (x, y) in branches:
                cur = branches[(x, y)]
                graph[cur].append((last, steps))
                graph[last].append((cur, steps))
            continue
        visited.add((x, y))
        cnt = 0
        neighbors = []
        for dx, dy, _ in dirs:
            nx, ny = x + dx, y + dy
            if tiles[ny][nx] != "#" and (nx, ny) != prev:
                cnt += 1
                neighbors.append((nx, ny))
        if cnt > 1:
            cur = branches[(x, y)] = len(branches)
            graph.append([])
            graph[cur].append((last, steps))
            graph[last].append((cur, steps))
            last = cur
            steps = 0
        for nx, ny in neighbors:
            if (nx, ny) in branches:
                cur = branches[(nx, ny)]
                graph[cur].append((last, steps + 1))
                graph[last].append((cur, steps + 1))
            else:
                stack.append((nx, ny, (x, y), last, steps + 1))

    q = deque([0])
    while q:
        cur = q.popleft()
        for dst, _ in graph[cur]:
            if len(graph[dst]) == 3:
                for t, d in graph[dst]:
                    if t == cur:
                        to_remove = (t, d)
                graph[dst].remove(to_remove)
                q.append(dst)

    best = 0
    stack = [(0, 0, 0)]
    while stack:
        cur, path, steps = stack.pop()
        if cur == 1:
            if steps > best:
                best = steps
            continue
        for dst, add in graph[cur]:
            if not path & (1 << dst):
                stack.append((dst, path | (1 << dst), steps + add))
    return best

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")