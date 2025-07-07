import sys

def step_by_step(instructions, second_part=False):
    instructions = list(instructions)
    i = 0
    steps = 0

    while 0 <= i < len(instructions):
        jump = instructions[i]
        instructions[i] += -1 if second_part and jump >= 3 else 1
        i += jump
        steps += 1

    return steps

input_strings = sys.argv[1]
with open(input_strings) as f:
    instructions = tuple(int(line.strip()) for line in f if line.strip())

print(step_by_step(instructions))
print(step_by_step(instructions, second_part=True))