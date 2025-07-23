import sys

def main():
    with open(sys.argv[1], 'r') as infile:
        raw_instructions = infile.read().splitlines()
    
    pre_inst = []
    for line in raw_instructions:
        parts = line.split()
        op = parts[0]
        args = []
        for token in parts[1:]:
            if token in 'abcd':
                args.append(('r', 'abcd'.index(token)))
            else:
                args.append(('i', int(token)))
        pre_inst.append((op, args))
    
    i = 0
    while True:
        regs = [i, 0, 0, 0]
        pc = 0
        output_count = 0
        last_out = 1
        
        while pc < len(pre_inst) and output_count < 10:
            op, args = pre_inst[pc]
            if op == 'out':
                t, val = args[0]
                value = val if t == 'i' else regs[val]
                if value not in (0, 1) or value == last_out:
                    break
                last_out = value
                output_count += 1
                pc += 1
            elif op == 'cpy':
                t_src, src_val = args[0]
                src = src_val if t_src == 'i' else regs[src_val]
                t_dest, dest_idx = args[1]
                regs[dest_idx] = src
                pc += 1
            elif op == 'inc':
                t, reg_idx = args[0]
                regs[reg_idx] += 1
                pc += 1
            elif op == 'dec':
                t, reg_idx = args[0]
                regs[reg_idx] -= 1
                pc += 1
            elif op == 'jnz':
                t1, v1 = args[0]
                cond = v1 if t1 == 'i' else regs[v1]
                if cond != 0:
                    t2, v2 = args[1]
                    offset = v2 if t2 == 'i' else regs[v2]
                    pc += offset
                else:
                    pc += 1
        if output_count == 10:
            break
        i += 1
    sys.stdout.write(str(i))

if __name__ == "__main__":
    main()