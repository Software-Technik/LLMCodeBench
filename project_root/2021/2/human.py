import sys

def part1(data):
    data = [x.split() for x in data]
    commands = [(x[0], int(x[1])) for x in data]

    h, d = 0, 0

    for cmd, val in commands:
        if cmd == 'forward':
            h += val
        elif cmd == 'down':
            d += val
        elif cmd == 'up':
            d -= val
        else:
            raise ValueError('Invalid command')

    return h * d    # 1962940

def part2(data):
    data = [x.split() for x in data]
    commands = [(x[0], int(x[1])) for x in data]

    aim, h, d = 0, 0, 0

    for cmd, val in commands:
        if cmd == 'forward':
            h += val
            d += val * aim
        elif cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
        else:
            raise ValueError('Invalid command')

    return h * d    # 1813664422

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")