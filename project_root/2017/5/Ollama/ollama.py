import sys

def step_by_step(instructions, second_part=False):
    i, steps = 0, 0
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
with open(sys.argv[1]) as f:
    instructions = [int(s.strip()) for s in f.readlines() if s.strip()]
print(step_by_step(instructions))
print(step_by_step(instructions, True))