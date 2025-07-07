import sys
def part1(grid):
    h=len(grid); w=len(grid[0])
    left=[[0]*w for _ in range(h)]
    right=[[0]*w for _ in range(h)]
    top=[[0]*w for _ in range(h)]
    bottom=[[0]*w for _ in range(h)]
    for y in range(h):
        m=-1
        for x in range(w):
            left[y][x]=m
            v=grid[y][x]
            if v>m: m=v
        m=-1
        for x in range(w-1,-1,-1):
            right[y][x]=m
            v=grid[y][x]
            if v>m: m=v
    for x in range(w):
        m=-1
        for y in range(h):
            top[y][x]=m
            v=grid[y][x]
            if v>m: m=v
        m=-1
        for y in range(h-1,-1,-1):
            bottom[y][x]=m
            v=grid[y][x]
            if v>m: m=v
    c=0
    for y in range(h):
        for x in range(w):
            if grid[y][x]>min(left[y][x],right[y][x],top[y][x],bottom[y][x]):
                c+=1
    return c
def part2(grid):
    h=len(grid); w=len(grid[0])
    best=0
    for y in range(1,h-1):
        row=grid[y]
        for x in range(1,w-1):
            v=row[x]
            d=0
            for i in range(x-1,-1,-1):
                d+=1
                if row[i]>=v: break
            l=d
            d=0
            for i in range(x+1,w):
                d+=1
                if row[i]>=v: break
            r=d
            d=0
            for i in range(y-1,-1,-1):
                d+=1
                if grid[i][x]>=v: break
            u=d
            d=0
            for i in range(y+1,h):
                d+=1
                if grid[i][x]>=v: break
            dwn=d
            s=l*r*u*dwn
            if s>best: best=s
    return best
with open(sys.argv[1]) as f:
    grid=[[ord(c)-48 for c in line.strip()] for line in f]
sys.stdout.write(f"{part1(grid)}\n{part2(grid)}\n")