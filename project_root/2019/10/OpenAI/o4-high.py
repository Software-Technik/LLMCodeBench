import sys, math
data = open(sys.argv[1]).read().splitlines()
positions = [(x,y) for y,row in enumerate(data) for x,ch in enumerate(row) if ch=='#']
gcd = math.gcd; atan2 = math.atan2; pi2 = 2*math.pi
best = 0; station = None
for sx,sy in positions:
    dirs = set()
    for x,y in positions:
        if x!=sx or y!=sy:
            dx = x-sx; dy = y-sy
            g = gcd(dx,dy)
            dirs.add((dx//g, dy//g))
    if len(dirs) > best:
        best = len(dirs); station = (sx,sy)
sx,sy = station
mapping = {}
for x,y in positions:
    if x!=sx or y!=sy:
        dx = x-sx; dy = y-sy
        g = gcd(dx,dy)
        d = (dx//g, dy//g)
        mapping.setdefault(d, []).append((dx*dx+dy*dy, x, y))
for v in mapping.values():
    v.sort()
angle_list = []
for d in mapping:
    a = atan2(d[0], -d[1])
    if a < 0: a += pi2
    angle_list.append((a, d))
angle_list.sort()
angles = [d for a,d in angle_list]
count = 0
while True:
    for d in angles:
        if mapping[d]:
            _, x, y = mapping[d].pop(0)
            count += 1
            if count == 200:
                sys.stdout.write(f"{best} {x*100+y}")
                sys.exit()