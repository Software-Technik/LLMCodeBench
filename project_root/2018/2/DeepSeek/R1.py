import collections
import sys


def get_checksum(fn) -> int:
    two = 0
    three = 0
    for item in fn:
        counts = collections.Counter(item)
        values = counts.values()
        two += 2 in values
        three += 3 in values
    return two * three


def get_common_letters(fn) -> str:
    if not fn:
        return ""
    m = len(fn[0])
    for j in range(m):
        seen = set()
        for s in fn:
            candidate = s[:j] + s[j+1:]
            if candidate in seen:
                return candidate
            seen.add(candidate)
    return ""


if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()

    data_lines = data.strip().splitlines()
    
    checksum = get_checksum(data_lines)
    common_letters = get_common_letters(data_lines)
    sys.stdout.write(f"{checksum} {common_letters}")