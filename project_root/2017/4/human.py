import sys

def are_only_distinct(words):
    return len(words) == len(set(words))

def letter_sort(word):
    return ''.join(sorted(word))

# Lecture du fichier passé en argument
input_strings = sys.argv[1]
with open(input_strings) as f:
    passphrases = [line.strip() for line in f]

first = 0
second = 0

for line in passphrases:
    words = line.split()
    anagrams = [letter_sort(word) for word in words]
    if are_only_distinct(words):
        first += 1
    if are_only_distinct(anagrams):
        second += 1

print(first)
print(second)