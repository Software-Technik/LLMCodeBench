import collections

def get_checksum(fn) -> int:
    two, three = 0, 0
    for item in fn:
        counts = set(collections.Counter(item).values())
        two += 2 in counts
        three += 3 in counts
    return two * three

def get_common_letters(fn) -> str:
    for i in range(len(fn)):
        for j in range(i + 1, len(fn)):
            if sum(c1 != c2 for c1, c2 in zip(fn[i], fn[j])) == 1:
                return "".join(c1 for c1, c2 in zip(fn[i], fn[j]) if c1 == c2)

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    checksum = get_checksum(data)
    common_letters = get_common_letters(data)
    print(f"{checksum} {common_letters}")