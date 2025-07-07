import sys
from sys import argv, stdout

f = open(argv[1])
first = f.readline().split()
n = len(first)
w = [1]
c = 1
for k in range(1, n):
    c = c * (n - k + 1) // k
    w.append(c)
w_rev = w[::-1]
sign_start = n % 2 != 0
t1 = t2 = 0
def process(vals):
    global t1, t2
    add = sign_start
    for v, a, b in zip(vals, w, w_rev):
        m = v * a
        t1 += m if add else -m
        n2 = v * b
        t2 += n2 if add else -n2
        add = not add

process(list(map(int, first)))
for line in f:
    process(list(map(int, line.split())))
stdout.write(f"{t1} {t2}")