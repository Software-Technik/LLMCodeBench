import sys
import re
from collections import defaultdict, Counter

input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [line.strip() for line in f]

pattern = re.compile(r"\w+")

weights = {}
children = defaultdict(list)
all_nodes = set()
all_kids = set()

for line in instructions:
    if not line.strip():
        continue

    words = pattern.findall(line)
    if len(words) < 2:
        continue

    name = words[0]
    weight = int(words[1])
    kids = words[2:]

    weights[name] = weight
    children[name] = kids
    all_nodes.add(name)
    all_kids.update(kids)

root = next(iter(all_nodes - all_kids))
print(root)

def find_offsprings_weights(node):
    kids_weights = [find_offsprings_weights(kid) for kid in children[node]]

    if len(set(kids_weights)) > 1:
        count = Counter(kids_weights)
        correct = count.most_common(1)[0][0]
        wrong = next(w for w in kids_weights if w != correct)
        difference = correct - wrong
        wrong_node = children[node][kids_weights.index(wrong)]
        wrong_weight = weights[wrong_node]
        print(wrong_weight + difference)
        return weights[node] + sum(kids_weights) + difference

    return weights[node] + sum(kids_weights)

find_offsprings_weights(root)