import sys

def part1(data):
    return simulate(data, 2)

def part2(data):
    return simulate(data, 10)

def simulate(data, knots_num):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    knots = [(0, 0)] * knots_num
    positions = {knots[-1]}
    for line in data:
        _dir, n = line.split()
        steps = int(n)
        dx, dy = directions[_dir]
        for _ in range(steps):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for idx in range(knots_num - 1):
                x_diff = knots[idx][0] - knots[idx + 1][0]
                y_diff = knots[idx][1] - knots[idx + 1][1]
                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    knots[idx + 1] = (knots[idx][0] - min(dx, x_diff), knots[idx][1] - min(dy, y_diff))
            positions.add(knots[-1])
    return len(positions)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")