import sys
import numpy as np

def part1(data):
    size = 0
    coords = []
    for line in data:
        parts = line.split(' -> ')
        x1, y1 = map(int, parts[0].split(','))
        x2, y2 = map(int, parts[1].split(','))
        coords.append((x1, y1, x2, y2))
        size = max(size, x1, y1, x2, y2)
    size += 1
    diagram = np.zeros((size, size), dtype=np.uint16)

    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            diagram[y1:y2+1, x1] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            diagram[y1, x1:x2+1] += 1

    return np.sum(diagram > 1)

def part2(data):
    size = 0
    coords = []
    for line in data:
        parts = line.split(' -> ')
        x1, y1 = map(int, parts[0].split(','))
        x2, y2 = map(int, parts[1].split(','))
        coords.append((x1, y1, x2, y2))
        size = max(size, x1, y1, x2, y2)
    size += 1
    diagram = np.zeros((size, size), dtype=np.uint16)

    for x1, y1, x2, y2 in coords:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            diagram[y1:y2+1, x1] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            diagram[y1, x1:x2+1] += 1
        else:
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            x, y = x1, y1
            while x != x2 + dx and y != y2 + dy:
                diagram[y, x] += 1
                x += dx
                y += dy

    return np.sum(diagram > 1)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")