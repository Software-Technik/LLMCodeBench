import sys
from functools import reduce

def mul_inv(a, b):
    b0, x0, x1 = b, 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b, x0, x1 = b, a % b, x1 - q * x0, x0
    return x1 + b0 if x1 < 0 else x1

def chinese_remainder(n, a):
    total, prod = 0, reduce(lambda x, y: x * y, n)
    for ni, ai in zip(n, a):
        p = prod // ni
        total += ai * mul_inv(p, ni) * p
    return total % prod

def main():
    data = open(sys.argv[1]).read().strip().splitlines()
    start = int(data[0])
    buses = [d for d in data[1].split(',')]
    ids = [int(d) for d in buses if d != 'x']
    waits = [(-start) % d for d in ids]
    w, bus = min(zip(waits, ids))
    result1 = w * bus
    n, a = [], []
    for i, d in enumerate(buses):
        if d != 'x':
            d = int(d)
            n.append(d)
            a.append((-i) % d)
    result2 = chinese_remainder(n, a)
    print(result1, result2)

if __name__ == '__main__':
    main()