import sys

def part1(data):
    count = 0
    vowels = set("aeiou")
    forbidden = {"ab","cd","pq","xy"}
    for s in data:
        v = 0
        has_double = False
        bad = False
        for i in range(len(s)-1):
            c, d = s[i], s[i+1]
            if c in vowels: v += 1
            if c == d: has_double = True
            if c+d in forbidden:
                bad = True
                break
        if bad: continue
        if s and s[-1] in vowels: v += 1
        if v > 2 and has_double:
            count += 1
    return count

def part2(data):
    count = 0
    for s in data:
        pairs = {}
        has_pair = False
        has_repeat = False
        for i in range(len(s)):
            if i+2 < len(s) and s[i] == s[i+2]:
                has_repeat = True
            if i+1 < len(s):
                p = s[i:i+2]
                if p in pairs and i - pairs[p] > 1:
                    has_pair = True
                else:
                    pairs[p] = i
            if has_pair and has_repeat:
                count += 1
                break
    return count

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]
print(part1(data))
print(part2(data))