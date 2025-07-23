import sys

def part1(data, size):
    position = 2019
    for line in data:
        if line == "deal into new stack":
            position = size - position - 1
        elif line.startswith("cut"):
            n = int(line.split()[-1])
            position = (position - n) % size
        elif line.startswith("deal with increment"):
            n = int(line.split()[-1])
            position = (n * position) % size
    return position

DECK = 119315717514047
REPEAT = 101741582076661
POSITION = 2020
IDENTITY = [0, 1]

def shuffle_apply(f, x):
    return (f[0] + f[1] * x) % DECK

def shuffle_compose(f, g):
    return [shuffle_apply(f, g[0]), (f[1] * g[1]) % DECK]

def shuffle_repeat(repeat, f, step=1):
    fN = IDENTITY
    if step <= repeat:
        fN, repeat = shuffle_repeat(repeat, shuffle_compose(f, f), step * 2)
    if step <= repeat:
        fN, repeat = shuffle_compose(f, fN), repeat - step
    return fN, repeat

def part2(data):
    shuf = IDENTITY
    for line in data:
        f = line.split()
        if line == "deal into new stack":
            shuf = shuffle_compose([-1, -1], shuf)
        elif line.startswith("cut"):
            shuf = shuffle_compose([-int(f[1]), 1], shuf)
        elif line.startswith("deal with increment"):
            shuf = shuffle_compose([0, int(f[3])], shuf)
    assert shuffle_repeat(DECK - 1, shuf)[0] == IDENTITY
    shufN, _ = shuffle_repeat(DECK - 1 - REPEAT, shuf)
    return shuffle_apply(shufN, POSITION)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data, 10007)} {part2(data)}")