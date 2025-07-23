import sys

def part1(elves):
    if len(elves) <= 2:
        return elves[0] + 1

    if len(elves) % 2:
        return part1([elves[i] for i in range(0, len(elves)-2, 3)])
    else:
        return part1([elves[i] for i in range(0, len(elves), 2)])

def part2(elves):
    n = len(elves)
    if n <= 2:
        return elves[0] + 1

    across = n // 2
    removed = (n - across) % 3
    if n % 2 == 0:
        new = [elves[i] for i in range(across, len(elves), 3)]
    else:
        new = [elves[i] for i in range(1 + across, len(elves), 3)]

    return part2(new)

inout_strings = sys.argv[1]
with open(inout_strings) as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(list(range(data)))} {part2(list(range(data)))}")