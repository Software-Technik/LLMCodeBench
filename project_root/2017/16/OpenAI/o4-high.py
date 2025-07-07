import sys

def dance(s, inst):
    arr = list(s)
    for instr in inst:
        if instr[0] == 's':
            x = instr[1]; arr = arr[-x:] + arr[:-x]
        elif instr[0] == 'x':
            a, b = instr[1], instr[2]; arr[a], arr[b] = arr[b], arr[a]
        else:
            a, b = instr[1], instr[2]; i = arr.index(a); j = arr.index(b); arr[i], arr[j] = arr[j], arr[i]
    return ''.join(arr)

def long_dance(s, inst, iters):
    states = [s]
    seen = {s: 0}
    for i in range(1, iters + 1):
        s = dance(states[-1], inst)
        if s in seen:
            start = seen[s]; length = i - start
            idx = (iters - start) % length + start
            return states[idx]
        seen[s] = i; states.append(s)
    return s

with open(sys.argv[1]) as f:
    insts = f.read().strip().split(',')
instructions = []
for inst in insts:
    c = inst[0]
    if c == 's':
        instructions.append(('s', int(inst[1:])))
    elif c == 'x':
        a, b = inst[1:].split('/'); instructions.append(('x', int(a), int(b)))
    else:
        a, b = inst[1:].split('/'); instructions.append(('p', a, b))
programs = "abcdefghijklmnop"
print(dance(programs, instructions))
print(long_dance(programs, instructions, 1000000000))