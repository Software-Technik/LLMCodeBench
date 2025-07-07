import sys
from collections import deque
from math import gcd
def lcm(a,b): return a*b//gcd(a,b)
def parse(data):
    h,w=len(data),len(data[0])
    dirs={">":(0,1),"<":(0,-1),"^":(-1,0),"v":(1,0)}
    bl=[]
    for y in range(1,h-1):
        for x in range(1,w-1):
            c=data[y][x]
            if c in dirs: bl.append((y,x,*dirs[c]))
    return h,w,bl
def precompute(h,w,bl):
    h0,h1=h-2,w-2
    P=lcm(h0,h1)
    blocked=[]
    for t in range(P):
        s=set()
        for y,x,dy,dx in bl:
            yy=(y-1+dy*t)%h0+1
            xx=(x-1+dx*t)%h1+1
            s.add((yy,xx))
        blocked.append(s)
    return P,blocked
def bfs1(data):
    h,w,bl=parse(data)
    P,blocked=precompute(h,w,bl)
    start=(0,1);target=(h-1,w-2)
    areas=set((y,x) for y in range(1,h-1) for x in range(1,w-1))
    areas|={start,target}
    dirs=[(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    vis=set()
    dq=deque()
    dq.append((start,0))
    while dq:
        (y,x),t=dq.popleft()
        if (y,x)==target: return t
        m=t%P
        if ((y,x),m) in vis: continue
        vis.add(((y,x),m))
        b=blocked[(m+1)%P]
        for dy,dx in dirs:
            ny,nx=y+dy,x+dx
            np=(ny,nx)
            if np in areas and np not in b:
                dq.append((np,t+1))
def bfs2(data):
    h,w,bl=parse(data)
    P,blocked=precompute(h,w,bl)
    start=(0,1);target=(h-1,w-2)
    areas=set((y,x) for y in range(1,h-1) for x in range(1,w-1))
    areas|={start,target}
    dirs=[(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    vis=set()
    dq=deque()
    dq.append((start,0,0))
    while dq:
        (y,x),t,leg=dq.popleft()
        if leg==0 and (y,x)==target: leg=1
        elif leg==1 and (y,x)==start: leg=2
        elif leg==2 and (y,x)==target: return t
        m=t%P
        if ((y,x),m,leg) in vis: continue
        vis.add(((y,x),m,leg))
        b=blocked[(m+1)%P]
        for dy,dx in dirs:
            ny,nx=y+dy,x+dx
            np=(ny,nx)
            if np in areas and np not in b:
                dq.append((np,t+1,leg))
if __name__=="__main__":
    data=[l.strip() for l in open(sys.argv[1])]
    print(bfs1(data))
    print(bfs2(data))