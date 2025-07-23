import sys

def execute(a):
    inout_strings = sys.argv[1]
    with open(inout_strings, 'r') as infile:
        instructions = [line.split() for line in infile.read().splitlines()]

    register = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    line = 0
    transmitted = [1]

    interpret = lambda val: register[val] if val.isalpha() else int(val)

    while line < len(instructions):
        parts = instructions[line]
        instr = parts[0]
        
        if instr == 'out':
            x_ = interpret(parts[1])
            if x_ not in {0, 1} or x_ == transmitted[-1]:
                return False
            transmitted.append(x_)
            if len(transmitted) > 10:
                return True
            line += 1
        elif instr == 'cpy':
            register[parts[2]] = interpret(parts[1])
            line += 1
        elif instr == 'inc':
            register[parts[1]] += 1
            line += 1
        elif instr == 'dec':
            register[parts[1]] -= 1
            line += 1
        elif instr == 'jnz':
            x_val = interpret(parts[1])
            if x_val != 0:
                line += interpret(parts[2])
            else:
                line += 1

i = 0
while True:
    if execute(i):
        break
    i += 1

sys.stdout.write(f"{i}")