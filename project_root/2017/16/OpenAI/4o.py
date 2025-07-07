import sys

def parse_instruction(instruction):
    first, rest = instruction[0], instruction[1:]
    if first == 's':
        return ('s', int(rest))
    elif first == 'x':
        a, b = map(int, rest.split('/'))
        return ('x', a, b)
    elif first == 'p':
        a, b = rest.split('/')
        return ('p', a, b)

def dance(dancers, instructions):
    dancers = list(dancers)
    for instr in instructions:
        if instr[0] == 's':
            x = instr[1]
            dancers = dancers[-x:] + dancers[:-x]
        elif instr[0] == 'x':
            a, b = instr[1], instr[2]
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif instr[0] == 'p':
            a_idx, b_idx = dancers.index(instr[1]), dancers.index(instr[2])
            dancers[a_idx], dancers[b_idx] = dancers[b_idx], dancers[a_idx]
    return ''.join(dancers)

def long_dance(dancers, instructions, iterations):
    seen = []
    current = dancers
    for i in range(iterations):
        if current in seen:
            cycle_start = seen.index(current)
            cycle_length = i - cycle_start
            return seen[(iterations - cycle_start) % cycle_length + cycle_start]
        seen.append(current)
        current = dance(current, instructions)
    return current

input_strings = sys.argv[1]
with open(input_strings) as f:
    content = f.read().strip()

instructions = [inst.strip() for inst in content.split(',') if inst.strip()]
parsed = [parse_instruction(inst) for inst in instructions]

programs = "abcdefghijklmnop"
print(dance(programs, parsed))
print(long_dance(programs, parsed, 1_000_000_000))