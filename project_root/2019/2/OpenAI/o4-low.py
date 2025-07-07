import sys

def run(data, noun, verb):
    prog = data[:]
    prog[1], prog[2] = noun, verb
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

f = open(sys.argv[1])
data = list(map(int, f.read().split(',', maxsplit=-1)))
p1 = run(data, 12, 2)
target = 19690720
res2 = next(100*n+v for n in range(100) for v in range(100) if run(data, n, v) == target)
sys.stdout.write(f"{p1} {res2}")