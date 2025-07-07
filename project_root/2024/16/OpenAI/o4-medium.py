import sys
import heapq
def part1(grid):
    n=len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='S':si,sj=i,j
            elif grid[i][j]=='E':ei,ej=i,j
    INF=10**18
    dist=[[[INF]*n for _ in range(n)] for _ in range(4)]
    dist[0][si][sj]=0
    h=[(0,0,si,sj)]
    dirs=((0,1),(1,0),(0,-1),(-1,0))
    while h:
        c,d,i,j=heapq.heappop(h)
        if c!=dist[d][i][j]:continue
        if grid[i][j]=='#':continue
        if i==ei and j==ej:return c
        di,dj=dirs[d]
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<n and c+1<dist[d][ni][nj]:
            dist[d][ni][nj]=c+1;heapq.heappush(h,(c+1,d,ni,nj))
        nd=(d+1)&3
        if c+1000<dist[nd][i][j]:
            dist[nd][i][j]=c+1000;heapq.heappush(h,(c+1000,nd,i,j))
        nd=(d+3)&3
        if c+1000<dist[nd][i][j]:
            dist[nd][i][j]=c+1000;heapq.heappush(h,(c+1000,nd,i,j))
def part2(grid):
    n=len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='S':si,sj=i,j
            elif grid[i][j]=='E':ei,ej=i,j
    INF=10**18
    size=4*n*n
    dist=[INF]*size
    deps=[[] for _ in range(size)]
    dirs=((0,1),(1,0),(0,-1),(-1,0))
    def idx(d,i,j):return (d*n+i)*n+j
    start_idx=idx(0,si,sj)
    dist[start_idx]=0
    q=[(0,0,si,sj,0,si,sj)]
    end_dir=0
    while q:
        c,d,i,j,pd,pi,pj=heapq.heappop(q)
        u=idx(d,i,j)
        if dist[u]!=INF:
            if dist[u]==c:deps[u].append(idx(pd,pi,pj))
            continue
        dist[u]=c;deps[u].append(idx(pd,pi,pj))
        if grid[i][j]=='#':continue
        if i==ei and j==ej:
            end_dir=d;break
        di,dj=dirs[d]
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<n:heapq.heappush(q,(c+1,d,ni,nj,d,i,j))
        nd=(d+1)&3;heapq.heappush(q,(c+1000,nd,i,j,d,i,j))
        nd=(d+3)&3;heapq.heappush(q,(c+1000,nd,i,j,d,i,j))
    targ=idx(end_dir,ei,ej)
    seen=[False]*size
    seen_pos=[False]*(n*n)
    stack=[targ]
    cnt=0
    while stack:
        u=stack.pop()
        if seen[u]:continue
        seen[u]=True
        r=u//n//n; rem=u%(n*n); i=rem//n; j=rem%n
        p=i*n+j
        if not seen_pos[p]:
            seen_pos[p]=True;cnt+=1
        for v in deps[u]:stack.append(v)
    return cnt
g=sys.argv[1]
with open(g) as f:
    grid=f.read().splitlines()
    print(part1(grid),part2(grid))