import sys

def execute(a):
    instructions, transmitted = [], [1]
    for line in open(sys.argv[1]):
        parts = line.split()
        instructions.append((parts[0], *map(lambda x: int(x) if '0' <= x <= '9' else {'a': a, 'b': 0, 'c': 0, 'd': 0}[x], parts[1:])))
    reg_a, reg_b = a, 0
    line = 0

    while line < len(instructions):
        instr, x, y = instructions[line]
        if instr == 'out':
            if not (x in {0, 1} and transmitted[-1] != x) or len(transmitted) > 9:
                return False
            transmitted.append(x)
            if len(transmitted) == 10: return True
        elif instr == 'cpy': reg_a = y
        elif instr == 'inc': reg_b += 1
        elif instr == 'dec': reg_b -= 1
        elif instr == 'jnz': line += x * (x != 0 and y or 0)
        else: line += 1

i = 0
while True:
    if execute(i): break
    i += 1

sys.stdout.write(f"{i}")