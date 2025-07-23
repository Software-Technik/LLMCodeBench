import sys

def run_program(data, initial_c):
    register = {'a': 0, 'b': 0, 'c': initial_c, 'd': 0}
    interpret = lambda val: int(val) if val.lstrip('-').isdigit() else register[val]
    i = 0
    n = len(data)
    
    while i < n:
        parts = data[i].split()
        instr = parts[0]
        
        if instr == 'cpy':
            x = parts[1]
            y = parts[2]
            register[y] = interpret(x)
            i += 1
        elif instr == 'inc':
            x = parts[1]
            register[x] += 1
            i += 1
        elif instr == 'dec':
            x = parts[1]
            register[x] -= 1
            i += 1
        elif instr == 'jnz':
            x = parts[1]
            y = parts[2]
            if interpret(x) != 0:
                i += int(y)
            else:
                i += 1
    return register['a']

def part1(data):
    return run_program(data, 0)

def part2(data):
    return run_program(data, 1)

with open(sys.argv[1], 'r') as infile:
    data = [line.strip() for line in infile]

sys.stdout.write(f"{part1(data)} {part2(data)}")