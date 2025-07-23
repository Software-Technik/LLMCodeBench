import sys
from collections import defaultdict

def runComputer(data, input_val):
    program = defaultdict(int, enumerate(data))
    output = None
    i = 0
    relbase = 0

    while True:
        instr = program[i]
        opcode = instr % 100
        if opcode == 99:
            break

        mode1 = (instr // 100) % 10
        mode2 = (instr // 1000) % 10
        mode3 = (instr // 10000) % 10

        p1, p2, p3 = None, None, None

        if opcode in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            if mode1 == 0:
                p1 = program[i+1]
            elif mode1 == 1:
                p1 = i+1
            else:
                p1 = program[i+1] + relbase

        if opcode in (1, 2, 5, 6, 7, 8):
            if mode2 == 0:
                p2 = program[i+2]
            elif mode2 == 1:
                p2 = i+2
            else:
                p2 = program[i+2] + relbase

        if opcode in (1, 2, 7, 8):
            if mode3 == 0:
                p3 = program[i+3]
            elif mode3 == 1:
                raise ValueError('Immediate mode invalid for param 3')
            else:
                p3 = program[i+3] + relbase

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
            i += 4
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]
            i += 4
        elif opcode == 3:
            program[p1] = input_val
            i += 2
        elif opcode == 4:
            output = program[p1]
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
            raise ValueError(f'opcode {opcode} from {instr}')

    return output

def part1(data):
    return runComputer(data, 1)

def part2(data):
    return runComputer(data, 2)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data_line = f.read().splitlines()[0]
    data = list(map(int, data_line.split(',')))
sys.stdout.write(f"{part1(data)} {part2(data)}")