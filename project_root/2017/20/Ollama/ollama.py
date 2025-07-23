import sys
import math

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

def subtract_particle(p1, p2):
    return tuple(tuple(a - b for a, b in zip(c1, c2)) for c1, c2 in zip(p1, p2))

def collision(p, v, a, t):
    return (2 * v + a * (1 + t)) * t + 2 * p == 0

def check_collision(p, v, a, t):
    return all(
        collision(p[i], v[i], a[i], t)
        for i in range(3)
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
            for t in [(b - math.sqrt(D)) / ax, (b + math.sqrt(D)) / ax]:
                if t > 0 and check_collision(p, v, a, t):
                    return t
    return None

def part2(data):
    particles = [parse_line(line) for line in data]
    dead = set()

    n = len(particles)
    for i in range(n - 1):
        if i in dead:
            continue
        for j in range(i + 1, n):
            if j in dead:
                continue
            t = find_collision_time(particles[i], particles[j])
            if t is not None:
                dead.update([i, j])

    return len(particles) - len(dead)

print(part1(instructions))
print(part2(instructions))