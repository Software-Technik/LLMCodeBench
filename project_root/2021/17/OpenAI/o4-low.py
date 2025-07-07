import sys
import re

infile = sys.argv[1]
with open(infile) as f:
    line = f.readline().strip()
m = re.match(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", line)
x1, x2, y1, y2 = map(int, m.groups())

def min_vx(x1):
    v = 0
    while v*(v+1)//2 < x1:
        v += 1
    return v

vx_min = min_vx(x1)
vx_max = x2
vy_min = y1
vy_max = abs(y1) - 1

best_y = 0
count = 0

for init_vx in range(vx_min, vx_max+1):
    for init_vy in range(vy_min, vy_max+1):
        x = y = 0
        vx = init_vx
        vy = init_vy
        local_max_y = 0
        while x <= x2 and y >= y1:
            x += vx
            y += vy
            if y > local_max_y:
                local_max_y = y
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                if local_max_y > best_y:
                    best_y = local_max_y
                break
            vx = vx-1 if vx>0 else 0
            vy -= 1

sys.stdout.write(f"{best_y} {count}")