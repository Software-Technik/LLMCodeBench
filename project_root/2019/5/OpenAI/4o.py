import sys

def solve(data, input_value):
    program = data[:]
    i = 0

    while True:
        opcode = program[i] % 100

        if opcode == 99:
            break

        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10

        param1 = program[i+1] if mode1 == 1 else program[program[i+1]]

        if opcode != 3 and opcode != 4:
            param2 = program[i+2] if mode2 == 1 else program[program[i+2]]

        if opcode == 1:
            program[program[i+3]] = param1 + param2
            i += 4
        elif opcode == 2:
            program[program[i+3]] = param1 * param2
            i += 4
        elif opcode == 3:
            program[program[i+1]] = input_value
            i += 2
        elif opcode == 4:
            output = param1
            i += 2
        elif opcode == 5:
            i = param2 if param1 != 0 else i + 3
        elif opcode == 6:
            i = param2 if param1 == 0 else i + 3
        elif opcode == 7:
            program[program[i+3]] = 1 if param1 < param2 else 0
            i += 4
        elif opcode == 8:
            program[program[i+3]] = 1 if param1 == param2 else 0
            i += 4

    return output

def part1(data):
    return solve(data, 1)

def part2(data):
    return solve(data, 5)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().strip().split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")