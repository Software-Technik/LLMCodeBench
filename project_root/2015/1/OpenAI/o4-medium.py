import sys
with open(sys.argv[1]) as f:
    s = f.readline().strip()
floor = 0
first = None
for i, c in enumerate(s, 1):
    floor += 1 if c == '(' else -1
    if first is None and floor < 0:
        first = i
sys.stdout.write(f"{floor}\n{first}\n")