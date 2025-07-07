import sys
from collections import deque

def part1(grid):
    n = len(grid)
    G = [[ord(c) for c in row] for row in grid]
    free = [[0]*n for _ in range(n)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(n):
        for j in range(n):
            cnt=0
            for di,dj in dirs:
                ii, jj = i+di, j+dj
                if ii<0 or ii>=n or jj<0 or jj>=n or G[ii][jj]!=G[i][j]:
                    cnt+=1
            free[i][j]=cnt
    seen = [[False]*n for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            if seen[i][j]: continue
            c = G[i][j]
            dq = deque([(i,j)])
            seen[i][j]=True
            size=0
            per=0
            while dq:
                x,y = dq.popleft()
                size+=1
                per+=free[x][y]
                for di,dj in dirs:
                    ii, jj = x+di, y+dj
                    if 0<=ii<n and 0<=jj<n and not seen[ii][jj] and G[ii][jj]==c:
                        seen[ii][jj]=True
                        dq.append((ii,jj))
            ans+=per*size
    return ans

def part2(grid):
    n = len(grid)
    G = [[ord(c) for c in row] for row in grid]
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    seen = [[False]*n for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            if seen[i][j]: continue
            c = G[i][j]
            dq = deque([(i,j)])
            seen[i][j]=True
            pts = []
            while dq:
                x,y = dq.popleft()
                pts.append((x,y))
                for di,dj in dirs:
                    ii, jj = x+di, y+dj
                    if 0<=ii<n and 0<=jj<n and not seen[ii][jj] and G[ii][jj]==c:
                        seen[ii][jj]=True
                        dq.append((ii,jj))
            s = set(pts)
            mi=min(x for x,_ in pts)-1; Ma=max(x for x,_ in pts)
            mj=min(y for _,y in pts)-1; Mb=max(y for _,y in pts)
            per=0
            for x in range(mi,Ma+1):
                for y in range(mj,Mb+1):
                    a = (x,y) in s
                    b = (x,y+1) in s
                    c2= (x+1,y) in s
                    d = (x+1,y+1) in s
                    tot = a+b+c2+d
                    if tot==1 or tot==3: per+=1
                    elif tot==2 and ((a and d) or (b and c2)): per+=2
            ans+=per*len(pts)
    return ans

if __name__=="__main__":
    path=sys.argv[1]
    with open(path) as f:
        grid=f.read().splitlines()
    print(part1(grid), part2(grid))