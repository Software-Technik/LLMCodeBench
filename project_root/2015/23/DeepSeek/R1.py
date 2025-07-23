import sys

def run_program(initial_a, program):
    a, b = initial_a, 0
    pc = 0
    n = len(program)
    while 0 <= pc < n:
        op, arg = program[pc]
        if op == 'hlf':
            if arg == 0:
                a //= 2
            else:
                b //= 2
            pc += 1
        elif op == 'tpl':
            if arg == 0:
                a *= 3
            else:
                b *= 3
            pc += 1
        elif op == 'inc':
            if arg == 0:
                a += 1
            else:
                b += 1
            pc += 1
        elif op == 'jmp':
            pc += arg
        elif op == 'jie':
            if arg[0] == 0:
                reg_val = a
            else:
                reg_val = b
            if reg_val % 2 == 0:
                pc += arg[1]
            else:
                pc += 1
        elif op == 'jio':
            if arg[0] == 0:
                reg_val = a
            else:
                reg_val = b
            if reg_val == 1:
                pc += arg[1]
            else:
                pc += 1
    return b

def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        data = [line.strip() for line in f]
    
    program = []
    for line in data:
        parts = line.split()
        op = parts[0]
        if op == 'jmp':
            program.append(('jmp', int(parts[1])))
        elif op in ['jie', 'jio']:
            reg_str = parts[1].rstrip(',')
            reg_index = 0 if reg_str == 'a' else 1
            offset = int(parts[2])
            program.append((op, (reg_index, offset)))
        else:
            reg_str = parts[1]
            reg_index = 0 if reg_str == 'a' else 1
            program.append((op, reg_index))
    
    part1_result = run_program(0, program)
    part2_result = run_program(1, program)
    sys.stdout.write(f"{part1_result}\n{part2_result}\n")

if __name__ == "__main__":
    main()