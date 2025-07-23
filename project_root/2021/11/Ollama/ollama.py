import sys
import numpy as np

def part1(data):
    df = np.array([[int(x) for x in line] for line in data])
    total = 0
    flashed_all = set(tuple(range(10)) for _ in range(10))
    for i in range(100):
        df += 1
        while any(df > 9):
            flashing = np.where(df > 9)
            for y, x in zip(*flashing):
                if (y, x) not in flashed_all:
                    flashed_all.add((y, x))
                    dy, dx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
                    for ddy, ddx in zip(dy, dx):
                        yy, xx = y + ddy, x + ddx
                        if 0 <= yy < 10 and 0 <= xx < 10:
                            df[yy, xx] += 1
        total += len(flashed_all)
        df[df > 9] = 0
        flashed_all.clear()
    return total

def part2(data):
    df = np.array([[int(x) for x in line] for line in data])
    step = 0
    while True:
        df += 1
        while any(df > 9):
            flashing = np.where(df > 9)
            for y, x in zip(*flashing):
                dy, dx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
                for ddy, ddx in zip(dy, dx):
                    yy, xx = y + ddy, x + ddx
                    if 0 <= yy < 10 and 0 <= xx < 10:
                        df[yy, xx] += 1
        step += 1
        if np.all(df == 0):
            return step

data = [line.strip() for line in open(sys.argv[1])]
sys.stdout.write(f"{part1(data)} {part2(data)}")