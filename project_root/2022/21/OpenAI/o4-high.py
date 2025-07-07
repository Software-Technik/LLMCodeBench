import sys
from functools import lru_cache
data = open(sys.argv[1]).read().splitlines()
monkeys = {}
for line in data:
    k, v = line.split(': ')
    if v.isdigit():
        monkeys[k] = int(v)
    else:
        a, op, b = v.split()
        monkeys[k] = (a, op, b)
@lru_cache(None)
def eval1(m):
    v = monkeys[m]
    if isinstance(v, int):
        return v
    a, op, b = v
    x = eval1(a); y = eval1(b)
    if op == '+': return x + y
    if op == '-': return x - y
    if op == '*': return x * y
    return x // y
res1 = eval1('root')
monkeys['humn'] = None
@lru_cache(None)
def contains_h(m):
    if m == 'humn': return True
    v = monkeys[m]
    if isinstance(v, int): return False
    a, _, b = v
    return contains_h(a) or contains_h(b)
@lru_cache(None)
def eval_const(m):
    v = monkeys[m]
    if isinstance(v, int):
        return v
    a, op, b = v
    x = eval_const(a); y = eval_const(b)
    if op == '+': return x + y
    if op == '-': return x - y
    if op == '*': return x * y
    return x // y
l, op, r = monkeys['root']
if contains_h(l):
    var, target = l, eval_const(r)
else:
    var, target = r, eval_const(l)
def solve(m, t):
    if m == 'humn':
        return t
    a, op, b = monkeys[m]
    if contains_h(a):
        c = eval_const(b)
        if op == '+': nt = t - c
        elif op == '-': nt = t + c
        elif op == '*': nt = t // c
        else: nt = t * c
        return solve(a, nt)
    else:
        c = eval_const(a)
        if op == '+': nt = t - c
        elif op == '-': nt = c - t
        elif op == '*': nt = t // c
        else: nt = c // t
        return solve(b, nt)
res2 = solve(var, target)
sys.stdout.write(f"{res1}\n{res2}\n")