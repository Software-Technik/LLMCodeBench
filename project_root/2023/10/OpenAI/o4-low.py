import sys

START="S";VPIPE="|";HPIPE="-";NE="L";NW="J";SE="F";SW="7";UP="up";DOWN="down";LEFT="left";RIGHT="right"
def get_start(maze):
    for i,row in enumerate(maze):
        j=row.find(START) if isinstance(row,str) else next((k for k,c in enumerate(row) if c==START),-1)
        if j>=0: return i,j
    return 0,0
def part1(text):
    maze=text.splitlines();h=len(maze);w=len(maze[0])
    i,j=get_start(maze);d=None
    if i>0 and maze[i-1][j] in [VPIPE,SE,SW]: i,d=i-1,UP
    elif i<h-1 and maze[i+1][j] in [VPIPE,NE,NW]: i,d=i+1,DOWN
    elif j>0 and maze[i][j-1] in [HPIPE,SE,NE]: j,d=j-1,LEFT
    elif j<w-1 and maze[i][j+1] in [HPIPE,SW,NW]: j,d=j+1,RIGHT
    steps=1
    while maze[i][j]!=START:
        p=maze[i][j]
        if p==VPIPE: i+=-1 if d==UP else 1
        elif p==HPIPE: j+=-1 if d==LEFT else 1
        elif p==SE:
            if d==UP: j,d=j+1,RIGHT
            else: i,d=i+1,DOWN
        elif p==SW:
            if d==UP: j,d=j-1,LEFT
            else: i,d=i+1,DOWN
        elif p==NW:
            if d==DOWN: j,d=j-1,LEFT
            else: i,d=i-1,UP
        elif p==NE:
            if d==DOWN: j,d=j+1,RIGHT
            else: i,d=i-1,UP
        steps+=1
    return steps//2
def get_edges(inter):
    e=[];n=len(inter)
    for i in range(n):
        a,b=inter[i],inter[(i+1)%n]
        if a[0]==b[0]: continue
        e.append((a,b) if a[0]<b[0] else (b,a))
    return e
def part2(text):
    maze=[list(line) for line in text.splitlines()]
    h=len(maze);w=len(maze[0])
    i,j=get_start(maze);inter=[(i,j)];d=None
    if i>0 and maze[i-1][j] in [VPIPE,SE,SW]: i,d=i-1,UP
    elif i<h-1 and maze[i+1][j] in [VPIPE,NE,NW]: i,d=i+1,DOWN
    elif j>0 and maze[i][j-1] in [HPIPE,SE,NE]: j,d=j-1,LEFT
    elif j<w-1 and maze[i][j+1] in [HPIPE,SW,NW]: j,d=j+1,RIGHT
    while maze[i][j]!=START:
        p=maze[i][j];maze[i][j]="X"
        if p in (SE,SW,NW,NE): inter.append((i,j))
        if p==VPIPE: i+=-1 if d==UP else 1
        elif p==HPIPE: j+=-1 if d==LEFT else 1
        elif p==SE:
            if d==UP: j,d=j+1,RIGHT
            else: i,d=i+1,DOWN
        elif p==SW:
            if d==UP: j,d=j-1,LEFT
            else: i,d=i+1,DOWN
        elif p==NW:
            if d==DOWN: j,d=j-1,LEFT
            else: i,d=i-1,UP
        elif p==NE:
            if d==DOWN: j,d=j+1,RIGHT
            else: i,d=i-1,UP
    maze[inter[0][0]][inter[0][1]]="X"
    edges=get_edges(inter)
    ys=sorted(y for y,_ in inter);miny,maxy=ys[0],ys[-1]
    total=0
    for y in range(miny+1,maxy):
        act=[e for e in edges if e[0][0]<=y<e[1][0]]
        act.sort(key=lambda x:x[0][1])
        for k in range(0,len(act),2):
            a=act[k][0][1];b=act[k+1][0][1]
            for x in range(a+1,b):
                if maze[y][x]!="X": total+=1
    return total

if __name__=="__main__":
    txt=open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(txt)} {part2(txt)}")