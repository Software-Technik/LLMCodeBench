import sys

def part1(data):
    d = data[0].split()
    r = int(d[-3][:-1])
    c = int(d[-1][:-1])

    rc = (r + c - 2) * (r + c - 1) // 2 + c

    s = 20151125
    for _ in range(rc - 1):
        s = (s * 252533) % 33554393
    return s

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n")