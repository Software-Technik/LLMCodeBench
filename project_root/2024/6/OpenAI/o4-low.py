import sys

def run(grid):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                return i, j
    return -1, -1

def steps(grid, si, sj):
    n = len(grid)
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    i, j, d = si, sj, 0
    seen = set()
    while (i,j) not in seen:
        seen.add((i,j))
        ni, nj = i+dd[d][0], j+dd[d][1]
        if not (0<=ni<n and 0<=nj<n): break
        if grid[ni][nj]=="#":
            d = (d+1)%4
        else:
            i, j = ni, nj
    return len(seen)

def loops(grid, si, sj, oi, oj):
    if grid[oi][oj]=="#": return False
    grid[oi][oj]="#"
    n = len(grid)
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    i, j, d = si, sj, 0
    seen = set()
    while True:
        key = (i,j,d)
        if key in seen:
            grid[oi][oj]="."
            return True
        seen.add(key)
        ni, nj = i+dd[d][0], j+dd[d][1]
        if not (0<=ni<n and 0<=nj<n):
            grid[oi][oj]="."
            return False
        if grid[ni][nj]=="#":
            d = (d+1)%4
        else:
            i, j = ni, nj

def main(path):
    with open(path) as f:
        lines = f.read().splitlines()
    grid1 = lines
    si, sj = run(grid1)
    p1 = steps(grid1, si, sj)
    grid2 = [list(r) for r in lines]
    si, sj = run(grid2)
    n = len(grid2)
    og = set()
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    i, j, d = si, sj, 0
    while (i,j) not in og:
        og.add((i,j))
        ni, nj = i+dd[d][0], j+dd[d][1]
        if not (0<=ni<n and 0<=nj<n): break
        if grid2[ni][nj]=="#":
            d=(d+1)%4
        else:
            i, j = ni, nj
    p2 = 0
    for oi, oj in og:
        if (oi,oj)==(si,sj): continue
        if loops(grid2, si, sj, oi, oj):
            p2+=1
    print(p1, p2)

if __name__=="__main__":
    main(sys.argv[1])