import sys

def parse_program(data):
    reg_map = {'a':0, 'b':1, 'c':2, 'd':3}
    precompiled = []
    for line in data:
        tokens = line.split()
        op = tokens[0]
        if op == 'cpy':
            src, dest = tokens[1], tokens[2]
            if src.replace('-', '', 1).isdigit():
                precompiled.append(('cpy', 'imm', int(src), reg_map[dest]))
            else:
                precompiled.append(('cpy', 'reg', reg_map[src], reg_map[dest]))
        elif op == 'inc':
            precompiled.append(('inc', reg_map[tokens[1]]))
        elif op == 'dec':
            precompiled.append(('dec', reg_map[tokens[1]]))
        elif op == 'jnz':
            cond, offset = tokens[1], tokens[2]
            offset_val = int(offset)
            if cond.replace('-', '', 1).isdigit():
                precompiled.append(('jnz', 'imm', int(cond), offset_val))
            else:
                precompiled.append(('jnz', 'reg', reg_map[cond], offset_val))
    return precompiled

def run_program(program, initial_registers):
    regs = initial_registers[:]
    pc = 0
    n = len(program)
    while pc < n:
        op = program[pc]
        if op[0] == 'cpy':
            src_type, src_val, dest_idx = op[1], op[2], op[3]
            value = src_val if src_type == 'imm' else regs[src_val]
            regs[dest_idx] = value
            pc += 1
        elif op[0] == 'inc':
            regs[op[1]] += 1
            pc += 1
        elif op[0] == 'dec':
            regs[op[1]] -= 1
            pc += 1
        elif op[0] == 'jnz':
            cond_type, cond_val, offset = op[1], op[2], op[3]
            value = cond_val if cond_type == 'imm' else regs[cond_val]
            if value != 0:
                pc += offset
            else:
                pc += 1
    return regs[0]

with open(sys.argv[1], 'r') as infile:
    data = infile.read().splitlines()

program = parse_program(data)
part1_result = run_program(program, [0, 0, 0, 0])
part2_result = run_program(program, [0, 0, 1, 0])
sys.stdout.write(f"{part1_result} {part2_result}")