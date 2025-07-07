import sys
import itertools

def run_amp(data, phase, inp):
    prog = data[:]
    i = 0
    first = True
    out = None
    while True:
        op = prog[i]
        opcode = op % 100
        if opcode == 99:
            break
        m1 = op // 100 % 10
        m2 = op // 1000 % 10
        if opcode in (1,2,5,6,7,8):
            a = prog[i+1] if m1 else prog[prog[i+1]]
            b = prog[i+2] if m2 else prog[prog[i+2]]
        if opcode == 1:
            prog[prog[i+3]] = a + b; i +=4
        elif opcode == 2:
            prog[prog[i+3]] = a * b; i +=4
        elif opcode == 3:
            prog[prog[i+1]] = phase if first else inp
            first = False
            i +=2
        elif opcode == 4:
            out = prog[i+1] if m1 else prog[prog[i+1]]
            i +=2
        elif opcode == 5:
            i = b if a else i+3
        elif opcode == 6:
            i = b if not a else i+3
        elif opcode == 7:
            prog[prog[i+3]] = 1 if a<b else 0; i +=4
        elif opcode == 8:
            prog[prog[i+3]] = 1 if a==b else 0; i +=4
        else:
            break
    return out

def part1(data):
    best = 0
    for seq in itertools.permutations(range(5)):
        val = 0
        for p in seq:
            val = run_amp(data, p, val)
        if val>best: best=val
    return best

def run_feedback(data, phase, i, inp, used):
    prog = data
    while True:
        op = prog[i]
        opcode = op % 100
        if opcode == 99:
            return None, i, True
        m1 = op // 100 % 10
        m2 = op // 1000 % 10
        if opcode in (1,2,5,6,7,8):
            a = prog[i+1] if m1 else prog[prog[i+1]]
            b = prog[i+2] if m2 else prog[prog[i+2]]
        if opcode == 1:
            prog[prog[i+3]] = a + b; i +=4
        elif opcode == 2:
            prog[prog[i+3]] = a * b; i +=4
        elif opcode == 3:
            prog[prog[i+1]] = phase if not used else inp
            used = True
            i +=2
        elif opcode == 4:
            out = prog[i+1] if m1 else prog[prog[i+1]]
            return out, i+2, used
        elif opcode == 5:
            i = b if a else i+3
        elif opcode == 6:
            i = b if not a else i+3
        elif opcode == 7:
            prog[prog[i+3]] = 1 if a<b else 0; i +=4
        elif opcode == 8:
            prog[prog[i+3]] = 1 if a==b else 0; i +=4

def part2(data):
    best = 0
    for seq in itertools.permutations(range(5,10)):
        comps = [{'prog':data[:],'i':0,'used':False,'phase':p} for p in seq]
        val = 0
        halted = False
        while not halted:
            for c in comps:
                out, ni, used = run_feedback(c['prog'], c['phase'], c['i'], val, c['used'])
                if out is None:
                    halted = True
                    break
                val = out
                c['i'], c['used'] = ni, used
        if val>best: best=val
    return best

data = list(map(int, open(sys.argv[1]).read().splitlines()[0].split(',')))
print(part1(data), part2(data))