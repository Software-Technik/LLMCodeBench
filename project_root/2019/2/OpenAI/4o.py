import sys

def execute_program(program):
    i = 0
    while program[i] != 99:
        opcode, pos1, pos2, pos3 = program[i:i+4]
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        elif opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
        i += 4
    return program[0]

def part1(data):
    program = data[:]
    program[1], program[2] = 12, 2
    return execute_program(program)

def part2(data):
    for noun in range(100):
        for verb in range(100):
            program = data[:]
            program[1], program[2] = noun, verb
            if execute_program(program) == 19690720:
                return 100 * noun + verb

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().strip().split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")