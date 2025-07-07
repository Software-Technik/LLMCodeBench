import sys

def simulate(c, days):
    c = c[:]
    for _ in range(days):
        zero = c[0]
        for i in range(8):
            c[i] = c[i+1]
        c[8] = zero
        c[6] += zero
    total = 0
    for x in c:
        total += x
    return total

data = open(sys.argv[1]).read().strip().split(',')
init = [0]*9
for x in data:
    init[int(x)] += 1

p1 = simulate(init, 80)
p2 = simulate(init, 256)
sys.stdout.write(f"{p1} {p2}")