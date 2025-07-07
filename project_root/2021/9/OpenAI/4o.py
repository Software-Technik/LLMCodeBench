import sys
import numpy as np

def part1(data):
    df = np.array([list(map(int, line)) for line in data])
    pad = np.pad(df, 1, constant_values=10)
    mask = (
        (df < pad[1:-1, :-2]).astype(int)
        + (df < pad[1:-1, 2:]).astype(int)
        + (df < pad[:-2, 1:-1]).astype(int)
        + (df < pad[2:, 1:-1]).astype(int)
    )
    return (df + 1)[mask == 4].sum()

def label_basin(matrix):
    label_id = 1
    labels = np.zeros_like(matrix)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        stack = [(x, y)]
        size = 0
        while stack:
            x, y = stack.pop()
            if labels[x, y] or matrix[x, y] == 9:
                continue
            labels[x, y] = label_id
            size += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < matrix.shape[0] and 0 <= ny < matrix.shape[1]:
                    stack.append((nx, ny))
        return size
    
    sizes = []
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if matrix[x, y] < 9 and not labels[x, y]:
                sizes.append(dfs(x, y))
                label_id += 1
    return sizes

def part2(data):
    df = np.array([list(map(int, line)) for line in data])
    sizes = label_basin(df)
    return np.prod(sorted(sizes)[-3:])

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")