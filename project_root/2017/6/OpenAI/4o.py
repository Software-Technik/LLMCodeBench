import sys

def redistribute(banks):
    seen = set()
    length = len(banks)

    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        max_value = max(banks)
        max_index = banks.index(max_value)
        banks[max_index] = 0

        for i in range(max_value):
            banks[(max_index + 1 + i) % length] += 1

    loop_start = len(seen)
    return loop_start, len(seen) - loop_start + 1

# Lecture du fichier
input_strings = sys.argv[1]
with open(input_strings) as f:
    banks = list(map(int, f.read().strip().split()))

# Calcul des résultats
part1, part2 = redistribute(banks)
print(part1)
print(part2)