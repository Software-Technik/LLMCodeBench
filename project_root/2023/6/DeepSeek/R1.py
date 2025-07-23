import sys

def count_wins(time, distance):
    lo = 1
    hi = time // 2
    first_win = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * (time - mid) > distance:
            first_win = mid
            hi = mid - 1
        else:
            lo = mid + 1
    if first_win is None:
        return 0
    return time - 2 * first_win + 1

def part1(text: str) -> int:
    lines = text.splitlines()
    times = list(map(int, lines[0].split(":", maxsplit=1)[1].split()))
    distances = list(map(int, lines[1].split(":", maxsplit=1)[1].split()))
    total = 1
    for i in range(len(times)):
        total *= count_wins(times[i], distances[i])
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    time = int("".join(lines[0].split(":", maxsplit=1)[1].split()))
    distance = int("".join(lines[1].split(":", maxsplit=1)[1].split()))
    return count_wins(time, distance)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")