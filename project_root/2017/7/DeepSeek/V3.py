import sys
import re
from collections import defaultdict, Counter

with open(sys.argv[1]) as f:
    instructions = [line.strip() for line in f if line.strip()]

pattern = re.compile(r"\w+")

weights = {}
children = defaultdict(list)
all_nodes = set()
all_kids = set()

for line in instructions:
    words = pattern.findall(line)
    if len(words) < 2:
        continue
    name = words[0]
    weight = int(words[1])
    kids = words[2:] if len(words) > 2 else []
    weights[name] = weight
    children[name] = kids
    all_nodes.add(name)
    all_kids.update(kids)

root = next(iter(all_nodes - all_kids))
print(root)

def find_correct_weight(weight_list):
    count = Counter(weight_list)
    return count.most_common(1)[0][0]

def find_offsprings_weights(node):
    kids_weights = []
    for kid in children[node]:
        kid_weight = find_offsprings_weights(kid)
        kids_weights.append(kid_weight)
    
    if kids_weights:
        if len(set(kids_weights)) > 1:
            correct = find_correct_weight(kids_weights)
            wrong = next(w for w in kids_weights if w != correct)
            difference = correct - wrong
            wrong_node = children[node][kids_weights.index(wrong)]
            wrong_weight = weights[wrong_node]
            print(wrong_weight + difference)
            return weights[node] + sum(kids_weights) + difference
    
    return weights[node] + (sum(kids_weights) if kids_weights else 0)

find_offsprings_weights(root)