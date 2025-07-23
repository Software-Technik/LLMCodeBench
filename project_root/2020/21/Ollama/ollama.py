import os
import sys
from itertools import chain, combinations

input_path = sys.argv[1]

try:
    with open(input_file) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

def line_transform(line):
    left, right = line.split(" (contains ")
    return set(left.split()), set(right[:-1].split(", "))

gibberish_sets = []
english_words = set()

for line in lines:
    gibberish, english = line_transform(line)
    for word in english:
        english_words.add(word)
    gibberish_sets.append((gibberish, english))

candidates = {word: set(chain.from_iterable(gibberish_sets)) for word in english_words}

for word1 in english_words:
    for word2 in candidates[word1]:
        if not any(word1 in english and word2 in gibberish for gibberish, english in gibberish_sets):
            candidates[word1].remove(word2)

def refine_candidates():
    done = set()
    while any(len(candidates[w]) > 1 for w in candidates if w not in done):
        for word in sorted(candidates, key=lambda x: len(candidates[x])):
            g_set = candidates[word]
            if len(g_set) == 1 and word not in done:
                for cand_word in candidates:
                    if cand_word != word:
                        candidates[cand_word].discard(*g_set)
                done.add(word)

refine_candidates()
dangerous_ingredients = set(chain.from_iterable(candidates.values()))
result1 = sum(sum(gib not in dangerous_ingredients for gib in left) for left, _ in gibberish_sets)
result2 = ",".join(sorted(map(str.swapcase, candidates)))
print(result1, result2)