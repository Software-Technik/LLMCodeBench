import sys

def part1(data):
    r, c = map(lambda x: int(x[:-1]), [data[0].split()[-3], data[0].split()[-1]])
    rc = (r * (r + 1)) // 2 + ((r + 1) + (r + 1 + c - 2)) * (c - 1) // 2

    s = pow(252533, rc - 1, 33554393)
    return s * 20151125 % 33554393

data = open(sys.argv[1]).read().strip().split('\n')
sys.stdout.write(f"{part1(data)}\n")