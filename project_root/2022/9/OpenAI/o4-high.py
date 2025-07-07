import sys
directions={'R':(1,0),'L':(-1,0),'U':(0,-1),'D':(0,1)}
def simulate(moves,k):
    xs=[0]*k; ys=[0]*k; seen={(0,0)}
    for dx,dy,n in moves:
        for _ in range(n):
            xs[0]+=dx; ys[0]+=dy
            for i in range(k-1):
                w=xs[i]-xs[i+1]; h=ys[i]-ys[i+1]
                if w*w>1 or h*h>1:
                    xs[i+1]+= (w>0)-(w<0); ys[i+1]+= (h>0)-(h<0)
            seen.add((xs[-1],ys[-1]))
    return len(seen)
with open(sys.argv[1]) as f:
    data=f.read().split()
moves=[]
it=iter(data)
for d,n in zip(it,it):
    dx,dy=directions[d]; moves.append((dx,dy,int(n)))
sys.stdout.write(str(simulate(moves,2))+"\n"+str(simulate(moves,10))+"\n")