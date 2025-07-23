import sys

def redistribute(banks):
    seen = {}
    length = len(banks)
    steps = 0

    while tuple(banks) not in seen:
        seen[tuple(banks)] = steps
        max_value = max(banks)
        max_index = banks.index(max_value)
        banks[max_index] = 0

        for i in range(1, max_value + 1):
            banks[(max_index + i) % length] += 1

        steps += 1

    return steps, steps - seen[tuple(banks)]

# Lecture du fichier
input_strings = sys.argv[1]
with open(input_strings) as f:
    banks = list(map(int, f.read().strip().split()))

part1, part2 = redistribute(banks)
print(part1)