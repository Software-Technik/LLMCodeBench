import os
import sys
import shutil
from itertools import chain, combinations
from copy import deepcopy
import math

input_path = sys.argv[1]

input_file = input_path
if "s" in sys.argv:
    input_file = "input_small.txt"
try:
    with open(input_file) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

def coords(arr2d):
    for y in range(len(arr2d)):
        for x in range(len(arr2d[y])):
            yield (x, y)

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def ans(answer):
    pass

strips = lambda l: list(map(str.strip, l))
ints = lambda l: list(map(int, l))
commas = lambda s: s.split(",")
comma_ints = lambda s: ints(strips(s.split(",")))

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

a, b = map(int, data.splitlines())
door_pub = a
card_pub = b

mod = 20201227

def trans(sub, loop_size):
    return pow(sub, loop_size, mod)

def find(sub, goal):
    m = math.isqrt(mod) + 1
    baby = {}
    x = 1
    for k in range(m):
        if x not in baby:
            baby[x] = k
        x = (x * sub) % mod
    g = pow(sub, m, mod)
    g_inv = pow(g, mod-2, mod)
    current = goal
    for j in range(m+1):
        if current in baby:
            k_val = baby[current]
            loop_size = j * m + k_val
            return loop_size
        current = (current * g_inv) % mod
    return None

door_loop = find(7, a)
card_loop = find(7, b)
secret = trans(door_pub, card_loop)
secret2 = trans(card_pub, door_loop)
print(secret, secret2)