import sys
t = str.maketrans('FBLR','0101')
lo = float('inf')
hi = -1
s = 0
with open(sys.argv[1]) as f:
    for line in f:
        c = line.strip()
        if not c: continue
        v = int(c.translate(t),2)
        s += v
        if v < lo: lo = v
        if v > hi: hi = v
n = hi - lo + 1
print(hi, n*(lo + hi)//2 - s)