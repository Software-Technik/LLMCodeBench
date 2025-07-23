import sys
from collections import Counter

def solve(data):
    transposed = zip(*data)
    most_list = []
    least_list = []
    for column in transposed:
        ctr = Counter(column)
        most_list.append(ctr.most_common(1)[0][0])
        least_list.append(ctr.most_common()[-1][0])
    return ''.join(most_list), ''.join(least_list)

input_file = sys.argv[1]
with open(input_file, 'r') as infile:
    data = [line.rstrip('\n') for line in infile]

part1, part2 = solve(data)
sys.stdout.write(f"{part1} {part2}")