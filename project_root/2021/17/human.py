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

best_y, count = 0, 0
for init_vx in range(1, x2 + 1):  # cannot go higher than x2, or it will go throught the target area
    for init_vy in range(y1, 500):
        vx, vy = init_vx, init_vy
        x, y, max_y = 0, 0, y1
        while x <= x2 and y >= y1:
            max_y = max(max_y, y)
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                best_y = max(best_y, max_y)
                break
            x += vx
            y += vy
            vx = max(0, vx - 1)
            vy -= 1

sys.stdout.write(f"{best_y} {count}")