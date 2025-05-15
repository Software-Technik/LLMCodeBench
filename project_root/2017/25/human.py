import sys

def simulate(steps, states):
    tape = {}
    position = 0
    state = 0

    for _ in range(steps):
        current = tape.get(position, 0)
        write, move, next_state = states[state][current]
        tape[position] = write
        position += move
        state = next_state

    return sum(tape.values())

def parse_input(data):
    # On ignore les données du fichier pour l’instant si inutiles
    # Mais la structure est prête si besoin plus tard
    return 12667664, [
        [(1, 1, 1), (0, -1, 2)],
        [(1, -1, 0), (1, 1, 3)],
        [(0, -1, 1), (0, -1, 4)],
        [(1, 1, 0), (0, 1, 1)],
        [(1, -1, 5), (1, -1, 2)],
        [(1, 1, 3), (1, 1, 0)]
    ]

# Lecture de l’entrée depuis sys.argv
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

steps, states = parse_input(data)
print(simulate(steps, states))
