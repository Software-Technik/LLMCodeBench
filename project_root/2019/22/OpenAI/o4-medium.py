import sys

def compose(f, g, m):
    return ((f[0] + f[1] * g[0]) % m, (f[1] * g[1]) % m)

def pow_transform(f, k, m):
    res = (0, 1)
    base = f
    while k:
        if k & 1:
            res = compose(base, res, m)
        base = compose(base, base, m)
        k >>= 1
    return res

def part1(lines):
    a, b = 0, 1
    m = 10007
    for line in lines:
        if line[0] == 'c':
            n = int(line[4:])
            a = (a - n) % m
        elif line[5] == 'i':
            a = (-1 - a) % m
            b = (-b) % m
        else:
            n = int(line.split()[-1])
            a = (a * n) % m
            b = (b * n) % m
    return (a + b * 2019) % m

def part2(lines):
    m = 119315717514047
    a, b = 0, 1
    for line in lines:
        if line[0] == 'c':
            n = int(line[4:])
            a = (a - n) % m
        elif line[5] == 'i':
            a = (-1 - a) % m
            b = (-b) % m
        else:
            n = int(line.split()[-1])
            a = (a * n) % m
            b = (b * n) % m
    invb = pow(b, -1, m)
    inva = (-a * invb) % m
    ai, bi = pow_transform((inva, invb), 101741582076661, m)
    return (ai + bi * 2020) % m

with open(sys.argv[1]) as f:
    lines = [l.strip() for l in f]
r1 = part1(lines)
r2 = part2(lines)
sys.stdout.write(f"{r1} {r2}")