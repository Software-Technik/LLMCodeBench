import sys
data = open(sys.argv[1]).read().splitlines()
deltas = [(-1,0),(1,0),(0,-1),(0,1)]
p1_nmask = [0]*25
p2_self = [0]*25
outer = [0]*25
inner = [0]*25
for idx in range(25):
    x, y = idx%5, idx//5
    for dx,dy in deltas:
        nx, ny = x+dx, y+dy
        if 0<=nx<5 and 0<=ny<5:
            j = ny*5+nx
            p1_nmask[idx] |= 1<<j
            if j!=12: p2_self[idx] |= 1<<j
            if j==12:
                if dx==1: inner[idx] |= sum(1<<(i*5+0) for i in range(5))
                if dx==-1: inner[idx] |= sum(1<<(i*5+4) for i in range(5))
                if dy==1: inner[idx] |= sum(1<<i for i in range(5))
                if dy==-1: inner[idx] |= sum(1<<i for i in range(20,25))
        else:
            if dy==-1: outer[idx] |= 1<<7
            if dy==1: outer[idx] |= 1<<17
            if dx==-1: outer[idx] |= 1<<11
            if dx==1: outer[idx] |= 1<<13
def part1():
    mask=0
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if c=='#': mask|=1<<(y*5+x)
    seen=set()
    while mask not in seen:
        seen.add(mask)
        nm=0
        for i in range(25):
            cnt=(mask&p1_nmask[i]).bit_count()
            if mask>>i&1:
                if cnt==1: nm|=1<<i
            else:
                if cnt==1 or cnt==2: nm|=1<<i
        mask=nm
    return mask
def part2():
    levels={0:0}
    m0=0
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if c=='#': m0|=1<<(y*5+x)
    levels[0]=m0
    for _ in range(200):
        nd={}
        keys=list(levels.keys())
        lo,hi=min(keys)-1,max(keys)+1
        for d in range(lo,hi+1):
            m=levels.get(d,0)
            po=levels.get(d+1,0)
            pi=levels.get(d-1,0)
            nm=0
            for i in range(25):
                if i==12: continue
                cnt=(m&p2_self[i]).bit_count()+(po&outer[i]).bit_count()+(pi&inner[i]).bit_count()
                if m>>i&1:
                    if cnt==1: nm|=1<<i
                else:
                    if cnt==1 or cnt==2: nm|=1<<i
            nd[d]=nm
        levels=nd
    return sum(v.bit_count() for v in levels.values())
print(f"{part1()} {part2()}")