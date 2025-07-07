import sys
from collections import deque
from functools import lru_cache

data = [line.strip() for line in open(sys.argv[1])]

adj = {}
rates = {}
for line in data:
    a, b = line.split('; ')
    parts = a.split()
    v = parts[1]
    r = int(parts[-1].split('=')[1])
    tos = [x.strip(',') for x in b.split()[4:]]
    adj.setdefault(v, []).extend(tos)
    if r > 0:
        rates[v] = r

nodes = list(rates.keys())
n = len(nodes)
idx = {v: i for i, v in enumerate(nodes)}
start = 'AA'
all_nodes = nodes + [start]
m = n + 1

dist = [[999] * m for _ in range(m)]
for i, v in enumerate(all_nodes):
    dq = deque([(v, 0)])
    seen = {v}
    while dq:
        u, d = dq.popleft()
        j = all_nodes.index(u)
        dist[i][j] = d
        for w in adj.get(u, []):
            if w not in seen:
                seen.add(w)
                dq.append((w, d + 1))

rates_list = [rates[v] for v in nodes] + [0]

@lru_cache(None)
def dfs(pos, time, mask):
    best = 0
    for i in range(n):
        bit = 1 << i
        if mask & bit: continue
        d = dist[pos][i]
        nt = time - d - 1
        if nt <= 0: continue
        val = rates_list[i] * nt + dfs(i, nt, mask | bit)
        if val > best: best = val
    return best

res1 = dfs(n, 30, 0)

stack = [(n, 26, 0, 0)]
bests = {}
while stack:
    pos, time, mask, pres = stack.pop()
    bests[mask] = max(bests.get(mask, 0), pres)
    for i in range(n):
        bit = 1 << i
        if mask & bit: continue
        d = dist[pos][i]
        nt = time - d - 1
        if nt <= 0: continue
        stack.append((i, nt, mask | bit, pres + rates_list[i] * nt))

full = (1 << n) - 1
res2 = 0
for m1, p1 in bests.items():
    p2 = bests.get(full ^ m1, 0)
    if p1 + p2 > res2:
        res2 = p1 + p2

print(res1)
print(res2)