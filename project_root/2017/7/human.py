import sys
import re
from collections import defaultdict, Counter

# Lire le fichier d'entrée
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
        continue  # Ignorer les lignes vides

    words = pattern.findall(line)
    if len(words) < 2:
        continue  # Ignorer les lignes mal formées

    name = words[0]
    weight = int(words[1])
    kids = words[2:] if len(words) > 2 else []

    weights[name] = weight
    children[name] = kids
    all_nodes.add(name)
    all_kids.update(kids)

# Trouver la racine
root = list(all_nodes - all_kids)[0]
print(root)

def find_correct_weight(weights_list):
    count = Counter(weights_list)
    return count.most_common(1)[0][0]

def find_offsprings_weights(node):
    kids_weights = [find_offsprings_weights(kid) for kid in children[node]]

    if len(set(kids_weights)) > 1:
        correct = find_correct_weight(kids_weights)
        for weight in set(kids_weights):
            if weight != correct:
                wrong = weight
        difference = correct - wrong
        wrong_index = kids_weights.index(wrong)
        wrong_node = children[node][wrong_index]
        wrong_weight = weights[wrong_node]
        print(wrong_weight + difference)
        # On continue malgré l'erreur pour retourner un poids global cohérent
        return weights[node] + sum(kids_weights) + difference

    return weights[node] + sum(kids_weights)

# Déclenche la détection de déséquilibre
find_offsprings_weights(root)

# Partie 2 : trouver le poids incorrect
def find_correct_weight(weight_list):
    count = Counter(weight_list)
    return count.most_common(1)[0][0]

def find_offsprings_weights(node):
    kids_weights = [find_offsprings_weights(kid) for kid in children[node]]

    if len(set(kids_weights)) > 1:
        correct = find_correct_weight(kids_weights)
        for w in set(kids_weights):
            if w != correct:
                wrong = w
        difference = correct - wrong
        wrong_node = children[node][kids_weights.index(wrong)]
        wrong_weight = weights[wrong_node]
        print(wrong_weight + difference)
        return weights[node] + sum(kids_weights) + difference

    return weights[node] + sum(kids_weights)

# Appel à la fonction
find_offsprings_weights(root)