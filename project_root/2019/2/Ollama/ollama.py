import sys

def run_program(program):
    i = 0
    while i < len(program):
        op = program[i]
        if op == 99:
            return True
        elif op in (1, 2):
            a, b, c = program[i + 1:i + 4]
            if op == 1:
                program[c] = program[a] + program[b]
            else:
                program[c] = program[a] * program[b]
            i += 4
        else:
            raise ValueError(f"Invalid opcode {op}")
    return False

def part1(data):
    program = data.copy()
    run_program(program)
    return program[0]

def part2(data):
    for noun in range(100):
        for verb in range(100):
            program = data.copy()
            program[1] = noun
            program[2] = verb
            if run_program(program) and program[0] == 19690720:
                return 100 * noun + verb

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")