import sys
from collections import deque, defaultdict

def runComputer(data, inputqueue, inputDefault=lambda: -1):
    program = defaultdict(int, enumerate(data))
    i = 0
    relbase = 0

    while True:
        full = program[i]
        opcode = full % 100
        if opcode == 99:
            break

        mode1 = (full // 100) % 10
        mode2 = (full // 1000) % 10
        mode3 = (full // 10000) % 10

        if mode1 == 0:
            p1 = program[i+1]
        elif mode1 == 1:
            p1 = i+1
        else:
            p1 = program[i+1] + relbase

        if mode2 == 0:
            p2 = program[i+2]
        elif mode2 == 1:
            p2 = i+2
        else:
            p2 = program[i+2] + relbase

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
            if inputqueue:
                program[p1] = inputqueue.popleft()
                i += 2
            else:
                program[p1] = inputDefault()
                i += 2
                yield "CONTINUE"
        elif opcode == 4:
            yield program[p1]
            i += 2
        elif opcode == 5:
            i = program[p2] if program[p1] else i+3
        elif opcode == 6:
            i = program[p2] if not program[p1] else i+3
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
            raise ValueError(f'opcode {opcode} from {full}')

def part1(data):
    inputs = [deque([i]) for i in range(50)]
    computers = [runComputer(data, q) for q in inputs]

    while True:
        for i in range(50):
            addr = next(computers[i])
            if addr == "CONTINUE":
                continue
            x = next(computers[i])
            y = next(computers[i])
            if addr == 255:
                return y
            inputs[addr].append(x)
            inputs[addr].append(y)

def part2(data):
    inputs = [deque([i]) for i in range(50)]
    computers = [runComputer(data, q) for q in inputs]
    natready = False
    natmemory = (0, 0)
    lasty = None
    idle = [False] * 50

    while True:
        all_idle = True
        for i in range(50):
            if inputs[i]:
                all_idle = False
                break
        if all_idle and natready:
            if lasty == natmemory[1]:
                return lasty
            inputs[0].extend(natmemory)
            lasty = natmemory[1]
            natready = False

        for i in range(50):
            try:
                addr = next(computers[i])
                if addr == "CONTINUE":
                    continue
                x = next(computers[i])
                y = next(computers[i])
                if addr == 255:
                    natmemory = (x, y)
                    natready = True
                else:
                    inputs[addr].append(x)
                    inputs[addr].append(y)
            except StopIteration:
                pass

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")