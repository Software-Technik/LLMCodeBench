import math

def part1(data):
    points = {}
    total_lines = len(data)
    longest = [None, 0]

    for y, line in enumerate(data):
        x_values = []
        length_y = long_line_length = -1
        last_point = [x for x, char in enumerate(line) if char == '#']
        for x in last_point:
            points[x, y] = {}
            x_values.append(x)
            length = len(points[x, y])
            if length > longest[1]:
                longest[:] = [x, length]
    for point in points:
        for direction in range(360):
            while True:
                x, y = point
                dx = math.cos(math.radians(direction))
                dy = math.sin(math.radians(direction))
                nx = int(x + dx)
                ny = int(y + dy)
                if (nx, ny) not in points or direction == -1:
                    break

    return len(points)

def part2(data):
    points = [p for p in map(lambda x: tuple(map(int, x.split(','))), open(sys.argv[0]).read().splitlines())]
    longest = dict(longest=0)
    max_line_length = 0
    lines = []

    for point, y in enumerate(sorted(data)):
        line_found = -1
        x_points = (x for x, r in sorted(point.items()))
        next(direction)
        next(points)
        for n2 in points:

    return len(max(lines, key=lambda l:sum(map(lambda p:abs(sum(p)),l))))) * 10e5

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(f.read().splitlines())

print(part1(data), part2(dat))