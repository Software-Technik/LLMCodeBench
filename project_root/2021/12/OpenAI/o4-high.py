import sys
from functools import lru_cache

f = open(sys.argv[1])
data = [line.strip() for line in f if line.strip()]
f.close()
pairs = [line.split('-') for line in data]
nodes = set()
for a, b in pairs:
    nodes.add(a); nodes.add(b)
names = ['start', 'end'] + [n for n in sorted(nodes) if n not in ('start', 'end')]
nid = {n: i for i, n in enumerate(names)}
start = nid['start']; end = nid['end']
adj = [[] for _ in names]
for a, b in pairs:
    u = nid[a]; v = nid[b]
    if b != 'start' and a != 'end': adj[u].append(v)
    if a != 'start' and b != 'end': adj[v].append(u)
small = [i for i, n in enumerate(names) if n.islower()]
bit = {i: j for j, i in enumerate(small)}

def count_paths(allow_double):
    @lru_cache(None)
    def dfs(u, mask, used):
        total = 0
        for v in adj[u]:
            if v == end:
                total += 1
            else:
                b = bit.get(v)
                if b is not None:
                    m = 1 << b
                    if not mask & m:
                        total += dfs(v, mask | m, used)
                    elif allow_double and not used:
                        total += dfs(v, mask, True)
                else:
                    total += dfs(v, mask, used)
        return total
    return dfs(start, 1 << bit[start], False)

p1 = count_paths(False)
p2 = count_paths(True)
sys.stdout.write(f"{p1} {p2}")