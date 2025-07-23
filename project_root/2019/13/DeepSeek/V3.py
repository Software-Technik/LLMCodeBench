import sys
from collections import defaultdict

def runComputer(data, input):
    program = defaultdict(int, { k: v for k, v in enumerate(data) })
    i = 0
    relbase = 0

    while True:
        opcode = program[i] % 100
        if opcode == 99:
            break

        modes = program[i] // 100
        mode1 = modes % 10
        mode2 = (modes // 10) % 10
        mode3 = (modes // 100) % 10

        p1 = program[i + 1] + (relbase if mode1 == 2 else 0) if mode1 != 1 else i + 1
        p2 = program[i + 2] + (relbase if mode2 == 2 else 0) if mode2 != 1 else i + 2
        p3 = program[i + 3] + (relbase if mode3 == 2 else 0) if mode3 != 1 else i + 3

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
            raise ValueError(f'opcode {opcode} from {program[i]}')

def part1(data):
    runner = runComputer(data.copy(), [])
    blocks = 0
    while True:
        x = next(runner, 'halt')
        if x == 'halt': break
        y = next(runner, 'halt')
        tile = next(runner, 'halt')
        if tile == 2:
            blocks += 1
    return blocks

def part2(data):
    data = data.copy()
    data[0] = 2
    runner = runComputer(data, [0])
    score = -1
    px, py = 0, 0
    bx, by = 0, 0
    inputs = []
    
    while True:
        x = next(runner, 'halt')
        if x == 'halt': break
        y = next(runner, 'halt')
        tile = next(runner, 'halt')
        
        if x == -1:
            score = tile
            continue
        
        if tile == 3:
            px, py = x, y
        elif tile == 4:
            bx, by = x, y
        
        inputs.clear()
        if px < bx:
            inputs.append(1 if by < py + 1 else -1)
        elif px > bx:
            inputs.append(-1 if by < py + 1 else 1)
        else:
            inputs.append(0)
    
    return score

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")