import sys,heapq

lines=open(sys.argv[1]).read().splitlines()
coords=[tuple(map(int,line.split(','))) for line in lines]
N=70

def part1(lst):
    block=[[False]*(N+1) for _ in range(N+1)]
    for x,y in lst[:1024]:
        if 0<=x<=N and 0<=y<=N: block[x][y]=True
    g=[[10**9]*(N+1) for _ in range(N+1)]
    vis=[[False]*(N+1) for _ in range(N+1)]
    g[0][0]=0
    q=[(2*N,0,0)]
    while q:
        f,i,j=heapq.heappop(q)
        if vis[i][j]: continue
        vis[i][j]=True
        if i==N and j==N: return g[i][j]
        gi=g[i][j]
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj=i+di,j+dj
            if 0<=ni<=N and 0<=nj<=N and not vis[ni][nj] and not block[ni][nj]:
                ng=gi+1
                if ng<g[ni][nj]:
                    g[ni][nj]=ng
                    heapq.heappush(q,(ng+abs(N-ni)+abs(N-nj),ni,nj))

def part2(lst):
    idxg=[[len(lst)]*(N+1) for _ in range(N+1)]
    for idx,(x,y) in enumerate(lst):
        if 0<=x<=N and 0<=y<=N: idxg[x][y]=idx
    def doable(mid):
        g=[[10**9]*(N+1) for _ in range(N+1)]
        vis=[[False]*(N+1) for _ in range(N+1)]
        g[0][0]=0
        q=[(2*N,0,0)]
        while q:
            f,i,j=heapq.heappop(q)
            if vis[i][j]: continue
            vis[i][j]=True
            if i==N and j==N: return True
            gi=g[i][j]
            for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<=N and 0<=nj<=N and not vis[ni][nj] and idxg[ni][nj]>=mid:
                    ng=gi+1
                    if ng<g[ni][nj]:
                        g[ni][nj]=ng
                        heapq.heappush(q,(ng+abs(N-ni)+abs(N-nj),ni,nj))
        return False
    lo,hi=0,len(lst)-1
    while hi>lo:
        mid=(lo+hi)//2
        if doable(mid): lo=mid+1
        else: hi=mid
    x,y=lst[lo-1]
    return f"{x},{y}"

print(part1(coords), part2(coords))