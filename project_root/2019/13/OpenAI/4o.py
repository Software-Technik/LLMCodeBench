from collections import defaultdict
import sys

def run_computer(data, input_vals):
    program = defaultdict(int, {k: v for k, v in enumerate(data)})
    i, relbase = 0, 0

    def get_param(mode, offset):
        if mode == 0:
            return program[i + offset]
        elif mode == 1:
            return i + offset
        elif mode == 2:
            return program[i + offset] + relbase

    while True:
        opcode = program[i] % 100
        if opcode == 99:
            break

        mode1, mode2, mode3 = (program[i] // 100 % 10), (program[i] // 1000 % 10), (program[i] // 10000 % 10)
        p1, p2, p3 = get_param(mode1, 1), get_param(mode2, 2), get_param(mode3, 3)

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
            i += 4
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]
            i += 4
        elif opcode == 3:
            program[p1] = input_vals.pop()
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
            raise ValueError(f'Unexpected opcode {opcode}')

def part1(data):
    runner = run_computer(data, [])
    level, blocks = defaultdict(int), 0

    while True:
        x, y, tile = next(runner, 'halt'), next(runner, 'halt'), next(runner, 'halt')
        if x == 'halt':
            break
        if tile == 2:
            blocks += 1
        level[(x, y)] = tile

    return blocks

def part2(data):
    data[0] = 2
    inputs, level = [0], defaultdict(int)
    runner = run_computer(data, inputs)
    score, bx, px = 0, 0, 0

    while True:
        x, y, tile = next(runner, 'halt'), next(runner, 'halt'), next(runner, 'halt')
        if x == 'halt':
            break
        if x == -1:
            score = tile
            continue
        level[(x, y)] = tile
        if tile == 3:
            px = x
        if tile == 4:
            bx = x
        inputs.clear()
        inputs.append((bx > px) - (bx < px)) 

    return score

if __name__ == '__main__':
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = list(map(int, f.read().strip().split(",")))

    print(f"{part1(data)} {part2(data)}")