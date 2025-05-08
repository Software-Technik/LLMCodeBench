import sys

def part1( data):
    expand_level = 2
    return calc_length(data, expand_level)

def part2( data):
    expand_level = 1000000

    # for the test case
    if len(data) == 10:
        expand_level = 100

    return calc_length(data, expand_level)

def calc_length( data, expand_level):
    expand_cols = []
    expand_rows = []
    galaxies = []

    for r, line in enumerate(data):
        if "#" in line:
            for c, v in enumerate(line):
                if v == "#":
                    galaxies.append((r, c))
        else:
            expand_rows.append(r)

    for c, col in enumerate(zip(*data)):
        if "#" not in col:
            expand_cols.append(c)

    _sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            y1, x1 = galaxies[i]
            y2, x2 = galaxies[j]

            y1, y2 = sorted([y1, y2])
            x1, x2 = sorted([x1, x2])

            w = x2 - x1
            h = y2 - y1

            cols = sum([1 for c in expand_cols if x1 < c < x2])
            rows = sum([1 for r in expand_rows if y1 < r < y2])

            _sum += w + h + (expand_level - 1) * (cols + rows)

    return _sum


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]
sys.stdout.write(str([part1(data), part2(data)]))