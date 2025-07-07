import sys

def are_only_distinct(words):
    seen = set()
    for word in words:
        if word in seen:
            return False
        seen.add(word)
    return True

def letter_sort(word):
    return ''.join(sorted(word))

input_strings = sys.argv[1]
with open(input_strings) as f:
    passphrases = f.read().splitlines()

first = 0
second = 0

for line in passphrases:
    words = line.split()
    if are_only_distinct(words):
        first += 1
    if are_only_distinct([letter_sort(word) for word in words]):
        second += 1

print(first)
print(second)