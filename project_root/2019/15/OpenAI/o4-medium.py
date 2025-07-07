import sys
from collections import defaultdict, deque

def runComputer(data, inputs):
    program = defaultdict(int)
    for i,v in enumerate(data):
        program[i]=v
    i=0
    rel=0
    while True:
        opcode = program[i] % 100
        if opcode == 99:
            return
        mode1 = (program[i] // 100) % 10
        mode2 = (program[i] // 1000) % 10
        mode3 = (program[i] // 10000) % 10
        def get(p, m):
            if m == 0: return program[program[p]]
            if m == 1: return program[p]
            return program[program[p] + rel]
        def setp(p, m, v):
            if m == 0: program[program[p]] = v
            else: program[program[p] + rel] = v
        if opcode == 1:
            setp(i+3, mode3, get(i+1,mode1) + get(i+2,mode2))
            i += 4
        elif opcode == 2:
            setp(i+3, mode3, get(i+1,mode1) * get(i+2,mode2))
            i += 4
        elif opcode == 3:
            setp(i+1, mode1, inputs.pop())
            i += 2
        elif opcode == 4:
            yield get(i+1,mode1)
            i += 2
        elif opcode == 5:
            if get(i+1,mode1) != 0: i = get(i+2,mode2)
            else: i += 3
        elif opcode == 6:
            if get(i+1,mode1) == 0: i = get(i+2,mode2)
            else: i += 3
        elif opcode == 7:
            setp(i+3, mode3, 1 if get(i+1,mode1) < get(i+2,mode2) else 0)
            i += 4
        elif opcode == 8:
            setp(i+3, mode3, 1 if get(i+1,mode1) == get(i+2,mode2) else 0)
            i += 4
        elif opcode == 9:
            rel += get(i+1,mode1)
            i += 2
        else:
            raise Exception(opcode)

N,S,W,E=1,2,3,4
dx={N:0,S:0,W:-1,E:1}
dy={N:-1,S:1,W:0,E:0}
opp={N:S,S:N,W:E,E:W}

def explore(data):
    inputs=[]
    gen=runComputer(data, inputs)
    x=y=0
    walls=set()
    space={(0,0)}
    visited={(0,0)}
    goal=None
    stack=[]
    while True:
        for d in (N,S,W,E):
            nx,ny = x+dx[d], y+dy[d]
            if (nx,ny) in visited or (nx,ny) in walls: continue
            inputs.append(d)
            status = next(gen)
            if status == 0:
                walls.add((nx,ny))
            else:
                x,y=nx,ny
                visited.add((x,y))
                space.add((x,y))
                if status == 2: goal=(x,y)
                stack.append(opp[d])
            break
        else:
            if not stack: break
            bd = stack.pop()
            inputs.append(bd)
            next(gen)
            x+=dx[bd]; y+=dy[bd]
    return space, walls, goal

def bfs(start, goal, space):
    dq=deque([(start,0)])
    seen={start}
    while dq:
        (x,y),d = dq.popleft()
        if (x,y)==goal: return d
        for dx_,dy_ in ((0,1),(0,-1),(1,0),(-1,0)):
            np = (x+dx_, y+dy_)
            if np in space and np not in seen:
                seen.add(np)
                dq.append((np,d+1))

def maxdist(goal, space):
    dq=deque([(goal,0)])
    seen={goal}
    md=0
    while dq:
        (x,y),d = dq.popleft()
        if d>md: md=d
        for dx_,dy_ in ((0,1),(0,-1),(1,0),(-1,0)):
            np = (x+dx_, y+dy_)
            if np in space and np not in seen:
                seen.add(np)
                dq.append((np,d+1))
    return md

data = list(map(int, open(sys.argv[1]).read().strip().split(',')))
space, walls, goal = explore(data)
p1 = bfs((0,0), goal, space)
p2 = maxdist(goal, space)
print(p1, p2)