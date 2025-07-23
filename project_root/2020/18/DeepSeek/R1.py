import os
from itertools import chain, combinations
from copy import deepcopy
import sys
from collections import deque

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

def coords(arr2d):
    coords = []
    for y in range(len(arr2d)):
        for x in range(len(arr2d[0])):
            coords.append((x, y))
    return coords

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def ans(answer):
    pass

def strips(l): return list(map(str.strip, l))
def ints(l): return list(map(int, l))
def commas(s): return s.split(",")
def comma_ints(s): return ints(strips(s.split(",")))

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

def line_transform(line):
    return line

lines = [line_transform(line) for line in lines]

def tokenize_improved(s):
    s = s.replace("(", " ( ").replace(")", " ) ")
    chunks = s.split()
    relevant_chunks = []
    for chunk in chunks:
        if chunk in "()+*":
            relevant_chunks.append(chunk)
        else:
            num = int(chunk)
            relevant_chunks.append(num)
    return relevant_chunks

def parse1(tokens):
    left = parse_factor1(tokens)
    while tokens and tokens[0] in ['+', '*']:
        op = tokens.popleft()
        right = parse_factor1(tokens)
        if op == '+':
            left += right
        elif op == '*':
            left *= right
    return left

def parse_factor1(tokens):
    token = tokens.popleft()
    if token == '(':
        value = parse1(tokens)
        if tokens and tokens[0] == ')':
            tokens.popleft()
        return value
    else:
        return token

def parse2(tokens):
    terms = [parse_term2(tokens)]
    while tokens and tokens[0] == '*':
        tokens.popleft()
        terms.append(parse_term2(tokens))
    prod = 1
    for t in terms:
        prod *= t
    return prod

def parse_term2(tokens):
    factors = [parse_factor2(tokens)]
    while tokens and tokens[0] == '+':
        tokens.popleft()
        factors.append(parse_factor2(tokens))
    return sum(factors)

def parse_factor2(tokens):
    token = tokens.popleft()
    if token == '(':
        value = parse2(tokens)
        if tokens and tokens[0] == ')':
            tokens.popleft()
        return value
    else:
        return token

total1 = 0
total2 = 0
for line in lines:
    tokens_list = tokenize_improved(line)
    d1 = deque(tokens_list)
    total1 += parse1(d1)
    d2 = deque(tokens_list)
    total2 += parse2(d2)

print(total1, total2)