import sys

sys.setrecursionlimit(10000)

dirs = ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v"))

def part1(text):
    tiles = text.strip().splitlines()
    dimx, dimy = len(tiles[0]), len(tiles)
    sx, sy, fx, fy = tiles[0].find("."), 0, tiles[-1].find("."), dimy - 1

    path = [0] * (dimx * dimy)

    def dfs(x, y, plen):
        if (x, y) == (fx, fy):
            return plen
        path[y * dimx + x] = 1
        best = 0
        for dx, dy, dc in dirs:
            nx, ny = x + dx, y + dy
            if (tiles[ny][nx] in ". " + dc) and not path[ny * dimx + nx]:
                best = max(best, dfs(nx, ny, plen + 1))
        path[y * dimx + x] = 0
        return best

    return dfs(sx, sy + 1, 1)

def part2(text):
    tiles = text.strip().splitlines()
    dimx, dimy = len(tiles[0]), len(tiles)
    sx, sy, fx, fy = tiles[0].find("."), 0, tiles[-1].find("."), dimy - 1

    branches = {(sx, sy): 0, (fx, fy): 1}
    graph = [[], []]

    def dfs(x, y, prev, last, steps):
        stack = [(x, y, prev, last, steps)]
        visited = set()
        
        while stack:
            x, y, prev, last, steps = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            cnt = sum(1 for dx, dy, _ in dirs if tiles[y+dy][x+dx] != '#' and (x+dx, y+dy) != prev)
            if cnt > 1:
                cur = branches.setdefault((x, y), len(branches))
                if cur == len(graph):
                    graph.append([])
                graph[cur].append((last, steps))
                graph[last].append((cur, steps))
                last = cur
                steps = 0
            for dx, dy, _ in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) in branches and (nx, ny) != prev:
                    cur = branches[(nx, ny)]
                    graph[cur].append((last, steps + 1))
                    graph[last].append((cur, steps + 1))
                elif tiles[ny][nx] != '#' and (nx, ny) not in visited:
                    stack.append((nx, ny, (x, y), last, steps + 1))

    dfs(sx, sy + 1, (sx, sy), 0, 1)

    def dfs3(cur, path, steps):
        stack = [(cur, path, steps)]
        best = 0
        while stack:
            cur, path, steps = stack.pop()
            if cur == 1:
                best = max(best, steps)
            path |= 1 << cur
            for dst, add in graph[cur]:
                if not path & (1 << dst):
                    stack.append((dst, path, steps + add))
        return best

    def bfstrim(start):
        queue = [start]
        while queue:
            next_queue = []
            for cur in queue:
                for dst, _ in graph[cur]:
                    if len(graph[dst]) == 3:
                        to_remove = next((t, d) for t, d in graph[dst] if t == cur)
                        graph[dst].remove(to_remove)
                        next_queue.append(dst)
            queue = next_queue

    bfstrim(0)
    return dfs3(0, 0, 0)

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")