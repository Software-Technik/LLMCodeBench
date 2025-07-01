import sys
import math

def solve(part):
    with open(sys.argv[1]) as f:
        # On filtre les lignes vides et mal formatées
        instructions = [line.strip().split() for line in f if line.strip()]
        instructions = [line for line in instructions if len(line) >= 3]

    reg = {chr(c): 0 for c in range(97, 105)}  # registres a-h
    i = 0
    reg["a"] = part - 1

    def interpret(s):
        return reg.get(s, 0) if s.isalpha() else int(s)

    while i < 11:
        line = instructions[i]
        op, r, s = line[0], line[1], line[2]
        v = interpret(s)

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
        for b in range(b + 17, c + 1, 34):
            for d in range(3, int(math.sqrt(b)) + 1, 2):
                if b % d == 0:
                    nonprimes += 1
                    break
        return nonprimes

# Lecture de l'argument de ligne de commande
input_strings = sys.argv[1]
sys.stdout.write(f"{solve(1)}\n{solve(2)}\n")
