import sys

def solve(data, override_b=None):
    ops = {}
    for line in data:
        expr, target = line.split(" -> ")
        ops[target] = expr.split()
    cache = {}
    def get(x):
        if x.isdigit():
            return int(x)
        if x == "b" and override_b is not None:
            return override_b
        if x in cache:
            return cache[x]
        expr = ops[x]
        if len(expr) == 1:
            val = get(expr[0])
        elif expr[0] == "NOT":
            val = ~get(expr[1]) & 0xFFFF
        else:
            a, op, b = expr
            a = get(a) if not a.isdigit() else int(a)
            b = get(b) if not b.isdigit() else int(b)
            if op == "AND":
                val = a & b
            elif op == "OR":
                val = a | b
            elif op == "LSHIFT":
                val = (a << b) & 0xFFFF
            elif op == "RSHIFT":
                val = a >> b
        cache[x] = val
        return val
    return get("a")

data = [l.strip() for l in open(sys.argv[1])]
p1 = solve(data)
p2 = solve(data, override_b=p1)
print(p1)
print(p2)