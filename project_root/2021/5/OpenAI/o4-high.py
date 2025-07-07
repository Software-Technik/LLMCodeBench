import sys
from collections import Counter

def read_data(path):
    segments = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.replace(' -> ', ',').split(',')
            segments.append(tuple(map(int, parts)))
    return segments

def part1(segments):
    cnt = Counter()
    for x1, y1, x2, y2 in segments:
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                cnt[(x1, y)] += 1
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                cnt[(x, y1)] += 1
    return sum(v > 1 for v in cnt.values())

def part2(segments):
    cnt = Counter()
    for x1, y1, x2, y2 in segments:
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                cnt[(x1, y)] += 1
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                cnt[(x, y1)] += 1
        else:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            x, y = x1, y1
            while True:
                cnt[(x, y)] += 1
                if x == x2 and y == y2: break
                x += dx; y += dy
    return sum(v > 1 for v in cnt.values())

if __name__ == '__main__':
    segments = read_data(sys.argv[1])
    a = part1(segments)
    b = part2(segments)
    sys.stdout.write(f"{a} {b}")