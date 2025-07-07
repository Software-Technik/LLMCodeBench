import sys, math

def sieve(n):
    is_p = [True] * (n + 1)
    ps = []
    for i in range(2, n + 1):
        if is_p[i]:
            ps.append(i)
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return ps

def main():
    inst = []
    with open(sys.argv[1]) as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                inst.append(parts)
                if len(inst) == 11:
                    break

    def interpret(s, reg):
        return reg[s] if s.isalpha() else int(s)

    def run(part):
        reg = {chr(c): 0 for c in range(97, 105)}
        reg['a'] = part - 1
        i = 0
        while i < 11:
            op, x, y = inst[i]
            vy = interpret(y, reg)
            if op == 'set':
                reg[x] = vy
            elif op == 'sub':
                reg[x] -= vy
            elif op == 'mul':
                reg[x] *= vy
            elif op == 'jnz' and interpret(x, reg) != 0:
                i += vy
                continue
            i += 1
        if part == 1:
            return (reg['b'] - reg['e']) * (reg['b'] - reg['d'])
        b, c = reg['b'], reg['c']
        nonp = (c - b) // 34 + 1
        primes = sieve(int(math.isqrt(c)) + 1)
        for bb in range(b + 17, c + 1, 34):
            for p in primes:
                if p * p > bb:
                    break
                if bb % p == 0:
                    nonp += 1
                    break
        return nonp

    r1 = run(1)
    r2 = run(2)
    sys.stdout.write(f"{r1}\n{r2}\n")

if __name__ == '__main__':
    main()