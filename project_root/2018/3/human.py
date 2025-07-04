import collections
import sys



def extract_coordinates(iterable) -> tuple:
    """Takes iterable with claims in the form of:
            '#1 @ 906,735: 28x17\n'
       Extracts ID number, coordinates, size
       Returns it as tuple of tuples
    """
    for label in iterable:
        number, _, specs = label.partition(" @ ")
        coor, _, size = specs.partition(": ")
        x, y = coor.split(",")
        width, height = size.strip().split("x")
        yield number[1:], (int(x), int(y)), (int(width), int(height))


def day3_part1(f) -> int:
    """Calculates the number of squares that have overlap from a claim file"""

    used = {}
    for _, (x, y), (width, height) in extract_coordinates(f):
        for x1 in range(x, x+width):
            for y1 in range(y, y+height):
                used[(x1, y1)] = used.setdefault((x1, y1), 0) + 1
    squares = sum(1 for square in used.values() if square >= 2)
    return squares


def day3_part2(f) -> int:
    """Finds the claim that has no overlap with other claims in a claim file"""
    claims_on_square = collections.defaultdict(list)
    labels = {}
    for number, (x, y), (width, height) in extract_coordinates(f):
        labels[number] = True
        for x1 in range(x, x+width):
            for y1 in range(y, y+height):
                claims_on_square[(x1, y1)].append(number)

                if len(claims_on_square[(x1, y1)]) > 1:
                    for claim in claims_on_square[(x1, y1)]:
                        labels[claim] = False

    for claim, no_overlap in labels.items():
        if no_overlap:
            return claim


if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()

    data_lines = data.strip().splitlines()


    overlap_squares = day3_part1(data_lines)
    claim_without_overlap = day3_part2(data_lines)

    sys.stdout.write(f"{overlap_squares} {claim_without_overlap}") 