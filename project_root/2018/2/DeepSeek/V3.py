import collections
import itertools
import sys


def get_checksum(fn) -> int:
    two = 0
    three = 0
    for item in fn:
        counts = collections.defaultdict(int)
        for c in item:
            counts[c] += 1
        vals = set(counts.values())
        two += 2 in vals
        three += 3 in vals
    return two * three


def get_common_letters(fn) -> str:
    for i, j in itertools.combinations(fn, 2):
        diff = 0
        common = []
        for c1, c2 in zip(i, j):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    break
            else:
                common.append(c1)
        if diff == 1:
            return ''.join(common)


if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()

    data_lines = data.strip().splitlines()
    
    checksum = get_checksum(data_lines)
    common_letters = get_common_letters(data_lines)

    sys.stdout.write(f"{checksum} {common_letters}")