import sys
import re

def solve(text, part):
    lines = text.splitlines()
    x = y = 0
    xs = [0]
    ys = [0]
    steps = 0
    if part == 1:
        for line in lines:
            d, n = line.split()
            n = int(n)
            steps += n
            if d == "U": x -= n
            elif d == "D": x += n
            elif d == "R": y += n
            else: y -= n
            xs.append(x); ys.append(y)
    else:
        for line in lines:
            h = line.split('(#',1)[1][:-1]
            d = int(h[-1])
            n = int(h[:-1],16)
            steps += n
            if d == 0: y += n
            elif d == 1: x += n
            elif d == 2: y -= n
            else: x -= n
            xs.append(x); ys.append(y)
    cross = 0
    for i in range(1, len(xs)):
        cross += xs[i-1]*ys[i] - xs[i]*ys[i-1]
    cross += xs[-1]*ys[0] - xs[0]*ys[-1]
    res = (abs(cross) + steps)//2 + 1
    return res

text = open(sys.argv[1]).read()
print(solve(text,1), solve(text,2))