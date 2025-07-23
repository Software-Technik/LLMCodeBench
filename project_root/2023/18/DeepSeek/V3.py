import sys
import re

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

def area(points: list[tuple[int, int]]) -> float:
    n = len(points)
    return abs(sum(points[i][0] * points[(i+1)%n][1] - points[(i+1)%n][0] * points[i][1] for i in range(n))) / 2

def part1(text: str) -> int:
    lines = text.splitlines()
    x, y = 0, 0
    points = [(x, y)]
    steps = 0
    for line in lines:
        direction, n, *_ = line.split()
        n = int(n)
        steps += n
        if direction == UP:
            x -= n
        elif direction == DOWN:
            x += n
        elif direction == RIGHT:
            y += n
        elif direction == LEFT:
            y -= n
        points.append((x, y))
    a = area(points)
    return int(a - steps // 2 + 1 + steps)

def part2(text: str) -> int:
    lines = text.splitlines()
    x, y = 0, 0
    points = [(x, y)]
    steps = 0
    pattern = re.compile(r".+\(#([a-z0-9]+)\)")
    for line in lines:
        hex_color = pattern.match(line).group(1)
        direction = N_TO_DIRECTION[int(hex_color[-1])]
        n = int(hex_color[:-1], 16)
        steps += n
        if direction == UP:
            x -= n
        elif direction == DOWN:
            x += n
        elif direction == RIGHT:
            y += n
        elif direction == LEFT:
            y -= n
        points.append((x, y))
    a = area(points)
    return int(a - steps // 2 + 1 + steps)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")