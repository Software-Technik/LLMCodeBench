import collections
import sys

def get_checksum(fn) -> int:
    two = 0
    three = 0
    for item in fn:
        counts = collections.Counter(item).values()
        if 2 in counts:
            two += 1
        if 3 in counts:
            three += 1
    return two * three

def get_common_letters(fn) -> str:
    for index, word in enumerate(fn):
        for other in fn[index + 1:]:
            mismatch_count = 0
            merge_result = []
            for c1, c2 in zip(word, other):
                if c1 == c2:
                    merge_result.append(c1)
                else:
                    mismatch_count += 1
                    if mismatch_count > 1:
                        break
            if mismatch_count == 1:
                return ''.join(merge_result)

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data_lines = f.read().splitlines()

    checksum = get_checksum(data_lines)
    common_letters = get_common_letters(data_lines)

    sys.stdout.write(f"{checksum} {common_letters}")