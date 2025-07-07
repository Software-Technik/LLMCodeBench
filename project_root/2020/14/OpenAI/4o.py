import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

lines = [(line.split(" = ")[0].strip(), line.split(" = ")[1].strip()) for line in lines]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def maskbits(mask, num):
    bnum = bin(num)[2:].zfill(36)
    bits = list(bnum)
    for i, m in enumerate(mask):
        if m != 'X':
            bits[i] = m
    return int("".join(bits), 2)

mem = {}

for l, r in lines:
    if l.startswith("mask"):
        mask = r
    else:
        mem[int(l[4 : l.find("]")])] = maskbits(mask, int(r))

result1 = sum(mem.values())

from itertools import product

def apply_premask(b, mask):
    bnum = bin(b)[2:].zfill(36)
    return ''.join(m if m != '0' else bn for m, bn in zip(mask, bnum))

def generation_x(bin_str):
    x_count = bin_str.count('X')
    for combo in product('01', repeat=x_count):
        new_str = list(bin_str)
        combo = iter(combo)
        new_str = [(next(combo) if c == 'X' else c) for c in new_str]
        yield ''.join(new_str)

mem = {}
for l, r in lines:
    if l.startswith("mask"):
        mask = r
    else:
        addr = int(l[4 : l.find("]")])
        xaddr = apply_premask(addr, mask)
        for addr in generation_x(xaddr):
            mem[int(addr, 2)] = int(r)

result2 = sum(mem.values())
print(result1, result2)