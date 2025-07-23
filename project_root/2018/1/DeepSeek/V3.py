import sys

def get_frequency(data, start: int = 0) -> int:
    return start + sum(int(item) for item in data)

def first_repeat(data, start: int = 0) -> int:
    seen = {start: True}
    frequency = start
    while True:
        for modulation in data:
            frequency += int(modulation)
            if frequency in seen:
                return frequency
            seen[frequency] = True

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data_lines = f.read().strip().splitlines()
    frequency = get_frequency(data_lines)
    repeating_frequency = first_repeat(data_lines)
    sys.stdout.write(f"{frequency} {repeating_frequency}")