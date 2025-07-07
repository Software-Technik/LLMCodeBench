import sys
from collections import deque

def part1(h, H, W, start, target):
    seen = [[-1]*W for _ in range(H)]
    dq = deque()
    dq.append((start[0], start[1], 0))
    seen[start[0]][start[1]] = 0
    dirs = ((1,0),(-1,0),(0,1),(0,-1))
    while dq:
        y,x,s = dq.popleft()
        if (y,x)==target:
            return s
        v = h[y][x]
        ns = s+1
        for dy,dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny<H and 0<=nx<W and seen[ny][nx]==-1 and h[ny][nx]-v<=1:
                seen[ny][nx]=ns
                dq.append((ny,nx,ns))

def part2(h, H, W, target):
    seen = [[-1]*W for _ in range(H)]
    dq = deque()
    dq.append((target[0], target[1], 0))
    seen[target[0]][target[1]] = 0
    dirs = ((1,0),(-1,0),(0,1),(0,-1))
    while dq:
        y,x,s = dq.popleft()
        if h[y][x]==97:
            return s
        v = h[y][x]
        ns = s+1
        for dy,dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<=ny<H and 0<=nx<W and seen[ny][nx]==-1 and v-h[ny][nx]<=1:
                seen[ny][nx]=ns
                dq.append((ny,nx,ns))

with open(sys.argv[1]) as f:
    data = [list(line.strip()) for line in f]
H, W = len(data), len(data[0])
h = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        c = data[i][j]
        if c=='S':
            start = (i,j); c='a'
        if c=='E':
            target = (i,j); c='z'
        h[i][j] = ord(c)
res1 = part1(h, H, W, start, target)
res2 = part2(h, H, W, target)
sys.stdout.write(f"{res1}\n{res2}\n")