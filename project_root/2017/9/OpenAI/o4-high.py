import sys
with open(sys.argv[1]) as f:
    d = f.read()
score = garbage = depth = 0
in_garbage = skip = False
for c in d:
    if skip:
        skip = False
    elif in_garbage:
        if c == '!':
            skip = True
        elif c == '>':
            in_garbage = False
        else:
            garbage += 1
    else:
        if c == '<':
            in_garbage = True
        elif c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
print(score)
print(garbage)