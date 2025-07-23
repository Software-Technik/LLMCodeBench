import sys
from time import perf_counter

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        return ret
    return wrapper_method

def parse(text):
    grid = set()
    free = set()
    start = None
    width = 0

    for y, line in enumerate(text.strip().splitlines()):
        for x, c in enumerate(line.strip()):
            pos = x + y * 1j
            if c == "#":
                grid.add(pos)
            elif c == "." or c == "S":
                free.add(pos)
                if c == "S":
                    start = pos
        width = len(line.strip())

    return grid, free, start, width

@profiler
def part1(text):
    grid, free, start, _ = parse(text)
    deltas = [1, -1, -1j, 1j]
    current = {start}
    
    for _ in range(64):
        next_pos = set()
        for pos in current:
            for d in deltas:
                new_pos = pos + d
                if new_pos in free:
                    next_pos.add(new_pos)
        current = next_pos
    
    return len(current)

@profiler
def part2(text):
    grid, free, start, grid_len = parse(text)
    deltas = [1, -1, -1j, 1j]
    current = {start}
    pts = []
    target_time = 26501365

    for steps in range(1, 3 * grid_len + 1):
        next_pos = set()
        for pos in current:
            for d in deltas:
                new_pos = pos + d
                mod_pos = (new_pos.real % grid_len) + (new_pos.imag % grid_len) * 1j
                if mod_pos in free:
                    next_pos.add(new_pos)
        current = next_pos
        if (steps - (grid_len // 2)) % grid_len == 0:
            pts.append(len(current))
            if len(pts) == 3:
                break

    c = pts[0]
    b = pts[1] - pts[0]
    a = pts[2] - pts[1]
    x = target_time // grid_len
    return c + b * x + (x * (x - 1) // 2) * (a - b)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")