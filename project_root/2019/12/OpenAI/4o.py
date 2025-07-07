import sys
from math import gcd
from functools import reduce

def part1(data):
    positions = [list(pos) for pos in data]
    velocities = [[0, 0, 0] for _ in range(4)]

    for _ in range(1000):
        for one in range(4):
            for two in range(one+1, 4):
                for i in range(3):
                    if positions[one][i] < positions[two][i]:
                        velocities[one][i] += 1
                        velocities[two][i] -= 1
                    elif positions[one][i] > positions[two][i]:
                        velocities[one][i] -= 1
                        velocities[two][i] += 1

        for one in range(4):
            for i in range(3):
                positions[one][i] += velocities[one][i]

    return sum(
        sum(map(abs, positions[one])) * sum(map(abs, velocities[one]))
        for one in range(4)
    )

def lcm(a, b, c):
    return (a * b // gcd(a, b)) * c // gcd(a * b // gcd(a, b), c)

def part2(data):
    initial_positions = [list(pos) for pos in data]
    velocities = [[0, 0, 0] for _ in range(4)]
    
    periods = [None, None, None]
    step = 0

    while not all(periods):
        step += 1

        for one in range(4):
            for two in range(one+1, 4):
                for i in range(3):
                    if initial_positions[one][i] < initial_positions[two][i]:
                        velocities[one][i] += 1
                        velocities[two][i] -= 1
                    elif initial_positions[one][i] > initial_positions[two][i]:
                        velocities[one][i] -= 1
                        velocities[two][i] += 1

        for one in range(4):
            for i in range(3):
                initial_positions[one][i] += velocities[one][i]

        for i in range(3):
            if periods[i] is None and all(
                initial_positions[one][i] == data[one][i] and velocities[one][i] == 0
                for one in range(4)
            ):
                periods[i] = step

    return lcm(*periods)

def parse_input(filepath):
    with open(filepath) as f:
        return [
            tuple(int(coord.split('=')[1]) for coord in line.strip('<>').split(', '))
            for line in f.read().strip().split('\n')
        ]

if __name__ == "__main__":
    filepath = sys.argv[1]
    positions = parse_input(filepath)
    print(f"{part1(positions)} {part2(positions)}")