import sys
total1 = total2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        a, b, c = map(int, line.split('x'))
        ab = a * b; ac = a * c; bc = b * c
        total1 += 2 * (ab + ac + bc) + min(ab, ac, bc)
        total2 += 2 * ((a + b + c) - max(a, b, c)) + ab * c
sys.stdout.write(f"{total1}\n{total2}\n")