import sys
sys.setrecursionlimit(10000)
def part1(lines):
    adj = {}
    for l in lines:
        a,b=l.split("-")
        adj.setdefault(a,set()).add(b)
        adj.setdefault(b,set()).add(a)
    nodes=sorted(adj)
    ans=0
    for i,u in enumerate(nodes):
        for v in adj[u]:
            if v<=u: continue
            for w in adj[u].intersection(adj[v]):
                if w<=v: continue
                if u.startswith("t") or v.startswith("t") or w.startswith("t"):
                    ans+=1
    return ans

def part2(lines):
    adj = {}
    for l in lines:
        a,b=l.split("-")
        adj.setdefault(a,set()).add(b)
        adj.setdefault(b,set()).add(a)
    maxc=[]
    def bk(R,P,X):
        nonlocal maxc
        if not P and not X:
            if len(R)>len(maxc): maxc=list(R)
            return
        u=max(P|X,key=lambda u: len(P&adj[u]))
        for v in tuple(P - adj[u]):
            bk(R|{v},P&adj[v],X&adj[v])
            P.remove(v)
            X.add(v)
    allnodes=set(adj)
    bk(set(),allnodes,set())
    return ",".join(sorted(maxc))

lines=open(sys.argv[1]).read().splitlines()
print(part1(lines),part2(lines))