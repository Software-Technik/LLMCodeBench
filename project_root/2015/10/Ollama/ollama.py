import sys
from itertools import groupby

def part1_and_2(data):
    seq = data[0]
    len_part1, len_part2 = 0, 0
    for step in range(50):
        seq = next_seq(seq)
        if step == 39:
            len_part1 = len(seq)
    len_part2 = len(seq)

    return f"{len_part1}\n{len_part2}"

def next_seq(seq):
    res = []
    for i, g in groupby(seq):
        r = list(g)
        res.append(f"{len(r)}{i}")
    return ''.join(res)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(part1_and_2(data))