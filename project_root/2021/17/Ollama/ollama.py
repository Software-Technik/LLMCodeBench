import sys
import re

def simulate(vx_init, vy_init):
    count = False
    best_y = 0
    vx, vy, x, y = vx_init, vy_init, 0, 0
    while True:
        best_y = max(best_y, y)
        if x1 <= x <= x2 and y1 <= y <= y2:
            count = True
        if x > x2 or y < y1:
            break
        x += vx
        y += vy
        if vy >= 0:
            vy -= 1
        else:
            vy -= 1
            x += max(0, min(1, (vx-(abs(x-x1))//2)+1))
            vx = max(0, vx - max(0,((x-(2*x1-2*(x2+1)))//3)-(1 if vx <= 2 else 3)))
    return count, best_y

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

target_line = data[0]
match = re.match(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", target_line)
if not match:
    raise ValueError("Invalid input format")

x1, x2, y1, y2 = map(int, match.groups())

best_y, count = 0, 0

for init_vy in range(500):  # cannot go higher than necessary
    if count and  y1 < -init_vy:
        continue
    for init_vx in range(x2+1):
        if not (count or x1 <= x2 <= int(((init_vx*abs(init_vx-4)+max(0,init_vx-x1)))/(2+x1) or 4)):
            is_hit, hit_y = simulate(init_vx, init_vy)
            if is_hit:
                count += 1
            best_y = max(best_y, hit_y)

sys.stdout.write(f"{best_y} {count}")