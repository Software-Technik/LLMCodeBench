import collections
import itertools
import sys


def get_checksum(fn) -> int:
    """Opens file and counts number of lines that contain:
    - Exactly two of a character
    - Exactly three of a character

    returns 'checksum' by multiplying both counts
    """
    two = 0
    three = 0
    for item in fn:
        counts = set(collections.Counter(item).values())
        two += 2 in counts
        three += 3 in counts
    return two*three


def get_common_letters(fn) -> str:
    """Finds the two items in file that differ in just 1 character location;
    Returns their common letters as a joined string.
    """
    for i, j in itertools.combinations(fn, 2):
        if sum(c1 != c2 for c1, c2 in zip(i, j)) == 1:
            return "".join(c1 for c1, c2 in zip(i, j) if c1 == c2)


if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()

    data_lines = data.strip().splitlines()
    
    checksum = get_checksum(data_lines)

    common_letters = get_common_letters(data_lines)

    sys.stdout.write(f"{checksum} {common_letters}") 
