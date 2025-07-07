import sys

def part1(data):
    vowels = set("aeiou")
    forbidden = {"ab", "cd", "pq", "xy"}
    count = 0
    
    for i in data:
        vowel_count = sum(1 for c in i if c in vowels)
        has_double = any(c == d for c, d in zip(i, i[1:]))
        has_forbidden = any(c + d in forbidden for c, d in zip(i, i[1:]))
        
        if vowel_count > 2 and has_double and not has_forbidden:
            count += 1
            
    return count

def part2(data):
    count = 0
    
    for i in data:
        pairs = {i[j:j+2] for j in range(len(i) - 1)}
        has_pair = any(i.count(pair) > 1 for pair in pairs)
        has_repeat = any(c == i[j+2] for j, c in enumerate(i[:-2]))
        
        if has_pair and has_repeat:
            count += 1
            
    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")