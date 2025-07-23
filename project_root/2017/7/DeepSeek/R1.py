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
    kids = words[2:] if len(words) > 2 else []

    weights[name] = weight
    children[name] = kids
    all_nodes.add(name)
    all_kids.update(kids)

root = list(all_nodes - all_kids)[0]
print(root)

def find_offsprings_weights(node):
    if not children[node]:
        return weights[node]
    
    kids_weights = []
    total_kids = 0
    for kid in children[node]:
        w = find_offsprings_weights(kid)
        kids_weights.append(w)
        total_kids += w
        
    total_base = weights[node] + total_kids

    all_same = True
    first = kids_weights[0]
    for w in kids_weights[1:]:
        if w != first:
            all_same = False
            break

    if all_same:
        return total_base
    else:
        count = Counter(kids_weights)
        correct = count.most_common(1)[0][0]
        for i, w in enumerate(kids_weights):
            if w != correct:
                wrong_index = i
                wrong = w
                break
        difference = correct - wrong
        wrong_node = children[node][wrong_index]
        wrong_weight = weights[wrong_node]
        print(wrong_weight + difference)
        return total_base + difference

find_offsprings_weights(root)