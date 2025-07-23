import sys
import math
from collections import defaultdict

def extract_numbers(s):
    return tuple(map(float, s[3:-1].split(',')))

def parse_line(line):
    parts = line.split(', ')
    return tuple(map(extract_numbers, parts))

def magnitude(coord):
    return sum(c * c for c in coord)

def part1(data):
    min_accel = float('inf')
    min_idx = 0
    for idx, line in enumerate(data):
        _, _, a = parse_line(line)
        current_mag = magnitude(a)
        if current_mag < min_accel:
            min_accel = current_mag
            min_idx = idx
    return min_idx

def subtract_coord(c1, c2):
    return tuple(a - b for a, b in zip(c1, c2))

def subtract_particle(p1, p2):
    return (
        subtract_coord(p1[0], p2[0]),
        subtract_coord(p1[1], p2[1]),
        subtract_coord(p1[2], p2[2]),
    )

def collision(p, v, a, t):
    return (2 * v + a * (1 + t)) * t + 2 * p == 0

def check_collision(p, v, a, t):
    return all(
        collision(p[i], v[i], a[i], t)
        for i in (1, 2)
    )

def find_collision_time(p1, p2):
    p, v, a = subtract_particle(p1, p2)
    px, vx, ax = p[0], v[0], a[0]
    if ax == 0:
        if vx != 0:
            t = -px / vx
            if t > 0 and check_collision(p, v, a, t):
                return t
    else:
        b = -vx - 0.5 * ax
        D = b * b - 2 * ax * px
        if D == 0:
            t = b / ax
            if t > 0 and check_collision(p, v, a, t):
                return t
        elif D > 0:
            sqrt_D = math.sqrt(D)
            t1 = (b - sqrt_D) / ax
            t2 = (b + sqrt_D) / ax
            if t1 > 0 and check_collision(p, v, a, t1):
                return t1
            if t2 > 0 and check_collision(p, v, a, t2):
                return t2
    return None

def part2(data):
    particles = [parse_line(line) for line in data]
    collisions = defaultdict(list)

    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            t = find_collision_time(particles[i], particles[j])
            if t is not None:
                collisions[int(t)].append((i, j))

    dead = set()
    for time in sorted(collisions):
        colliding = set()
        for i, j in collisions[time]:
            if i not in dead and j not in dead:
                colliding.add(i)
                colliding.add(j)
        dead.update(colliding)

    return len(particles) - len(dead)

input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f if line.strip()]

print(part1(instructions))
print(part2(instructions))