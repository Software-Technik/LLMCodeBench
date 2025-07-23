import sys
import itertools
import collections

def runComputer1(data, phase, input):
    program = data.copy()
    output = None
    i = 0
    hasUsedPhase = False

    while True:
        opcode = program[i] % 100

        if opcode == 99:
            break

        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10

        param1 = program[i+1] if mode1 == 1 or opcode == 3 else program[program[i+1]]
        if opcode in (1, 2, 5, 6, 7, 8):
            param2 = program[i+2] if mode2 == 1 else program[program[i+2]]
        else:
            param2 = None

        if opcode == 1:
            program[program[i+3]] = param1 + param2
            i += 4
        elif opcode == 2:
            program[program[i+3]] = param1 * param2
            i += 4
        elif opcode == 3:
            program[program[i+1]] = input if hasUsedPhase else phase
            hasUsedPhase = True
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
        else:
            raise ValueError(f'opcode {opcode} from {program[i]}')

    if output is None:
        raise ValueError(f'input {input} resulted in no output')

    return output

def part1(data):
    max_output = 0
    for seq in itertools.permutations(range(5), 5):
        amplification = 0
        for phase in seq:
            amplification = runComputer1(data, phase, amplification)
        if amplification > max_output:
            max_output = amplification
    return max_output

class Computer:
    __slots__ = ['i', 'lastOutput', 'halted', 'phase', 'hasUsedPhase', 'program']
    def __init__(self, program, phase):
        self.i = 0
        self.lastOutput = None
        self.halted = False
        self.phase = phase
        self.hasUsedPhase = False
        self.program = program.copy()

    def run(self, input):
        if self.halted:
            raise RuntimeError("Computer was halted already")
        i, output, hasUsedPhase = runComputer2(self.program, self.i, input, self.phase, self.hasUsedPhase)
        self.i = i
        self.halted = output is None
        self.lastOutput = output
        self.hasUsedPhase = hasUsedPhase
        return output

def runComputer2(program, i, input, phase, hasUsedPhase):
    while True:
        opcode = program[i] % 100

        if opcode == 99:
            return (i, None, True)

        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10

        param1 = program[i+1] if mode1 == 1 or opcode == 3 else program[program[i+1]]
        if opcode in (1, 2, 5, 6, 7, 8):
            param2 = program[i+2] if mode2 == 1 else program[program[i+2]]
        else:
            param2 = None

        if opcode == 1:
            program[program[i+3]] = param1 + param2
            i += 4
        elif opcode == 2:
            program[program[i+3]] = param1 * param2
            i += 4
        elif opcode == 3:
            program[program[i+1]] = input if hasUsedPhase else phase
            hasUsedPhase = True
            i += 2
        elif opcode == 4:
            output = param1
            i += 2
            return (i, output, hasUsedPhase)
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
        else:
            raise ValueError(f'opcode {opcode} from {program[i]}')

def part2(data):
    max_output = 0
    for seq in itertools.permutations(range(5, 10), 5):
        computers = [Computer(data, phase) for phase in seq]
        computers[4].lastOutput = 0
        running = True

        while running:
            running = False
            for n in range(5):
                if computers[n].halted:
                    continue
                x = n - 1 if n > 0 else 4
                input_val = computers[x].lastOutput
                computers[n].run(input_val)
                running = True
            if not computers[4].halted and computers[4].lastOutput > max_output:
                max_output = computers[4].lastOutput
    return max_output

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")