import sys

input_path = sys.argv[1]

with open(input_path) as f:
    lines = [line.strip() for line in f]

split = [line.split() for line in lines]

valid_count1 = 0
valid_count2 = 0

for entry in split:
    low, high = map(int, entry[0].split('-'))
    char = entry[1][0]
    password = entry[2]
    
    # Part 1
    count = password.count(char)
    if low <= count <= high:
        valid_count1 += 1
    
    # Part 2
    pos1 = low - 1
    pos2 = high - 1
    matches = 0
    if pos1 < len(password) and password[pos1] == char:
        matches += 1
    if pos2 < len(password) and password[pos2] == char:
        matches += 1
    if matches == 1:
        valid_count2 += 1

print(valid_count1, valid_count2)