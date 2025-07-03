import sys


def part1(data):
    _left, _right = zip(*[map(int, line.split()) for line in data])
    distance = sum(abs(x - y) for x, y in zip(sorted(_left), sorted(_right)))

    return distance


def part2(data):
    _left, _right = zip(*[map(int, line.split()) for line in data])
    score = sum(x * _right.count(x) for x in _left)

    return score


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(str([part1(data), part2(data)]))
