import sys

p1 = p2 = 0
buf = []
with open(sys.argv[1]) as f:
    for line in f:
        s = line.strip()
        h = len(s) // 2
        c = set(s[:h]).intersection(s[h:]).pop()
        p1 += ord(c) - (96 if c.islower() else 38)
        buf.append(s)
        if len(buf) == 3:
            c = set(buf[0]).intersection(buf[1], buf[2]).pop()
            p2 += ord(c) - (96 if c.islower() else 38)
            buf.clear()
sys.stdout.write(f"{p1}\n{p2}\n")