import sys

def part1(data):
    wire1 = set()
    x, y = 0, 0
    for move in data[0].split(','):
        d = move[0]
        n = int(move[1:])
        dx, dy = 0, 0
        if d == 'U': dy = -1
        elif d == 'R': dx = 1
        elif d == 'D': dy = 1
        elif d == 'L': dx = -1
        for _ in range(n):
            x += dx
            y += dy
            wire1.add((x, y))
    
    x, y = 0, 0
    min_dist = float('inf')
    for move in data[1].split(','):
        d = move[0]
        n = int(move[1:])
        dx, dy = 0, 0
        if d == 'U': dy = -1
        elif d == 'R': dx = 1
        elif d == 'D': dy = 1
        elif d == 'L': dx = -1
        for _ in range(n):
            x += dx
            y += dy
            if (x, y) in wire1:
                dist = abs(x) + abs(y)
                if dist < min_dist:
                    min_dist = dist
    return min_dist

def part2(data):
    wire1 = {}
    x, y = 0, 0
    steps = 0
    for move in data[0].split(','):
        d = move[0]
        n = int(move[1:])
        dx, dy = 0, 0
        if d == 'U': dy = -1
        elif d == 'R': dx = 1
        elif d == 'D': dy = 1
        elif d == 'L': dx = -1
        for _ in range(n):
            steps += 1
            x += dx
            y += dy
            if (x, y) not in wire1:
                wire1[(x, y)] = steps
    
    x, y = 0, 0
    steps2 = 0
    min_steps = float('inf')
    for move in data[1].split(','):
        d = move[0]
        n = int(move[1:])
        dx, dy = 0, 0
        if d == 'U': dy = -1
        elif d == 'R': dx = 1
        elif d == 'D': dy = 1
        elif d == 'L': dx = -1
        for _ in range(n):
            steps2 += 1
            x += dx
            y += dy
            if (x, y) in wire1:
                total_steps = steps2 + wire1[(x, y)]
                if total_steps < min_steps:
                    min_steps = total_steps
    return min_steps

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")