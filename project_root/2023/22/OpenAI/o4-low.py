import sys
from collections import deque

def run(text):
    data = [tuple(map(int, line.split("~")[0].split(",") + line.split("~")[1].split(","))) for line in text.strip().splitlines()]
    n = len(data)
    bricks = [list(d) + [i] for i, d in enumerate(data)]
    world = {}
    for x1,y1,z1,x2,y2,z2,i in bricks:
        if x1!=x2:
            for x in range(min(x1,x2),max(x1,x2)+1): world[(x,y1,z1)] = i
        elif y1!=y2:
            for y in range(min(y1,y2),max(y1,y2)+1): world[(x1,y,z1)] = i
        else:
            for z in range(min(z1,z2),max(z1,z2)+1): world[(x1,y1,z)] = i

    def cubes(b):
        x1,y1,z1,x2,y2,z2,i=b
        if x1!=x2:
            for x in range(min(x1,x2),max(x1,x2)+1): yield x,y1,z1
        elif y1!=y2:
            for y in range(min(y1,y2),max(y1,y2)+1): yield x1,y,z1
        else:
            for z in range(min(z1,z2),max(z1,z2)+1): yield x1,y1,z

    def is_falling(b, inv):
        x1,y1,z1,x2,y2,z2,i = b
        if i==inv: return False
        if z1!=z2:
            z=min(z1,z2)
            if z==1: return False
            below=world.get((x1,y1,z-1))
            return below is None or below==inv
        if z1==1: return False
        for x,y,z in cubes(b):
            below=world.get((x,y,z-1))
            if below is not None and below!=inv: return False
        return True

    def drop_tick(inv=-1):
        falling=set()
        maxz = max(z for _,_,z in world)
        minz = 1 if inv==-1 else max(data[inv][2],data[inv][5])+1
        for z in range(minz, maxz+1):
            for b in bricks:
                if b[2]==z or b[5]==z:
                    if is_falling(b,inv):
                        falling.add(b[6])
                        for x,y,zz in list(cubes(b)):
                            del world[(x,y,zz)]
                            world[(x,y,zz-1)] = b[6]
                        if inv==-1:
                            b[2]-=1; b[5]-=1
        return falling

    def drop_all():
        while drop_tick(): pass

    drop_all()
    p1=0
    w0=world.copy()
    bs0=[b[:] for b in bricks]
    for b in bricks:
        world=w0.copy(); bricks=bs0
        if not drop_tick(b[6]): p1+=1
    world=w0; bricks=bs0

    p2=0
    for b in bricks:
        w1=world.copy(); bs1=[b2[:] for b2 in bricks]
        f=set()
        while True:
            before=len(f)
            f |= drop_tick(b[6])
            if len(f)==before: break
        p2+=len(f)
        world=w1; bricks=bs1
    return p1, p2

if __name__=='__main__':
    text=open(sys.argv[1]).read()
    a,b=run(text)
    print(a, b)