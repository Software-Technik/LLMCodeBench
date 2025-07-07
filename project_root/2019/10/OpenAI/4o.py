import sys
import math
from collections import defaultdict

def compute_points(data):
    points = {}
    y = 0
    for line in data:
        for x, char in enumerate(line):
            if char == "#":
                points[(x, y)] = defaultdict(list)
        y += 1
    return points

def calculate_angles(points):
    for p in points:
        for other in points:
            if p != other:
                dx, dy = other[0] - p[0], other[1] - p[1]
                rad = math.atan2(dy, dx)
                key = int(rad * 1e6)
                points[p][key].append(other)

def sort_by_distance(points):
    for p in points:
        for key in points[p]:
            points[p][key].sort(key=lambda p2: (abs(p[0] - p2[0]), abs(p[1] - p2[1])))

def part1(data):
    points = compute_points(data)
    calculate_angles(points)
    result = max(points, key=lambda p: len(points[p]))
    return len(points[result])

def part2(data):
    points = compute_points(data)
    calculate_angles(points)
    sort_by_distance(points)
    station = max(points, key=lambda p: len(points[p]))
    all_keys = sorted(points[station])

    count = 0
    while True:
        for key in all_keys:
            if points[station][key]:
                count += 1
                target = points[station][key].pop(0)
                if count == 200:
                    return target[0] * 100 + target[1]

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

print(f"{part1(data)} {part2(data)}")