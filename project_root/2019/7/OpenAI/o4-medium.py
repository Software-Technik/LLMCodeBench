import sys, itertools
from collections import deque

class Computer:
    def __init__(self, program):
        self.mem = program.copy()
        self.ip = 0
        self.inputs = deque()
        self.halted = False
    def send(self, value):
        self.inputs.append(value)
    def run(self):
        mem, inp = self.mem, self.inputs
        ip = self.ip
        while True:
            instr = mem[ip]
            op = instr % 100
            if op == 99:
                self.halted = True
                self.ip = ip
                return None
            modes = instr // 100
            m1 = modes % 10
            m2 = modes // 10 % 10
            a = mem[ip+1] if m1 else mem[mem[ip+1]]
            if op in (1,2,5,6,7,8):
                b = mem[ip+2] if m2 else mem[mem[ip+2]]
            if op == 1:
                mem[mem[ip+3]] = a + b
                ip += 4
            elif op == 2:
                mem[mem[ip+3]] = a * b
                ip += 4
            elif op == 3:
                mem[mem[ip+1]] = inp.popleft()
                ip += 2
            elif op == 4:
                self.ip = ip + 2
                return a
            elif op == 5:
                ip = b if a else ip + 3
            elif op == 6:
                ip = b if not a else ip + 3
            elif op == 7:
                mem[mem[ip+3]] = 1 if a < b else 0
                ip += 4
            elif op == 8:
                mem[mem[ip+3]] = 1 if a == b else 0
                ip += 4
        self.ip = ip

def part1(prog):
    best = 0
    for perm in itertools.permutations(range(5)):
        signal = 0
        for phase in perm:
            c = Computer(prog)
            c.send(phase)
            c.send(signal)
            signal = c.run()
        if signal > best:
            best = signal
    return best

def part2(prog):
    best = 0
    for perm in itertools.permutations(range(5, 10)):
        comps = [Computer(prog) for _ in range(5)]
        for c, phase in zip(comps, perm):
            c.send(phase)
        signal = 0
        while True:
            halted = False
            for c in comps:
                c.send(signal)
                out = c.run()
                if out is None:
                    halted = True
                    break
                signal = out
            if halted:
                break
        if signal > best:
            best = signal
    return best

data = list(map(int, open(sys.argv[1]).readline().split(',')))
sys.stdout.write(f"{part1(data)} {part2(data)}")