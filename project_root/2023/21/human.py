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
            elif c == ".":
                free.add(pos)
            elif c == "S":
                start = pos
        width = len(line.strip())  # assumes all rows are equal width

    return grid, free, start, width

@profiler
def part1(text):
    grid, _, start, _ = parse(text)
    deltas = [1, -1, -1j, 1j]
    reach = {0: {start}}

    while max(reach.keys()) < 64:
        steps = max(reach.keys())
        reach[steps + 1] = set()
        for pos in reach[steps]:
            for d in deltas:
                if (pos + d) not in grid:
                    reach[steps + 1].add(pos + d)

    return len(reach[64])

@profiler
def part2(text):
    grid, _, start, grid_len = parse(text)
    deltas = [1, -1, -1j, 1j]
    reach = {0: {start}}
    pts = []
    target_time = 26501365

    while len(pts) < 3:
        steps = max(reach.keys())
        if steps - 1 in reach:
            del reach[steps - 1]

        reach[steps + 1] = set()
        for pos in reach[steps]:
            for d in deltas:
                npt = pos + d
                nx = npt.real % grid_len
                ny = npt.imag % grid_len
                if (nx + ny * 1j) not in grid:
                    reach[steps + 1].add(pos + d)

        if (steps - (grid_len // 2) + 1) % grid_len == 0:
            pts.append(len(reach[steps + 1]))

    c = pts[0]
    b = pts[1] - pts[0]
    a = pts[2] - pts[1]
    x = target_time // grid_len
    assert grid_len // 2 == target_time % grid_len
    return c + b * x + (x * (x - 1) // 2) * (a - b)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")