import sys
data = open(sys.argv[1]).read().splitlines()
def part1(data):
    size = 10007
    pos = 2019
    for line in data:
        if line.startswith('deal into'):
            pos = size - pos - 1
        elif line.startswith('deal with increment'):
            n = int(line.split()[-1])
            pos = pos * n % size
        else:
            n = int(line.split()[-1])
            pos = (pos - n) % size
    return pos
def part2(data):
    m = 119315717514047
    rep = 101741582076661
    pos = 2020
    a = 0
    b = 1
    for line in data:
        if line.startswith('deal into'):
            a = (-a - 1) % m
            b = -b % m
        elif line.startswith('deal with increment'):
            n = int(line.split()[-1])
            a = a * n % m
            b = b * n % m
        else:
            n = int(line.split()[-1])
            a = (a - n) % m
    bn = pow(b, rep, m)
    if b != 1:
        an = a * (bn - 1) * pow(b - 1, m - 2, m) % m
    else:
        an = a * rep % m
    inv_bn = pow(bn, m - 2, m)
    return (pos - an) * inv_bn % m
sys.stdout.write(f"{part1(data)} {part2(data)}")