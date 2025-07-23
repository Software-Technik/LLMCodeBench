import sys
import re

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

target_line = data[0]
match = re.match(r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", target_line)
if not match:
    raise ValueError("Invalid input format")

x1, x2, y1, y2 = map(int, match.groups())

best_y = 0
count = 0
for init_vx in range(1, x2 + 1):
    total_x = init_vx * (init_vx + 1) // 2
    if total_x < x1:
        continue
    for init_vy in range(y1, -y1):
        vx, vy = init_vx, init_vy
        x, y = 0, 0
        max_y = y1
        hit = False
        while x <= x2 and y >= y1:
            if y > max_y:
                max_y = y
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                if max_y > best_y:
                    best_y = max_y
                hit = True
                break
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if vx == 0 and x < x1:
                break

sys.stdout.write(f"{best_y} {count}")