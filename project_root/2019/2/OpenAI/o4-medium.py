import sys
with open(sys.argv[1]) as f:
    orig = list(map(int, f.read().split(',')))
def run(noun, verb, mem=orig):
    prog = mem.copy()
    prog[1] = noun; prog[2] = verb
    i = 0
    while True:
        op = prog[i]
        if op == 1:
            a, b, c = prog[i+1], prog[i+2], prog[i+3]
            prog[c] = prog[a] + prog[b]
        elif op == 2:
            a, b, c = prog[i+1], prog[i+2], prog[i+3]
            prog[c] = prog[a] * prog[b]
        else:
            return prog[0]
        i += 4
p1 = run(12, 2)
t = 19690720
p2 = next(100*n + v for n in range(100) for v in range(100) if run(n, v) == t)
sys.stdout.write(f"{p1} {p2}")