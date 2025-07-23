import sys

def part1(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0
    for x in range(lower, upper + 1):
        s = str(x)
        increasing = True
        has_dup = False
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                increasing = False
                break
            if s[i] == s[i-1]:
                has_dup = True
        if increasing and has_dup:
            n += 1
    return n

def part2(data):
    lower, upper = map(int, data[0].split("-"))
    n = 0
    for x in range(lower, upper + 1):
        s = str(x)
        increasing = True
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                increasing = False
                break
        if not increasing:
            continue
        has_exactly_two = False
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                left_ok = (i - 2 < 0) or (s[i-2] != s[i])
                right_ok = (i + 1 >= len(s)) or (s[i+1] != s[i])
                if left_ok and right_ok:
                    has_exactly_two = True
                    break
        if has_exactly_two:
            n += 1
    return n

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")