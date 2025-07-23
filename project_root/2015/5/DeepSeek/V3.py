import sys

def part1(data):
    count = 0
    for s in data:
        vowels = sum(s.count(v) for v in 'aeiou')
        if vowels <= 2:
            continue
        has_double = any(c1 == c2 for c1, c2 in zip(s, s[1:]))
        if not has_double:
            continue
        has_forbidden = any(f in s for f in ['ab', 'cd', 'pq', 'xy'])
        if has_forbidden:
            continue
        count += 1
    return count

def part2(data):
    count = 0
    for s in data:
        has_pair = False
        pairs = {}
        for i in range(len(s) - 1):
            pair = s[i:i+2]
            if pair in pairs:
                if pairs[pair] < i - 1:
                    has_pair = True
                    break
            else:
                pairs[pair] = i
        if not has_pair:
            continue
        has_repeat = any(s[i] == s[i+2] for i in range(len(s) - 2))
        if not has_repeat:
            continue
        count += 1
    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")