import sys
import math

def part1(text: str) -> int:
    lines = text.splitlines()
    times = list(map(int, lines[0].split(":", 1)[1].split()))
    distances = list(map(int, lines[1].split(":", 1)[1].split()))

    total = 1
    for time, distance in zip(times, distances):
        i = math.ceil((time - math.sqrt(time**2 - 4 * distance)) / 2)
        if (i * (time - i)) <= distance:
            i += 1

        max_peak = (time - 1) // 2
        if time % 2 == 0:
            max_peak += 1
        if i < max_peak:
            subtotal = (max_peak - i) * 2 + 1 if time % 2 == 0 else (max_peak - i + 1) * 2
            total *= subtotal
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    time = int("".join(lines[0].split(":", 1)[1].split()))
    distance = int("".join(lines[1].split(":", 1)[1].split()))

    i = math.ceil((time - math.sqrt(time**2 - 4 * distance)) / 2)
    if (i * (time - i)) <= distance:
        i += 1

    max_peak = (time - 1) // 2
    if time % 2 == 0:
        max_peak += 1
    if i < max_peak:
        return (max_peak - i) * 2 + 1 if time % 2 == 0 else (max_peak - i + 1) * 2
    return 0

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        text = f.read()
    sys.stdout.write(f"{part1(text)} {part2(text)}")