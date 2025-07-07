import sys
import os
import readchar
from collections import defaultdict

clear = lambda: os.system('cls')

def runComputer(data, input):
    program = defaultdict(int, {i: v for i, v in enumerate(data)})
    i = 0
    relbase = 0

    while True:
        opcode = program[i] % 100
        if opcode == 99:
            break

        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10
        mode3 = (program[i] // 10000) % 10

        def get_param(mode, index):
            if mode == 0:
                return program[program[index]]
            elif mode == 1:
                return program[index]
            elif mode == 2:
                return program[program[index] + relbase]

        def set_param(mode, index, value):
            if mode == 0:
                program[program[index]] = value
            elif mode == 2:
                program[program[index] + relbase] = value

        if opcode in (1, 2, 7, 8):
            p1 = get_param(mode1, i + 1)
            p2 = get_param(mode2, i + 2)
            if opcode == 1:
                set_param(mode3, i + 3, p1 + p2)
            elif opcode == 2:
                set_param(mode3, i + 3, p1 * p2)
            elif opcode == 7:
                set_param(mode3, i + 3, int(p1 < p2))
            elif opcode == 8:
                set_param(mode3, i + 3, int(p1 == p2))
            i += 4
        elif opcode == 3:
            set_param(mode1, i + 1, input.pop())
            i += 2
        elif opcode == 4:
            yield get_param(mode1, i + 1)
            i += 2
        elif opcode in (5, 6):
            p1 = get_param(mode1, i + 1)
            p2 = get_param(mode2, i + 2)
            if (opcode == 5 and p1 != 0) or (opcode == 6 and p1 == 0):
                i = p2
            else:
                i += 3
        elif opcode == 9:
            relbase += get_param(mode1, i + 1)
            i += 2

N, S, W, E, QUIT, AUTO = 1, 2, 3, 4, -1, -2
WALL, OK, GOAL = 0, 1, 2
opposites = {N: S, S: N, E: W, W: E}
dxs, dys = {N: 0, S: 0, W: -1, E: 1}, {N: -1, S: 1, W: 0, E: 0}
controls = {'j': W, 'i': N, 'l': E, 'k': S, 'q': QUIT, 'a': AUTO}

def part1(data):
    inputs = []
    runner = runComputer(data, inputs)
    x, y = 0, 0
    walls = set()
    space = {(0, 0)}
    stack = []
    goal = None

    while True:
        moved = False
        for move_try in [N, S, E, W]:
            nx_, ny_ = x + dxs[move_try], y + dys[move_try]
            if (nx_, ny_) not in walls and (nx_, ny_) not in space:
                move = move_try
                stack.append(move)
                moved = True
                break
        if not moved:
            if not stack:
                continue
            last_move = stack.pop()
            move = opposites[last_move]

        inputs.append(move)
        status = next(runner, 'halt')
        if status == 'halt':
            break

        x += dxs[move]
        y += dys[move]

        if status == WALL:
            walls.add((x, y))
            x -= dxs[move]
            y -= dys[move]
            if stack and move == stack[-1]:
                stack.pop()
        elif status == OK:
            space.add((x, y))
        elif status == GOAL:
            space.add((x, y))
            goal = (x, y)
            break

    from collections import deque
    q = deque([((0, 0), 0)])
    visited = {(0, 0)}
    while q:
        (cx, cy), length = q.popleft()
        if (cx, cy) == goal:
            return length
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in space and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), length + 1))

def part2(data):
    inputs = []
    runner = runComputer(data, inputs)
    x, y = 0, 0
    goal = None
    walls = set()
    space = {(0, 0)}
    exhausted = {(0, 0)}
    visited = {(0, 0)}

    while True:
        visited.add((x, y))
        for m in [N, E, S, W]:
            inputs.append(m)
            status = next(runner, 'halt')

            x += dxs[m]
            y += dys[m]

            if status == WALL:
                walls.add((x, y))
                exhausted.add((x, y))
                x -= dxs[m]
                y -= dys[m]
            elif status == OK:
                space.add((x, y))
                m = opposites[m]
                x += dxs[m]
                y += dys[m]
                inputs.append(m)
                next(runner, 'halt')
            elif status == GOAL:
                goal = (x, y)
                m = opposites[m]
                x += dxs[m]
                y += dys[m]
                inputs.append(m)
                next(runner, 'halt')

        opts = {N: (x, y - 1), E: (x + 1, y), S: (x, y + 1), W: (x - 1, y)}
        candidates = [c for c, (nx, ny) in opts.items() if (nx, ny) not in exhausted]

        if len(candidates) == 1:
            exhausted.add((x, y))

        if not candidates:
            break
        else:
            move = candidates[1 if opts[candidates[0]] in visited and len(candidates) > 1 else 0]

        inputs.append(move)
        status = next(runner, 'halt')
        if status == 'halt': break

        x += dxs[move]
        y += dys[move]
        
        if status == WALL:
            walls.add((x, y))
            x -= dxs[move]
            y -= dys[move]
        elif status == OK:
            space.add((x, y))
        elif status == GOAL:
            break

    from collections import deque
    q = deque([(goal, 0)])
    visited = {goal}
    max_length = 0
    while q:
        (cx, cy), length = q.popleft()
        max_length = max(max_length, length)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in space and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append(((nx, ny), length + 1))

    return max_length

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().strip().split(',')))
sys.stdout.reconfigure(encoding='utf-8')
sys.stdout.write(f"{part1(data)} {part2(data)}")