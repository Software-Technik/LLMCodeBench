import sys

def solve(data, input_val):
    program = data.copy()
    output = None
    i = 0

    while i < len(program):
        opcode = program[i] % 100
        modes = program[i] // 100
        mode1 = modes % 10
        mode2 = (modes // 10) % 10

        if opcode == 99:
            break

        param1 = program[i+1] if mode1 else program[program[i+1]]
        
        if opcode in {1, 2, 5, 6, 7, 8}:
            param2 = program[i+2] if mode2 else program[program[i+2]]

        if opcode == 1:
            program[program[i+3]] = param1 + param2
            i += 4
        elif opcode == 2:
            program[program[i+3]] = param1 * param2
            i += 4
        elif opcode == 3:
            program[program[i+1]] = input_val
            i += 2
        elif opcode == 4:
            output = param1
            i += 2
        elif opcode == 5:
            i = param2 if param1 else i + 3
        elif opcode == 6:
            i = param2 if not param1 else i + 3
        elif opcode == 7:
            program[program[i+3]] = int(param1 < param2)
            i += 4
        elif opcode == 8:
            program[program[i+3]] = int(param1 == param2)
            i += 4
        else:
            raise ValueError(f'Invalid opcode {opcode}')

    return output

def part1(data):
    return solve(data, 1)

def part2(data):
    return solve(data, 5)

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))

sys.stdout.write(f"{part1(data)} {part2(data)}")