import sys

def enhance(times, data):
    algo = [1 if c == "#" else 0 for c in data[0]]
    lit = {(x, y) for y, row in enumerate(data[2:]) for x, c in enumerate(row) if c == "#"}
    minx = min(x for x, y in lit)
    maxx = max(x for x, y in lit)
    miny = min(y for x, y in lit)
    maxy = max(y for x, y in lit)
    background = 0
    for _ in range(times):
        new_lit = set()
        for y in range(miny - 1, maxy + 2):
            for x in range(minx - 1, maxx + 2):
                idx = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        nx, ny = x + dx, y + dy
                        bit = background if nx < minx or nx > maxx or ny < miny or ny > maxy else (1 if (nx, ny) in lit else 0)
                        idx = (idx << 1) | bit
                if algo[idx]:
                    new_lit.add((x, y))
        lit = new_lit
        minx -= 1; maxx += 1; miny -= 1; maxy += 1
        background = algo[0] if background == 0 else algo[511]
    return len(lit)

def part1(data):
    return enhance(2, data)

def part2(data):
    return enhance(50, data)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = [line.rstrip("\n") for line in f]
    print(part1(data), part2(data))