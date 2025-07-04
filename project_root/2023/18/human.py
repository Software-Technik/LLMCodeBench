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
    """
    Get the area of a polygon using the shoelace formula.

    See https://en.wikipedia.org/wiki/Shoelace_formula.
    """
    overlaped_points = zip(points, points[1:] + [points[0]])
    return abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in overlaped_points)) / 2


def part1(text: str) -> int:
    lines = text.splitlines()
    intersections: list[tuple[int, int]] = [(0, 0)]

    steps = 0
    for line in lines:
        direction, n, *_ = line.split()
        n = int(n)
        point = intersections[-1]
        steps += n
        if direction == UP:
            intersections.append((point[0] - n, point[1]))
        elif direction == DOWN:
            intersections.append((point[0] + n, point[1]))
        elif direction == RIGHT:
            intersections.append((point[0], point[1] + n))
        elif direction == LEFT:
            intersections.append((point[0], point[1] - n))

    intersections.pop(-1)
    # Use Pick's theorem to calculate inner points of the polygon,
    # and add the number of steps to get the total number of points.
    # See https://en.wikipedia.org/wiki/Pick's_theorem.
    interior_points = area(intersections) - steps / 2 + 1
    return int(interior_points + steps)

def part2(text: str) -> int:
    lines = text.splitlines()
    intersections: list[tuple[int, int]] = [(0, 0)]

    pattern = re.compile(r".+\(#([a-z0-9]+)\)")
    steps = 0
    for line in lines:
        point = intersections[-1]
        hex_color = pattern.match(line).group(1)
        direction = N_TO_DIRECTION[int(hex_color[-1])]
        n = int(hex_color[:-1], 16)
        steps += n
        if direction == UP:
            intersections.append((point[0] - n, point[1]))
        elif direction == DOWN:
            intersections.append((point[0] + n, point[1]))
        elif direction == RIGHT:
            intersections.append((point[0], point[1] + n))
        elif direction == LEFT:
            intersections.append((point[0], point[1] - n))

    intersections.pop(-1)
    # Use Pick's theorem to calculate inner points of the polygon,
    # and add the number of steps to get the total number of points.
    # See https://en.wikipedia.org/wiki/Pick's_theorem.
    interior_points = area(intersections) - steps / 2 + 1
    return int(interior_points + steps)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")