import sys,math

def manhattan_distance(n):
    if n==1: return 0
    layer=math.ceil((math.sqrt(n)-1)/2)
    side=2*layer
    maxv=(2*layer+1)**2
    back=(maxv-n)%side
    return layer+abs(back-layer)

def spiral_sum(th):
    deltas=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    g={(0,0):1}
    x=y=0
    dx,dy=1,0
    steps=1
    gget=g.get
    while True:
        for _ in range(2):
            for _ in range(steps):
                x+=dx; y+=dy
                s=0
                for dx2,dy2 in deltas:
                    s+=gget((x+dx2,y+dy2),0)
                if s>th: return s
                g[(x,y)]=s
            dx,dy=-dy,dx
        steps+=1

def main():
    with open(sys.argv[1]) as f:
        n=int(f.readline())
    print(manhattan_distance(n))
    print(spiral_sum(n))

if __name__=='__main__':
    main()