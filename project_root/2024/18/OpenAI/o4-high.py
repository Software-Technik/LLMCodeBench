import sys
from heapq import heappush, heappop

N=70
dim=N+1
total=dim*dim
dirs=((1,0),(0,1),(-1,0),(0,-1))
hlist=[0]*total
for i in range(dim):
    bi=abs(N-i)
    for j in range(dim):
        hlist[i*dim+j]=bi+abs(N-j)
start_h=hlist[0]
goal_idx=N*dim+N

def astar_mask(blocked):
    visited=bytearray(total)
    pq=[(start_h,0,0,0)]
    while pq:
        f,i,j,g=heappop(pq)
        idx=i*dim+j
        if visited[idx]: continue
        visited[idx]=1
        if idx==goal_idx: return g
        ng=g+1
        for di,dj in dirs:
            ii=i+di; jj=j+dj
            if 0<=ii<dim and 0<=jj<dim:
                idx2=ii*dim+jj
                if not visited[idx2] and not blocked[idx2]:
                    heappush(pq,(ng+hlist[idx2],ii,jj,ng))

def part1(coords):
    blocked=bytearray(total)
    for x,y in coords[:1024]:
        blocked[x*dim+y]=1
    return astar_mask(blocked)

def part2(coords):
    lo,hi=0,len(coords)-1
    while lo<hi:
        mid=(lo+hi)//2
        blocked=bytearray(total)
        for x,y in coords[:mid]:
            blocked[x*dim+y]=1
        if astar_mask(blocked): lo=mid+1
        else: hi=mid
    return coords[lo-1]

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        lines=f.read().splitlines()
    coords=[tuple(map(int,l.split(','))) for l in lines]
    p1=part1(coords)
    x,y=part2(coords)
    print(p1,f"{x},{y}")