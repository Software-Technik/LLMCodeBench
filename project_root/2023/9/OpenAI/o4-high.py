import sys
f = open(sys.argv[1])
first = f.readline().split()
n = len(first)
c = [1] * (n + 1)
for i in range(1, n + 1):
    c[i] = c[i - 1] * (n - i + 1) // i
w1 = [0] * n
sign = 1
for i in range(n):
    w1[i] = sign * c[i]
    sign = -sign
w1r = [0] * n
sign = 1 if n & 1 else -1
for i in range(n):
    w1r[i] = sign * c[i + 1]
    sign = -sign
s1 = s2 = 0
arr = list(map(int, first))
for a, w, wr in zip(arr, w1, w1r):
    s1 += a * w
    s2 += a * wr
for line in f:
    arr = list(map(int, line.split()))
    for a, w, wr in zip(arr, w1, w1r):
        s1 += a * w
        s2 += a * wr
if not n & 1:
    s1 = -s1
    s2 = -s2
sys.stdout.write(f"{s1} {s2}")