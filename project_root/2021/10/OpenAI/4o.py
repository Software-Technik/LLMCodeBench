import sys

def part1(data):
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    match = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def checker(line):
        stack = []
        for char in line:
            if char in match:
                stack.append(char)
            elif stack and char != match[stack.pop()]:
                return score_map[char]
        return 0

    return sum(checker(line) for line in data)

def part2(data):
    match = {'(': ')', '[': ']', '{': '}', '<': '>'}
    score_weights = {'(': 1, '[': 2, '{': 3, '<': 4}

    def checker(line):
        stack = []
        for char in line:
            if char in match:
                stack.append(char)
            elif stack and char != match[stack.pop()]:
                return 0
        score = 0
        for char in reversed(stack):
            score = score * 5 + score_weights[char]
        return score

    scores = sorted(score for line in data if (score := checker(line)) > 0)
    return scores[len(scores) // 2]

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")