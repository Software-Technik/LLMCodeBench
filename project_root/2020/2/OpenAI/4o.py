import sys

input_path = sys.argv[1]

with open(input_path) as f:
    lines = [line.strip().split() for line in f.readlines()]

valid_count1 = 0
valid_count2 = 0

for entry in lines:
    start, end = map(int, entry[0].split("-"))
    char = entry[1][0]
    password = entry[2]

    # Part 1
    if start <= password.count(char) <= end:
        valid_count1 += 1

    # Part 2
    idx1, idx2 = start - 1, end - 1
    first_match = password[idx1] == char if idx1 < len(password) else False
    second_match = password[idx2] == char if idx2 < len(password) else False

    if first_match ^ second_match:
        valid_count2 += 1

print(valid_count1, valid_count2)