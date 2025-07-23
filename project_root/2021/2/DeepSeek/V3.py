import sys

def part1(data):
    h = d = 0
    for line in data:
        cmd, val = line.split()
        val = int(val)
        if cmd == 'forward':
            h += val
        elif cmd == 'down':
            d += val
        elif cmd == 'up':
            d -= val
    return h * d

def part2(data):
    aim = h = d = 0
    for line in data:
        cmd, val = line.split()
        val = int(val)
        if cmd == 'forward':
            h += val
            d += val * aim
        elif cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
    return h * d

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")