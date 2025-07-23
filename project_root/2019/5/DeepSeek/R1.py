import sys

def solve(data, input_val):
    program = data.copy()
    output = 'no result found'
    i = 0

    while True:
        opcode = program[i] % 100
        if opcode == 99:
            break

        if opcode == 3:
            addr = program[i+1]
            program[addr] = input_val
            i += 2
        elif opcode == 4:
            modes = program[i] // 100
            mode1 = modes % 10
            if mode1 == 1:
                value = program[i+1]
            else:
                addr = program[i+1]
                value = program[addr]
            output = value
            i += 2
        else:
            modes = program[i] // 100
            mode1 = modes % 10
            mode2 = (modes // 10) % 10

            if mode1 == 1:
                p1 = program[i+1]
            else:
                p1 = program[program[i+1]]

            if opcode in [1,2,5,6,7,8]:
                if mode2 == 1:
                    p2 = program[i+2]
                else:
                    p2 = program[program[i+2]]

            if opcode == 1:
                addr3 = program[i+3]
                program[addr3] = p1 + p2
                i += 4
            elif opcode == 2:
                addr3 = program[i+3]
                program[addr3] = p1 * p2
                i += 4
            elif opcode == 5:
                if p1 != 0:
                    i = p2
                else:
                    i += 3
            elif opcode == 6:
                if p1 == 0:
                    i = p2
                else:
                    i += 3
            elif opcode == 7:
                addr3 = program[i+3]
                program[addr3] = 1 if p1 < p2 else 0
                i += 4
            elif opcode == 8:
                addr3 = program[i+3]
                program[addr3] = 1 if p1 == p2 else 0
                i += 4
            else:
                raise ValueError(f'opcode {opcode} from {program[i]}')

    return output

def part1(data):
    return solve(data, 1)

def part2(data):
    return solve(data, 5)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")