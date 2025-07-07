import sys

with open(sys.argv[1]) as f:
    s = f.readline().strip()

floor = 0
basement_pos = None

for i, ch in enumerate(s, 1):
    floor += 1 if ch == '(' else -1
    if basement_pos is None and floor < 0:
        basement_pos = i

sys.stdout.write(f"{floor}\n{basement_pos}\n")