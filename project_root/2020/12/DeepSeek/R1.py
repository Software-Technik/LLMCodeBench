import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

def ans(answer):
    pass

def line_transform(line):
    d = line[0]
    mag = int(line[1:])
    return d, mag

lines = [line_transform(line) for line in lines]

ship = [0, 0]
facing = 0

dist = lambda s: abs(s[0]) + abs(s[1])

for d, mag in lines:
    dx, dy = 0, 0
    if d == "N":
        dy = -mag
    elif d == "S":
        dy = mag
    elif d == "W":
        dx = -mag
    elif d == "E":
        dx = mag
    elif d == "L":
        facing = (facing + mag) % 360
    elif d == "R":
        facing = (facing - mag) % 360
    elif d == "F":
        if facing == 0:
            dx = mag
        elif facing == 90:
            dy = -mag
        elif facing == 180:
            dx = -mag
        elif facing == 270:
            dy = mag
    ship[0] += dx
    ship[1] += dy

result1 = dist(ship)

ship = [0, 0]
wx, wy = 10, -1

for d, mag in lines:
    if d == 'N':
        wy -= mag
    elif d == 'S':
        wy += mag
    elif d == 'E':
        wx += mag
    elif d == 'W':
        wx -= mag
    elif d == 'R':
        mag %= 360
        if mag == 90:
            wx, wy = -wy, wx
        elif mag == 180:
            wx, wy = -wx, -wy
        elif mag == 270:
            wx, wy = wy, -wx
    elif d == 'L':
        mag %= 360
        if mag == 90:
            wx, wy = wy, -wx
        elif mag == 180:
            wx, wy = -wx, -wy
        elif mag == 270:
            wx, wy = -wy, wx
    elif d == 'F':
        ship[0] += mag * wx
        ship[1] += mag * wy

result2 = dist(ship)

print(result1, result2)