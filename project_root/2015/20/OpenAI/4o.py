import sys

def part1(data):
    target = int(data[0]) // 10
    n = 1
    while True:
        s = sum(i + n // i for i in range(1, int(n**0.5) + 1) if n % i == 0)
        if s >= target:
            return n
        n += 1

def part2(data):
    target = int(data[0])
    n = 1
    while True:
        s = sum((i if n // i < 51 else 0) + (n // i if i < 51 else 0) for i in range(1, int(n**0.5) + 1) if n % i == 0) * 11
        if s >= target:
            return n
        n += 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")