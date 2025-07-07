import sys

def to_bool_row(s):
    return [c == '#' for c in s]

def parse_input(lines):
    rules = {}
    for line in lines:
        if "=>" not in line:
            continue
        source, dest = line.strip().split(' => ')
        src_grid = tuple(tuple(to_bool_row(row)) for row in source.split('/'))
        dest_grid = tuple(tuple(to_bool_row(row)) for row in dest.split('/'))
        for variant in generate_transformations(src_grid):
            rules[variant] = dest_grid
    return rules

def rotate(grid):
    return tuple(zip(*grid[::-1]))

def flip(grid):
    return grid[::-1]

def generate_transformations(grid):
    grids = set()
    g = grid
    for _ in range(4):
        grids.add(g)
        grids.add(flip(g))
        g = rotate(g)
    return grids

def get_square(grid, i, j, size):
    return tuple(tuple(grid[i + x][j + y] for y in range(size)) for x in range(size))

def insert_square(grid, square, i, j):
    size = len(square)
    for x in range(size):
        for y in range(size):
            grid[i + x][j + y] = square[x][y]

def find_next(grid, rules):
    size = len(grid)
    step = 2 if size % 2 == 0 else 3
    new_size = size * (step + 1) // step
    new_grid = [[False] * new_size for _ in range(new_size)]
    for i in range(0, size, step):
        for j in range(0, size, step):
            square = get_square(grid, i, j, step)
            enhanced = rules[square]
            insert_square(new_grid, enhanced, (i // step) * (step + 1), (j // step) * (step + 1))
    return new_grid

def pixels_on(grid):
    return sum(sum(row) for row in grid)

def part1(data):
    rules = parse_input(data)
    grid = [to_bool_row(row) for row in ".#./..#/###".split("/")]
    for _ in range(5):
        grid = find_next(grid, rules)
    return pixels_on(grid)

def part2(data):
    rules = parse_input(data)
    return fast_count(tuple(tuple(to_bool_row(row)) for row in ".#./..#/###".split("/")), rules, 18)

def fast_count(grid, rules, steps):
    from collections import Counter

    def forward3steps(pattern):
        g = pattern
        for _ in range(3):
            g = tuple(tuple(row) for row in find_next([list(row) for row in g], rules))
        count = Counter()
        for i in range(0, len(g), 3):
            for j in range(0, len(g), 3):
                sq = tuple(tuple(g[i + x][j + y] for y in range(3)) for x in range(3))
                count[sq] += 1
        return count

    pattern = grid
    counts = Counter({pattern: 1})
    mapping_counts = {}

    for _ in range(steps // 3):
        next_counts = Counter()
        for pat, n in counts.items():
            if pat not in mapping_counts:
                mapping_counts[pat] = forward3steps(pat)
            for sub_pat, sub_n in mapping_counts[pat].items():
                next_counts[sub_pat] += n * sub_n
        counts = next_counts

    return sum(pixels_on(sub_pat) * n for sub_pat, n in counts.items())

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f if line.strip()]

print(part1(data))
print(part2(data))