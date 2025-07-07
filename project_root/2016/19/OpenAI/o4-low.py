import sys

n = int(open(sys.argv[1]).read().strip())
b = n.bit_length() - 1
p1 = 2 * (n - (1 << b)) + 1
p = 1
while p * 3 <= n:
    p *= 3
l = n - p
if n == p:
    p2 = n
elif n <= 2 * p:
    p2 = l
else:
    p2 = 2 * l
print(f"{p1} {p2}")