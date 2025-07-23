import sys
from functools import reduce

def part1(data):
    target = int(data[0]) // 10
    n, s = 1, set()
    while 1:
        s = {j for i in range(1, int(n**0.5) + 1) if n % i == 0 for j in (i, n//i)}
        s.discard(n)
        if sum(s) * 2 >= target:
            return n
        n += 1

def part2(data):
    target = int(data[0])
    n, s = 1, set()
    while 1:
        s = {j for i in range(1, min(int(n**0.5) + 1, target//n + 1)) if n % i == 0 for j in (i, n//i)}
        s.discard(n)
        s = sum(i for i in s if i < 51)
        if s * 22 >= target:
            return n
        n += 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")