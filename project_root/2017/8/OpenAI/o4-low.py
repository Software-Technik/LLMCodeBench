import sys

def main():
    registers = {}
    maximum_ever = float('-inf')
    with open(sys.argv[1]) as f:
        for line in f:
            if not line.strip(): continue
            parts = line.split()
            reg, instr, amt = parts[0], parts[1], int(parts[2])
            cond_reg, op, val = parts[4], parts[5], int(parts[6])
            cond_val = registers.get(cond_reg, 0)
            if ((op == '<' and cond_val < val) or
                (op == '>' and cond_val > val) or
                (op == '<=' and cond_val <= val) or
                (op == '>=' and cond_val >= val) or
                (op == '==' and cond_val == val) or
                (op == '!=' and cond_val != val)):
                cur = registers.get(reg, 0) + (amt if instr == 'inc' else -amt)
                registers[reg] = cur
                if cur > maximum_ever: maximum_ever = cur
    current_max = max(registers.values()) if registers else 0
    print(current_max)
    print(maximum_ever)

if __name__ == "__main__":
    main()