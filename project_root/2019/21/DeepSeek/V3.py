import sys
from collections import defaultdict

def run_computer(data, input_stack):
    program = defaultdict(int, {k: v for k, v in enumerate(data)})
    i = relbase = 0

    while True:
        opcode = program[i] % 100
        if opcode == 99:
            break

        modes = [(program[i] // 10**d) % 10 for d in range(2, 5)]
        params = []
        for m, offset in zip(modes, [1, 2, 3]):
            if m == 0:
                params.append(program[i + offset])
            elif m == 1:
                params.append(i + offset)
            else:
                params.append(program[i + offset] + relbase)

        p1, p2, p3 = params

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
            i += 4
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]
            i += 4
        elif opcode == 3:
            program[p1] = input_stack.pop()
            i += 2
        elif opcode == 4:
            yield program[p1]
            i += 2
        elif opcode == 5:
            i = program[p2] if program[p1] != 0 else i + 3
        elif opcode == 6:
            i = program[p2] if program[p1] == 0 else i + 3
        elif opcode == 7:
            program[p3] = 1 if program[p1] < program[p2] else 0
            i += 4
        elif opcode == 8:
            program[p3] = 1 if program[p1] == program[p2] else 0
            i += 4
        elif opcode == 9:
            relbase += program[p1]
            i += 2
        else:
            raise ValueError(f'Invalid opcode {opcode}')

def add_moves_to_input(moves, input_stack):
    for c in reversed(''.join(moves) + '\n'):
        input_stack.append(ord(c))

def part1(data):
    inputs = []
    runner = run_computer(data, inputs)
    moves = [
        "NOT A J",
        "NOT C T",
        "AND D T",
        "OR T J",
        "WALK",
    ]
    add_moves_to_input(moves, inputs)
    result = None
    for status in runner:
        if status > 255:
            result = status
            break
    return result

def part2(data):
    inputs = []
    program = defaultdict(int, {k: v for k, v in enumerate(data)})
    runner = run_computer(program, inputs)
    moves = [
        "NOT C T",
        "OR T J",
        "NOT E T",
        "NOT T T",
        "OR H T",
        "AND T J",
        "NOT A T",
        "OR T J",
        "AND D J",
        "NOT B T",
        "NOT T T",
        "OR E T",
        "NOT T T",
        "OR T J",
        "RUN",
    ]
    add_moves_to_input(moves, inputs)
    result = None
    for status in runner:
        if status > 255:
            result = status
            break
    return result

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

print(f"{part1(data)} {part2(data)}")