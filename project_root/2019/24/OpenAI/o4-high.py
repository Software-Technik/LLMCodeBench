import sys
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
flat_neighbors = [[] for _ in range(25)]
for i in range(25):
    x=i%5; y=i//5
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0<=nx<5 and 0<=ny<5:
            flat_neighbors[i].append(ny*5+nx)
neighbor_mask = [0]*25
for i in range(25):
    m=0
    for j in flat_neighbors[i]:
        m|=1<<j
    neighbor_mask[i]=m
rec_neighbors = [[] for _ in range(25)]
for i in range(25):
    if i==12: continue
    x=i%5; y=i//5
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if nx<0:
            rec_neighbors[i].append((1,11))
        elif nx>4:
            rec_neighbors[i].append((1,13))
        elif ny<0:
            rec_neighbors[i].append((1,7))
        elif ny>4:
            rec_neighbors[i].append((1,17))
        elif nx==2 and ny==2:
            if dx==1:
                for jj in (0,5,10,15,20):
                    rec_neighbors[i].append((-1,jj))
            elif dx==-1:
                for jj in (4,9,14,19,24):
                    rec_neighbors[i].append((-1,jj))
            elif dy==1:
                for jj in (0,1,2,3,4):
                    rec_neighbors[i].append((-1,jj))
            elif dy==-1:
                for jj in (20,21,22,23,24):
                    rec_neighbors[i].append((-1,jj))
        else:
            rec_neighbors[i].append((0,ny*5+nx))
def part1(data):
    mask=0
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if c=='#': mask|=1<<(y*5+x)
    seen=set()
    while mask not in seen:
        seen.add(mask)
        nm=0
        for i in range(25):
            cnt=(mask&neighbor_mask[i]).bit_count()
            if (mask>>i)&1:
                if cnt==1: nm|=1<<i
            else:
                if cnt==1 or cnt==2: nm|=1<<i
        mask=nm
    return mask
def part2(data):
    init=0
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if c=='#': init|=1<<(y*5+x)
    levels={0:init}
    for minute in range(1,201):
        nl={}
        for d in range(-minute,minute+1):
            old=levels.get(d,0); nm=0
            for i in range(25):
                if i==12: continue
                cnt=0
                for dd,j in rec_neighbors[i]:
                    if (levels.get(d+dd,0)>>j)&1: cnt+=1
                if (old>>i)&1:
                    if cnt==1: nm|=1<<i
                else:
                    if cnt==1 or cnt==2: nm|=1<<i
            if nm: nl[d]=nm
        levels=nl
    t=0
    for m in levels.values(): t+=m.bit_count()
    return t
data = open(sys.argv[1]).read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")