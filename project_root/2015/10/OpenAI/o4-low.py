import sys

def next_seq(seq):
    res = []
    prev = seq[0]
    cnt = 1
    for c in seq[1:]:
        if c == prev:
            cnt += 1
        else:
            res.append(str(cnt)); res.append(prev)
            prev = c; cnt = 1
    res.append(str(cnt)); res.append(prev)
    return ''.join(res)

def part(seq, steps):
    for _ in range(steps):
        seq = next_seq(seq)
    return len(seq)

with open(sys.argv[1]) as f:
    seq = f.readline().strip()

print(part(seq, 40))
print(part(seq, 50))