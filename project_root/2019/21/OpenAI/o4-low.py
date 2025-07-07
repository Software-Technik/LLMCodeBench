import sys
from collections import defaultdict

def run_intcode(data, inputs):
    mem = defaultdict(int, enumerate(data))
    i = rel = 0
    inp = inputs
    while True:
        op = mem[i] % 100
        if op == 99: break
        m1 = mem[i]//100%10; m2 = mem[i]//1000%10; m3 = mem[i]//10000%10
        def adr(off, m):
            if m==0: return mem[i+off]
            if m==1: return i+off
            return mem[i+off]+rel
        if op==1:
            mem[adr(3,m3)] = mem[adr(1,m1)] + mem[adr(2,m2)]; i+=4
        elif op==2:
            mem[adr(3,m3)] = mem[adr(1,m1)] * mem[adr(2,m2)]; i+=4
        elif op==3:
            mem[adr(1,m1)] = inp.pop(); i+=2
        elif op==4:
            yield mem[adr(1,m1)]; i+=2
        elif op==5:
            i = mem[adr(2,m2)] if mem[adr(1,m1)] else i+3
        elif op==6:
            i = mem[adr(2,m2)] if not mem[adr(1,m1)] else i+3
        elif op==7:
            mem[adr(3,m3)] = int(mem[adr(1,m1)] < mem[adr(2,m2)]); i+=4
        elif op==8:
            mem[adr(3,m3)] = int(mem[adr(1,m1)] == mem[adr(2,m2)]); i+=4
        elif op==9:
            rel += mem[adr(1,m1)]; i+=2
        else:
            raise
    return

def feed_moves(moves):
    stk = []
    for line in moves:
        for c in line+"\n":
            stk.append(ord(c))
    return stk[::-1]

def run_part(data, moves, cmd):
    inputs = feed_moves(moves+[cmd])
    gen = run_intcode(data, inputs)
    out = []
    for v in gen:
        if v>512: return v
        out.append(v)
    return None

def part1(data):
    moves = ["NOT A J","NOT C T","AND D T","OR T J"]
    return run_part(data, moves, "WALK")

def part2(data):
    moves = [
        "NOT C T","OR T J",
        "NOT E T","NOT T T","OR H T","AND T J",
        "NOT A T","OR T J","AND D J",
        "NOT B T","NOT T T","OR E T","NOT T T","OR T J"
    ]
    return run_part(data, moves, "RUN")

data = list(map(int, open(sys.argv[1]).read().split(",",)))
print(part1(data), part2(data))