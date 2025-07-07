import sys

data = open(sys.argv[1]).read().splitlines()

# Part 1 using bitmask
adj = []
for i in range(25):
    x, y = i % 5, i // 5
    nbrs = []
    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            nbrs.append(ny*5+nx)
    adj.append(tuple(nbrs))

mask = 0
for i, c in enumerate("".join(data)):
    if c == '#': mask |= 1<<i

seen = set()
while mask not in seen:
    seen.add(mask)
    nm = 0
    for i in range(25):
        cnt = sum((mask>>j)&1 for j in adj[i])
        if (mask>>i)&1:
            if cnt == 1: nm |= 1<<i
        else:
            if cnt in (1,2): nm |= 1<<i
    mask = nm
p1 = sum(1<<i for i in range(25) if (mask>>i)&1)

# Part 2
def create(level):
    d = {}
    for y,line in enumerate(level):
        for x,c in enumerate(line):
            d[x,y] = c
    d[(2,2)]='?'
    return d

levels = {0:create(data)}
empty = create(["....."]*5)

def nbrs(levels, r, p):
    x,y = p
    res = []
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx,ny = x+dx,y+dy
        if (nx,ny)==(2,2): continue
        if 0<=nx<5 and 0<=ny<5:
            res.append(levels[r][(nx,ny)])
    if r+1 in levels:
        if y==0: res.append(levels[r+1][(2,1)])
        if y==4: res.append(levels[r+1][(2,3)])
        if x==0: res.append(levels[r+1][(1,2)])
        if x==4: res.append(levels[r+1][(3,2)])
    if r-1 in levels:
        up = levels[r-1]
        if p==(2,1): res += [up[(i,0)] for i in range(5)]
        if p==(1,2): res += [up[(0,i)] for i in range(5)]
        if p==(3,2): res += [up[(4,i)] for i in range(5)]
        if p==(2,3): res += [up[(i,4)] for i in range(5)]
    return res

for _ in range(200):
    nl = {}
    for d in range(-_ -1, _ +2):
        if d not in levels: levels[d]=empty.copy()
        L = levels[d]
        new = {}
        for p,v in L.items():
            cnt = sum(1 for c in nbrs(levels,d,p) if c=='#')
            if v=='#':
                new[p] = '#' if cnt==1 else '.'
            elif v=='.':
                new[p] = '#' if cnt in (1,2) else '.'
            else:
                new[p] = v
        nl[d]=new
    levels = nl

p2 = sum(1 for d in levels for v in levels[d].values() if v=='#')
print(p1, p2)