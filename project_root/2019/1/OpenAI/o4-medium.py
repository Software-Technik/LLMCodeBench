import sys

t1 = t2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        s = line.strip()
        if not s: continue
        m = int(s)
        f0 = m // 3 - 2
        t1 += f0
        t2 += f0
        while True:
            f0 = f0 // 3 - 2
            if f0 <= 0:
                break
            t2 += f0
sys.stdout.write(f"{t1} {t2}")