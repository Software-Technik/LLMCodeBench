import sys
from collections import deque, defaultdict

def runComputer(data, inputqueue: deque, inputDefault=lambda: -1):
    program = defaultdict(int, enumerate(data))
    outputs = []
    i = 0
    relbase = 0

    while True:
        opcode = program[i] % 100
        if opcode == 99:
            break

        mode1, mode2, mode3 = (
            (program[i] // 100 % 10),
            (program[i] // 1000 % 10),
            (program[i] // 10000 % 10)
        )

        def get_param(mode, offset):
            if mode == 0:
                return program[program[i + offset]]
            elif mode == 1:
                return program[i + offset]
            elif mode == 2:
                return program[program[i + offset] + relbase]
            raise ValueError(f"Unknown mode: {mode}")

        def set_param(mode, offset, value):
            if mode == 0:
                program[program[i + offset]] = value
            elif mode == 2:
                program[program[i + offset] + relbase] = value
            else:
                raise ValueError("Immediate mode invalid for param 3")

        if opcode == 1:
            set_param(mode3, 3, get_param(mode1, 1) + get_param(mode2, 2))
            i += 4
        elif opcode == 2:
            set_param(mode3, 3, get_param(mode1, 1) * get_param(mode2, 2))
            i += 4
        elif opcode == 3:
            if inputqueue:
                set_param(mode1, 1, inputqueue.popleft())
            else:
                set_param(mode1, 1, inputDefault())
                yield "CONTINUE"
            i += 2
        elif opcode == 4:
            outputs.append(get_param(mode1, 1))
            if len(outputs) == 3:
                yield tuple(outputs)
                outputs.clear()
            i += 2
        elif opcode == 5:
            i = get_param(mode2, 2) if get_param(mode1, 1) != 0 else i + 3
        elif opcode == 6:
            i = get_param(mode2, 2) if get_param(mode1, 1) == 0 else i + 3
        elif opcode == 7:
            set_param(mode3, 3, 1 if get_param(mode1, 1) < get_param(mode2, 2) else 0)
            i += 4
        elif opcode == 8:
            set_param(mode3, 3, 1 if get_param(mode1, 1) == get_param(mode2, 2) else 0)
            i += 4
        elif opcode == 9:
            relbase += get_param(mode1, 1)
            i += 2
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

def part1(data):
    inputs = []
    computers = []
    for i in range(50):
        q = deque()
        inputs.append(q)
        computers.append(runComputer(data, q))
        q.append(i)

    while True:
        for i in range(50):
            packet = next(computers[i])
            if packet == "CONTINUE":
                continue
            addr, x, y = packet

            if addr == 255:
                return y

            inputs[addr].extend([x, y])

def part2(data):
    inputs = []
    computers = []
    for i in range(50):
        q = deque()
        inputs.append(q)
        computers.append(runComputer(data, q))
        q.append(i)

    idlecount = 0
    natmemory = (None, None)
    lasty = None
    natready = False

    while True:
        if idlecount == 50 and natready:
            if lasty == natmemory[1]:
                return lasty
            inputs[0].extend(natmemory)
            lasty = natmemory[1]
            natready = False

        idlecount = 0

        for i in range(50):
            packet = next(computers[i])
            if packet == "CONTINUE":
                idlecount += 1
                continue
            addr, x, y = packet

            if addr == 255:
                natmemory = (x, y)
                natready = True
            else:
                inputs[addr].extend([x, y])

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().strip().split(',')))

sys.stdout.write(f"{part1(data)} {part2(data)}")