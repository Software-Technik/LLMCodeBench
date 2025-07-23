import sys
import os
from collections import defaultdict, deque

def runComputer(data, input):
    program = defaultdict(int, { k: v for k, v in enumerate(data) })
    output = None
    i = 0
    relbase = 0

    while True:
        opcode = program[i] % 100

        if opcode == 99:
            break

        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10
        mode3 = (program[i] // 10000) % 10

        p1, p2, p3 = None, None, None

        if mode1 == 0: p1 = program[i + 1]
        elif mode1 == 1: p1 = i + 1
        elif mode1 == 2: p1 = program[i + 1] + relbase

        if mode2 == 0: p2 = program[i + 2]
        elif mode2 == 1: p2 = i + 2
        elif mode2 == 2: p2 = program[i + 2] + relbase
  
        if mode3 == 0: p3 = program[i + 3]
        elif mode3 == 2: p3 = program[i + 3] + relbase

        if opcode == 1:
            program[p3] = program[p1] + program[p2]
            i += 4
        elif opcode == 2:
            program[p3] = program[p1] * program[p2]
            i += 4
        elif opcode == 3:
            if not input:
                yield None
            program[p1] = input.pop(0)
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

N, S, W, E = 1, 2, 3, 4
WALL, OK, GOAL = 0, 1, 2
opposites = { N: S, S: N, E: W, W: E }

dxs = { N: 0, S: 0, W: -1, E: 1 }
dys = { N: -1, S: 1, W: 0, E: 0 }

def explore_maze(data, stop_at_goal):
    inputs = []
    runner = runComputer(data, inputs)
    x, y = 0, 0
    walls = set()
    space = set([(0,0)])
    stack = []
    goal = None

    while True:
        if stop_at_goal and goal is not None:
            break

        moved = False
        for move_try in [N, S, E, W]:
            nx, ny = x + dxs[move_try], y + dys[move_try]
            if (nx, ny) in walls or (nx, ny) in space:
                continue
            inputs.append(move_try)
            status = next(runner, None)
            if status is None:
                break

            if status == WALL:
                walls.add((nx, ny))
            else:
                x, y = nx, ny
                space.add((x, y))
                if status == GOAL:
                    goal = (x, y)
                stack.append(move_try)
                moved = True
                break

        else:
            if not stack:
                break
            last_move = stack.pop()
            backtrack_move = opposites[last_move]
            inputs.append(backtrack_move)
            status = next(runner, None)
            if status is None:
                break
            x += dxs[backtrack_move]
            y += dys[backtrack_move]
            moved = True

        if stop_at_goal and goal is not None:
            break

    return walls, space, goal

def part1(data):
    walls, space, goal = explore_maze(data, stop_at_goal=True)
    if goal is None:
        return 0
    dist = {}
    queue = deque()
    dist[(0,0)] = 0
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        if (x,y) == goal:
            break
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if (nx,ny) in space and (nx,ny) not in dist:
                dist[(nx,ny)] = dist[(x,y)] + 1
                queue.append((nx,ny))
    return dist[goal]

def part2(data):
    walls, space, goal = explore_maze(data, stop_at_goal=False)
    if goal is None:
        return 0
    dist = {}
    queue = deque()
    dist[goal] = 0
    queue.append(goal)
    while queue:
        x, y = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if (nx,ny) in space and (nx,ny) not in dist:
                dist[(nx,ny)] = dist[(x,y)] + 1
                queue.append((nx,ny))
    return max(dist.values()) if dist else 0

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",")))
sys.stdout.write(f"{part1(data)} {part2(data)}")