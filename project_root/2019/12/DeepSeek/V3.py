import sys
from itertools import combinations
from math import gcd
from functools import reduce

def part1(data):
    positions = [list(p) for p in data]
    velocities = [[0, 0, 0] for _ in range(4)]

    for _ in range(1000):
        for i, j in combinations(range(4), 2):
            for k in range(3):
                if positions[i][k] < positions[j][k]:
                    velocities[i][k] += 1
                    velocities[j][k] -= 1
                elif positions[i][k] > positions[j][k]:
                    velocities[i][k] -= 1
                    velocities[j][k] += 1

        for i in range(4):
            for k in range(3):
                positions[i][k] += velocities[i][k]

    energy = 0
    for i in range(4):
        pot = sum(abs(x) for x in positions[i])
        kin = sum(abs(v) for v in velocities[i])
        energy += pot * kin
    return energy

def lcm(a, b):
    return a * b // gcd(a, b)

def part2(data):
    positions = [list(p) for p in data]
    velocities = [[0, 0, 0] for _ in range(4)]
    initial_pos = [[p[i] for p in positions] for i in range(3)]
    initial_vel = [[v[i] for v in velocities] for i in range(3)]
    cycles = [0, 0, 0]

    for step in range(1, 1000000):
        for i, j in combinations(range(4), 2):
            for k in range(3):
                if positions[i][k] < positions[j][k]:
                    velocities[i][k] += 1
                    velocities[j][k] -= 1
                elif positions[i][k] > positions[j][k]:
                    velocities[i][k] -= 1
                    velocities[j][k] += 1

        for i in range(4):
            for k in range(3):
                positions[i][k] += velocities[i][k]

        for k in range(3):
            if cycles[k] == 0:
                current_pos = [p[k] for p in positions]
                current_vel = [v[k] for v in velocities]
                if (current_pos == initial_pos[k] and 
                    current_vel == initial_vel[k]):
                    cycles[k] = step

        if all(cycles):
            return reduce(lcm, cycles)

    return 0

with open(sys.argv[1]) as f:
    data = []
    for line in f:
        parts = line.strip()[1:-1].split(', ')
        x = int(parts[0][2:])
        y = int(parts[1][2:])
        z = int(parts[2][2:])
        data.append((x, y, z))

print(f"{part1(data)} {part2(data)}")