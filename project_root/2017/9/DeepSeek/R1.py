import sys

with open(sys.argv[1]) as f:
    stream = f.read().strip()

in_garbage = False
skip_next = False
nesting_level = 0
score = 0
garbage_cleaned = 0

for char in stream:
    if skip_next:
        skip_next = False
        continue
        
    if in_garbage:
        if char == '!':
            skip_next = True
        elif char == '>':
            in_garbage = False
        else:
            garbage_cleaned += 1
    else:
        if char == '<':
            in_garbage = True
        elif char == '{':
            nesting_level += 1
        elif char == '}':
            score += nesting_level
            nesting_level -= 1

print(score)
print(garbage_cleaned)