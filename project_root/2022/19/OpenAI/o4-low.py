import sys
from math import prod

def parse(data):
    bps=[]
    for l in data:
        i=l.split()
        bps.append(((int(i[6]),0,0,0),(int(i[12]),0,0,0),(int(i[18]),int(i[21]),0,0),(int(i[27]),0,int(i[30]),0)))
    return bps

def solve(bp, T):
    max_cost=[max(bp[r][i] for r in range(4)) for i in range(4)]
    memo={}
    best=0
    def dfs(t,robots,res):
        nonlocal best
        if t==0:
            best=max(best,res[3]);return
        ub=res[3]+robots[3]*t+t*(t-1)//2
        if ub<=best: return
        key=(t,robots,res)
        if key in memo and memo[key]>=res: return
        memo[key]=res
        for r in range(4):
            if r<3 and robots[r]>=max_cost[r]: continue
            cost=bp[r]
            if all(res[i]>=cost[i] for i in range(4)):
                nr=tuple(robots[i]+(1 if i==r else 0) for i in range(4))
                nres=tuple(res[i]-cost[i]+robots[i] for i in range(4))
                dfs(t-1,nr,nres)
        nres=tuple(res[i]+robots[i] for i in range(4))
        dfs(t-1,robots,nres)
    dfs(T,(1,0,0,0),(0,0,0,0))
    return best

data=[l.strip() for l in open(sys.argv[1])]
bps=parse(data)
p1=sum((i+1)*solve(bps[i],24) for i in range(len(bps)))
p2=prod(solve(bps[i],32) for i in range(min(3,len(bps))))
print(p1)
print(p2)