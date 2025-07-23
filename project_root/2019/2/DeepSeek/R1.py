import sys

def run_program(program, noun, verb):
    mem = program.copy()
    n = len(mem)
    mem[1] = noun
    mem[2] = verb
    pc = 0
    while pc < n:
        op = mem[pc]
        if op == 99:
            break
        a = mem[mem[pc+1]]
        b = mem[mem[pc+2]]
        dest = mem[pc+3]
        if op == 1:
            mem[dest] = a + b
        elif op == 2:
            mem[dest] = a * b
        else:
            break
        pc += 4
    return mem[0]

def part1(data):
    return run_program(data, 12, 2)

def part2(data):
    for noun in range(100):
        for verb in range(100):
            if run_program(data, noun, verb) == 19690720:
                return 100 * noun + verb

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))

sys.stdout.write(f"{part1(data)} {part2(data)}")