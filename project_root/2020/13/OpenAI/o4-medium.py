import sys

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def inv(a, m):
    g, x, _ = egcd(a, m)
    return x % m

path = sys.argv[1]
lines = open(path).read().splitlines()
start = int(lines[0])
parts = lines[1].split(',')
buses = [int(x) for x in parts if x != 'x']
result1 = min(b * ((-start) % b) for b in buses)
n = []
a = []
for i, x in enumerate(parts):
    if x != 'x':
        bi = int(x)
        n.append(bi)
        a.append((-i) % bi)
N = 1
for ni in n:
    N *= ni
total = 0
for ni, ai in zip(n, a):
    p = N // ni
    total += ai * p * inv(p, ni)
result2 = total % N
print(result1, result2)