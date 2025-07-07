import sys
import re

N_TO_DIRECTION = {
    '0': (0, 1),   # RIGHT
    '1': (1, 0),   # DOWN
    '2': (0, -1),  # LEFT
    '3': (-1, 0),  # UP
}

def area(points):
    return abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(points, points[1:] + [points[0]]))) / 2

def compute_intersections(lines, conversion_func):
    intersections = [(0, 0)]
    steps = 0
    for line in lines:
        steps += conversion_func(intersections, line)
    intersections.pop(-1)
    return intersections, steps

def conversion_part1(intersections, line):
    direction, n = line.split()[:2]
    n = int(n)
    dx, dy = {'U': (-n, 0), 'D': (n, 0), 'R': (0, n), 'L': (0, -n)}[direction]
    intersections.append((intersections[-1][0] + dx, intersections[-1][1] + dy))
    return n

def conversion_part2(intersections, line):
    hex_color = re.match(r".+\(#([a-z0-9]+)\)", line).group(1)
    direction = hex_color[-1]
    n = int(hex_color[:-1], 16)
    dx, dy = N_TO_DIRECTION[direction]
    intersections.append((intersections[-1][0] + dx * n, intersections[-1][1] + dy * n))
    return n

def solve_part(intersections, steps):
    return int(area(intersections) - steps / 2 + 1 + steps)

def main():
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read().strip()

    lines = text.splitlines()
    part1_intersections, part1_steps = compute_intersections(lines, conversion_part1)
    part2_intersections, part2_steps = compute_intersections(lines, conversion_part2)

    sys.stdout.write(f"{solve_part(part1_intersections, part1_steps)} {solve_part(part2_intersections, part2_steps)}")
    
if __name__ == "__main__":
    main()