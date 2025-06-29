import sys
from collections import Counter

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    noise = infile.readlines()

columns = (''.join(column) for column in zip(*noise))

first_solution = ''
second_solution = ''

for column in columns:
    (most, _), *others, (least, _) = Counter(column).most_common()
    first_solution += most
    second_solution += least

print(first_solution, second_solution)