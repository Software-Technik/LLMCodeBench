import sys

def lineToTupleSet(line):
    points = [(0, 0)]
    x, y = 0, 0
    costs = {(x, y): 0}
    cost = 0
    for instruction in line.split(","):
        direction, length = instruction[0], int(instruction[1:])
        dx, dy = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}[direction]
        while length > 0:
            cost += 1
            x += dx
            y += dy
            points.append((x, y))
            if (x, y) not in costs:
                costs[(x, y)] = cost
            length -= 1
    return set(points), costs

def distance(p1, p2=(0, 0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1(data):
    points1, _ = lineToTupleSet(data[0])
    points2, _ = lineToTupleSet(data[1])
    crossings = points1 & points2
    return min(map(distance, crossings))

def part2(data):
    _, costs1 = lineToTupleSet(data[0])
    _, costs2 = lineToTupleSet(data[1])
    crossings = set(costs1.keys()) & set(costs2.keys())
    return min(costs1[p] + costs2[p] for p in crossings)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")