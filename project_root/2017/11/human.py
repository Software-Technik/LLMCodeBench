import sys

# Conversion des directions en coordonnées axiales (p, q)
def to_axial(direction):
    return {
        "n":  (0, -1),
        "nw": (-1, 0),
        "sw": (-1, 1),
        "s":  (0, 1),
        "se": (1, 0),
        "ne": (1, -1)
    }[direction]

# Addition de points
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

# Distance à l'origine dans un système axial (hex grid)
def distance_to_origin(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))

# Lecture du fichier d'entrée
input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = f.read().strip().split(",")

position = (0, 0)
distances = []

for direction in instructions:
    position = add(position, to_axial(direction))
    distances.append(distance_to_origin(position))

# Partie 1 : distance finale
print(distance_to_origin(position))
# Partie 2 : distance maximale atteinte
print(max(distances))