import sys

def is_valid(line):
    return len(set(line.split())) == len(line)

# Lecture du fichier passé en argument
with open(sys.argv[1]) as f:
    passphrases = [line.strip() for line in f]

first = second = 0

for phrase in passphrases:
    words, anagrams = map(sorted, (phrase.split(), ' '.join(phrase.split()).replace(' ', '')))
    first += len(set(words)) == len(words)
    second += len(set(anagrams)) == len(anagrams)

print(first, second)