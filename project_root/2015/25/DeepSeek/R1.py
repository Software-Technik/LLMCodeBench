import sys

def part1(data):
    d = data[0].split()
    r = int(d[-3][:-1])
    c = int(d[-1][:-1])
    diag = r + c - 1
    n = (diag - 1) * diag // 2 + c - 1
    power = pow(252533, n, 33554393)
    return (20151125 * power) % 33554393

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n")