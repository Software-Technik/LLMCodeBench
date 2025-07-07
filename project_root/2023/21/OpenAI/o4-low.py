import sys
def parse(text):
    grid=set()
    for y,line in enumerate(text.strip().splitlines()):
        for x,c in enumerate(line):
            if c=='#': grid.add(x+y*1j)
            elif c=='S': start=x+y*1j
    width=len(text.strip().splitlines()[0])
    return grid,start,width
def part1(text):
    grid,start,_=parse(text)
    curr={start}
    for _ in range(64):
        nxt=set()
        for p in curr:
            for d in (1,-1,1j,-1j):
                q=p+d
                if q not in grid: nxt.add(q)
        curr=nxt
    return len(curr)
def part2(text):
    grid,start,L=parse(text)
    curr={start}
    pts=[]
    half=L//2
    step=0
    while len(pts)<3:
        nxt=set()
        for p in curr:
            for d in (1,-1,1j,-1j):
                q=p+d
                x=q.real%L; y=q.imag%L
                if (x+y*1j) not in grid: nxt.add(q)
        step+=1
        if (step-half)%L==0: pts.append(len(nxt))
        curr=nxt
    c,b=a=None,None
    c=pts[0]; b=pts[1]-pts[0]; a=pts[2]-pts[1]
    T=26501365
    x=T//L
    return c+b*x+(x*(x-1)//2)*(a-b)
if __name__=='__main__':
    text=open(sys.argv[1]).read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")