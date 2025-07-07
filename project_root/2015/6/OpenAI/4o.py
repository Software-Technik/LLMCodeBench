import sys
import re

def process(data, part):
    grid = [0] * 1000 * 1000
    for inst in data:
        op, coord1, coord2 = re.findall(r"(.*)\s(\d+,\d+)\sthrough\s(\d+,\d+)", inst)[0]
        x1, y1 = map(int, coord1.split(","))
        x2, y2 = map(int, coord2.split(","))
        idx = {"turn on": 0, "turn off": 1, "toggle": 2}[op]

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                pos = x * 1000 + y
                if part == 1:
                    grid[pos] = [1, 0, 1 - grid[pos]][idx]
                else:
                    grid[pos] += [1, -1, 2][idx]
                    grid[pos] = max(grid[pos], 0)

    return sum(grid)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{process(data, 1)}\n{process(data, 2)}\n")