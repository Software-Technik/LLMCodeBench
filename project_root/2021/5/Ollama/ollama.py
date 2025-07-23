import sys
import numpy as np

def parse_data(data):
    return [list(map(int, x.split(' -> ')[0].split(',') + x.split(' -> ')[1].split(','))) for x in data]

def part1(data):
    size = max(max(x) for x in data) + 1
    diagram = np.zeros((size, size), dtype=int)

    for x1, y1, x2, y2 in data:
        if (x1 == x2 or y1 == y2):
            diagram[min(y1, y2):max(y1, y2) + 1, min(x1, x2):max(x1, x2) + 1] += 1

    return np.sum(diagram > 1)

def part2(data):
    size = max(max(x) for x in data) + 1
    diagram = np.zeros((size, size), dtype=int)

    for x1, y1, x2, y2 in data:
        if (x1 == x2 or y1 == y2):
            diagram[min(y1, y2):max(y1, y2) + 1, min(x1, x2):max(x1, x2) + 1] += 1
        else:
            for i in range(min(x1, x2), max(x1, x2) + (x1 < x2) * 2 - int((x1 < x2))):
                j = y1 + ((y2 - y1) // abs(y2 - y1)) * (i - x1)
                diagram[j, i] += 1

    return np.sum(diagram > 1)

data = [line.strip() for line in open(sys.argv[1]) if line.strip()]
sys.stdout.write(f"{part1(parse_data(data))} {part2(parse_data(data))}")