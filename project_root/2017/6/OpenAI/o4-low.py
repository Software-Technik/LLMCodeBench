import sys

def redistribute(banks):
    seen = {}
    b = banks[:]
    length = len(b)
    step = 0
    while True:
        state = tuple(b)
        if state in seen:
            return step, step - seen[state]
        seen[state] = step
        max_idx = max(range(length), key=b.__getitem__)
        blocks = b[max_idx]
        b[max_idx] = 0
        q, r = divmod(blocks, length)
        if q:
            for i in range(length):
                b[i] += q
        for i in range(1, r + 1):
            b[(max_idx + i) % length] += 1
        step += 1

with open(sys.argv[1]) as f:
    banks = list(map(int, f.read().split()))

part1, part2 = redistribute(banks)
print(part1)
print(part2)