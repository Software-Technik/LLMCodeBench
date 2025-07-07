import sys
from collections import deque

def parse(lines):
    grid, moves = [], []
    for line in lines:
        line = line.rstrip('\n')
        if line and line[0] in '.#@O':
            grid.append(list(line))
        elif line:
            moves = list(line)
    return grid, moves

def part1(grid, moves):
    R, C = len(grid), len(grid[0])
    for r in range(R):
        grid[r] += ['.']*(50-C)
    C = 50
    for move in moves:
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='@':
                    rr,cc=r,c; break
            else: continue
            break
        dr,dc = {'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}[move]
        nr,nc = rr+dr, cc+dc
        if grid[nr][nc]=='.':
            grid[rr][cc], grid[nr][nc] = '.', '@'
        elif grid[nr][nc]=='O':
            orr,occ = dr,dc
            while True:
                orr += dr; occ += dc
                r2,c2 = rr+orr, cc+occ
                if grid[r2][c2]=='#': break
                if grid[r2][c2]=='.':
                    grid[rr][cc]='.'
                    grid[rr+dr][cc+dc]='@'
                    grid[r2][c2]='O'
                    break
    return sum(r*100+c for r in range(R) for c in range(C) if grid[r][c]=='O')

def part2(grid0, moves):
    R0,C0 = len(grid0), len(grid0[0])
    R, C = R0, 2*C0
    grid = [['.']*C for _ in range(R)]
    for r in range(R0):
        for c in range(C0):
            ch=grid0[r][c]
            if ch=='#': grid[r][2*c:2*c+2]=['#','#']
            elif ch=='O': grid[r][2*c:2*c+2]=['[',']']
            elif ch=='@': grid[r][2*c:2*c+2]=['@','.']
    drdc = {'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}
    for move in moves:
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='@':
                    rr,cc=r,c; break
            else: continue
            break
        dr,dc = drdc[move]
        nr,nc = rr+dr, cc+dc
        if grid[nr][nc]=='.':
            grid[rr][cc], grid[nr][nc] = '.', '@'
        elif grid[nr][nc] in '[]':
            if dc==0:
                # up/down
                visited=set()
                q=deque([(nr,nc)])
                while q:
                    x,y=q.popleft()
                    if (x,y) in visited: continue
                    visited.add((x,y))
                    for nx,ny in [(x+dr,y+dc)]:
                        if 0<=nx<R and 0<=ny<C:
                            if grid[nx][ny] in '[]': q.append((nx,ny))
                            if grid[nx][ny]=='#': visited=None; q.clear(); break
                if not visited: continue
                boxes=sorted(visited, key=lambda p:p[0], reverse=(dr>0))
                for x,y in boxes:
                    grid[x+dr][y+dc]=grid[x][y]; grid[x][y]='.'
                grid[rr][cc]='.'; grid[nr][nc]='@'
            else:
                seq=[]
                y=dc
                while True:
                    if grid[rr][cc+y]=='#': break
                    seq.append((rr,cc+y))
                    if grid[rr][cc+y]=='.':
                        for i in range(len(seq)-1,0,-1):
                            x0,y0=seq[i-1]; x1,y1=seq[i]
                            grid[x1][y1]=grid[x0][y0]
                        grid[rr][cc]='.'; grid[rr][cc+seq[0][1]-cc]='@'
                        break
                    y+=dc
    return sum(r*100+c for r in range(R) for c in range(C) if grid[r][c]==']')

if __name__=='__main__':
    lines = open(sys.argv[1]).readlines()
    g,m = parse(lines)
    g1 = [row[:] for row in g]
    print(part1(g1, m), part2(g, m))