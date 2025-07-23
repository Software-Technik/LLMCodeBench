import sys
from statistics import median

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

closers = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
d_score = {'(': 1, '[': 2, '{': 3, '<': 4}

corrupted_total = 0
incomplete_scores = []

for line in data:
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if c in closers:
                exp, score_val = closers[c]
                if not stack or stack.pop() != exp:
                    corrupted_total += score_val
                    break
    else:
        score = 0
        for c in reversed(stack):
            score = score * 5 + d_score[c]
        incomplete_scores.append(score)

part2 = median(incomplete_scores)

sys.stdout.write(f"{corrupted_total} {part2}")