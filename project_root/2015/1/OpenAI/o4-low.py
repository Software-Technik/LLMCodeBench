import sys
s = open(sys.argv[1]).read().strip()
part1 = s.count('(') - s.count(')')
level = 0
part2 = 0
for i, ch in enumerate(s, 1):
    level += 1 if ch == '(' else -1
    if level < 0:
        part2 = i
        break
sys.stdout.write(f"{part1}\n{part2}\n")