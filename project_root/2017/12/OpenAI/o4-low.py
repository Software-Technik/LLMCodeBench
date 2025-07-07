import sys

def main():
    lines = sys.stdin if len(sys.argv) == 1 else open(sys.argv[1])
    maxn = 0
    pairs = []
    for l in lines:
        l = l.strip()
        if not l: continue
        a, rest = l.split(" <-> ")
        u = int(a)
        nbrs = list(map(int, rest.split(", ")))
        if u > maxn: maxn = u
        for v in nbrs:
            if v > maxn: maxn = v
        pairs.append((u, nbrs))
    n = maxn + 1
    g = [[] for _ in range(n)]
    for u, nbrs in pairs:
        g[u] = nbrs
    def dfs(s, vis):
        st = [s]
        cnt = 0
        while st:
            u = st.pop()
            if not vis[u]:
                vis[u] = True
                cnt += 1
                st.extend(g[u])
        return cnt
    vis0 = [False] * n
    c0 = dfs(0, vis0)
    vis = [False] * n
    groups = 0
    for i in range(n):
        if not vis[i]:
            dfs(i, vis)
            groups += 1
    sys.stdout.write(f"{c0}\n{groups}")

if __name__ == "__main__":
    main()