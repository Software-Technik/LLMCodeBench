import sys
from collections import deque
def main():
    data=[line.strip() for line in open(sys.argv[1])]
    neighbors={}
    rates={}
    for line in data:
        a,b=line.split('; ')
        parts=a.split()
        name=parts[1]
        rate=int(parts[-1].split('=')[1])
        rates[name]=rate
        tos=b.split()[4:]
        neighbors[name]=[t.strip(',') for t in tos]
    pos=['AA']+[n for n,r in rates.items() if r>0]
    idx={n:i for i,n in enumerate(pos)}
    M=len(pos)
    P=M-1
    rate_list=[rates.get(n,0) for n in pos]
    dist=[[1000]*M for _ in range(M)]
    for i,n in enumerate(pos):
        dq=deque([n]); seen={n:0}
        while dq:
            u=dq.popleft(); d=seen[u]
            for v in neighbors.get(u,[]):
                if v not in seen:
                    seen[v]=d+1; dq.append(v)
        for j,n2 in enumerate(pos):
            dist[i][j]=seen.get(n2,1000)
    max1=0
    stack=[(0,30,0,0)]
    while stack:
        u,t,mask,press=stack.pop()
        if press>max1: max1=press
        for v in range(1,M):
            bit=1<<(v-1)
            if mask&bit: continue
            d=dist[u][v]
            nt=t-d-1
            if nt<=0: continue
            p2=press+rate_list[v]*nt
            stack.append((v,nt,mask|bit,p2))
    best={}
    stack=[(0,26,0,0)]
    while stack:
        u,t,mask,press=stack.pop()
        for v in range(1,M):
            bit=1<<(v-1)
            if mask&bit: continue
            d=dist[u][v]
            nt=t-d-1
            if nt<=0: continue
            p2=press+rate_list[v]*nt
            m2=mask|bit
            if best.get(m2,0)<p2:
                best[m2]=p2
                stack.append((v,nt,m2,p2))
    size=1<<P
    dp=[0]*size
    for m,p in best.items(): dp[m]=p
    for i in range(P):
        for m in range(size):
            if not (m&(1<<i)):
                m2=m|(1<<i)
                if dp[m]>dp[m2]: dp[m2]=dp[m]
    full=size-1
    max2=0
    for m in range(size):
        p=dp[m]+dp[full^m]
        if p>max2: max2=p
    sys.stdout.write(f"{max1}\n{max2}")
if __name__=="__main__":
    main()