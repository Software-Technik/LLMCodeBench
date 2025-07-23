import sys
import math

def solve(part):
    with open(sys.argv[1]) as f:
        instructions = [line.strip().split() for line in f if line.strip()]
        instructions = [line for line in instructions if len(line) >= 3]

    reg = {chr(c): 0 for c in range(97, 105)}
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
        b_start = reg["b"]
        c_end = reg["c"]
        nonprimes = (c_end - b_start) // 34 + 1
        
        n = 360
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        for i in range(2, math.isqrt(n) + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        primes = [i for i in range(3, n+1) if sieve[i]]
        
        for b_val in range(b_start + 17, c_end + 1, 34):
            root = math.isqrt(b_val)
            for p in primes:
                if p > root:
                    break
                if b_val % p == 0:
                    nonprimes += 1
                    break
                    
        return nonprimes

sys.stdout.write(f"{solve(1)}\n{solve(2)}\n")