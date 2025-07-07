import sys
import itertools

def runComputer(program, phase, input_signal):
    program = program[:]
    output = None
    i = 0
    hasUsedPhase = False

    while True:
        opcode = program[i] % 100

        if opcode == 99:
            return output

        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10

        param1 = program[i+1] if mode1 else program[program[i+1]]
        if opcode in [1, 2, 5, 6, 7, 8]:
            param2 = program[i+2] if mode2 else program[program[i+2]]

        if opcode in [1, 2, 7, 8]:
            param3 = program[i+3]

        if opcode == 1: # add
            program[param3] = param1 + param2
            i += 4
        elif opcode == 2: # mul
            program[param3] = param1 * param2
            i += 4
        elif opcode == 3: # mov
            program[program[i+1]] = input_signal if hasUsedPhase else phase
            hasUsedPhase = True
            i += 2
        elif opcode == 4: # out
            output = param1
            i += 2
        elif opcode == 5: # jump-if-true
            i = param2 if param1 != 0 else i + 3
        elif opcode == 6: # jump-if-false
            i = param2 if param1 == 0 else i + 3
        elif opcode == 7: # less-than
            program[param3] = int(param1 < param2)
            i += 4
        elif opcode == 8: # equals
            program[param3] = int(param1 == param2)
            i += 4
        else:
            raise ValueError(f"Invalid opcode {opcode} at position {i}")

def part1(data):
    max_signal = 0
    for phases in itertools.permutations(range(5)):
        signal = 0
        for phase in phases:
            signal = runComputer(data, phase, signal)
        max_signal = max(max_signal, signal)
    return max_signal

def runComputerLoop(program, phases):
    programs = [program[:] for _ in range(5)]
    positions = [0] * 5
    inputs = [0] + [-1] * 4
    hasUsedPhase = [False] * 5

    signal = 0
    while True:
        for i in range(5):
            program = programs[i]
            pos = positions[i]

            while True:
                opcode = program[pos] % 100

                if opcode == 99:
                    if i == 4:
                        return signal
                    positions[i] = pos
                    break

                mode1 = (program[pos] // 100) % 10
                mode2 = (program[pos] // 1000) % 10

                param1 = program[pos+1] if mode1 else program[program[pos+1]]
                if opcode in [1, 2, 5, 6, 7, 8]:
                    param2 = program[pos+2] if mode2 else program[program[pos+2]]

                if opcode in [1, 2, 7, 8]:
                    param3 = program[pos+3]

                if opcode == 1:
                    program[param3] = param1 + param2
                    pos += 4
                elif opcode == 2:
                    program[param3] = param1 * param2
                    pos += 4
                elif opcode == 3:
                    program[program[pos+1]] = phases[i] if not hasUsedPhase[i] else signal
                    hasUsedPhase[i] = True
                    pos += 2
                elif opcode == 4:
                    signal = param1
                    pos += 2
                    positions[i] = pos
                    break
                elif opcode == 5:
                    pos = param2 if param1 != 0 else pos + 3
                elif opcode == 6:
                    pos = param2 if param1 == 0 else pos + 3
                elif opcode == 7:
                    program[param3] = int(param1 < param2)
                    pos += 4
                elif opcode == 8:
                    program[param3] = int(param1 == param2)
                    pos += 4
                else:
                    raise ValueError(f"Invalid opcode {opcode} at position {pos}")

def part2(data):
    max_signal = 0
    for phases in itertools.permutations(range(5, 10)):
        signal = runComputerLoop(data, phases)
        max_signal = max(max_signal, signal)
    return max_signal

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = list(map(int, f.read().strip().split(",")))

    print(part1(data), part2(data))