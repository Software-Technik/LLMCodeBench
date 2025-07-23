import sys

total1 = 0
total2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        parts = line.strip().split()
        if not parts:
            continue
        range_str, char_str, pwd = parts[0], parts[1], parts[2]
        low, high = map(int, range_str.split('-'))
        char = char_str[0]
        
        cnt = pwd.count(char)
        if low <= cnt <= high:
            total1 += 1
        
        idx1 = low - 1
        idx2 = high - 1
        matches = 0
        n = len(pwd)
        if idx1 < n and pwd[idx1] == char:
            matches += 1
        if idx2 < n and pwd[idx2] == char:
            matches += 1
        if matches == 1:
            total2 += 1

print(total1, total2)