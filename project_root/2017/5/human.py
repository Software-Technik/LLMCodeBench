import sys

def step_by_step(instructions, second_part=False):
    instructions = instructions.copy()
    i = 0
    steps = 0

    while 0 <= i < len(instructions):
        jump = instructions[i]
        if second_part and jump >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += jump
        steps += 1

    return steps

# Lecture des données depuis le fichier
input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = [int(line.strip()) for line in f if line.strip()]

# Affichage des résultats
print(step_by_step(instructions))
print(step_by_step(instructions, second_part=True))