import sys

def redistribute(banks):
    seen = {}
    length = len(banks)
    banks_tuple = tuple(banks)

    while banks_tuple not in seen:
        seen[banks_tuple] = len(seen)
        max_value = max(banks_tuple)
        max_index = banks_tuple.index(max_value)
        new_banks = list(banks_tuple)
        new_banks[max_index] = 0

        for i in range(1, max_value + 1):
            new_banks[(max_index + i) % length] += 1

        banks_tuple = tuple(new_banks)

    loop_start = seen[banks_tuple]
    return len(seen), len(seen) - loop_start

input_strings = sys.argv[1]
with open(input_strings) as f:
    banks = list(map(int, f.read().strip().split()))

part1, part2 = redistribute(banks)
print(part1)
print(part2)