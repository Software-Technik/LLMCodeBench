import sys

def part1(data):
    d = data[0].split()
    r = int(d[-3][:-1])
    c = int(d[-1][:-1])

    r1 = (r * (r - 1)) // 2 + 1
    rc = r1 + (((r + 1) + (r + 1 + c - 2)) * (c - 1)) // 2
    # print(rc)

    s = 20151125
    for i in range(rc - 1):
        s = (s * 252533) % 33554393
    return s


input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n")