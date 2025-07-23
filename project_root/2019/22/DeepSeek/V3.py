import sys

def num(line):
    return int(''.join(filter(lambda x: x.isdigit() or x == "-", line)))

def part1(data, size):
    position = 2019
    for line in data:
        if "stack" in line:
            position = size - position - 1
        elif "inc" in line:
            n = num(line)
            position = (n * position) % size
        elif "cut" in line:
            n = num(line)
            position = (position - n) % size
    return position

DECK = 119315717514047
REPEAT = 101741582076661
POSITION = 2020
IDENTITY = [0, 1]

def shuffle_apply(f, x):
    return (f[0] + f[1] * x) % DECK

def shuffle_compose(f, g):
    return [(f[0] + f[1] * g[0]) % DECK, (f[1] * g[1]) % DECK]

def shuffle_pow(shuf, power):
    result = IDENTITY.copy()
    while power > 0:
        if power % 2 == 1:
            result = shuffle_compose(result, shuf)
        shuf = shuffle_compose(shuf, shuf)
        power //= 2
    return result

def part2(data):
    shuf = IDENTITY.copy()
    for line in data:
        parts = line.split()
        if line == "deal into new stack":
            new_shuf = [-1, -1]
        elif line.startswith("cut"):
            n = int(parts[-1])
            new_shuf = [-n, 1]
        elif line.startswith("deal with increment"):
            n = int(parts[-1])
            new_shuf = [0, n]
        shuf = shuffle_compose(new_shuf, shuf)
    
    inv_shuf = shuffle_pow(shuf, DECK - 1 - REPEAT)
    return shuffle_apply(inv_shuf, POSITION)

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

print(f"{part1(data, 10007)} {part2(data)}")