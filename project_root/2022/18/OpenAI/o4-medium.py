import sys
from collections import deque

def main():
    path = sys.argv[1]
    droplets = set()
    xs = []
    ys = []
    zs = []
    for line in open(path):
        x, y, z = map(int, line.split(','))
        droplets.add((x, y, z))
        xs.append(x)
        ys.append(y)
        zs.append(z)
    shifts = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
    part1 = sum(1 for x, y, z in droplets for dx, dy, dz in shifts if (x+dx, y+dy, z+dz) not in droplets)
    min_x, max_x = min(xs) - 1, max(xs) + 1
    min_y, max_y = min(ys) - 1, max(ys) + 1
    min_z, max_z = min(zs) - 1, max(zs) + 1
    q = deque([(min_x, min_y, min_z)])
    seen = set(droplets)
    part2 = 0
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        for dx, dy, dz in shifts:
            nx, ny, nz = x+dx, y+dy, z+dz
            if (nx, ny, nz) in droplets:
                part2 += 1
            elif (nx, ny, nz) not in seen and min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z:
                q.append((nx, ny, nz))
    sys.stdout.write(f"{part1}\n{part2}\n")

if __name__ == "__main__":
    main()