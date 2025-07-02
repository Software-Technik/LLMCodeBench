import sys
from statistics import median

def part1(data):
    def checker(line):
        stack = []
        for char in line:
            if char in '([{<':
                stack.append(char)
            elif char in ')':
                if stack.pop() != '(':
                    return 3
            elif char in ']':
                if stack.pop() != '[':
                    return 57
            elif char in '}':
                if stack.pop() != '{':
                    return 1197
            elif char in '>':
                if stack.pop() != '<':
                    return 25137
        return 0

    return sum(checker(line) for line in data) # 299793

def part2(data):
    def checker(line):
        stack = []
        for char in line:
            if char in '([{<':
                stack.append(char)
            elif char in ')':
                if stack.pop() != '(':
                    return 0
            elif char in ']':
                if stack.pop() != '[':
                    return 0
            elif char in '}':
                if stack.pop() != '{':
                    return 0
            elif char in '>':
                if stack.pop() != '<':
                    return 0
        score = 0
        d = {'(': 1, '[': 2, '{': 3, '<': 4}
        for char in stack[::-1]:
            score *= 5
            score += d[char]
        return score

    scores = [checker(line) for line in data]
    return median([x for x in scores if x != 0])    # 3654963618

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")