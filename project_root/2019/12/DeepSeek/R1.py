import sys
from math import gcd
from functools import reduce

def part1(data):
    positions = [list(p) for p in data]
    velocities = [[0,0,0] for _ in range(4)]
    combis = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]
    
    for _ in range(1000):
        vchanges = [[0,0,0] for _ in range(4)]
        for i, j in combis:
            for k in range(3):
                if positions[i][k] < positions[j][k]:
                    vchanges[i][k] += 1
                    vchanges[j][k] -= 1
                elif positions[i][k] > positions[j][k]:
                    vchanges[i][k] -= 1
                    vchanges[j][k] += 1
        for i in range(4):
            for k in range(3):
                velocities[i][k] += vchanges[i][k]
                positions[i][k] += velocities[i][k]
    
    energy = 0
    for i in range(4):
        pot = sum(abs(x) for x in positions[i])
        kin = sum(abs(v) for v in velocities[i])
        energy += pot * kin
    return energy

def lcm(*args):
    return reduce(lambda a, b: a * b // gcd(a, b), args)

def find_cycle(initial):
    n = len(initial)
    pos = initial[:]
    vel = [0] * n
    initial_state = (tuple(pos), tuple(vel))
    steps = 0
    
    while True:
        steps += 1
        new_vel = vel[:]
        for i in range(n):
            for j in range(i+1, n):
                if pos[i] < pos[j]:
                    new_vel[i] += 1
                    new_vel[j] -= 1
                elif pos[i] > pos[j]:
                    new_vel[i] -= 1
                    new_vel[j] += 1
        new_pos = [pos[i] + new_vel[i] for i in range(n)]
        current_state = (tuple(new_pos), tuple(new_vel))
        if current_state == initial_state:
            return steps
        pos, vel = new_pos, new_vel

def part2(data):
    xs = [p[0] for p in data]
    ys = [p[1] for p in data]
    zs = [p[2] for p in data]
    x_cycle = find_cycle(xs)
    y_cycle = find_cycle(ys)
    z_cycle = find_cycle(zs)
    return lcm(x_cycle, y_cycle, z_cycle)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
    positions = []
    for line in data.strip().split('\n'):
        coords = line.strip('<>').split(', ')
        x = int(coords[0].split('=')[1])
        y = int(coords[1].split('=')[1])
        z = int(coords[2].split('=')[1])
        positions.append((x, y, z))

sys.stdout.write(f"{part1(positions)} {part2(positions)}")