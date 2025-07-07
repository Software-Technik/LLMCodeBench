import sys
from array import array

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

insts = []
for line in lines:
    if line.startswith('toggle'):
        op = 2
        rest = line[7:]
    elif line.startswith('turn off'):
        op = 1
        rest = line[9:]
    else:
        op = 0
        rest = line[8:]
    a, b = rest.split(' through ')
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))
    insts.append((op, x1, y1, x2, y2))

grid1 = [bytearray(1000) for _ in range(1000)]
grid2 = [array('I', [0] * 1000) for _ in range(1000)]

for op, x1, y1, x2, y2 in insts:
    for y in range(y1, y2 + 1):
        row1 = grid1[y]
        row2 = grid2[y]
        if op == 0:
            for x in range(x1, x2 + 1):
                row1[x] = 1
                row2[x] += 1
        elif op == 1:
            for x in range(x1, x2 + 1):
                row1[x] = 0
                if row2[x]:
                    row2[x] -= 1
        else:
            for x in range(x1, x2 + 1):
                row1[x] ^= 1
                row2[x] += 2

part1 = sum(row.count(1) for row in grid1)
part2 = sum(sum(row) for row in grid2)
print(part1)
print(part2)