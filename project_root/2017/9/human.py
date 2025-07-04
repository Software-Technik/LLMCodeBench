import sys

# Lecture du fichier d'entrée
input_strings = sys.argv[1]
with open(input_strings) as f:
    stream = f.read().strip()

# Initialisation des compteurs
garbage_cleaned = 0
nesting_level = 0
score = 0
i = 0

# Analyse du flux caractère par caractère
while i < len(stream):
    if stream[i] == '<':
        i += 1
        while stream[i] != '>':
            if stream[i] == '!':
                i += 2  # Skip the next character
            else:
                garbage_cleaned += 1
                i += 1
    elif stream[i] == '{':
        nesting_level += 1
    elif stream[i] == '}':
        score += nesting_level
        nesting_level -= 1
    i += 1

# Affichage des résultats
print(score)
print(garbage_cleaned)