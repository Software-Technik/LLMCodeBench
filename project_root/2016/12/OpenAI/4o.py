import sys

def execute(data, part2=False):
    register = {'a': 0, 'b': 0, 'c': int(part2), 'd': 0}
    interpret = lambda val: register[val] if val.isalpha() else int(val)
    i = 0

    while i < len(data):
        instr, x, *y = data[i].split()
        y = y[0] if y else None

        if instr == 'cpy' and y.isalpha():
            register[y] = interpret(x)
        elif instr == 'inc':
            register[x] += 1
        elif instr == 'dec':
            register[x] -= 1
        elif instr == 'jnz' and interpret(x) != 0:
            i += interpret(y) - 1

        i += 1

    return register['a']

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings, 'r') as infile:
        data = infile.read().splitlines()

    sys.stdout.write(f"{execute(data)} {execute(data, part2=True)}")