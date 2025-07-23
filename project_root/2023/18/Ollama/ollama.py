import re

UP, DOWN, RIGHT, LEFT = range(4)
N_TO_DIRECTION = {0: RIGHT, 1: DOWN, 2: LEFT, 3: UP}

def area(points):
    return abs(sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(points, points[1:] + [points[0]]))) / 2

def process_line(point, direction, n):
    if direction == UP:
        point = (point[0] - n, point[1])
    elif direction == DOWN:
        point = (point[0] + n, point[1])
    elif direction == RIGHT:
        point = (point[0], point[1] + n)
    elif direction == LEFT:
        point = (point[0], point[1] - n)
    return point

def part1(text):
    lines, intersections, steps = text.splitlines(), [(0, 0)], 0
    for line in lines:
        _, n, _ = re.match(r".+\(#([a-z0-9]+)\)", line).group(1), line.split()[1], None
        n = int(n)
        point = intersections[-1]
        direction = N_TO_DIRECTION[int(line.split()[-2][-1])]
        steps += n
        intersections.append(process_line(point, direction, n))
    return int(area(intersections) - steps / 2 + 1 + steps)

def part2(text):
    lines, intersections, steps = text.splitlines(), [(0, 0)], 0
    for line in lines:
        _, n, _ = re.match(r".+\(#([a-z0-9]+)\)", line).group(1), int(n, 16), None
        n = int(n)
        point = intersections[-1]
        direction = N_TO_DIRECTION[int(line.split()[-2][-1])]
        steps += n
        intersections.append(process_line(point, direction, n))
    return int(area(intersections) - steps / 2 + 1 + steps)

if __name__ == '':
    with open(sys.argv[1]) as f:
        text = f.read()
    print(part1(text), part2(text))