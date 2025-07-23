import sys

def solve(data, input):
    program = memoryview(data)
    output = 'no result found'
    i = 0

    while True:
        opcode = program[i] % 100
        mode1 = (program[i] - opcode) // 100 % 10
        mode2 = (program[i] - opcode) // 1000 % 10

        param1, param2 = None, None

        if opcode in [1, 2, 7, 8]:
            param1 = program[program[i+1]] if mode1 == 0 else program[i+1]
            param2 = program[program[i+2]] if mode2 == 0 else program[i+2]

        if opcode < 4:
            if opcode in [5, 6]:
                i += 3
            if opcode in [7, 8]:
                i += 4
            continue

        elif opcode == 99:
            break

        output = param1
        i += 2

    return output

def part1(data):
    return solve(data, 1)

def part2(data):
    return solve(data, 5)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))

sys.stdout.write(f"{part1(data.copy())} {part2(data)}")