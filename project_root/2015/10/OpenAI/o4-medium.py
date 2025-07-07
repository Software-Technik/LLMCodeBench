import sys

def next_seq(seq):
    builder = []
    last = seq[0]
    count = 1
    for c in seq[1:]:
        if c == last:
            count += 1
        else:
            builder.append(str(count)); builder.append(last)
            last = c; count = 1
    builder.append(str(count)); builder.append(last)
    return ''.join(builder)

path = sys.argv[1]
with open(path) as f:
    seq = f.readline().strip()

part1 = part2 = None
for i in range(1, 51):
    seq = next_seq(seq)
    if i == 40:
        part1 = len(seq)
    if i == 50:
        part2 = len(seq)

sys.stdout.write(f"{part1}\n{part2}\n")