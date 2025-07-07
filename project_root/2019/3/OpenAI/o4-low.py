import sys

dirs = {'U':(0,-1),'R':(1,0),'D':(0,1),'L':(-1,0)}
with open(sys.argv[1]) as f:
    a,b = f.read().splitlines()
dict1 = {}
x=y=cost=0
for instr in a.split(','):
    dx,dy=dirs[instr[0]];steps=int(instr[1:])
    for _ in range(steps):
        cost+=1; x+=dx; y+=dy
        dict1.setdefault((x,y),cost)
best_dist=10**18; best_cost=10**18
x=y=cost=0
for instr in b.split(','):
    dx,dy=dirs[instr[0]];steps=int(instr[1:])
    for _ in range(steps):
        cost+=1; x+=dx; y+=dy
        p=(x,y)
        if p in dict1:
            d=abs(x)+abs(y)
            if d<best_dist: best_dist=d
            s=cost+dict1[p]
            if s<best_cost: best_cost=s
sys.stdout.write(f"{best_dist} {best_cost}")