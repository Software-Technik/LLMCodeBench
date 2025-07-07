import sys
from collections import defaultdict

def part1(lines):
    adj=defaultdict(set)
    for line in lines:
        a,b=line.split('-')
        adj[a].add(b); adj[b].add(a)
    ans=0
    for u in adj:
        for v in adj[u]:
            if v<=u: continue
            common=adj[u]&adj[v]
            for w in common:
                if w<=v: continue
                if u[0]=='t' or v[0]=='t' or w[0]=='t':
                    ans+=1
    return ans

def part2(lines):
    adj=defaultdict(set)
    for line in lines:
        a,b=line.split('-')
        adj[a].add(b); adj[b].add(a)
    global_max=[]
    def bk(R,P,X):
        nonlocal global_max
        if not P and not X:
            if len(R)>len(global_max): global_max=list(R)
            return
        U=P|X
        if U:
            u=max(U,key=lambda x: len(P&adj[x]))
            cand=P-adj[u]
        else:
            cand=set(P)
        for v in list(cand):
            newR=R|{v}
            newP=P&adj[v]
            newX=X&adj[v]
            if len(newR)+len(newP)<=len(global_max):
                P.remove(v); X.add(v)
                continue
            bk(newR,newP,newX)
            P.remove(v); X.add(v)
    for v in adj:
        if len(adj[v])+1<=len(global_max): continue
        bk({v},set(adj[v]),set())
    return ",".join(sorted(global_max))

if __name__=="__main__":
    lines=open(sys.argv[1]).read().splitlines()
    print(part1(lines),part2(lines))