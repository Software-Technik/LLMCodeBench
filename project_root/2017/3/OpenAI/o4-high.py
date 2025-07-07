import sys,math

def manhattan_distance(n):
    if n==1: return 0
    l=(math.isqrt(n-1)+1)//2
    s=2*l
    m=(2*l+1)**2
    o=(m-n)%s
    return l+abs(o-l)

def spiral_sum(th):
    g={(0,0):1}
    x=y=0
    dx,dy=1,0
    st=1
    get=g.get
    while True:
        for _ in range(2):
            for _ in range(st):
                x+=dx; y+=dy
                v = get((x-1,y-1),0)+get((x-1,y),0)+get((x-1,y+1),0)+get((x,y-1),0)+get((x,y+1),0)+get((x+1,y-1),0)+get((x+1,y),0)+get((x+1,y+1),0)
                g[(x,y)]=v
                if v>th: return v
            dx,dy=-dy,dx
        st+=1

def main():
    n=int(open(sys.argv[1]).read().strip())
    print(manhattan_distance(n))
    print(spiral_sum(n))

if __name__=="__main__":
    main()