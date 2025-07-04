import sys

def part1(data):
    register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    interpret = lambda val: int(val) if val.isdigit() else register[val]
    i = 0

    while i < len(data):
        instr, x, *y = data[i].split()
        y = y[0] if y else None

        if instr == 'cpy':
            register[y] = interpret(x)

        if instr == 'inc':
            register[x] += 1

        if instr == 'dec':
            register[x] -= 1

        if instr == 'jnz':
            if interpret(x) != 0:
                i += int(y)
                continue

        i += 1
    return register['a']


def part2(data):
    register = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    interpret = lambda val: int(val) if val.isdigit() else register[val]
    i = 0

    while i < len(data):
        instr, x, *y = data[i].split()
        y = y[0] if y else None

        if instr == 'cpy':
            register[y] = interpret(x)

        if instr == 'inc':
            register[x] += 1

        if instr == 'dec':
            register[x] -= 1

        if instr == 'jnz':
            if interpret(x) != 0:
                i += int(y)
                continue

        i += 1
    return register['a']



inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")  
