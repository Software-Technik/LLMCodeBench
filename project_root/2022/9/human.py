import sys

def part1(data):
    return simulate(data, 2)

def part2(data):
    return simulate(data, 10)

def simulate(data, knots_num):
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    knots = [(0, 0) for _ in range(knots_num)]

    positions = set()
    positions.add(knots[-1])

    for line in data:
        _dir, n = line.split()

        for _ in range(int(n)):
            knots[0] = (knots[0][0] + directions[_dir][0], knots[0][1] + directions[_dir][1])

            for idx in range(knots_num - 1):
                _w = knots[idx][0] - knots[idx + 1][0]
                _h = knots[idx][1] - knots[idx + 1][1]
                dx, dy = 0, 0
                if abs(_w) == 2 or abs(_h) == 2:
                    dx = 0 if _w == 0 else 1 if _w > 0 else -1
                    dy = 0 if _h == 0 else 1 if _h > 0 else -1
                if dx or dy:
                    knots[idx + 1] = (knots[idx + 1][0] + dx, knots[idx + 1][1] + dy)
            positions.add(knots[-1])
    return len(positions)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")