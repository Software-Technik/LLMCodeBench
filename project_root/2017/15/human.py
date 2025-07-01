import sys

FACTOR_A = 16807
FACTOR_B = 48271
DIVISOR = 2147483647

def find_next(value, factor, mask):
    while True:
        value = (value * factor) % DIVISOR
        if (value & mask) == 0:
            return value

def solve(limit, multiA, multiB):
    a = 699
    b = 124
    count = 0
    for _ in range(limit):
        a = find_next(a, FACTOR_A, multiA - 1)
        b = find_next(b, FACTOR_B, multiB - 1)
        if (a ^ b) & 0xFFFF == 0:
            count += 1
    return count

def part1(data):
    # Pas besoin des données dans ce cas précis, valeurs initiales fixes dans le code Nim
    return solve(40_000_000, 1, 1)

def part2(data):
    return solve(5_000_000, 4, 8)

# Bloc standard d'entrée/sortie
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

import sys
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")