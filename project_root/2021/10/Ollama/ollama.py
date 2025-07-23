import sys
from statistics import median

def part1(data):
    def checker(line, costs={')': 3, ']': 57, '}': 1197, '>': 25137}):
        stack = []
        for char in line:
            if char in '([{<':
                stack.append(char)
            elif not stack or costs.get(stack.pop(), 0) != char:
                return costs[char]
        return 0
    return sum(checker(line) for line in data)

def part2(data):
    def checker(line, costs={')': 1, ']': 2, '{': 3, '>': 4}, comp={'(': ')', '[': ']', '<': '>', '{': '}'}):
        stack = []
        for char in line:
            if char in '([{<':
                stack.append(char)
            elif not stack or comp[stack.pop()] != char:
                return 0
        score, d = 0, costs
        for char in [comp[c] for c in reversed(stack)]:
            score *= 5
            score += d.get(char)
        return score

    scores = (checker(line) for line in data if checker(line))
    return median(scores)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)} {part2(data)}")