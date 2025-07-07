import sys,heapq
def navigate(grid,minval,maxval):
    rows,len_cols=len(grid),len(grid[0])
    cols=len_cols
    INF=10**18
    dist=[[[INF,INF] for _ in range(cols)] for __ in range(rows)]
    h=[]
    dist[0][0][0]=dist[0][0][1]=0
    heapq.heappush(h,(0,0,0,0));heapq.heappush(h,(0,0,0,1))
    goaly,goalx=rows-1,cols-1
    moves=[[(1,0),(-1,0)],[(0,1),(0,-1)]]
    while h:
        cost,y,x,d=heapq.heappop(h)
        if y==goaly and x==goalx: return cost
        if cost!=dist[y][x][d]: continue
        for dy,dx in moves[d]:
            running=0
            for step in range(1,maxval+1):
                ny=y+dy*step; nx=x+dx*step
                if ny<0 or ny>=rows or nx<0 or nx>=cols: break
                running+=grid[ny][nx]
                if step>=minval:
                    nd=1-d; nc=cost+running
                    if nc<dist[ny][nx][nd]:
                        dist[ny][nx][nd]=nc
                        heapq.heappush(h,(nc,ny,nx,nd))
    return INF

grid=[list(map(int,line.strip())) for line in open(sys.argv[1]) if line.strip()]
p1=navigate(grid,1,3); p2=navigate(grid,4,10)
sys.stdout.write(f"{p1} {p2}")