import sys
m={'U':(0,-1),'D':(0,1),'L':(-1,0),'R':(1,0)}
k1=["123","456","789"]
k2=["00100","02340","56789","0ABC0","00D00"]
p1x,p1y=1,1
p2x,p2y=0,2
r1=[]
r2=[]
with open(sys.argv[1]) as f:
    for line in f:
        for c in line.strip():
            dx,dy=m[c]
            nx,ny=p1x+dx,p1y+dy
            if 0<=nx<3 and 0<=ny<3:p1x,p1y=nx,ny
            nx,ny=p2x+dx,p2y+dy
            if 0<=nx<5 and 0<=ny<5 and k2[ny][nx]!="0":p2x,p2y=nx,ny
        r1.append(k1[p1y][p1x])
        r2.append(k2[p2y][p2x])
sys.stdout.write("".join(r1)+" "+ "".join(r2))