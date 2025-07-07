import sys
from collections import defaultdict

def runComputer(data, input):
    program = defaultdict(int, enumerate(data))
    i = 0
    relbase = 0

    def get_param(offset, mode):
        if mode == 0:
            return program[program[i + offset]]
        elif mode == 1:
            return program[i + offset]
        elif mode == 2:
            return program[program[i + offset] + relbase]
        else:
            raise ValueError("Unknown mode")

    def get_addr(offset, mode):
        if mode == 0:
            return program[i + offset]
        elif mode == 2:
            return program[i + offset] + relbase
        else:
            raise ValueError("Invalid address mode")

    while True:
        opcode = program[i] % 100
        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10
        mode3 = (program[i] // 10000) % 10

        if opcode == 99:
            break

        if opcode == 1:
            program[get_addr(3, mode3)] = get_param(1, mode1) + get_param(2, mode2)
            i += 4
        elif opcode == 2:
            program[get_addr(3, mode3)] = get_param(1, mode1) * get_param(2, mode2)
            i += 4
        elif opcode == 3:
            program[get_addr(1, mode1)] = input
            i += 2
        elif opcode == 4:
            output = get_param(1, mode1)
            i += 2
        elif opcode == 5:
            i = get_param(2, mode2) if get_param(1, mode1) != 0 else i + 3
        elif opcode == 6:
            i = get_param(2, mode2) if get_param(1, mode1) == 0 else i + 3
        elif opcode == 7:
            program[get_addr(3, mode3)] = 1 if get_param(1, mode1) < get_param(2, mode2) else 0
            i += 4
        elif opcode == 8:
            program[get_addr(3, mode3)] = 1 if get_param(1, mode1) == get_param(2, mode2) else 0
            i += 4
        elif opcode == 9:
            relbase += get_param(1, mode1)
            i += 2
        else:
            raise ValueError(f'Unknown opcode {opcode}')
    
    return output

def part1(data):
    return runComputer(data, 1)

def part2(data):
    return runComputer(data, 2)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().strip().split(',')))
    sys.stdout.write(f"{part1(data)} {part2(data)}")