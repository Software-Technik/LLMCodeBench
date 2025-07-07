import sys
from collections import deque
from functools import lru_cache

def main():
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f]
    rates = {}
    adj = {}
    for l in lines:
        a, b = l.split("; ")
        parts = a.split()
        v = parts[1]
        r = int(parts[-1].split("=")[1])
        adj.setdefault(v, [])
        for w in b.split()[4:]:
            w = w.rstrip(",")
            adj[v].append(w)
            adj.setdefault(w, []).append(v)
        if r > 0:
            rates[v] = r
    flow = list(rates.keys())
    n = len(flow)
    idx = {v: i for i, v in enumerate(flow)}
    nodes = ["AA"] + flow
    dist = {u: {} for u in nodes}
    for u in nodes:
        d = {u: 0}
        q = deque([u])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    q.append(y)
        for v in nodes:
            dist[u][v] = d.get(v, 10**9)
    @lru_cache(None)
    def dfs(u, t, mask):
        best = 0
        for v in flow:
            b = idx[v]
            if not (mask >> b) & 1:
                c = dist[u][v] + 1
                if c < t:
                    best = max(best, (t - c) * rates[v] + dfs(v, t - c, mask | (1 << b)))
        return best
    p1 = dfs("AA", 30, 0)
    best_state = {}
    best_by_mask = {}
    stack = [("AA", 26, 0, 0)]
    while stack:
        u, t, mask, p = stack.pop()
        if best_by_mask.get(mask, 0) < p:
            best_by_mask[mask] = p
        for v in flow:
            b = idx[v]
            if (mask >> b) & 1:
                continue
            c = dist[u][v] + 1
            if c < t:
                t2 = t - c
                p2 = p + rates[v] * t2
                m2 = mask | (1 << b)
                key = (v, t2, m2)
                if best_state.get(key, -1) < p2:
                    best_state[key] = p2
                    stack.append((v, t2, m2, p2))
    full = (1 << n) - 1
    size = 1 << n
    best_sub = [0] * size
    for m, p in best_by_mask.items():
        best_sub[m] = p
    for i in range(n):
        for m in range(size):
            if m & (1 << i):
                if best_sub[m ^ (1 << i)] > best_sub[m]:
                    best_sub[m] = best_sub[m ^ (1 << i)]
    p2 = 0
    for m, p in best_by_mask.items():
        r = best_sub[full ^ m]
        if p + r > p2:
            p2 = p + r
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == "__main__":
    main()