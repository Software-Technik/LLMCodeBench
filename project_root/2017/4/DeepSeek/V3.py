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

with open(sys.argv[1]) as f:
    passphrases = [line.strip() for line in f]

first = 0
second = 0

for line in passphrases:
    words = line.split()
    if are_only_distinct(words):
        first += 1
    anagrams = [letter_sort(word) for word in words]
    if are_only_distinct(anagrams):
        second += 1

print(first)
print(second)