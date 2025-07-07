import sys

f = open(sys.argv[1])
t1 = t2 = 0
for line in f:
    x = ord(line[0]) - 64
    y1 = ord(line[2]) - 87
    d = y1 - x
    if d == 0:
        s1 = 3
    elif d == 1 or d == -2:
        s1 = 6
    else:
        s1 = 0
    t1 += y1 + s1
    rs = (ord(line[2]) - 88) * 3
    if rs == 6:
        y2 = x % 3 + 1
    elif rs == 3:
        y2 = x
    else:
        y2 = (x + 1) % 3 + 1
    t2 += y2 + rs
f.close()
sys.stdout.write(f"{t1}\n{t2}\n")