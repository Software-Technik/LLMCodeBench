import sys

def run(data, inputs):
    mem = data[:] + [0]*10000
    ip = rb = 0
    while True:
        instr = mem[ip]; op = instr % 100
        if op == 99: return
        m1 = instr//100%10; m2 = instr//1000%10; m3 = instr//10000%10
        def A(off, m):
            if m == 0: return mem[ip+off]
            if m == 1: return ip+off
            return mem[ip+off] + rb
        if op == 1:
            a, b, c = A(1,m1), A(2,m2), A(3,m3)
            mem[c] = mem[a] + mem[b]; ip += 4
        elif op == 2:
            a, b, c = A(1,m1), A(2,m2), A(3,m3)
            mem[c] = mem[a] * mem[b]; ip += 4
        elif op == 3:
            a = A(1,m1)
            mem[a] = inputs.pop(); ip += 2
        elif op == 4:
            yield mem[A(1,m1)]; ip += 2
        elif op == 5:
            a, b = A(1,m1), A(2,m2)
            ip = mem[b] if mem[a] != 0 else ip + 3
        elif op == 6:
            a, b = A(1,m1), A(2,m2)
            ip = mem[b] if mem[a] == 0 else ip + 3
        elif op == 7:
            a, b, c = A(1,m1), A(2,m2), A(3,m3)
            mem[c] = 1 if mem[a] < mem[b] else 0; ip += 4
        elif op == 8:
            a, b, c = A(1,m1), A(2,m2), A(3,m3)
            mem[c] = 1 if mem[a] == mem[b] else 0; ip += 4
        elif op == 9:
            rb += mem[A(1,m1)]; ip += 2

def run_part(data, moves):
    inputs = [ord(c) for line in moves for c in line+"\n"][::-1]
    for out in run(data, inputs):
        if out > 512:
            return out

def main():
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().splitlines()[0].split(",")))
    part1_moves = ["NOT A J", "NOT C T", "AND D T", "OR T J", "WALK"]
    part2_moves = ["NOT C T", "OR T J", "NOT E T", "NOT T T", "OR H T", "AND T J", "NOT A T", "OR T J", "AND D J", "NOT B T", "NOT T T", "OR E T", "NOT T T", "OR T J", "RUN"]
    r1 = run_part(data, part1_moves)
    r2 = run_part(data, part2_moves)
    sys.stdout.write(f"{r1} {r2}")

if __name__ == "__main__":
    main()