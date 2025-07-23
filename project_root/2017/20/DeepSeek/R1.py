import sys
import math
from collections import defaultdict

input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f if line.strip()]

def extract_numbers(s):
    return tuple(map(float, s[3:-1].split(',')))

def parse_line(line):
    parts = line.split(', ')
    return tuple(map(extract_numbers, parts))

def magnitude(coord):
    return sum(c ** 2 for c in coord)

def part1(data):
    particles = [parse_line(line) for line in data]
    min_idx = min(
        enumerate(particles),
        key=lambda kv: magnitude(kv[1][2])
    )[0]
    return min_idx

def part2(data):
    particles = [parse_line(line) for line in data]
    n = len(particles)
    collisions = defaultdict(list)
    
    for i in range(n):
        p1 = particles[i]
        for j in range(i+1, n):
            p2 = particles[j]
            px = p1[0][0] - p2[0][0]
            py = p1[0][1] - p2[0][1]
            pz = p1[0][2] - p2[0][2]
            vx = p1[1][0] - p2[1][0]
            vy = p1[1][1] - p2[1][1]
            vz = p1[1][2] - p2[1][2]
            ax = p1[2][0] - p2[2][0]
            ay = p1[2][1] - p2[2][1]
            az = p1[2][2] - p2[2][2]
            
            t = None
            if ax == 0:
                if vx == 0:
                    if px != 0:
                        t = None
                    else:
                        t = 0.0
                else:
                    t = -px / vx
                    if t < 0:
                        t = None
                    else:
                        if abs((2*vy + ay*(1+t)) * t + 2*py) > 1e-9:
                            t = None
                        elif abs((2*vz + az*(1+t)) * t + 2*pz) > 1e-9:
                            t = None
            else:
                b = -vx - 0.5 * ax
                D = b*b - 2*ax*px
                if D < 0:
                    t = None
                else:
                    times = []
                    if D == 0:
                        times.append(b / ax)
                    else:
                        times.append((b - math.sqrt(D)) / ax)
                        times.append((b + math.sqrt(D)) / ax)
                    for candidate in times:
                        if candidate < 0:
                            continue
                        if abs((2*vy + ay*(1+candidate)) * candidate + 2*py) <= 1e-9 and abs((2*vz + az*(1+candidate)) * candidate + 2*pz) <= 1e-9:
                            t = candidate
                            break
            
            if t is not None:
                it = int(t)
                collisions[it].append((i, j))
    
    dead = set()
    for time in sorted(collisions):
        colliding = set()
        for i, j in collisions[time]:
            if i not in dead and j not in dead:
                colliding.add(i)
                colliding.add(j)
        dead.update(colliding)
    
    return n - len(dead)

print(part1(instructions))
print(part2(instructions))