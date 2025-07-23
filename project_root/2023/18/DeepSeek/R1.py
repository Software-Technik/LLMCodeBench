import sys

UP = "U"
DOWN = "D"
RIGHT = "R"
LEFT = "L"

N_TO_DIRECTION = {
    0: RIGHT,
    1: DOWN,
    2: LEFT,
    3: UP,
}

DIR_ACTIONS = {
    UP: lambda x, y, n: (x - n, y),
    DOWN: lambda x, y, n: (x + n, y),
    RIGHT: lambda x, y, n: (x, y + n),
    LEFT: lambda x, y, n: (x, y - n),
}

def area(points: list[tuple[int, int]]) -> float:
    n = len(points)
    s = 0
    for i in range(n):
        x0, y0 = points[i]
        x1, y1 = points[(i+1) % n]
        s += x0 * y1 - x1 * y0
    return abs(s) / 2

def part1(text: str) -> int:
    lines = text.splitlines()
    intersections = []
    current = (0, 0)
    steps = 0
    for line in lines:
        parts = line.split()
        direction = parts[0]
        n_val = int(parts[1])
        steps += n_val
        intersections.append(current)
        current = DIR_ACTIONS[direction](*current, n_val)
    interior_points = area(intersections) - steps / 2 + 1
    return int(interior_points + steps)

def part2(text: str) -> int:
    lines = text.splitlines()
    intersections = []
    current = (0, 0)
    steps = 0
    for line in lines:
        hex_str = line.split()[-1][2:8]
        n_val = int(hex_str[:5], 16)
        direction_digit = int(hex_str[5])
        direction = N_TO_DIRECTION[direction_digit]
        steps += n_val
        intersections.append(current)
        current = DIR_ACTIONS[direction](*current, n_val)
    interior_points = area(intersections) - steps / 2 + 1
    return int(interior_points + steps)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")