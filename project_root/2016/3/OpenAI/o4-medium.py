import sys
p1=p2=0
buf=[]
with open(sys.argv[1]) as f:
    for line in f:
        a,b,c=map(int,line.split())
        s=a+b+c; m=max(a,b,c)
        if s>2*m: p1+=1
        buf.append((a,b,c))
        if len(buf)==3:
            (a1,b1,c1),(a2,b2,c2),(a3,b3,c3)=buf
            for u,v,w in ((a1,a2,a3),(b1,b2,b3),(c1,c2,c3)):
                if u+v+w>2*max(u,v,w): p2+=1
            buf=[]
sys.stdout.write(f"{p1} {p2}")