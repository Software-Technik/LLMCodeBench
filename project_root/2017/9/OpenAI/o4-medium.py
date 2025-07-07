import sys
with open(sys.argv[1]) as f:
    data = f.read()
it = iter(data)
score = garbage = level = 0
in_garbage = False
for c in it:
    if in_garbage:
        if c == '!':
            next(it, None)
        elif c == '>':
            in_garbage = False
        else:
            garbage += 1
    else:
        if c == '<':
            in_garbage = True
        elif c == '{':
            level += 1
        elif c == '}':
            score += level
            level -= 1
print(score)
print(garbage)