import sys
infile=sys.argv[1]
d1={'U':(-1,0),'D':(1,0),'R':(0,1),'L':(0,-1)}
d2=[(0,1),(1,0),(0,-1),(-1,0)]
c1=c2=s1=s2=0
x1=y1=x2=y2=0
with open(infile) as f:
    for L in f:
        D=L[0]
        p=L.find(' ',2)
        n=int(L[2:p])
        dx,dy=d1[D]
        nx=x1+dx*n; ny=y1+dy*n
        c1+=x1*ny-nx*y1
        x1,y1=nx,ny
        s1+=n
        i=L.find('#',p)+1
        j=L.find(')',i)
        H=L[i:j]
        t=ord(H[-1])-48
        dx,dy=d2[t]
        m=int(H[:-1],16)
        nx2=x2+dx*m; ny2=y2+dy*m
        c2+=x2*ny2-nx2*y2
        x2,y2=nx2,ny2
        s2+=m
r1=(abs(c1)+s1+2)//2
r2=(abs(c2)+s2+2)//2
sys.stdout.write(f"{r1} {r2}")