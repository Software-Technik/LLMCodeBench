import sys
from collections import deque

def part1(data):
    h = len(data)
    w = len(data[0])

    blizzards = parse_data(data)
    start = (0, 1)
    target = (h - 1, w - 2)

    areas = set((y, x) for y in range(1, h - 1) for x in range(1, w - 1))
    areas.add(start)
    areas.add(target)

    queue = deque()
    queue.append((start, 0))
    seen = set()
    blizzard_cache = {}

    while queue:
        pos, time = queue.popleft()
        if pos == target:
            return time

        if time + 1 not in blizzard_cache:
            new_blizzards = []
            for (y, x), (dy, dx) in blizzards:
                ny = (y + dy - 1) % (h - 2) + 1
                nx = (x + dx - 1) % (w - 2) + 1
                new_blizzards.append(((ny, nx), (dy, dx)))
            blizzards = new_blizzards
            blizzard_cache[time + 1] = {pos for pos, _ in blizzards}
        occupied = blizzard_cache[time + 1]

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
            ny, nx = pos[0] + dy, pos[1] + dx
            if (ny, nx) in areas and (ny, nx) not in occupied:
                state = ((ny, nx), time + 1)
                if state not in seen:
                    seen.add(state)
                    queue.append(state)

def part2(data):
    h = len(data)
    w = len(data[0])

    blizzards = parse_data(data)
    start = (0, 1)
    target = (h - 1, w - 2)

    areas = set((y, x) for y in range(1, h - 1) for x in range(1, w - 1))
    areas.add(start)
    areas.add(target)

    targets = [target, start, target]
    current_target = targets.pop(0)
    total_time = 0

    queue = deque()
    queue.append((start, 0))
    seen = set()
    blizzard_cache = {}

    while queue:
        pos, time = queue.popleft()
        if pos == current_target:
            total_time += time
            if not targets:
                return total_time
            current_target = targets.pop(0)
            queue = deque()
            queue.append((pos, 0))
            seen = set()
            continue

        if time + 1 not in blizzard_cache:
            new_blizzards = []
            for (y, x), (dy, dx) in blizzards:
                ny = (y + dy - 1) % (h - 2) + 1
                nx = (x + dx - 1) % (w - 2) + 1
                new_blizzards.append(((ny, nx), (dy, dx)))
            blizzards = new_blizzards
            blizzard_cache[time + 1] = {pos for pos, _ in blizzards}
        occupied = blizzard_cache[time + 1]

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
            ny, nx = pos[0] + dy, pos[1] + dx
            if (ny, nx) in areas and (ny, nx) not in occupied:
                state = ((ny, nx), time + 1)
                if state not in seen:
                    seen.add(state)
                    queue.append(state)

def parse_data(data):
    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }
    blizzards = [((y, x), directions[c]) for y, line in enumerate(data[1:-1], 1) for x, c in enumerate(line[1:-1], 1) if c in "><^v"]
    return blizzards

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")