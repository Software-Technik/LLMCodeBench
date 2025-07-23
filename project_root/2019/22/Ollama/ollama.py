import sys

def num(line):
    return int(''.join(filter(str.isdigit, line)))

def part1(ls, size=10007):
    p = 2019
    for l in ls:
        if 'stack' in l: p = size - 1 - p
        elif 'cut' in l: n, p = int(num(l)), p - num(l) if p >= num(l) else size + (p - num(l))
        elif 'inc' in l:p = (num(l) * p) % size
    return p

DECK = 119315717514047

def shuffle(l):
    f = l.split()
    if "new" in f: return [-1, -1]
    elif 'cut' in f: return [-int(f[1]), 1]
    else: return [0, int(f[3])]

def apply(f, x): return (f[0] + f[1] * x) % DECK

def compose(f, g):
    c = shuffle(g)
    return [apply(f, c[0]), (f[1] * c[1]) % DECK]

shuf = None
for l in ls: shuf = compose(shuffle(l), shuf)

assert apply(compose([DECK - 1, -1], shuf) for _ in range(DECK-1)) == [0, 1]

REPEAT = (DECK - REPEAT % DECK) + 2020
shuf = [(apply(f, REPEAT) , (REPEAT - 1)) for f in shuf]
return [x for x in ls.copy()][0:5] # to maintain the test output without extra spaces.