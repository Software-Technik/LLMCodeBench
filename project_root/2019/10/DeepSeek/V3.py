import sys
import math

def part1(data):
    points = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                points.add((x, y))
    
    max_count = 0
    for p in points:
        angles = set()
        for other in points:
            if p == other:
                continue
            dx = other[0] - p[0]
            dy = other[1] - p[1]
            angle = math.atan2(dy, dx)
            angles.add(angle)
        if len(angles) > max_count:
            max_count = len(angles)
    return max_count

def part2(data):
    points = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                points.add((x, y))
    
    station = None
    max_count = 0
    for p in points:
        angles = set()
        for other in points:
            if p == other:
                continue
            dx = other[0] - p[0]
            dy = other[1] - p[1]
            angle = math.atan2(dy, dx)
            angles.add(angle)
        if len(angles) > max_count:
            max_count = len(angles)
            station = p
    
    angle_map = {}
    for other in points:
        if other == station:
            continue
        dx = other[0] - station[0]
        dy = other[1] - station[1]
        angle = math.atan2(dy, dx)
        if angle < -math.pi/2:
            angle += 2 * math.pi
        distance = abs(dx) + abs(dy)
        if angle not in angle_map:
            angle_map[angle] = []
        angle_map[angle].append((distance, other))
    
    for angle in angle_map:
        angle_map[angle].sort()
    
    sorted_angles = sorted(angle_map.keys())
    count = 0
    while True:
        for angle in sorted_angles:
            if angle_map[angle]:
                distance, (x, y) = angle_map[angle].pop(0)
                count += 1
                if count == 200:
                    return x * 100 + y

with open(sys.argv[1]) as f:
    data = list(f.read().splitlines())

sys.stdout.write(f"{part1(data)} {part2(data)}")