import sys,itertools

class Computer:
    def __init__(self, mem, phase):
        self.mem = mem[:]
        self.ip = 0
        self.phase = phase
        self.phase_used = False
        self.halted = False
    def run(self, input_signal):
        mem = self.mem
        ip = self.ip
        while True:
            inst = mem[ip]
            opcode = inst % 100
            modes = inst // 100
            if opcode == 1:
                a = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                b = mem[ip+2] if modes//10%10 else mem[mem[ip+2]]
                mem[mem[ip+3]] = a + b
                ip += 4
            elif opcode == 2:
                a = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                b = mem[ip+2] if modes//10%10 else mem[mem[ip+2]]
                mem[mem[ip+3]] = a * b
                ip += 4
            elif opcode == 3:
                dest = mem[ip+1]
                if not self.phase_used:
                    mem[dest] = self.phase
                    self.phase_used = True
                else:
                    mem[dest] = input_signal
                ip += 2
            elif opcode == 4:
                output = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                ip += 2
                self.ip = ip
                return output
            elif opcode == 5:
                cond = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                if cond:
                    ip = mem[ip+2] if modes//10%10 else mem[mem[ip+2]]
                else:
                    ip += 3
            elif opcode == 6:
                cond = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                if not cond:
                    ip = mem[ip+2] if modes//10%10 else mem[mem[ip+2]]
                else:
                    ip += 3
            elif opcode == 7:
                a = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                b = mem[ip+2] if modes//10%10 else mem[mem[ip+2]]
                mem[mem[ip+3]] = 1 if a < b else 0
                ip += 4
            elif opcode == 8:
                a = mem[ip+1] if modes%10 else mem[mem[ip+1]]
                b = mem[ip+2] if modes//10%10 else mem[mem[ip+2]]
                mem[mem[ip+3]] = 1 if a == b else 0
                ip += 4
            elif opcode == 99:
                self.halted = True
                self.ip = ip
                return None
            else:
                raise
        # unreachable

def part1(data):
    max_signal = 0
    for seq in itertools.permutations(range(5)):
        signal = 0
        for phase in seq:
            signal = Computer(data, phase).run(signal)
        if signal > max_signal:
            max_signal = signal
    return max_signal

def part2(data):
    max_signal = 0
    for seq in itertools.permutations(range(5,10)):
        comps = [Computer(data, phase) for phase in seq]
        signal = 0
        idx = 0
        while not comps[4].halted:
            comp = comps[idx]
            if not comp.halted:
                out = comp.run(signal)
                if out is not None:
                    signal = out
            idx = (idx + 1) % 5
        if signal > max_signal:
            max_signal = signal
    return max_signal

data = list(map(int, open(sys.argv[1]).read().strip().split(',')))
sys.stdout.write(f"{part1(data)} {part2(data)}")