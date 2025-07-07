import sys
h=v=0
buf=[]
with open(sys.argv[1]) as f:
    for line in f:
        x,y,z=map(int,line.split())
        if x+y>z and x+z>y and y+z>x: h+=1
        buf.append((x,y,z))
        if len(buf)==3:
            (a1,b1,c1),(a2,b2,c2),(a3,b3,c3)=buf
            s=a1+a2+a3; m=a1 if a1>=a2 and a1>=a3 else (a2 if a2>=a3 else a3)
            if s-m>m: v+=1
            s=b1+b2+b3; m=b1 if b1>=b2 and b1>=b3 else (b2 if b2>=b3 else b3)
            if s-m>m: v+=1
            s=c1+c2+c3; m=c1 if c1>=c2 and c1>=c3 else (c2 if c2>=c3 else c3)
            if s-m>m: v+=1
            buf.clear()
sys.stdout.write(f"{h} {v}")