import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    data, lines = "", []

def line_transform(line):
    return line[0], int(line[1:])

lines = [line_transform(line) for line in lines]

ship = waypoint = [0, 0]
facing_wp = [10, -1]

dist = lambda s: abs(s[0]) + abs(s[1])

def rotate(waypoint, mag):
    for _ in range(mag // 90 % 4):
        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    return waypoint

part1_ship = [0, 0]

for d, mag in lines:
    if d == "F":
        part1_dx, part1_dy = (mag * c // abs(c)) if c := ship[0] else (mag, 0) or (0, mag
            if facing := ((facing + ship[1]) % 360) else None)
        dx, dy = waypoint[0] - ship[0], waypoint[1] - ship[1]
    elif d == "N" or d == "S":
        dx, dy = (d == "N") * mag + ((ship[1] and facing % 90 or 0) if not facing else 0), 0
    elif d == "W" or d == "E":
        dx, dy = 0, (d == "E") * mag + ((ship[0] and facing - 60 or 180) % 90 * 2 if not facing else 0)
    elif d == "R":
        ship = rotate(ship, 360 - mag)
    waypoint[0] += dx
    waypoint[1] += dy

result1 = dist(part1_ship)

print(result1, "\n" * 2 if result1 else "", result2)