import itertools
import sys


def get_frequency(data, start: int = 0) -> int:
    """Takes frequency modulation file and returns final frequency"""
    return sum(int(start) + item for item in map(int, data))


def first_repeat(data, start: int = 0) -> int:
    """Finds the first repeating frequency when cycling the modulation file

    Note: Updating a dict item-by-item seems faster than set; using dummy dict
    """
    seen = {start}
    frequency = start
    for modulation in map(int, itertools.cycle(data)):
        frequency += modulation
        if frequency in seen:
            return frequency
        seen.add(frequency)


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file) as f:
        data = list(map(int, f.read().strip().splitlines()))

    frequency = get_frequency(data)
    repeating_frequency = first_repeat(data)

    print(f"{frequency} {repeating_frequency}")