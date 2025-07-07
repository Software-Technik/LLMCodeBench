import sys

def trace_wire(line, record_steps=False):
    points = {} if record_steps else set()
    x = y = cost = 0
    for instruction in line.split(","):
        direction = instruction[0]
        length = int(instruction[1:])
        dx, dy = 0, 0
        if direction == "U": dy = -1
        elif direction == "R": dx = 1
        elif direction == "D": dy = 1
        elif direction == "L": dx = -1
        for _ in range(length):
            x, y = x + dx, y + dy
            cost += 1
            if record_steps:
                if (x, y) not in points:
                    points[(x, y)] = cost
            else:
                points.add((x, y))
    return points

def distance(p1, p2=(0, 0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1(data):
    points1 = trace_wire(data[0])
    points2 = trace_wire(data[1])
    crossings = points1 & points2
    return min(map(distance, crossings))

def part2(data):
    points1 = trace_wire(data[0], record_steps=True)
    points2 = trace_wire(data[1], record_steps=True)
    crossings = set(points1.keys()) & set(points2.keys())
    return min(points1[p] + points2[p] for p in crossings)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")