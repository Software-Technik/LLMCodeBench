import sys
d={"n":(0,-1),"nw":(-1,0),"sw":(-1,1),"s":(0,1),"se":(1,0),"ne":(1,-1)}
with open(sys.argv[1]) as f:
    steps=f.read().strip().split(",")
x=y=mx=0
for s in steps:
    dx,dy=d[s]
    x+=dx; y+=dy
    a=abs(x); b=abs(y); c=abs(x+y)
    dist=a if a>b and a>c else b if b>c else c
    if dist>mx: mx=dist
a=abs(x); b=abs(y); c=abs(x+y)
final=a if a>b and a>c else b if b>c else c
print(final)
print(mx)