import sys

def part1(data):
    count = 0
    forbidden = {"ab", "cd", "pq", "xy"}
    for s in data:
        vowels = 0
        for c in s:
            if c in "aeiou":
                vowels += 1
                if vowels >= 3:
                    break
        if vowels < 3:
            continue
            
        found_double = False
        found_forbidden = False
        for i in range(len(s)-1):
            pair = s[i:i+2]
            if pair in forbidden:
                found_forbidden = True
                break
            if s[i] == s[i+1]:
                found_double = True
                
        if not found_double or found_forbidden:
            continue
            
        count += 1
    return count

def part2(data):
    count = 0
    for s in data:
        first_occurrence = {}
        cond1 = False
        for i in range(len(s)-1):
            pair = s[i:i+2]
            if pair in first_occurrence:
                if i - first_occurrence[pair] >= 2:
                    cond1 = True
                    break
            else:
                first_occurrence[pair] = i
                
        if not cond1:
            continue
            
        cond2 = False
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                cond2 = True
                break
                
        if cond2:
            count += 1
            
    return count

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")