import sys

t1 = t2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        if len(line) < 3: continue
        x = ord(line[0]) - 64
        a = ord(line[2]) - 88
        y = a + 1
        d = y - x
        if d == 0:
            t1 += y + 3
        elif d == 1 or d == -2:
            t1 += y + 6
        else:
            t1 += y
        rs = a * 3
        if rs == 6:
            y2 = x % 3 + 1
        elif rs == 3:
            y2 = x
        else:
            y2 = (x + 1) % 3 + 1
        t2 += y2 + rs

sys.stdout.write(f"{t1}\n{t2}\n")