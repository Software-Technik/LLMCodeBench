import sys

def lineToTupleSet1(line):
    points = set()
    x = y = 0
    for instruction in line.split(","):
        direction = instruction[0]
        length = int(instruction[1:])
        dx = dy = 0
        if direction == 'U':
            dy = -1
        elif direction == 'R':
            dx = 1
        elif direction == 'D':
            dy = 1
        elif direction == 'L':
            dx = -1
        for _ in range(length):
            x += dx
            y += dy
            points.add((x, y))
    return points

def distance(p, origin=(0, 0)):
    return abs(p[0] - origin[0]) + abs(p[1] - origin[1])

def part1(data):
    points1 = lineToTupleSet1(data[0])
    points2 = lineToTupleSet1(data[1])
    crossings = points1 & points2
    return min(map(distance, crossings)) if crossings else 0

def lineToTupleSet2(line):
    points = {}
    cost = x = y = 0
    for instruction in line.split(","):
        direction = instruction[0]
        length = int(instruction[1:])
        dx = dy = 0
        if direction == 'U':
            dy = -1
        elif direction == 'R':
            dx = 1
        elif direction == 'D':
            dy = 1
        elif direction == 'L':
            dx = -1
        for _ in range(length):
            cost += 1
            x += dx
            y += dy
            if (x, y) not in points:
                points[(x, y)] = cost
    return points

def part2(data):
    points1 = lineToTupleSet2(data[0])
    points2 = lineToTupleSet2(data[1])
    crossings = points1.keys() & points2.keys()
    return min(points1[p] + points2[p] for p in crossings) if crossings else 0

with open(sys.argv[1]) as f:
    data = f.read().splitlines()
print(f"{part1(data)} {part2(data)}")