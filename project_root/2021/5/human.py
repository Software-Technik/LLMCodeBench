import sys
import numpy as np

def part1(data):
    data = [x.replace(' -> ', ',').split(',') for x in data]
    data = [list(map(int, x)) for x in data]

    size = max(max(x) for x in data) + 1
    diagram = np.zeros((size, size), dtype=int)

    for x1, y1, x2, y2 in data:
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            diagram[y1: y2+1, x1: x2+1] += 1

    return np.sum(diagram > 1)  # 6283

def part2(data):
    data = [x.replace(' -> ', ',').split(',') for x in data]
    data = [list(map(int, x)) for x in data]

    size = max(max(x) for x in data) + 1
    diagram = np.zeros((size, size), dtype=int)

    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
            diagram[y1: y2+1, x1: x2+1] += 1
        else:
            x = range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)
            y = range(y1, y2+1) if y1 <= y2 else range(y1, y2-1, -1)
            for i, j in zip(x, y):
                diagram[j, i] += 1

    return np.sum(diagram > 1)  # 18864

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")