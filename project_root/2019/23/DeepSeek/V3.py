import sys
from collections import deque, defaultdict

def runComputer(data, inputqueue, inputDefault=lambda: -1):
    program = defaultdict(int, enumerate(data))
    i = relbase = 0

    while True:
        opcode = program[i] % 100
        if opcode == 99: break

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
            i = program[p2] if program[p1] else i + 3
        elif opcode == 6:
            i = program[p2] if not program[p1] else i + 3
        elif opcode == 7:
            program[p3] = int(program[p1] < program[p2])
            i += 4
        elif opcode == 8:
            program[p3] = int(program[p1] == program[p2])
            i += 4
        elif opcode == 9:
            relbase += program[p1]
            i += 2
        else:
            raise ValueError(f'Invalid opcode {opcode}')

def part1(data):
    inputs = [deque([i]) for i in range(50)]
    computers = [runComputer(data, q) for q in inputs]

    while True:
        for i in range(50):
            addr = next(computers[i])
            if addr == "CONTINUE": continue
            x, y = next(computers[i]), next(computers[i])
            if addr == 255: return y
            inputs[addr].extend([x, y])

def part2(data):
    inputs = [deque([i]) for i in range(50)]
    computers = [runComputer(data, q) for q in inputs]
    natmemory = lasty = None
    idlecount = 0

    while True:
        if idlecount >= 50 and natmemory is not None:
            x, y = natmemory
            if y == lasty: return y
            inputs[0].extend([x, y])
            lasty = y
            idlecount = 0

        idle = True
        for i in range(50):
            try:
                addr = next(computers[i])
                if addr == "CONTINUE": continue
                x, y = next(computers[i]), next(computers[i])
                if addr == 255:
                    natmemory = (x, y)
                else:
                    inputs[addr].extend([x, y])
                idle = False
            except StopIteration:
                pass

        idlecount = idlecount + 1 if idle else 0

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))

sys.stdout.write(f"{part1(data)} {part2(data)}")