import sys

with open(sys.argv[1]) as f:
    stream = f.read().strip()

garbage_cleaned = 0
nesting_level = 0
score = 0
i = 0
length = len(stream)

while i < length:
    c = stream[i]
    if c == '<':
        i += 1
        while i < length and stream[i] != '>':
            if stream[i] == '!':
                i += 2
            else:
                garbage_cleaned += 1
                i += 1
    elif c == '{':
        nesting_level += 1
        i += 1
    elif c == '}':
        score += nesting_level
        nesting_level -= 1
        i += 1
    else:
        i += 1

print(score)
print(garbage_cleaned)