import sys
import math

def solve(part):
    with open(sys.argv[1]) as f:
        instructions = [line.strip().split() for line in f if len(line.strip()) >= 3]

    reg = {chr(c): 0 for c in range(97, 105)}
    i = reg["a"] = part - 1

    while i < 11:
        op, r, s = instructions[i]
        v = reg.get(s, int(s)) if not s.isalpha() else int(s)

        if op == "set":
            reg[r] = v
        elif op == "sub":
            reg[r] -= v
        elif op == "mul":
            reg[r] *= v
        elif op == "jnz" and interpret(r) != 0:
            i += v
            continue

        i += 1

    if part == 1:
        return (reg["b"] - reg["e"]) * (reg["b"] - reg["d"])
    else:
        b, c = reg["b"], reg["c"]
        nonprimes = (c - b) // 34 + 1
        for i in range(b + 17, c + 1, 34):
            for d in range(3, int(math.sqrt(i)) + 1, 2):
                if i % d == 0:
                    nonprimes += 1
                    break

        return nonprimes

input_strings = sys.argv[1]
sys.stdout.write(f"{solve(1)}\n{solve(2)}\n")