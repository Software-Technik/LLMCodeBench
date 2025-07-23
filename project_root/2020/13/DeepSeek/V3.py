from functools import reduce
from math import gcd
import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

start = int(lines[0])
min_ans = []
small = float('inf')

for d in lines[1].split(","):
    if d != "x":
        d = int(d)
        m = d - (start % d)
        if m < small:
            small = m
            min_ans.append(small * d)
result1 = min_ans[-1]

departs = []
offsets3 = []
for i, d in enumerate(lines[1].split(",")):
    if d != "x":
        d = int(d)
        departs.append(d)
        offsets3.append(d - (i % d))

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

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