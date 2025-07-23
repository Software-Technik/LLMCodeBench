import sys

def run_program(program, noun=None, verb=None):
    if noun is not None:
        program[1] = noun
    if verb is not None:
        program[2] = verb
    i = 0
    while True:
        op = program[i]
        if op == 99:
            break
        a, b, c = program[i+1], program[i+2], program[i+3]
        if op == 1:
            program[c] = program[a] + program[b]
        elif op == 2:
            program[c] = program[a] * program[b]
        i += 4
    return program[0]

def part1(data):
    program = data.copy()
    return run_program(program, 12, 2)

def part2(data):
    for noun in range(100):
        for verb in range(100):
            program = data.copy()
            if run_program(program, noun, verb) == 19690720:
                return 100 * noun + verb

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))

sys.stdout.write(f"{part1(data)} {part2(data)}")