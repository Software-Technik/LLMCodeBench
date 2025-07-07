import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

def line_transform(line):
    d = line[0]
    mag = int(line[1:])
    return d, mag

lines = [line_transform(line) for line in lines]

def calculate_distance(lines, part):
    ship = [0, 0]
    waypoint = [10, -1] if part == 2 else None
    facing = 0

    dist = lambda s: abs(s[0]) + abs(s[1])

    for d, mag in lines:
        dx, dy = 0, 0
        if part == 1:
            if d == "N": dy = -mag
            if d == "S": dy = mag
            if d == "W": dx = -mag
            if d == "E": dx = mag
            if d == "L": facing += mag
            if d == "R": facing -= mag
            facing %= 360
            if d == "F":
                if facing == 0: dx = mag
                if facing == 90: dy = -mag
                if facing == 180: dx = -mag
                if facing == 270: dy = mag
            ship[0] += dx
            ship[1] += dy
        else:
            if d == "N": waypoint[1] -= mag
            if d == "S": waypoint[1] += mag
            if d == "W": waypoint[0] -= mag
            if d == "E": waypoint[0] += mag
            if d in "LR":
                if d == "L": mag = 360 - mag
                while mag > 0:
                    waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
                    mag -= 90
            if d == "F":
                difx = waypoint[0] - ship[0]
                dify = waypoint[1] - ship[1]
                dx, dy = mag * difx, mag * dify
                waypoint[0] += dx
                waypoint[1] += dy
                ship[0] += dx
                ship[1] += dy

    return dist(ship)

result1 = calculate_distance(lines, part=1)
result2 = calculate_distance(lines, part=2)

print(result1, result2)