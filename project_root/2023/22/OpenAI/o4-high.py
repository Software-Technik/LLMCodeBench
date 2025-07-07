import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    n = len(lines)
    bricks = [None]*n
    world = {}
    for i,line in enumerate(lines):
        a,b = line.split("~")
        x1,y1,z1 = map(int,a.split(","))
        x2,y2,z2 = map(int,b.split(","))
        bricks[i] = [x1,y1,z1,x2,y2,z2]
        if z1!=z2:
            zmin,zmax = (z1,z2) if z1<z2 else (z2,z1)
            for z in range(zmin,zmax+1):
                world[(x1,y1,z)] = i
        elif x1!=x2:
            xmin,xmax = (x1,x2) if x1<x2 else (x2,x1)
            for x in range(xmin,xmax+1):
                world[(x,y1,z1)] = i
        else:
            ymin,ymax = (y1,y2) if y1<y2 else (y2,y1)
            for y in range(ymin,ymax+1):
                world[(x1,y,z1)] = i

    def coords(b):
        x1,y1,z1,x2,y2,z2 = b
        if z1!=z2:
            zmin,zmax = (z1,z2) if z1<z2 else (z2,z1)
            return [(x1,y1,z) for z in range(zmin,zmax+1)]
        elif x1!=x2:
            xmin,xmax = (x1,x2) if x1<x2 else (x2,x1)
            return [(x,y1,z1) for x in range(xmin,xmax+1)]
        else:
            ymin,ymax = (y1,y2) if y1<y2 else (y2,y1)
            return [(x1,y,z1) for y in range(ymin,ymax+1)]

    def is_falling(i):
        x1,y1,z1,x2,y2,z2 = bricks[i]
        if z1!=z2:
            zmin = z1 if z1<z2 else z2
            if zmin==1: return False
            return (x1,y1,zmin-1) not in world
        else:
            if z1==1: return False
            if x1!=x2:
                xmin,xmax = (x1,x2) if x1<x2 else (x2,x1)
                for x in range(xmin,xmax+1):
                    if (x,y1,z1-1) in world: return False
                return True
            else:
                ymin,ymax = (y1,y2) if y1<y2 else (y2,y1)
                for y in range(ymin,ymax+1):
                    if (x1,y,z1-1) in world: return False
                return True

    while True:
        falling = [i for i in range(n) if is_falling(i)]
        if not falling: break
        for i in falling:
            for p in coords(bricks[i]):
                del world[p]
            bricks[i][2] -= 1
            bricks[i][5] -= 1
            for p in coords(bricks[i]):
                world[p] = i

    support = [set() for _ in range(n)]
    dependents = [[] for _ in range(n)]
    ground = [False]*n
    for i,b in enumerate(bricks):
        x1,y1,z1,x2,y2,z2 = b
        if z1!=z2:
            zmin = z1 if z1<z2 else z2
            if zmin==1:
                ground[i] = True
            else:
                s = world.get((x1,y1,zmin-1))
                if s is not None: support[i].add(s)
        else:
            if z1==1:
                ground[i] = True
            elif x1!=x2:
                xmin,xmax = (x1,x2) if x1<x2 else (x2,x1)
                for x in range(xmin,xmax+1):
                    s = world.get((x,y1,z1-1))
                    if s is not None: support[i].add(s)
            else:
                ymin,ymax = (y1,y2) if y1<y2 else (y2,y1)
                for y in range(ymin,ymax+1):
                    s = world.get((x1,y,z1-1))
                    if s is not None: support[i].add(s)
    for i,s in enumerate(support):
        for p in s:
            dependents[p].append(i)

    def falling_ids(removed):
        seen = set()
        q = []
        for b in dependents[removed]:
            if not ground[b] and support[b]=={removed}:
                seen.add(b); q.append(b)
        for idx in range(len(q)):
            f = q[idx]
            for b2 in dependents[f]:
                if not ground[b2] and b2 not in seen and not (support[b2] - seen - {removed}):
                    seen.add(b2); q.append(b2)
        return seen

    c1 = 0
    total = 0
    for i in range(n):
        f = falling_ids(i)
        if not f: c1 += 1
        total += len(f)
    sys.stdout.write(f"{c1} {total}")

if __name__=="__main__":
    main()