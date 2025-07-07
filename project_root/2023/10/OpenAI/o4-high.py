import sys

S='S';V='|';H='-';NE='L';NW='J';SE='F';SW='7'
SU={V,SE,SW};SD={V,NE,NW};SL={H,SE,NE};SR={H,SW,NW}

def get_start(grid):
    for i,row in enumerate(grid):
        try:
            j=row.index(S)
            return i,j
        except ValueError:
            pass
    return 0,0

def part1(lines):
    i,j=get_start(lines)
    d=None
    if i>0 and lines[i-1][j] in SU:
        i-=1;d=0
    elif i<len(lines)-1 and lines[i+1][j] in SD:
        i+=1;d=1
    elif j>0 and lines[i][j-1] in SL:
        j-=1;d=2
    elif j<len(lines[i])-1 and lines[i][j+1] in SR:
        j+=1;d=3
    steps=1
    while lines[i][j]!=S:
        c=lines[i][j]
        if c==V:
            i+= -1 if d==0 else 1
        elif c==H:
            j+= -1 if d==2 else 1
        elif c==SE:
            if d==0:
                j+=1;d=3
            else:
                i+=1;d=1
        elif c==SW:
            if d==0:
                j-=1;d=2
            else:
                i+=1;d=1
        elif c==NW:
            if d==1:
                j-=1;d=2
            else:
                i-=1;d=0
        else:
            if d==1:
                j+=1;d=3
            else:
                i-=1;d=0
        steps+=1
    return steps//2

def get_edges(pts):
    e=[];n=len(pts)
    for k in range(n):
        a=pts[k];b=pts[(k+1)%n]
        if a[0]==b[0]:
            continue
        if a[0]<b[0]:
            e.append((a,b))
        else:
            e.append((b,a))
    return e

def part2(lines):
    grid=[list(row) for row in lines]
    i,j=get_start(grid)
    d=None
    pts=[(i,j)]
    if i>0 and grid[i-1][j] in SU:
        i-=1;d=0
    elif i<len(grid)-1 and grid[i+1][j] in SD:
        i+=1;d=1
    elif j>0 and grid[i][j-1] in SL:
        j-=1;d=2
    elif j<len(grid[i])-1 and grid[i][j+1] in SR:
        j+=1;d=3
    while grid[i][j]!=S:
        c=grid[i][j];grid[i][j]='X'
        if c==V:
            i+= -1 if d==0 else 1
        elif c==H:
            j+= -1 if d==2 else 1
        elif c==SE:
            pts.append((i,j))
            if d==0:
                j+=1;d=3
            else:
                i+=1;d=1
        elif c==SW:
            pts.append((i,j))
            if d==0:
                j-=1;d=2
            else:
                i+=1;d=1
        elif c==NW:
            pts.append((i,j))
            if d==1:
                j-=1;d=2
            else:
                i-=1;d=0
        else:
            pts.append((i,j))
            if d==1:
                j+=1;d=3
            else:
                i-=1;d=0
    grid[i][j]='X'
    edges=get_edges(pts)
    pts.sort()
    min_y=pts[0][0];max_y=pts[-1][0]
    total=0
    for y in range(min_y+1,max_y):
        active=[edge for edge in edges if edge[0][0]<=y<edge[1][0]]
        active.sort(key=lambda e:e[0][1])
        for k in range(0,len(active),2):
            a=active[k][0][1];b=active[k+1][0][1]
            for x in range(a+1,b):
                if grid[y][x]!='X':
                    total+=1
    return total

if __name__=='__main__':
    p=sys.argv[1]
    with open(p) as f:
        lines=f.read().splitlines()
    sys.stdout.write(f"{part1(lines)} {part2(lines)}")