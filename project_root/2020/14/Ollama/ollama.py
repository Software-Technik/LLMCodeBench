import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    data = []
    lines = []

def line_transform(line):
    l, r = line.split("=")
    return (l.strip(), r.strip())

lines = [line_transform(line) for line in lines]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def maskbits(mask, num):
    ones = find(mask, "1")
    zeroes = find(mask, "0")
    bnum = bin(num)[2:].zfill(36)
    bits = list(bnum)
    for i in ones:
        bits[i] = "1"
    for i in zeroes:
        bits[i] = "0"

    return int("".join(bits), 2)

mem = {}
for l, r in lines:
    if l.startswith("mask"):
        mask = r
    else:
        val = int(r)
        addr = int(l[4:].strip("[]"))
        write_val = maskbits(mask, val)
        mem[addr] = write_val

result1 = sum(mem.values())

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

from itertools import chain, combinations
import copy

num2bin = lambda num: bin(num)[2:].zfill(36)

def apply_premask(b, mask):
    ones = find(mask, "1")
    xs = find(mask, "X")
    bnum = num2bin(b)
    bits = list(bnum)
    for i in ones:
        bits[i] = "1"
    for i in xs:
        bits[i] = "X"
    return "".join(bits)

def generation_x(bin_str):
    xidx = find(bin_str, "X")
    og_bits = list(bin_str)
    for i in xidx:
        og_bits[i] = "0"
    pool = []
    for write_to in powerset(xidx):
        bits = copy.deepcopy(og_bits)
        for loc in write_to:
            bits[loc] = "1"
        pool.append("".join(bits).zfill(36))
    return pool

mem = {}
for l, r in lines:
    if l.startswith("mask"):
        premask = r
    else:
        val = int(r)
        addr = int(l[4:].strip("[]"))
        xaddr = apply_premask(addr, premask)
        for addr in generation_x(xaddr):
            mem[int(addr, 2)] = val

result2 = sum(mem.values())
print(result1, result2)