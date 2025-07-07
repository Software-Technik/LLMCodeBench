#!/usr/bin/env python3
import sys
import operator
from collections import defaultdict

ops = {'<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge, '==': operator.eq, '!=': operator.ne}

regs = defaultdict(int)
max_e = float('-inf')
with open(sys.argv[1]) as f:
    for l in f:
        a,i,am,_,cr,co,va = l.split()
        am = int(am); va = int(va)
        if ops[co](regs[cr], va):
            regs[a] += am if i=='inc' else -am
            v = regs[a]
            if v > max_e: max_e = v
m = max(regs.values())
print(m)
print(int(max_e))