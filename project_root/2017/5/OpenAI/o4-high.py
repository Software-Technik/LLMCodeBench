import sys
with open(sys.argv[1]) as f:
    instr0 = list(map(int, f.read().split()))
l = len(instr0)
instr = instr0[:]
i = steps = 0
while 0 <= i < l:
    j = instr[i]
    instr[i] = j + 1
    i += j
    steps += 1
print(steps)
instr = instr0[:]
i = steps = 0
while 0 <= i < l:
    j = instr[i]
    instr[i] = j - 1 if j >= 3 else j + 1
    i += j
    steps += 1
print(steps)