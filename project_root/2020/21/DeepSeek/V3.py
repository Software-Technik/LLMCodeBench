import sys
from itertools import chain, combinations

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
except:
    lines = []

def line_transform(line):
    left, right = line.split(" (contains ")
    right = right[:-1]
    return left.split(" "), right.split(", ")

lines = [line_transform(line) for line in lines]

english_words = set()
candidates = {}

l_sets = []
r_sets = []
for line in lines:
    gibberish, english = line
    english_words.update(english)
    l_sets.append(set(gibberish))
    r_sets.append(set(english))

for english_word in english_words:
    possible_translations = []
    for l, r in zip(l_sets, r_sets):
        if english_word in r:
            possible_translations.append(l)
    intersect = set.intersection(*possible_translations)
    candidates[english_word] = intersect

discarded = set()
while True:
    updated = False
    for english_word, gset in candidates.items():
        if len(gset) == 1 and english_word not in discarded:
            unique = next(iter(gset))
            for other_word in candidates:
                if other_word != english_word:
                    candidates[other_word].discard(unique)
            discarded.add(english_word)
            updated = True
            break
    if not updated:
        break

dangerous_gibberish = set()
for gset in candidates.values():
    dangerous_gibberish.update(gset)

tot = 0
for left, _ in lines:
    for gib in left:
        if gib not in dangerous_gibberish:
            tot += 1

sorted_english = sorted(candidates.keys())
result2 = ",".join([next(iter(candidates[e])) for e in sorted_english])

print(tot, result2)