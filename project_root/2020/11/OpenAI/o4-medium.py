import sys
data=[list(line.rstrip()) for line in open(sys.argv[1]) if line.strip()]
H,W=len(data),len(data[0])
m={'.':0,'L':1,'#':2}
grid0=[[m[c] for c in row] for row in data]
dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
n1=[[[] for _ in range(W)] for _ in range(H)]
n2=[[[] for _ in range(W)] for _ in range(H)]
for y in range(H):
    for x in range(W):
        for dy,dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny<H and 0<=nx<W: n1[y][x].append((ny,nx))
            step=1
            while True:
                yy,xx=y+dy*step,x+dx*step
                if not (0<=yy<H and 0<=xx<W): break
                if grid0[yy][xx]!=0:
                    n2[y][x].append((yy,xx)); break
                step+=1
def sim(neighbors,thr):
    grid=[row[:] for row in grid0]
    while True:
        changed=False
        new=[row[:] for row in grid]
        for y in range(H):
            for x in range(W):
                v=grid[y][x]
                if v==0: continue
                cnt=0
                for yy,xx in neighbors[y][x]:
                    if grid[yy][xx]==2: cnt+=1
                if v==1 and cnt==0:
                    new[y][x]=2; changed=True
                elif v==2 and cnt>=thr:
                    new[y][x]=1; changed=True
        if not changed: break
        grid=new
    return sum(c==2 for row in grid for c in row)
print(sim(n1,4),sim(n2,5))