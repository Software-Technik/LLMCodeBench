import sys
from collections import deque, defaultdict
def parse(text):
    lines = text.strip().splitlines()
    h = len(lines); w = len(lines[0])
    grid = [c for line in lines for c in line]
    start = 1; end = (h-1)*w + (w-2)
    return grid, w, h, start, end
def find_adjacent(src, grid, w, h, terms, ndirs):
    adj = []
    q = deque([(src, 0, {src})])
    while q:
        p, l, seen = q.popleft()
        if p in terms and p != src:
            adj.append((p, l)); continue
        r, c = divmod(p, w)
        nbrs = []
        if r>0:
            n = p-w
            if n not in seen and grid[n] != '#': nbrs.append(n)
        if c>0:
            n = p-1
            if n not in seen and grid[n] != '#': nbrs.append(n)
        if c<w-1:
            n = p+1
            if n not in seen and grid[n] != '#': nbrs.append(n)
        if r<h-1:
            n = p+w
            if n not in seen and grid[n] != '#': nbrs.append(n)
        if len(nbrs)>1 and p!=src:
            adj.append((p, l)); continue
        for n in nbrs:
            ch = grid[n]
            if ndirs and ch in ('>','<','^','v'):
                d = 1 if ch=='>' else -1 if ch=='<' else -w if ch=='^' else w
                np = n + d
                if np != p:
                    q.append((np, l+2, seen|{n,np}))
            elif ch=='.' or not ndirs:
                q.append((n, l+1, seen|{n}))
    return adj
def build_graph(grid, w, h, start, end, ndirs):
    graph = defaultdict(list)
    seen = set()
    stack = [start]
    terms = {start, end}
    while stack:
        p = stack.pop()
        if p in seen: continue
        seen.add(p)
        for n, l in find_adjacent(p, grid, w, h, terms, ndirs):
            graph[p].append((n, l))
            if n not in seen:
                stack.append(n)
    return graph
def longest_path(graph, start, end):
    best = 0
    stack = [(start, 0, {start})]
    while stack:
        p, l, seen = stack.pop()
        if p == end:
            if l > best: best = l
            continue
        for n, nl in graph.get(p, ()):
            if n not in seen:
                stack.append((n, l+nl, seen|{n}))
    return best
def part1(text):
    grid, w, h, start, end = parse(text)
    g = build_graph(grid, w, h, start, end, True)
    return longest_path(g, start, end)
def part2(text):
    grid, w, h, start, end = parse(text)
    g = build_graph(grid, w, h, start, end, False)
    return longest_path(g, start, end)
if __name__=="__main__":
    with open(sys.argv[1]) as f:
        t = f.read()
    sys.stdout.write(f"{part1(t)} {part2(t)}")