import sys
from math import isqrt

def part1(data):
    target = int(data[0]) // 10
    n = 1
    while True:
        divisors = set()
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        s = sum(divisors)
        if s >= target:
            return n
        n += 1

def part2(data):
    target = int(data[0])
    n = 1
    while True:
        divisors = set()
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                if n // i <= 50:
                    divisors.add(i)
                if i <= 50:
                    divisors.add(n // i)
        s = sum(divisors) * 11
        if s >= target:
            return n
        n += 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")