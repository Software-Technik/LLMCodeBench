import sys

def lineToTupleSet1(line):
    points = set()
    x = 0
    y = 0
    for instruction in line.split(","):
        direction = instruction[0]
        length = int(instruction[1:])
        for _ in range(0, length):
            if direction == "U": y -= 1
            if direction == "R": x += 1
            if direction == "D": y += 1
            if direction == "L": x -= 1
            points.add((x, y))
    return points

def distance(p1, p2 = (0, 0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1(data):
    points1 = lineToTupleSet1(data[0])
    points2 = lineToTupleSet1(data[1])
    crossings = points1 & points2
    return min(map(distance, crossings))

def lineToTupleSet2(line):
    points = {}
    cost = 0
    x = 0
    y = 0
    for instruction in line.split(","):
        direction = instruction[0]
        length = int(instruction[1:])
        for _ in range(0, length):
            cost += 1
            if direction == "U": y -= 1
            if direction == "R": x += 1
            if direction == "D": y += 1
            if direction == "L": x -= 1
            if (x, y) not in points:
                points[(x, y)] = cost
    return points

def part2(data):
    points1 = lineToTupleSet2(data[0])
    points2 = lineToTupleSet2(data[1])
    crossings = set(points1.keys()) & set(points2.keys())
    return min(map(lambda p: points1[p] + points2[p], crossings))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")