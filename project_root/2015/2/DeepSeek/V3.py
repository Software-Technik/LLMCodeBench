import sys
import math

def part1(data):
    total = 0
    for line in data:
        l, w, h = map(int, line.split('x'))
        area = 2*l*w + 2*w*h + 2*h*l
        smallest_side = min(l*w, w*h, h*l)
        total += area + smallest_side
    return total

def part2(data):
    total = 0
    for line in data:
        dimensions = sorted(map(int, line.split('x')))
        ribbon = 2 * (dimensions[0] + dimensions[1])
        bow = math.prod(dimensions)
        total += ribbon + bow
    return total

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")