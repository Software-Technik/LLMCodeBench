import sys
data = sys.stdin if len(sys.argv)==1 else open(sys.argv[1])
off = 1000
rock = set()
maxy = 0
for line in data:
    line=line.strip()
    if not line: continue
    pts = [tuple(map(int,p.split(','))) for p in line.split('->')]
    for (x1,y1),(x2,y2) in zip(pts,pts[1:]):
        if x1==x2:
            y0,y3 = sorted((y1,y2))
            for y in range(y0,y3+1):
                rock.add(((x1+off)<<16)|y)
                if y>maxy: maxy=y
        else:
            x0,x3 = sorted((x1,x2))
            for x in range(x0,x3+1):
                rock.add(((x+off)<<16)|y1)
    if pts:
        for _,y in pts:
            if y>maxy: maxy=y
ground = maxy+2
d0 = 1
d1 = (-1<<16)|1
d2 = (1<<16)|1
base = (500+off)<<16
rest = set()
count1 = 0
while True:
    p = base
    while True:
        for d in (d0,d1,d2):
            np = p + d
            y = np & 0xFFFF
            if y<=maxy and np not in rock and np not in rest:
                p = np
                break
        else:
            rest.add(p); count1+=1
            break
        if y>maxy:
            break
    if y>maxy:
        break
rest.clear()
count2 = 0
while True:
    p = base
    while True:
        for d in (d0,d1,d2):
            np = p + d
            y = np & 0xFFFF
            if y<ground and np not in rock and np not in rest:
                p = np
                break
        else:
            rest.add(p); count2+=1
            break
    if p==base:
        break
sys.stdout.write(f"{count1}\n{count2}\n")