import sys

with open(sys.argv[1]) as f:
    stream = f.read().strip()

score, garbage, nesting, in_garbage = 0, 0, 0, False
i = 0

while i < len(stream):
    if in_garbage:
        if stream[i] == '!':
            i += 1
        elif stream[i] == '>':
            in_garbage = False
        else:
            garbage += 1
    else:
        if stream[i] == '<':
            in_garbage = True
        elif stream[i] == '{':
            nesting += 1
            score += nesting
        elif stream[i] == '}':
            nesting -= 1
    i += 1

print(score)
print(garbage)