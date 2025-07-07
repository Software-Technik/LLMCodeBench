import sys
from collections import deque

data = open(sys.argv[1]).read().splitlines()
coords = [tuple(map(int, line.split(','))) for line in data]
droplets = set(coords)
neighbors = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))

sides1 = 0
for x,y,z in coords:
    for dx,dy,dz in neighbors:
        if (x+dx,y+dy,z+dz) not in droplets:
            sides1 += 1

xs, ys, zs = zip(*coords)
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)
min_z, max_z = min(zs), max(zs)
xr = range(min_x-1, max_x+2)
yr = range(min_y-1, max_y+2)
zr = range(min_z-1, max_z+2)

start = (min_x-1, min_y-1, min_z-1)
dq = deque([start])
seen = set(droplets)
sides2 = 0

while dq:
    x,y,z = dq.popleft()
    if (x,y,z) in seen: continue
    seen.add((x,y,z))
    for dx,dy,dz in neighbors:
        nx,ny,nz = x+dx, y+dy, z+dz
        if (nx,ny,nz) in droplets:
            sides2 += 1
        elif (nx,ny,nz) not in seen and nx in xr and ny in yr and nz in zr:
            dq.append((nx,ny,nz))

sys.stdout.write(f"{sides1}\n{sides2}\n")