from functools import reduce
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().strip().splitlines()
except:
    data, lines = "", []

start = int(lines[0])
buses = [(int(bus), idx) for idx, bus in enumerate(lines[1].split(",")) if bus != "x"]

result1 = min(((bus - start % bus) * bus, bus) for bus, _ in buses)[0]

def chinese_remainder(n, a):
    total = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

n = [bus for bus, _ in buses]
a = [bus - idx % bus for bus, idx in buses]

result2 = chinese_remainder(n, a)

print(result1, result2)