import sys
from collections import defaultdict

def runComputer(data, input):
    program = defaultdict(int, {k: v for k, v in enumerate(data)})
    i = 0
    relbase = 0

    def get_index(offset, mode):
        if mode == 0: return program[i + offset]
        if mode == 1: return i + offset
        if mode == 2: return program[i + offset] + relbase

    while True:
        opcode = program[i] % 100
        if opcode == 99: break

        modes = [(program[i] // (10 ** x)) % 10 for x in range(2, 5)]
        p1 = get_index(1, modes[0])
        p2 = get_index(2, modes[1])
        p3 = get_index(3, modes[2])

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
            i += 4
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]
            i += 4
        elif opcode == 3:
            program[p1] = input.pop()
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
            raise ValueError(f'Unknown opcode {opcode}')

def addMovesToInputStack(moves, inputsStack):
    for i in reversed([ord(c) for line in moves for c in (line + "\n")]):
        inputsStack.append(i)

def part1(data):
    inputs = []
    runner = runComputer(data, inputs)
    level = ""
    result = None
    moves = [
        "NOT A J",
        "NOT C T",
        "AND D T",
        "OR T J",
        "WALK",
    ]
    addMovesToInputStack(moves, inputs)

    while True:
        status = next(runner, 'halt')
        if status == 'halt': break

        if status > 512:
            return status
        else:
            level += chr(status)

def part2(data):
    inputs = []
    runner = runComputer(data, inputs)
    level = ""
    result = None
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
    addMovesToInputStack(moves, inputs)

    while True:
        status = next(runner, 'halt')
        if status == 'halt': break

        if status > 512:
            return status
        else:
            level += chr(status)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")