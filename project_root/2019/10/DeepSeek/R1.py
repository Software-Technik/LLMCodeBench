import sys
import math

def part1(data):
    asteroids = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append((x, y))
    
    best_count = 0
    station = None
    for p in asteroids:
        angles = set()
        for other in asteroids:
            if other == p:
                continue
            dx = other[0] - p[0]
            dy = other[1] - p[1]
            rad = math.atan2(dy, dx)
            key = int(rad * 100000) + 1
            angles.add(key)
        if len(angles) > best_count:
            best_count = len(angles)
            station = p
            
    return best_count, station

def part2(data, station):
    asteroids = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append((x, y))
    
    station_angles = {}
    for other in asteroids:
        if other == station:
            continue
        dx = other[0] - station[0]
        dy = other[1] - station[1]
        rad = math.atan2(dy, dx)
        if rad < -math.pi/2:
            rad += 2 * math.pi
        key = int(rad * 1000000)
        if key not in station_angles:
            station_angles[key] = []
        station_angles[key].append(other)
    
    for key in station_angles:
        station_angles[key].sort(key=lambda p2: abs(station[0]-p2[0])+abs(station[1]-p2[1]))
    
    count = 0
    while count < 200:
        for key in sorted(station_angles.keys()):
            if station_angles[key]:
                asteroid = station_angles[key].pop(0)
                count += 1
                if count == 200:
                    return asteroid[0] * 100 + asteroid[1]

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

part1_result, station = part1(data)
part2_result = part2(data, station)
sys.stdout.write(f"{part1_result} {part2_result}")