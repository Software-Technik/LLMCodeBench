import sys

def process_input(data):
    return [(x[0], int(x[1])) for x in (line.split() for line in data)]

def part1(commands):
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
    return h * d

def part2(commands):
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
    return h * d

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]
commands = process_input(data)

print(part1(commands), part2(commands))