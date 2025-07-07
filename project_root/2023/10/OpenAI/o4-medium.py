import sys
def get_start(maze):
    for i,row in enumerate(maze):
        for j,c in enumerate(row):
            if c=='S': return i,j
    return 0,0
moves={'up':(-1,0),'down':(1,0),'left':(0,-1),'right':(0,1)}
transitions={
    '|':{'up':('up',-1,0),'down':('down',1,0)},
    '-':{'left':('left',0,-1),'right':('right',0,1)},
    'L':{'down':('right',0,1),'left':('up',-1,0)},
    'J':{'down':('left',0,-1),'right':('up',-1,0)},
    'F':{'up':('right',0,1),'left':('down',1,0)},
    '7':{'up':('left',0,-1),'right':('down',1,0)}
}
corners={'L','J','F','7'}
def walk(maze,start,record):
    si,sj=start
    for d,(dx,dy) in moves.items():
        i,j=si+dx,sj+dy
        if 0<=i<len(maze) and 0<=j<len(maze[i]):
            c=maze[i][j]
            if c in transitions and d in transitions[c]:
                direction=d; break
    steps=1; i,j=si+dx,sj+dy
    intersections=[start] if record else None
    while maze[i][j]!='S':
        c=maze[i][j]
        if record:
            maze[i][j]='X'
            if c in corners: intersections.append((i,j))
        nd,dx,dy=transitions[c][direction]
        direction=nd; i+=dx; j+=dy; steps+=1
    if record: maze[si][sj]='X'
    return steps,intersections
def get_edges(intersections):
    n=len(intersections)
    e=[]
    for k in range(n):
        a=intersections[k]; b=intersections[(k+1)%n]
        if a[0]==b[0]: continue
        e.append((a,b) if a[0]<b[0] else (b,a))
    return e
text=open(sys.argv[1]).read()
lines=text.splitlines()
start=get_start(lines)
steps,_=walk(lines,start,False)
p1=steps//2
maze2=[list(l) for l in lines]
_,ints=walk(maze2,start,True)
edges=get_edges(ints)
ys=[y for y,x in ints]
min_y,min_y2=min(ys),max(ys)
total=0
for y in range(min_y+1,min_y2):
    aedges=[e for e in edges if e[0][0]<=y<e[1][0]]
    aedges.sort(key=lambda e:e[0][1])
    for k in range(0,len(aedges),2):
        x1=aedges[k][0][1]; x2=aedges[k+1][0][1]
        for x in range(x1+1,x2):
            if maze2[y][x]!='X': total+=1
print(f"{p1} {total}")