import sys

sys.setrecursionlimit(10000)

dirs = ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v"))

def part1(text):
    tiles = text.strip().splitlines()
    dimx = len(tiles[0])
    dimy = len(tiles)
    sx, sy = tiles[0].index("."), 0
    fx, fy = tiles[-1].index("."), dimy - 1

    def dfs1(x, y, path, plen):
        if (x, y) == (fx, fy):
            return plen
        path[y * dimx + x] = 1
        best = 0
        for dx, dy, dc in dirs:
            nx, ny = x + dx, y + dy
            if tiles[ny][nx] in {".", dc} and not path[ny * dimx + nx]:
                best = max(best, dfs1(nx, ny, path, plen + 1))
        path[y * dimx + x] = 0
        return best

    path = [0] * (dimx * dimy)
    return dfs1(sx, sy + 1, path, 1)

def part2(text):
    tiles = text.strip().splitlines()
    dimx = len(tiles[0])
    dimy = len(tiles)
    sx, sy = tiles[0].index("."), 0
    fx, fy = tiles[-1].index("."), dimy - 1

    def dfs2(x, y, visited, prev, last, steps, branches, graph):
        visited.add((x, y))
        cnt = sum(1 for dx, dy, _ in dirs if (nx := x + dx, ny := y + dy) != prev and tiles[ny][nx] != "#")
        if cnt > 1:
            cur = branches[(x, y)] = len(branches)
            graph.append([])
            graph[cur].append((last, steps))
            graph[last].append((cur, steps))
            last = cur
            steps = 0
        for dx, dy, _ in dirs:
            nx, ny = x + dx, y + dy
            if (nx, ny) != prev and (nx, ny) in branches:
                cur = branches[(nx, ny)]
                graph[cur].append((last, steps + 1))
                graph[last].append((cur, steps + 1))
            elif tiles[ny][nx] != "#" and (nx, ny) not in visited:
                dfs2(nx, ny, visited, (x, y), last, steps + 1, branches, graph)

    def dfs3(cur, path, steps, graph):
        if cur == 1:
            return steps
        path |= 1 << cur
        best = 0
        for dst, add in graph[cur]:
            if not path & (1 << dst):
                best = max(best, dfs3(dst, path, steps + add, graph))
        return best

    def bfstrim(start, graph):
        stack = [start]
        while stack:
            next_stack = []
            for cur in stack:
                for dst, _ in graph[cur]:
                    if len(graph[dst]) == 3:
                        for t, d in graph[dst]:
                            if t == cur:
                                to_remove = (t, d)
                        graph[dst].remove(to_remove)
                        next_stack.append(dst)
            stack = next_stack

    branches = {(sx, sy): 0, (fx, fy): 1}
    graph = [[], []]
    dfs2(sx, sy + 1, set(), (sx, sy), 0, 1, branches, graph)
    bfstrim(0, graph)
    return dfs3(0, 0, 0, graph)

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")