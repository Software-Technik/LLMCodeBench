import sys
d={'R':(1,0),'L':(-1,0),'D':(0,1),'U':(0,-1)}
kb1=['123','456','789']
kb2=['00100','02340','56789','0ABC0','00D00']
x1=y1=0
x2=-2; y2=0
c1=[]; c2=[]
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        for ch in line:
            dx,dy=d[ch]
            nx=x1+dx; ny=y1+dy
            if -1<=nx<=1 and -1<=ny<=1:
                x1,y1=nx,ny
            nx=x2+dx; ny=y2+dy
            if abs(nx)+abs(ny)<=2:
                x2,y2=nx,ny
        c1.append(kb1[y1+1][x1+1])
        c2.append(kb2[y2+2][x2+2])
sys.stdout.write(''.join(c1)+' '+''.join(c2))