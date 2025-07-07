import sys
sys.setrecursionlimit(10000)
def main():
    conns=[]
    doubles=set()
    with open(sys.argv[1]) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            a,b=map(int,line.split('/'))
            if a!=b:
                conns.append((a,b))
            else:
                doubles.add(a)
    adj={}
    for i,(a,b) in enumerate(conns):
        adj.setdefault(a,[]).append((i,b))
        adj.setdefault(b,[]).append((i,a))
    max_score=0
    best_len=0
    best_score2=0
    path=[]
    def dfs(node,visited):
        nonlocal max_score,best_len,best_score2
        s=0
        for n in path:
            s+=2*n
        length=len(path)
        used=set()
        for n in path:
            if n in doubles and n not in used:
                s+=2*n
                length+=1
                used.add(n)
        if path:
            s-=path[-1]
        if s>max_score:
            max_score=s
        if length>best_len or (length==best_len and s>best_score2):
            best_len=length
            best_score2=s
        for i,nxt in adj.get(node,()):
            if visited>>i&1: continue
            path.append(nxt)
            dfs(nxt,visited|1<<i)
            path.pop()
    dfs(0,0)
    print(max_score)
    print(best_score2)

if __name__=='__main__':
    main()