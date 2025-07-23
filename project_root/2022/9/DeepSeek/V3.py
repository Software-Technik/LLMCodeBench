import sys

def part1(data):
    return simulate(data, 2)

def part2(data):
    return simulate(data, 10)

def simulate(data, knots_num):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    knots = [(0, 0) for _ in range(knots_num)]
    positions = {knots[-1]}

    for line in data:
        _dir, n = line.split()
        dx_head, dy_head = directions[_dir]
        n = int(n)

        for _ in range(n):
            knots[0] = (knots[0][0] + dx_head, knots[0][1] + dy_head)

            for idx in range(knots_num - 1):
                _w = knots[idx][0] - knots[idx + 1][0]
                _h = knots[idx][1] - knots[idx + 1][1]
                dx = dy = 0
                if abs(_w) > 1 or abs(_h) > 1:
                    dx = (_w > 0) - (_w < 0)
                    dy = (_h > 0) - (_h < 0)
                if dx or dy:
                    knots[idx + 1] = (knots[idx + 1][0] + dx, knots[idx + 1][1] + dy)
            positions.add(knots[-1])
    return len(positions)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")