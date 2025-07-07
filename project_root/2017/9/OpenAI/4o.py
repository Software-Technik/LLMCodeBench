import sys

# Lecture du fichier d'entrée
input_strings = sys.argv[1]
with open(input_strings) as f:
    stream = f.read().strip()

# Initialisation des variables
garbage_cleaned = 0
score = 0
nesting_level = 0
i = 0
length = len(stream)

# Analyse du flux caractère par caractère
while i < length:
    c = stream[i]
    if c == '<':
        i += 1
        while stream[i] != '>':
            if stream[i] == '!':
                i += 1  # Skip the next character more efficiently
            else:
                garbage_cleaned += 1
            i += 1
    elif c == '{':
        nesting_level += 1
    elif c == '}':
        score += nesting_level
        nesting_level -= 1
    i += 1

# Affichage des résultats
print(score)
print(garbage_cleaned)