import sys

def part1(data):
    result = filter(
        lambda s: sum(c in 'aeiou' for c in s) > 2 and any(s[i] == s[i + 1] for i in range(len(s) - 1)) and not any(s[i:i + 2] in ('ab', 'cd', 'pq', 'xy') for i in range(len(s) - 1)),
        data
    )
    return sum(1 for _ in result)

def part2(data):
    def double_pair(s):
        for i in range(len(s) - 1):
            if s[i:i + 2] in s[i + 2:]:
                return True
        return False

    def same_at_intervals(s):
        for i, c in enumerate(s[:-2]):
            if c == s[i + 2]:
                return True
        return False

    result = filter(lambda s: double_pair(s) and same_at_intervals(s), data)
    return sum(1 for _ in result)

input_strings = sys.argv[1]
with open(input_strings, 'r') as f:
    data = [line.strip() for line in f]

print(f"{part1(data)}\n{part2(data)}")