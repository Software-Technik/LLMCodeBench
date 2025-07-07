import sys
from collections import deque

NEIGHBORS = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))

def part1(droplets):
    sides = 0
    for x,y,z in droplets:
        for dx,dy,dz in NEIGHBORS:
            if (x+dx,y+dy,z+dz) not in droplets:
                sides += 1
    return sides

def part2(droplets):
    it = iter(droplets)
    x,y,z = next(it)
    min_x = max_x = x; min_y = max_y = y; min_z = max_z = z
    for x,y,z in it:
        if x<min_x: min_x=x
        elif x>max_x: max_x=x
        if y<min_y: min_y=y
        elif y>max_y: max_y=y
        if z<min_z: min_z=z
        elif z>max_z: max_z=z
    min_x-=1; min_y-=1; min_z-=1
    max_x+=1; max_y+=1; max_z+=1
    dq = deque(((min_x,min_y,min_z),))
    seen = {(min_x,min_y,min_z)}
    sides = 0
    while dq:
        x,y,z = dq.popleft()
        for dx,dy,dz in NEIGHBORS:
            nx,ny,nz = x+dx,y+dy,z+dz
            if nx<min_x or nx>max_x or ny<min_y or ny>max_y or nz<min_z or nz>max_z:
                continue
            pos = (nx,ny,nz)
            if pos in droplets:
                sides += 1
            elif pos not in seen:
                seen.add(pos)
                dq.append(pos)
    return sides

def main():
    droplets = {tuple(map(int,line.split(','))) for line in open(sys.argv[1]).read().splitlines()}
    print(part1(droplets))
    print(part2(droplets))

if __name__=='__main__':
    main()