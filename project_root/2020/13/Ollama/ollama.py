from functools import reduce
import sys

input_file = sys.argv[1]

with open(input_file) as f:
    lines = list(f)

start_time = int(lines[0])
departs, offsets, waits = [], [], []

for i, bus in enumerate(lines[1].split(',')):
    if bus != 'x':
        d = int(bus)
        waits.append((d - start_time % d) % d)
        departs.append(d)
        offsets.append(i)

min_wait = min(waits)
bus_id = departs[waits.index(min_wait)]
result1 = min_wait * bus_id

def chinese_remainder(n, a):
    total = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % prod

def mul_inv(a, b):
    x0, x1 = 0, 1
    if b == 1: return x0
    while a > 1:
        q = a // b
        a, b = b, (a % b)
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b
    return x1

offsets3 = [(dep - off) for dep, off in zip(departs, offsets)]
cr = chinese_remainder(departs, offsets3)

print(result1, cr)