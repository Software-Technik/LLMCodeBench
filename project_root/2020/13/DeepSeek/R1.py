import sys
from functools import reduce
from math import gcd

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

if not lines:
    sys.exit(0)

start = int(lines[0])
min_wait = float('inf')
min_product = None

bus_ids = []
for d in lines[1].split(","):
    if d != "x":
        bus_id = int(d)
        bus_ids.append(bus_id)
        wait = bus_id - (start % bus_id)
        if wait < min_wait:
            min_wait = wait
            min_product = wait * bus_id

result1 = min_product

departs = []
offsets = []
offsets3 = []
for i, d in enumerate(lines[1].split(",")):
    if d != "x":
        d_val = int(d)
        departs.append(d_val)
        offsets.append(i)
        offsets3.append((-i) % d_val)

def chinese_remainder(n, a):
    prod = reduce(lambda a, b: a * b, n)
    total = 0
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

result2 = chinese_remainder(departs, offsets3)
print(result1, result2)