import sys
from collections import defaultdict

def part1(lines):
    adj = defaultdict(set)
    for l in lines:
        a,b = l.split('-')
        adj[a].add(b)
        adj[b].add(a)
    ans = 0
    for u in adj:
        for v in adj[u]:
            if u < v:
                common = adj[u] & adj[v]
                for w in common:
                    if v < w and (u[0]=='t' or v[0]=='t' or w[0]=='t'):
                        ans += 1
    return ans

def part2(lines):
    adj = defaultdict(set)
    for l in lines:
        a,b = l.split('-')
        adj[a].add(b)
        adj[b].add(a)
    best = []
    def bronk(R, P, X):
        nonlocal best
        if not P and not X:
            if len(R) > len(best):
                best = list(R)
            return
        u = max(P|X, key=lambda x: len(P & adj[x]), default=None)
        for v in list(P - (adj[u] if u else set())):
            bronk(R|{v}, P & adj[v], X & adj[v])
            P.remove(v)
            X.add(v)
    bronk(set(), set(adj), set())
    return ",".join(sorted(best))

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path) as f:
        lines = f.read().strip().split('\n')
    print(part1(lines), part2(lines))