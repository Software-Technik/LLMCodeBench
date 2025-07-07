import sys

def enhance(times, data):
    algo = [1 if c == '#' else 0 for c in data[0]]
    lit = {(x, y) for y, line in enumerate(data[2:]) for x, c in enumerate(line) if c == '#'}
    fill = 0
    for _ in range(times):
        new_lit = set()
        if lit:
            xs = [x for x, _ in lit]; ys = [y for _, y in lit]
            minx, maxx = min(xs), max(xs); miny, maxy = min(ys), max(ys)
        else:
            minx = miny = maxx = maxy = 0
        for y in range(miny - 1, maxy + 2):
            for x in range(minx - 1, maxx + 2):
                idx = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        idx = (idx << 1) | ((x + dx, y + dy) in lit and 1 or fill)
                if algo[idx]:
                    new_lit.add((x, y))
        lit = new_lit
        fill = algo[0] if fill == 0 else algo[511]
    return len(lit)

def part1(data):
    return enhance(2, data)

def part2(data):
    return enhance(50, data)

data = open(sys.argv[1]).read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")