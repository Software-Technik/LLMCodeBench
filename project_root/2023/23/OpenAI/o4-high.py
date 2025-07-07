import sys
sys.setrecursionlimit(10000)
def part1(text):
    lines = text.strip().splitlines()
    H = len(lines); W = len(lines[0]); grid = ''.join(lines).encode()
    N = H*W
    s = lines[0].find('.'); f = lines[-1].find('.')
    start = s + W; finish = f + (H-1)*W
    Wm1 = W-1; Hm1 = H-1
    neighbors = [[] for _ in range(N)]
    for pos in range(N):
        x = pos % W; y = pos // W
        if x>0: neighbors[pos].append((pos-1,60))
        if x<Wm1: neighbors[pos].append((pos+1,62))
        if y>0: neighbors[pos].append((pos-W,94))
        if y<Hm1: neighbors[pos].append((pos+W,118))
    visited = bytearray(N)
    best = 0
    def dfs(pos, plen):
        nonlocal best
        if pos == finish:
            if plen > best: best = plen
            return
        visited[pos] = 1
        for npos, d in neighbors[pos]:
            if visited[npos] == 0:
                v = grid[npos]
                if v == 46 or v == d:
                    dfs(npos, plen+1)
        visited[pos] = 0
    dfs(start, 1)
    return best

def part2(text):
    lines = text.strip().splitlines()
    H = len(lines); W = len(lines[0]); grid = ''.join(lines).encode()
    N = H*W
    s = lines[0].find('.'); f = lines[-1].find('.')
    start_cell = s; finish_cell = f + (H-1)*W
    neighbors = [[] for _ in range(N)]
    for pos in range(N):
        if grid[pos] == 35: continue
        x = pos % W; y = pos // W
        if x>0 and grid[pos-1] != 35: neighbors[pos].append(pos-1)
        if x<W-1 and grid[pos+1] != 35: neighbors[pos].append(pos+1)
        if y>0 and grid[pos-W] != 35: neighbors[pos].append(pos-W)
        if y<H-1 and grid[pos+W] != 35: neighbors[pos].append(pos+W)
    visited = bytearray(N)
    branch = [-1]*N
    branch[start_cell] = 0; branch[finish_cell] = 1
    graph = [[],[]]
    def dfs2(pos, prev, last, steps):
        visited[pos] = 1
        cnt = 0
        for npos in neighbors[pos]:
            if npos != prev: cnt += 1
        if cnt > 1:
            cur = len(graph)
            branch[pos] = cur
            graph.append([])
            graph[cur].append((last, steps))
            graph[last].append((cur, steps))
            last = cur; steps = 0
        for npos in neighbors[pos]:
            if npos == prev: continue
            b = branch[npos]
            if b != -1:
                graph[b].append((last, steps+1))
                graph[last].append((b, steps+1))
            elif not visited[npos]:
                dfs2(npos, pos, last, steps+1)
    dfs2(start_cell+W, start_cell, 0, 1)
    stack = [0]
    while stack:
        ns = []
        for cur in stack:
            for dst, d in graph[cur]:
                if len(graph[dst]) == 3:
                    for t, dd in graph[dst]:
                        if t == cur:
                            graph[dst].remove((t, dd)); break
                    ns.append(dst)
        stack = ns
    def dfs3(cur, mask, steps):
        if cur == 1: return steps
        mask |= 1<<cur
        best = 0
        for dst, w in graph[cur]:
            if not (mask >> dst & 1):
                v = dfs3(dst, mask, steps+w)
                if v > best: best = v
        return best
    return dfs3(0, 0, 0)

if __name__ == "__main__":
    data = sys.argv[1]
    with open(data) as f: text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")