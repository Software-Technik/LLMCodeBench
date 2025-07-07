import sys

def get_frequency(data, start: int = 0) -> int:
    return start + sum(map(int, data))

def first_repeat(data, start: int = 0) -> int:
    seen = {start}
    frequency = start
    while True:
        for modulation in data:
            frequency += int(modulation)
            if frequency in seen:
                return frequency
            seen.add(frequency)

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data_lines = f.read().strip().splitlines()

    frequency = get_frequency(data_lines)
    repeating_frequency = first_repeat(data_lines)

    sys.stdout.write(f"{frequency} {repeating_frequency}")