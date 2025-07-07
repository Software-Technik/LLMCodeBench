import sys
g = open(sys.argv[1]).read().strip().splitlines()
n = len(g)
m = {}
for i,row in enumerate(g):
    for j,c in enumerate(row):
        if c!='.': m.setdefault(c,[]).append((i,j))
vals = list(m.values())
ant1 = set(); a1 = ant1.add
for locs in vals:
    L = len(locs)
    for i in range(L):
        x1,y1 = locs[i]
        for j in range(i+1,L):
            x2,y2 = locs[j]
            dx = x2-x1; dy = y2-y1
            cx = x1-dx; cy = y1-dy
            if 0<=cx<n and 0<=cy<n: a1((cx,cy))
            ex = x2+dx; ey = y2+dy
            if 0<=ex<n and 0<=ey<n: a1((ex,ey))
ans1 = len(ant1)
ant2 = set(); a2 = ant2.add
for locs in vals:
    L = len(locs)
    for i in range(L):
        x1,y1 = locs[i]
        for j in range(i+1,L):
            x2,y2 = locs[j]
            dx = x2-x1; dy = y2-y1
            if dx>0: mkx = x1//dx
            elif dx<0: mkx = (n-1-x1)//(-dx)
            else: mkx = n
            if dy>0: mky = y1//dy
            elif dy<0: mky = (n-1-y1)//(-dy)
            else: mky = n
            k = mkx if mkx<mky else mky
            for t in range(k+1): a2((x1-dx*t, y1-dy*t))
            if dx>0: mkx = (n-1-x2)//dx
            elif dx<0: mkx = x2//(-dx)
            else: mkx = n
            if dy>0: mky = (n-1-y2)//dy
            elif dy<0: mky = y2//(-dy)
            else: mky = n
            k = mkx if mkx<mky else mky
            for t in range(k+1): a2((x2+dx*t, y2+dy*t))
ans2 = len(ant2)
print(ans1, ans2)