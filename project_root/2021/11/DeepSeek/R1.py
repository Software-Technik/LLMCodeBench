import sys
import numpy as np
from collections import deque

def part1(data):
    df = np.array([[int(x) for x in line] for line in data])
    rows, cols = df.shape
    total = 0
    for _ in range(100):
        flashed = np.zeros_like(df, dtype=bool)
        q = deque()
        df += 1
        for i in range(rows):
            for j in range(cols):
                if df[i, j] > 9:
                    flashed[i, j] = True
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        df[nx, ny] += 1
                        if df[nx, ny] > 9 and not flashed[nx, ny]:
                            flashed[nx, ny] = True
                            q.append((nx, ny))
        df[flashed] = 0
        total += np.sum(flashed)
    return total

def part2(data):
    df = np.array([[int(x) for x in line] for line in data])
    rows, cols = df.shape
    step = 0
    while True:
        step += 1
        flashed = np.zeros_like(df, dtype=bool)
        q = deque()
        df += 1
        for i in range(rows):
            for j in range(cols):
                if df[i, j] > 9:
                    flashed[i, j] = True
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        df[nx, ny] += 1
                        if df[nx, ny] > 9 and not flashed[nx, ny]:
                            flashed[nx, ny] = True
                            q.append((nx, ny))
        df[flashed] = 0
        if np.all(flashed):
            return step

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")