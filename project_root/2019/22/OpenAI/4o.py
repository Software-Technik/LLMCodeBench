import sys

def num(line):
    return int(''.join(c for c in line if c.isdigit() or c == "-"))

def rev(position, size):
    return size - position - 1

def inc(position, size, n):
    return (n * position) % size

def cut(position, size, n):
    return (position - n) % size

def part1(data, size):
    position = 2019
    for line in data:
        if "stack" in line:
            position = rev(position, size)
        elif "inc" in line:
            position = inc(position, size, num(line))
        elif "cut" in line:
            position = cut(position, size, num(line))
    return position

DECK = 119315717514047
REPEAT = 101741582076661
POSITION = 2020
IDENTITY = [0, 1]

def shuffle_apply(f, x):
    return (f[0] + f[1] * x) % DECK

def shuffle_compose(f, g):
    return [(f[0] + f[1] * g[0]) % DECK, (f[1] * g[1]) % DECK]

def shuffle_repeat(repeat, f, step=1):
    fN = IDENTITY
    while step <= repeat:
        fN = shuffle_compose(fN, fN)
        repeat -= step
        step *= 2
    return fN

def part2(data):
    shuf = IDENTITY
    for line in data:
        if "stack" in line:
            shuf = shuffle_compose([-1, -1], shuf)
        elif "cut" in line:
            shuf = shuffle_compose([-num(line), 1], shuf)
        elif "inc" in line:
            shuf = shuffle_compose([0, num(line.split()[3])], shuf)

    shufN = shuffle_repeat(DECK - 1 - REPEAT, shuf)
    return shuffle_apply(shufN, POSITION)

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read().splitlines()

    sys.stdout.write(f"{part1(data.copy(), 10007)} {part2(data.copy())}")