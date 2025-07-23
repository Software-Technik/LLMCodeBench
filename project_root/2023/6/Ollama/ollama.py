import sys
from math import ceil, sqrt

def part1(text: str) -> int:
    lines = text.splitlines()
    times = list(map(int, lines[0].split(":", 1)[1].split()))
    distances = list(map(int, lines[1].split(":", 1)[1].split()))

    total = 1
    for time, distance in zip(times, distances):
        x2 = ceil((time - sqrt(time**2 - 4 * distance)) / 2)
        if (x2 * (time - x2)) <= distance:
            x2 += 1

        max_peak = (time - 1) // 2 + time % 2
        total *= max_peak - x2 + 1
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    time = int("".join(lines[0].split(":", 1)[1].replace(" ", "")))
    distance = int("".join(lines[1].split(":", 1)[1].replace(" ", "")))

    x2 = ceil((time - sqrt(time**2 - 4 * distance)) / 2)
    if (x2 * (time - x2)) <= distance:
        x2 += 1

    max_peak = (time - 1) // 2 + time % 2
    return max(max_peak, x2)

with open(sys.argv[1]) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")