import sys

def part1(data):
    return simulate(data, 2)

def part2(data):
    return simulate(data, 10)

def simulate(data, knots_num):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    knots = [(0, 0)] * knots_num
    positions = set()

    for line in data:
        _dir, n = line.split()
        dx, dy = directions[_dir]

        for _ in range(int(n)):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)

            for idx in range(knots_num - 1):
                _w = knots[idx][0] - knots[idx + 1][0]
                _h = knots[idx][1] - knots[idx + 1][1]

                if abs(_w) == 2 or abs(_h) == 2:
                    x_move = (_w > 0) - (_w < 0)
                    y_move = (_h > 0) - (_h < 0)
                    knots[idx + 1] = (knots[idx + 1][0] + x_move, knots[idx + 1][1] + y_move)

            positions.add(knots[-1])

    return len(positions)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")