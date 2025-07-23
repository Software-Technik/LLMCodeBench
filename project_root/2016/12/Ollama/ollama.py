import sys

def part1(data):
    register = [0] * 4
    interpret = lambda val: int(val) if val.isdigit() else register[ord(val)-ord('a')]
    i = 0
    while i < len(data):
        instr, x, *y = data[i].split()
        y = y[0] if y else None
        if instr == 'cpy':
            register[ord(y)-ord('a')] = interpret(x)
        elif instr == 'inc':
            register[ord(x)-ord('a')] += 1
        elif instr == 'dec':
            register[ord(x)-ord('a')] -= 1
        elif instr == 'jnz' and interpret(x) != 0:
            i += int(y)
            continue
        i += 1
    return register[0]

def part2(data):
    register = [0, 0, 1, 0]
    interpret = lambda val: int(val) if val.isdigit() else register[ord(val)-ord('a')]
    i = 0
    while i < len(data):
        instr, x, *y = data[i].split()
        y = y[0] if y else None
        if instr == 'cpy':
            register[ord(y)-ord('a')] = interpret(x)
        elif instr == 'inc':
            register[ord(x)-ord('a')] += 1
        elif instr == 'dec':
            register[ord(x)-ord('a')] -= 1
        elif instr == 'jnz' and interpret(x) != 0:
            i += int(y)
            continue
        i += 1
    return register[0]

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")