import sys
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def step(g):
    q=[]
    n=len(g);m=len(g[0])
    for i in range(n):
        for j in range(m):
            g[i][j]+=1
            if g[i][j]>9:q.append((i,j))
    flashed=[[False]*m for _ in range(n)]
    fcount=0
    while q:
        i,j=q.pop()
        if flashed[i][j]:continue
        flashed[i][j]=True
        fcount+=1
        for di,dj in dirs:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m:
                g[ni][nj]+=1
                if g[ni][nj]>9 and not flashed[ni][nj]:q.append((ni,nj))
    for i in range(n):
        for j in range(m):
            if flashed[i][j]:g[i][j]=0
    return fcount, fcount==n*m

def part1(o):
    g=[row.copy() for row in o]
    t=0
    for _ in range(100):
        f,_=step(g);t+=f
    return t

def part2(o):
    g=[row.copy() for row in o]
    s=0;n=len(g)*len(g[0])
    while True:
        s+=1
        f,allf=step(g)
        if allf:return s

data=[list(map(int,line.strip())) for line in open(sys.argv[1]) if line.strip()]
sys.stdout.write(f"{part1(data)} {part2(data)}")