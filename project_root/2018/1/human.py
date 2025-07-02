import itertools
import sys


def get_frequency(data, start: int = 0) -> int:
    """Takes frequency modulation file and returns final frequency"""
    return start + sum(int(item) for item in data)


def first_repeat(data, start: int = 0) -> int:
    """Finds the first repeating frequency when cycling the modulation file

    Note: Updating a dict item-by-item seems faster than set; using dummy dict
    """
    seen = {start: 0}
    frequency = start
    for modulation in itertools.cycle(data):
        frequency += int(modulation)
        if frequency in seen:
            return frequency

        seen[frequency] = 0




if __name__ == "__main__":

    
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()

    data_lines = data.strip().splitlines()

    frequency = get_frequency(data_lines)

    repeating_frequency = first_repeat(data_lines)

    sys.stdout.write(f"{frequency} {repeating_frequency}") 
