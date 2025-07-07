import sys

DECK = 119315717514047
REPEAT = 101741582076661
POSITION = 2020

def num(line):
    return int(''.join(c for c in line if c.isdigit() or c == '-'))

def part1(data, size):
    ops = []
    for line in data:
        if line == "deal into new stack":
            ops.append(("rev", None))
        elif line.startswith("deal with increment"):
            ops.append(("inc", num(line)))
        else:
            ops.append(("cut", num(line)))
    pos = 2019
    for op, v in ops:
        if op == "rev":
            pos = size - pos - 1
        elif op == "inc":
            pos = (v * pos) % size
        else:
            pos = pos - v if pos >= v else size - (v - pos)
    return pos

def compose(f, g):
    return ((f[0] + f[1] * g[0]) % DECK, (f[1] * g[1]) % DECK)

def f_pow(f, n):
    res = (0, 1)
    base = f
    while n:
        if n & 1:
            res = compose(base, res)
        base = compose(base, base)
        n >>= 1
    return res

def part2(data):
    shuf = (0, 1)
    for line in data:
        if line == "deal into new stack":
            shuf = compose((-1) % DECK, -1 % DECK), None  # placeholder
        # Fix above placeholder by writing correct tuple directly
        # Actually we need to handle signs:
        # deal into new stack: f(x) = -1 - x => a = -1, b = -1

def part2(data):
    shuf = (0, 1)
    for line in data:
        if line == "deal into new stack":
            f = (-1, -1)
        elif line.startswith("cut"):
            n = int(line.split()[1])
            f = (-n, 1)
        else:
            n = int(line.split()[3])
            f = (0, n)
        shuf = compose(f, shuf)
    inv_repeat = DECK - 1 - REPEAT
    fN = f_pow(shuf, inv_repeat)
    return (fN[0] + fN[1] * POSITION) % DECK

if __name__ == "__main__":
    data = open(sys.argv[1]).read().splitlines()
    sys.stdout.write(f"{part1(data, 10007)} {part2(data)}")