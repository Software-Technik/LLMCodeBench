import sys

def process_commands(data):
    commands = (line.split() for line in data)
    return ((cmd, int(val)) for cmd, val in commands)

def part1(data):
    h, d = 0, 0
    for cmd, val in process_commands(data):
        if cmd == 'forward':
            h += val
        elif cmd == 'down':
            d += val
        elif cmd == 'up':
            d -= val
    return h * d

def part2(data):
    aim, h, d = 0, 0, 0
    for cmd, val in process_commands(data):
        if cmd == 'forward':
            h += val
            d += val * aim
        elif cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
    return h * d

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")