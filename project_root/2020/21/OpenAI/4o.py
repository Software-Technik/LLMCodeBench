import sys
from itertools import chain, combinations

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    data, lines = "", []

def line_transform(line):
    left, right = line.split(" (contains ")
    right = right[:-1]
    return left.split(" "), right.split(", ")

lines = [line_transform(line) for line in lines]

english_words = set()
candidates = dict()

l_sets = []
r_sets = []

for line in lines:
    gibberish, english = line
    for e in english:
        english_words.add(e)
    l_sets.append(set(gibberish))
    r_sets.append(set(english))

for english_word in english_words:
    possible_translations = []
    for l, r in zip(l_sets, r_sets):
        if english_word in r:
            possible_translations.append(l)
    intersect = set.intersection(*possible_translations)
    candidates[english_word] = intersect

done = False
discarded = set()
while not done:
    for english_word, gset in candidates.items():
        if len(gset) == 1 and english_word not in discarded:
            for kinner in candidates:
                if kinner != english_word:
                    candidates[kinner] -= gset
            discarded.add(english_word)
            break
    if all(len(s) == 1 for s in candidates.values()):
        done = True

dangerous_gibberish = set().union(*candidates.values())

tot = sum(1 for left, _ in lines for gib in left if gib not in dangerous_gibberish)

s = ",".join(candidates[e].pop() for e in sorted(english_words))

result1 = tot
result2 = s
print(result1, result2)