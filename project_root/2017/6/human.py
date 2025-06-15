import sys

def redistribute(banks):
    seen = []
    length = len(banks)

    while banks not in seen:
        seen.append(banks[:])
        max_value = max(banks)
        max_index = banks.index(max_value)
        banks[max_index] = 0

        for i in range(1, max_value + 1):
            banks[(max_index + i) % length] += 1

    loop_start = seen.index(banks)
    return len(seen), len(seen) - loop_start

# Lecture du fichier
input_strings = sys.argv[1]
with open(input_strings) as f:
    banks = list(map(int, f.read().strip().split()))

# Calcul des résultats
part1, part2 = redistribute(banks)
print(part1)
print(part2)