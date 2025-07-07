import sys
from collections import Counter

def compute_solutions(data):
    first_solution = []
    second_solution = []

    for column in zip(*data):
        common = Counter(column).most_common()
        most, least = common[0][0], common[-1][0]
        first_solution.append(most)
        second_solution.append(least)

    return ''.join(first_solution), ''.join(second_solution)

def main(filename):
    with open(filename, 'r') as infile:
        data = infile.read().splitlines()

    part1_result, part2_result = compute_solutions(data)
    sys.stdout.write(f"{part1_result} {part2_result}")

if __name__ == "__main__":
    input_file = sys.argv[1]
    main(input_file)