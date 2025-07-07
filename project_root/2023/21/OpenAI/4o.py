import sys

def parse(text):
    grid = set()
    start = None
    width = 0

    for y, line in enumerate(text.strip().splitlines()):
        for x, c in enumerate(line.strip()):
            pos = x + y * 1j
            if c == "#":
                grid.add(pos)
            elif c == "S":
                start = pos
        width = len(line.strip())

    return grid, start, width

def part1(text):
    grid, start, _ = parse(text)
    deltas = [1, -1, -1j, 1j]
    reach = {0: {start}}

    for _ in range(64):
        current_reach = reach[max(reach)]
        new_reach = {p + d for p in current_reach for d in deltas if (p + d) not in grid}
        reach[max(reach) + 1] = new_reach

    return len(reach[64])

def part2(text):
    grid, start, grid_len = parse(text)
    deltas = [1, -1, -1j, 1j]
    reach = {0: {start}}
    pts = []
    target_time = 26501365

    while len(pts) < 3:
        current_reach = reach[max(reach)]
        new_reach = set()
        for pos in current_reach:
            for d in deltas:
                npt = pos + d
                if ((npt.real % grid_len) + (npt.imag % grid_len) * 1j) not in grid:
                    new_reach.add(npt)
        reach[max(reach) + 1] = new_reach

        if (max(reach) - (grid_len // 2) + 1) % grid_len == 0:
            pts.append(len(new_reach))

    c, b, a = pts
    x = target_time // grid_len
    return c + b * x + (x * (x - 1) // 2) * (a - b)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    print(f"{part1(text)} {part2(text)}")