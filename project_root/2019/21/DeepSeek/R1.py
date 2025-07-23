import sys
from collections import defaultdict

def runComputer(program, inputs):
    i = 0
    relbase = 0

    while True:
        opcode = program[i] % 100

        if opcode == 99:
            break

        mode1 = (program[i] - opcode) // 100 % 10
        mode2 = (program[i] - opcode) // 1000 % 10
        mode3 = (program[i] - opcode) // 10000 % 10

        p1 = program[i+1] + relbase if mode1 == 2 else (i+1 if mode1 == 1 else program[i+1])
        p2 = program[i+2] + relbase if mode2 == 2 else (i+2 if mode2 == 1 else program[i+2])
        if mode3 == 0:
            p3 = program[i+3]
        elif mode3 == 2:
            p3 = program[i+3] + relbase
        else:
            raise ValueError('Immediate mode invalid for param 3')

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
            i += 4
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]
            i += 4
        elif opcode == 3:
            program[p1] = inputs.pop()
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
            raise ValueError(f'opcode {opcode} from {program[i]}')

def addMovesToInputStack(moves, inputsStack):
    s = "\n".join(moves) + "\n"
    inputsStack.extend(ord(c) for c in reversed(s))

def part1(data):
    program = defaultdict(int, enumerate(data))
    inputs = []
    moves = [
        "NOT A J",
        "NOT C T",
        "AND D T",
        "OR T J",
        "WALK",
    ]
    addMovesToInputStack(moves, inputs)
    runner = runComputer(program, inputs)
    result = None
    for status in runner:
        if status > 512:
            result = status
            break
    return result

def part2(data):
    program = defaultdict(int, enumerate(data))
    inputs = []
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
    runner = runComputer(program, inputs)
    result = None
    for status in runner:
        if status > 512:
            result = status
            break
    return result

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))
sys.stdout.write(f"{part1(data)} {part2(data)}")