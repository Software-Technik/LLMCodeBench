import sys

def get_frequency(data, start: int = 0) -> int:
    return start + sum(data)

def first_repeat(data, start: int = 0) -> int:
    seen = set()
    current = start
    seen.add(current)
    n = len(data)
    index = 0
    while True:
        current += data[index]
        if current in seen:
            return current
        seen.add(current)
        index = (index + 1) % n

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()
    data_lines = data.strip().splitlines()
    mods = [int(x) for x in data_lines]
    frequency = get_frequency(mods)
    repeating_frequency = first_repeat(mods)
    sys.stdout.write(f"{frequency} {repeating_frequency}")