import sys

def execute(a):

    with open(sys.argv[1], 'r') as infile:
        instructions = infile.read().splitlines()

    register = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    line = 0
    transmitted = [1]

    interpret = lambda val: register[val] if val.isalpha() else int(val)

    while line < len(instructions):
        parts = instructions[line].split()
        instr, x = parts[0], parts[1]
        y = parts[2] if len(parts) > 2 else None

        if instr == 'out':
            x_ = interpret(x)
            if x_ not in {0, 1} or x_ == transmitted[-1]:
                return False
            transmitted.append(x_)
            if len(transmitted) > 10:
                return True

        elif instr == 'cpy':
            if y in register:
                register[y] = interpret(x)

        elif instr == 'inc':
            register[x] += 1

        elif instr == 'dec':
            register[x] -= 1

        elif instr == 'jnz':
            if interpret(x) != 0:
                line += interpret(y)
                continue

        line += 1
    
    return False

i = 0
while not execute(i):
    i += 1

sys.stdout.write(f"{i}")