import sys,math
def manhattan_distance(n):
    if n==1: return 0
    l=math.ceil((math.sqrt(n)-1)/2)
    s=2*l
    m=(2*l+1)**2
    b=(m-n)%s
    return l+abs(b-l)
def spiral_sum(t):
    g={(0,0):1}
    x=y=0;dx=1;dy=0;st=1
    while 1:
        for _ in range(2):
            for __ in range(st):
                x+=dx; y+=dy
                v= g.get((x+1,y),0)+g.get((x+1,y+1),0)+g.get((x,y+1),0)+g.get((x-1,y+1),0)+g.get((x-1,y),0)+g.get((x-1,y-1),0)+g.get((x,y-1),0)+g.get((x+1,y-1),0)
                g[(x,y)]=v
                if v>t: return v
            dx,dy=-dy,dx
        st+=1
def part1(d): return manhattan_distance(int(d[0]))
def part2(d): return spiral_sum(int(d[0]))
f=open(sys.argv[1])
d=[l.strip() for l in f]
print(part1(d))
print(part2(d))