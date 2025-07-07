import sys
from array import array

def step_by_step(instr, second_part):
    i = steps = 0
    n = len(instr)
    while 0 <= i < n:
        jump = instr[i]
        instr[i] += -1 if second_part and jump >= 3 else 1
        i += jump
        steps += 1
    return steps

with open(sys.argv[1]) as f:
    base = array('i', (int(line) for line in f if line.strip()))

a = base[:]
b = base[:]
print(step_by_step(a, False))
print(step_by_step(b, True))