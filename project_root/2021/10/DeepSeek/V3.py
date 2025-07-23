import sys
from statistics import median

def part1(data):
    def checker(line):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
        scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        for char in line:
            if char in '([{<':
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return scores[char]
        return 0
    return sum(checker(line) for line in data)

def part2(data):
    def checker(line):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
        for char in line:
            if char in '([{<':
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return 0
        score = 0
        d = {'(': 1, '[': 2, '{': 3, '<': 4}
        for char in reversed(stack):
            score = score * 5 + d[char]
        return score

    scores = [checker(line) for line in data]
    return median([x for x in scores if x != 0])

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")