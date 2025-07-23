import sys
import re
from collections import Counter, defaultdict

input_strings = sys.argv[1]
instructions = [line.strip() for line in open(input_strings)]

pattern = re.compile(r"\w+")
weights = {}
children = defaultdict(list)
all_nodes = set()
all_kids = set()

for line in instructions:
    if not line or len(words := pattern.findall(line)) < 2: continue
    name, weight, *kids = words[:3]
    weights[name] = int(weight)
    children[name], kids, all_kids.update(kids), all_nodes.add(name)

root = (all_nodes - all_kids).pop()

def find_offsprings_weights(node):
    kids_weights = [find_offsprings_weights(kid) for kid in children[node]]
    correct = Counter(kids_weights).most_common(1)[0][0]
    unique_weights = list(set(kids_weights))

    if len(s := set(kids_weights)) > 1:
        wrong = next(w for w in unique_weights if w != correct)
        difference, node_weight = kids_weights.index(wrong), int(weights[children[node][kids_weights.index(wrong)]])
        print(node_weight + (correct - wrong))
    return weights[node] + sum(kids_weights)

print(root)
find_offsprings_weights