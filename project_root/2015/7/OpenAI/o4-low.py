import sys
sys.setrecursionlimit(10000)
def solve(data, override_b=None):
    inst = {}
    for line in data:
        lhs, dest = line.split(" -> ")
        inst[dest] = lhs.split()
    cache = {}
    def eval_wire(x):
        if x.isdigit():
            return int(x)
        if x in cache:
            return cache[x]
        if x == 'b' and override_b is not None:
            res = override_b
        else:
            parts = inst[x]
            if len(parts) == 1:
                res = eval_wire(parts[0])
            elif parts[0] == 'NOT':
                res = ~eval_wire(parts[1]) & 0xFFFF
            else:
                a, op, b = parts
                va = eval_wire(a)
                vb = eval_wire(b)
                if op == 'AND':
                    res = va & vb
                elif op == 'OR':
                    res = va | vb
                elif op == 'LSHIFT':
                    res = (va << vb) & 0xFFFF
                elif op == 'RSHIFT':
                    res = va >> vb
        cache[x] = res
        return res
    return eval_wire('a')

data = [line.strip() for line in open(sys.argv[1])]
part1 = solve(data)
part2 = solve(data, override_b=part1)
print(part1)
print(part2)