import sys
dirs={'n':(0,-1),'nw':(-1,0),'sw':(-1,1),'s':(0,1),'se':(1,0),'ne':(1,-1)}
x=y=0
maxd=0
with open(sys.argv[1]) as f:
    for d in f.read().strip().split(','):
        dx,dy=dirs[d]
        x+=dx; y+=dy
        d0=max(abs(x),abs(y),abs(x+y))
        if d0>maxd: maxd=d0
final=max(abs(x),abs(y),abs(x+y))
print(final)
print(maxd)