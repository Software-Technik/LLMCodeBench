import sys
import os
import readchar
import networkx as nx
from collections import defaultdict

clear = lambda: os.system('cls')

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

N, S, W, E, QUIT, AUTO = 1, 2, 3, 4, -1, -2
WALL, OK, GOAL = 0, 1, 2
opposites = { N: S, S: N, E: W, W: E }

dxs = { N: 0, S: 0, W: -1, E: 1 }
dys = { N: -1, S: 1, W: 0, E: 0 }

controls = { 'j': W, 'i': N, 'l': E, 'k': S, 'q': QUIT, 'a': AUTO }

def draw(walls, space, pos):
    clear()
    for y in range(-40, 40):
        line = ""
        for x in range(-40, 40):
            if (x,y) == (0,0): line += 'S'
            elif (x,y) in walls: line += '█'
            elif (x,y) == pos: line += 'D'
            elif (x,y) in space: line += '·'
            else: line += '░'
    pass

def readmove():
    move = QUIT
    while move < 0:
        i = readchar.readchar()
        if i in controls:
            move = controls[i]
            break
    return move

def part1(data):
    inputs = []
    runner = runComputer(data, inputs)
    x, y = 0, 0
    walls = set()
    space = set([(0,0)])
    mode = 0
    stack = []
    goal = None

    while True:
        if mode == 1:
            draw(walls, space, (x, y))
            move = readmove()
        else:
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
                    mode = 1
                    continue
                last_move = stack.pop()
                move = opposites[last_move]

        if move == QUIT:
            break
        if move == AUTO:
            mode = 0
            continue

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
            if mode == 0 and stack and move == stack[-1]:
                stack.pop()
        elif status == OK:
            space.add((x, y))
        elif status == GOAL:
            space.add((x, y))
            goal = (x, y)
            break

    graph = nx.Graph()
    for (px, py) in space:
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (px + dx, py + dy)
            if neighbor in space:
                graph.add_edge((px, py), neighbor)

    path_len = nx.shortest_path_length(graph, (0, 0), goal)
    return path_len

def part2(data):
    inputs = []
    runner = runComputer(data, inputs)
    x, y = 0, 0
    goal = None
    walls = set()
    space = set([(0,0)])
    exhausted = set([(0,0)])
    visited = set([(0,0)])
    ends = set()
    mode = 0

    while True:
        visited.add((x,y))

        for m in [N,E,S,W]:
            inputs.append(m)
            status = next(runner, 'halt')

            x += dxs[m]
            y += dys[m]

            if status == WALL:
                walls.add((x, y))
                exhausted.add((x,y))
                x -= dxs[m]
                y -= dys[m]
            elif status == OK:
                space.add((x,y))
                m = opposites[m]
                x += dxs[m]
                y += dys[m]
                inputs.append(m)
                _ = next(runner, 'halt')
            elif status == GOAL:
                goal = (x,y)
                m = opposites[m]
                x += dxs[m]
                y += dys[m]
                inputs.append(m)
                _ = next(runner, 'halt')

        if mode == 0:
            opts = {
                N: (x, y - 1),
                E: (x + 1, y),
                S: (x, y + 1),
                W: (x - 1, y),
            }

            candidates = [c for c in opts if opts[c] not in exhausted]

            if len(candidates) == 1:
                exhausted.add((x,y))

            if len(candidates) == 0:
                mode = 1
            else:
                if opts[candidates[0]] in visited and len(candidates) > 1:
                    move = candidates[1]
                else:
                    move = candidates[0]

        if mode == 1:
            break

        if move == QUIT:
            break
        if move == AUTO:
            mode = 0
            continue

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
            space.add((x,y))
        elif status == GOAL:
            goal = (x,y)

        counter = 0
        for m in [N,E,S,W]:
            tx = x + dxs[m]
            ty = y + dys[m]
            if (tx,ty) in exhausted: counter += 1
        if counter >= 3:
            ends.add((x,y))
            exhausted.add((x,y))

    graph = nx.Graph()
    points = space | {goal}
    for p in points:
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (p[0] + dx, p[1] + dy)
            if neighbor in points:
                graph.add_edge(p, neighbor)
    
    lengths = nx.single_source_shortest_path_length(graph, goal)

    return max(lengths.values())


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = list(map(int, f.read().splitlines()[0].split(",")))
sys.stdout.reconfigure(encoding='utf-8')
sys.stdout.write(f"{part1(data)} {part2(data)}")