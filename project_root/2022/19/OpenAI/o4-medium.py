import sys
from functools import lru_cache
from math import prod

def parse_data(data):
    bps=[]
    for line in data:
        items=line.split()
        bps.append(((int(items[6]),0,0,0),(int(items[12]),0,0,0),(int(items[18]),int(items[21]),0,0),(int(items[27]),0,int(items[30]),0)))
    return bps

def solve_blueprint(bp,time_limit):
    maxcost=[max(bp[i][j] for i in range(4)) for j in range(4)]
    best=[0]
    @lru_cache(None)
    def dfs(time,left_o,left_c,left_s,left_g,r_o,r_c,r_s,r_g):
        if time==0: return left_g
        left_o=min(left_o, maxcost[0]*time)
        left_c=min(left_c, maxcost[1]*time)
        left_s=min(left_s, maxcost[2]*time)
        ub=left_g + r_g*time + time*(time-1)//2
        if ub<=best[0]: return 0
        val=0
        for typ in (3,2,1,0):
            if typ==0 and r_o>=maxcost[0] or typ==1 and r_c>=maxcost[1] or typ==2 and r_s>=maxcost[2]: 
                if typ!=3: continue
            cost=bp[typ]
            wait=0
            possible=True
            for have,rate,c in ((left_o,r_o,cost[0]),(left_c,r_c,cost[1]),(left_s,r_s,cost[2])):
                if have<c:
                    if rate==0:
                        possible=False; break
                    d=(c-have+rate-1)//rate
                    if d>wait: wait=d
            if not possible: continue
            wait+=1
            if wait>time: continue
            no=left_o + r_o*wait - cost[0]
            nc=left_c + r_c*wait - cost[1]
            ns=left_s + r_s*wait - cost[2]
            ng=left_g + r_g*wait - cost[3]
            nr_o, nr_c, nr_s, nr_g = r_o, r_c, r_s, r_g
            if typ==0: nr_o+=1
            elif typ==1: nr_c+=1
            elif typ==2: nr_s+=1
            else: nr_g+=1
            res=dfs(time-wait,no,nc,ns,ng,nr_o,nr_c,nr_s,nr_g)
            if res>val: val=res
        if val>best[0]: best[0]=val
        return val
    return dfs(time_limit,0,0,0,0,1,0,0,0)

data=[l.strip() for l in open(sys.argv[1])]
bps=parse_data(data)
p1=sum((i+1)*solve_blueprint(bp,24) for i,bp in enumerate(bps))
p2=prod(solve_blueprint(bp,32) for bp in bps[:3])
print(p1)
print(p2)