import sys

h1 = d1 = aim = h2 = d2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        if not line: continue
        cmd, s = line.split()
        v = int(s)
        if cmd == 'forward':
            h1 += v
            h2 += v
            d2 += aim * v
        elif cmd == 'down':
            d1 += v
            aim += v
        elif cmd == 'up':
            d1 -= v
            aim -= v
sys.stdout.write(f"{h1*d1} {h2*d2}")