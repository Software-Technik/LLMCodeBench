import sys
from collections import Counter

def is_pass(pw, twosame):
    counts = Counter(pw)
    return 2 in counts.values() == twosame and list(pw) == sorted(pw)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    l, u = map(int, next(f).split("-"))
sys.stdout.write(' '.join(str(sum(twosame in counter.values() for pw in range(l, u+1) if is_pass(str(pw), twosame))) for twosame in [False, True]))